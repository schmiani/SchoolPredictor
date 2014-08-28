USE school;
SELECT 
    *
FROM
    Final
WHERE
    2006_07_GRADE = ''
        AND 2007_08_GRADE = ''
        AND 2008_09_GRADE = ''
        AND 2009_10_GRADE = ''
        AND 2010_11_GRADE = ''
        AND 2011_12_GRADE = ''
        AND 2012_13_GRADE = '';

UPDATE Final 
SET 
    2013_14_SCORE_PRED = '', 2013_14_GRADE_PRED = ''
WHERE
    2006_07_GRADE = ''
        AND 2007_08_GRADE = ''
        AND 2008_09_GRADE = ''
        AND 2009_10_GRADE = ''
        AND 2010_11_GRADE = ''
        AND 2011_12_GRADE = ''
        AND 2012_13_GRADE = '';