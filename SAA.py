from io import StringIO
import pandas as pd
import requests
import numpy as np

url = "https://www.ishares.com/us/products/239600/ishares-msci-acwi-etf/1467271812596.ajax?fileType=csv&fileName=ACWI_holdings&dataType=fund"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

text = response.text

# iShares coloca disclaimer nas primeiras linhas
csv_start = text.find("Ticker")
clean_csv = text[csv_start:]

acwi = pd.read_csv(StringIO(clean_csv))
acwi_filtrada = acwi.loc[acwi["Weight (%)"]>0.05]
concentracao_acwi = acwi_filtrada.groupby("Location").sum()["Weight (%)"]
concentracao_acwi = pd.DataFrame(concentracao_acwi)
print(concentracao_acwi.index)

etfs_por_pais = {
    "Australia": "EWA",     # iShares MSCI Australia ETF (EWA) :contentReference[oaicite:1]{index=1}
    "Belgium": "EWK",       # iShares MSCI Belgium ETF (EWK) :contentReference[oaicite:2]{index=2}
    "Brazil": "EWZ",        # iShares MSCI Brazil ETF (EWZ) :contentReference[oaicite:3]{index=3}
    "Canada": "EWC",        # iShares MSCI Canada ETF (EWC) :contentReference[oaicite:4]{index=4}
    "China": "FXI",         # iShares FTSE China Large-Cap ETF (FXI) :contentReference[oaicite:5]{index=5}
    "Denmark": "EDEN",      # iShares MSCI Denmark ETF (EDEN) :contentReference[oaicite:6]{index=6}
    "Finland": "EFNL",      # iShares MSCI Finland ETF (EFNL) :contentReference[oaicite:7]{index=7}
    "France": "EWQ",        # iShares MSCI France ETF (EWQ) :contentReference[oaicite:8]{index=8}
    "Germany": "EWG",       # iShares MSCI Germany ETF (EWG) :contentReference[oaicite:9]{index=9}
    "Hong Kong": "EWH",     # iShares MSCI Hong Kong ETF (EWH) :contentReference[oaicite:10]{index=10}
    "India": "INDY",        # iShares India 50 ETF (INDY) – maior foco em ações indianas :contentReference[oaicite:11]{index=11}
    "Italy": "EWI",         # iShares MSCI Italy ETF (EWI) :contentReference[oaicite:12]{index=12}
    "Japan": "EWJ",         # iShares MSCI Japan ETF (EWJ) :contentReference[oaicite:13]{index=13}
    "Korea (South)": "EWY", # iShares MSCI Korea ETF (EWY) :contentReference[oaicite:14]{index=14}
    "Netherlands": "EWN",   # iShares MSCI Netherlands ETF (EWN) :contentReference[oaicite:15]{index=15}
    "Saudi Arabia": None,   # iShares não tem ETF país-específico típico listado nos EUA
    "Singapore": "EWS",     # iShares MSCI Singapore ETF (EWS) :contentReference[oaicite:16]{index=16}
    "South Africa": "EZA",  # iShares MSCI South Africa ETF (EZA) – país emergente :contentReference[oaicite:17]{index=17}
    "Spain": "EWP",         # iShares MSCI Spain ETF (EWP) :contentReference[oaicite:18]{index=18}
    "Sweden": "EWD",        # iShares MSCI Sweden ETF (EWD) :contentReference[oaicite:19]{index=19}
    "Switzerland": "EWL",   # iShares MSCI Switzerland ETF (EWL) :contentReference[oaicite:20]{index=20}
    "Taiwan": "EWT",        # iShares MSCI Taiwan ETF (EWT) :contentReference[oaicite:21]{index=21}
    "United Kingdom": "EWU",# iShares MSCI United Kingdom ETF (EWU) :contentReference[oaicite:22]{index=22}
    "United States": "IVV" # iShares MSCI USA ETF (EUSA) ou similar amplo mercado dos EUA
}

concentracao_acwi["ETFs"] = concentracao_acwi.index.map(etfs_por_pais)

url2 = "https://www-ishares-com.translate.goog/uk/individual/en/products/291773/fund/1506575576011.ajax?fileType=csv&fileName=AGGG_holdings&dataType=fund&_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc"

response2 = requests.get(url2,headers)


text2 = response2.text

# iShares coloca disclaimer nas primeiras linhas
csv_start = text2.find("Ticker")
clean_csv = text2[csv_start:]

aggg = pd.read_csv(StringIO(clean_csv))

# Regras para Renda Fixa

