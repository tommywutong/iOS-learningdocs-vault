---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies5.html
archived_at: '2026-07-18T01:23:04.191022Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies4.md)

## Choosing What to Include in Your Model

In this next wizard page, you can specify the degree to which the wizard configures your model.

!

The basic model the wizard creates contains _entities_, _attributes_, and _relationships._ An _entity_ is the part of the database-to-object mapping that associates a database table with an enterprise object class. For example, the Movie entity maps rows from the MOVIE table to Movie objects. Similarly, an _attribute_ associates a database column with an instance variable. For example, the __title__ attribute in the Movie entity maps the TITLE column of the MOVIE table to the __title__ instance variable of Movie objects.
A _relationship_ is a link between two entities that's based on attributes of the entities. For example, the Movie entity has a relationship to the MovieRole entity based on the entities' __movieId__ attributes (although the attributes in this example have the same name in both entities, they don't have to). This relationship makes it possible to find all of a Movie's MovieRoles.
How complete the basic model is depends on how completely the schema information is inside your database server. For example, the wizard includes relationships in your model only if the server's schema information specifies foreign key definitions.
Using the options in this page, you can supplement the basic model with additional information. (Note that the wizard doesn't modify the underlying database.)

- Check the "Assign primary keys to all entities" box.

!

Enterprise Objects Framework uses primary keys to uniquely identify enterprise objects and to map them to the appropriate database row. Therefore, you must assign a primary key to each entity you use in your application. The wizard automatically assigns primary keys to the model if it finds primary key information in the database's schema information.

Checking this box causes the wizard to prompt you to choose primary keys that aren't defined in the database's schema information. If your database doesn't define them, the wizard later prompts you to choose primary keys.

- Check the "Ask about relationships" box.

!

If there are foreign key definitions in the database's schema information, the wizard includes the corresponding relationships in the basic model. However, a definition in the schema information doesn't provide enough information for the wizard to set all of a relationship's options. Checking this box causes the wizard to prompt you to provide the additional information it needs to complete the relationship configurations.

- Uncheck the "Ask about stored procedures" box.

!

Checking this box causes the wizard to read stored procedures from the database's schema information, display them, and allow you to choose which to include in your model. Because the Movies application doesn't require the use of any stored procedures, don't check this box.

- Uncheck the "Use custom enterprise objects" box.

!

An entity maps a table to enterprise objects by storing the name of a database table (MOVIE, for example) and the name of the corresponding enterprise object class (a Java class, Movie, for example). When deciding what class to map a table to, you have two choices: EOGenericRecord or a custom class. EOGenericRecord is a class whose instances store key-value pairs that correspond to an entity's properties and the data associated with each property.

If you don't check the "Use custom enterprise objects" box, the wizard maps all your database tables to EOGenericRecord. If you do check this box, the wizard maps all your database tables to custom classes. The wizard assumes that each entity is to be represented by a custom class with the same name. For example, a table named MOVIE has an entity named Movie, whose corresponding custom class is also named Movie.

_Use a custom enterprise object class only when you need to add business logic; otherwise use EOGenericRecord_. The Movies application uses EOGenericRecord for the Movie entity and custom classes for the Talent and MovieRole entities. Later on, you'll use EOModeler to specify the custom classes.

- Click Next.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies6.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
