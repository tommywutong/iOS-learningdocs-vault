---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.07.html
archived_at: '2026-07-15T07:58:01.941427Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](New%20Convenience%20API.md)

# Changes to EOModeler

EOModeler in release 3.0 has the following changes:

- Improvements in the way you create a model file and database from scratch
- Support for prototype attributes, which you can use to quickly set up attributes
- The ability to create and store complex queries (or EOFetchSpecifications)
- A different bundle loading procedure

Each is discussed in more detail in the following sections.

## Improved Database Creation Support

The most common way to create a model file is to use information stored in an already-created database. Sometimes, however, it's useful to create the model file first and use that model to create the empty database and generate the database tables. In release 3.0, EOModeler contains improvements that make it easier to create and delete the database:

- The adaptor login panels now allow you to create a new database or user.
- The SQL Generation panel now has options for creating a database and deleting a database.
- EOModeler now supports the definition of prototype attributes that you can use to quickly set up attributes in the new model (see the section "[Prototype Attributes](#apple-geydknrx)").

To create a model file and its database from scratch, do the following:

- Choose New from the Model menu.
- Select an adaptor.
- Enter connection information for the new database (user name, password, and so on).

Once the database is created, users will log into the database with this information.

- Click Create.
- Provide the administrator connection information.

The information you provide in this panel will be used to log into the database server to create the new database. The login information you provide must be for an account that has database creation permissions.

- Click Finish.
- Define the entities and attributes that you want the model to represent.
- Choose Generate SQL from the Property menu.
- Select the Create Tables option.
- Click the Execute SQL button.

### API for Database Creation and Deletion

This section describes new API that supports the database creation feature in EOModeler.

|  EOLoginPanel |  EOLoginPanel |
|  administrativeConnectionDictionaryForAdaptor: |  Returns the administrative connection dictionary, which contains the values (user name and password) needed to connect to the database server as the administrator. |
|  runPanelForAdaptor:validate:allowsCreation: (Objective-C)  runPanelForAdaptor (Java) |  Replaces runPanelForAdaptor:validate:. |

```
```

|  EOAdaptor |  EOAdaptor |
|  createDatabaseWithAdministrativeConnectionDictionary: and dropDatabaseWithAdministrativeConnectionDictionary: |  Creates or deletes the database specified in the receiver's connection dictionary, connecting to the database server using the information in the provided administrative connection dictionary. |

```
```

|  EOSQLExpression |  EOSQLExpression |
|  dropDatabaseStatementsForConnectionDictionary: administrativeConnectionDictionary: (Objective-C class method)  dropDatabaseStatementsForConnectionDictionary (Java static method) |  Generates the SQL statements to delete the database (or user for Oracle). Note that the statements generated only work if you are connected with administrative privileges. |
|  createDatabaseStatementsForConnectionDictionary: administrativeConnectionDictionary: (Objective-C class method)  createDatabaseStatementsForConnectionDictionary (Java static method) |  Generates the SQL statements that will create a database (or user for Oracle) that can be accessed by the provided connection dictionary and administrative connection dictionary. Note that the statements generated only work if you are connected with administrative privileges. |
|  schemaCreationStatementsForEntities:options: (Objective-C class method)  schemeCreationStatementsForEntities (Java static method) |  This method already exists, but takes these new keys to its option dictionary:  EOCreateDatabaseKey EODropDatabaseKey |

```
```

|  Option Keys for EOSQLExpression's schema creation methods |  Option Keys for EOSQLExpression's schema creation methods |
|  Objective-C  For use with schemaCreationScriptForEntities:options: and schemaCreationStatementsForEntities:options: |  Java  For use with schemaCreationScriptForEntities and schemaCreationStatementsForEntities |
|  EOCreateDatabaseKey |  EOSQLExpression.CreateDatabaseKey |
|  EOCreatePrimaryKeySupportKey |  EOSQLExpression.CreatePrimaryKeySupportKey |
|  EOCreateTablesKey |  EOSQLExpression.CreateTablesKey |
|  EODropDatabaseKey |  EOSQLExpression.DropDatabaseKey |
|  EODropPrimaryKeySupportKey |  EOSQLExpression.DropPrimaryKeySupportKey |
|  EODropTablesKey |  EOSQLExpression.DropTablesKey |
|  EOForeignKeyConstraintsKey |  EOSQLExpression.ForeignKeyConstraintsKey |
|  EOPrimaryKeyConstraintsKey |  EOSQLExpression.PrimaryKeyConstraintsKey |

