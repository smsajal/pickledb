import src.interfaces.storageInterface as StorageInterface

def testCreateDB():
	db=StorageInterface.createDatabase("db2")

if __name__ == '__main__':
    testCreateDB()