---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.012.html
archived_at: '2026-07-15T07:57:55.561734Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Support%20for%20Multi-Threaded%20Applications.md)

# Changes to Key-Value Coding

In release 3.0, Enterprise Objects Framework makes slight changes to key-value coding:

- The implementations of the primitive key-value coding methods resolve their keys differently: the search order for resolving the key has changed and the __valueForKey__ methods now support Java-style getter methods (such as __get___Key_). More detailed information on the search order is provided in the table below.
- A new method, __storedValueForKey__:, has been added to the set of primitive key-value coding methods. It is the corresponding getter method to __takeStoredValue:forKey:__ (Objective-C) and __takeStoredValue__ (Java).
- The methods __takeStoredValue:forKeyPath:__ and __takeStoredValuesFromDictionary:__ have been removed.

The new key-value coding API is summarized in the following table:

|  Key-Value Coding Primitives |  Key-Value Coding Primitives |
|  valueForKey: |  The search order for resolving the provided key has changed to the following:  method get_Key_, _key_ method _get_Key_, __key_ instance variable __key_, _key_ |
|  takeValue:forKey:(Objective-C)  takeValueForKey (Java) |  The search order for resolving the provided key has changed to the following:  method set_Key_, _set_Key_ instance variable _key_, __key_ |
|  storedValueForKey: |  The search order for resolving the provided key has changed to the following:  method _get_Key_, __key_ instance variable __key_, _key_ method get_Key_, _key_ |
|  takeStoredValue:forKey:(Objective-C)  takeStoredValueForKey (Java) |  The search order for resolving the provided key has changed to the following:  method _set_Key_, __key_ instance variable _key_, set_Key_ |

```
```


## Stored Value Methods

The stored value methods, __storedValueForKey:__ and __takeStoredValue:forKey:__ (__storedValueForKey__ and __takeStoredValueForKey__ in Java), are used by the framework when accessing properties of an enterprise object to get or set properties for state storage and restoration (either from the database or to an in-memory snapshot). This access is considered private to the enterprise object and is invoked by the Framework to effect persistence on the object's behalf.
On the other hand, the basic key-value coding methods, __valueForKey:__ and __takeValue:forKey:__ (__valueForKey__ and __takeValueForKey__ in Java), are the public interface to an enterprise object. They are invoked by clients external to the object (such as for interactions with user interface or other business object logic).
Enterprise object classes can take advantage of this distinction to perform additional processing in accessor methods except when the object is being initialized with values from an external store. For instance, suppose an object wanted to update a total whenever the bonus was set:

```
void setBonus(double newBonus) {
    willChange();
    _total += (newBonus - _bonus);
}
```


This code should be activated when the object is updated with values provided by a user through the application's user interface, but not when the __bonus__ property is restored from the database. Since the Framework restores the property using __takeStoredValue:forKey:__ (__takeStoredValueForKey__ in Java)and since this method accesses the ___bonus__ instance variable in preference to calling the accessor, the unnecessary (and possibly harmful) recomputation of ___total__ is avoided. If the object actually wants to intervene when a property is set from the database, it has two options:

- Implement ___setBonus:__
- Turn off stored accessors by overriding the class (Objective-C) or static (Java) method __useStoredAccessor__ to return NO or __false__.

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Changes%20to%20Enterprise%20Object%20Validation.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
