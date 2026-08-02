---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/ReleaseNotes/ReleaseNotes.html
archived_at: '2026-07-15T08:04:35.192011Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Release Notes

Enterprise Objects Framework Release Notes  Copyright 1998-2000 by Apple Computer, Inc. All Rights Reserved.

# Enterprise Objects Framework 4.5 Release Notes

_Last Updated March 24, 2000_

This document lists those problems known to exist in the Enterprise Objects Framework (which is a major component of WebObjects 4.5). Release notes for the remaining portions of WebObjects are listed separately and can be found [here](WebObjects%204.5%20Release%20Notes.md).

Among the documention supplied with this release is ["What's New in WebObjects 4.5"](What%27s%20New%20in%20WebObjects%204.5.md), which details those features that are new or have substantially changed since the last release of WebObjects. As well, ["WebObjects Post-Installation Instructions"](WebObjects%20Release%204.5%20Post-Installation%20Instructions.md) details a number of important steps you may need to take--depending on your particular configuration--after installing WebObjects.

## Obtaining and Installing Database Client Libraries on Windows NT

To use Enterprise Objects Framework on Windows NT, you must have the appropriate database client libraries, which you must purchase from your database vendor.

### Oracle

Phone: (800) 542-1170 or call your local sales representative

Ask for: Oracle 8 Client

The Oracle adaptor on NT requires the Oracle 8.0, 7.3, or 7.2 Client Library. It won't work with the 7.1 libraries.

On Windows NT, using the latest release of the Oracle client library (8.0) requires you to use SQL\*Net v2, which requires a __tnsnames.ora__ file. __tnsnames.ora__ is a file that you put on client machines, generally in the directory Orant/Network/Admin or Orant/Net80/Admin. The file contains information needed to connect to a server over the network. Entries in __tnsnames.ora__ are keyed off of a server ID alias, and they include information such as the server ID, the host machine name, and the network protocol used by the client library to resolve the server ID alias. An entry in __tnsnames.ora__ might resemble the following:

> ```
> myServerAlias = (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
> (HOST=myMachine) (PORT=1521))(CONNECT_DATA=(SID=eof)))
> ```

Oracle provides tools you can use to create __tnsnames.ora__ files. Refer to your Oracle documentation for more information on __tnsnames.ora__ files and the tools you can use to create them.

If you're using the 7.2 version of the Oracle client libraries on Windows NT, you can use either SQL\*Net v1 or SQL\*Net v2. To use SQL\*Net v1, you should set your adaptor's connectionDictionary __serverId__ entry to

> ```
> T:<host-machine>:<server-name>
> ```

### Informix

Phone: (800) 331-1763 or call your local sales representative

Ask for: ESQL/C version 7.23.TC9 for Win32

If you get the error "INFORMIXSERVER not in sqlhosts file (25596)" but can connect to your database server using the Informix
__ilogin__ program, you may need to run SetNet32 to update the environment variables used by Informix.

The Informix client libraries appear to have redundant sources of server information. They use the
__sqlhosts__ file (__$INFORMIXDIR/etc/sqlhosts__) as well as a collection of environment variables managed by the Setnet32 program.

See your Informix documentation for more information on the __sqlhosts__ file and the Setnet32 program.

### Sybase

Phone: (800) 685-8225 or call your local sales representative

Ask for: OpenClient/C Version 11.1

## Obtaining and Installing Database Client Libraries on Solaris

To use Enterprise Objects Framework on Solaris, you must have the appropriate database client libraries.

Here's what you need:

### Oracle

Phone: (800) 542-1170 or call your local sales representative

Ask for: 8.0 SQLNet V2 TCP/IP Client libraries

The Oracle adaptor on Solaris requires the Oracle 8.0 or 7.3 Client Library. The makefiles are configured for 7.3 or 8.0 (they default to 7.3); with some modifications of the makefiles, you can also link with 7.2.

### Informix

Phone: (800) 331-1763 or call your local sales representative

Ask for: ESQL/C Version 7.23.UC9

If you get the error "INFORMIXSERVER not in sqlhosts file (25596)" but can connect to your database server using the Informix ilogin program, you may need to run SetNet32 to update the environment variables used by Informix.

The Informix client libraries appear to have redundant sources of server information. They use the sqlhosts file (__$INFORMIXDIR/etc/sqlhosts__) as well as a collection of environment variables managed by the Setnet32 program.

See your Informix documentation for more information on the sqlhosts file and the Setnet32 program.

### Sybase

Phone: (800) 685-8225 or call your local sales representative

Ask for: OpenClient/C Version 11.1

### Linking Against the Adaptor

On Solaris applications must explicitly link against the adaptor framework and the client libraries. New makefiles look for adaptor frameworks and automatically add in the right linker arguments. Simply add the adaptor framework to your project, and set the requisite environment variable specifying where the client libraries are installed. For Oracle set ORACLE_HOME and optionally ORACLE_REL. (The ORACLE_REL flag controls which set of libraries are used. It uses the Oracle 7.3 static link libraries by default, but you can also specify "8.0-static" or "7.3-dynamic".) For Sybase set SYBASE_HOME. For Informix set INFORMIX_HOME.

If you use dynamic libraries on Solaris, you need to set the LD_LIBRARY_PATH environment variable when running your application.

## Obtaining and Installing Database Client Libraries on HP-UX

To use Enterprise Objects Framework on HP-UX, you must have the appropriate database client libraries.

### Oracle

Phone: (800) 542-1170 or call your local sales representative

Ask for: 8.0 SQLNet V2 TCP/IP Client libraries

The Oracle adaptor on HP-UX requires the Oracle 8.0 or 7.3 Client Library. The makefiles are configured for 7.3 or 8.0 (they default to 7.3); with some modifications of the makefiles, you can also link with 7.2.

### Informix

Phone: (800) 331-1763 or call your local sales representative

Ask for: ESQL/C Version 7.23.UC6

If you get the error "INFORMIXSERVER not in sqlhosts file (25596)" but can connect to your database server using the Informix ilogin program, you may need to run SetNet32 to update the environment variables used by Informix.

The Informix client libraries appear to have redundant sources of server information. They use the sqlhosts file (__$INFORMIXDIR/etc/sqlhosts__) as well as a collection of environment variables managed by the Setnet32 program.

See your Informix documentation for more information on the sqlhosts file and the Setnet32 program.

### Sybase

Phone: (800) 685-8225 or call your local sales representative

Ask for: OpenClient/C Version 11.1

### Linking Against the Adaptor

On HP-UX applications must explicitly link against the adaptor framework and the client libraries. New makefiles look for adaptor frameworks and automatically add in the right linker arguments. Simply add the adaptor framework to your project, and set the requisite environment variable specifying where the client libraries are installed. For Oracle set ORACLE_HOME and optionally ORACLE_REL. (The ORACLE_REL flag controls which set of libraries are used. It uses the Oracle 7.3 static link libraries by default, but you can also specify "8.0-static" or "7.3-dynamic".) For Sybase set SYBASE_HOME. For Informix set INFORMIX_HOME.

## Known Problems in This Release

---

### Enterprise Objects Framework

