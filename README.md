# TRUE LONGITUDINAL DATA FORMAT (LDF)

## Why this exists
There isn't an universally agreed upon longitudinal data file format. Longitudinal Data is often stored in seprated rows for each data entry which bloats the file size and causes uneccessary slowdown of data reading. Longitudinal data can also be stored in a dense table format; however, this can leads to a lot of empty cells for missing variables. Moreover, the ununiformity in longitudinal data format makes sharing and processing a longitudinal data file extremely cumbersome. This is am as-simple-as-possible attempt to standardize the data format for "true" longitudinal data in which each longitudinal variable is observed at different frequency and time intervals.

## General Infomration about LDF Data Format
file.LDF = {Metadata, Data}

Data structure is serialized and stored using python's _Pickle_ (or _cPickle_ when available) library. The data can also be stored in simple csv file for portability.

### Metadata
The first 2 lines in the metadata are reserved for header
Line 1 - format - format variable is a short string ("ldf") to make sure the data is of correct type.
Line 2 - temporalType specifies the type of temporal information the data use. This could be either REAL or FORMATED (More info below)

The rest of the metadata is simply a table, and is tab delimited. The first line is always reserved for header

| ID |  metavar1  |  metavar2  |  ... | metavarN |
|:---:|:----------:|:----------:|:----:|:--------:|
| id1 | value 1_1 | value 1_2 | ... | value 1_N |
| id2 | value 2_1 | value 2_2 | ... | value 2_N |
|... |||||

### Data
The data portion of ldf is also tab delimited. associated times and values are delimited using semi colon. There is no header.

ID | longitudinal_var_name1 | time;values

### Temporal Type
#### Real temporal type
Time point information is stored in the form of real numbers. There is no constraint on negative and/or fractional values in real time. This time value type provides temporal order and interval between observations in term of real  number

#### Formated temporal type
Time point information is stored in the form of formated datetime. In the case of formated temporal type,  

## Save to CSV

The data format can be stored as a csv file. When ldf data is exported to csv, there will be 2 associated files. 1 - the metadata and 2 - the data itself

## Other information
##### NOTE: While LDF format is intended to use on true longitudinal data where each longitudinal variables is sampled at different frequency. It will also work for regular timeseries data. However, this is probably not desirable since the data could be stored more compactly  using a regular table format.