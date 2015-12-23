UPDATE mysql.user SET Password=PASSWORD($CONTRASENA) WHERE User=$USUARIO;
flush privileges; 
quit
