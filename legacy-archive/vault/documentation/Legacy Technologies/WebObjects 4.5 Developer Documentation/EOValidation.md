---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOValidation.html
archived_at: '2026-07-15T08:11:39.051289Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOValidation

> __Implemented by:__ : EOEnterpriseObject
> : EOCustomObject
> : EOGenericRecord

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The EOValidation interface defines the way that enterprise
objects validate their values. The validation methods check for
illegal value types, values outside of established limits, illegal
relationships, and so on. EOCustomObject and EOGenericRecord provide
default implementations of EOValidation, which are described in
detail in this specification.

There are two kinds of validation methods. The first validates
individual properties, and the second validates an entire object
to see if it's ready for a specific operation (inserting, updating,
and deleting). The two different types are discussed in more detail
in the sections ["Validating Individual Properties"](EOValidation-2.md#apple-infemrccizeec) and ["Validating Before an Operation"](EOValidation-2.md#apple-infemrkbifbuu).

## Instance Methods

---

### validateForDelete

`public abstract void validateForDelete()`

Confirms that the receiver can be deleted in
its current state, throwing an [EOValidation.Exception](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOValidationException.html#BAABJIHH) if it can't.
For example, an object can't be deleted if it has a relationship
with a delete rule of EOClassDescription. [DeleteRuleDeny](EOClassDescription.md#apple-ijaucrchivdeo) and that relationship
has a destination object.

EOCustomObject's implementation sends the receiver's EOClassDescription
a message (which performs basic checking based on the presence or
absence of values). Subclasses should invoke `super`'s implementation
before performing their own validation, and should combine any exception thrown by `super`'s
implementation with their own.

__See Also:__
[propagateDeleteWithEditingContext](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxa4tpobqwoylumvcgk3dforsvo2lunbcwi2lunfxgoq3pnz2gk6du) (EOEnterpriseObject), `EOValidation.` [Exception](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOValidationException.html#//apple_ref/java/instm/EOValidation.Exception/Exception) constructor

---

### validateForInsert

`public abstract void validateForInsert()`

Confirms that the receiver can be inserted in
its current state, throwing an [EOValidation.Exception](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOValidationException.html#BAABJIHH) if it can't. EOCustomObject's
implementation simply invokes [validateForSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfgylwmu).

The method `validateForSave` is the
generic validation method for when an object is written to the external
store. If an object performs validation that isn't specific to
insertion, it should go in `validateForSave`.

---

### validateForSave

`public abstract void validateForSave()`

Confirms that the receiver can be saved in its
current state, throwing an [EOValidation.Exception](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOValidationException.html#BAABJIHH) if it can't. EOCustomObject's
implementation sends the receiver's EOClassDescription a [validateObjectForSave](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxmylmnfsgc5dfj5rguzldordg64stmf3gk) message,
then iterates through all of the receiver's properties, invoking [validateValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkwmfwhkzkgn5zewzlz) for
each one. If this results in more than one exception, the exception
returned contains the additional ones in its `userInfo` dictionary
under the EOValidation.Exception`.` [AdditionalExceptionsKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOValidationException.html#CHCFHDBI). Subclasses
should invoke `super`'s implementation before
performing their own validation, and should combine any exception thrown by `super`'s implementation
with their own.

Enterprise objects can implement this method to check that
certain relations between properties hold; for example, that the
end date of a vacation period follows the begin date. To validate
an individual property, you can simply implement a method for it
as described under `validateValueForKey`.

__See Also:__
`EOValidation.` [Exception](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOValidationException.html#//apple_ref/java/instm/EOValidation.Exception/Exception) constructor

---

### validateForUpdate

`public abstract void validateForUpdate()`

Confirms that the receiver can be inserted in
its current state, [EOValidation.Exception](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOValidationException.html#BAABJIHH). EOCustomObject's
implementation simply invokes [validateForSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfgylwmu).

The method `validateForSave` is the
generic validation method for when an object is written to the external
store. If an object performs validation that isn't specific to
updating, it should go in `validateForSave`.

---

### validateValueForKey

`public abstract Object validateValueForKey(
Object value,
String key)`

Confirms that _value_ is
legal for the receiver's property named by _key._ Throws
an [EOValidation.Exception](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOValidationException.html#BAABJIHH) if it can't
confirm that the value is legal. The implementation can provide
a coerced value by returning the value_._
This lets you convert strings to dates or numbers or maybe convert
strings to an enumerated type value. EOCustomObject's implementation
sends a [validateValueForKey](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxmylmnfsgc5dfkzqwy5lfizxxes3fpe) message
to the receiver's EOClassDescription.

Enterprise objects can implement individual `validate` _Key_  methods
to check limits, test for nonsense values, and otherwise confirm
individual properties. To validate multiple properties based on
relations among them, override the appropriate `validateFor...` method.

__See Also:__
`EOValidation.` [Exception](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOValidationException.html#//apple_ref/java/instm/EOValidation.Exception/Exception) constructor

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
