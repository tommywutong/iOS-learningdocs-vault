---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/CreatingModels4.html
archived_at: '2026-07-15T08:03:45.095121Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Creating%20a%20New%20Model.md) [!Previous Section](Creating%20a%20New%20Model-2.md)

# What a New Model Includes

When you create a new model, the information it includes depends on how completely you've specified the underlying database. EOModeler can read all of the following from a database and include it in a default model:

- Table and column names
- Column data types, including the width constraint of string data types
- Primary keys
- User constraints, such as null constraints and uniqueness
- Foreign key definitions (which are expressed in a model as relationships)
- Stored procedures

A model contains not only the information it reads from the database, but values it derives from that information, including:

- Entity and attribute names
- A mapping between the data type of a database column and a corresponding value class, such as String, Number, or NSGregorianDate (NSString, NSNumber, or NSCalendarDate in Objective-C). See the class specification for each adaptor for a listing of the adaptor's default database type to value class mapping.

EOModeler derives entity names by taking a database table name and making all of it lowercase except for the first letter. It then removes underbar (_) characters and capitalizes any characters following underbars. For example:

|  Database Table |  Entity Name |
|  EMPLOYEE |  Employee |
|  EMPLOYEE_PHOTO |  EmployeePhoto |
|  TEST_OF_SEVERAL_WORDS |  TestOfSeveralWords |

```
```


Attribute names are based on corresponding database columns. They're derived in the same way as entities, except that EOModeler doesn't capitalize the first character. For example:

|  Database Column |  Attribute Name |
|  NAME |  name |
|  FIRST_NAME |  firstName |
|  MOVIE_ID |  movieId |

```
```

[!Table of Contents](Creating%20a%20New%20Model.md) [!Next Section](Updating%20Your%20Model.md)
