#!/bin/bash
  
NewUser(){
echo "Name: "
read: NAME
echo "Group: "
read GROUP
}

newUser(){
    echo "New Name: "
    sudo useadd $NAME
    echo "New Group: "
    sudo groupadd $GROUP
    sudo useradd -aG $NAME $GROUP
}

Prompt(){
echo "New Name? Y/N"
read Y
read N
}

while [ Prompt = "Y" ]
    do NAME GROUP
    done

    echo "exit"
~                                                                                              
~                                                                                              
~                                                                                              
~                                                                                              
~                                                                                              
~                                                                                              
~                                                                                              
~                                                                                              
~                                                                                              
~                                                                                              
~                                                                                              
-- INSERT --                                                                 1,1           All
[ttyd] 0:vim*                                                 "student@bchd: ~" 16:46 28-Sep-22
