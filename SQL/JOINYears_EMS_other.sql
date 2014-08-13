USE school;
CREATE OR REPLACE VIEW AllYears_EMS_other AS
    SELECT 
        a.DBN, a.School, a.School_Type,
        b.Math_Average_Proficiency AS 2012_13_MATH,
		b.ELA_Average_Proficiency AS 2012_13_ELA,
        c.Math_Average_Proficiency AS 2011_12_MATH,
        c.ELA_Average_Proficiency AS 2011_12_ELA,
        d.Math_Average_Proficiency AS 2010_11_MATH,
        d.ELA_Average_Proficiency AS 2010_11_ELA,
		e.Math_Median_Proficiency AS 2009_10_MATH,
		e.ELA_Median_Proficiency AS 2009_10_ELA,
		f.Math_Median_Proficiency AS 2008_09_MATH,
		f.ELA_Median_Proficiency AS 2008_09_ELA,
		g.Math_Median_Proficiency AS 2007_08_MATH,
		g.ELA_Median_Proficiency AS 2007_08_ELA,
		h.Math_Median_Proficiency AS 2006_07_MATH,
		h.ELA_Median_Proficiency AS 2006_07_ELA
    FROM
        EMS_All_Info a
            LEFT JOIN
        EMS_2013_All b ON a.DBN = b.DBN
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