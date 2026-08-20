---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/NSExceptionAdditions.html
archived_at: '2026-07-18T01:28:40.469219Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](NSArray.md)
[!](NSObject%20Additions.md)

---

# NSException Additions

__Inherits From:__
NSObject

__Declared in:__ EOControl/EOClassDescription.h

Enterprise Objects Framework adds methods to the Foundation Framework's NSException class for handling validating errors and augmenting an exception's `userInfo` dictionary. The methods used for validation errors are __validationExceptionWithFormat:__ and __aggregateExceptionWithExceptions:__ . You use __validationExceptionWithFormat:__ in an enterprise object's __validateFor...__ or __validate__ _Property___:__ method, as described in the NSObject Additions class specification. The other method used for validation errors, __aggregateExceptionWithExceptions:__ , is used internally by the Framework to group multiple validation exceptions together.

The method __exceptionAddingEntriesToUserInfo:__ is used to augment an exception's `userInfo` dictionary.

**Creating a validation exception**

**+ validationExceptionWithFormat:**

**Collecting exceptions**

**+ aggregateExceptionWithExceptions:**

**Returning an exception with an augmented userInfo dictionary**

**- exceptionAddingEntriesToUserInfo:**

---

#### aggregateExceptionWithExceptions:

+ (NSException \*)`aggregateExceptionWithExceptions:`(NSArray \*)_subexceptions_

Returns an NSException with the same name, reason, and `userInfo` dictionary of the first exception in the _subexceptions_ array, but with the `userInfo` dictionary augmented with the list of subexceptions under the key EOAdditionalExceptionsKey.

__See also:__ - __exceptionAddingEntriesToUserInfo:__

---

#### validationExceptionWithFormat:

+ (NSException \*)__validationExceptionWithFormat:__ (NSString \*)_format_, ...

Returns an NSException whose name is EOValidationException and whose reason is an NSString created from _format_ and subsequent arguments. For example:

> ```
> [NSException validationExceptionWithFormat:@"invalid name \"%@\": entity names cannot be
> nil or empty", name];
> ```

---

#### exceptionAddingEntriesToUserInfo:

- (NSException \*)`exceptionAddingEntriesToUserInfo:`(NSDictionary \*)_additions_

Returns an NSException whose `userInfo` dictionary has been augmented with the object and property information contained in _additions_. When exceptions are raised by certain validation methods such as `validateValue:forKey:`, this message is sent to the exception to create a duplicate exception with object and property information added to the new exception's `userInfo` dictionary. This information is stored in the `userInfo` dictionary under the keys EOValidatedObjectUserInfoKey and EOValidatedPropertyUserInfoKey, respectively. The exception that's returned by this method has the same class with the same name and reason as the original exception; the only difference is the augmented `userInfo` dictionary.

---

[!](NSArray.md)
[!](NSObject%20Additions.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
