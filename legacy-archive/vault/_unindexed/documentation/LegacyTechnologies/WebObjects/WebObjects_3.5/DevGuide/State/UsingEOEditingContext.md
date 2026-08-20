---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/UsingEOEditingContext.html
archived_at: '2026-07-15T07:52:23.830913Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](StateForCustomObjects.md)

## Archiving Custom Objects in a Database Application

If your application accesses a database, it uses the Enterprise Objects Framework and should use the EOEditingContext class (EditingContext in Java) to archive objects. An editing context manages a graph of enterprise objects that represent records fetched from a database. You send messages to the editing context to fetch objects from the database, insert or delete objects, and save the data from the changed objects back to the database. (See the _Enterprise Objects Framework Developer's Guide_ for more information.)
In WebObjects, applications that use the Enterprise Objects Framework must enlist the help of the EOEditingContext class to archive enterprise objects. The primary reason is so that EOEditingContext can keep track, from one database transaction to the next, of the objects it is designed to manage. But using an EOEditingContext for archiving also benefits your application in these other ways:

- During archiving, an EOEditingContext stores only as much information about its enterprise objects as is needed to reconstitute the object graph at a later time. For example, unmodified objects are stored as simple references that will allow the EOEditingContext to recreate the object from the database at a later time. Thus, your application can store state very efficiently by letting an EOEditingContext archive your enterprise objects.
- During unarchiving, an EOEditingContext can recreate individual objects in the graph only as they are needed by the application. This approach can significantly improve an application's perceived performance.

An enterprise object (like any other object that uses the OpenStep archiving scheme) makes itself available for archiving by declaring that it conforms to the NSCoding protocol and by implementing the protocol's two methods, encodeWithCoder: and initWithCoder:. It implements these methods like this:

```
    // WebScript example
    - encodeWithCoder:(NSCoder *)aCoder {
        [EOEditingContext encodeObject:self withCoder:aCoder];
    }

    - initWithCoder:(NSCoder *)aDecoder {
        [EOEditingContext initObject:self withCoder:aDecoder];
        return self;
    }
```


Even though the Java packages provide a different archiving mechanism, your Java classes should use the Foundation archiving mechanism. In Java, the NSCoding protocol is called the Coding interface, and it declares only one method, __encodeWithCoder__. If your class conforms to the Coding interface, it should also implement a constructor that takes a Coder object as an argument. (This is the equivalent of the __initWithCoder:__ method.)

```
    // Java example
    public void encodeWithCoder(Coder aCoder) {
        EditingContext.encodeObjectWithCoder(this, aCoder);
    }

    public MyClass(Coder aDecoder) {
        EditingContext.initObjectWithCoder(this, aDecoder);
    }
```


The enterprise object simply passes on responsibility for archiving and unarchiving itself to the EOEditingContext class, by invoking the encodeObject:withCoder: and initObject:withCoder: class methods and passing a reference to itself (self) as one of the arguments. The editing context takes care of the rest. (See the EOEditingContext class specification in the _Enterprise Objects Class Reference_ for more information.)

[!Table of Contents](StateTOC.md) [!Next Section](UsingNSCoding.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
