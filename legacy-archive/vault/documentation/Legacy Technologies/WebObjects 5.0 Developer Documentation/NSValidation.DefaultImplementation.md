---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSValDfltImpl.html
archived_at: '2026-07-15T08:13:56.667824Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSValidation.DefaultImplementation

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSValidation.DefaultImplementation class provides default implementations of the NSValidation interface. For more information, see the [NSValidation](NSValidation.md#apple-infemrcejfeec) interface specification.

## Static Methods

---

### validateTakeValueForKeyPath

`public static Object validateTakeValueForKeyPath( Object anObject, Object value, String key) throws NSValidation.ValidationException`

Confirms that _value_ is legal for the receiver's property named by _keyPath_, and assigns the value to the property if it's legal (and if _value_ is different from the current value), or throws an [NSValidation.ValidationException](NSValidation.ValidationException.md#apple-ijeugssfjjdeg) if _value_ isn't legal.

__See Also:__ [validateTakeValueForKeyPath](NSValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstkzqwy2lemf2gs33of53gc3djmrqxizkumfvwkvtbnr2wkrtpojfwk6kqmf2gq) ( [NSValidation](NSValidation.md#apple-infemrcejfeec))

---

### validateValueForKey

`public static Object validateValueForKey( Object anObject, Object value, String key) throws NSValidation.ValidationException`

Confirms that _value_ is legal for the receiver's property named by _key_, and returns the validated value if it's legal, or throws an [NSValidation.ValidationException](NSValidation.ValidationException.md#apple-ijeugssfjjdeg) if it isn't.

__See Also:__ [validateValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvtbnruwiylunfxw4lsemvtgc5lmorew24dmmvwwk3tumf2gs33of53gc3djmrqxizkwmfwhkzkgn5zewzlz) ( [NSValidation](NSValidation.md#apple-infemrcejfeec))

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