dm_em_map = {
    # Developed Markets
    "United States": "DM",
    "Canada": "DM",
    "United Kingdom": "DM",
    "Germany": "DM",
    "France": "DM",
    "Italy": "DM",
    "Spain": "DM",
    "Netherlands": "DM",
    "Belgium": "DM",
    "Switzerland": "DM",
    "Sweden": "DM",
    "Denmark": "DM",
    "Norway": "DM",
    "Finland": "DM",
    "Ireland": "DM",
    "Austria": "DM",
    "Portugal": "DM",
    "Greece": "DM",
    "Japan": "DM",
    "Australia": "DM",
    "New Zealand": "DM",
    "Singapore": "DM",
    "Hong Kong": "DM",
    "Luxembourg": "DM",
    "Iceland": "DM",

    # Emerging Markets
    "China": "EM",
    "India": "EM",
    "Brazil": "EM",
    "Mexico": "EM",
    "Chile": "EM",
    "Colombia": "EM",
    "Peru": "EM",
    "South Africa": "EM",
    "Saudi Arabia": "EM",
    "Qatar": "EM",
    "United Arab Emirates": "EM",
    "Kuwait": "EM",
    "Bahrain": "EM",
    "Oman": "EM",
    "Indonesia": "EM",
    "Malaysia": "EM",
    "Thailand": "EM",
    "Philippines": "EM",
    "Taiwan": "EM",
    "Korea (South)": "EM",
    "Israel": "EM",
    "Poland": "EM",
    "Czech Republic": "EM",
    "Hungary": "EM",
    "Slovak Republic": "EM",
    "Slovenia": "EM",
    "Romania": "EM",
    "Croatia (Hrvatska)": "EM",
    "Bulgaria": "EM",
    "Latvia": "EM",
    "Lithuania": "EM",
    "Estonia": "EM",
    "Kazakhstan": "EM",
    "Morocco": "EM",
    "Nigeria": "EM",
    "Ecuador": "EM",
    "Panama": "EM",
    "Uruguay": "EM",
    "Paraguay": "EM",
    "Gabon": "EM",

    # Casos especiais
    "Supranational": "SUPRA",
    "Cayman Islands": "OFFSHORE",
    "Bermuda": "OFFSHORE",
    "Jersey": "OFFSHORE",
    "Guernsey": "OFFSHORE",
    "Isle of Man": "OFFSHORE",
    "Macau": "OFFSHORE",
    "Andorra": "OFFSHORE",
}

aggg['Market Class'] = aggg['Location'].map(dm_em_map)


gov_corp_map = {
    # Government / Public
    "Treasuries": "GOV",
    "Sovereign": "GOV",
    "Government Guaranteed": "GOV",
    "Government Sponsored": "GOV",
    "Agency Fixed Rate": "GOV",
    "Agency CMBS": "GOV",
    "Mortgage Collateralized": "GOV",
    "Public Sector Collateralized": "GOV",
    "Local Authority": "GOV",
    "Supranational": "GOV",

    # Corporate / Private
    "Owned No Guarantee": "CORP",
    "Non-Agency CMBS": "CORP",
    "Hybrid Collateralized": "CORP",
    "Whole Business": "CORP",

    # Corporate Sectors
    "Banking": "CORP",
    "Insurance": "CORP",
    "Finance Companies": "CORP",
    "Brokerage/Asset Managers/Exchanges": "CORP",
    "Financial Other": "CORP",
    "Reits": "CORP",

    "Energy": "CORP",
    "Electric": "CORP",
    "Natural Gas": "CORP",
    "Utility Other": "CORP",
    "Stranded Cost Utility": "CORP",

    "Technology": "CORP",
    "Communications": "CORP",
    "Capital Goods": "CORP",
    "Transportation": "CORP",
    "Industrial Other": "CORP",
    "Basic Industry": "CORP",

    "Consumer Cyclical": "CORP",
    "Consumer Non-Cyclical": "CORP",

    # Caixa / derivativos
    "Cash and/or Derivatives": "CASH"
}

aggg['Asset Class'] = aggg['Sector'].map(gov_corp_map)

etf_factor_map = {
    # Developed Markets — Government — IG
    "DM_GOV_IG_SHORT": "SHY",
    "DM_GOV_IG_MID":   "IEF",
    "DM_GOV_IG_LONG":  "TLT",

    # Developed Markets — Corporate — IG
    "DM_CORP_IG_SHORT": "IGSB",
    "DM_CORP_IG_MID":   "LQD",
    "DM_CORP_IG_LONG":  "IGLB",

    # Emerging Markets — Government
    "EM_GOV_IG_MID": "EMB",
    "EM_GOV_IG_LONG": "EMB",   # proxy único (duration média-longa)

    # Emerging Markets — Corporate
    "EM_CORP_IG_MID": "CEMB",
    "EM_CORP_HY_MID": "HYEM",

    # High Yield DM
    "DM_CORP_HY_SHORT": "SHYG",
    "DM_CORP_HY_MID":   "HYG",

    # Inflation / Linkers (opcional)
    "DM_GOV_IG_INFL": "TIP",

    # Cash
    "CASH": "SHV"
}



def infer_ig_hy(row):
    if row["Asset Class"] == "GOV":
        return "IG"

    price = row["Price"]
    dur = row["Duration"]

    # Ajuste simples por duration
    if price < 80 and dur < 7:
        return "HY"
    if price < 70:
        return "HY"
    return "IG"

aggg["IG_HY_EST"] = aggg.apply(infer_ig_hy, axis=1)


def classify_duration(x):
    if x < 3:
        return "SHORT"
    elif x < 7:
        return "MID"
    else:
        return "LONG"

aggg["Duration Class"] = aggg["Duration"].apply(classify_duration)


aggg['Factor'] = (
    aggg['Market Class'] + "_" +
    aggg['Asset Class'] + "_" +
    aggg['IG_HY_EST'] + "_" +
    aggg['Duration Class']
    )


aggg['ETFs'] = aggg['Factor'].map(etf_factor_map)
aggg['ETFs'].replace(np.nan,'AGG',inplace=True)


concentracao_aggg = aggg.groupby('ETFs').sum()["Weight (%)"]
