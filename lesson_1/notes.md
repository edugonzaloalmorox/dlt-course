# Get started

## dlt 

- It is a system to load data mainly. It automates the schema creation (see below what a schema is), the data normalization and the incremental loading. It does not automate data modelling.







## Creating a pipeline

- A pipeline is a connection that moves data from the Python code to a destination. This destination can be a database or a simpler format such csv or json file. 

- In `dlt`, the pipeline accepts `dlt` sources or resources, as well as generators, async generators, lists, and any iterables. Once the pipeline runs, all resources are evaluated, the schema is created and the data is loaded at the destination. 

- A schema is a logical structure that defines the organization and storage of data within a database. It acts as a blueprint for how data is organized, including tables, views, indexes, constraints, relationships, and other database objects. The key features of a schema are the organization of the data, the relationships, the security and access control and the modularity. `dlt` flattens dictionaries and unpacks nested lists into sub-tables


- `dlt.pipeline` creates a pipeline object and then it must be run with the method `run`. This method is used to load the data

`<dlt.pipeline.pipeline.Pipeline object at 0x115433f50>``

- The creation of a pipeline (`dlt.pipeline()`) has the following arguments:

    - `pipeline_name`: This is the name you give to your pipeline. It helps you track and monitor your pipeline, and also helps to bring back its state and data structures for future runs. If you don't give a name, dlt will use the name of the Python file you're running as the pipeline name.
    - `destination`: a name of the destination to which dlt will load the data. It may also be provided to the run method of the pipeline (this can be sqlite, duckdb, etc...)
    - `dataset_name`: This is the name of the group of tables (or dataset) where your data will be sent. You can think of a dataset like a folder that holds many files, or a schema in a relational database. You can also specify this later when you run or load the pipeline. If you don't provide a name, it will default to the name of your pipeline.
    - `dev_mode`: If you set this to True, dlt will add a timestamp to your dataset name every time you create a pipeline. This means a new dataset will be created each time you create a pipeline.

- dlt pipelines are portable, making them a great fit for local development, cloud deployment, and serverless environments—essentially anywhere Python runs.

- The `schemas` are the same on different DB systems with slightly different datatypes based on database support.