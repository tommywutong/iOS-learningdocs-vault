---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/More/EODataSource_m.html
archived_at: '2026-07-18T01:28:37.664623Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODataSource-3.md)
[!](EODelayedObserver-3.md)

---

# EODataSource

---

### Creating a Subclass

The job of an EODataSource is to provide objects that share a set of properties so that they can be managed uniformly by its client, such as an EODisplayGroup (defined in EOInterface) or a WODisplayGroup (defined in WebObjects). Typically, these objects are all of the same class or share a superclass that defines the common properties managed by the client. All that's needed, however, is that every object have the properties expected by the client. For example, if an EODataSource provides Member and Guest objects, they can be implemented as subclasses of a more general Customer class, or they can be independent classes defining the same properties (__lastName__ , __firstName__ , and __address__ , for example). You typically specify the kind of objects an EODataSource provides when you initialize it. Subclasses usually define a special __init...__ method whose arguments describe the objects. EODatabaseDataSource, for example, defines __initWithEditingContext:entityName:__ , which uses an EOEntity to describe the set of objects. Another subclass might use an EOClassDescription, a class or superclass for the objects, or even a collection of existing instances.

A subclass can provide two other pieces of information about its objects, using methods declared by EODataSource. First, if your subclass keeps its objects in an EOEditingContext, it should override the __[editingContext](EODataSource-3.md)__ method to return that EOEditingContext. It doesn't have to use an EOEditingContext, though, in which case it can just use the default implementation of __[editingContext](EODataSource-3.md)__ , which returns __nil__ . Keep in mind, however, the amount of work EOEditingContexts do for you, especially when you use EODisplayGroups. For example, EODisplayGroups depend on change notifications from EOEditingContexts to update changes in the objects displayed. If your subclass or its clients depend on change notification, you should use an EOEditingContext for object storage and change notification. If you don't use one, you'll have to implement that functionality yourself. For more information, see these class specifications:

- [EOObjectStore](EOObjectStore-2.md)
- [EOEditingContext](EOEditingContext-3.md)
- [EODisplayGroup](EODisplayGroup-2.md) (EOInterface)
- [EODelayedObserverQueue](EODelayedObserverQueue-3.md)
- [EODelayedObserver](EODelayedObserver-3.md)

The other piece of information-also optional-is an EOClassDescription for the objects. Interface Builder uses an EOClassDescription to get the keys it displays in its Connections Inspector, and EODataSource uses it by default when creating new objects. Your subclass should override [__classDescriptionForObjects__](EODataSource-3.md)to return the class description if it uses one and if it's providing objects of a single superclass. Your subclass can either record an EOClassDescription itself, or get it from some other object, such as an EOEntity or from the objects it provides (through the EOEnterpriseObject method [__classDescription__](EOEnterpriseObject-3.md), which is implemented in a category of NSObject and also by and EOGenericRecord). If your EODataSource subclass doesn't use an EOClassDescription at all it, can use the default implementation of [__classDescriptionForObjects__](EODataSource-3.md), which returns __nil__ .

---

#### Manipulating Objects

A concrete subclass of EODataSource must at least provide objects by implementing __[fetchObjects](EODataSource-3.md)__ . If it supports insertion of new objects, it should implement __[insertObject:](EODataSource-3.md)__ , and if it supports deletion it should also implement [__deleteObject:__](EODataSource-3.md). An EODataSource that implements its own store must define these methods from scratch. An EODataSource that uses another object as a store can forward these messages to that store. For example, an EODatabaseDataSource turns these three requests into __objectsWithFetchSpecification:__ , [__insertObject:__](EOEditingContext-3.md), and [__deleteObject:__](EOEditingContext-3.md)messages to its EOEditingContext.

---

#### Implementing Master-Detail Data Sources

An EODataSource subclass can also implement a pair of methods that allow it to be used in master-detail configurations. The first method, [__dataSourceQualifiedByKey:__](EODataSource-3.md), should create and return a new data source, set up to provide objects of the destination class for a relationship in a master-detail setup. In a master-detail setup, changes to the detail apply to the objects in the master; for example, adding an object to the detail also adds it to the relationship of the master object. The standard EODetailDataSource class works well for this purpose, so you can simply implement [__dataSourceQualifiedByKey:__](EODataSource-3.md)to create and return one of these. Once you have a detail EODataSource, you can set the master object by sending the detail a [__qualifyWithRelationshipKey:ofObject:__](EODataSource-3.md)message. The detail then uses the master object in evaluating the relationship and applies inserts and deletes to that master object.

Another kind of paired EODataSource setup, called master-peer, is exemplified by the EODatabaseDataSource class. In a master-peer setup, the two EODataSources are independent, so that changes to one don't affect the other. Inserting into the "peer," for example, does not update the relationship property of the master object. See that class description for more information.

---

[!](EODataSource-3.md)
[!](EODelayedObserver-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
