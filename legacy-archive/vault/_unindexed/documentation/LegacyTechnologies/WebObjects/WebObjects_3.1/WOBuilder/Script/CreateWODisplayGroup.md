---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/CreateWODisplayGroup.html
archived_at: '2026-07-15T07:50:54.482574Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](DeleteClasses.md)

Creating a WODisplayGroup

# Creating a WODisplayGroup

Choose Database Wizard from the Tools menu.

Follow the instructions provided in the wizard.

_OR:_

Drag an entity from the icon path in EOModeler to a component window, or drag the entire model file from the file system to a component window.

!

!

To write a WebObjects application that accesses a database, you need a WODisplayGroup. The [WODisplayGroup](Enterprise.md) can fetch, display, update, and search records in a database.

In most cases, you can create a database application using the Database Wizard. The wizard creates the WODisplayGroup, lays out the dynamic elements on the page, and creates bindings between the display group and the dynamic elements. After running the wizard, you have a working WebObjects application that fetches records from a database.

__Note:__ You must run the database wizard from a component that's inside an application. That is, before you run the wizard, you must have created an application and that application must have at least one component.

If you need to do something more complex than the wizard provides, you can start by using the Database Wizard and then modify the results. If you don't want to use one of the wizard's layouts, you can create the application yourself.

If you create the application yourself, create the WODisplayGroup by dragging an entity from the EOModeler application. After you do this, you'll want to set display group options, and you'll have to bind elements to the display group. See "[Setting Up a WODisplayGroup](SetUpWODisplayGroup.md#apple-kjcumobugq3dm)" and "[Common WODisplayGroup Methods](WODisplayGroupMethods.md#apple-kjcumnzqge4ts)" for help.

Whichever way you add the WODisplayGroup, you get the following items with it:

- The model that contains the WODisplayGroup's entity is copied into the application. If you need to change the model or add another entity to a component, you should use this copy of the model file.
- All of the entities that are defined in the model are added to the component as [classes](Classes.md). You can create instances of these classes and bind to them if necessary.
- An [EOEditingContext](Enterprise.md) is added to the session. You generally can't see this in the object browser, but it is accessible in the script.

[!Table of Contents](Script.book.md)
[!Next Section](Enterprise.md)
