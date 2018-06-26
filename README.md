
#TRUE LONGITUDINAL DATA FORMAT (LDF)

##Why this exists

##General Data Format
file.LDF = {Metadata, Data, format, temporalType}

Data structure is serialized and stored using python's _Pickle_ (or _cPickle_ when available) library

###Metadata
The metadata portion of ldf is simply a table, and is tab delimited. The first line is always reserved for header

| ID |  metavar1  |  metavar2  |  ... | metavarN |
|:---:|:----------:|:----------:|:----:|:--------:|
| id1 | value 1_1 | value 1_2 | ... | value 1_N |
| id2 | value 2_1 | value 2_2 | ... | value 2_N |
|... |
###Data
The data portion of ldf is also tab delimited. associated times and values are delimited using semi colon. There is no header

ID | longitudinal_var_name1 | time1;value1 | time

###Format and Temporal Type

Format variable is a short string to make sure 

## Other info
##### NOTE: While LDF format is intended to use on true longitudinal data where each longitudinal variables is sampled at different frequency. It will also work for regular timeseries data. However, this is probably not desirable since the data could be stored more compactly  using a regular table format.