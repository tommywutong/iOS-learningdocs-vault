---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements6.html
archived_at: '2026-07-18T01:26:17.314850Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DynamicElements5.md)

## Adding Display Groups

A _display group_ is an important type of variable that you use in WebObjects applications that access databases. A display group is an object that can fetch, insert, delete, display, update and search records in a database.
This section describes the mechanics of adding display groups to a WebObjects project. For detailed information about display groups, see the WODisplayGroup class specification in the [_WebObjects Class Reference._](WebObjectsTOC.md) To learn more about how to create a WebObjects database application, see ["Creating a WebObjects Database Application"](Creating%20a%20Simple%20WebObjects%20Application.md) in _Getting Started With WebObjects._

WebObjects applications access databases through the Enterprise Objects Framework, which represents database rows as _enterprise objects_. Enterprise object classes typically correspond to database tables, and an enterprise object instance corresponds to a single row or record in a table. For detailed information on enterprise objects, read the _Enterprise Objects Framework Tools and Techniques_.
In a database application, you use _entity-relationship models_. A modelassociates database columns with instance variables of objects. You create a model with the EOModeler application, or you can specify one when you use the Wizard to set up your application (when you add a model to your project, it is added to the Resources suitcase). A model is stored in a _model file_. For more information on creating models, see the chapter "Using EOModeler" in _Enterprise Objects Framework Developer's Guide_.
A model contains _entities_, _attributes_, and _relationships._ An _entity_ associates a database table with an enterprise object class. Display groups manage objects associated with a single entity. An _attribute_ associates a database column with an instance variable. A _relationship_ is a link between two entities that's based on attributes of the entities.
If you used the Wizard to set up your application, a display group was set up for you based on the model you specified. There are several other ways to create a display group:

- Drag a model (a folder with the extension __.eomodeld__) from the file system into the object browser in your component window, or drag an entity from the EOModeler application into the object browser.

When you do this, a panel asks you if you want to add the model to your project. If you reply Yes, the Add Display Group panel appears.

!

It allows you to specify a name for your display group and decide if you want to simply add the display group, or configure it as well. ["Configuring the Display Group"](DynamicElements7-2.md#apple-geztcoby) describes the configuration process.

- Use Add Variable/Method to define a variable of typeWODisplayGroup, or declare the display group directly in your code:

```
protected WODisplayGroup myDisplayGroup; //this is a Java example
```


When you add a display group this way, you are responsible for making sure your project contains the appropriate model file. (For example, once a model file has been added, you can create any number of display groups based on it). In addition, you need to configure the display group.

When you use the Add Variable/Method panel, you can create not only display group variables, but also enterprise objects associated with any of the entities in your project's models.

!

In the figure, if you choose the entity Movie as the variable's type, the following code gets added to your source file:

```
/** @TypeInfo Movie */
protected EOEnterpriseObject selectedMovie;
```


The variable __selectedMovie__ is declared as type EnterpriseObject. The comment /\*\* @TypeInfo Movie \*/ is a _structured comment_ that WebObjects Builder uses to identify the entity associated with the object (don't edit it). It is then able to display the attributes in the object browser as shown here:

!

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DynamicElements7-2.md)
