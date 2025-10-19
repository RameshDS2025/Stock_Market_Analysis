import matplotlib.pyplot as plt
import pymysql
import pandas as pd
import base64
import seaborn as sns
import streamlit as st

#To set the background image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()  #  only read once

# Path to your background image
image_base64 = get_base64_of_bin_file("SMA_image.jpg")

# CSS to set background across the entire app
page_bg_img = f"""
<style>
/* Main page background */
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{image_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Sidebar background */
[data-testid="stSidebar"] {{
    background-image: url("data:image/png;base64,{image_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-color: rgba(0, 0, 0, 0.6);  /* Optional dark overlay for contrast */
    background-blend-mode: overlay;
}}

/* Make the top header (Deploy bar) transparent */
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

/* Reduce unnecessary padding for a cleaner layout */
.block-container {{
    padding-top: 0rem;
    padding-bottom: 1rem;
}}
</style>
"""

# Inject CSS once
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar logo
st.sidebar.image("Side_Bar_Image.JPG", width=150)

#Connecting to the database
mydb = pymysql.connect(
 host="localhost",
 user="root",
 password="",
 database="stock_market_analysis"
 
)
mycursor = mydb.cursor()

#Header with customized styles
st.markdown(
    """
    <div style="padding:2px; border-radius:2px; text-align:center;">
    <h2 style="
        color: #539c17; 
        font-size: 3.7em; 
        font-family: Impact, Arial Black, Arial, sans-serif; 
        font-weight: bold; 
        letter-spacing: 0.05em;
        margin-bottom: -18px;   /* reduce bottom margin */
        padding-bottom: 0;     /* remove extra padding */
        text-shadow:
           2px 2px 0 #bbb,
           4px 4px 0 #888,
           6px 6px 0 #333,
           8px 8px 8px #000;
        ">
        &#128200; Stock Driven Analysis
    </h2>
</div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
div.stButton > button {
    background-color: #351482;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    margin-right: 8px;
}
div.stButton > button:hover {
    background-color: #c92e3a;
}
</style>
""", unsafe_allow_html=True)

Volatility = st.sidebar.button("Stock Volatility", type="primary")
Cumulative_Return = st.sidebar.button("Cumulative Return", type="primary")
yearly_returns = st.sidebar.button("Average yearly Return", type="primary")
Correlation = st.sidebar.button("Correlation of closing stocks", type="primary")
Gainers_Losers = st.sidebar.button("Top 5 Gainers and Losers", type="primary")

# Button layout with minimal spacing between them
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col1:
    About_us = st.button("About us", type="primary")

with col2:
    Stock_Names = st.button("Stock Names", type="primary")

with col3:
    Market_Trends = st.button("Market Trends", type="primary")

with col4:
    Market_Insights = st.button("Market Insights", type="primary")

with col5:
    Contact = st.button("Contact Us", type="primary")

if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = True

# If any button is clicked, hide the welcome
if any([
    About_us, Stock_Names, Market_Trends, Market_Insights, Contact,
    Volatility, Cumulative_Return, yearly_returns, Correlation, Gainers_Losers
]):
    st.session_state.show_welcome = False

#  Animated Welcome Message 
if st.session_state.show_welcome:
    st.markdown("""
        <style>
        @keyframes moveArrowLeft {
            0% {transform: translateX(0);}
            50% {transform: translateX(-15px);}
            100% {transform: translateX(0);}
        }
        .arrow {
            display: inline-block;
            color: #E63946;
            font-size: 48px;  /* Enlarged arrow */
            font-weight: bold;
            animation: moveArrowLeft 1.2s infinite ease-in-out;
            margin-right: 12px;
        }
        .welcome {
            text-align: center;
            margin-top: 20px;
            margin-bottom: 30px;
            font-family: 'Trebuchet MS', sans-serif;
            font-size: 36px;
            font-weight: bold;
            color: #4b064f;
        }
        .highlight {
            color: #274091;
        }
        </style>

        <div class="welcome">
            👋 Welcome to <span class="highlight">Stock Driven Analysis!</span><br>
            <span class="arrow">←</span> Explore insightful stock visualizations from the sidebar
        </div>
    """, unsafe_allow_html=True)

