import pandas as pd

class DojiScanner:
    def __init__(self, preferences):
        print(preferences)
        self.tolerance = preferences['doji_tolerance']

    def scan(self, historical_data):
        historical_data = pd.DataFrame(historical_data)
       # print(historical_data)
        historical_data['range'] = historical_data['high'] - historical_data['low']
        historical_data['mean'] = historical_data.groupby('symbol')['range'].transform('mean')
        historical_data = historical_data.sort_values('date', ascending=False)
        historical_data_last = historical_data.iloc[[0]].reset_index(drop=True)  # Reset the index
        
        body = abs(historical_data_last['close'] - historical_data_last['open'])
        
        
        if (historical_data_last['range'] > historical_data_last['mean']).all():
            doji_tolerance = body / historical_data_last['range']
            
            if (doji_tolerance <= self.tolerance).all():
                print(doji_tolerance)
                print(self.tolerance)
                historical_data_last['doji'] = 1
                results = historical_data_last.dropna()
                print(results)
                return results
            else:
                return None

        else:
            return None
                    
