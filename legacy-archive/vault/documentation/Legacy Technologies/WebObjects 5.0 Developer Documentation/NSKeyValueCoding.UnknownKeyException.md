---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSKVCUnkKeyExc.html
archived_at: '2026-07-15T08:13:56.071815Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCoding.UnknownKeyException

> **__Inherits from:__**
> : RuntimeException

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

Instances of the NSKeyValueCoding. UnknownKeyException class are created and thrown when an unknown key is encountered during key-value coding.

For example, suppose an Employee object receives a [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) message with "partNumber" as the key. The Employee class doesn't declare a method or instance variable for "partNumber", so __valueForKey__ throws an UnknownKeyException. An NSKeyValueCoding. UnknownKeyException has a userInfo dictionary containing entries for the object for which key-value coding failed ( [TargetObjectUserInfoKey](#apple-ijaucq2ei5bek)) and the unknown key ( [UnknownUserInfoKey](#apple-ijeecr2iiveeo)). For the Employee/partNumber example, the `TargetObjectUserInfoKey` entry would contain the Employee object and the `UnknownUserInfoKey` would contain the string "partNumber".

For more information on key-value coding and error conditions, see the [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) and [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo) interface specifications.

## Constants

---

[NSKeyValueCoding. UnknownKeyException](#apple-incemscfineeq) defines the following constants:

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| TargetObjectUserInfoKey | `String` | The key for an entry in the exception's user info dictionary. The entry contains the target object that does not implement the unknown key. This constant is deprecated. You should access this user info dictionary entry using the object method. |
| UnknownUserInfoKey | `String` | The key for an entry in the exception's user info dictionary. The entry contains the unknown key. This constant is deprecated. You should access this user info dictionary entry using the key method. |

## Constructors

---

### NSKeyValueCoding.UnknownKeyException

`public NSKeyValueCoding.UnknownKeyException( String message, Object anObject, String key)`

Creates and returns a new UnknownKeyException with _message_ as the message and a userInfo dictionary specifying _anObject_ for the [TargetObjectUserInfoKey](#apple-ijaucq2ei5bek) and _key_ for the [UnknownUserInfoKey](#apple-ijeecr2iiveeo).

`public NSKeyValueCoding.UnknownKeyException( String message, NSDictionary userInfo)`

Deprecated in the Java Foundation framework. Don't use this method. Use __NSKeyValueCoding.UnknownKeyException(String,Object,String)__ instead. Creates and returns a new UnknownKeyException with the specified message and userInfo dictionary.

---

## Instance Methods

---

### key

`public String key()`

Returns the unknown key that caused the exception to be thrown. Equivalent to getting the [UnknownUserInfoKey](#apple-ijeecr2iiveeo) entry from the userInfo dictionary.

---

### object

`public Object object()`

Returns the object on which key-value coding was operating when an unknown key was encountered. Equivalent to getting the [TargetObjectUserInfoKey](#apple-ijaucq2ei5bek) entry from the userInfo dictionary.

---

### __userInfo__

`public NSDictionary userInfo()`

Deprecated in the Java Foundation framework. Don't use this method. Use the object and key methods to access the exception's object and key instead. Returns the receiver's userInfo dictionary.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
