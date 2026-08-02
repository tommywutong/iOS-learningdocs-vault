---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Java/Packages.html
archived_at: '2026-07-15T07:49:22.623976Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](TOC.md)
[!Previous Section](AccessingObjectiveC.md)

## The Java Packages

The WebObjects Java Extensions includes a Java package corresponding to each of the three key WebObjects Frameworks: Foundation, Enterprise Objects, and WebObjects. These packages are __next.util__, __next.eo__, and __next.wo__, respectively.

### next.util

The __next.util__ package contains Java classes that correspond to some of the more useful classes and protocols within NeXT's Foundation Framework. The Java classes in __next.util__ and their corresponding Foundation classes or protocols are listed here:

```
---------------------------------------------
                       Foundation Class
Java Class             or Protocol
---------------------------------------------
Bundle                 NSBundle
CalendarDate           NSCalendarDate
Coder                  NSCoder
Coding                 NSCoding protocol
DecimalNumber          NSDecimalNumber
ImmutableBytes         NSData
ImmutableHashtable     NSDictionary
ImmutableVector        NSArray
keyValue
KeyValueCoding         See NSObjectAdditions
                       in EOF's EOControl
                       Framework.
MutableHashtable       NSMutableDictionary
MutableVector          NSMutableArray
NextException          NSException
NextObject             NSObject
ProcessInfo            NSProcessInfo
---------------------------------------------
```

Note that a given Java class doesn't necessarily implement all of the methods in the corresponding Foundation class. Also, the names of some of the methods in the Java class may not correspond exactly to the names of the equivalent methods in the corresponding Foundation class.

Reference documentation for the Java versions of these classes can be found in [Reference/util/util.html](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/WOFClasses/Java/util/util.html). For the corresponding Foundation Framework documentation, see _NEXT_ROOT___/NextLibrary/Frameworks/Foundation.framework/Resources/English.lproj/Documentation/Reference/found.hlp__.

#### next.util.keyValue

The KeyValueCoding interface implements key-value coding for wrapped Objective-C objects. For "pure" Java objects (those that don't inherit from __next.util.NextObject__), you can obtain behavior similar to that provided by the __next.util.KeyValueCoding__ interface through the use of the __next.util.keyValue__ class.

Note that while the behavior is similar, it isn't identical. With a wrapped Objective-C object you'd use:

```
anObject.getValue("someField")
```

Whereas with __next.util.keyValue__ you'd use:

```
keyValue.getValue(anObject, "someField")
```

### next.eo

The Java package __next.eo__ contains a number of classes corresponding to some of the more useful classes within NeXT's Enterprise Objects Framework (specifically, within the EOControl and EOAccess frameworks). Those classes, and their corresponding EOF classes, are listed in the following table:

```
----------------------------------------------------------------------
Java Class              EOControl Class           EOAccess Class
----------------------------------------------------------------------
AndQualifier            EOAndQualifier
CustomObject            NSObjectAdditions
DataSource              EODataSource
DatabaseDataSource                                EODatabaseDataSource
DetailDataSource        EODetailDataSource
EditingContext          EOEditingContext
FetchSpecification      EOFetchSpecification
GenericRecord                                     EOGenericRecord
ModelGroup                                        EOModelGroup
NotQualifier            EONotQualifier
ObjectStore             EOObjectStore
ObjectStoreCoordinator  EOObjectStoreCoordinator
OrQualifier             EOOrQualifier
Qualifier               EOQualifier
SortOrdering            EOSortOrdering and
                        NSArrayAdditions
----------------------------------------------------------------------
```

Note that a given Java class doesn't necessarily implement all of the methods in the corresponding Enterprise Objects Framework class. Also, the names of some of the methods in the Java class may not correspond exactly to the names of the equivalent methods in the corresponding EOF class.

Reference documentation for the Java versions of these classes can be found in [Reference/eo/eo.html](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/WOFClasses/Java/eo/eo.html). For the corresponding Enterprise Objects Framework documentation, see _NEXT_ROOT___/NextLibrary/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/EOControl.hlp__ or _NEXT_ROOT___/NextLibrary/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/EOAccess.hlp__.

### next.wo

The __next.wo__ package contains a set of Java classes that correspond to some of the more useful classes within NeXT's WebObjects Framework. Those Java classes, and the WebObjects classes to which they correspond, are listed here:

```
--------------------------------
Java Class      WebObjects Class
--------------------------------
Component       WOComponent
Context         WOContext
DisplayGroup    WODisplayGroup
DynamicElement  WODynamicElement
Element         WOElement
Request         WORequest
Response        WOResponse
SessionStore    WOSessionStore
WebApplication  WOApplication
WebSession      WOSession
--------------------------------
```

Note that a given Java class doesn't necessarily implement all of the methods in the corresponding WebObjects class. Also, the names of some of the methods in the Java class may not correspond exactly to the names of the equivalent methods in the corresponding WebObjects class.

For information about this package, refer to the corresponding WebObjects documentation. WebObjects documentation can be accessed through the WebObjects "Home Page," which is located in _NEXT_ROOT___/NextLibrary/Documentation/NextDev/WebObjects/WOHomePage.html__.

[!Table of Contents](TOC.md)
[!Next Section](WrappingObjectiveC.md)
