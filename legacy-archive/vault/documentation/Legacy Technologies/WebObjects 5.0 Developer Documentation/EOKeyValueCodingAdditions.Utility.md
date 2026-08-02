---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOKVCAdditionsUtil.html
archived_at: '2026-07-15T08:13:46.973322Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOKeyValueCodingAdditions.Utility

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

The EOKeyValueCodingAdditions.Utility class is a convenience that allows you to access the properties of EOKeyValueCodingAdditions objects and non-EOKeyValueCodingAdditions objects using the same code.

Utility's methods are just like the methods defined by the EOKeyValueCodingAdditions interface, except they are static methods and they take an extra argument-the object on which the method should operate. Utility's methods simply check to see if the object on which they operate is an EOKeyValueCodingAdditions object and invoke the corresponding EOKeyValueCodingAdditions method on the object if it is. Otherwise, they invoke the corresponding DefaultImplementation method (formerly implemented in the Support class), passing the object on which to operate.

For example, suppose that you want to access an object with the EOKeyValueCodingAdditions API but you don't know if the object is an EOKeyValueCodingAdditions object. To do so, you simply use the corresponding Utility API, as in the following line of code:

> ```
> values = EOKeyValueCodingAdditions.Utility.valuesForKeys(object, keys);
> ```

The above line of code is simply a short-cut for the following:

> ```
> if (object instanceof EOKeyValueCodingAdditions) {
>     values = ((EOKeyValueCodingAdditions)object).valuesForKeys(keys);
> } else {
>     values = EOKeyValueCodingAdditions.DefaultImplementation.valuesForKeys(         object, keys);
> }
> ```

## Instance Methods

---

### takeValuesFromDictionary

`public abstract void takeValuesFromDictionary( Object object, NSDictionary dictionary)`

If the specified object is an EOKeyValueCodingAdditions object, invokes __takeValuesFromDictionary__ on that object; otherwise invokes EOKeyValueCodingAdditions.DefaultImplementation's __takeValuesFromDictionary__ method with the object as the object on which to operate.

---

### valuesForKeys

`public abstract NSDictionary valuesForKeys( Object object, NSArray keys)`

If the specified object is an EOKeyValueCodingAdditions object, invokes __valuesForKeys__ on that object; otherwise invokes EOKeyValueCodingAdditions.DefaultImplementation's __valuesForKeys__ method with the object as the object on which to operate.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