# Left-align content below buttons
if About_us:

    st.markdown("""
            <div style="background-color:#e6f0ff; padding:20px; border-radius:10px;">
            <h3 style="color:#800000;">About Us</h3>
            
            <p style="color:#061f38; font-size:16px; text-align:left;"> 
                Stock Driven Analysis transforms raw market data into actionable insights for informed investment
                decisions. Our user-friendly dashboards visualize real-time volatility, returns, and 
                correlations across leading stocks. Powerful analytics tools help investors identify 
                top-performing stocks and emerging trends with confidence. The platform is designed for both 
                beginners and professionals, making advanced stock analysis intuitive and accessible. We are 
                committed to transparency, reliability, and empowering users to succeed in today's 
                dynamic markets.
            </p>

            <h6><b>Stock Volatility:</b> <span style="font-weight: normal;"> Measure and compare real-time price fluctuations to assess market risk. </span> </h6>
            <h6><b>Cumulative Return:</b> <span style="font-weight: normal;"> Track the total percentage gain or loss of a stock over a specific period. </span> </h6>
            <h6><b>Average Yearly Return:</b> <span style="font-weight: normal;"> Evaluate the mean annual growth of investments for better financial planning. </span> </h6>
            <h6><b>Correlation of Closing Stocks:</b> <span style="font-weight: normal;"> Analyze how different stocks move in relation to each other. </span> </h6>
            <h6><b>Top 5 Gainers and Losers:</b> <span style="font-weight: normal;"> Instantly discover which stocks led or lagged in performance each day. </span> </h6>
            </div>

            """, unsafe_allow_html=True)

if Stock_Names:
    st.markdown(
        "<h3 style='color:#660d0d; font-weight:bold; text-align:left;'>Stock Names</h3>",
        unsafe_allow_html=True
    )
    st.image("SMA_Stock_Names.JPG")

if Market_Trends:

    st.markdown("""
            <div style="background-color:#e6f0ff; padding:20px; border-radius:10px;">
            <h3 style="color:#800000;">Market Trends</h3>
            
            <p style="color:#061f38; font-size:16px; text-align:left;"> 
            The current market trends reveal notable volatility in some sectors, with FMCG and 
            pharmaceuticals showing strong price movements based on recent data. Stocks like Britannia 
            and Cipla have demonstrated both upward momentum and periodic corrections, indicating active 
            trading and frequent adjustments by investors. The engineering and banking sectors are 
            witnessing periodic surges, with companies like L&T and Kotak Mahindra Bank frequently 
            breaking monthly highs and lows. Overall, the market is characterized by sector rotation 
            and a quest for stability amidst fluctuation. Trading volumes have spiked during specific 
            windows, supporting breakout moves and reflecting investor sentiment shifts. Recent months 
            have seen increased attention to retail stocks like TRENT, which have shown persistent 
            gains alongside heightened volatility. The data suggests that market participants remain 
            sensitive to economic and industry news, creating opportunities for agile decision-making. 
            Investors should monitor leading sectors and top-traded stocks closely to benefit from these 
            evolving trends.
            </p>

            """, unsafe_allow_html=True)
    
if Market_Insights:

    st.markdown("""
            <div style="background-color:#e6f0ff; padding:20px; border-radius:10px;">
            <h3 style="color:#800000;">Market Insights</h3>
            
            <p style="color:#061f38; font-size:16px; text-align:left;"> 
            Recent analytics highlight unusually rapid price changes across major indices and frequent reversals 
                in trend, with several stocks recording high standard deviations over recent periods. Sector 
                leaders benefit from strong fundamentals, while some engineering and bank stocks show more 
                speculative-driven volatility. Volume spikes accompany breakout sessions, confirming that 
                liquidity and news flow remain decisive market drivers. Retail investor activity is noticeable 
                in high-turnover stocks like TRENT, often correlating with broader sentiment swings. Persistent 
                volatility underscores the importance of monitoring both macroeconomic trends and micro-level 
                company updates. The dashboard and image collectively capture how trader psychology and 
                real-time events shape market outcomes. Insightful interpretation of these patterns supports 
                better investment timing and risk management strategies for all types of market participants.
            </p>

            """, unsafe_allow_html=True)
    
if Contact:

    st.markdown("""
            <div style="background-color:#e6f0ff; padding:20px; border-radius:10px;">
            <h3 style="color:#800000;">Contact Us</h3>
            
            <p style="color:#061f38; font-size:16px; text-align:left;"> 
            0001 North Avenue, <br>
            Hollywood,  <br>
            USA - 10001.
            </p>

            """, unsafe_allow_html=True)
    

# Top 10 Most Volatile Stocks

