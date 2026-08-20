---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/CreatingModels1.html
archived_at: '2026-07-15T08:03:37.948647Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Creating%20a%20New%20Model.md) [!Previous Section](Creating%20a%20New%20Model.md)

# About Models

Although a model can be generated dynamically at run time, you typically create models using EOModeler and then add them to your project as model files.
Models are designed to be loaded incrementally to maximize performance. A model consists of one global file, with a separate file for each entity. Entity descriptions are loaded in to an application as needed. Models have an __.eomodeld__ file wrapper (which is actually a directory), and the individual entity files within the model are in ASCII format. If you want to view the ASCII files in a model, open the __.eomodeld__ directory. This displays the individual entity, stored procedure, and fetch specification files in the model. The entity files have a __.plist__ extension, indicating that the files' contents are in ASCII property list format. The stored procedure files have the extension __.storedProcedure__. The fetch specification files have the extension __.fspec__.You can view the individual files in a text editor.
The global file has the name __index.eomodeld__. It contains the connection dictionary, the adaptor name, and a list of all of the entities in the model.
Models describe the database-to-enterprise object mapping by using the modeling classes EOModel, EOEntity, EOAttribute, and EORelationship (EORelationships include additional information in the form of EOJoin objects).
The following table describes the database-to-object mapping provided in a model:

|  Database Element |  Model Object |  Object Mapping |
|  Data Dictionary |  EOModel |  - |
|  Table |  EOEntity |  Enterprise object class |
|  Row |  - |  Enterprise object instance |
|  Column |  EOAttribute |  Enterprise object instance variable (class property) |
|  Referential Constraint |  EORelationship |  Reference to another object |

```
```


While the modeling classes correspond to elements in a relational database, a model represents a level of abstraction above the database. Consequently, the mapping between modeling classes and database components doesn't have to be one-to-one. So, for example, while an EOEntity object described in a model corresponds to a database table, in reality it can contain references to multiple tables. In that sense, a model is actually more analogous to a database view. Similarly, an EOAttribute can either correspond directly to a column in the root entity, or it can be derived or flattened. A derived attribute typically has no corresponding database column, while a flattened attribute is added to one entity from another entity. For more information, see the chapter[Adding Derived Properties](Adding%20Derived%20Properties.md).

You can store your model files anywhere, but to use a model in an application you must copy it into your application's project directory.

[!Table of Contents](Creating%20a%20New%20Model.md) [!Next Section](Starting%20EOModeler.md)
