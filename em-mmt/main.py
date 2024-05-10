from em_mmt.em_mmt import MMT

data_dir = 'DM4_Sales'
dma_fName = 'DM4_Sales_Q1_V3.csv'
gmm_metric = "Trials"
corr_thresh = 0.6
pval_threshold = 0.1
pre_period_start = '2018-01-01' 
pre_period_end = '2018-07-29'
post_period_start = '2018-07-30' 
post_period_end = '2018-08-19'
gmm_rank = 3
initials = 'mdh'
campaign = 'DM4_Test'
brand = 'UP'
gmm_plots = False
parallel_processing = True

# First create the Object
mmt = MMT()

# Then call the object's function
mm = mmt.get_market_matches(data_dir = data_dir, 
                            dma_fName = dma_fName, 
                            gmm_metric = gmm_metric, 
                            corr_thresh = corr_thresh, 
                            pval_threshold = pval_threshold, 
                            pre_period_start = pre_period_start, 
                            pre_period_end = pre_period_end, 
                            post_period_start = post_period_start, 
                            post_period_end = post_period_end, 
                            gmm_rank = gmm_rank, 
                            initials = initials, 
                            campaign = campaign, 
                            brand = brand, 
                            gmm_plots = False, 
                            parallel_processing= True)

mm.head()
