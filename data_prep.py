import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import re 

# Read in data file
xls = pd.ExcelFile('./data/raw/DataDownload.xls')
# Included
county_supp_data = pd.read_excel(xls, 'Supplemental Data - County')
socioeconomic = pd.read_excel(xls, 'SOCIOECONOMIC')
insecurity = pd.read_excel(xls, 'INSECURITY')
access = pd.read_excel(xls, 'ACCESS')
# Included, but columns were filtered
prices_taxes = pd.read_excel(xls, 'PRICES_TAXES') 
restaurants = pd.read_excel(xls, 'RESTAURANTS') 
assistance  = pd.read_excel(xls, 'ASSISTANCE')
local = pd.read_excel(xls, 'LOCAL')
# Not Included
# health = pd.read_excel(xls, 'HEALTH') # Dropped
# variables = pd.read_excel(xls, 'Variable List') # Dropped
# state_supp_data = pd.read_excel(xls, 'Supplemental Data - State') # Dropped, not granular enough
# stores = pd.read_excel(xls, 'STORES') # Dropped, included in ACCESS

# Drop state & county (captured in FIPS)
# insecurity.drop(columns=state_county) Kept so we have it in one...
state_county = ['State', 'County']
county_supp_data.drop(columns=state_county, inplace=True)
socioeconomic.drop(columns=state_county, inplace=True)
prices_taxes.drop(columns=state_county, inplace=True)
restaurants.drop(columns=state_county, inplace=True)
assistance.drop(columns=state_county, inplace=True)
access.drop(columns=state_county, inplace=True)
local.drop(columns=state_county, inplace=True)

# Drop Columns
# We dropped all columns that were aggregates (percentages, etc.)

# PRICES_TAXES
# We also dropped taxes because the actual prices seems more relevant
to_drop = ['MILK_SODA_PRICE10', 'SODATAX_VENDM14', 'CHIPSTAX_VENDM14', 'SODATAX_STORES14', 'CHIPSTAX_STORES14', 'FOOD_TAX14']
prices_taxes.drop(columns=to_drop, inplace=True)

# RESTAURANTS
# We also dropped things related to population because we have a population column and can determine its relevance with the predictive model
to_drop = ['PCH_FFRPTH_09_14', 'PCH_FFR_09_14', 'PCH_FSR_09_14', 'PCH_FSRPTH_09_14', 'PC_FFRSALES07', 'FFRPTH09', 'FFRPTH14', 'FSRPTH09', 'FSRPTH14', 'PC_FFRSALES12', 'PC_FSRSALES07', 'PC_FSRSALES12']
restaurants.drop(columns=to_drop, inplace=True)

# ASSISTANCE
# We only dropped the percentages here
to_drop = ['PCH_REDEMP_SNAPS_12_16', 'PCT_SNAP12', 'PCH_SNAP_12_16',
       'PC_SNAPBEN10', 'PC_SNAPBEN15', 'PCH_PC_SNAPBEN_10_15','SNAP_PART_RATE08', 'SNAP_PART_RATE13',
       'SNAP_REPORTSIMPLE09', 'SNAP_REPORTSIMPLE16', 'PCT_NSLP09',
       'PCH_NSLP_09_15', 'PCT_FREE_LUNCH09', 'PCT_FREE_LUNCH14',
       'PCT_REDUCED_LUNCH09', 'PCT_REDUCED_LUNCH14', 'PCT_SBP09',
       'PCH_SBP_09_15', 'PCT_SFSP09', 'PCH_SFSP_09_15',
       'PC_WIC_REDEMP08', 'PC_WIC_REDEMP12', 'PCH_PC_WIC_REDEMP_08_12',
       'PCH_REDEMP_WICS_08_12', 'PCT_WIC09',
       'PCH_WIC_09_15', 'PCT_CACFP09',
       'PCH_CACFP_09_15'
       ]
assistance.drop(columns=to_drop, inplace=True)

# LOCAL
# Only included columns that seems directly relevant or "pure" in the sense that they had numbers we could draw conclusions from
# rather than being columns that were combined with others.. (aggregates again basically)
wanted = ['FIPS', 'DIRSALES07','DIRSALES12','FMRKT09','FMRKT16','FMRKT_SNAP16','FMRKT_WIC16','FMRKT_WICCASH16','FMRKT_SFMNP16',
    'FMRKT_CREDIT16','FMRKT_FRVEG16','FMRKT_ANMLPROD16','FMRKT_BAKED16','FMRKT_OTHERFOOD16','FRESHVEG_ACRES07','FRESHVEG_ACRES12',
    'ORCHARD_ACRES07','ORCHARD_ACRES12','BERRY_ACRES07','BERRY_ACRES12','SLHOUSE07','SLHOUSE12','GHVEG_SQFT07','GHVEG_SQFT12',
    'FOODHUB16','FARM_TO_SCHOOL09','FARM_TO_SCHOOL13'
]
local = local[wanted]

# read in county level data for food insecurity
county = pd.read_csv("data/prepped/insec15.csv")
county["FIPS"] = county.Fips
county = county[["FIPS", "Food_Insec", "Food_Insec_Children"]]

# Scope variables
scoped = pd.DataFrame()
scoped = socioeconomic.merge(county_supp_data, left_on='FIPS', right_on='FIPS ')
scoped = scoped.merge(insecurity, on='FIPS')
scoped = scoped.merge(access, on='FIPS')
scoped = scoped.merge(prices_taxes, on='FIPS')
scoped = scoped.merge(restaurants, on='FIPS')
scoped = scoped.merge(assistance, on='FIPS')
scoped = scoped.merge(local, on='FIPS')
scoped = scoped.merge(county, on='FIPS')

cols = ['2010 Census Population',	'Population Estimate, 2011',	'Population Estimate, 2012',	'Population Estimate, 2013',	'Population Estimate, 2014',	'Population Estimate, 2015',	'Population Estimate, 2016']
for idx, row in scoped.iterrows():
    for col in cols:
        scoped.loc[idx, col] = np.float64(re.sub('[^0-9]', '', row[col]))

scoped.drop(columns=['County', 'State'], inplace=True)
scoped.fillna(-1, inplace=True)

# Train, test, split
train_features, test_features, train_outcome, test_outcome = train_test_split(
    scoped, #features
    scoped.Food_Insec_Children, #outcome # or scoped['FOODINSEC_CHILD_03_11']
    test_size=0.30, #percent of data to use as test set
    random_state=11
)


scoped.to_csv('./data/prepped/compiled_data.csv', sep=',')

train_features.to_csv('./data/prepped/train_features.csv', sep=',')
test_features.to_csv('./data/prepped/test_features.csv', sep=',')
train_outcome.to_csv('./data/prepped/train_outcome.csv', sep=',')
test_outcome.to_csv('./data/prepped/test_outcome.csv', sep=',')

