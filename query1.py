from data.users import User
from data import db_session


db_session.global_init('database/mars_explorer.db')

sess = db_session.create_session()

capitan = User()
capitan.surname = 'scott'
capitan.name = 'Redley'
capitan.age = 21
capitan.position = 'capitan'
capitan.speciality = 'esearch engineer'
capitan.address = 'module_1'
capitan.email = 'scott_chief@mars.org'
capitan.hashed_password = 'asrdfcgvhbjnkm'

sess.add(capitan)

capitan = User()
capitan.surname = '312321'
capitan.name = '312312'
capitan.age = 21
capitan.position = 'user'
capitan.speciality = 'engineer'
capitan.address = 'module_3012309123'
capitan.email = 'email_email_email@emal.emmail'
capitan.hashed_password = 'l[dkfwekf;asd'

sess.add(capitan)

capitan = User()
capitan.surname = 'alex'
capitan.name = 'alexov'
capitan.age = 25
capitan.position = 'user'
capitan.speciality = 'programmer'
capitan.address = 'module_1313'
capitan.email = 'alex_2008@mars.aaaaaaa'
capitan.hashed_password = '12331231'

sess.add(capitan)

capitan = User()
capitan.surname = 'Andrey'
capitan.name = 'Andreev'
capitan.age = 32
capitan.position = 'user'
capitan.speciality = 'testerr'
capitan.address = 'module_4'
capitan.email = 'scott_chief2@mars.org'
capitan.hashed_password = 'fdsfd'

sess.add(capitan)

sess.commit()