|  |  |  |
| --- | --- | --- |
| Reference | 2359723 | 2359723 |
| Problem | The EOF documentation implies that only a single SELECT statement is needed to perform a deep fetch when all the subentities of the fetch specification's entity map to the same table. However, only one specific case is handled with a single SELECT. In the general case, one SELECT is issued for each subentity. | The EOF documentation implies that only a single SELECT statement is needed to perform a deep fetch when all the subentities of the fetch specification's entity map to the same table. However, only one specific case is handled with a single SELECT. In the general case, one SELECT is issued for each subentity. |
| Description | EOF 4.5 performs one SELECT for an inheritance hierarchy if each subentity is mapped to the same table and if each subentity either has a restricting qualifier of the form "attr = val", where "attr" is the same for all subentities and "val" is unique to each subentity, or the subentity is abstract and has no restricting qualifier. If some subentity doesn't qualify for the optimization, then its parent also doesn't qualify. However, if some subtree of an inheritance hierarchy qualifies for the single table fetch, then that subtree is fetched in one SELECT even though other subentities of the parent entity have to be fetched individually. | EOF 4.5 performs one SELECT for an inheritance hierarchy if each subentity is mapped to the same table and if each subentity either has a restricting qualifier of the form "attr = val", where "attr" is the same for all subentities and "val" is unique to each subentity, or the subentity is abstract and has no restricting qualifier. If some subentity doesn't qualify for the optimization, then its parent also doesn't qualify. However, if some subtree of an inheritance hierarchy qualifies for the single table fetch, then that subtree is fetched in one SELECT even though other subentities of the parent entity have to be fetched individually. |
| Workaround | Arrange your single table inheritance heirarchy so that it meets the optimization criteria. | Arrange your single table inheritance heirarchy so that it meets the optimization criteria. |
|  |  |  |
|  |  |  |
| Reference | 2280881 | 2280881 |
| Problem | Concurrent multithreaded saves may bypass optimistic locking check | Concurrent multithreaded saves may bypass optimistic locking check |
| Description | Although it has not yet been verified, EOF may have a brief window where two sessions modifying the same object will get last-one-wins behavior, instead of a merge (which is still last-one-wins at the attribute level). For example:   Editing context 1 locks, modifies object 1  Editing context 2 locks, modifies object 1  Editing context 1 saves changes, unlocks, change notification enqueued on editing context 1  Editing context 2 saves its modifications to object 1 without merging in editing context 1's modifications | Although it has not yet been verified, EOF may have a brief window where two sessions modifying the same object will get last-one-wins behavior, instead of a merge (which is still last-one-wins at the attribute level). For example:   Editing context 1 locks, modifies object 1  Editing context 2 locks, modifies object 1  Editing context 1 saves changes, unlocks, change notification enqueued on editing context 1  Editing context 2 saves its modifications to object 1 without merging in editing context 1's modifications |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2182008 | 2182008 |
| Problem | An NSNumber primary key with a value of 0 is assumed to mean NULL, invoking EOF's primary key generation (perhaps erroneously). | An NSNumber primary key with a value of 0 is assumed to mean NULL, invoking EOF's primary key generation (perhaps erroneously). |
| Description | Starting in EOF 2.2, EODatabaseContext assumes that an object with a single attribute primary key with a value of zero indicates a newly created instance. And as such, EOF attempts to get a new primary key for the object using the delegate hook or the adaptor-specific primary key generation mechanism. This change allows you to use scalar data types in your EO's (like "int") for primary keys, and still rely on EOF's automatic primary key generation. Unfortunately, if you have an existing database rows with primary keys of 0, attempts to update corresponding enterprise objects cause the EODatabaseContext to incorrectly attempt to get a new primary key. This can leave invalid foreign key refernces in other tables. | Starting in EOF 2.2, EODatabaseContext assumes that an object with a single attribute primary key with a value of zero indicates a newly created instance. And as such, EOF attempts to get a new primary key for the object using the delegate hook or the adaptor-specific primary key generation mechanism. This change allows you to use scalar data types in your EO's (like "int") for primary keys, and still rely on EOF's automatic primary key generation. Unfortunately, if you have an existing database rows with primary keys of 0, attempts to update corresponding enterprise objects cause the EODatabaseContext to incorrectly attempt to get a new primary key. This can leave invalid foreign key refernces in other tables. |
| Workaround | Implement the EODatabaseContext delegate method databaseContext:newPrimaryKeyForObject:entity: and catch the case where the framework will mistakenly get a new key.    From EODatabaseContext.h  - (NSDictionary \*)databaseContext:(EODatabaseContext \*)context  newPrimaryKeyForObject:(id)object  entity:(EOEntity \*)entity;  // If a newly inserted EO doesn't already have have a primary key set,  // this delegate is called to generate a key. If the delegate is not implemented,  // or returns nil, then the DatabaseContext will call  // [EOAdaptorChannel primaryKeyForNewRowWithEntity:(EOEntity \*)entity]  // to attempt to generate the key.    Example delegate implementation:  {  ...  model = [[EOModelGroup defaultGroup] modelNamed:@"myModel"];  dbContext = [EODatabaseContext registeredDatabaseContextForModel:model editingContext:editingContext];  [dbContext setDelegate:self];  ...  }    - (NSDictionary \*)databaseContext:(EODatabaseContext \*)context  newPrimaryKeyForObject:(id)object  entity:(EOEntity \*)entity  {  if (entity == entityThatIKnowHasAValidRowWithAKeyOfZero)  \xE6if ([[object valueForKey:primaryKeyThatCanBeZero] isEqual:[NSNumber zero]])  return [NSNumber zero];  return nil;  } | Implement the EODatabaseContext delegate method databaseContext:newPrimaryKeyForObject:entity: and catch the case where the framework will mistakenly get a new key.    From EODatabaseContext.h  - (NSDictionary \*)databaseContext:(EODatabaseContext \*)context  newPrimaryKeyForObject:(id)object  entity:(EOEntity \*)entity;  // If a newly inserted EO doesn't already have have a primary key set,  // this delegate is called to generate a key. If the delegate is not implemented,  // or returns nil, then the DatabaseContext will call  // [EOAdaptorChannel primaryKeyForNewRowWithEntity:(EOEntity \*)entity]  // to attempt to generate the key.    Example delegate implementation:  {  ...  model = [[EOModelGroup defaultGroup] modelNamed:@"myModel"];  dbContext = [EODatabaseContext registeredDatabaseContextForModel:model editingContext:editingContext];  [dbContext setDelegate:self];  ...  }    - (NSDictionary \*)databaseContext:(EODatabaseContext \*)context  newPrimaryKeyForObject:(id)object  entity:(EOEntity \*)entity  {  if (entity == entityThatIKnowHasAValidRowWithAKeyOfZero)  \xE6if ([[object valueForKey:primaryKeyThatCanBeZero] isEqual:[NSNumber zero]])  return [NSNumber zero];  return nil;  } |
|  |  |  |
|  |  |  |
| Reference | 2165078 | 2165078 |
| Problem | Seemingly innocuous qualified fetch always causes exception. | Seemingly innocuous qualified fetch always causes exception. |
| Description | Some qualified fetches raise exceptions because values in the SQL have been formatted as strings when they should have been formatted as some other type. This can happen when you enter an invalid external type or when a Sybase model doesn't contain information about user-defined types that are used in the model. | Some qualified fetches raise exceptions because values in the SQL have been formatted as strings when they should have been formatted as some other type. This can happen when you enter an invalid external type or when a Sybase model doesn't contain information about user-defined types that are used in the model. |
| Workaround | In the case of an invalid external type, simply correct it. In the case of a user defined type, create a new model by reverse engineering the database. The new model's connection dictionary contains information about user-defined types. Copy the connection dictionary from the new model to the original one. | In the case of an invalid external type, simply correct it. In the case of a user defined type, create a new model by reverse engineering the database. The new model's connection dictionary contains information about user-defined types. Copy the connection dictionary from the new model to the original one. |
|  |  |  |
|  |  |  |
| Reference | 2147832 | 2147832 |
| Problem | Enterprise Objects Framework can't update attributes whose internal types are custom (such as NSImages). | Enterprise Objects Framework can't update attributes whose internal types are custom (such as NSImages). |
| Description | A custom value class must implement isEqual: to be used for attributes marked as used for locking. | A custom value class must implement isEqual: to be used for attributes marked as used for locking. |
| Workaround | Implement isEqual: in the custom value class or don't mark the attribute as used for locking. | Implement isEqual: in the custom value class or don't mark the attribute as used for locking. |
|  |  |  |
|  |  |  |
| Reference | 2176885 | 2176885 |
| Problem | The set of valid values for the databaseEncoding entry of a connection dictionary are not documented, and the set can vary in different locales. | The set of valid values for the databaseEncoding entry of a connection dictionary are not documented, and the set can vary in different locales. |
| Description | A connection dictionary's databaseEncoding entry contains the localized name for the string encoding. The localized names are not documented. Furthermore, the localized names for string encodings can vary with the user's locale. Consequently, the specified encoding for an application might not work for users in different locales. | A connection dictionary's databaseEncoding entry contains the localized name for the string encoding. The localized names are not documented. Furthermore, the localized names for string encodings can vary with the user's locale. Consequently, the specified encoding for an application might not work for users in different locales. |
| Workaround | You can find the localized name for string encodings in /Library/Frameworks/Foundation.framework/Resources/<language>.lproj/EncodingNames.strings. | You can find the localized name for string encodings in /Library/Frameworks/Foundation.framework/Resources/<language>.lproj/EncodingNames.strings. |
|  |  |  |
|  |  |  |
| Reference | 2163118 | 2163118 |
| Problem | Schema generation may produce identifiers that are too long. | Schema generation may produce identifiers that are too long. |
| Description | If your database table names are long, the names generated for constraints may be too long. | If your database table names are long, the names generated for constraints may be too long. |
| Workaround | Shorten your table names, or edit the SQL EOModeler generates to shorten the constraint names. | Shorten your table names, or edit the SQL EOModeler generates to shorten the constraint names. |
|  |  |  |
|  |  |  |
| Reference | 2177354 | 2177354 |
| Problem | There are problems saving changes to attributes with mutable custom value objects. | There are problems saving changes to attributes with mutable custom value objects. |
| Description | Suppose you have a mutable custom value type, PhoneNumber, that implements mutator methods like setAreaCode:, setPrefix:, and so on. If you modify one of these values and save changes, the enterprise object is not saved to the database. | Suppose you have a mutable custom value type, PhoneNumber, that implements mutator methods like setAreaCode:, setPrefix:, and so on. If you modify one of these values and save changes, the enterprise object is not saved to the database. |
| Workaround | To use mutable value classes you must do three things:    1) In the PhoneNumber value class object, implement isEqual: to appropriately compare two instances.    2) If the PhoneNumber value is modified, it's owning enterprise object must (first) invoke [self willChange];    3) The enterprise object must provide a set method that copies rather than retains the object passed to it:    - (void)setDayTimePhone:(PhoneNumber \*)number {  [dayTimePhone autorelease];  dayTimePhone = [number copy];  }    #1 would be required, even in a perfect world. #2 is a requirement of the basic EOF architecture. #3 is required because of a bug -- EOF should pass enterprise objects a copy of their values (currently we are passing the the same instance that's shared in the snapshot).    In general, your simplest workaround is to use immutable custom value objects. | To use mutable value classes you must do three things:    1) In the PhoneNumber value class object, implement isEqual: to appropriately compare two instances.    2) If the PhoneNumber value is modified, it's owning enterprise object must (first) invoke [self willChange];    3) The enterprise object must provide a set method that copies rather than retains the object passed to it:    - (void)setDayTimePhone:(PhoneNumber \*)number {  [dayTimePhone autorelease];  dayTimePhone = [number copy];  }    #1 would be required, even in a perfect world. #2 is a requirement of the basic EOF architecture. #3 is required because of a bug -- EOF should pass enterprise objects a copy of their values (currently we are passing the the same instance that's shared in the snapshot).    In general, your simplest workaround is to use immutable custom value objects. |
|  |  |  |
|  |  |  |
| Reference | 2176526 | 2176526 |
| Problem | Applying a qualifier with key path to top of horizontally mapped inheritance hierarchy generates invalid SQL. | Applying a qualifier with key path to top of horizontally mapped inheritance hierarchy generates invalid SQL. |
| Description | Enterprise Objects Framework's query building mechanism doesn't handle relationships to inheritance hierarchies. For example, suppose that you are are attempting to qualify a fetch through a to-many relationship (planes) that points to the top of a horizontally mapped inheritance hierarchy (for the entities Plane, FighterPlane, and TrainerPlane). If you want the query to test against all tables, you'd expect Enterprise Objects Framework to generate SQL similar to the following:    SELECT t0.AIRPORT_ID  FROM PLANE t1, FIGHTER t2, TRAINER t3, AIRPORT t0  WHERE  (t1.LENGTH <= 1000 AND t0.AIRPORT_ID = t1.AIRPORT_FK) OR  (t2.LENGTH <= 1000 AND t0.AIRPORT_ID = t1.AIRPORT_FK) OR  (t3.LENGTH <= 1000 AND t0.AIRPORT_ID = t1.AIRPORT_FK)    Instead, Enterprise Objects Framework generates the following SQL:    SELECT t0.AIRPORT_ID  FROM PLANE t1, AIRPORT t0  WHERE  (t1.LENGTH <= 1000) AND  t0.AIRPORT_ID = t1.AIRPORT_FK    In other words, only the table for the root of the hierarchy is queried. | Enterprise Objects Framework's query building mechanism doesn't handle relationships to inheritance hierarchies. For example, suppose that you are are attempting to qualify a fetch through a to-many relationship (planes) that points to the top of a horizontally mapped inheritance hierarchy (for the entities Plane, FighterPlane, and TrainerPlane). If you want the query to test against all tables, you'd expect Enterprise Objects Framework to generate SQL similar to the following:    SELECT t0.AIRPORT_ID  FROM PLANE t1, FIGHTER t2, TRAINER t3, AIRPORT t0  WHERE  (t1.LENGTH <= 1000 AND t0.AIRPORT_ID = t1.AIRPORT_FK) OR  (t2.LENGTH <= 1000 AND t0.AIRPORT_ID = t1.AIRPORT_FK) OR  (t3.LENGTH <= 1000 AND t0.AIRPORT_ID = t1.AIRPORT_FK)    Instead, Enterprise Objects Framework generates the following SQL:    SELECT t0.AIRPORT_ID  FROM PLANE t1, AIRPORT t0  WHERE  (t1.LENGTH <= 1000) AND  t0.AIRPORT_ID = t1.AIRPORT_FK    In other words, only the table for the root of the hierarchy is queried. |
| Workaround | You can create a qualifier that generates the correct SQL by:    1. Adding relationships in the source entity to all the tables in the inheritance hierarchy. For example, to the Airport entity, you'd add the relationships toFighters and toTrainers to the destination entities FighterPlane and TrainerPlane, respectively. Mark the relationships so they aren't class properties.    2. When building your query, explicitly list these extra relationships. In the Planes example, you'd fetch from Airport where "planes.length < 1000 OR toFigtherPlanes.length < 1000 OR toTrainerPlanes.length < 1000"    Alternatively, you might be able to solve this problem more generally by writing a post processor for EOQualifiers that splits up clauses that perform inheritance tests. The post processor could even programmatically generate the additional relationships on demand and register them with the model using names like "plane_Subclass_Fighter".    A generic EOQualifier post processor could be wired into Enterprise Objects Framework so that application writers don't have to know it exists. The right place for such a mechanism is probably in EOKeyValueQualifier's schemaBasedQualifierWithRootEntity: method (see EOSQLQualifier.h). You could put the post processor code in a subclass of EOKeyValueQualifier (with an appropriate call to super after the transformation, if any, is performed) and have your subclass pose as EOKeyValueQualifier. | You can create a qualifier that generates the correct SQL by:    1. Adding relationships in the source entity to all the tables in the inheritance hierarchy. For example, to the Airport entity, you'd add the relationships toFighters and toTrainers to the destination entities FighterPlane and TrainerPlane, respectively. Mark the relationships so they aren't class properties.    2. When building your query, explicitly list these extra relationships. In the Planes example, you'd fetch from Airport where "planes.length < 1000 OR toFigtherPlanes.length < 1000 OR toTrainerPlanes.length < 1000"    Alternatively, you might be able to solve this problem more generally by writing a post processor for EOQualifiers that splits up clauses that perform inheritance tests. The post processor could even programmatically generate the additional relationships on demand and register them with the model using names like "plane_Subclass_Fighter".    A generic EOQualifier post processor could be wired into Enterprise Objects Framework so that application writers don't have to know it exists. The right place for such a mechanism is probably in EOKeyValueQualifier's schemaBasedQualifierWithRootEntity: method (see EOSQLQualifier.h). You could put the post processor code in a subclass of EOKeyValueQualifier (with an appropriate call to super after the transformation, if any, is performed) and have your subclass pose as EOKeyValueQualifier. |
|  |  |  |
|  |  |  |
| Reference | 2174379 | 2174379 |
| Problem | EODatabaseContext can't be the direct parentObjectStore of an EOEditingContext. | EODatabaseContext can't be the direct parentObjectStore of an EOEditingContext. |
| Description | The EODatabaseContext requires that an EOObjectStoreCoordinator sit between it and any EOEditingContexts that it serves. This is the default configuration set up by the framework, so you shouldn't normally run into this problem. Just a reminder, you can set up an editingContext and be ready to go with this one line:    EOEditingContext \*editingContext = [EOEditingContext new];   // automatically uses [EOObjectStoreCoordinator defaultCoordinator]  // as parentObjectStore    Any necessary EODatabaseContexts are created and registered automatically. | The EODatabaseContext requires that an EOObjectStoreCoordinator sit between it and any EOEditingContexts that it serves. This is the default configuration set up by the framework, so you shouldn't normally run into this problem. Just a reminder, you can set up an editingContext and be ready to go with this one line:    EOEditingContext \*editingContext = [EOEditingContext new];   // automatically uses [EOObjectStoreCoordinator defaultCoordinator]  // as parentObjectStore    Any necessary EODatabaseContexts are created and registered automatically. |
| Workaround | Don't assign an EODatabaseContext as the parentObjectStore of an EOEditingContext. There's no benefit to doing so anyway. | Don't assign an EODatabaseContext as the parentObjectStore of an EOEditingContext. There's no benefit to doing so anyway. |
|  |  |  |
|  |  |  |
| Reference | 2174345 | 2174345 |
| Problem | You can't update to-many relationship if the foreign key isn't marked as a class property or as used for locking. | You can't update to-many relationship if the foreign key isn't marked as a class property or as used for locking. |
| Description | Suppose that an entity's foreign key attribute isn't marked as a class property or as used for locking. If you designate the foreign key attribute as a to-many relationship's destination key, the foreign key value isn't always updated. This occurs because the destination entity doesn't know that the attribute participates in a relationship. Therefore, the destination entity doesn't fetch the foreign key from the database or update it. | Suppose that an entity's foreign key attribute isn't marked as a class property or as used for locking. If you designate the foreign key attribute as a to-many relationship's destination key, the foreign key value isn't always updated. This occurs because the destination entity doesn't know that the attribute participates in a relationship. Therefore, the destination entity doesn't fetch the foreign key from the database or update it. |
| Workaround | Mark attributes that are destination keys of a to-many relationship so they are fetched. For example, you could:  - Mark them as class properties.  - Mark them as used for locking.  - Use them in inverse relationships to the problematic to-many's source entity. | Mark attributes that are destination keys of a to-many relationship so they are fetched. For example, you could:  - Mark them as class properties.  - Mark them as used for locking.  - Use them in inverse relationships to the problematic to-many's source entity. |
|  |  |  |
|  |  |  |
| Reference | 2431180 | 2431180 |
| Problem | After calling myEODatabaseContext.invalidateAllObjects(), subsequent saves either fail to save changes or just raise. | After calling myEODatabaseContext.invalidateAllObjects(), subsequent saves either fail to save changes or just raise. |
| Description | If an application has any EOEditingContexts that contain unsaved inserted objects, any call to myEODatabaseContext.invalidateAllObjects() will leave those EOEditingContexts in an inconsistent state. If you try to save the changes in any such EOEditingContext, the inserted objects will not be saved, or you might get an exception because these objects are mistakenly treated as updated objects. | If an application has any EOEditingContexts that contain unsaved inserted objects, any call to myEODatabaseContext.invalidateAllObjects() will leave those EOEditingContexts in an inconsistent state. If you try to save the changes in any such EOEditingContext, the inserted objects will not be saved, or you might get an exception because these objects are mistakenly treated as updated objects. |
| Workaround | Replace all invocations of   dbc.invalidateAllObjects()  with   dbc.invalidateObjectsWithGlobalIDs(dbc.database().snapshots().allKeys()) | Replace all invocations of   dbc.invalidateAllObjects()  with   dbc.invalidateObjectsWithGlobalIDs(dbc.database().snapshots().allKeys()) |
|  |  |  |
|  |  |  |
| Reference | 2174251 | 2174251 |
| Problem | Changes made during saveChanges are silently lost. | Changes made during saveChanges are silently lost. |
| Description | If you change an enterprise object while its editing context is in it's saveChanges method (for example, if you change an enterprise object in an EODatabaseContext delegate method), the changes may be silently lost. | If you change an enterprise object while its editing context is in it's saveChanges method (for example, if you change an enterprise object in an EODatabaseContext delegate method), the changes may be silently lost. |
| Workaround | Don't make changes to objects during the save process. Instead, make the changes from the EOEditingContext delegate method editingContextWillSaveChanges:. | Don't make changes to objects during the save process. Instead, make the changes from the EOEditingContext delegate method editingContextWillSaveChanges:. |
|  |  |  |
|  |  |  |
| Reference | 2176892 | 2176892 |
| Problem | Multiple fetch-on-load display groups associated with an invalid connection dictionary can cause an exception. | Multiple fetch-on-load display groups associated with an invalid connection dictionary can cause an exception. |
| Description | When loading a nib file that has more than one display group set to fetch on load, an application can crash if the display groups' model has an invalid connection dictionary. A crash occurs because the second display group tries to run the adaptor's login panel while the first one already has the panel open. This confuses the Application Kit. | When loading a nib file that has more than one display group set to fetch on load, an application can crash if the display groups' model has an invalid connection dictionary. A crash occurs because the second display group tries to run the adaptor's login panel while the first one already has the panel open. This confuses the Application Kit. |
| Workaround | Validate the connection dictionaries for all models in the [EOModelGroup defaultGroup] before opening the nib. | Validate the connection dictionaries for all models in the [EOModelGroup defaultGroup] before opening the nib. |
|  |  |  |
|  |  |  |
| Reference | 2429478 | 2429478 |
| Problem | After calling myEODatabaseContext.invalidateAllObjects(), subsequent saves either fail to save changes or just raise. | After calling myEODatabaseContext.invalidateAllObjects(), subsequent saves either fail to save changes or just raise. |
| Description | If an application has any EOEditingContexts that contain unsaved inserted objects, any call to myEODatabaseContext.invalidateAllObjects() will leave those EOEditingContexts in an inconsistent state. If you try to save the changes in any such EOEditingContext, the inserted objects will not be saved, or you might get an exception because these objects are mistakenly treated as updated objects. | If an application has any EOEditingContexts that contain unsaved inserted objects, any call to myEODatabaseContext.invalidateAllObjects() will leave those EOEditingContexts in an inconsistent state. If you try to save the changes in any such EOEditingContext, the inserted objects will not be saved, or you might get an exception because these objects are mistakenly treated as updated objects. |
| Workaround | Replace all invocations of   dbc.invalidateAllObjects()  with   dbc.invalidateObjectsWithGlobalIDs(dbc.database().snapshots().allKeys()) | Replace all invocations of   dbc.invalidateAllObjects()  with   dbc.invalidateObjectsWithGlobalIDs(dbc.database().snapshots().allKeys()) |
|  |  |  |
|  |  |  |
| Reference | 2418179 | 2418179 |
| Problem | EOModeler doesn't generate a no-arg constructor for EO classes. | EOModeler doesn't generate a no-arg constructor for EO classes. |
| Description | When you generate Java class files for an entity using EOModeler,  the no-argument constructor is not generated. Rather, a three-argument constructor  is generated. When you attempt to use a no-argument constructor to instantiate a  new object of your custom class, the compilation fails with "No constructor matching  MyClass() found in class MyClass". | When you generate Java class files for an entity using EOModeler,  the no-argument constructor is not generated. Rather, a three-argument constructor  is generated. When you attempt to use a no-argument constructor to instantiate a  new object of your custom class, the compilation fails with "No constructor matching  MyClass() found in class MyClass". |
| Workaround | 1) Always instantiate a new object with the three-argument constructor.  MyObject = new MyClass(null,null,null);    2) Add the no-argument constructor by hand to the <class>.java file:  public MyClass() {  this (null,null,null);  }    3) Modify the EOJavaClass.template file to add the no-argument constructor in a similar  way. | 1) Always instantiate a new object with the three-argument constructor.  MyObject = new MyClass(null,null,null);    2) Add the no-argument constructor by hand to the <class>.java file:  public MyClass() {  this (null,null,null);  }    3) Modify the EOJavaClass.template file to add the no-argument constructor in a similar  way. |
|  |  |  |
|  |  |  |
| Reference | 2404037 | 2404037 |
| Problem | On MacOS X Server, resource loading (of models, for instance) can fail mysteriously. | On MacOS X Server, resource loading (of models, for instance) can fail mysteriously. |
| Description | There is a bug in the MacOS X Server implementation of Foundation such that NSBundle can return duplicates. If you launch an EOF application with a relative path such as ./MyApp, some EOF applications (including some of the WebObjects examples) trip over this behavior. Since EOF doesn't allow duplicate models to be loaded, you are presented with a fatal exception as EOF tries to load the same model multiple times. | There is a bug in the MacOS X Server implementation of Foundation such that NSBundle can return duplicates. If you launch an EOF application with a relative path such as ./MyApp, some EOF applications (including some of the WebObjects examples) trip over this behavior. Since EOF doesn't allow duplicate models to be loaded, you are presented with a fatal exception as EOF tries to load the same model multiple times. |
| Workaround | Launch the application from within PB, gdb, or with an absolute path. | Launch the application from within PB, gdb, or with an absolute path. |
|  |  |  |
|  |  |  |
| Reference | 2397380 | 2397380 |
| Problem | Java beans embedded in a Java Client application in 4.5 don't run out of a jar/zip file. | Java beans embedded in a Java Client application in 4.5 don't run out of a jar/zip file. |
| Description | The Java Client framework cannot directly reference individual resources within a jar/zip file. Therefore Java Client cannot act as a container for a Java Beans inside jar/zip files. | The Java Client framework cannot directly reference individual resources within a jar/zip file. Therefore Java Client cannot act as a container for a Java Beans inside jar/zip files. |
| Workaround | Unarchive Java beans into .class files (and other resources) and put them in the CLASSPATH. | Unarchive Java beans into .class files (and other resources) and put them in the CLASSPATH. |
|  |  |  |
|  |  |  |
| Reference | 2385153 | 2385153 |
| Problem | The OracleChannel class specification specifies an incorrect default name. | The OracleChannel class specification specifies an incorrect default name. |
| Description | The OracleChannel method description for setOracleTableNamesSQL: method states that "OracleTableNamesSQL" is the name of the default that sets SQL for getting Oracle table names. The correct default name is "EOOracleTableNamesSQL". Note that this and the other defaults for Enterprise Objects Framework are now described in the "Enterprise Objects Framework\xCDs User Defaults" document, which is available through Info Center. | The OracleChannel method description for setOracleTableNamesSQL: method states that "OracleTableNamesSQL" is the name of the default that sets SQL for getting Oracle table names. The correct default name is "EOOracleTableNamesSQL". Note that this and the other defaults for Enterprise Objects Framework are now described in the "Enterprise Objects Framework\xCDs User Defaults" document, which is available through Info Center. |
| Workaround | Refer to the "Enterprise Objects Framework's User Defaults" document. | Refer to the "Enterprise Objects Framework's User Defaults" document. |
|  |  |  |
|  |  |  |
| Reference | 2272980 | 2272980 |
| Problem | The EODisableClassParser user default isn't documented | The EODisableClassParser user default isn't documented |
| Description | In EOF 3.0, InterfaceBuilder is integrated with a class parser that will automatically read keys from your source code. Because this may negatively affect performance when you are editing a nib file, there is a user default to turn off the class parsing. In order to turn off the class parsing, type the following on the command line:     "defaults write InterfaceBuilder EODisableClassParser YES" | In EOF 3.0, InterfaceBuilder is integrated with a class parser that will automatically read keys from your source code. Because this may negatively affect performance when you are editing a nib file, there is a user default to turn off the class parsing. In order to turn off the class parsing, type the following on the command line:     "defaults write InterfaceBuilder EODisableClassParser YES" |
| Workaround | See the description, above. | See the description, above. |
|  |  |  |
|  |  |  |
| Reference | 2266541 | 2266541 |
| Problem | The EOProjectSourceSearchPaths user default is now NSProjectSearchPath | The EOProjectSourceSearchPaths user default is now NSProjectSearchPath |
| Description | EOProjectSourceSearchPaths is deprecated. Use NSProjectSearchPath instead. However, for backwards compatibility, EOProjectSourceSearchPaths will be used if there is no default value for NSProjectSearchPath.    NSProjectSearchPath is an optional array of paths which should contain project source directories. At development time (in InterfaceBuilder and EOModeler) EOF searches this patch for models in frameworks used by the application being edited. | EOProjectSourceSearchPaths is deprecated. Use NSProjectSearchPath instead. However, for backwards compatibility, EOProjectSourceSearchPaths will be used if there is no default value for NSProjectSearchPath.    NSProjectSearchPath is an optional array of paths which should contain project source directories. At development time (in InterfaceBuilder and EOModeler) EOF searches this patch for models in frameworks used by the application being edited. |
| Workaround | Use NSProjectSearchPath. | Use NSProjectSearchPath. |
|  |  |  |
|  |  |  |
| Reference | 2246743 | 2246743 |
| Problem | The OpenBase Lite LIKE operator is always case-insensitive. | The OpenBase Lite LIKE operator is always case-insensitive. |
| Description | There is no way to perform a case sensitive LIKE comparison with the OpenBase Lite database. | There is no way to perform a case sensitive LIKE comparison with the OpenBase Lite database. |
| Workaround | There is no convenient workaround. Depending on the application, = may be sufficient, or the programmer may have to do a case-sensitive comparison in memory using a custom comparison method. | There is no convenient workaround. Depending on the application, = may be sufficient, or the programmer may have to do a case-sensitive comparison in memory using a custom comparison method. |
|  |  |  |
|  |  |  |
| Reference | 2307145 | 2307145 |
| Problem | The UsingStoredProcedures example does not work correctly with Informix. | The UsingStoredProcedures example does not work correctly with Informix. |
| Description | The example in Examples/EnterpriseObjects/UsingStoredProcedures does not work correctly with Informix and the stored procedure INSERT_MOVIE. | The example in Examples/EnterpriseObjects/UsingStoredProcedures does not work correctly with Informix and the stored procedure INSERT_MOVIE. |
| Workaround | Do not use the INSERT_MOVIE stored procedure. | Do not use the INSERT_MOVIE stored procedure. |
|  |  |  |
|  |  |  |
| Reference | 2281252 | 2281252 |
| Problem | The MoviesAppKit model used in the Enterprise Objects examples generates a consistency check warning | The MoviesAppKit model used in the Enterprise Objects examples generates a consistency check warning |
| Description | A consistency check warning is generated for /System/Developer/Examples/EnterpriseObjects/AppKit/Movie/MoviesAppKit.eomodeld. The warning says: "Attribute photo in Entity TalentPhoto has a valueClassName of NSImage, but it doesn't have a adaptorValueConversionMethodName". | A consistency check warning is generated for /System/Developer/Examples/EnterpriseObjects/AppKit/Movie/MoviesAppKit.eomodeld. The warning says: "Attribute photo in Entity TalentPhoto has a valueClassName of NSImage, but it doesn't have a adaptorValueConversionMethodName". |
| Workaround | Ignore the warning. The examples should work fine, except that talent photos cannot be written to the database. | Ignore the warning. The examples should work fine, except that talent photos cannot be written to the database. |
|  |  |  |
|  |  |  |
| Reference | 2273015 | 2273015 |
| Problem | SetupWizard: primary key generation may not work when installing into a Sybase database | SetupWizard: primary key generation may not work when installing into a Sybase database |
| Description | If you run the SetupWizard and install both the Movies and Rentals databases into the same Sybase database, the automatic primary key generation will not work for the Movies schema. | If you run the SetupWizard and install both the Movies and Rentals databases into the same Sybase database, the automatic primary key generation will not work for the Movies schema. |
| Workaround | Open the Movies eomodel in EOModeler and use Generate SQL to generate primary key support ONLY. Ignore any warnings you may get from the database. | Open the Movies eomodel in EOModeler and use Generate SQL to generate primary key support ONLY. Ignore any warnings you may get from the database. |
|  |  |  |
|  |  |  |
| Reference | 2260833 | 2260833 |
| Problem | EOAttribute has "Value Class" and "Value Class Obj-C" columns; these are really the same thing. | EOAttribute has "Value Class" and "Value Class Obj-C" columns; these are really the same thing. |
| Description | The "Value Class" column is old. It is included only to prevent problems for users with defaults information from a previous version of EOModeler. | The "Value Class" column is old. It is included only to prevent problems for users with defaults information from a previous version of EOModeler. |
| Workaround | Only use one of the columns. | Only use one of the columns. |
|  |  |  |
|  |  |  |
| Reference | 2275174 | 2275174 |
| Problem | Cannot delete an EOFetchSpecification in EOModeler: the "Cut" and "Delete" menu items are not enabled | Cannot delete an EOFetchSpecification in EOModeler: the "Cut" and "Delete" menu items are not enabled |
| Description | It is possible to get a fetch specification that incorrectly disables the "Cut" and "Delete" menu items. This usually happens when you have a new fetch specification without a name. | It is possible to get a fetch specification that incorrectly disables the "Cut" and "Delete" menu items. This usually happens when you have a new fetch specification without a name. |
| Workaround | Use the "Cut" icon on the toolbar, or give the EOFetchSpecification a new or different name. | Use the "Cut" icon on the toolbar, or give the EOFetchSpecification a new or different name. |
|  |  |  |
|  |  |  |
| Reference | 2177608 | 2177608 |
| Problem | Existing EOF projects don't see the new EOF 3.0 source-code generation templates | Existing EOF projects don't see the new EOF 3.0 source-code generation templates |
| Description | Enterprise Objects Framework 3.0 includes fixes and additions to EOInterfaceFile.template and EOImplementationFile.template. If you have an EOF 2.x project that contains the old versions of these files, the old versions will continue to be used when you generate source files in EOModeler. | Enterprise Objects Framework 3.0 includes fixes and additions to EOInterfaceFile.template and EOImplementationFile.template. If you have an EOF 2.x project that contains the old versions of these files, the old versions will continue to be used when you generate source files in EOModeler. |
| Workaround | If you haven't customized the templates, just remove EOInterfaceFile.template and EOImplementationFile.template from your project. EOModeler will then use the most up-to-date versions of these files.    If you want to build a customized template based on the newest versions, copy /Developer/Applications/EOModeler.app/Resources/EOImplementationFile.template and /Developer/Apps/EOModeler.app/Resources/EOInterfaceFile.template into your project directory. | If you haven't customized the templates, just remove EOInterfaceFile.template and EOImplementationFile.template from your project. EOModeler will then use the most up-to-date versions of these files.    If you want to build a customized template based on the newest versions, copy /Developer/Applications/EOModeler.app/Resources/EOImplementationFile.template and /Developer/Apps/EOModeler.app/Resources/EOInterfaceFile.template into your project directory. |
|  |  |  |
|  |  |  |
| Reference | 2177631 | 2177631 |
| Problem | An EORelationship can return nil for its inverseRelationship after the inverse is added | An EORelationship can return nil for its inverseRelationship after the inverse is added |
| Description | The first time you ask the EORelationship for its inverseRelationship it searches all relationships in its destinationEntity looking for an inverse, it caches the result of this search. This cache does not always get invalidated when the relationships of the destinationEntity change, so after editing a model and adding an inverse relationship to an EORelationship (either in code or with EOModeler), an inverseRelationship message sent to the EORelationship can return nil. | The first time you ask the EORelationship for its inverseRelationship it searches all relationships in its destinationEntity looking for an inverse, it caches the result of this search. This cache does not always get invalidated when the relationships of the destinationEntity change, so after editing a model and adding an inverse relationship to an EORelationship (either in code or with EOModeler), an inverseRelationship message sent to the EORelationship can return nil. |
| Workaround | See the category on EORelationship in the ModelerBundle/RelationshipExtras.m example. | See the category on EORelationship in the ModelerBundle/RelationshipExtras.m example. |
|  |  |  |
|  |  |  |
| Reference | 2159472 | 2159472 |
| Problem | Derived attributes are limited and don't offer full SQL as advertised. | Derived attributes are limited and don't offer full SQL as advertised. |
| Description | Placing a string or a numeric constant in the definition field of a derived attribute generates invalid SQL. Definitions such as "title" and "0.0" don't work correctly. However, definitions such as "att1 + 5" should work correctly when "att1" specifies another attribute. | Placing a string or a numeric constant in the definition field of a derived attribute generates invalid SQL. Definitions such as "title" and "0.0" don't work correctly. However, definitions such as "att1 + 5" should work correctly when "att1" specifies another attribute. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2176256 | 2176256 |
| Problem | Additions or changes to a relationship in a parent entity aren't pushed down the children | Additions or changes to a relationship in a parent entity aren't pushed down the children |
| Description | AnyAny additions or changes you make using EOModeler to a relationship in a parent entity won't get pushed down to the parent's children. Changes to attributes are propagated correctly, but relationship information is lost. This can make editing parent EO's rather tedious and error prone | AnyAny additions or changes you make using EOModeler to a relationship in a parent entity won't get pushed down to the parent's children. Changes to attributes are propagated correctly, but relationship information is lost. This can make editing parent EO's rather tedious and error prone |
| Workaround | Use at least two windows onto the same model, allowing you to see the parent and its children at the same time. This should make it easier to catch changes that don't get progagated. | Use at least two windows onto the same model, allowing you to see the parent and its children at the same time. This should make it easier to catch changes that don't get progagated. |
|  |  |  |
|  |  |  |
| Reference | 2174947 | 2174947 |
| Problem | Interface Builder crashes after adding a symbolic link for a model to a project | Interface Builder crashes after adding a symbolic link for a model to a project |
| Description | On MacOS X Server, if you drag a symbolic link for a model into Interface Builder and answer YES to the "add Model to project" panel, Interface Builder crashes. | On MacOS X Server, if you drag a symbolic link for a model into Interface Builder and answer YES to the "add Model to project" panel, Interface Builder crashes. |
| Workaround | Drag the actual model file instead of the symbolic link. | Drag the actual model file instead of the symbolic link. |
|  |  |  |
|  |  |  |
| Reference | 2329635 | 2329635 |
| Problem | EOF can generate incorrect SQL for disjunctions of qualifiers where one of the qualifiers involves an optional relationship. | EOF can generate incorrect SQL for disjunctions of qualifiers where one of the qualifiers involves an optional relationship. |
| Description | The form of the SQL generated for an EOOrQualifier is similar to the SQL generated for an EOAndQualifier, but with "OR" substituted for "AND". For example, the qualifier "attr1 = v1 OR rel.attr2 = v2" would generate a SQL WHERE clause something like...    WHERE (ENTITY.ATTR1 = v1 or REL.ATTR2 = v2) AND REL.PK = ENTITY.PK    For a mandatory relationship 'rel', there will always be a match in the REL table and the above SQL WHERE clause will end up giving the correct result. However, for an optional relationship with a NULL value, the WHERE clause fails to return any rows even if there were rows in the ENTITY table that matched the value v1.     The appropriate SQL would be    WHERE ENTITY.ATTR1 = v1 or (REL.ATTR2 = v2 AND REL.PK = ENTITY.PK)    which would give the correct results for all cases. | The form of the SQL generated for an EOOrQualifier is similar to the SQL generated for an EOAndQualifier, but with "OR" substituted for "AND". For example, the qualifier "attr1 = v1 OR rel.attr2 = v2" would generate a SQL WHERE clause something like...    WHERE (ENTITY.ATTR1 = v1 or REL.ATTR2 = v2) AND REL.PK = ENTITY.PK    For a mandatory relationship 'rel', there will always be a match in the REL table and the above SQL WHERE clause will end up giving the correct result. However, for an optional relationship with a NULL value, the WHERE clause fails to return any rows even if there were rows in the ENTITY table that matched the value v1.     The appropriate SQL would be    WHERE ENTITY.ATTR1 = v1 or (REL.ATTR2 = v2 AND REL.PK = ENTITY.PK)    which would give the correct results for all cases. |
| Workaround | Separate your original fetch specification into independent fetch specifications that do not have disjunctions involving optional relationships, and concatenate the multiple results. Naturally, the same EO might be returned by multiple fetch specifications so you may need to filter out duplicates from the concatenated results. For complicated fetch specifications, it may be more effecient to use a custom SQL query (see documentation on EOCustomQueryExpressionHintKey in EODatabaseContext.h). If you choose to use custom SQL and you have multiple qualifiers across relationships, you should consider using DISTINCT since there may be multiple ways for one EO to satisfy the qualifier. | Separate your original fetch specification into independent fetch specifications that do not have disjunctions involving optional relationships, and concatenate the multiple results. Naturally, the same EO might be returned by multiple fetch specifications so you may need to filter out duplicates from the concatenated results. For complicated fetch specifications, it may be more effecient to use a custom SQL query (see documentation on EOCustomQueryExpressionHintKey in EODatabaseContext.h). If you choose to use custom SQL and you have multiple qualifiers across relationships, you should consider using DISTINCT since there may be multiple ways for one EO to satisfy the qualifier. |
|  |  |  |
|  |  |  |
| Reference | 2370377 | 2370377 |
| Problem | It isn't documented that locking operations aren't supported in the client side of a Java Client application are no-ops. | It isn't documented that locking operations aren't supported in the client side of a Java Client application are no-ops. |
| Description | Locking is not implemented in com.apple.client.eocontrol.EOEditingContext and EODistributedObjectStore, but there is public API in those classes that makes it appear otherwise. The EODistributedObjectStore method isObjectLockedWithGlobalID always returns false because locking isn't supported in the client. Similarly, the EODistributedObjectStore method lockObjectWithGlobalID raises an exception. The client-side EOEditingContext locking methods (lockObjectWithGlobalID, lockObject, locksObjectBeforeFirstModification, setLocksObjectBeforeFirstModification, and isObjectLockedWithGlobalID) are also affected: lockObjectWithGlobalID and lockObject raise on first use; locksObjectBeforeFirstModification and setLocksObjectBeforeFirstModification trigger a raise if set to true and you modify an object; and isObjectLockedWithGlobalID always returns false. | Locking is not implemented in com.apple.client.eocontrol.EOEditingContext and EODistributedObjectStore, but there is public API in those classes that makes it appear otherwise. The EODistributedObjectStore method isObjectLockedWithGlobalID always returns false because locking isn't supported in the client. Similarly, the EODistributedObjectStore method lockObjectWithGlobalID raises an exception. The client-side EOEditingContext locking methods (lockObjectWithGlobalID, lockObject, locksObjectBeforeFirstModification, setLocksObjectBeforeFirstModification, and isObjectLockedWithGlobalID) are also affected: lockObjectWithGlobalID and lockObject raise on first use; locksObjectBeforeFirstModification and setLocksObjectBeforeFirstModification trigger a raise if set to true and you modify an object; and isObjectLockedWithGlobalID always returns false. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2346795 | 2346795 |
| Problem | Java Client's EODisplayGroup (com.apple.client.eointerface.EODisplayGroup) doesn't use defaultStringMatchFormat like the Objective-C and com.apple.yellow counterparts do. | Java Client's EODisplayGroup (com.apple.client.eointerface.EODisplayGroup) doesn't use defaultStringMatchFormat like the Objective-C and com.apple.yellow counterparts do. |
| Description | Java Client's use of defaultStringMatchFormat in EODisplayGroup is inconsistent with the Objective-C behavior. Because format string parsing isn't currently available in pure java, EODisplayGroup merely appends the characters in the range [2, n] of the stringMatchFormat (which behaves correctly with the default value of this variable being "%@\*" i.e. append the '\*' character). If developers supply their own defaultStringMatchFormats, the first two characters will be ignored and the rest merely appended. | Java Client's use of defaultStringMatchFormat in EODisplayGroup is inconsistent with the Objective-C behavior. Because format string parsing isn't currently available in pure java, EODisplayGroup merely appends the characters in the range [2, n] of the stringMatchFormat (which behaves correctly with the default value of this variable being "%@\*" i.e. append the '\*' character). If developers supply their own defaultStringMatchFormats, the first two characters will be ignored and the rest merely appended. |
| Workaround | For simple appending, change the defaultStringMatchFormat with setDefaultStringMatchFormat() or setGlobalDefaultStringMatchFormat(). For more complex alterations, you can modify the query value strings yourself and set them within the appropriate query dictionary using EODisplayGroup's setEqualToQueryValues(), setGreaterThanQueryValues() or setLessThanQueryValues(). | For simple appending, change the defaultStringMatchFormat with setDefaultStringMatchFormat() or setGlobalDefaultStringMatchFormat(). For more complex alterations, you can modify the query value strings yourself and set them within the appropriate query dictionary using EODisplayGroup's setEqualToQueryValues(), setGreaterThanQueryValues() or setLessThanQueryValues(). |
|  |  |  |
|  |  |  |
| Reference | 2448190 | 2448190 |
| Problem | Java Client doesn't support inheritance. | Java Client doesn't support inheritance. |
| Description | Inheritance, which is supported on server-side EOF applications, isn't supported in client-side Java Client applications. | Inheritance, which is supported on server-side EOF applications, isn't supported in client-side Java Client applications. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |

