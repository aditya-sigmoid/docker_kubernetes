create table if not exists assignmnt_data (
id int primary key,
dag_id varchar not null,
execution_date varchar not null
);
insert into assignmnt_data(id,dag_id,execution_date)
select id,dag_id,execution_date from dag_run
on conflict (id)
do nothing;
