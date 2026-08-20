---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.06.html
archived_at: '2026-07-18T01:17:43.364087Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Support%20for%20the%20OpenBase%20Lite%20Database.md)

# New Convenience API

Enterprise Objects Framework 3.0 introduces new API to facilitate common programming tasks. Tasks that used to take several lines of code now only take one. The following sections describe the new convenience API.

## EOUtilities

Most of the new convenience API is implemented in EOUtilities. In Objective-C, EOUtilities is a category on EOEditingContext provided in EOAccess. In Java, it's a new class called EOUtilities in EOAccess. The Objective-C and Java methods work the same way, but you invoke them differently. For example, compare the invocations for the following method:
Objective-C

```
[editingContext objectsForEntityNamed:entityName];
```


Java

```
EOUtilities.objectsForEntityNamed(editingContext, entityName);
```


Both versions of the method require an editing context into which the objects should be fetched. In Objective-C, the editing context is the receiver of the message. In Java, the editing context must be passed as an argument.
__Note:__  The Objective-C source code for EOUtilities is available as an example. On Rhapsody systems, see __/System/Developer/Examples/EnterpriseObjects/Sources/EOUtilities__. On NT, see __NEXT_ROOT/Developer/Examples/EnterpriseObjects/Sources/EOUtilities__.
The complete documentation for the Objective-C EOUtilities methods are documented in the "EOEditingContext Additions" class specification (EOAccess). The corresponding Java EOUtilities API documentation is available in the EOUtilities class specification (EOAccess). The following tables summarize the EOUtilities methods.
__Note:__  All the Java EOUtilities methods are static methods.

|  Fetching Enterprise Objects |  Fetching Enterprise Objects |
|  objectsForEntityNamed: |  Fetches and returns the enterprise objects associated with the specified entity. |
|  objectsOfClass: |  Fetches and returns the enterprise objects associated with the specified class. Raises or throws an exception if more than one entity for the class exists. |
|  objectsWithFetchSpecificationNamed:entityNamed:bindings: (Objective-C)  objectsWithFetchSpecificationAndBindings (Java) |  Fetches and returns the enterprise objects retrieved with the specified fetch specification and bindings. (For more information on bindings, see "[Binding to Complex Qualifiers](Binding%20to%20Complex%20Qualifiers.md#apple-ha3deni).") |
|  objectWithFetchSpecificationNamed:entityNamed:bindings: (Objective-C)  objectWithFetchSpecificationAndBindings (Java) |  Same as the corresponding __objects...__ method (immediately above), except this method raises or throws an exception unless exactly one object is retrieved. |
|  objectsForEntityNamed:qualifierFormat: (Objective-C)  objectsWithQualifierFormat (Java) |  Creates a qualifier with the provided format string and returns matching enterprise objects. |
|  objectForEntityNamed:qualifierFormat: (Objective-C)  objectWithQualifierFormat (Java) |  Same as the corresponding __objects...__ method (immediately above), except this method raises or throws an exception unless exactly one object is retrieved. |
|  objectsMatchingValue:forKey:entityNamed: (Objective-C)  objectsMatchingKeyAndValue (Java) |  Creates an EOKeyValueQualifier with the specified key and value and returns matching enterprise objects. |
|  objectMatchingValue:forKey:entityNamed: (Objective-C)  objectMatchingKeyAndValue (Java) |  Same as the corresponding __objects...__ method (immediately above), except this method raises or throws an exception unless exactly one object is retrieved. |
|  objectsMatchingValues:entityNamed: (Objective-C)  objectsMatchingValues (Java) |  Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching enterprise objects. |
|  objectMatchingValues:entityNamed: (Objective-C)  objectMatchingValues (Java) |  Same as the corresponding __objects...__ method (immediately above), except this method raises or throws an exception unless exactly one object is retrieved. |
|  objectWithPrimaryKeyValue:entityNamed: (Objective-C)  objectWithPrimaryKeyValue (Java) |  Fetches and returns the enterprise object identified by the specified primary key value. For use only with enterprise objects that have non-compound primary keys. Raises or throws an exception unless exactly one object is retrieved. |
|  objectWithPrimaryKey:entityNamed: (Objective-C)  objectWithPrimaryKey (Java) |  Fetches and returns the enterprise object identified by the specified primary key dictionary. Raises or throws an exception unless exactly one object is retrieved. |

```
```

