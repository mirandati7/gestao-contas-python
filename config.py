DEBUG=True

USERNAME='root'
PASSWORD='root'
SERVER='localhost'
DB='contas_flutter'

#SQLALCHEMY_DATABASE_URI=f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_DATABASE_URI='mysql://b931484d9553dd:0077d205@us-cdbr-east-06.cleardb.net/heroku_99e461bf00aaa78?reconnect=true'
#username=b931484d9553dd
#password=0077d205
#host=us-cdbr-east-06.cleardb.net
#database=heroku_99e461bf00aaa78

SQLALCHEMY_TRACK_MODIFICATIONS=True

SECRET_KEY='chave_secreta1'