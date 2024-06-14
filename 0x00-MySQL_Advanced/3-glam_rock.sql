-- File: 3-glam_rock.sql
SELECT
    band_name,
    -- Calculate lifespan: if 'split' is not null use the year difference to 2022; otherwise use 'split' year minus 'formed' year
    IF(split IS NULL OR split = '', 2022 - formed, split - formed) AS lifespan
FROM
    bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;
