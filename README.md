# QuantResearchEnvironment
Infrastructure for my financial modeling and research work, including statistical software, custom financial data infrastructure, and visualization utilities.

## The function of different directories 

- `data/` : parquet + csv files for fast loading of historical data 

    - `market/` : prices and other data related to financial securities and commodities
    - `raw/` : unprocessed data dumped here to process and structure 

- `data_connectors/` : infrastructure to pull data from web sources 

- `db/` : CRUD functionality for database and excel data storage

- `mathematics/` : implementation of computational methods to help with strategy development 
    - `linalg/` : linear system solvers and modern lin-alg algorithms 
    - `numerical/` : interpolation, numerical diff. and int.
    - `optimization/` : efficient numerical optimization routines 
    - `stats/` : hypothesis testing, regression and stats models utils 
        - `hyptest` : hypothesis/statistical significance testing functions 
        - `linear_models` : OLS, ridge, lasso, and other regression approaches 
        - `stochastic` : markov chain, bayes net, and other probabilistic algorithms
        - `timeseries` : ADF, GARCH, Engle-granger, and other time-series functions

- `modeling/` : implementations of quant financial models
    - `factor/` : CAPM, Fama-French and other linear factor models
    - `ml/` : routines for PCA, random forests / gradient boosters and other ML algorithms
    - `sde/` : GBM, OU and other base models for stochastic process modeling 

- `sim/` : backtesting and simulation utilities 
    - `backtest/` : robust class for both vectorized and event driven backtesting

- `vis/` : figures and visualization utils
