import streamlit as st
import requests

'''
# tmz_use_case front
'''

# Parameters in the form
with st.form(key='params_for_api'):
    st.write("Fill in the information")

    # Site URL
    site_url = st.text_input('Give an url', 'https://www.larousse.fr/')

    # Blocklist_value -> found what it is
    if st.checkbox('Blocklist_value?'):
        blocklist_value = 1

    # Geo
    available_geos = ['FR',
                'JP',
                'IT',
                'BR',
                'ES',
                'DE',
                'US',
                'RU',
                'MX',
                'IN',
                'AR',
                'CO',
                'UA',
                'GB',
                'ID',
                'PE',
                'GR',
                'CL',
                'KZ',
                'NG',
                'Other']

    geo = st.selectbox('Select a country', available_geos)

    # Ads format to select
    st.write('Please select the ads the website owner can place?')

    # columns = st.columns(3)

    if st.checkbox('Format 1'):
        _1_ = 1

    if st.checkbox('Format 2'):
        _2_ = 1

    if st.checkbox('Format 3'):
        _3_ = 1

    if st.checkbox('Format 4'):
        _4_ = 1

    if st.checkbox('Format 5'):
        _5_ = 1

    if st.checkbox('Format 6'):
        _6_ = 1

    if st.checkbox('Format 11'):
        _11_ = 1

    if st.checkbox('Format 15'):
        _15_ = 1

    if st.checkbox('Format 16'):
        _16_ = 1

    if st.checkbox('Format 19'):
        _19_ = 1

    if st.checkbox('Format 20'):
        _20_ = 1

    if st.checkbox('Format 24'):
        _24_ = 1

    if st.checkbox('Format 27'):
        _27_ = 1

    if st.checkbox('Format 28'):
        _28_ = 1

    if st.checkbox('Format 30'):
        _30_ = 1

    if st.checkbox('Format 31'):
        _31_ = 1

    if st.checkbox('Format 34'):
        _34_ = 1

    if st.checkbox('Format 38'):
        _38_ = 1

    if st.checkbox('Format 39'):
        _39_ = 1

    if st.checkbox('Format 43'):
        _43_ = 1

    if st.checkbox('Format 44'):
        _44_ = 1

    if st.checkbox('Format 46'):
        _46_ = 1

    # Submit button
    st.form_submit_button("Get the details!")



# Get the prediction from the API
api_url = 'http://127.0.0.1:8000/predict'

def get_api_params(site_url, blocklist_value=0, geo='Other', _1_=0, _2_=1, _3_=0, _4_=0, _5_=0,
       _6_=0, _11_=0, _15_=0, _16_=0, _19_=0, _20_=0, _24_=0, _27_=0, _28_=0, _30_=0,
       _31_=0, _34_=0, _38_=0, _39_=0, _43_=0, _44_=0, _46_=0):
    return {'site_url' : site_url,
            'blocklist_value' : blocklist_value,
            'geo' : geo,
            '_1_' : _1_,
            '_2_' : _2_,
            '_3_' : _3_,
            '_4_' : _4_,
            '_5_' : _5_,
            '_6_' : _6_,
            '_11_' : _11_,
            '_15_' : _15_,
            '_16_' : _16_,
            '_19_' : _19_,
            '_20_' : _20_,
            '_24_' : _24_,
            '_27_' : _27_,
            '_28_' : _28_,
            '_30_' : _30_,
            '_31_' : _31_,
            '_34_' : _34_,
            '_38_' : _38_,
            '_39_' : _39_,
            '_43_' : _43_,
            '_44_' : _44_,
            '_46_' : _46_
        }

params = get_api_params(site_url, blocklist_value=0, geo='Other', _1_=0, _2_=1, _3_=0, _4_=0, _5_=0,
       _6_=0, _11_=0, _15_=0, _16_=0, _19_=0, _20_=0, _24_=0, _27_=0, _28_=0, _30_=0,
       _31_=0, _34_=0, _38_=0, _39_=0, _43_=0, _44_=0, _46_=0)

response = requests.get(api_url, params=params).json()

estimated_ca = round(response.get('estimated_ca'), 4)

lighthouse_score = round(response.get('lighthouse_score'), 4)
LCP = round(response.get('LCP'), 4)
FID = round(response.get('FID'), 4)
CLS = round(response.get('CLS'), 4)
FCP = round(response.get('FCP'), 4)
INP = round(response.get('INP'), 4)
TTFB = round(response.get('TTFB'), 4)
Social = round(response.get('Social'), 4)
Mail = round(response.get('Mail'), 4)
Referrals = round(response.get('Referrals'), 4)
Search = round(response.get('Search'), 4)
Direct = round(response.get('Direct'), 4)
BounceRate = round(response.get('BounceRate'), 4)
PagePerVisit = round(response.get('PagePerVisit'), 4)
Category = response.get('Category')
EstimatedMonthlyVisits = round(response.get('EstimatedMonthlyVisits'), 4)

# Write the result
st.write('The estimated CA is: ', estimated_ca)
st.write('The Lighthouse score is: ', lighthouse_score)



# All additionnal KPIs from API
# Pie chart for traffic?
# Métrique les unes à côté des autres?
# Ajouter une carte pour la géographie du site