---

### OpenBase Lite

|  |  |  |
| --- | --- | --- |
| Reference | 2361264 | 2361264 |
| Problem | Database path handling is now more flexible in OpenBase Lite | Database path handling is now more flexible in OpenBase Lite |
| Description | In previous releases, the OpenBase Lite adaptor's path handling was poor:  - the file was hard coded by default (when reverse engineering) and it wasn't obvious how to erase it. This path could result in unexpected failures when copying projects between machines (especially between different file systems).  - the search path (when the PATH is not set) was unknown to the user and couldn't be changed.  - databases couldn't be packaged easily in the application resources directory.    As part of the reorganization of the OpenBase Lite login panel, this was fixed. Instead of encoding a separate database name and path, we just encode the path. The preferred connection dictionary entry key is DBPATH, whose value is a full path to the \*.db wrapper. Optionally, it can be a simple name in which case the full path is found by searching the app's Resources and then the {~, /Local, /Network, /System}/Library/Databases/ directories at runtime for the \*.db wrapper. For backwards compatibility, the old connection keys are considered if there is no value for DBPATH.    If the user default EOAdaptorDebubEnabled is YES, the full path to the database will be logged when a connection is made. This can be helpful if there are multiple databases with the same name at different points in the OpenBase Lite search path. | In previous releases, the OpenBase Lite adaptor's path handling was poor:  - the file was hard coded by default (when reverse engineering) and it wasn't obvious how to erase it. This path could result in unexpected failures when copying projects between machines (especially between different file systems).  - the search path (when the PATH is not set) was unknown to the user and couldn't be changed.  - databases couldn't be packaged easily in the application resources directory.    As part of the reorganization of the OpenBase Lite login panel, this was fixed. Instead of encoding a separate database name and path, we just encode the path. The preferred connection dictionary entry key is DBPATH, whose value is a full path to the \*.db wrapper. Optionally, it can be a simple name in which case the full path is found by searching the app's Resources and then the {~, /Local, /Network, /System}/Library/Databases/ directories at runtime for the \*.db wrapper. For backwards compatibility, the old connection keys are considered if there is no value for DBPATH.    If the user default EOAdaptorDebubEnabled is YES, the full path to the database will be logged when a connection is made. This can be helpful if there are multiple databases with the same name at different points in the OpenBase Lite search path. |
| Workaround | None necessary. | None necessary. |
|  |  |  |
|  |  |  |
| Reference | 2307176 | 2307176 |
| Problem | OpenBaseLite can corrupt data in /tmp/work. | OpenBaseLite can corrupt data in /tmp/work. |
| Description | OpenBaseLite writes temporary files in /tmp/work. These files are used when restarting a database in order to improve performance. However, if an application crashes, OpenBaseLite can leave corrupt data in /tmp/work which might cause any application that uses that database to crash. The actual database tables are probably still valid, but the corrupt scratch files in /tmp/work cause the crash. | OpenBaseLite writes temporary files in /tmp/work. These files are used when restarting a database in order to improve performance. However, if an application crashes, OpenBaseLite can leave corrupt data in /tmp/work which might cause any application that uses that database to crash. The actual database tables are probably still valid, but the corrupt scratch files in /tmp/work cause the crash. |
| Workaround | Delete the directory /tmp/work (or C:/TEMP/WORK on Windows NT). OpenBaseLite will recreate the files as necessary the next time it starts up the database. | Delete the directory /tmp/work (or C:/TEMP/WORK on Windows NT). OpenBaseLite will recreate the files as necessary the next time it starts up the database. |
|  |  |  |
|  |  |  |
| Reference | 2303101 | 2303101 |
| Problem | OpenBaseLite doesn't reliably compare DATETIME values and can result in optimistic locking failures. | OpenBaseLite doesn't reliably compare DATETIME values and can result in optimistic locking failures. |
| Description | OpenBaseLite does not correctly compare DATETIME values that have non-zero millisecond values. User-entered datetimes will typically be in integral values for seconds, but generated values such as [NSCalendarDate date] are precise to the millisecond. The incorrect comparison can lead to optimistic locking failures during UPDATEs and DELETEs. | OpenBaseLite does not correctly compare DATETIME values that have non-zero millisecond values. User-entered datetimes will typically be in integral values for seconds, but generated values such as [NSCalendarDate date] are precise to the millisecond. The incorrect comparison can lead to optimistic locking failures during UPDATEs and DELETEs. |
| Workaround | Do not use DATETIME columns for optimistic locking with OpenBaseLite. | Do not use DATETIME columns for optimistic locking with OpenBaseLite. |
|  |  |  |
|  |  |  |
| Reference | 2300903 | 2300903 |
| Problem | OpenBaseLite cannot use "ID" as a column name. | OpenBaseLite cannot use "ID" as a column name. |
| Description | "ID" is a reserved word in OpenBaseLite and cannot be used as a column name. (This includes any variation of "ID" with upper or lowercase letters.) There is no error message when a table is created using "ID" as a column name, but that column will not be accessible and the table is practically unusable. | "ID" is a reserved word in OpenBaseLite and cannot be used as a column name. (This includes any variation of "ID" with upper or lowercase letters.) There is no error message when a table is created using "ID" as a column name, but that column will not be accessible and the table is practically unusable. |
| Workaround | Use another name for the column. | Use another name for the column. |
|  |  |  |
|  |  |  |
| Reference | 2284355 | 2284355 |
| Problem | In an OpenBase Lite model, an attribute with Value Class of NSDecimalNumber or BigDecimal can overflow the indicated precision | In an OpenBase Lite model, an attribute with Value Class of NSDecimalNumber or BigDecimal can overflow the indicated precision |
| Description | If the actual value in an enterprise object exceeds the precision of the attribute that maps to an NSDecimalNumber (Objective-C) or BigDecimal (Java), memory can become corrupted when the value is written to the OpenBase Lite database. | If the actual value in an enterprise object exceeds the precision of the attribute that maps to an NSDecimalNumber (Objective-C) or BigDecimal (Java), memory can become corrupted when the value is written to the OpenBase Lite database. |
| Workaround | Make sure that your EOModel has the correct precision set for the attribute, and do not try to use values that are beyond that precision. | Make sure that your EOModel has the correct precision set for the attribute, and do not try to use values that are beyond that precision. |
|  |  |  |
|  |  |  |
| Reference | 2282377 | 2282377 |
| Problem | OpenBase Lite changes the current working directory | OpenBase Lite changes the current working directory |
| Description | When OpenBase Lite connects to a database, it changes the current working directory to the database directory. If your code expects the current working directory to remain the same as it was when the application was launched, it may not work correctly. | When OpenBase Lite connects to a database, it changes the current working directory to the database directory. If your code expects the current working directory to remain the same as it was when the application was launched, it may not work correctly. |
| Workaround | Your code should use absolute pathnames, and should not depend on the current working directory. Command-line arguments for filenames should also be absolute pathnames. | Your code should use absolute pathnames, and should not depend on the current working directory. Command-line arguments for filenames should also be absolute pathnames. |
|  |  |  |
|  |  |  |
| Reference | 2276780 | 2276780 |
| Problem | OpenBase Lite logs a spurious error message if EO_PK_TABLE doesn't exist | OpenBase Lite logs a spurious error message if EO_PK_TABLE doesn't exist |
| Description | The obliteadaptor generates primary keys from an EO_PK_TABLE. The adaptor knows how to create the table if it doesn't exist. However, the OpenBaseLiteAPI.framework still writes a log message: "SQL ERROR - [position 26, near 'WHERE'] (1) table 'EO_PK_TABLE' does not exist." This can safely be ignored. | The obliteadaptor generates primary keys from an EO_PK_TABLE. The adaptor knows how to create the table if it doesn't exist. However, the OpenBaseLiteAPI.framework still writes a log message: "SQL ERROR - [position 26, near 'WHERE'] (1) table 'EO_PK_TABLE' does not exist." This can safely be ignored. |
| Workaround | None necessary, just ignore the spurious error message. | None necessary, just ignore the spurious error message. |
|  |  |  |
|  |  |  |

