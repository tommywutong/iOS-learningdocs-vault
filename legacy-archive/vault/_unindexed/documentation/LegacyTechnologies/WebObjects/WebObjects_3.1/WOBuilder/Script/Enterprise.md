---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/Enterprise.html
archived_at: '2026-07-15T07:50:58.041711Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](CreateWODisplayGroup.md)

 WODisplayGroup, EOEditingContext, and Enterprise Objects

|  |  |
| --- | --- |
|  | ---  WODisplayGroup, EOEditingContext,  and Enterprise Objects  WebObjects applications that access a database use two things that most other WebObjects applications don't, the Enterprise Objects Framework and a WODisplayGroup instance.  The Enterprise Objects Framework represents items in your database as objects (enterprise objects). To begin creating a database application, you use the EOModeler application that comes with the Enterprise Objects Framework to create an entity-relationship model. (The Database Wizard can help you create a model.) You create an _entity_ for each table in the database. For each entity, you create attributes that map to the columns in the table. Each entity in turn maps to an enterprise object, which means you can access that entity as an object. The columns in the database's table become the enterprise object's instance variables.  When you add an entity to a WebObjects application (either by selecting it in the wizard or by dragging it from EOModeler), it creates a WODisplayGroup. The WODisplayGroup manages objects associated with a single entity. For example, if you choose the Movie entity, the resulting WODisplayGroup operates on Movie objects. Note, however, that you can also access other kinds of objects through a Movie object's relationships. For example, if a relationship between a MOVIE table and a STUDIO table can be expressed with a join, you could access Studio objects associated with a particular Movie object.  For more information on creating models, see the chapter "Using EOModeler" in _Enterprise Objects Framework Developer's Guide_.  The WODisplayGroup has methods that can perform almost any operation on a database. A WODisplayGroup can fetch, insert, update, delete, and find records in the database as well as manage batches of search results. Thus, WODisplayGroup allows you to create a database application without writing much or any code. All you have to do is bind your dynamic elements to methods in the WODisplayGroup. For a list of commonly used methods and what they do, see "[Common WODisplay Group Methods](WODisplayGroupMethods.md#apple-kjcumnzqge4ts)."  WODisplayGroup uses an EOEditingContext to manage the graph of enterprise objects in your application. The EOEditingContext is stored in the session (WOSes sion instance) as the variable __defaultEditingContext__. You generally can't see the EOEditingContext in WebObjects Builder, but some of the scripts created by the Database Wizard reference this object. The EOEditingContext is responsible for ensuring that all parts of your application stay in sync. You need to access the EOEditingContext if your application can update database records---you use the EOEditingContext to save the changes. To learn more about how to create a WebObjects database application, work through the Movies tutorial in _[Getting Started](../../GettingStarted/GettingStartedTOC.md)_. The Movies tutorial teaches you how to use Enterprise Objects with WebObjects. For more detailed information on Enterprise Objects, read the _Enterprise Objects Framework Developer's Guide_.     --- |

[!Table of Contents](Script.book.md)
[!Next Section](SetUpWODisplayGroup.md)
