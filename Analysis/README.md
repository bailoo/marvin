# Analysis of Deal Information.

## Dataset

`CSV Data/ArtistsMapping.csv`: Mapping of Artists ID to (Category and ProfileURL). <br>
`CSV Data/deal-details-infomation.csv`: Deals Data fetched from Pipedrive using `DealsDetails.py`. <br>
`CSV Data/updated-deal-details-infomation.csv`: Cleaned and Parsed version of `deal-details-infomation.csv`. <br>
`CSV Data/PYR.csv`: Data of only Post Your Requirements Deals. <br>

Both `deal-details-infomation.csv` & `updated-deal-details-infomation.csv` contains <b>Artists_Pitched</b> columns which represents the Artists Pitched to the Client on that Deal and contains the <b>ProfileURL</b> of the Artists Pitched.

--

## Notebook

To run & replicate the Notebook along with all the results.<br>

```shell
cd marvin/Analysis
jupyter notebook
```
