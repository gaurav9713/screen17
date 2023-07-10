SELECT
    tpep_dropoff_datetime,
    trip_distance ,
    AVG(trip_distance) OVER (ORDER BY tpep_dropoff_datetime ROWS BETWEEN 44 PRECEDING AND CURRENT ROW) AS rolling_average_45_days
FROM
    yellow_trip yt
ORDER BY
    tpep_dropoff_datetime;