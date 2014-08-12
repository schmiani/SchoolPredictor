USE school;
CREATE TABLE EMS_All_Info AS
    SELECT 
        DBN
    FROM
        EMS_2013_All 
    UNION SELECT 
        DBN
    FROM
        EMS_2012_All 
    UNION SELECT 
        DBN
    FROM
        EMS_2011_All 
    UNION SELECT 
        DBN
    FROM
        EMS_2010_All 
    UNION SELECT 
        DBN
    FROM
        EMS_2009_All 
    UNION SELECT 
        DBN
    FROM
        EMS_2008_All 
    UNION SELECT 
        DBN
    FROM
        EMS_2007_All;
ALTER TABLE EMS_All_Info ADD School varchar(100);
UPDATE EMS_All_Info,
    EMS_2007_All 
SET 
    EMS_All_Info.School = EMS_2007_All.School
WHERE
    EMS_All_Info.DBN = EMS_2007_All.DBN;
UPDATE EMS_All_Info,
    EMS_2008_All 
SET 
    EMS_All_Info.School = EMS_2008_All.School
WHERE
    EMS_All_Info.DBN = EMS_2008_All.DBN;
UPDATE EMS_All_Info,
    EMS_2009_All 
SET 
    EMS_All_Info.School = EMS_2009_All.School
WHERE
    EMS_All_Info.DBN = EMS_2009_All.DBN;
UPDATE EMS_All_Info,
    EMS_2010_All 
SET 
    EMS_All_Info.School = EMS_2010_All.School
WHERE
    EMS_All_Info.DBN = EMS_2010_All.DBN;
UPDATE EMS_All_Info,
    EMS_2011_All 
SET 
    EMS_All_Info.School = EMS_2011_All.School
WHERE
    EMS_All_Info.DBN = EMS_2011_All.DBN;
UPDATE EMS_All_Info,
    EMS_2012_All 
SET 
    EMS_All_Info.School = EMS_2012_All.School
WHERE
    EMS_All_Info.DBN = EMS_2012_All.DBN;
UPDATE EMS_All_Info,
    EMS_2013_All 
SET 
    EMS_All_Info.School = EMS_2013_All.School
WHERE
    EMS_All_Info.DBN = EMS_2013_All.DBN;

ALTER TABLE EMS_All_Info ADD School_Type varchar(10);
UPDATE EMS_All_Info,
    EMS_2007_All 
SET 
    EMS_All_Info.School_Type = EMS_2007_All.School_Type
WHERE
    EMS_All_Info.DBN = EMS_2007_All.DBN;
UPDATE EMS_All_Info,
    EMS_2008_All 
SET 
    EMS_All_Info.School_Type = EMS_2008_All.School_Type
WHERE
    EMS_All_Info.DBN = EMS_2008_All.DBN;
UPDATE EMS_All_Info,
    EMS_2009_All 
SET 
    EMS_All_Info.School_Type = EMS_2009_All.School_Type
WHERE
    EMS_All_Info.DBN = EMS_2009_All.DBN;
UPDATE EMS_All_Info,
    EMS_2010_All 
SET 
    EMS_All_Info.School_Type = EMS_2010_All.School_Type
WHERE
    EMS_All_Info.DBN = EMS_2010_All.DBN;
UPDATE EMS_All_Info,
    EMS_2011_All 
SET 
    EMS_All_Info.School_Type = EMS_2011_All.School_Type
WHERE
    EMS_All_Info.DBN = EMS_2011_All.DBN;
UPDATE EMS_All_Info,
    EMS_2012_All 
SET 
    EMS_All_Info.School_Type = EMS_2012_All.School_Type
WHERE
    EMS_All_Info.DBN = EMS_2012_All.DBN;
UPDATE EMS_All_Info,
    EMS_2013_All 
SET 
    EMS_All_Info.School_Type = EMS_2013_All.School_Type
WHERE
    EMS_All_Info.DBN = EMS_2013_All.DBN;