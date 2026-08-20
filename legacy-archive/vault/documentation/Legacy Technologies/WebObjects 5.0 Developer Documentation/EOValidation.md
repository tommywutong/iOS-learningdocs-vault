---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOValidation.html
archived_at: '2026-07-15T08:13:48.238932Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOValidation

> __(informal interface)__
>
> __Implemented by:__
> EOEnterpriseObject
> EOCustomObject
> EOGenericRecord
>
> __Package:__ com.webobjects.eocontrol

---

## Interface Description

---

The EOValidation interface defines the way that enterprise objects validate their values. The validation methods check for illegal value types, values outside of established limits, illegal relationships, and so on. EOCustomObject and EOGenericRecord provide default implementations of EOValidation, which are described in detail in this specification.

There are two kinds of validation methods. The first validates individual properties, and the second validates an entire object to see if it's ready for a specific operation (inserting, updating, and deleting). The two different types are discussed in more detail in the sections ["Validating Individual Properties" (page 415)](EOValidation.Concepts.md#apple-infemrccizeec) and ["Validating Before an Operation" (page 416)](EOValidation.Concepts.md#apple-infemrkbifbuu).

## Instance Methods

---

### validateForDelete

`public abstract void validateForDelete()`

Confirms that the receiver can be deleted in its current state, throwing an NSValidation.ValidationException if it can't. For example, an object can't be deleted if it has a relationship with a delete rule of EOClassDescription.DeleteRuleDeny and that relationship has a destination object.

EOCustomObject's implementation sends the receiver's EOClassDescription a message (which performs basic checking based on the presence or absence of values). Subclasses should invoke __super__'s implementation before performing their own validation, and should combine any exception thrown by __super__'s implementation with their own.:

__See Also:__ propagateDeleteWithEditingContext (EOEnterpriseObject),

---

### validateForInsert

`public abstract void validateForInsert()`

Confirms that the receiver can be inserted in its current state, throwing an NSValidation.ValidationException if it can't. EOCustomObject's implementation simply invokes [validateForSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfgylwmu).

The method __validateForSave__ is the generic validation method for when an object is written to the external store. If an object performs validation that isn't specific to insertion, it should go in __validateForSave__.

---

### validateForSave

`public abstract void validateForSave()`

Confirms that the receiver can be saved in its current state, throwing an NSValidation.ValidationException if it can't. EOCustomObject's implementation sends the receiver's EOClassDescription a validateObjectForSave message, then iterates through all of the receiver's properties. If this results in more than one exception, the exception returned contains the additional ones in its __userInfo__ dictionary under the NSValidation.ValidationException`.`AdditionalExceptionsKey. Subclasses should invoke __super__'s implementation before performing their own validation, and should combine any exception thrown by __super__'s implementation with their own.

Enterprise objects can implement this method to check that certain relations between properties hold; for example, that the end date of a vacation period follows the begin date. To validate an individual property, you can simply implement a method for it.

__See Also:__ NSValidation.ValidationException constructor

---

### validateForUpdate

`public abstract void validateForUpdate()`

Confirms that the receiver can be inserted in its current state, NSValidation.ValidationException. EOCustomObject's implementation simply invokes [validateForSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfgylwmu).

The method __validateForSave__ is the generic validation method for when an object is written to the external store. If an object performs validation that isn't specific to updating, it should go in __validateForSave__.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
