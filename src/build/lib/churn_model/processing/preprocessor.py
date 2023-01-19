from sklearn.base import BaseEstimator,TransformerMixin


class sklearnWrapper(BaseEstimator,TransformerMixin):
    
    def __init__(self,features,transformer):
        super().__init__()
        
        self.features = features
        self.transformer = transformer
        
    def fit(self,df):
        x = df.copy()
        self.transformer.fit(x[self.features])
        
        return self
    
    def transform(self,df):
        x = df.copy()
        x[self.features] = self.transformer.transform(x[self.features])
        
        return x


class dropAndRenameColumns(BaseEstimator,TransformerMixin):
    
    def __init__(self,features,features_rename,categorical):
        
        super().__init__()
        self.features = features
        self.features_rename = features_rename
        self.categorical = categorical
        
    def fit(self,df):
        
        return self
    
    
    def transform(self,df):
        
        x = df.copy()
        x = x.rename(columns= self.features_rename)
        x[self.categorical]= x[self.categorical].astype('O')
        x.drop(columns= self.features,inplace=True)
        return x
        
class createFeatures(BaseEstimator,TransformerMixin):
    
    def __init__(self):
        
        super().__init__()
        self
        
    def fit(self,df):
        
        return self
    
    
    def transform(self,df):
        
        xx = df.copy()
        
        # Derived variables to measure change in usage 

        # Usage 
        xx['delta_vol_3g'] = xx['vol_3g_mb_8'] - xx['vol_3g_mb_6']\
                                .add(xx['vol_3g_mb_7']).div(2)
        
        xx['delta_total_og_mou'] = xx['total_og_mou_8'] - xx['total_og_mou_6']\
                                        .add(xx['total_og_mou_7']).div(2)
        
        xx['delta_total_ic_mou'] = xx['total_ic_mou_8'] - xx['total_ic_mou_6']\
                                    .add(xx['total_ic_mou_7']).div(2)
        
        xx['delta_vbc_3g'] = xx['vbc_3g_8'] - xx['vbc_3g_6'].add(xx['vbc_3g_7']).div(2)

        # Revenue 
        xx['delta_arpu'] = xx['arpu_8'] - xx['arpu_6'].add(xx['arpu_7']).div(2)
        xx['delta_total_rech_amt'] = xx['total_rech_amt_8'] - \
                                xx['total_rech_amt_6'].add(xx['total_rech_amt_7']).div(2)
        
        
        
        xx.drop(columns=[
                 'vol_2g_mb_8', 'vol_2g_mb_6', 'vol_2g_mb_7','vol_3g_mb_8'  ,
            'vol_3g_mb_6', 'vol_3g_mb_7' ,
            'total_og_mou_8','total_og_mou_6', 'total_og_mou_7', 
            'total_ic_mou_8','total_ic_mou_6', 'total_ic_mou_7',
            'vbc_3g_8','vbc_3g_6','vbc_3g_7','arpu_8','arpu_6','arpu_7',
            'total_rech_amt_8', 'total_rech_amt_6', 'total_rech_amt_7'
    
            ], inplace=True)
        
        return xx
        
    