```
```


## Prototype Attributes

To allow easier model creation from scratch, EOModeler now supports the concept of prototype attributes. Prototype attributes are just what they sound like - special EOAttributes from which other EOAttributes derive their settings. A prototype can specify any of the characteristics you normally define for an attribute. When you create an attribute, you can associate it with one of these prototypes, and the attribute's characteristics are then set from the prototype definition.
For example, suppose your adaptor contains a date prototype that defines the value class to be NSCalendarDate and the external type to be DATE. When you create an attribute and associate it with this date prototype, the attribute's value class is dynamically resolved to NSCalendarDate and its external type is dynamically resolved to DATE. If any of the prototype information is not correct for your attribute, you can override it. Simply set the property of the attribute to the correct value. The remaining attribute properties will still dynamically resolve to the values set in the prototype.
To associate an attribute with a prototype, use the table mode of the Model Editor. In the row for your attribute, choose a prototype from the combo box in the Prototype column. (If EOModeler doesn't display the Prototype column, activate it from the Columns pull-down menu.) The prototypes in the combo box come from three places:

- An EOEntity named __EO<adaptor-name>Prototypes__, where __<adaptor-name>__ is the name of the adaptor for your model (EOOraclePrototypes, for example)
- An EOEntity named __EOPrototypes__
- The adaptor for your model

So to create your own prototype, create a prototype entity-an entity named either __EO<adaptor-name>Prototypes__ or __EOPrototypes__-and add an attribute to it. Note that the __EO<adaptor-name>Prototypes__ and __EOPrototypes__ entities can be defined in the current model or in another model in the model group (all the models in your project are typically a part of the same model group).
When resolving a prototype name, Enterprise Objects Framework looks for prototypes in __EO<adaptor-name>Prototypes__, then in __EOPrototypes__, and finally in the adaptor for your model. This search path allows you to override the prototypes provided by each adaptor. Furthermore, if you don't want to use the adaptor-defined prototypes at all, you can hide them. Create an entity named __EOPrototypesToHide__. For each prototype you want to hide, create an attribute with that name; you don't need to specify other attribute properties.

### API for Prototype Attributes

The following tables describe the API that has been added to support prototype attributes.

|  EOAdaptor |  EOAdaptor |
|  prototypeAttributes |  Returns an array of prototype attributes specific to the adaptor. |

```
```

|  EOModel |  EOModel |
|  prototypeAttributeNamed: |  Returns the prototype attribute identified by the specified name or nil or null if there isn't one by that name. Looks first for the prototype in the prototypes entity named EO<adaptorName>Prototypes, then in prototypes entity named EOPrototypes, and then in the list of prototypes provided by the adaptor itself (using EOAdaptor's prototypeAttributes method). |
|  availablePrototypeAttributeNames |  Returns an array of the names of all the prototypes available to the model. |

```
```

|  EOAttribute |  EOAttribute |
|  overridesPrototypeDefinitionForKey: |  Returns NO or false if the requested key gets its value from the prototype attribute, or YES or true if the attribute overrides the prototype information for that key ("columnName", "valueClass", or so on). If the attribute doesn't have a prototype, this method returns NO or false. |
|  setPrototype: |  Sets the prototype attribute from which the receiver derives its settings. Invoking this method overrides any existing settings in the receiver. |
|  prototypeName |  Returns the name of the attribute's prototype, or nil or null if the attribute has none. |
|  prototype |  Returns the attribute's prototype, or nil or null if the attribute has none. |

```
```


## Query Builder

You can now use EOModeler to create a query, name it, and store it in the model file. To perform a query in Enterprise Objects Framework, you create an EOFetchSpecification object, which has associated with it an entity, a qualifier, a sort ordering for the fetched objects, and several other options. In previous releases, creating a fetch specification was usually done programmatically and could be quite complex and error prone. EOModeler now has a user interface that allows you to create the fetch specification, associate it with an entity, build the qualifier graphically, and specify the sort ordering and any other options, and test the complete fetch specification by dragging it into the Data Browser.
To create a query, select an entity and then click the New Fetch Specification button (second from the right in the tool bar).

