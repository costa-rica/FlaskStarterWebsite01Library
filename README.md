# Flask Starter Website Library

![Flask and DashAndData Logo](https://venturer.dashanddata.com/get_aux_file_from_dir/images/dd_and_flask.png)

## Description
This library includes the fsw_config and the fsw_models packages. 
- fsw_config contains the all the environmental varaibles
- fsw_models contains the MySQL database schema and other database related objects.


## Documentation
This uses MySQL and in order to create the tables you must do it from a terminal:
```
from sqlalchemy import create_engine
from fsw_models import Base,engine
from fsw_config import ConfigWorkstation
config = ConfigWorkstation()
new_engine_str = f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_SERVER}/{config.MYSQL_DATABASE_NAME}"
new_engine = create_engine(new_engine_str)
Base.metadata.create_all(new_engine)
```


