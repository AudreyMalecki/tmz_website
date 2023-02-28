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
    if st.checkbox('Would you like to prevent some publishers to post on your website?'):
        blocklist_value = 1
    else :
        blocklist_value = 0

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

    columns = st.columns(5)
    global ads_format_list
    ads_format_list = [1, 2, 3, 4, 5, 6, 11, 15, 16, 19, 20, 24, 27, 28, 30, 31, 34, 38, 39, 43, 44, 46]
    ads_format_answer = []
    column_num = 0
    for i, e in enumerate(ads_format_list):
        if columns[i%5].checkbox(f'Format {e}'):
            ads_format_answer.append(1)
        else:
            ads_format_answer.append(0)

    # Submit button form
    form_button = st.form_submit_button("Get the details!")


    # Get params for API request
    api_url = 'http://127.0.0.1:8000/predict'

    def get_api_params(site_url, blocklist_value=0, geo='Other', ads_format_answer=[]):
        dicto = {'site_url' : site_url,
                'blocklist_value' : blocklist_value,
                'geo' : geo,
            }
        for ans, lis in zip(ads_format_answer,ads_format_list):
            dicto[f'_{lis}_']=ans
        return dicto

# API request and answer when button submitted
if form_button:
    params = get_api_params(site_url, blocklist_value, geo, ads_format_answer)

    response = requests.get(api_url, params=params).json()

    # KPIs retrieved from our API of prediction

    estimated_ca = round(response.get('estimated_ca'), 4)

    lighthouse_score = round(response.get('lighthouse_score'), 4)
    LCP = response.get('LCP')
    FID = response.get('FID')
    CLS = response.get('CLS')
    FCP = response.get('FCP')
    INP = response.get('INP')
    TTFB = response.get('TTFB')
    Social = response.get('Social')
    Mail = response.get('Mail')
    Referrals = response.get('Referrals')
    Search = response.get('Search')
    Direct = response.get('Direct')
    BounceRate = response.get('BounceRate')
    PagePerVisit = response.get('PagePerVisit')
    Category = response.get('Category')
    EstimatedMonthlyVisits = response.get('EstimatedMonthlyVisits')

    # Write the result
    st.write(params)
    st.write('The estimated CA is: ', estimated_ca)
    st.write('The Lighthouse score is: ', lighthouse_score)
    st.write(TTFB, Social)

    # Highlight major KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Lighthouse Score", f'{round(lighthouse_score*100,0)}%')
    col2.metric("Bounce Rate", f'{round(BounceRate*100, 2)}%')
    col3.metric("Estimated Monthly Visits", EstimatedMonthlyVisits)
    col4.metric("Page Per Visit", round(PagePerVisit, 2))



# All additionnal KPIs from API
# Pie chart for traffic?
# Métrique les unes à côté des autres?
# Ajouter une carte pour la géographie du site
