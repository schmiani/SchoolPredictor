USE school;
SELECT Overall_Score FROM EMS_2007_All WHERE Overall_Score = '';
UPDATE EMS_2007_All SET Overall_Score = NULL WHERE Overall_Score = '';
SELECT Overall_Score FROM EMS_2008_All ORDER BY Overall_Score ASC LIMIT 10;
UPDATE EMS_2008_All SET Overall_Score = NULL WHERE Overall_Score = '';
SELECT Overall_Score FROM EMS_2009_All ORDER BY Overall_Score ASC LIMIT 10;
UPDATE EMS_2009_All SET Overall_Score = NULL WHERE Overall_Score = '';
SELECT Overall_Score FROM EMS_2010_All ORDER BY Overall_Score ASC LIMIT 10;
UPDATE EMS_2010_All SET Overall_Score = NULL WHERE Overall_Score = '';
SELECT Overall_Score FROM EMS_2011_All ORDER BY Overall_Score ASC LIMIT 10;
UPDATE EMS_2011_All SET Overall_Score = NULL WHERE Overall_Score = '.';
SELECT Overall_Score FROM EMS_2012_All ORDER BY Overall_Score ASC LIMIT 10;
UPDATE EMS_2012_All SET Overall_Score = NULL WHERE Overall_Score = '';
SELECT Overall_Score FROM EMS_2013_Summary ORDER BY Overall_Score ASC LIMIT 10;
UPDATE EMS_2013_Summary SET Overall_Score = NULL WHERE Overall_Score = '.';

SELECT Overall_Score FROM EMS_2007_All WHERE Overall_Score LIKE '%(%)%';
UPDATE EMS_2007_All SET Overall_Score = '0' WHERE Overall_Score LIKE '%(%)%';

SELECT School_Type FROM EMS_2007_All WHERE School_Type = 'MIDDLE SCHOOL';
UPDATE EMS_2007_All SET School_Type = 'Middle' WHERE School_Type = 'MIDDLE SCHOOL';
SELECT School_Type FROM EMS_2007_All WHERE School_Type = 'ELEMENTARY';
UPDATE EMS_2007_All SET School_Type = 'Elementary' WHERE School_Type = 'ELEMENTARY';

SELECT School_Type FROM EMS_2008_All WHERE School_Type = 'MIDDLE SCHOOL';
UPDATE EMS_2008_All SET School_Type = 'Middle' WHERE School_Type = 'MIDDLE SCHOOL';
SELECT School_Type FROM EMS_2008_All WHERE School_Type = 'ELEMENTARY';
UPDATE EMS_2008_All SET School_Type = 'Elementary' WHERE School_Type = 'ELEMENTARY';

UPDATE EMS_2007_All SET Math_Median_Proficiency = NULL WHERE Math_Median_Proficiency = '';
UPDATE EMS_2007_All SET ELA_Median_Proficiency = NULL WHERE ELA_Median_Proficiency = '';
UPDATE EMS_2008_All SET Math_Median_Proficiency = NULL WHERE Math_Median_Proficiency = '';
UPDATE EMS_2008_All SET ELA_Median_Proficiency = NULL WHERE ELA_Median_Proficiency = '';
UPDATE EMS_2009_All SET Math_Median_Proficiency = NULL WHERE Math_Median_Proficiency = '';
UPDATE EMS_2009_All SET ELA_Median_Proficiency = NULL WHERE ELA_Median_Proficiency = '';
UPDATE EMS_2010_All SET Math_Median_Proficiency = NULL WHERE Math_Median_Proficiency = '';
UPDATE EMS_2010_All SET ELA_Median_Proficiency = NULL WHERE ELA_Median_Proficiency = '';
UPDATE EMS_2011_All SET Math_Average_Proficiency = NULL WHERE Math_Average_Proficiency = '';
UPDATE EMS_2011_All SET ELA_Average_Proficiency = NULL WHERE ELA_Average_Proficiency = '';
UPDATE EMS_2012_All SET Math_Average_Proficiency = NULL WHERE Math_Average_Proficiency = '';
UPDATE EMS_2012_All SET ELA_Average_Proficiency = NULL WHERE ELA_Average_Proficiency = '';
UPDATE EMS_2013_All SET Math_Average_Proficiency = NULL WHERE Math_Average_Proficiency = '';
UPDATE EMS_2013_All SET ELA_Average_Proficiency = NULL WHERE ELA_Average_Proficiency = '';