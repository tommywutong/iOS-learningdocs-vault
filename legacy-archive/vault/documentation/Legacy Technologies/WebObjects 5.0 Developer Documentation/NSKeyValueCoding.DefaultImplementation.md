---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSKVCDfltImpl.html
archived_at: '2026-07-15T08:13:56.015726Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCoding.DefaultImplementation

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSKeyValueCoding. DefaultImplementation class provides default implementations of the NSKeyValueCoding and NSKeyValueCoding.ErrorHandling interfaces. For more information, see the [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) and [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo) interface specifications.

## Static Methods

---

### handleQueryWithUnboundKey

`public static Object handleQueryWithUnboundKey( Object anObject, String key)`

Throws an [NSKeyValueCoding. UnknownKeyException](NSKeyValueCoding.UnknownKeyException.md#apple-incemscfineeq) with _anObject_ as the exception's object and _key_ as the exception's key. Invoked from valueForKey when it finds no property binding for _key_.

__See Also:__ [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo)

---

### handleTakeValueForUnboundKey

`public static void handleTakeValueForUnboundKey( Object anObject, Object value, String key)`

Throws an [NSKeyValueCoding. UnknownKeyException](NSKeyValueCoding.UnknownKeyException.md#apple-incemscfineeq) with _anObject_ as the exception's object and _key_ as the exception's key. Invoked from takeValueForKey when it finds no property binding for _key_.

__See Also:__ [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo)

---

### takeValueForKey

`public static void takeValueForKey( Object anObject, Object value, String key)`

Sets _anObject_'s property identified by _key_ to _value_, or invokes __handleTakeValueForUnboundKey__.

__See Also:__ [takeValueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) ( [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu))

---

### unableToSetNullForKey

`public static void unableToSetNullForKey( Object anObject, String key)`

Throws an IllegalArgumentException. Invoked from takeValueForKey when it's given a `null` value for a scalar property (such as an __int__ or a __float__).

__See Also:__ [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo)

---

### valueForKey

`public static Object valueForKey( Object anObject, String key)`

Returns _anObject_'s value for the property identified by _key_, or invokes __handleQueryWithUnboundKey__.

__See Also:__ [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) ( [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu))

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
