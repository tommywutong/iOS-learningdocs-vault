---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOEditingContextAdditions.html
archived_at: '2026-07-18T01:28:24.090454Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODatabaseContextDelegation.md)
[!](EOModelGroupClassDelegation.md)

---

# EOEditingContext `Additions`

(informal protocol)

EOEditingContext

__Declared in:__
EOAccess/EOUtilities.h

---

## Class Description

EOEditingContext Additions is a collection of convenience methods intended to make common operations with EOF easier. EOEditingContext Additions is a category on EOEditingContext provided in EOAccess.

__Note:__
The Objective-C source code for EOUtilities is available as an example. On Mac OS X Server
systems, see `/System/Developer/Examples/EnterpriseObjects/Sources/EOUtilities`. On NT, see
$_NEXT_ROOT_`\Developer\Examples\EnterpriseObjects\Sources\EOUtilities`.

---

## Method Types

**Fetching multiple objects**

**[- objectsForEntityNamed:](#apple-giydony)

**[- objectsForEntityNamed:qualifierFormat:](#apple-gi4tmni)

**[- objectsMatchingValue:forKey:entityNamed:](#apple-gi3tcoa)

**[- objectsMatchingValues:entityNamed:](#apple-gi3temy)

**[- objectsOfClass:](#apple-giytama)

**[- objectsWithFetchSpecificationNamed:entityNamed:bindings:](#apple-giytami)************

**Fetching single objects**

**[- objectForEntityNamed:qualifierFormat:](#apple-gi3tgna)

**[- objectMatchingValue:forKey:entityNamed:](#apple-gmzdqoa)

**[- objectMatchingValues:entityNamed:](#apple-gi3tioi)

**[- objectWithFetchSpecificationNamed:entityNamed:bindings:](#apple-gi3taoa)

**[- objectWithPrimaryKey:entityNamed:](#apple-gi3tkoi)

**[- objectWithPrimaryKeyValue:entityNamed:](#apple-gi3tmoi)************

**Fetching raw rows**

**[- executeStoredProcedureNamed:arguments:](#apple-gi4dcna)

**[- objectFromRawRow:entityNamed:](#apple-gi4dena)

**[- rawRowsForEntityNamed:qualifierFormat:](#apple-gi3tooi)

**[- rawRowsMatchingValue:forKey:entityNamed:](#apple-gi3tqna)

**[- rawRowsMatchingValues:entityNamed:](#apple-gi3tqoi)

**[- rawRowsWithSQL:modelNamed:](#apple-gi3tsoi)

**[- rawRowsWithStoredProcedureNamed:arguments:](#apple-gi4dana)**************

**Accessing the EOF stack**

**[- connectWithModelNamed:connectionDictionaryOverrides:](#apple-gmztgna)

**[- databaseContextForModelNamed:](#apple-gi4dkma)****

**Accessing object data**

**[- destinationKeyForSourceObject:relationshipNamed:](#apple-gi4doma)

**[- localInstanceOfObject:](#apple-gi4dqnq)

**[- localInstancesOfObjects:](#apple-gi4dsmi)

**[- primaryKeyForObject:](#apple-gi4dmma)********

**Accessing model information**

**[- entityForClass:](#apple-gi4tcny)

**[- entityForObject:](#apple-gi4temq)

**[- entityNamed:](#apple-gi4teoa)

**[- modelGroup](#apple-gi4dsny)********

---

## Instance Methods

---

### connectWithModelNamed:connectionDictionaryOverrides:

- (void)`connectWithModelNamed:`(NSString \*)_modelName_
`connectionDictionaryOverrides:`(NSDictionary \*)_overrides_

Connects to the database using the connection information in the specified model and the provided overrides dictionary. This method facilitates per-session database logins in WebObjects applications. Typically, you'd put a login name and password in the overrides dictionary and otherwise use the values in the model's connection dictionary. Raises an exception if the connection failed.

---

### databaseContextForModelNamed:

- (EODatabaseContext \*)`databaseContextForModelNamed:`(NSString \*)_entityName_

Returns the database context used to service the specified model.

---

### destinationKeyForSourceObject:relationshipNamed:

- (NSDictionary \*)`destinationKeyForSourceObject:`(id)_object_
`relationshipNamed:`(NSString \*)_entityName_

Returns the foreign key for the rows at the destination entity of the specified relationship. As an example, given entities Department and Employee with a relationship called "department" joining `Department.ID Employee.deptID`, invoking this method on a Department object with ID equal to 5 will return a dictionary with a value of 5 for the deptID key.

__See also:__
[- `primaryKeyForObject:`](#apple-gi4dmma)

---

### entityForClass:

- (EOEntity \*)`entityForClass:`(Class)_classObject_

Returns the entity associated with the specified class. Raises an exception if the specified entity can't be found or if more than one entity is associated with the class.

__See also:__
[- `entityForObject:`](#apple-gi4temq), [- `entityNamed:`](#apple-gi4teoa), [- `objectsOfClass:`](#apple-giytama)

---

### entityForObject:

- (EOEntity \*)`entityForObject:`(id)_object_

Returns the entity associated with the provided enterprise object. Raises an exception if the specified entity can't be found.

__See also:__
[- `entityForClass:`](#apple-gi4tcny), [- `entityNamed:`](#apple-gi4teoa)

---

### entityNamed:

- (EOEntity \*)`entityNamed:`(NSString \*)_entityName_

Returns the entity with the specified name. Raises an exception if the specified entity can't be found.

__See also:__
[- `entityForClass:`](#apple-gi4tcny), [- `entityForObject:`](#apple-gi4temq)

---

### executeStoredProcedureNamed:arguments:

- (NSDictionary \*)`executeStoredProcedureNamed:`(NSString \*)_storedProcedureName_
`arguments:`(NSDictionary \*)_arguments_

Executes the specified stored procedure with the provided arguments. Returns the stored procedure's return values (if any). Use only with stored procedures that don't return results rows.

__See also:__
[- `rawRowsWithStoredProcedureNamed:arguments:`](#apple-gi4dana)

---

### localInstanceOfObject:

- (id)`localInstanceOfObject:`(id)_object_

Translates the specified enterprise object from another editing context to the specified one.

__See also:__
[- `localInstancesOfObjects:`](#apple-gi4dsmi)

---

### localInstancesOfObjects:

- (NSArray \*)`localInstancesOfObjects:`(NSArray \*)_objects_

Translates the specified enterprise objects from another editing context to the specified one.

__See also:__
[- `localInstanceOfObject:`](#apple-gi4dqnq)

---

### modelGroup

- (EOModelGroup \*)`modelGroup`

Returns the model group associated with the editing context's root object store, an EOObjectStoreCoordinator.

---

### objectForEntityNamed:qualifierFormat:

- (id)`objectForEntityNamed:`(NSString \*)_entityName_ `qualifierFormat:`(NSString \*)_format_, ...

Creates a qualifier with the provided format string and arguments, and returns matching enterprise objects. Raises an EOMoreThanOneException unless exactly one object is retrieved.

__See also:__
[- `objectsForEntityNamed:qualifierFormat:`](#apple-gi4tmni), [- `rawRowsForEntityNamed:qualifierFormat:`](#apple-gi3tooi)

---

### objectFromRawRow:entityNamed:

- (id)`objectFromRawRow:`(NSDictionary \*)_row_ `entityNamed:`(NSString \*)_entityName_

Fetches and returns the object corresponding to the specified raw row (using EOEditingContext's faultForRawRow:entityNamed:). This method can only be used on raw rows that include the row's primary key.

---

### objectMatchingValue:forKey:entityNamed:

- (id)`objectMatchingValue:`(id)_value_ `forKey:`(NSString \*)_key_ `entityNamed:`(NSString \*)_entityName_

Creates an EOKeyValueQualifier with the specified key and value and returns matching enterprise objects. Raises an EOMoreThanOneException unless exactly one object is retrieved.

__See also:__
[- `objectMatchingValues:entityNamed:`](#apple-gi3tioi), [- `objectsMatchingValue:forKey:entityNamed:`](#apple-gi3tcoa)

---

### objectMatchingValues:entityNamed:

- (id)`objectMatchingValues:`(NSDictionary \*)_values_ `entityNamed:`(NSString \*)_entityName_

Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching enterprise objects. Raises an EOMoreThanOneException unless exactly one object is retrieved.

__See also:__
[- `objectMatchingValue:forKey:entityNamed:`](#apple-gmzdqoa), [- `objectsMatchingValues:entityNamed:`](#apple-gi3temy)

---

### objectsForEntityNamed:

- (NSArray \*)`objectsForEntityNamed:`(NSString \*)_entityName_

Fetches and returns the enterprise objects associated with the specified entity.

__See also:__
[- `objectsForEntityNamed:qualifierFormat:`](#apple-gi4tmni), [- `objectsMatchingValue:forKey:entityNamed:`](#apple-gi3tcoa),
[- `objectsMatchingValues:entityNamed:`](#apple-gi3temy)

---

### objectsForEntityNamed:qualifierFormat:

- (NSArray \*)`objectsForEntityNamed:`(NSString \*)_entityName_
`qualifierFormat:`(NSString \*)_format_, ...

Creates a qualifier with the provided format string and arguments, and returns matching enterprise objects.

__See also:__
[- `objectForEntityNamed:qualifierFormat:`](#apple-gi3tgna), [- `objectsForEntityNamed:`](#apple-giydony)

---

### objectsMatchingValue:forKey:entityNamed:

- (NSArray \*)`objectsMatchingValue:`(id)_value_
`forKey:`(NSString \*)_key_
`entityNamed:`(NSString \*)_entityName_

Creates an EOKeyValueQualifier with the specified key and value and returns matching enterprise objects.

__See also:__
[- `objectMatchingValue:forKey:entityNamed:`](#apple-gmzdqoa), [- `objectsForEntityNamed:`](#apple-giydony),
[- `objectsMatchingValues:entityNamed:`](#apple-gi3temy)

---

### objectsMatchingValues:entityNamed:

- (NSArray \*)`objectsMatchingValues:`(NSDictionary \*)_values_ `entityNamed:`(NSString \*)_entityName_

Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching enterprise objects.

__See also:__
[- `objectMatchingValues:entityNamed:`](#apple-gi3tioi), [- `objectsForEntityNamed:`](#apple-giydony),
[- `objectsMatchingValue:forKey:entityNamed:`](#apple-gi3tcoa)

---

### objectsOfClass:

- (NSArray \*)`objectsOfClass:`(Class)_classObject_

Fetches and returns the enterprise objects associated with the specified class. Raises an EOMoreThanOneException if more than one entity for the class exists.

__See also:__
[- `entityForClass:`](#apple-gi4tcny)

---

### objectsWithFetchSpecificationNamed:entityNamed:bindings:

- (NSArray \*)`objectsWithFetchSpecificationNamed:`(NSString \*)_fetchSpecName_
`entityNamed:`(NSString \*)_entityName_ `bindings:`(NSDictionary \*)_bindings_

Fetches and returns the enterprise objects retrieved with the specified fetch specification and bindings.

__See also:__
[- `objectWithFetchSpecificationNamed:entityNamed:bindings:`](#apple-gi3taoa)

---

### objectWithFetchSpecificationNamed:entityNamed:bindings:

- (id)`objectWithFetchSpecificationNamed:`(NSString \*)_fetchSpecName_
`entityNamed:`(NSString \*)_entityName_
`bindings:`(NSDictionary \*)_bindings_

Fetches and returns the enterprise objects retrieved with the specified fetch specification and bindings. Raises an EOMoreThanOneException unless exactly one object is retrieved.

__See also:__
[- `objectsWithFetchSpecificationNamed:entityNamed:bindings:`](#apple-giytami)

---

### objectWithPrimaryKey:entityNamed:

- (id)`objectWithPrimaryKey:`(NSDictionary \*)_keyDictionary_ `entityNamed:`(NSString \*)_entityName_

Fetches and returns the enterprise object identified by the specified primary key dictionary. Raises an EOMoreThanOneException unless exactly one object is retrieved.

__See also:__
[- `objectMatchingValue:forKey:entityNamed:`](#apple-gmzdqoa), [- `objectWithPrimaryKeyValue:
entityNamed:`](#apple-gi3tmoi), [- `primaryKeyForObject:`](#apple-gi4dmma)

---

### objectWithPrimaryKeyValue:entityNamed:

- (id)`objectWithPrimaryKeyValue:`(id)_value_ `entityNamed:`(NSString \*)_entityName_

Fetches and returns the enterprise object identified by the specified primary key value. For use only with enterprise objects that have non-compound primary keys. Raises an EOMoreThanOneException unless exactly one object is retrieved.

__See also:__
[- `objectsMatchingValues:entityNamed:`](#apple-gi3temy), [- `objectWithPrimaryKey:entityNamed:`](#apple-gi3tkoi)

---

### primaryKeyForObject:

- (NSDictionary \*)`primaryKeyForObject:`(id)_object_

Returns the primary key dictionary for the specified enterprise object.

__See also:__
[- `objectWithPrimaryKey:entityNamed:`](#apple-gi3tkoi), [- `objectWithPrimaryKeyValue:entityNamed:`](#apple-gi3tmoi)

---

### rawRowsForEntityNamed:qualifierFormat:

- (NSArray \*)`rawRowsForEntityNamed:`(NSString \*)_entityName_
`qualifierFormat:`(NSString \*)_format_, ...;

Creates a qualifier for the specified entity and with the specified qualifier format and returns matching raw row dictionaries.

__See also:__
[- `objectsForEntityNamed:qualifierFormat:`](#apple-gi4tmni), [- `rawRowsWithSQL:modelNamed:`](#apple-gi3tsoi)

---

### rawRowsMatchingValue:forKey:entityNamed:

- (NSArray \*)`rawRowsMatchingValue:`(id)_value_
`forKey:`(NSString \*)_key_
`entityNamed:`(NSString \*)_entityName_

Creates an EOKeyValueQualifier with the specified key and value and returns matching raw rows.

__See also:__
[- `objectMatchingValue:forKey:entityNamed:`](#apple-gmzdqoa), [- `objectsMatchingValue:forKey:
entityNamed:`](#apple-gi3tcoa), [- `rawRowsMatchingValues:entityNamed:`](#apple-gi3tqoi)

---

### rawRowsMatchingValues:entityNamed:

- (NSArray \*)`rawRowsMatchingValues:`(NSDictionary \*)_values_
`entityNamed:`(NSString \*)_entityName_

Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching raw rows.

__See also:__
[- `objectMatchingValues:entityNamed:`](#apple-gi3tioi), [- `objectsMatchingValues:entityNamed:`](#apple-gi3temy),
[- `rawRowsMatchingValue:forKey:entityNamed:`](#apple-gi3tqna)

---

### rawRowsWithSQL:modelNamed:

- (NSArray \*)`rawRowsWithSQL:`(NSString \*)_sqlString_ `modelNamed:`(NSString \*)_modelName_

Evaluates the specified SQL and returns the resulting raw rows.

__See also:__
[- `rawRowsForEntityNamed:qualifierFormat:`](#apple-gi3tooi), [- `rawRowsWithStoredProcedureNamed:
arguments:`](#apple-gi4dana)

---

### rawRowsWithStoredProcedureNamed:arguments:

- (NSArray \*)`rawRowsWithStoredProcedureNamed:`(NSString \*)_storedProcedureName_
`arguments:`(NSDictionary \*)_arguments_

Executes the specified stored procedure with the provided arguments and returns the resulting raw rows.

__See also:__
[- `rawRowsWithSQL:modelNamed:`](#apple-gi3tsoi)

****

---

[!](EODatabaseContextDelegation.md)
[!](EOModelGroupClassDelegation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
