---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSValUtil.html
archived_at: '2026-07-15T08:13:56.708051Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSValidation.Utility

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSValidation.Utility class is a convenience that allows you to access the properties of NSValidation objects and non-NSValidation objects using the same code. For more information, see the [NSValidation](NSValidation.md#apple-infemrcejfeec) interface specification.

## Static Methods

---

### validateTakeValueForKeyPath

`public static Object validateTakeValueForKeyPath( Object anObject, Object value, String keyPath) throws NSValidation.ValidationException`

If _anObject_ is an [NSValidation](NSValidation.md#apple-infemrcejfeec), invokes [validateTakeValueForKeyPath](NSValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstkzqwy2lemf2gs33of53gc3djmrqxizkumfvwkvtbnr2wkrtpojfwk6kqmf2gq) on _anObject_; otherwise invokes [NSValidation.DefaultImplementation](NSValidation.DefaultImplementation.md#apple-incukr2ejfeei)'s [validateTakeValueForKeyPath](NSValidation.DefaultImplementation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvtbnruwiylunfxw4lsemvtgc5lmorew24dmmvwwk3tumf2gs33of53gc3djmrqxizkumfvwkvtbnr2wkrtpojfwk6kqmf2gq) method with _anObject_ as the object on which to operate.

---

### validateValueForKey

`public static Object validateValueForKey( Object anObject, Object value, String key) throws NSValidation.ValidationException`

If _anObject_ is an [NSValidation](NSValidation.md#apple-infemrcejfeec), invokes [validateValueForKey](NSValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstkzqwy2lemf2gs33of53gc3djmrqxizkwmfwhkzkgn5zewzlz) on _anObject_; otherwise invokes [NSValidation.DefaultImplementation](NSValidation.DefaultImplementation.md#apple-incukr2ejfeei)'s [validateValueForKey](NSValidation.DefaultImplementation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvtbnruwiylunfxw4lsemvtgc5lmorew24dmmvwwk3tumf2gs33of53gc3djmrqxizkwmfwhkzkgn5zewzlz) method with _anObject_ as the object on which to operate.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
