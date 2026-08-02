---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSKVCAddUtil.html
archived_at: '2026-07-15T08:13:55.999690Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCodingAdditions.Utility

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSKeyValueCodingAdditions.Utility class is a convenience that allows you to access the properties of [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek) objects and non-__NSKeyValueCodingAdditions__ objects using the same code. For more information, see the [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek) interface specification.

## Static Methods

---

### takeValueForKeyPath

`public static void takeValueForKeyPath( Object anObject, Object value, String keyPath)`

If _anObject_ is an [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek), invokes [takeValueForKeyPath](NSKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3umfvwkvtbnr2wkrtpojfwk6kqmf2gq) on _anObject_; otherwise invokes [NSKeyValueCodingAdditions. DefaultImplementation](NSKeyValueCodingAdditions.DefaultImplementation.md#apple-iraumrkki5cui)'s [takeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgs3fpflgc3dvmvbw6zdjnztuczdenf2gs33oomxfk5djnruxi6jporqwwzkwmfwhkzkgn5zewzlzkbqxi2a) method with _anObject_ as the object on which to operate.

---

### valueForKeyPath

`public static Object valueForKeyPath( Object anObject, String keyPath)`

If _anObject_ is an [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek), invokes [valueForKeyPath](NSKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3wmfwhkzkgn5zewzlzkbqxi2a) on _anObject_; otherwise invokes [NSKeyValueCodingAdditions. DefaultImplementation](NSKeyValueCodingAdditions.DefaultImplementation.md#apple-iraumrkki5cui)'s [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgs3fpflgc3dvmvbw6zdjnztuczdenf2gs33oomxfk5djnruxi6jpozqwy5lfizxxes3fpfigc5di) method with _anObject_ as the object on which to operate.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
