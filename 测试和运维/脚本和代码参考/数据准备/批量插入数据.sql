/* 
    运行环境：Oracle数据库
    测试需求，id、姓名、邮箱、手机号不可重复
 */
create sequence id_sequence; -- 创建序列id_sequence
create table USERINFO
(
    ids number(11) NOT NULL,
    activity_name varchar(255) NOT NULL,
    intractive_type varchar(255) DEFAULT NULL NOT NULL,
    email varchar(255) NOT NULL,
    mobile int NOT NULL,
    userAgent varchar(255) NOT NULL,
    email_title varchar(255) NOT NULL,
    label varchar(255) NOT NULL,
    category1 varchar(255) NOT NULL,
    time date NOT NULL,
    time1 date NOT NULL,
    primary key(ids)
);

declare
i number;
begin
    for i in 100..130 -- 100..130代表循环30次，按需求修改
loop
    insert into USERINFO
    values(id_sequence.nextval, '这是名字'||id_sequence.nextval, '现金', 137||lpad(id_sequence.nextval,8,0)||'@qq.com', 137||lpad(id_sequence.nextval,8,0), 2, 1, 2, 20, to_date('2018-09-29','yyyy-mm-dd'), to_date('2018-09-29','yyyy-mm-dd'));
end
loop;
commit;
end;