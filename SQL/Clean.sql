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