if Volatility:
    st.markdown(
            "<h4 style='color:#020005; background-color:#3b7ead; padding:8px 12px; border-radius:6px; margin-bottom:16px;'>"
            "Top 10 Most Volatile Stocks Based on Standard Deviation"
            "</h4>",    
    unsafe_allow_html=True
)
    mycursor.execute("SELECT Ticker, Std_dev FROM stock_std_dev ORDER BY Std_dev DESC LIMIT 10")
    data = mycursor.fetchall()
    df = pd.DataFrame(data, columns=['Ticker', 'Std_dev'])
    
    fig, ax = plt.subplots(figsize=(6, 4), facecolor='#020005')  # Figure background black
    fig.patch.set_facecolor("#A1C0E7")
    ax.set_facecolor("#B0DAEE")
    ax.bar(df['Ticker'], df ['Std_dev'], color="#D48D3B")
    ax.set_title('Top 10 Most Volatile Stocks', color= 'Red', fontsize=12)
    ax.set_xlabel('Stock Name', color= "#181A96", fontsize=12)
    ax.set_ylabel('Standard Deviation', color= "#2A1794", fontsize=12)
    ax.legend(['Standard Deviation\n(Amount in Dollars($))'], loc='upper right', fontsize=6)
    ax.tick_params(axis='x', rotation=75, colors="#9B1542", labelsize=10)
    ax.tick_params(axis='y', colors="#9B1542", labelsize=10)
    plt.tight_layout()  # Ensures nothing gets cut off
    st.pyplot(plt)

#Cumulative Return for Top 5 Performing Stocks
if Cumulative_Return:
    st.markdown(
        "<h4 style='color:#020005; background-color:#3b7ead; padding:8px 12px; border-radius:6px; margin-bottom:16px;'>"
        "Cumulative Return for Top 5 Performing Stocks"
        "</h4>",    
    unsafe_allow_html=True
)
    mycursor.execute("""SELECT Ticker, Cumulative_amount FROM cumulative_return ORDER BY
                    Cumulative_amount DESC LIMIT 5""")
    data = mycursor.fetchall()
    df = pd.DataFrame(data, columns=['Ticker', 'Cumulative_amount'])

    fig, ax = plt.subplots(figsize=(6, 4), facecolor='#020005')  # Figure background black
    fig.patch.set_facecolor("#A1C0E7")
    ax.set_facecolor("#B0DAEE")
    ax.plot(df['Ticker'], df ['Cumulative_amount'], color="#D48D3B")
    ax.set_title('Top 5 Cumulative return of top 5 stocks', color= 'Red', fontsize=12)
    ax.set_xlabel('Stock Name', color= "#181A96", fontsize=6)
    ax.set_ylabel('Cumulative_amount', color= "#2A1794", fontsize=6)
    ax.legend(['Cumulative_amount\n(Amount in Dollars($))'], loc='upper right', fontsize=6)
    ax.tick_params(axis='x', rotation=75, colors="#9B1542", labelsize=6)
    ax.tick_params(axis='y', colors="#D12651", labelsize=6)
    plt.tight_layout()  # Ensures nothing gets cut off
    st.pyplot(plt)

#Sector-wise Performance
#Average Yearly Return by Sector
if yearly_returns:

    st.markdown(
        "<h4 style='color:#020005; background-color:#3b7ead; padding:8px 12px; border-radius:6px; margin-bottom:16px;'>"
        "Average Yearly Return by Sector"
        "</h4>",    
    unsafe_allow_html=True
)
    mycursor.execute("Select Sector, Yearly_Return_Percentage from Avg_Yearly_Return")
    data = mycursor.fetchall()
    df = pd.DataFrame(data, columns=['Sector', 'Yearly_Return_Percentage'])

    fig, ax = plt.subplots(figsize=(6, 4), facecolor='#020005')  # Figure background black
    fig.patch.set_facecolor("#A1C0E7")
    ax.set_facecolor("#B0DAEE")
    ax.bar(df['Sector'], df ['Yearly_Return_Percentage'], color="#D48D3B")
    ax.set_title('Average Yearly return by sector', color= 'Red', fontsize=12)
    ax.set_xlabel('Sector', color= "#181A96", fontsize=6)
    ax.set_ylabel('Yearly_Return_Percentage', color= "#2A1794", fontsize=6)
    ax.legend(['Yearly_Return\n(Values in Percentage(%))'], loc='upper center', fontsize=6)
    ax.tick_params(axis='x', rotation=75, colors="#9B1542", labelsize=6)
    ax.tick_params(axis='y', colors="#D12651", labelsize=6)
    plt.tight_layout()  # Ensures nothing gets cut off
    st.pyplot(plt)


#Correlation of the closing stocks

