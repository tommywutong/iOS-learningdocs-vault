---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/NSExceptionAdditions.html
archived_at: '2026-07-15T08:11:42.140052Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# NSException Additions

> __Category
> of:__ NSException

> __Declared in:__ : EOControl/EOClassDescription.h

---

## Category Description

---

Enterprise Objects Framework adds methods to the Foundation
Framework's NSException class for handling validating errors and
augmenting an exception's userInfo dictionary. The methods used
for validation errors are [validationExceptionWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjzjuk6ddmvyhi2lpnyqeczdenf2gs33oomxxmylmnfsgc5djn5xek6ddmvyhi2lpnzlws5diizxxe3lboq5a) and [aggregateExceptionWithExceptions:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjzjuk6ddmvyhi2lpnyqeczdenf2gs33oomxwcz3hojswoylumvcxqy3fob2gs33ok5uxi2cfpbrwk4dunfxw44z2).
You use __validationExceptionWithFormat:__ in
an enterprise object's __validateFor...__ or __validate___Property___:__ method,
as described in the NSObject Additions class specification. The
other method used for validation errors, __aggregateExceptionWithExceptions:__,
is used internally by the Framework to group multiple validation
exceptions together.

The method [exceptionAddingEntriesToUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2fpbrwk4dunfxw4icbmrsgs5djn5xhgl3fpbrwk4dunfxw4qlemruw4z2fnz2he2lfonkg6vltmvzes3tgn45a) is
used to augment an exception's __userInfo__ dictionary.

## Class Methods

---

### aggregateExceptionWithExceptions:

`+ (NSException *)aggregateExceptionWithExceptions:(NSArray
*)subexceptions`

Returns an NSException with the same name, reason,
and userInfo dictionary of the first exception in the _subexceptions_ array,
but with the userInfo dictionary augmented with the list of subexceptions under
the key EOAdditionalExceptionsKey.

__See Also:__  [- exceptionAddingEntriesToUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2fpbrwk4dunfxw4icbmrsgs5djn5xhgl3fpbrwk4dunfxw4qlemruw4z2fnz2he2lfonkg6vltmvzes3tgn45a)

---

### validationExceptionWithFormat:

`+ (NSException *)validationExceptionWithFormat:(NSString
*)format,
...`

Returns an NSException whose name is EOValidationException
and whose reason is an NSString created from _format_ and
subsequent arguments. For example:
> ```
> [NSException validationExceptionWithFormat:@"invalid name \"%@\": entity names cannot be nil or  empty", name];
> ```

---

## Instance Methods

---

### exceptionAddingEntriesToUserInfo:

`- (NSException *)exceptionAddingEntriesToUserInfo:(NSDictionary
*)additions`

Returns an NSException whose userInfo dictionary
has been augmented with the object and property information contained
in _additions_. When exceptions are
raised by certain validation methods such as __validateValue:forKey:__,
this message is sent to the exception to create a duplicate exception
with object and property information added to the new exception's
userInfo dictionary. This information is stored in the userInfo
dictionary under the keys EOValidatedObjectUserInfoKey and EOValidatedPropertyUserInfoKey,
respectively. The exception that's returned by this method has
the same class with the same name and reason as the original exception;
the only difference is the augmented userInfo dictionary.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
