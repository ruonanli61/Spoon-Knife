import pandas as pd

from primo.utils.demo_utils import(
    get_well_type,
    sort_columns,
    sort_by_disadvantaged_community_impact,
    get_population_by_state
)

result_df = get_population_by_state(37)
print(result_df['state'].dtypes)
assert result_df['state'].dtypes == str