---

### Oracle Adaptor

|  |  |  |
| --- | --- | --- |
| Reference | 2429341 | 2429341 |
| Problem | Reverse engineering an Oracle 8.1.5 database causes a strange Oracle exception to be raised. | Reverse engineering an Oracle 8.1.5 database causes a strange Oracle exception to be raised. |
| Description | During the process of reverse engineering the database, EOModeler (or ProjectBuilder) attempts to analyze all of the existing stored procedures. Some of the new stored procedures in Oracle 8.1.5 contain data types that cause the Oracle adaptor to raise an exception. The EOEntities, EOAttributes, and EORelationships are fine, but you aren't likely to see any stored procedures.    This problem is slightly worse if you are reverse engineering a model as part of the process for creating a new "WebObjects Application" from within ProjectBuilder. In that case the project creation fails part way through the task, leaving you with a non-functional project. | During the process of reverse engineering the database, EOModeler (or ProjectBuilder) attempts to analyze all of the existing stored procedures. Some of the new stored procedures in Oracle 8.1.5 contain data types that cause the Oracle adaptor to raise an exception. The EOEntities, EOAttributes, and EORelationships are fine, but you aren't likely to see any stored procedures.    This problem is slightly worse if you are reverse engineering a model as part of the process for creating a new "WebObjects Application" from within ProjectBuilder. In that case the project creation fails part way through the task, leaving you with a non-functional project. |
| Workaround | The easiest workaround is to skip the stored-procedure reverse-engineering step. If you need any stored procedures in your model, you'll need to explictly remove the stored procedures in the CTXSYS and SYS schemas from the list of those selected or select only the stored procedures you need. | The easiest workaround is to skip the stored-procedure reverse-engineering step. If you need any stored procedures in your model, you'll need to explictly remove the stored procedures in the CTXSYS and SYS schemas from the list of those selected or select only the stored procedures you need. |
|  |  |  |
|  |  |  |
| Reference | 2177990 | 2177990 |
| Problem | The primary-key-support creation code can die, causing subsequent database installation procedures to fail. | The primary-key-support creation code can die, causing subsequent database installation procedures to fail. |
| Description | Sometimes when you run the install_database script or use the schema object creation window in EOModeler, one of the following errors may occur:    Mar 27 10:19:34 eoutil[1577] Exception running dump: ORA-00955: name is already used by an existing object  create table !!! eo_temp_table as select max(MOVIE_ID) counter from MOVIE    OR    Mar 27 10:27:54 eoutil[1591] Exception running dump: ORA-00955: name is already used by an existing object  create procedure !!! eo_set_sequence is  xxx number;  yyy number;  begin  select max(counter) into xxx from eo_temp_table;  if xxx is not NULL then  yyy := 0;  while (yyy < xxx) loop  select MOVIE_SEQ.nextval into yyy from dual;  end loop;  end if;  end;    The reason for these errors is as follows. If the primary-key-support code dies unexpectedly, it can leave the eo_set_sequence stored procedure and the eo_temp_table table in the user's schema. This isn't a problem right away, but any subsequent attempt to run the install_database script will fail because the statements that attempt to create these schema objects will fail, and the data loading will stop before it is finished. | Sometimes when you run the install_database script or use the schema object creation window in EOModeler, one of the following errors may occur:    Mar 27 10:19:34 eoutil[1577] Exception running dump: ORA-00955: name is already used by an existing object  create table !!! eo_temp_table as select max(MOVIE_ID) counter from MOVIE    OR    Mar 27 10:27:54 eoutil[1591] Exception running dump: ORA-00955: name is already used by an existing object  create procedure !!! eo_set_sequence is  xxx number;  yyy number;  begin  select max(counter) into xxx from eo_temp_table;  if xxx is not NULL then  yyy := 0;  while (yyy < xxx) loop  select MOVIE_SEQ.nextval into yyy from dual;  end loop;  end if;  end;    The reason for these errors is as follows. If the primary-key-support code dies unexpectedly, it can leave the eo_set_sequence stored procedure and the eo_temp_table table in the user's schema. This isn't a problem right away, but any subsequent attempt to run the install_database script will fail because the statements that attempt to create these schema objects will fail, and the data loading will stop before it is finished. |
| Workaround | Use the following commands from SQLPlus to remove these objects before you attempt to create the schema objects with the install_database script:    SQL> drop table eo_temp_table;  SQL> drop procedure eo_set_sequence; | Use the following commands from SQLPlus to remove these objects before you attempt to create the schema objects with the install_database script:    SQL> drop table eo_temp_table;  SQL> drop procedure eo_set_sequence; |
|  |  |  |
|  |  |  |
| Reference | 2177517 | 2177517 |
| Problem | Updating LONG RAW columns in Oracle with lockingOnDemand causes an exception. | Updating LONG RAW columns in Oracle with lockingOnDemand causes an exception. |
| Description | Using lockingOnDemand on Oracle, when you try to update an enterprise object with an attribute that maps to a LONG RAW columm, the following exception is raised:    "fetchObject -- EODatabaseChannel 0x12345678: attempt to lock object that has out of date snapshot".    This is because the Oracle Database sometimes returns incorrect BLOB values when the Framework sends "SELECT ... <long-raw-column,... FOR UPDATE". So when the EODatabaseChannel attempts to acquire a lock on the row, the results of the SELECT don't match the results we got on the last SELECT (without the FOR UPDATE clause). | Using lockingOnDemand on Oracle, when you try to update an enterprise object with an attribute that maps to a LONG RAW columm, the following exception is raised:    "fetchObject -- EODatabaseChannel 0x12345678: attempt to lock object that has out of date snapshot".    This is because the Oracle Database sometimes returns incorrect BLOB values when the Framework sends "SELECT ... <long-raw-column,... FOR UPDATE". So when the EODatabaseChannel attempts to acquire a lock on the row, the results of the SELECT don't match the results we got on the last SELECT (without the FOR UPDATE clause). |
| Workaround | You cannot use the lockingOnDemand mode of locking if you are going to be updating tables with LONG RAW columns that are marked used for locking in the model. Mark the long columns as not used for locking. | You cannot use the lockingOnDemand mode of locking if you are going to be updating tables with LONG RAW columns that are marked used for locking in the model. Mark the long columns as not used for locking. |
|  |  |  |
|  |  |  |
| Reference | 2177366 | 2177366 |
| Problem | I'm getting the "ORA-01786: FOR UPDATE of this query expression is not allowed" error when I run my app. | I'm getting the "ORA-01786: FOR UPDATE of this query expression is not allowed" error when I run my app. |
| Description | If you are using the Pessimistic Locking mode, and you are using batch fauling or prefetching of relationships, EOF can generate a SQL statement like the following:  <OracleSQLExpression: "SELECT DISTINCT t0.CATEGORY, t0.DATE_RELEASED, t0.LANGUAGE, t0.MOVIE_ID, t0.RATING, t0.REVENUE, t0.STUDIO_ID, t0.TITLE FROM DIRECTOR t1, MOVIE t0 WHERE t1.TALENT_ID = :talentID AND t0.MOVIE_ID = t1.MOVIE_ID FOR UPDATE" withBindings:{talentID = 87; }>    This statement with fail with the ORA-01786 error. The Oracle RDBMS doesn't support the use of DISTINCT with the FOR UPDATE clause. | If you are using the Pessimistic Locking mode, and you are using batch fauling or prefetching of relationships, EOF can generate a SQL statement like the following:  <OracleSQLExpression: "SELECT DISTINCT t0.CATEGORY, t0.DATE_RELEASED, t0.LANGUAGE, t0.MOVIE_ID, t0.RATING, t0.REVENUE, t0.STUDIO_ID, t0.TITLE FROM DIRECTOR t1, MOVIE t0 WHERE t1.TALENT_ID = :talentID AND t0.MOVIE_ID = t1.MOVIE_ID FOR UPDATE" withBindings:{talentID = 87; }>    This statement with fail with the ORA-01786 error. The Oracle RDBMS doesn't support the use of DISTINCT with the FOR UPDATE clause. |
| Workaround | If you must use the Pessimistic locking mode against an Oracle database, you will not be able to use the batch faulting or prefetching features. | If you must use the Pessimistic locking mode against an Oracle database, you will not be able to use the batch faulting or prefetching features. |
|  |  |  |
|  |  |  |
| Reference | 2162425 | 2162425 |
| Problem | Oracle Adaptor doesn't read stored procedures inside of packages. | Oracle Adaptor doesn't read stored procedures inside of packages. |
| Description | There is no way to get the database to tell you the components (procedures and functions) that are inside a package definition. Clients can still create stored procedures in the model that will call into packages, it's just that model description using EOModeler won't create these at connect time. | There is no way to get the database to tell you the components (procedures and functions) that are inside a package definition. Clients can still create stored procedures in the model that will call into packages, it's just that model description using EOModeler won't create these at connect time. |
| Workaround | You can use EOModeler to create the stored procedure definitions in the model. Just set the external name of the stored procedure to package-name.procedure-name. | You can use EOModeler to create the stored procedure definitions in the model. Just set the external name of the stored procedure to package-name.procedure-name. |
|  |  |  |
|  |  |  |
| Reference | 2424670 | 2424670 |
| Problem | WOInfoCenter displays Objective-C reference documentation for the Java-wrapped database adaptors (Informix, ODBC, Oracle, and Sybase). | WOInfoCenter displays Objective-C reference documentation for the Java-wrapped database adaptors (Informix, ODBC, Oracle, and Sybase). |
| Description | WOInfoCenter is configured incorrectly. | WOInfoCenter is configured incorrectly. |
| Workaround | Access the documentation through the WebObjects Documentation Page. This file is called WOHomePage.html and is located in /System/Documentation/Developer/WebObjects/ on MacOS X Server and $(NEXT_ROOT)\Documentation\Developer\WebObjects on Windows NT.    The Java adaptor documentation is available in the Reference section of this page. | Access the documentation through the WebObjects Documentation Page. This file is called WOHomePage.html and is located in /System/Documentation/Developer/WebObjects/ on MacOS X Server and $(NEXT_ROOT)\Documentation\Developer\WebObjects on Windows NT.    The Java adaptor documentation is available in the Reference section of this page. |
|  |  |  |
|  |  |  |

