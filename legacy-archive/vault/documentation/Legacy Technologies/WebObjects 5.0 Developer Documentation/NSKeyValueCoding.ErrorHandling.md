---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSKVCErrHandling.html
archived_at: '2026-07-15T08:13:56.852998Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCoding.ErrorHandling

> **__Package:__**
> : com.webobjects.foundation

---

## Interface Description

---

The NSKeyValueCoding.ErrorHandling interface declares an API for handling errors that occur during key-value coding. For more information, see the [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) interface specification.

## Instance Methods

---

### handleQueryWithUnboundKey

`public Object handleQueryWithUnboundKey(String key)`

Invoked from [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) when it finds no property binding for _key_. The default implementation (see the [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui) class specification) throws an NSKeyValueCoding.UnknownKeyException, with the target object ( [TargetObjectUserInfoKey](NSKeyValueCoding.UnknownKeyException.md#apple-ijaucq2ei5bek)) and key ( [UnknownUserInfoKey](NSKeyValueCoding.UnknownKeyException.md#apple-ijeecr2iiveeo)) in the user info. An NSKeyValueCoding.ErrorHandling class can override this method to handle the query in some other way. The method can return a value, in which case that value is returned by the corresponding [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) invocation.

---

### handleTakeValueForUnboundKey

`public void handleTakeValueForUnboundKey( Object value, String key)`

Invoked from [takeValueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) when it finds no property binding for _key_. The default implementation (see the [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui) class specification) throws an NSKeyValueCoding.UnknownKeyException, with the target object ( [TargetObjectUserInfoKey](NSKeyValueCoding.UnknownKeyException.md#apple-ijaucq2ei5bek)) and key ( [UnknownUserInfoKey](NSKeyValueCoding.UnknownKeyException.md#apple-ijeecr2iiveeo)) in the user info.

---

### unableToSetNullForKey

`public void unableToSetNullForKey(String key)`

Invoked from [takeValueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) when it's given a `null` value for a scalar property (such as an __int__ or a __float__). The default implementation (see the [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui) class specification) throws an IllegalArgumentException. You might want to implement the method (or override the inherited implementation) to handle the request in some other way, such as by substituting zero or a sentinel value and invoking [takeValueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) again.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
