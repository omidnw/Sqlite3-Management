/*------------------------------*
 *				*
 *	Sqlite3 Management.	*
 *	omid reza keshtkar.	*
 *	erfan azhdari.	*
 *				*
 *------------------------------*/


// this file just created for test sqlite3 CRUD Control.
// you can delete this file.


#include "sqlite3mgt.h"


struct Sqlite3_MGT Sqlite3_Default =
{
	.condition = "1",
	.databasename = "test.db",
	.tablename = "testtable",
	.columnname = "test1, test2, test3",
	.value = "testv1, testv2, testv3",
	.column = "",
	.wherecondition = ""
};