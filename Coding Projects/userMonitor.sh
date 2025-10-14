#!/bin/bash
#Written By: Charles Steward
#Created On: 10/07/2025
#Last Updated: 10/07/2025

#Asks user for the username of the user they wish to monitor
echo "Enter the username of the user that you wish to monitor:"
read username

#Only displays info if the user could be found in the file /etc/passwd
if grep -q $username /etc/passwd; then
        #Displays the groups that the specified user belongs to
        echo "Groups ${username} belongs to:"
        groups $username
        echo "------------------------------------------------------------------------------"

        #If the user is logged in, it displays how long they have been logged in for
        #Otherwise, it says that the user is not currently logged in
        echo "Current Login Info"
        if w | grep -q $username; then
                echo w $username
        else
                echo "${username} is not currently logged in"
        fi
        echo "------------------------------------------------------------------------------"

        #Checks for the user's login activity in system logs
        #If no information is found, it tells the user
        echo "Recent Logins:"
        if last | grep -q $username; then
                last | grep $username
        else
                echo "No recent logins found"
        fi
        echo "------------------------------------------------------------------------------"

        #Checks their overall command history
        #Although their command history is usually stored in .bash_history, some users have it saved in .zsh_history (kali, for example)
        #Lets the user know if the specified user doesn't have a saved command history
        echo "Command History:"
        if [[ ! -f /home/$username/.zsh_history ]]; then
                if [[ ! -f /home/$username/.bash_history ]]; then
                        echo "No command history found"
                else
                        cat /home/$username/.bash_history
                fi
        else
                cat /home/$username/.zsh_history
                echo "YEEEEEEEEEEEE"
        fi
                                                              
        echo "------------------------------------------------------------------------------"

        #Checks their sudo command history
        #Lets the user know if no sudo command history for the specified user is found
        echo "Sudo Command History:"
        if [[ -f /var/log/auth.log ]]; then     
                if  grep -q $username /var/log/auth.log; then
                        if grep $username /var/log/auth.log | grep -q sudo; then
                                echo "it was me"
                                cat /var/log/auth.log | grep $username | grep sudo
                        else
                                echo "No sudo command history found"
                        fi
                else
                        echo "No sudo command history found"
                fi
        else
                echo "No sudo command history found"
        fi
        echo "------------------------------------------------------------------------------"
else
        echo "User not found"
fi