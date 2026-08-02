---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSKVCAddDfltImpl.html
archived_at: '2026-07-15T08:13:55.985069Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCodingAdditions.DefaultImplementation

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSKeyValueCodingAdditions. DefaultImplementation class provides default implementations of the NSKeyValueCodingAdditions interface. For more information, see the [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek) interface specification.

## Static Methods

---

### takeValueForKeyPath

`public static void takeValueForKeyPath( Object anObject, Object value, String keyPath)`

Sets _anObject_'s property identified by _keyPath_ to _value_. A key path has the form _relationship.property_ (with one or more relationships). This method gets the destination object for each relationship using [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe), and sends the final object a [takeValueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz)message with _value_ and _property_.

__See Also:__ [takeValueForKeyPath](NSKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3umfvwkvtbnr2wkrtpojfwk6kqmf2gq) ( [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek))

---

### valueForKeyPath

`public static Object valueForKeyPath( Object anObject, String keyPath)`

Returns _anObject_'s value for the derived property identified by _keyPath_. A key path has the form _relationship.property_ (with one or more relationships). This method gets the destination object for each relationship using [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe), and returns the result of a __valueForKey__ message to the final object.

__See Also:__ [valueForKeyPath](NSKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3wmfwhkzkgn5zewzlzkbqxi2a) ( [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek))

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
