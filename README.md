# TRUE LONGITUDINAL DATA FORMAT (LDF)

## Why this exists
Longitudinal datasets are not very portable. There isn't an universally agreed upon longitudinal data file format. Longitudinal data are often stored in separated rows for each data entry which bloats the file with repetitive elements and causes unnecessary inefficiency in data reading. Longitudinal data are also stored in a dense table format; however, this leads to excessive empty cells for missing longitudinal variable entries. Other solutions are sometime very framework dependent. Moreover, the in-uniformity in longitudinal data format makes sharing and processing different longitudinal data files extremely cumbersome. This is a as-simple-as-possible language/framework agnostic solution to standardize the data format for "true" multivariate longitudinal data in which each longitudinal variable is observed at different frequency and time intervals.

## About LDF package
This package provides standard routines for manipulating the ldf data format including converting some other data format into ldf, merging, joining and splitting different ldf dataset. The package also contain convenient methods to read data directly into pandas matrices. Documentation can be found here

## General Information about LDF Data Format
file.LDF = {Metadata, Data}

Data structure is serialized and stored using python's _Pickle_ (or _cPickle_ when available) library. The data can also be stored in simple csv file for portability.

### Metadata
The first 3 lines in the metadata are reserved for header

Line 1 - format - format variable is a short string ("ldf") to make sure the data is of correct type.

Line 2 - temporalType specifies the type of temporal information the data use. This could be either REAL or FORMATTED (More info below)

Line 3 - Reference date (if Formatted Type) and Empty (if Real Type)

The rest of the metadata is simply a table, and is tab delimited. The first line of the meta table is always reserved for header

| ID |  metavar1  |  metavar2  |  ... | metavarN |
|:---:|:----------:|:----------:|:----:|:--------:|
| id1 | value 1_1 | value 1_2 | ... | value 1_N |
| id2 | value 2_1 | value 2_2 | ... | value 2_N |
|... |||||
 
 At the end of the metadata table, There is a separator which consists of 10 underscores "__________" follow by a list of variables and their data types. The table is tab delimited and there is no header. If the data is of nominal type, a list of nominal values needs to be supplied - this list is semi-colon delimited.
 
 | VarName | Datatype | Nominal Value |
 |:-------:|:--------:|:-------------:|
 | Weight  | numeric  ||
 | BMI     | numeric  ||
 | preference  | nominal  |donut;cake;bread |
 |...|||
 
### Data
The data portion of ldf is also tab delimited. associated times and values are delimited using semi colon. There is no header.

ID | longitudinal_var_name1 | Data type | time;values

Data can be of 2 types - numeric and nominal. Below is an example of sample PT0001

PT0001      BMI      0;23.4     3.5;24.1      8.9;23.9      ...

PT0001      Weight     0;156.00      1.2;165.10      3.5;159.45      ...

PT0001      preference  0;0     0.2;1       0.75;2          ...

### Temporal Type
#### Real temporal type
Time point information is stored in the form of real numbers. There is no constraint on negative and/or fractional values in real time. This time value type provides temporal order and interval between observations in term of real  number

#### Formatted temporal type
Time point information is stored in the form of datetime ISO 8601 format (‘YYYY-MM-DD’). In the case of formatted temporal Type. There exist a reference date in the meta data and the rest of the data will be store in Real increments or decrements of the reference date.  

## Save to CSV

The data format can be stored as a csv file. When ldf data is exported to csv, there will be 2 associated files. 1 - the metadata and 2 - the data itself

## Other information
##### NOTE: While LDF format is intended to use on true longitudinal data where each longitudinal variable is sampled at different frequency. LDF format will also work for storing regular time series data. However, this is probably not preferable since the data could be stored more efficently using a regular dense table format.