---

### Informix Adaptor

|  |  |  |
| --- | --- | --- |
| Reference | 2281550 | 2281550 |
| Problem | The Informix client library cannot be called from multiple threads | The Informix client library cannot be called from multiple threads |
| Description | On Windows NT, a multi-threaded application that uses the Informix client library produces an error of the form "Informix Error -180 no connection". On Solaris, a different error is produced. The Informix client library cannot be called from multiple threads. | On Windows NT, a multi-threaded application that uses the Informix client library produces an error of the form "Informix Error -180 no connection". On Solaris, a different error is produced. The Informix client library cannot be called from multiple threads. |
| Workaround | Run you application with WOWorkerThreadCount set to 0 or 1 on NT, and 0 on Solaris. | Run you application with WOWorkerThreadCount set to 0 or 1 on NT, and 0 on Solaris. |
|  |  |  |
|  |  |  |
| Reference | 2239652 | 2239652 |
| Problem | Can't create an Informix database from within EOModeler | Can't create an Informix database from within EOModeler |
| Description | Creation of a new Informix database from within EOModeler generates a "Not able to create a database during an explicit database connection" error. This is due to the fact that the Informix API won't let you create a new database once you've specified that you're using an existing one; the EOInformixAdaptor as currently implemented always specifies a database when it connects. | Creation of a new Informix database from within EOModeler generates a "Not able to create a database during an explicit database connection" error. This is due to the fact that the Informix API won't let you create a new database once you've specified that you're using an existing one; the EOInformixAdaptor as currently implemented always specifies a database when it connects. |
| Workaround | Copy the database creation statements out of the SQL text area and paste them into a tool like dbaccess. | Copy the database creation statements out of the SQL text area and paste them into a tool like dbaccess. |
|  |  |  |
|  |  |  |
| Reference | 2170232 | 2170232 |
| Problem | Informix adaptor raises an exception when you try to sort on attributes that are not in the select list | Informix adaptor raises an exception when you try to sort on attributes that are not in the select list |
| Description | Due to a restriction in the Informix adaptor, it's not possible to sort on attributes that aren't included in the select list. This means that it isn't possible to sort the results using an attribute that's not marked on the entity as either a primary key, used for locking, or a class property. | Due to a restriction in the Informix adaptor, it's not possible to sort on attributes that aren't included in the select list. This means that it isn't possible to sort the results using an attribute that's not marked on the entity as either a primary key, used for locking, or a class property. |
| Workaround | If possible, add the attribute to the entity and mark it as used for locking. Otherwise, there is no workaround. | If possible, add the attribute to the entity and mark it as used for locking. Otherwise, there is no workaround. |
|  |  |  |
|  |  |  |

