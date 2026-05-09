FROM mysql

# mysql root password will be set to root
ENV MYSQL_ROOT_PASSWORD=root

# mysql will create a new database named mydb
ENV MYSQL_DATABASE=mydb

# the file db_schema.sql will get executed immediately when 
# the container gets created
COPY db_schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306

