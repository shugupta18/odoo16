
#  Odoo (16) 
## custom_addons setup

- `python` commands
  ```python
  # venv is present

  # initialize db with base
  ./odoo-bin -c conf/odoo.conf -i base 
  ```
- `powershell` commands
  ```powershell
  D:\shubham\development_odoo\odoo17_dev\venv\Scripts\python.exe D:\shubham\development_odoo\odoo17_dev\odoo\odoo-bin scaffold dotpl_helpdesk D:\shubham\development_odoo\odoo17_dev\custom_addons
  ```
- `postgreSQL` commands
  ```postgresql
  -- use postgres (user)
  CREATE DATABASE your_database_name;
  CREATE USER your_user WITH PASSWORD 'your_password';
  GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_user;
  -- inside the your_database_name db
  GRANT ALL PRIVILEGES ON SCHEMA public TO your_user;
  ```
  

### `dotpl_helpdesk` setup
- `postgreSQL` commands to run:
  ```postgresql
  -- To see the Module info
  update public.ir_module_module set module_type = 'official' where name = 'dotpl_helpdesk'
  
  ``` 
- 




