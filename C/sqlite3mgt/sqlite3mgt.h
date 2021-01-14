/*------------------------------*
 *				*
 *	Sqlite3 Management.	*
 *	omid reza keshtkar.	*
 *	erfan azhdari.	*
 *				*
 *------------------------------*/


#ifndef SQLITE3_MGT_H
#define SQLITE3_MGT_H


typedef char string[1024];
typedef char ministring[512];

typedef struct Sqlite3_MGT
{
	char condition[3];
	ministring databasename;
	ministring tablename;
	ministring columnname;
	string value;
	ministring column;
	ministring wherecondition;
}Sqlite3_MGT;

void sqlite3mgt(struct Sqlite3_MGT SqliteSTC);

#endif