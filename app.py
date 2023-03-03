import streamlit as st
import requests
from numerize import numerize
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

# Adding logo at the beginning
columns_1 = st.columns(3)

image = Image.open('images/logomoneytizer.png')
columns_1[2].image(image, use_column_width=True)

# API title
st.markdown(
'''
# 🚀 The Estimator 🚀
'''
)

# Parameters in the form
with st.form(key='params_for_api'):
    st.markdown('''#### Provide the infos of your website and get your estimation 💸''')

    # Site URL
    site_url = st.text_input('What is your website url ? 🌐', 'https://www.larousse.fr/')

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

    geo = st.selectbox('Where is the majority of your audience living ? 🌍', available_geos)

    # Blocklist_value -> found what it is
    if st.checkbox('Would you like to prevent some publishers to post on your website ? ⛔'):
        blocklist_value = 1
    else :
        blocklist_value = 0

    # Ads format to select
    st.write('Which ad formats would you like to display on your website ? Tick as many as you wish ! ✔️')

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
    form_button = st.form_submit_button("Get your estimation ! 🙃")


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
    with st.spinner('Estimation in progress...'):

        params = get_api_params(site_url, blocklist_value, geo, ads_format_answer)

        response = requests.get(api_url, params=params).json()

    # Display sth fun once the result is available
    st.balloons()

    # KPIs retrieved from our API of prediction
    estimated_ca = round(response.get('estimated_ca'), 4)

    lighthouse_score = round(response.get('lighthouse_score'), 4)
    LCP = response.get('LCP')
    FID = response.get('FID')
    CLS = response.get('CLS')
    FCP = response.get('FCP')
    INP = response.get('INP')
    TTFB = response.get('TTFB')
    Social = float(response.get('Social'))
    Mail = float(response.get('Mail'))
    Referrals = float(response.get('Referrals'))
    Search = float(response.get('Search'))
    Direct = float(response.get('Direct'))
    BounceRate = response.get('BounceRate')
    PagePerVisit = response.get('PagePerVisit')
    Category = response.get('Category')
    EstimatedMonthlyVisits = response.get('EstimatedMonthlyVisits')

    # CA prediction
    # st.write('The estimated CA is: ', estimated_ca)
    # st.markdown('''
    #             ### Your estimated CA is:
    #             ''')
    columns_2 = st.columns(3)
    columns_2[1].metric("Your estimated CA is", round(estimated_ca, 2))


    # Highlight major KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Lighthouse Score", f'{round(lighthouse_score*100,0)}%')
    col2.metric("Bounce Rate", f'{round(BounceRate*100, 2)}%')
    col3.metric("Estimated Monthly Visits", numerize.numerize(EstimatedMonthlyVisits))
    col4.metric("Page Per Visit", round(PagePerVisit, 2))

    # Display category website
    columns_3 = st.columns([1, 3])
    columns_3[0].metric('Website Category: ', Category.title())

    # Traffic repartition
    labels = ['Social', 'Mail', 'Referrals', 'Search', 'Direct']
    y = np.array([Social, Mail, Referrals, Search, Direct])

    dict_kpis = {}
    for i, j in zip(labels, y):
        dict_kpis[i] = j

    hist_values = pd.DataFrame(dict_kpis, index=[0])
    fig, ax = plt.subplots()
    ax.bar(x=labels, height=y, color=['blue', 'red', 'yellow', 'green'])

    columns_3[1].pyplot(fig)

    # # Pie chart
    # y = np.array([Social, Mail, Referrals, Search, Direct])

    # fig, ax = plt.subplots()
    # ax.pie(y, labels=['Social', 'Mail', 'Referrals', 'Search', 'Direct'])
    # fig.legend()

    # st.pyplot(fig)

    # # Map to localize the web site
    # def geocode(address):
    #     params = { "q": address, 'format': 'json' }
    #     places = requests.get(f"https://nominatim.openstreetmap.org/search", params=params).json()
    #     return [places[0]['lat'], places[0]['lon']]

    # coordinates = {
    #     'latitude': [float(geocode(geo)[0])],
    #     'longitude': [float(geocode(geo)[1])]
    # }

    # df = pd.DataFrame(coordinates)
    # st.map(coordinates)
