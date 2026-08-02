---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSValExc.html
archived_at: '2026-07-15T08:13:56.686609Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSValidation.ValidationException

> **__Inherits from:__**
> : RuntimeException : Exception : Throwable : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

Instances of the NSValidation.ValidationException class are created and thrown when an error condition is encountered during the validation of an object that implements NSValidation. For more information, see the interface specification for [NSValidation](NSValidation.md#apple-infemrcejfeec).

## Constants

---

[NSValidation.ValidationException](#apple-ijeugssfjjdeg) defines the following constants:

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| AdditionalExceptionsKey | `String` | The key for an entry in the exception's user info dictionary that contains subexceptions. This constant is deprecated. You should access this user info dictionary entry using the [additionalExceptions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkzqwy2lemf2gs33ofzlgc3djmrqxi2lpnzcxqy3fob2gs33of5qwizdjoruw63tbnrcxqy3fob2gs33oom) method. |
| ValidatedKeyUserInfoKey | `String` | The key for an entry in the exception's user info dictionary. The entry contains the key for the property that failed to validate. This constant is deprecated. You should access this user info dictionary entry using the [key](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkzqwy2lemf2gs33ofzlgc3djmrqxi2lpnzcxqy3fob2gs33of5vwk6i) method. |
| ValidatedObjectUserInfoKey | `String` | A key for an entry in the exception's user info dictionary. The entry contains the object that failed to validate. This constant is deprecated. You should access this user info dictionary entry using the [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkzqwy2lemf2gs33ofzlgc3djmrqxi2lpnzcxqy3fob2gs33of5xwe2tfmn2a) method. |

## Constructors

---

### NSValidation.ValidationException

`public NSValidation.ValidationException(String message)`

Creates and returns a new exception with _message_ as the message.

`public NSValidation.ValidationException( String message, NSDictionary userInfo)`

Deprecated in the Java Foundation framework. Don't use this method. Use __NSValidation.ValidationException(String,Object,String)__ instead.

`public NSValidation.ValidationException( String message, Object anObject, String key)`

Creates and returns a new exception with _message_ as the message and a userInfo dictionary specifying _anObject_ for the [ValidatedObjectUserInfoKey](#apple-ijaucrccirbuo) and _key_ for the [ValidatedKeyUserInfoKey](#apple-ijeecr2iiveeo).

---

## Static Methods

---

### aggregateExceptionWithExceptions

`public static NSValidation.ValidationException aggregateExceptionWithExceptions( NSArray exceptions)`

Returns an exception that is the aggregate of the exceptions in the _exceptions_ array. The returned aggregate exception has the message and userInfo dictionary of the first exception in the _exceptions_ array, but the userInfo dictionary is augmented with the list of subexceptions under the key [AdditionalExceptionsKey](#apple-ijaucq2ei5bek).

---

## Instance Methods

---

### additionalExceptions

`public NSArray additionalExceptions()`

Returns the array in the receiver's userInfo dictionary for the [AdditionalExceptionsKey](#apple-ijaucq2ei5bek).

---

### exceptionAddingEntriesToUserInfo

`public NSValidation.ValidationException exceptionAddingEntriesToUserInfo( Object anObject, String key)`

Deprecated in the Java Foundation framework. Don't use this method. Use [exceptionWithObjectAndKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkzqwy2lemf2gs33ofzlgc3djmrqxi2lpnzcxqy3fob2gs33of5sxqy3fob2gs33ok5uxi2cpmjvgky3uifxgis3fpe) instead. Returns a new exception that is a copy of the receiver message and userInfo, but whose userInfo dictionary has been augmented with anObject and key.

---

### __exceptionWithObjectAndKey__

`public NSValidation.ValidationException exceptionWithObjectAndKey(Object anObject, String key)`

Returns a new exception with the same message as the receiver, but whose userInfo dictionary contains contains _anObject_ and _key_. When validation exceptions are raised by certain validation methods such as [validateValueForKey](NSValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstkzqwy2lemf2gs33of53gc3djmrqxizkwmfwhkzkgn5zewzlz), this method is invoked on the exception to create a duplicate exception with object and property information stored to the new exception's userInfo dictionary. The information is stored under the keys [ValidatedObjectUserInfoKey](#apple-ijaucrccirbuo) and [ValidatedKeyUserInfoKey](#apple-ijeecr2iiveeo), respectively. The exception this method returns has the same message as the original, receiving exception; the only difference is the userInfo dictionary.

---

### key

`public String key()`

Returns the key in the receiver's userInfo dictionary for the [ValidatedKeyUserInfoKey](#apple-ijeecr2iiveeo).

---

### object

`public Object object()`

Returns the value in the receiver's userInfo dictionary for the [ValidatedObjectUserInfoKey](#apple-ijaucrccirbuo).

---

### __userInfo__

`public NSDictionary userInfo()`

Deprecated in the Java Foundation framework. Don't use this method. Access the individual entries using the [key](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkzqwy2lemf2gs33ofzlgc3djmrqxi2lpnzcxqy3fob2gs33of5vwk6i) and [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkzqwy2lemf2gs33ofzlgc3djmrqxi2lpnzcxqy3fob2gs33of5xwe2tfmn2a) methods. Returns the receiver's userInfo dictionary.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