---

### ODBC Adaptor

|  |  |  |
| --- | --- | --- |
| Reference | 2382074 | 2382074 |
| Problem | Using Wildcard Operator '%' with LIKE May Produce Inconsistent Row Patterns with SQL Server 7.0. | Using Wildcard Operator '%' with LIKE May Produce Inconsistent Row Patterns with SQL Server 7.0. |
| Description | The Microsoft Knowledge Base has the following article: ID Q237793, last revised 8/27/99, "BUG: Using Wildcard Operator '%' with LIKE May Produce Inconsistent Row Patterns", Bug # 55911 (SQLBUG_70). For instance, specifying a search for "title LIKE 'Star%'" finds 'Star Wars', but specifying "title LIKE 'S%'" finds nothing. | The Microsoft Knowledge Base has the following article: ID Q237793, last revised 8/27/99, "BUG: Using Wildcard Operator '%' with LIKE May Produce Inconsistent Row Patterns", Bug # 55911 (SQLBUG_70). For instance, specifying a search for "title LIKE 'Star%'" finds 'Star Wars', but specifying "title LIKE 'S%'" finds nothing. |
| Workaround | Contact Microsoft for a patch. | Contact Microsoft for a patch. |
|  |  |  |
|  |  |  |
| Reference | 2226610 | 2226610 |
| Problem | Some bugs in old versions of the ODBCJT32.DLL (used to access Microsoft Access) can cause problems with primary key generation in the ODBC Adaptor. | Some bugs in old versions of the ODBCJT32.DLL (used to access Microsoft Access) can cause problems with primary key generation in the ODBC Adaptor. |
| Description | The ODBC manager reports an invalid SQL statement when updating the EO_PK_TABLE. ODBCJT32.DLL version 3.40.2728 causes this problem, but the more recent ODBCJT32.DLL version 3.51.1029 works correctly. The ODBC Control Panel can be used to check the version of the ODBC drivers installed on a Windows NT machine. Open the ODBC Control Panel and click on the tab labeled "ODBC Drivers". | The ODBC manager reports an invalid SQL statement when updating the EO_PK_TABLE. ODBCJT32.DLL version 3.40.2728 causes this problem, but the more recent ODBCJT32.DLL version 3.51.1029 works correctly. The ODBC Control Panel can be used to check the version of the ODBC drivers installed on a Windows NT machine. Open the ODBC Control Panel and click on the tab labeled "ODBC Drivers". |
| Workaround | The latest ODBC manager and drivers for Windows NT are available from Microsoft. See <http://www.microsoft.com/data/mdac15.htm>. | The latest ODBC manager and drivers for Windows NT are available from Microsoft. See <http://www.microsoft.com/data/mdac15.htm>. |
|  |  |  |
|  |  |  |
