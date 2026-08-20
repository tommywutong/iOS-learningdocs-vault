---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ManagingState11.html
archived_at: '2026-07-18T01:20:13.635493Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Managing%20State.md) [!Previous Section](Storing%20State%20for%20Custom%20Objects.md)

## Archiving Custom Objects in a Database Application

If your application accesses a database, it uses the Enterprise Objects framework and should use the EOEditingContext class to archive objects. An editing context manages a graph of enterprise objects that represent records fetched from a database. You send messages to the editing context to fetch objects from the database, insert or delete objects, and save the data from the changed objects back to the database. (See the _Enterprise Objects Framework Developer's Guide_ for more information.)
In WebObjects, applications that use the Enterprise Objects Framework must enlist the help of the EOEditingContext class to archive enterprise objects. The primary reason is so that EOEditingContext can keep track, from one database transaction to the next, of the objects it is designed to manage. But using an EOEditingContext for archiving also benefits your application in these other ways:

- During archiving, an EOEditingContext stores only as much information about its enterprise objects as is needed to reconstitute the object graph at a later time. For example, unmodified objects are stored as simple references that will allow the EOEditingContext to recreate the object from the database at a later time. Thus, your application can store state very efficiently by letting an EOEditingContext archive your enterprise objects.
- During unarchiving, an EOEditingContext can recreate individual objects in the graph only as they are needed by the application. This approach can significantly improve an application's perceived performance.

An enterprise object (like any other object that uses the Foundation archiving scheme) makes itself available for archiving by declaring that it conforms to the NSCoding protocol and by implementing the protocol's two methods, __encodeWithCoder__: and __initWithCoder__:. It implements these methods like this:

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


The Java packages provide a different archiving mechanism; your Java classes should implement the __java.io.Serializable__ interface. This interface consists of two methods: __writeObject__, which roughly corresponds to __encodeWithCoder:__; and __readObject__, which roughly corresponds to __initWithCoder:__.

```
// Java example
private void writeObject(java.io.ObjectOutputStream out)
throws IOException {
    EOEditingContext.writeObjectToStream(this, out);
}

private void readObject(java.io.ObjectInputStream in)
throws IOException, ClassNotFoundException{
    EOEditingContext.initObjectFromStream(this, in);
}
```


The enterprise object simply passes on responsibility for archiving and unarchiving itself to the EOEditingContext class, by invoking the __encodeObject__:__withCoder__: and __initObject__:__withCoder__: methods in WebScript or Objective-C (__writeObject__ and __readObject__ in Java) and passing a reference to itself (__self__ or __this__) as one of the arguments. The editing context takes care of the rest. (See the EOEditingContext class specification in the _Enterprise Objects Framework Reference_ for more information.)

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState12.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
