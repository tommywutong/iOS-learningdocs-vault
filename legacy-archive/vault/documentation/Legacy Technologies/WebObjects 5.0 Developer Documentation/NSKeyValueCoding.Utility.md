---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSKVCUtil.html
archived_at: '2026-07-15T08:13:56.088063Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCoding.Utility

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSKeyValueCoding.Utility class is a convenience that allows you to access the properties of [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) objects and non-NSKeyValueCoding objects using the same code. For more information, see the [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) and interface specification.

## Static Methods

---

### handleQueryWithUnboundKey

`public static Object handleQueryWithUnboundKey( Object anObject, String key)`

If _anObject_ is an [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo), invokes [handleQueryWithUnboundKey](NSKeyValueCoding.ErrorHandling.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzoivzhe33sjbqw4zdmnfxgol3imfxgi3dfkf2wk4tzk5uxi2cvnzrg65lomrfwk6i) on _anObject_; otherwise invokes [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui)'s handleQueryWithUnboundKey method with _anObject_ as the object on which to operate.

---

### handleTakeValueForUnboundKey

`public static void handleTakeValueForUnboundKey( Object anObject, Object value, String key)`

If _anObject_ is an [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo), invokes [handleTakeValueForUnboundKey](NSKeyValueCoding.ErrorHandling.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzoivzhe33sjbqw4zdmnfxgol3imfxgi3dfkrqwwzkwmfwhkzkgn5zfk3tcn52w4zclmv4q) on _anObject_; otherwise invokes [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui)'s handleTakeValueForUnboundKey method with _anObject_ as the object on which to operate.

---

### takeValueForKey

`public static void takeValueForKey( Object anObject, Object value, String key)`

If _anObject_ is an [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu), invokes [takeValueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) on _anObject_; otherwise invokes [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui)'s takeValueForKey method with _anObject_ as the object on which to operate.

---

### unableToSetNullForKey

`public static void unableToSetNullForKey( Object anObject, String key)`

If _anObject_ is an [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo), invokes [unableToSetNullForKey](NSKeyValueCoding.ErrorHandling.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzoivzhe33sjbqw4zdmnfxgol3vnzqwe3dfkrxvgzlujz2wy3cgn5zewzlz) on _anObject_; otherwise invokes [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui)'s unableToSetNullForKey method with _anObject_ as the object on which to operate.

---

### valueForKey

`public static Object valueForKey( Object anObject, String key)`

If _anObject_ is an [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu), invokes [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) on _anObject_; otherwise invokes [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui)'s valueForKey method with _anObject_ as the object on which to operate.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
