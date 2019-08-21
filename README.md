# ISO-8601_time_converter
A simple time conversion function written in Python. 

## time_convert(iso_time, offset=0)
The time_convert() function takes an ISO 8601 formatted datetime string and an optional time zone offset integer as input and returns timezone converted datetime sting in a more human readable format. 

## Input
```python
time = "2020-03-01-T00:33:25.000Z"
print(time_convert(time, -1))
time = "2019-03-01-T00:33:25.000Z"
print(time_convert(time, -1))
time = "2020-01-01-T00:33:25.000Z"
print(time_convert(time, -1))
time = "2020-02-28-T15:33:25.000Z"
print(time_convert(time, +12))
time = "2020-12-31-T23:33:25.000Z"
print(time_convert(time, +1))
```

## Output
```
February 29, 2020, 11:33 PM
February 28, 2019, 11:33 PM
December 31, 2019, 11:33 PM
February 29, 2020, 3:33 AM
January 1, 2021, 12:33 AM
```
