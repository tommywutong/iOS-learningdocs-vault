---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/EOsI4.html
archived_at: '2026-07-18T01:19:40.140943Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Designing%20Enterprise%20Objects.md) [!Previous Section](Implementing%20an%20Enterprise%20Object.md)

# Gotchas

This section discusses some of the more subtle issues you need to be aware of in designing enterprise objects.

## Constructor for Creating Enterprise Objects

Your Java custom enterprise object classes must provide a constructor of the following form:

```
public MyCustomEO (
    EOEditingContext  anEOEditingContext,
    EOClassDescription  anEOClassDescription,
    EOGlobalID  anEOGlobalID)
```


Enterprise Objects Framework uses this constructor to create instances of your custom classes, and it throws an exception if it doesn't find such a constructor.

## Numeric Values and NULL

An important issue to consider in using scalar types is that relational databases allow the use of a NULL value distinct from any numeric value. When a NULL value is encountered in __takeValueForKey__ (__takeValue:forKey:__ in Objective-C), your enterprise object will be passed __null__ (__nil__ in Objective-C). Since the scalar types can't accommodate __null__, the default implementations of the key-value coding methods throw an exception when asked to assign __null__ to a scalar property. You should either design your database not to use NULL values for numeric columns, use Number to represent scalar values in your enterprise class (NSNumber in Objective-C), or implement the method __unableToSetNullForKey__ (__unableToSetNilForKey:__ in Objective-C) method in your enterprise object class.
__unableToSetNullForKey__ is part of the EOKeyValueCoding interface, and you use it to set policy for an attempt to assign __null__ to an instance variable that requires a scalar type. Classes can implement this method to determine the behavior when __null__ is assigned to a property in an enterprise object that requires a scalar type (such as __int__ or __double__). One possible implementation is to reinvoke __takeValueForKey__ with a special constant value.

## Cautions in Implementing Accessor Methods

Whether you're implementing accessor methods to be used by the key-value coding methods or overriding the key-value coding methods themselves, you need to be aware of a few issues. The first involves handling NULL values from the database; the second involves accessing property values while they're being set.
NULL values in a database come into the access layer as EONullValue objects (EONull objects in Objective-C), but they're converted to __null__ (or __nil__ in Objective-C) before they're passed to your enterprise objects. The preceding section described how this scheme can cause problems for properties with numeric types, but they can cause problems for other property types as well. If your database uses NULL values, your enterprise objects may want to check any object values received through accessor methods to see that they're not __null__ (or __nil__) before sending them messages.
You can encounter another kind of problem if your object's accessor methods for one property assume that another property has already been set and exists in usable form. Enterprise Objects Framework doesn't guarantee the order that properties are set, so your object's accessor methods can't count on the values of other properties being initialized or usable. Also, when the Framework creates an enterprise object, it creates _faults_ for related objects, and these faults can be passed to your enterprise objects in a key-value coding message while the Framework is busy fetching. Your accessor methods (or overridden key-value coding methods) should be doubly careful about sending messages to objects fetched through relationships, because these messages can cause a fault object to attempt a fetch while the Framework is already busy, resulting in resource contention.
In most cases, you can overcome this problem using the stored value methods described in the section "[Private Access with the Stored Value Methods](Implementing%20an%20Enterprise%20Object.md#apple-gezdknjy)."

## Don't Override equals

Your enterprise objects shouldn't override the __equals__ method (__isEqual:__ in Objective-C). This is because Enterprise Objects Framework relies on the default implementation to check instance equality rather than value equality.
[!Table of Contents](Designing%20Enterprise%20Objects.md) [!Next Section](Advanced%20Enterprise%20Object%20Modeling.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
