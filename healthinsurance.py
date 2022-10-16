import numpy as np
import pandas as pd
import pickle

class HealthInsurance():
    def __init__(self):
        self.home_path = 'C:\\Users\\Notebook\\repos\\Insurance-Cross-Sell\\'
        self.annual_premium_scaler      = pickle.load(open(self.home_path + 'src\\features\\annual_premium_scaler.pkl','rb'))
        self.age_scaler                  = pickle.load(open(self.home_path + 'src\\features\\age_scaler.pkl','rb'))
        self.vintage_scaler              = pickle.load(open(self.home_path + 'src\\features\\vintage_scaler.pkl','rb'))
        self.gender_scaler               = pickle.load(open(self.home_path + 'src\\features\\gender_scaler.pkl','rb'))
        self.region_code_scaler          = pickle.load(open(self.home_path + 'src\\features\\region_code_scaler.pkl','rb'))
        self.policy_sales_channel_scaler = pickle.load(open(self.home_path + 'src\\features\\policy_sales_channel_scaler.pkl','rb'))       
        self.vehicle_damage_scaler       = pickle.load(open(self.home_path + 'src\\features\\vehicle_damage_scaler.pkl','rb'))       

    def data_cleaning(self, df1):

        # region_code
        df1['region_code'] = df1['region_code'].astype('int64')

        # policy_sales_channel 
        df1['policy_sales_channel'] = df1['policy_sales_channel'].astype('int64')

        return df1

    def feature_engineering(self, df2):

        # vericle_age
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'bellow_1_year' if x == '< 1 Year' else 
                                                             'between_1_2_year' if x == '1-2 Year' else 
                                                             'over_2_years')
        return df2
    
    
    def data_preparation(self, df5):

        ## annual_premium
        df5['annual_premium'] = self.annual_premium_scaler.transform(df5[['annual_premium']].values)

        ## 5.3 Rescaling

        ## age
        df5['age'] = self.age_scaler.transform( df5[['age']].values )

        ## vintage
        df5['vintage'] = self.vintage_scaler.transform( df5[['vintage']].values )

        ## 5.4 Encoder
        ### 5.4.1 One Hot Enconding

        ## vehicle_age
        df5 = pd.get_dummies(df5, prefix='vehicle_age',columns=['vehicle_age'])

        ### 5.4.2 Target Enconding

        # gender 
        df5.loc[:,'gender'] = df5['gender'].map(self.gender_scaler)

        # region_code 
        df5.loc[:,'region_code'] = df5['region_code'].map(self.region_code_scaler)

        # vehicle damage
        df5.loc[:,'vehicle_damage'] = df5['vehicle_damage'].map(self.vehicle_damage_scaler)

        ### 5.4.3 Frequency Enconding

        ## policy_sales_channel 
        df5.loc[:,'policy_sales_channel'] = df5['policy_sales_channel'].map(self.policy_sales_channel_scaler)

        cols_selected = [
                'vintage',
                'annual_premium',
                'age',
                'region_code',
                'vehicle_damage',
                'policy_sales_channel',
                'previously_insured']
        
        return df5[cols_selected]

    def get_predict(self, model, original_data, test_data):
        
        # model prediction
        pred = model.predict_proba(test_data)
        
        # join prediction into original data
        original_data['prediction'] = pred[:,1].tolist()
        
        return original_data.to_json(orient='records', date_format='iso')
        