import unittest
import cgitb


class TestDataSource(unittest.TestCase):
	
	db_source = DataSource()
	#for testing purpouses I will rely on several specific datapoints hardcoded
	#into the test code, here are the databse entries for the particular objects
	#I will be testing so it is clear to see what I am emulating in code

	#Bill example = (100, 109, 188, datetime.date(2005, 7, 14), 'amendment', 'On
	#the Amendment S.Amdt. 1222 to H.R. 2360 (Department of Homeland Security
	#Appropriations Act, 2006)', [300001, 300005, 300006, 300008, 300009,
	#300011, 300016, 300018, 300019, 300022, 300026, 300028, 300032, 300034,
	#300037, 300038, 300042, 300043, 300051, 300056, 300057, 300058, 300059,
	#300060, 300061, 300063, 300064, 300065, 300066, 300067, 300068, 300076,
	#300078, 300077, 400629, 300080, 300081, 300082, 300084, 400619, 300086,
	#300087, 300093, 300100], [300002, 300003, 300004, 300007, 300010, 300013,
	#300014, 300015, 400054, 300020, 300021, 400576, 300023, 300024, 300025,
	#300027, 300029, 300030, 300033, 300035, 300036, 300040, 300041, 300045,
	#300047, 300048, 300049, 300050, 300052, 300054, 300055, 400194, 300062,
	#300070, 400621, 300071, 300072, 300075, 300083, 300085, 300088, 300089,
	#300090, 300091, 300092, 300094, 300095, 300096, 300097, 400546, 400418,
	#300098, 300099], [], [400105, 300069, 300073])

	#senator example =




	test_billnv = Bill([100, 109, 188, datetime'2005-07-14 18:53:00', 'amendment', 'On the Amendment S.Amdt. 1222 to H.R. 2360 (Department of Homeland Security Appropriations Act, 2006)'])

	#note, this is not entirely accurate as what db_source really passes to the
	#constructor are lists of senator objects but in this case it is still
	#possible to test by comparing the id integer to senator.getId()
	test_billwv = Bill(100, 109, 188, datetime.date(2005, 7, 14), 'amendment', 'On the Amendment S.Amdt. 1222 to H.R. 2360 (Department of Homeland Security Appropriations Act, 2006)', [300001, 300005, 300006, 300008, 300009, 300011, 300016, 300018, 300019, 300022, 300026, 300028, 300032, 300034, 300037, 300038, 300042, 300043, 300051, 300056, 300057, 300058, 300059, 300060, 300061, 300063, 300064, 300065, 300066, 300067, 300068, 300076, 300078, 300077, 400629, 300080, 300081, 300082, 300084, 400619, 300086, 300087, 300093, 300100], [300002, 300003, 300004, 300007, 300010, 300013, 300014, 300015, 400054, 300020, 300021, 400576, 300023, 300024, 300025, 300027, 300029, 300030, 300033, 300035, 300036, 300040, 300041, 300045, 300047, 300048, 300049, 300050, 300052, 300054, 300055, 400194, 300062, 300070, 400621, 300071, 300072, 300075, 300083, 300085, 300088, 300089, 300090, 300091, 300092, 300094, 300095, 300096, 300097, 400546, 400418, 300098, 300099], [], [400105, 300069, 300073])


	## testing that GetBill does indeed return the expectd bill object
	testGetBill():
		actual = db_source.getBill(100)
		assert test_billnv.getId()==actual.getId()
		assert test_billnv.getSession()==actual.getSession()
		assert test_billnv.getRoll()==actual.getRoll()
		assert test_billnv.getVoteDate()==actual.getVoteDate()
		assert test_billnv.get()==actual.getRoll()









	if __name__ == '__main__':
    	unittest.main()