### API for Query Builder

This section describes API that has been added to support storing an EOFetchSpecification in the EOModel.

- A new class, EOQualifierVariable, defines objects that serve as placeholders in the qualifier. When you create a qualifier programmatically, you typically do something like this:

In Objective-C

```
aQual = [EOQualifier
    qualifierWithQualifierFormat:"dateReleased = %@", aDate];
```


In Java

```
aQual = EOQualifier.qualifierWithQualifierFormat(
    "dateReleased = %@", aDate);
```


where __aDate__ is a variable that contains the actual date you want to query upon. When you store the qualifier in an EOModel, there is no way to know the actual value to query upon or the variable that will contain that value. The EOQualifierVariable object acts as a placeholder for the actual variable that will represent the right side of the expression. You specify an EOQualifierVariable by using a $, as in the following:

```
dateReleased = $aDate
```


For more information, see the section "[Binding to Complex Qualifiers](Binding%20to%20Complex%20Qualifiers.md#apple-ha3deni)."

- Methods have been added to EOEntity to retrieve the fetch specification by name. When you create an EOFetchSpecification programmatically, you pass it the entity with which it should be associated. When you create an EOFetchSpecification in EOModeler, you select the entity that it should be associated with and you assign a name to the fetch specification. The EOEntity now keeps a list of all fetch specifications associated with it and can retrieve them by name. Note that EOFetchSpecifications don't know their names; rather the owning entity keeps a fetch specification-to-name mapping.

The following tables describe the new API in more detail.

|  EOQualifierVariable (New Class) |  EOQualifierVariable (New Class) |
|  variableWithKey: class method (Objective-C)  EOQualifierVariable(String) constructor (Java) |  Creates and returns a new EOQualifierVariable object with the specified name. For example, if your qualifier is "dateReleased = $aDate", then this method would be invoked with the key "aDate". |
|  initWithKey: (Objective-C only) |  Initializes a newly created EOQualifierVariable object for the specified name. |
|  key |  Returns the name with which the receiver is associated. |

```
```

|  EOModelGroup |  EOModelGroup |
|  fetchSpecificationNamed:entityNamed: (Objective-C)  fetchSpecificationNamed (Java) |  Returns the fetch specification identified by the provided name from the specified entity. |

```
```

|  EOEntity |  EOEntity |
|  fetchSpecificationNames |  Returns an alphabetically sorted array of names of the entity's fetch specifications. |
|  fetchSpecificationNamed: |  Returns the fetch specification named with the provided name. |
|  addFetchSpecification:withName: (Objective-C)  addFetchSpecification (Java) |  Adds the fetch specification and associates the provided name with it. |
|  removeFetchSpecificationNamed: |  Removes the fetch specification referred to by the provided name. |

```
```

|  EODatabaseDataSource |  EODatabaseDataSource |
|  initWithEditingContext: entityName: fetchSpecificationName: (Objective-C)  EODatabaseDataSource(EOEditingContext, String, String) (Java) |  Initializes a new data source with an editing context, an entity name, and a named fetch specification. If the provided fetch specification name is nil or null, this method creates a new fetch specification that fetches all of the entities objects and assigns this fetch specification to the new data source. |
|  setFetchSpecificationByName: |  Sets the database data source's fetch specification to the one identified by the provided name. This method is an alternative to setFetchSpecification: |
|  fetchSpecificationName |  Returns the name of the data source's fetch specification or nil or null if the data source's fetch specification doesn't have a name. |

```
```


## EOModeler Bundle Loading

EOModeler's Preferences panel now allows you to specify file system locations in which to look for EOModeler bundles. EOModeler loads all the __.EOMbundle__ files it finds in those locations. In the past, you specified the bundles you wanted to load with a user default. This same default still exists (and is used by the Preferences panel), but its value has a slightly different meaning. Whereas you used to specify the full path to each bundle to load, you now specify paths in which to search for bundles.

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Binding%20to%20Complex%20Qualifiers.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
