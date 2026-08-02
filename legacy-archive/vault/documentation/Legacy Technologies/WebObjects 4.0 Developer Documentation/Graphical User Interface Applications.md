---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/AppConfs1.html
archived_at: '2026-07-18T01:19:10.086107Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Application%20Configurations.md) [!Previous Section](Application%20Configurations.md)

# Graphical User Interface Applications

In a typical Enterprise Objects Framework application, a display group binds data fetched from a database to elements of the application's user interface. As shown in [Figure 31](#apple-gm3tooi), a display group relies on a network of objects to connect to a database and interact with it.

!

Figure 31. Typical Configuration of a Graphical User Interface Application

The network of objects is created automatically. For example, all the following procedures create a display group that is automatically associated with an EODatabaseDataSource and its underpinnings:

- Running the EOF Wizard in Project Builder (to create an Application Kit Framework application with a graphical user interface).
- Dragging an entity from a model file into a nib file in Interface Builder.
- Running the WebObjects Application Wizard in Project Builder to create a Main component with database access.
- Dragging an entity from a model file into a component in WebObjects Builder.
- Creating a "Direct-to-Web" application.

For more information on these classes and their roles in a database application, see the chapter["Enterprise Objects Framework Viewed Through Its Classes"](Enterprise%20Objects%20Framework%20Viewed%20Through%20Its%20Classes.md#apple-ge4demzv) and the class specification for each in the _Enterprise Objects Framework Reference_.

The following sections describe how the network of objects is created, starting with a nib or component.

## Loading a User Interface

When you drag an entity from a model file into Interface Builder or WebObjects Builder, you create an _entity display group_-a display group that's connected to an EODatabaseDataSource. The builder application automatically creates a display group, an EODatabaseDataSource, and an EOEditingContext. These objects are _archived_ in your nib file or WebObjects component directory. At run-time, your application _unarchives_ these objects as their interface is loaded, as shown in [Figure 32](#apple-gm3tsoa). As part of unarchiving a nib file or component, many other objects are brought into the network of behind-the-scenes objects.

!

Figure 32. Enterprise Objects Framework Objects in a Nib or Component

## Unarchiving an Editing Context

During unarchiving, an EOEditingContext uses the EOEditingContext class method __defaultParentObjectStore__ to determine its parent object store. Normally, it's the EOObjectStoreCoordinator returned from the EOObjectStoreCoordinator class method __defaultCoordinator__. If a coordinator has not yet been created, it is created at this time.

## Unarchiving a Database Data Source

Unarchiving an EODatabaseDataSource sets a more complex chain of events into motion: an EODatabaseContext and a host of associated objects are brought into the network of objects as follows:

- The EODatabaseDataSource verifies that its underlying EOObjectStoreCoordinator has an EOModelGroup that can service its entity. If you haven't assigned a model group to the coordinator, then the coordinator uses the default model group-the shared EOModelGroup instance returned by the EOModelGroup class method __defaultGroup__.

The default model group is created the first time __defaultGroup__ is invoked. Subsequent invocations return the same shared instance. It contains all the models for an application, as well as for any frameworks the application references. In the majority of applications, the default model group is sufficient. However, if your particular application requires different model grouping semantics, you can create your own EOModelGroup instance, add the appropriate models, and assign it to your application's EOObjectStoreCoordinator using the EOModelGroup method __setModelGroup__ (or the EOObjectStoreCoordinator method __setModelGroup:__ in Objective-C).

- After establishing that its entity can be serviced, the EODatabaseDataSource connects to an EODatabaseContext using the EODatabaseContext static method __registeredDatabaseContextForModel__ (__registeredDatabaseContextForModel:editingContext:__ in Objective-C). This method checks to see if the application's EOObjectStoreCoordinator already has a database context that the data source can use. If it does, it returns that database context. Otherwise it instantiates a new database context, adds it to the coordinator, and returns it.

When an EODatabaseDataSource connects to an EODatabaseContext, the database context brings in additional supporting objects. A database context can't exist without an EODatabase and an EOAdaptorContext. Similarly, an EODatabase and an EOAdaptorContext can't exist without an EOAdaptor. Thus, as shown in [Figure 33](#apple-gm4dcnq), connecting to a database context also connects an EODatabase, an EOAdaptor, and an EOAdaptorContext. Furthermore, if the adaptor bundle associated with the EODatabaseDataSource's model hasn't yet been loaded, it is loaded now.

!

Figure 33. Connecting an EODatabaseDataSource with an EODatabaseContext

## Sharing Editing Contexts and Coordinators

For Application Kit applications, Interface Builder creates only one EOEditingContext per nib. Therefore two entity display groups in the same nib share the same editing context by default.
Similarly, all editing contexts in an application share the same EOObjectStoreCoordinator by default.
If you want a different configuration, see the section ["Editing Context Configurations"](Editing%20Context%20Configurations.md#apple-gm4tcmy). It describes how objects in different nibs can share the same editing context and how to set up nested editing context. The section ["Object Store Coordinator Configurations"](Object%20Store%20Coordinator%20Configurations.md#apple-guzdana) describes how you can set up multiple EOObjectStoreCoordinators.

!

Figure 34. Display Groups in the Same Nib Share an Editing Context

!

Figure 35. Display Groups in Different Nibs Have Separate Editing Contexts

## Database Context Rendezvousing

To minimize the number of database connections an Enterprise Objects Framework application uses, an EODatabaseDataSource may share an existing EODatabaseContext with other data sources.
Using the EODatabaseContext static method __registeredDatabaseContextForModel__ (__registeredDatabaseContextForModel:editingContext:__ in Objective-C), a database data source _rendezvouses_ with compatible database contexts whenever possible. A data source is compatible with a database context when the data source's model is compatible with the models in the EOModelGroup of the database context's EODatabase. Two models are compatible when their connection dictionaries are equal as determined by NSDictionary's __isEqualToDictionary__ method (__isEqualToDictionary:__ in Objective-C).
For example, in [Figure 36](#apple-g43timy), like-colored gray objects are associated with compatible models-models that have the same connection dictionary. The light gray data source is associated with the light gray database context, and the dark gray data sources are associated with the dark gray database context. The second dark gray data source to be unarchived rendevouses with the first data source's database context.

!

Figure 36. Data Sources Rendezvous With Compatible EODatabaseContexts

Note that two database data sources can be associated with different models and still share database contexts. So long as the models are compatible, they can be serviced by the same EODatabase and EODatabaseContext.
If you want to prevent an EODatabaseDataSource from rendezvousing on an existing EODatabaseContext, see ["Object Store Coordinator Configurations"](Object%20Store%20Coordinator%20Configurations.md#apple-guzdana).

## Setting Up Channels

The remaining objects in the network-an EODatabaseChannel and an EOAdaptorChannel-are created on demand when the application initiates a database interaction. For more information, see the section ["Inside EODatabaseContext"](Non-Graphical%20User%20Interface%20Applications.md#apple-gm4dsoi).

[!Table of Contents](Application%20Configurations.md) [!Next Section](Non-Graphical%20User%20Interface%20Applications.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
