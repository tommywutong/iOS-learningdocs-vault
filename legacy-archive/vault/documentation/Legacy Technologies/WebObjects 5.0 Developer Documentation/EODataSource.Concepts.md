---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/Concepts/EODataSourceConcepts.html
archived_at: '2026-07-15T08:13:43.609449Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md) 

# EODataSource.Concepts

## Creating a Subclass

The job of an EODataSource is to provide objects that share a set of properties so that they can be managed uniformly by its client, such as an EODisplayGroup (defined in EOInterface) or a WODisplayGroup (defined in WebObjects). Typically, these objects are all of the same class or share a superclass that defines the common properties managed by the client. All that's needed, however, is that every object have the properties expected by the client. For example, if an EODataSource provides Member and Guest objects, they can be implemented as subclasses of a more general Customer class, or they can be independent classes defining the same properties (__lastName__, __firstName__, and __address__, for example). You typically specify the kind of objects an EODataSource provides when you initialize it. Subclasses usually define a constructor whose arguments describe the objects. The EODatabaseDataSource constructor, for example, uses an EOEntity to describe the set of objects. Another subclass might use an EOClassDescription, a class or superclass for the objects, or even a collection of existing instances.

A subclass can provide two other pieces of information about its objects, using methods declared by EODataSource. First, if your subclass keeps its objects in an EOEditingContext, it should override the editingContext method to return that EOEditingContext. It doesn't have to use an EOEditingContext, though, in which case it can just use the default implementation of __editingContext__, which returns null. Keep in mind, however, the amount of work EOEditingContexts do for you, especially when you use EODisplayGroups. For example, EODisplayGroups depend on change notifications from EOEditingContexts to update changes in the objects displayed. If your subclass or its clients depend on change notification, you should use an EOEditingContext for object storage and change notification. If you don't use one, you'll have to implement that functionality yourself. For more information, see these class specifications:

- EOObjectStore
- EOEditingContext
- EODisplayGroup (EOInterface)
- EODelayedObserverQueue
- EODelayedObserver

The other piece of information-also optional-is an EOClassDescription for the objects. EODataSource uses an EOClassDescription by default when creating new objects. Your subclass should override classDescriptionForObjects to return the class description if it uses one and if it's providing objects of a single superclass. Your subclass can either record an EOClassDescription itself, or get it from some other object, such as an EOEntity or from the objects it provides (through the EOEnterpriseObject method classDescription, which is implemented by EOCustomObject and EOGenericRecord). If your EODataSource subclass doesn't use an EOClassDescription at all it, can use the default implementation of __classDescriptionForObjects__, which returns null.

### Manipulating Objects

A concrete subclass of EODataSource must at least provide objects by implementing fetchObjects. If it supports insertion of new objects, it should implement insertObject, and if it supports deletion it should also implement deleteObject. An EODataSource that implements its own store must define these methods from scratch. An EODataSource that uses another object as a store can forward these messages to that store. For example, an EODatabaseDataSource turns these three requests into objectsWithFetchSpecification, insertObject, and deleteObject messages to its EOEditingContext.

### Implementing Master-Detail Data Sources

An EODataSource subclass can also implement a pair of methods that allow it to be used in master-detail configurations. The first method, dataSourceQualifiedByKey, should create and return a new data source, set up to provide objects of the destination class for a relationship in a master-detail setup. In a master-detail setup, changes to the detail apply to the objects in the master; for example, adding an object to the detail also adds it to the relationship of the master object. The standard EODetailDataSource class works well for this purpose, so you can simply implement dataSourceQualifiedByKey to create and return one of these. Once you have a detail EODataSource, you can set the master object by sending the detail a qualifyWithRelationshipKey message. The detail then uses the master object in evaluating the relationship and applies inserts and deletes to that master object.

Another kind of paired EODataSource setup, called master-peer, is exemplified by the EODatabaseDataSource class. In a master-peer setup, the two EODataSources are independent, so that changes to one don't affect the other. Inserting into the "peer," for example, does not update the relationship property of the master object. See that class description for more information.

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
