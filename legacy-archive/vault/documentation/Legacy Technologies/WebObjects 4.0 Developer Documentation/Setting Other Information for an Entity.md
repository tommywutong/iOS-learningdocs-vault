---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/Entities6.html
archived_at: '2026-07-18T01:18:19.916630Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Changing%20an%20Entity%27s%20Characteristics.md) [!Previous Section](Creating%20a%20Subclass.md)

# Setting Other Information for an Entity

From the Entity Inspector you can navigate to other Inspectors to specify additional information for your entity.

!

Figure 36. Icons for Navigating to Other Inspectors

## Advanced Entity Inspector

The Advanced Entity Inspector lets you set more complex behavior for your entity, such as that to support inheritance.
To display the Advanced Entity Inspector, select the Advanced Entity Inspector icon at the top of the Entity Inspector.

!

Figure 37. Advanced Entity Inspector

Batch Faulting Size
The Batch Faulting Size field lets you set the number of EOFaults that should be triggered when you first access an object of this type. By default, only one object is fetched from the database when you trigger an EOFault. By providing a number _N_ in this field, you specify that _N_ other EOFaults of the same entity should be fetched from the database along with the first one. This improves performance by minimizing round trips to the database server. For more information, see the chapter "Answers to Common Design Questions" in the book _Enterprise Objects Framework Developer's Guide_.
External Query
The External Query field allows you to specify any SQL statement that will be executed as is (that is, you can't perform any substitutions) when EOF does an unqualified fetch. On Sybase this can be a stored procedure. The columns selected by this SQL statement must be in alphabetical order by internal name, and must match in number and type with the class properties specified for the entity.
Qualifier
This field is used to specify a restricting qualifier. A restricting qualifier maps an entity to a subset of rows in a table. Restricting qualifiers are commonly used when you're using single table inheritance mapping, in which the data for a class and its subclasses is all stored in a single table. When you add a restricting qualifier to an entity, it causes a fetch for that entity to only retrieve objects of the appropriate type. For example, the Rentals sample database has a MOVIE_MEDIA table that includes rows for both the VideoTape and LaserDisk entities. VideoTape has the restricting qualifier (media = `T'), and LaserDisk has the restricting qualifier (media = `D'). When you fetch objects for the entity VideoTape, only rows that have the value `T' for the attribute __media__ are fetched. For more discussion of single table and other types of inheritance mapping, see the chapter "Advanced Enterprise Object Modeling" in the book _Enterprise Objects Framework Developer's Guide_.
Parent
You use this field to specify a parent entity for the current entity. This field is used to model inheritance relationships. For example, in the Rentals database, the Customer entity is the parent of the Member and Guest entities (since Members and Guests are types of Customers). For more information, see the chapter "Advanced Enterprise Object Modeling" in the book _Enterprise Objects Framework Developer's Guide_.
Read Only
The Read Only checkbox indicates whether the data that's represented by the entity can be altered by your application.
Cache In Memory
The Cache In Memory checkbox lets you specify that the objects associated with an entity should be cached in memory for quick access. Caching an entity's objects allows Enterprise Objects Framework to evaluate queries in memory, thereby avoiding round trips to the database. This is most useful for read-only entities, where there is no danger of the cached data getting out of sync with database data. This technique should only be used with small tables, since it fetches the entire table into memory.
Abstract
The Abstract checkbox indicates whether the entity is abstract. An abstract entity is one for which no objects are ever instantiated in your application. For example, in the Rentals database, the Customer entity is abstract since Customer objects are never instantiated (though objects of its sub-entities, Member and Guest, are). Like the Parent field, this option is used to model inheritance. For more information, see the chapter "Advanced Enterprise Object Modeling" in the book _Enterprise Objects Framework Developer's Guide_.

## Stored Procedures Inspector

You use the Stored Procedures Inspector to specify stored procedures that should be executed when a particular database operation (such as insert or delete) occurs. You type the name of the stored procedure in the field associated with the database operation. Stored procedures are read from the database when you create a new model and included in its __.eomodeld__ file. You can also add stored procedures through EOModeler after the fact.
Creating stored procedures and assigning them to entities is described in detail in the chapter [Working with Stored Procedures](Working%20with%20Stored%20Procedures.md#apple-ge2tmojs).

## UserInfo Inspector

You use the UserInfo Inspector to add key-value pairs to the UserInfo NSDictionary. The UserInfo dictionary provides a mechanism for extending your model. You can use it to define custom behavior for an entity. For example, you can put information in the UserInfo dictionary to be used by delegate methods that perform operations on the entity.
[!Table of Contents](Changing%20an%20Entity%27s%20Characteristics.md) [!Next Section](Working%20with%20Stored%20Procedures.md)
