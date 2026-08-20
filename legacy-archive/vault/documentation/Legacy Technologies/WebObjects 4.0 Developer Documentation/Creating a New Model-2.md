---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/CreatingModels3.html
archived_at: '2026-07-18T01:17:53.446922Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Creating%20a%20New%20Model.md) [!Previous Section](Starting%20EOModeler.md)

# Creating a New Model

To create a model, choose Model ! New.
EOModeler starts the New Model Wizard, which assists you to configure your new model. The following sections describe the wizard pages that guide you through the model creation process.

## Selecting an Adaptor

An _adaptor_ is a mechanism that connects your application to a particular database server. For each type of server you use, you need a separate adaptor. Enterprise Objects Framework provides adaptors for Informix, Oracle, and Sybase servers, and for any server that is ODBC compliant. It also provides a sample adaptor for a flat-file data store and an adaptor for OpenBase Lite-a database that ships with Enterprise Objects Framework as an unsupported demo.

!

Figure 2. Selecting an Adaptor

After you select an adaptor, EOModeler displays the login panel for the database that corresponds to the adaptor you selected. Fill in the login panel and click OK.

!

Figure 3. Oracle Login Panel

Different databases require different login information, so each database's login panel looks different.The examples in this chapter use the Oracle version of the Movies database included with the Enterprise Objects Framework; [Figure 3](#apple-he2do) shows the Oracle login panel. 

## Choosing What to Include in Your Model

In this next wizard page, you can specify the degree to which the wizard configures your model.

!

Figure 4. Choosing What to Include in the Model

How complete the model EOModeler creates is depends on how completely the schema information is inside your database server. For example, the wizard includes relationships in your model only if the server's schema information specifies foreign key definitions.
Using the options in this page, you can tell EOModeler that you want to supplement the model with additional information. (Note that the wizard doesn't modify the underlying database.)
Assign primary keys to all entities
Enterprise Objects Framework uses primary keys to uniquely identify enterprise objects and to map them to the appropriate database row. Therefore, you must assign a primary key to each entity you use in your application. The wizard automatically assigns primary keys to the model if it finds primary key information in the database's schema information.
Checking this box causes the wizard to prompt you to choose primary keys that aren't defined in the database's schema information. If your database doesn't define them, the wizard later prompts you to choose primary keys.
Ask about relationships
If there are foreign key definitions in the database's schema information, the wizard includes the corresponding relationships in the model. However, a definition in the schema information doesn't provide enough information for the wizard to set all of a relationship's options. Checking this box causes the wizard to prompt you to provide the additional information it needs to complete the relationship configurations.
Ask about stored procedures
Checking this box causes the wizard to read stored procedures from the database's schema information, display them, and allow you to choose which to include in your model.
Use custom enterprise objects
An entity maps a table to enterprise objects by storing the name of a database table (MOVIE, for example) and the name of the corresponding enterprise object class (a Java class, Movie, for example). When deciding what class to map a table to, you have two choices: EOGenericRecord or a custom class. EOGenericRecord is a class whose instances store key-value pairs that correspond to an entity's properties and the data associated with each property.
If you don't check the "Use custom enterprise objects" box, the wizard maps all your database tables to EOGenericRecord. If you do check this box, the wizard maps all your database tables to custom classes. The wizard assumes that each entity is to be represented by a custom class with the same name. For example, a table named MOVIE has an entity named Movie, whose corresponding custom class is also named Movie.
Use a custom enterprise object class only when you need to add business logic; otherwise use EOGenericRecord.

## Choosing the Tables to Include

After specifying what additional information to include in your model, the wizard prompts you to choose the tables to include in your model. By default, all the tables are selected.

!

Figure 5. Choosing the Tables to Include

The wizard creates entities only for the tables you select. If you later decide you want to include a table you didn't select at this stage, you can add it using the Model ! New Updated Model command, as described in [Updating Your Model](Updating%20Your%20Model.md#apple-ge2tgmbr).

## Specifying Primary Keys

If you are using a database that stores primary key information in its database server's schema information, the wizard skips this step. The wizard has already successfully read primary key information from the schema information and assigned primary keys to your model.
However, if primary key information isn't specified in your database server's schema information or if the adaptor can't read it (as with Microsoft Access), the wizard now asks you to specify a primary key for each entity.

!

Figure 6. Specifying an Entity's Primary Key

If an entity's primary key is _compound_; that is, if it's composed of more than one attribute, control-shift-click to select all of the attributes in the primary key. You use a compound primary key when any single attribute isn't sufficient to uniquely identify a row. For example, in the MovieRole entity, if requires the combination of the __movieId__ and __talentId__ attributes to uniquely identify a row.

## Specifying Referential Integrity Rules

If foreign key definitions aren't specified in your database server's schema information or the adaptor can't read that information (as with Microsoft Access), the wizard hasn't created any relationships at all, and it skips this step. You can add relationships later as described in the chapter[Working with Relationships](Working%20with%20Relationships.md#apple-ge2tqmbz).

On the other hand, if you're using a database that stores foreign key definitions in its database server's schema information, the wizard reads them and creates corresponding relationships in your model. For example, Movie has a to-many relationship to MovieRole (that is, a Movie has an array of MovieRoles), and Talent has a to-many relationship to MovieRole.
At this point, if you specified that the wizard ask about relationships (as described in[Choosing What to Include in Your Model](#apple-geytsojz)), the wizard now asks you to provide additional information about the relationships so it can further configure them.

!

Figure 7. Specifying Referential Integrity Rules for a Relationship

Owns Destination
The checkbox in this page lets you specify whether the relationship's source _owns_ its destination objects. When a source object owns its destination objects and you remove a destination object from the source object's relationship array, this also has the effect of deleting it from the database (alternatively, you can transfer it to a new owner). This is because ownership implies that the owned object can't exist without an owner.
For example, in the relationship shown in [Figure 7](#apple-gezdembv), Movie owns its MovieRole objects.This means that a destination object (MovieRole) can't exist without its source (a Movie). Consequently, when a MovieRole is removed from its Movie's array of MovieRoles, the MovieRole is deleted-deleted in memory and deleted in the database.

Delete Rule
The radio button you choose in this page specifies what to do when the relationship source is deleted: nullify, cascade, or delete. For example, in the relationship shown in [Figure 7](#apple-gezdembv), when a user tried to delete a Movie, you could:

- Delete the Movie and set all it's MovieRoles not to be associated with a Movie (nullify).
- Delete the Movie and all its MovieRoles (cascade).
- Refuse the deletion if the Movie has MovieRoles (deny).

## Choosing Stored Procedures

If you asked the wizard to include stored procedures in your model (as described in[Choosing What to Include in Your Model](#apple-geytsojz)), the wizard asks you to specify which stored procedures to include. By default, all the stored procedures are selected.

!

Figure 8. Choosing the Stored Procedures to Include

The wizard includes stored procedure information only for the stored procedures you select. If you later decide you want to include a stored procedure you didn't select at this stage, you can add it using the Property ! Add Stored Procedure command, as described in the chapter[Working with Stored Procedures](Working%20with%20Stored%20Procedures.md#apple-ge2tmojs).

## Saving the Model

When you finish the wizard, EOModeler displays the new model. If you're planning to use your model in an application for which you've already created a project, you should save the model into your project folder. You will be prompted to add it to the project; click OK.

[!Table of Contents](Creating%20a%20New%20Model.md) [!Next Section](What%20a%20New%20Model%20Includes.md)
