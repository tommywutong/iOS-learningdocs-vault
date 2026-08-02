---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/FAQ6.html
archived_at: '2026-07-18T01:19:48.198855Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Previous Section](How%20Do%20I%20Order%20Database%20Operations.md)

# How Are Enterprise Objects Cleaned Up?

If you use an EODisplayGroup to fetch enterprise objects into your application, you might wonder:

- Who "owns" the objects?
- How do they get cleaned up?
- How are their snapshots cleaned up?
- What happens if you have reference cycles?

In applications that fetch a lot of enterprise objects or are long-running, these are important questions. How they're answered depends on what language you're using. However, regardless of language, you don't typically have to worry about any of these issues. With Java's garbage collection, enterprise objects and their related resources are automatically cleaned up when they are no longer in use.
In Objective-C, as long as you follow the object ownership conventions defined in the Foundation framework, enterprise objects and their related resources are similarly deallocated automatically. The following sections provide more information on how this happens in Objective-C Enterprise Objects Framework applications.
For more general information on this automatic object disposal mechanism in Objective-C, see the introduction to the _Foundation Framework Reference._

## Who Owns an Enterprise Object?

In design terms, one object might own another; but in the Foundation Framework, no object really "owns" another. Rather, one or more objects may "retain" another object. If one object retains another, it has a responsibility to release it when it no longer needs the other object. In Enterprise Objects Framework applications, an enterprise object is retained by other enterprise objects that have a relationship to it. An enterprise object is also retained by an EODisplayGroup object that fetches and displays it.

## How Does an Enterprise Object Get Deallocated?

In a Enterprise Objects Framework applications, an enterprise object is retained by other enterprise objects that have a relationship to it and by any EODisplayGroup objects that fetch and display it. Typically, enterprise objects are deallocated automatically when they are no longer referenced by other objects. You don't ordinarily manage the deallocation of enterprise objects explicitly.
Accessor methods that manage relationships to one or more enterprise objects also release objects when they no longer need to reference them. For example, the following method releases an employee's old manager before assigning a new one:

```objc
- (void)setManager:(Employee *)aManager
{
    [self willChange];
    [manager autorelease];
    manager = [aManager retain];
}
```


If an enterprise object class doesn't implement accessor methods for a relationship, the Framework automatically releases and retains the destination objects. Similarly, an EODisplayGroup object releases its enterprise objects immediately before it fetches a new set of objects or immediately before it is deallocated itself. Unless you explicitly retain an enterprise object, it is automatically deallocated when its display group stops displaying it.
If you _do_ explicitly retain an enterprise object (either by sending it a retain message or by adding it to a collection), the enterprise object is not deallocated until you release it (either by sending it a __release__ message or, if it's in a collection, by releasing its collection).
Methods for getting enterprise objects without using an EODisplayGroup don't automatically retain objects. For example, the objects returned from EODataSource's __fetchObjects__ method and EOEditingContext's __objectsWithFetchSpecification:__ method are not retained by any object. Unless you retain them, they will be deallocated automatically.

## How Are an Object's Snapshots Deallocated?

Enterprise Objects Framework keeps two kinds of snapshots:

- Object snapshots that are maintained by EOEditingContexts
- Row snapshots that are maintained by EODatabaseContexts

An object snapshot is deallocated at the same time its enterprise object is deallocated. A row snapshot, however, is only invalidated when its EODatabaseContext is deallocated or when it receives an __invalidateAllObjects__ message or __invalidateObjectWithGlobalID:__ message. Multiple EOEditingContexts may use a single EODatabaseContext object and its row snapshots. As a result, it isn't practical to deallocate a row snapshot when a corresponding enterprise object is deallocated. An enterprise object in another EOEditingContext may still reference the snapshot. To deallocate row snapshots explicitly, use one of the __invalidate...__ methods.

## What Happens If You Have Retain Cycles?

A retain cycle occurs when two objects retain one another. They may retain one another directly, or indirectly through a collection or another object. Retain cycles occur quite commonly in Enterprise Objects Framework applications. For example, if an Employee object has a relationship to a Department object, the Department object probably has a relationship to its employees as well. Normally an object retains the objects to which it has a relationship, so the reciprocal relationships between Employee and Department objects form a retain cycle.
Objects in a cycle stay in memory until the cycle is broken. If the cycle is never broken, the objects stay in memory until the process exits. Too many unbroken retain cycles degrade an application's performance.
One strategy for handling retain cycles is to ensure that none are created. If you don't need reciprocal relationships, don't create them. Reciprocal relationships, however, are very useful. You are more likely to use one of the following approaches for handling retain cycles.

### invalidateObjectsWhenFreed

Retain cycles between objects can be broken automatically when their EOEditingContext is deallocated. To break retain cycles automatically, set the EOEditingContext's __invalidatesObjectsWhenFreed__ attribute to YES, which is the default. This approach works well in multi-document applications in which EOEditingContexts are deallocated when their windows close.

### invalidateAllObjects

In applications that aren't multi-document, you can break cycles by sending an __invalidateAllObjects__ message to an EOEditingContext's root EOObjectStore. You typically invalidate enterprise objects after saving changes to the database or after reverting.

### invalidateAllObjects

This method replaces all the associated enterprise objects with EOFault objects, eliminating retain cycles in the process. It has the side-effect of invalidating all the enterprise objects in a peer editing context as well.

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Next Section](Should%20I%20Make%20Foreign%20Key%20Attributes%20Class%20Properties.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
