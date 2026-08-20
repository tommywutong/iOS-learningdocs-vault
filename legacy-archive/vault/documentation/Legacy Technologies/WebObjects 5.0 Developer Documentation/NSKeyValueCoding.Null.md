---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSKVCNull.html
archived_at: '2026-07-15T08:13:56.032654Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCoding.Null

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Serializable: Cloneable: NSCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSKeyValueCoding.Null is a final class that defines a unique object used to represent `null` values in collection objects, such as NSArrays, which don't allow `null` values.

For instance, Enterprise Objects Framework uses NSKeyValueCoding.Null to represent null values from database rows in its database level snapshots (NSDictionary objects). However, Enterprise Objects Framework automatically translates NSKeyValueCoding.Null to `null` in enterprise objects, so you should rarely need to write code that accounts for this class.

Whenever `null` is represented by NSKeyValueCoding.Null, it should be represented with the instance stored in the [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) constant, [NullValue](NSKeyValueCoding.md#apple-ijaucrccirbuo). You can safely use this instance with the == operator to test for the presence of a null value:

> ```
> if (value == NSKeyValueCoding.NullValue) {
>     /* ... */
> }
> ```

## Interfaces Implemented

---

> : [NSCoding](NSCoding.md#apple-ineucskcizbeq)
>
> : [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjnsxsvtbnr2wkq3pmruw4zzojz2wy3bpmnwgc43tizxxeq3pmrsxe): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjnsxsvtbnr2wkq3pmruw4zzojz2wy3bpmvxgg33emvlws5diinxwizls)
>
> :
>
> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjnsxsvtbnr2wkq3pmruw4zzojz2wy3bpmnwg63tf)
>
> :

## Static Methods

---

### decodeObject

`public static Object decodeObject(NSCoder aNSCoder)`

Returns the shared instance of NSKeyValueCoding.Null stored in the [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) constant [NullValue](NSKeyValueCoding.md#apple-ijaucrccirbuo).

__See Also:__ [NSCoding](NSCoding.md#apple-ineucskcizbeq) Interface Description

---

## Instance Methods

---

### classForCoder

`public Class classForCoder()`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description for [classForCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) in the NSCoding interface specification.

---

### clone

`public Object clone()`

Simply returns the shared instance of NSKeyValueCoding.Null stored in the constant [NullValue](NSKeyValueCoding.md#apple-ijaucrccirbuo).

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder aNSCoder)`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description for [encodeWithCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) in the NSCoding interface specification.

---

### toString

`public String toString()`

Returns a string representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