if Correlation:
    st.markdown(
        "<h4 style='color:#020005; background-color:#3b7ead; padding:8px 12px; border-radius:6px; margin-bottom:16px;'>"
        "Correlation of the closing all stocks"
        "</h4>",    
    unsafe_allow_html=True)

    #  Fetch data with Date included 
    mycursor.execute("SELECT Company, close, Date FROM stock_data")
    data = mycursor.fetchall()
    df = pd.DataFrame(data, columns=['Company', 'close', 'Date'])
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure 'Date' is datetime format

    #  Remove duplicates by averaging same-date entries 
    df = df.groupby(['Date', 'Company'], as_index=False)['close'].mean()

    #  Pivot: Date as index, Company as columns 
    df_pivot = df.pivot(index='Date', columns='Company', values='close')

    #  Compute correlation matrix 
    corr_matrix = df_pivot.corr()

    #  Plot heatmap 
    fig, ax = plt.subplots(figsize=(20, 15))  #  Better fit for Streamlit
    fig.patch.set_facecolor("#A1C0E7")

    sns_plot = sns.heatmap(
        corr_matrix,
        annot=False,
        cmap="coolwarm",
        linewidths=0.5,
        fmt=".2f",
        cbar_kws={'shrink': 0.8, 'aspect': 25, 'pad': 0.02},
        ax=ax
    )

    #  Colorbar styling 
    colorbar = sns_plot.collections[0].colorbar
    colorbar.ax.tick_params(labelsize=18)
    colorbar.ax.set_ylabel('Correlation Coefficient', fontsize=20)

    #  Axis labels and title 
    ax.set_title('Nifty 50: Correlation Matrix of Closing Prices', fontsize=24, color='black', pad=20)
    ax.set_xlabel('Ticker', fontsize=40, labelpad=10)
    ax.set_ylabel('Ticker', fontsize=40, labelpad=10)

    #  Tick label rotation and font 
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=16, ha='center')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=16, va='center')

    #  Adjust layout to avoid clipping 
    plt.tight_layout()

    #  Display in Streamlit 
    st.pyplot(fig)


#  Top 5 Gainers and Losers (Month-wise) 

if Gainers_Losers:
    st.markdown(
        "<h4 style='color:#020005; background-color:#3b7ead; padding:8px 12px; border-radius:6px; margin-bottom:16px;'>"
        "Top 5 Gainers and Losers (Month-wise)"
        "</h4>",    
        unsafe_allow_html=True
    )

    #  Fetch monthly return data 
    mycursor.execute("SELECT Month, Ticker, Monthly_Return_Percentage FROM monthly_stock_returns")
    data = mycursor.fetchall()
    df = pd.DataFrame(data, columns=['Month', 'Ticker', 'Monthly_Return_Percentage'])
    months = df['Month'].unique()

    #  Loop over each month 
    for month in months:
        st.write(f"##### Month: {month}")
        month_data = df[df['Month'] == month]

        top_gainers = month_data.nlargest(5, 'Monthly_Return_Percentage')
        top_losers = month_data.nsmallest(5, 'Monthly_Return_Percentage')

        #  Create side-by-side plots 
        fig, ax = plt.subplots(1, 2, figsize=(14, 6), facecolor='#020005')  # Background black
        fig.patch.set_facecolor("#A1C0E7")

        # Apply subplot-specific background
        for a in ax:
            a.set_facecolor("#E4F1FB")

        #  Top Gainers 
        sns.barplot(
        x='Ticker', y='Monthly_Return_Percentage',
        data=top_gainers, ax=ax[0], palette='Greens_r'
        )
        ax[0].set_title('Top 5 Gainers', fontsize=18, weight='bold', color='#004225')
        ax[0].set_xlabel('Ticker', fontsize=14)
        ax[0].set_ylabel('Monthly Return (%)', fontsize=14)
        ax[0].tick_params(axis='x', rotation=45, labelsize=11)
        ax[0].tick_params(axis='y', labelsize=11)

        #  Label every bar
        for container in ax[0].containers:
            ax[0].bar_label(container, fmt='%.2f', fontsize=10, padding=3)

        #Top Losers
        sns.barplot(
            x='Ticker', y='Monthly_Return_Percentage',
            data=top_losers, ax=ax[1], palette='Reds_r'
        )
        ax[1].invert_yaxis()
        ax[1].set_title('Top 5 Losers', fontsize=18, weight='bold', color='#6B0000')
        ax[1].set_xlabel('Ticker', fontsize=14)
        ax[1].set_ylabel('Monthly Return (%)', fontsize=14)
        ax[1].tick_params(axis='x', rotation=45, labelsize=11)
        ax[1].tick_params(axis='y', labelsize=11)

        # Label every bar
        for container in ax[1].containers:
            ax[1].bar_label(container, fmt='%.2f', fontsize=10, padding=3)


        #  Layout and display 
        plt.tight_layout()
        st.pyplot(fig)