UPDATE mysql.user SET Password=PASSWORD('') WHERE User='root';
flush privileges; 
quit
