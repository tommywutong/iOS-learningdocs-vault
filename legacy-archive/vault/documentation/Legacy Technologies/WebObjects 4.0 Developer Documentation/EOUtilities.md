---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOUtilities.html
archived_at: '2026-07-18T01:28:14.935916Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EODatabaseContext.Delegate.md)
[!](EOModelGroup.ClassDelegate.md)

---

## EOUtilities

__Inherits From:__
NSObject

__Declared in:__
EOAccess/EOUtilities.h

### Class Description

EOUtilities is a collection of convenience methods intended to make common operations with EOF easier. EOUtilities is an EOAccess class that consists entirely of static methods-you never instantiate an EOUtilities object.

Each method requires an editing context into which the objects should be fetched; this editing context is passed as the first argument to each method in EOUtilities.

__Note:__
The Objective-C source code for EOUtilities is available as an example. On Mac OS X Server
systems, see `/System/Developer/Examples/EnterpriseObjects/Sources/EOUtilities`. On NT, see
$_NEXT_ROOT_`\Developer\Examples\EnterpriseObjects\Sources\EOUtilities`.

### Method Types

**Fetching multiple objects**

**[objectsForEntityNamed](#apple-giydony)

**[objectsWithQualifierFormat](#apple-gi4tmni)

**[objectsMatchingKeyAndValue](#apple-gi3tcoa)

**[objectsMatchingValues](#apple-gi3temy)

**[objectsOfClass](#apple-giytama)

**[objectsWithFetchSpecificationAndBindings](#apple-giytami)************

**Fetching single objects**

**[objectWithQualifierFormat](#apple-gi3tgna)

**[objectMatchingKeyAndValue](#apple-gmzdqoa)

**[objectMatchingValues](#apple-gi3tioi)

**[objectWithFetchSpecificationAndBindings](#apple-gi3taoa)

**[objectWithPrimaryKey](#apple-gi3tkoi)

**[objectWithPrimaryKeyValue](#apple-gi3tmoi)************

**Fetching raw rows**

**[executeStoredProcedureNamed](#apple-gi4dcna)

**[objectFromRawRow](#apple-gi4dena)

**[rawRowsWithQualifierFormat](#apple-gi3tooi)

**[rawRowsMatchingKeyAndValue](#apple-gi3tqna)

**[rawRowsMatchingValues](#apple-gi3tqoi)

**[rawRowsForSQL](#apple-gi3tsoi)

**[rawRowsWithStoredProcedureNamed](#apple-gi4dana)**************

**Accessing the EOF stack**

**[connectWithModelNamed](#apple-gmztgna)

**[databaseContextForModelNamed](#apple-gi4dkma)****

**Accessing object data**

**[destinationKeyForSourceObject](#apple-gi4doma)

**[localInstanceOfObject](#apple-gi4dqnq)

**[localInstancesOfObjects](#apple-gi4dsmi)

**[primaryKeyForObject](#apple-gi4dmma)********

**Accessing model information**

**[entityForClass](#apple-gi4tcny)

**[entityForObject](#apple-gi4temq)

**[entityNamed](#apple-gi4teoa)

**[modelGroup](#apple-gi4dsny)********

##

#### connectWithModelNamed

public static void `connectWithModelNamed`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _modelName_,
NSDictionary _overrides_)

Connects to the database using the connection information in the specified model and the provided overrides dictionary. This method facilitates per-session database logins in WebObjects applications. Typically, you'd put a login name and password in the overrides dictionary and otherwise use the values in the model's connection dictionary. Throws an exception if the connection failed.

#### databaseContextForModelNamed

public static EODatabaseContext `databaseContextForModelNamed`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_)

Returns the database context used to service the specified model.

#### destinationKeyForSourceObject

public static NSDictionary `destinationKeyForSourceObject`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.Object _object_,
java.lang.String _entityName_)

Returns the foreign key for the rows at the destination entity of the specified relationship. As an example, given entities Department and Employee with a relationship called "department" joining `Department.ID Employee.deptID`, invoking this method on a Department object with ID equal to 5 will return a dictionary with a value of 5 for the deptID key.

__See also:__
[`primaryKeyForObject`](#apple-gi4dmma)

#### entityForClass

public static EOEntity `entityForClass`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.Class _classObject_)

Returns the entity associated with the specified class. Throws an exception if the specified entity can't be found or if more than one entity is associated with the class.

__See also:__
[`entityForObject`](#apple-gi4temq), [`entityNamed`](#apple-gi4teoa), [`objectsOfClass`](#apple-giytama)

#### entityForObject

public static EOEntity `entityForObject`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.Object _object_)

Returns the entity associated with the provided enterprise object. Throws an exception if the specified entity can't be found.

__See also:__
[`entityForClass`](#apple-gi4tcny), [`entityNamed`](#apple-gi4teoa)

#### entityNamed

public static EOEntity `entityNamed`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_)

Returns the entity with the specified name. Throws an exception if the specified entity can't be found.

__See also:__
[`entityForClass`](#apple-gi4tcny), [`entityForObject`](#apple-gi4temq)

#### executeStoredProcedureNamed

public static NSDictionary `executeStoredProcedureNamed`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _storedProcedureName_,
NSDictionary _arguments_)

Executes the specified stored procedure with the provided arguments. Returns the stored procedure's return values (if any). Use only with stored procedures that don't return results rows.

__See also:__
[`rawRowsWithStoredProcedureNamed`](#apple-gi4dana)

#### localInstanceOfObject

public static java.lang.Object `localInstanceOfObject`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.Object _object_)

Translates the specified enterprise object from another editing context to the specified one.

__See also:__
[`localInstancesOfObjects`](#apple-gi4dsmi)

#### localInstancesOfObjects

public static NSArray `localInstancesOfObjects`(
com.apple.yellow.eocontrol.EOEditingContext, _editingContext,_NSArray _objects_)

Translates the specified enterprise objects from another editing context to the specified one.

__See also:__
[`localInstanceOfObject`](#apple-gi4dqnq)

#### modelGroup

public static EOModelGroup `modelGroup`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_)

Returns the model group associated with the editing context's root object store, an EOObjectStoreCoordinator.

#### objectWithQualifierFormat

public static java.lang.Object `objectWithQualifierFormat`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
java.lang.String _format_,
NSArray _arguments_)

Creates a qualifier with the provided format string and arguments, and returns matching enterprise objects. Throws an exception unless exactly one object is retrieved.

__See also:__
[`objectsWithQualifierFormat`](#apple-gi4tmni), [`rawRowsWithQualifierFormat`](#apple-gi3tooi)

#### objectFromRawRow

public static java.lang.Object `objectFromRawRow`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
NSDictionary _row_)

Fetches and returns the object corresponding to the specified raw row (using EOEditingContext's faultForRawRow). This method can only be used on raw rows that include the row's primary key.

#### objectMatchingKeyAndValue

public static java.lang.Object `objectMatchingKeyAndValue`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
java.lang.Object _value_,
java.lang.String _key_)

Creates an EOKeyValueQualifier with the specified key and value and returns matching enterprise objects. Throws an exception unless exactly one object is retrieved.

__See also:__
[`objectMatchingValues`](#apple-gi3tioi), [`objectsMatchingKeyAndValue`](#apple-gi3tcoa)

#### objectMatchingValues

public static java.lang.Object `objectMatchingValues`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
NSDictionary _values_)

Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching enterprise objects. Throws an exception unless exactly one object is retrieved.

__See also:__
[`objectMatchingKeyAndValue`](#apple-gmzdqoa), [`objectsMatchingValues`](#apple-gi3temy)

#### objectsForEntityNamed

public static NSArray `objectsForEntityNamed`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_)

Fetches and returns the enterprise objects associated with the specified entity.

__See also:__
[`objectsWithQualifierFormat`](#apple-gi4tmni), [`objectsMatchingKeyAndValue`](#apple-gi3tcoa), [`objectsMatchingValues`](#apple-gi3temy)

#### objectsWithQualifierFormat

public static NSArray `objectsWithQualifierFormat`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
java.lang.String _format_,
NSArray _arguments_)

Creates a qualifier with the provided format string and arguments, and returns matching enterprise objects.

__See also:__
[`objectWithQualifierFormat`](#apple-gi3tgna), [`objectsForEntityNamed`](#apple-giydony)

#### objectsMatchingKeyAndValue

public static NSArray `objectsMatchingKeyAndValue`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
java.lang.String _key_,
java.lang.Object _value_)

Creates an EOKeyValueQualifier with the specified key and value and returns matching enterprise objects.

__See also:__
[`objectMatchingKeyAndValue`](#apple-gmzdqoa), [`objectsForEntityNamed`](#apple-giydony), [`objectsMatchingValues`](#apple-gi3temy)

#### objectsMatchingValues

public static NSArray `objectsMatchingValues`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
NSDictionary _values_)

Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching enterprise objects.

__See also:__
[`objectMatchingValues`](#apple-gi3tioi), [`objectsForEntityNamed`](#apple-giydony), [`objectsMatchingKeyAndValue`](#apple-gi3tcoa)

#### objectsOfClass

public static NSArray `objectsOfClass`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.Class _classObject_)

Fetches and returns the enterprise objects associated with the specified class. Throws an exception if more than one entity for the class exists.

__See also:__
[`entityForClass`](#apple-gi4tcny)

#### objectsWithFetchSpecificationAndBindings

public static NSArray `objectsWithFetchSpecificationAndBindings`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _fetchSpecName_,
java.lang.String _entityName_,
NSDictionary _bindings_)

Fetches and returns the enterprise objects retrieved with the specified fetch specification and bindings.

__See also:__
[`objectWithFetchSpecificationAndBindings`](#apple-gi3taoa)

#### objectWithFetchSpecificationAndBindings

public static java.lang.Object `objectWithFetchSpecificationAndBindings`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _fetchSpecName_,
java.lang.String _entityName_,
NSDictionary _bindings_)

Fetches and returns the enterprise objects retrieved with the specified fetch specification and bindings. Throws an exception unless exactly one object is retrieved.

__See also:__
[`objectsWithFetchSpecificationAndBindings`](#apple-giytami)

#### objectWithPrimaryKey

public static java.lang.Object `objectWithPrimaryKey`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
NSDictionary _keyDictionary_)

Fetches and returns the enterprise object identified by the specified primary key dictionary. Throws an exception unless exactly one object is retrieved.

__See also:__
[`objectMatchingKeyAndValue`](#apple-gmzdqoa), [`objectWithPrimaryKeyValue`](#apple-gi3tmoi), [`primaryKeyForObject`](#apple-gi4dmma)

#### objectWithPrimaryKeyValue

public static java.lang.Object `objectWithPrimaryKeyValue`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
java.lang.Object _value_)

Fetches and returns the enterprise object identified by the specified primary key value. For use only with enterprise objects that have non-compound primary keys. Throws an exception unless exactly one object is retrieved.

__See also:__
[`objectsMatchingValues`](#apple-gi3temy), [`objectWithPrimaryKey`](#apple-gi3tkoi)

#### primaryKeyForObject

public static NSDictionary `primaryKeyForObject`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.Object _object_)

Returns the primary key dictionary for the specified enterprise object.

__See also:__
[`objectWithPrimaryKey`](#apple-gi3tkoi), [`objectWithPrimaryKeyValue`](#apple-gi3tmoi)

#### rawRowsWithQualifierFormat

public static NSArray `rawRowsWithQualifierFormat`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
java.lang.String _format_,
NSArray _arguments_)

Creates a qualifier for the specified entity and with the specified qualifier format and returns matching raw row dictionaries.

__See also:__
[`objectsWithQualifierFormat`](#apple-gi4tmni), [`rawRowsForSQL`](#apple-gi3tsoi)

#### rawRowsMatchingKeyAndValue

public static NSArray `rawRowsMatchingKeyAndValue`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
java.lang.String _key_,
java.lang.Object _value_);

Creates an EOKeyValueQualifier with the specified key and value and returns matching raw rows.

__See also:__
[`objectMatchingKeyAndValue`](#apple-gmzdqoa), [`objectsMatchingKeyAndValue`](#apple-gi3tcoa), [`rawRowsMatchingValues`](#apple-gi3tqoi)

#### rawRowsMatchingValues

public static NSArray `rawRowsMatchingValues`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _entityName_,
NSDictionary _values_)

Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching raw rows.

__See also:__
[`objectMatchingValues`](#apple-gi3tioi), [`objectsMatchingValues`](#apple-gi3temy), [`rawRowsMatchingKeyAndValue`](#apple-gi3tqna)

#### rawRowsForSQL

public static NSArray `rawRowsForSQL`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _sqlString_,
java.lang.String _modelName_)

Evaluates the specified SQL and returns the resulting raw rows.

__See also:__
[`rawRowsWithQualifierFormat`](#apple-gi3tooi), [`rawRowsWithStoredProcedureNamed`](#apple-gi4dana)

#### rawRowsWithStoredProcedureNamed

public static NSArray `rawRowsForStoredProcedureNamed`(
com.apple.yellow.eocontrol.EOEditingContext _editingContext_,
java.lang.String _storedProcedureName_,
NSDictionary _arguments_)

Executes the specified stored procedure with the provided arguments and returns the resulting raw rows.

__See also:__
[`rawRowsForSQL`](#apple-gi3tsoi)

****

---

[!](EODatabaseContext.Delegate.md)
[!](EOModelGroup.ClassDelegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
