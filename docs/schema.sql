create database virgo default character set utf8mb4 collate utf8mb4_unicode_ci;

drop table if exists user;
create table user (
    id int unsigned not null auto_increment primary key,
    nickname varchar(20) default 'xxx',
    username varchar(20) unique not null,
    password varchar(20) not null,
    status int not null default 1 comment '状态 1 启用 2 禁用',
    create_time datetime not null default current_timestamp()
)ENGINE=InnoDB comment='用户表';

insert into user(id, nickname, username, password, create_time) values(1, 'xgj', 'xgj', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(2, 'zhangyunan', 'zhangyunan', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(3, 'dujinlei', 'dujinlei', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(4, 'zhangyufei', 'zhangyufei', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(5, 'zhangxueyan', 'zhangxueyan', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(6, 'fudongkai', 'futongkai', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(7, 'zhangchenchen', 'zhangchenchen', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(8, 'niuzhaorong', 'niuzhaorong', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(9, 'huxulei', 'huxulei', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(10, 'liurenyu', 'liurenyu', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(11, 'changhongyuan', 'changhongyuan', '123456', '2015-08-01 14:56:49');
insert into user(id, nickname, username, password, create_time) values(12, 'cuishan', 'cuishan', '123456', '2015-08-01 14:56:49');


SELECT * from user;

drop table if exists movie_category;
create table movie_category (
  id int unsigned not null auto_increment primary key,
  name varchar(30) not null comment '分类名称',
  create_time datetime not null default current_timestamp()
)ENGINE=InnoDB comment='电影分类表';

select * from movie_category;

create table movie (
   id int unsigned not null auto_increment primary key,
   category_id int unsigned not null comment '分类id',
   img_url varchar(150) null comment '影片还报地址',
   description varchar(200) null comment '简介',
   douban_score decimal(5,2) default 0.0 comment '豆瓣分数',
   release_time datetime comment '上映时间',
   resource_url varchar(200) comment '资源地址',
   name varchar(30) not null comment '电影名称',
   create_time datetime not null default current_timestamp()
)ENGINE=InnoDB comment='电影';