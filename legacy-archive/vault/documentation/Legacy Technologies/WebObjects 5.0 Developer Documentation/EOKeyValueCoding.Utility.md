---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOKeyValueCodingUtility.html
archived_at: '2026-07-15T08:13:47.050687Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOKeyValueCoding.Utility

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

The EOKeyValueCoding.Utility class is a convenience that allows you to access the properties of EOKeyValueCoding objects and non-EOKeyValueCoding objects using the same code.

Utility's methods are just like the methods defined by the EOKeyValueCoding interface, except they are static methods and they take an extra argument-the object on which the method should operate. Utility's methods simply check to see if the object on which they operate is an EOKeyValueCoding object and invoke the corresponding EOKeyValueCoding method on the object if it is. Otherwise, they invoke the corresponding DefaultImplementation method (formerly implemented in the Support class), passing the object on which to operate.

For example, suppose that you want to access an object with the EOKeyValueCoding API but you don't know if the object is an EOKeyValueCoding object. To do so, you simply use the corresponding Utility API, as in the following line of code:

> ```
> theValue = EOKeyValueCoding.Utility.storedValueForKey(object, key);
> ```

The above line of code is simply a short-cut for the following:

> ```
> if (object instanceof EOKeyValueCoding) {
>     theValue = ((EOKeyValueCoding)object).storedValueForKey(key);
> } else {
>     theValue = EOKeyValueCoding.DefaultImplementation.storedValueForKey(         object, key);
> }
> ```

## Static Methods

---

### storedValueForKey

`public static Object storedValueForKey(Object object, String key)`

If the specified object is an EOKeyValueCoding object, invokes __storedValueForKey__ on that object; otherwise invokes EOKeyValueCoding.DefaultImplementation's __storedValueForKey__ method with the object as the object on which to operate.

---

### decodeWithKeyValueUnarchiver

`public static void takeStoredValueForKey(Object object, Object value, String key)`

If the specified object is an EOKeyValueCoding object, invokes __takeStoredValueForKey__ on that object; otherwise invokes EOKeyValueCoding.DefaultImplementation's __takeStoredValueForKey__ method with the object as the object on which to operate.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