|  Fetching Raw Rows  (For information on raw rows, see "[Raw Row Fetching](Raw%20Row%20Fetching.md#apple-hezdcnq).") |  Fetching Raw Rows  (For information on raw rows, see "[Raw Row Fetching](Raw%20Row%20Fetching.md#apple-hezdcnq).") |
|  rawRowsForEntityNamed:qualifierFormat: (Objective-C)  rawRowsWithQualifierFormat (Java) |  Creates a qualifier for the specified entity and with the specified qualifier format and returns matching raw row dictionaries. |
|  rawRowsMatchingValue:forKey:entityNamed: (Objective-C)  rawRowsMatchingKeyAndValue (Java) |  Creates an EOKeyValueQualifier with the specified key and value and returns matching raw rows. |
|  rawRowsMatchingValues:entityNamed: (Objective-C)  rawRowsMatchingValues (Java) |  Creates EOKeyValueQualifiers for each key-value pair in the specified dictionary, ANDs these qualifiers together into an EOAndQualifier, and returns matching raw rows. |
|  rawRowsWithSQL:modelNamed: (Objective-C)  rawRowsForSQL (Java) |  Evaluates the specified SQL and returns the resulting raw rows. |
|  rawRowsWithStoredProcedureNamed:arguments: (Objective-C)  rawRowsForStoredProcedureNamed (Java) |  Executes the specified stored procedure with the provided arguments and returns the resulting raw rows. |
|  executeStoredProcedureNamed:arguments: (Objective-C)  executeStoredProcedureNamed (Java) |  Executes the specified stored procedure with the provided arguments. Returns the stored procedure's return values (if any). Use only with stored procedures that don't return results rows. |
|  objectFromRawRow:entityNamed: (Objective-C)  objectFromRawRow (Java) |  Fetches and returns the object corresponding to the specified raw row (using EOEditingContext's faultForRawRow:entityNamed: in Objective-C or faultForRawRow in Java). This method can only be used on raw rows that include the row's primary key. |

```
```

|  Accessing the Enterprise Objects Framework Stack |  Accessing the Enterprise Objects Framework Stack |
|  databaseContextForModelNamed: |  Returns the database context used to service the specified model. |
|  connectWithModelNamed:connectionDictionaryOverrides: (Objective-C)  connectWithModelNamed (Java) |  Connects to the database using the connection information in the specified model and the provided overrides dictionary. This method facilitates per-session database logins in WebObjects applications. Typically, you'd put a login name and password in the overrides dictionary and otherwise use the values in the model's connection dictionary. |

```
```

|  Accessing Enterprise Object Data |  Accessing Enterprise Object Data |
|  primaryKeyForObject: |  Returns the primary key dictionary for the specified enterprise object. |
|  destinationKeyForSourceObject:relationshipNamed: (Objective-C)  destinationKeyForSourceObject (Java) |  Returns the foreign key for the rows at the destination entity of the specified relationship. |
|  localInstanceOfObject: |  Translates the specified enterprise object from one editing context to another. |
|  localInstancesOfObjects: |  Translates the specified enterprise objects from one editing context to another. |

```
```

|  Accessing Model Information |  Accessing Model Information |
|  modelGroup |  Returns the model group associated with the editing context's root object store, an EOObjectStoreCoordinator. |
|  entityNamed: |  Returns the entity with the specified name. Raises or throws an exception if the specified entity can't be found. |
|  entityForClass: |  Returns the entity associated with the specified class. Raises or throws an exception if the specified entity can't be found or if more than one entity is associated with the class. |
|  entityForObject: |  Returns the entity associated with the provided enterprise object. Raises or throws an exception if the specified entity can't be found. |

```
```


## Supporting Convenience Methods

The following tables describe the remainder of the convenience API.

|  EOQualifier |  EOQualifier |
|  qualifierToMatchAllValues: |  Takes a dictionary of search criteria, from which the method creates EOKeyValueQualifiers (one for each dictionary entry). The method ANDs these qualifiers together, and returns the resulting EOAndQualifier. |
|  qualifierToMatchAnyValues: |  Takes a dictionary of search criteria, from which the method creates EOKeyValueQualifiers (one for each dictionary entry). The method ORs these qualifiers together, and returns the resulting EOOrQualifier. |

```
```

|  EODatabaseContext |  EODatabaseContext |
|  forceConnectionWithModel: connectionDictionaryOverrides: editingContext: (Objective-C)  forceConnectionWithModel: (Java) |  Added to facilitate per-session database logins in WebObjects applications, this method connects to the database using the provided model's connection information and the provided overrides dictionary. |

```
```

|  EOModelGroup |  EOModelGroup |
|  storedProcedureNamed: |  Returns the stored procedure identified by the provided name. |

```
```

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Changes%20to%20EOModeler.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
