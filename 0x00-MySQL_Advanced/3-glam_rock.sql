-- File: 3-glam_rock.sql
SELECT
    band_name,
    IF(split IS NULL OR split = '', 2022 - formed, split - formed) AS lifespan
FROM
    bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;
