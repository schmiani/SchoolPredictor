USE school;
CREATE OR REPLACE VIEW AllYears_EMS AS
    SELECT 
        a.DBN, a.School, a.School_Type,
        b.Overall_Score AS 2012_13_SCORE,
		b.Overall_Grade AS 2012_13_GRADE,
        c.Overall_Score AS 2011_12_SCORE,
        c.Overall_Grade AS 2011_12_GRADE,
        d.Overall_Score AS 2010_11_SCORE,
        d.Overall_Grade AS 2010_11_GRADE,
		e.Overall_Score AS 2009_10_SCORE,
		e.Grade AS 2009_10_GRADE,
		f.Overall_Score AS 2008_09_SCORE,
		f.Grade AS 2008_09_GRADE,
		g.Overall_Score AS 2007_08_SCORE,
		g.Grade AS 2007_08_GRADE,
		h.Overall_Score AS 2006_07_SCORE,
		h.Grade AS 2006_07_GRADE
    FROM
        EMS_All_Info a
            LEFT JOIN
        EMS_2013_Summary b ON a.DBN = b.DBN
            LEFT JOIN
        EMS_2012_All c ON a.DBN = c.DBN
            LEFT JOIN
        EMS_2011_All d ON a.DBN = d.DBN
			LEFT JOIN
        EMS_2010_All e ON a.DBN = e.DBN
			LEFT JOIN
        EMS_2009_All f ON a.DBN = f.DBN
			LEFT JOIN
        EMS_2008_All g ON a.DBN = g.DBN
			LEFT JOIN
        EMS_2007_All h ON a.DBN = h.DBN;
SELECT COUNT(*) FROM allyears_EMS;