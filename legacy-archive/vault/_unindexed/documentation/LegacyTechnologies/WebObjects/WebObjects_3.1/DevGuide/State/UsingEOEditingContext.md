---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/UsingEOEditingContext.html
archived_at: '2026-07-15T07:47:55.399438Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](StateForCustomObjects.md)

# __Using EOEditingContext to Archive Custom Objects__

In an Enterprise Objects application, an EOEditingContext manages a graph of enterprise objects which represent records fetched from a database. You send messages to the EOEditingContext to fetch objects from the database, insert or delete objects, and save the data from the changed objects back to the database. (See the _Enterprise Objects Framework Developer's Guide_ for more information.)

In WebObjects, applications that use the Enterprise Objects framework must enlist the help of the EOEditingContext to archive enterprise objects. The primary reason is so that the EOEditingContext can keep track, from one transaction to the next, of the objects it is designed to manage. But using an EOEditingContext for archiving also benefits your application in these other ways:

- During archiving, an EOEditingContext stores only as much information about its enterprise objects as is needed to reconstitute the object graph at a later time. For example, unmodified objects are stored as simple references that will allow the EOEditingContext to recreate the object from the database at a later time. Thus, your application can store state very efficiently by letting an EOEditingContext archive your enterprise objects.
- During unarchiving, an EOEditingContext can recreate individual objects in the graph only as they are needed by the application. This approach can significantly improve an application's perceived performance.

An enterprise object (like any other object that uses the OpenStep archiving scheme) makes itself available for archiving by declaring that it conforms to the NSCoding protocol and by implementing the protocol's two methods, __encodeWithCoder:__ and __initWithCoder:__. It implements these methods like this:

```objc
- (void)encodeWithCoder:(NSCoder *)aCoder {
    [EOEditingContext encodeObject:self withCoder:aCoder];
}

- (id)initWithCoder:(NSCoder *)aDecoder {
    [EOEditingContext initObject:self withCoder:aDecoder];
    return self;
}
```

The enterprise object simply passes on responsibility for archiving and unarchiving itself to the EOEditingContext class, by invoking the __encodeObject:withCoder:__ and __initObject:withCoder:__ class methods and passing a reference to itself (__self__) as one of the arguments. The EOEditingContext takes care of the rest. (See the EOEditingContext class reference for more information.)

[!Table of Contents](ManagingState.book.md)
[!Next Section](UsingNSCoding.md)
