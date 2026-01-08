USE sampledb;

CREATE TABLE emps(
	empno int not null,
    empname varchar(50),
    job varchar(30),
    constraint pK_emps PRIMARY KEY (empno)
);

CREATE TABLE salary(
	empno int not null,
    salary int,
    constraint fk_emps FOREIGN KEY (empno) REFERENCES emps(empno)
);

CREATE TABLE orders(
	pono int not null,
    empno int not null,
    total int,
    constraint pk_orders PRIMARY KEY (pono),
    constraint fk_emps_orders FOREIGN KEY (empno) REFERENCES emps(empno)
);


