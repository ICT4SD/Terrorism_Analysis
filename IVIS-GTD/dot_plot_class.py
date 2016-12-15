from util import *

class Dot_Plot_Data():
    def __init__(self, data, yaxis_vals, xaxis_vals, user_filter1, user_filter2, metric):
        '''Defines attributes of the dot plot'''
        self.data = data[[yaxis_vals, xaxis_vals, user_filter1, user_filter2]]
        self.yaxis_vals = yaxis_vals
        self.xaxis_vals = xaxis_vals
        self.user_filter1 = user_filter1
        self.user_filter2 = user_filter2
        self.subgroups = group_by_columns(self.data, [self.yaxis_vals, self.user_filter1, self.user_filter2], self.xaxis_vals)
        self.metric = metric
        if self.metric == 'occurrences':
            self.count_by_subgroup()
        if self.metric == 'casualties':
            self.sum_by_subgroup()
        
    def count_by_subgroup(self):
        '''Uses group from init function to create a count'''
        self.data = unstack_table(count_by_groups(self.subgroups))
        
    def sum_by_subgroup(self):
        '''Uses sum from init function to create a sum'''
        self.data = unstack_table(sum_by_groups(self.subgroups))
  
    def user_selection(self, year_tuple, attack_type):
        '''Selects year and attack type'''
        years = tuple(range(year_tuple[0], year_tuple[1]))
        self.attack_type = attack_type
        self.data = self.data.loc[:, (slice(None), attack_type, years)]
    
    def aggregate(self):
        '''sum horizontally'''
        self.data = self.data.sum(axis=1)
        
    def convert_series(self, label):
        '''Takes a series and label for the series' values, returns dataframe with 2 columns: the series' row index, & the series' values'''
        self.label = label
        self.data = pd.DataFrame(self.data)
        self.data.columns = [label]
        self.data.reset_index(level=0, inplace=True)
    
    def take_top_20(self):
        self.data = self.data.sort_values(self.label, ascending=False).iloc[0:20, :]