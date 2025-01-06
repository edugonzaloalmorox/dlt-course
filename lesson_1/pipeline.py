import dlt
import os
from dlt.common.pipeline import get_dlt_pipelines_dir

# Sample data containing pokemon details
data = [
    {"id": "1", "name": "bulbasaur", "size": {"weight": 6.9, "height": 0.7}},
    {"id": "4", "name": "charmander", "size": {"weight": 8.5, "height": 0.6}},
    {"id": "25", "name": "pikachu", "size": {"weight": 6, "height": 0.4}},
]


print(data)

# Set pipeline name, destination, and dataset name
pipeline = dlt.pipeline(
    pipeline_name="pokemon_data_pipeline",
    destination="duckdb", 
    dataset_name="pokemon_data",             
    dev_mode=True

)


# Run the pipeline and load the info

load_info = pipeline.run(data, table_name="pokemon")
print(load_info)










