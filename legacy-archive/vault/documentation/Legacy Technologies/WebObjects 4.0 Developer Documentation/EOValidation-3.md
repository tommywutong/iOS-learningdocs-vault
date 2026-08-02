---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOValidation.html
archived_at: '2026-07-18T01:28:41.820474Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOSortOrderingComparison.md)
[!](EOValidation-4.md)

---

# EOValidation

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOClassDescription.h

__Inherits From:__
java.lang.Object

__Package:__
com.apple.client.eocontrol

## Protocol Description

The EOValidation informal protocol defines the way that enterprise objects validate their values. The validation methods check for illegal value types, values outside of established limits, illegal relationships, and so on. the Framework additions to NSObject provide default implementations of EOValidation, which are described in detail in this specification.

There are two kinds of validation methods. The first validates individual properties, and the second validates an entire object to see if it's ready for a specific operation (inserting, updating, and deleting). The two different types are discussed in more detail in the sections "[Validating Individual Properties](EOValidation-4.md)" and "[Validating Before an Operation](EOValidation-4.md)."

---

#### validateForDelete

- (NSException \*)__validateForDelete__

Confirms that the receiver can be deleted in its current state, returning __nil__ if it can or an NSException that the sender may raise if it can't. For example, an object can't be deleted if it has a relationship with a delete rule of [EODeleteRuleDeny](EOClassDescription-3.md) and that relationship has a destination object.

NSObject's implementation sends the receiver's EOClassDescription a message (which performs basic checking based on the presence or absence of values). Subclasses should invoke __super__ 's implementation before performing their own validation, and should combine any exception returned by __super__ 's implementation with their own:

> ```
> - (NSException *)validateForDelete
> {
>     NSException *exception = [super validateForDelete];
>
>     if ([balance intValue] != 0) {
>         NSException *validationExample = [NSException
>             validationExceptionWithFormat:@"The balance must be zero."];
>       if (!exception)
>          exception = validationException;
>       else
>          exception = [NSException aggregateExceptionWithExceptions:
>             [NSArray arrayWithObjects:exception, validationException, nil]];
>    }
>    return exception;
> }
> ```

__See also:__ [- __propagateDeleteWithEditingContext:__](EOEnterpriseObject-3.md)(EOEnterpriseObject), [+ __validationExceptionWithFormat:__](NSException%20Additions.md)(NSException Additions)

---

#### validateForInsert

- (NSException \*)__validateForInsert__

Confirms that the receiver can be inserted in its current state, returning __nil__ if it can or an NSException that the sender may raise if it can't. NSObject's implementation simply invokes __validateForSave__ .

The method __validateForSave__ is the generic validation method for when an object is written to the external store. If an object performs validation that isn't specific to insertion, it should go in __validateForSave__ .

---

#### validateForSave

- (NSException \*)__validateForSave__

Confirms that the receiver can be saved in its current state, returning __nil__ if it can or an NSException that the sender may raise if it can't. NSObject's implementation sends the receiver's EOClassDescription a [__validateObjectForSave:__](EOClassDescription-3.md)message, then iterates through all of the receiver's properties, invoking __validateValue:forKey:__ for each one. If this results in more than one exception, the exception returned contains the additional ones in its __userInfo__ dictionary under the EOAdditionalExceptions key. Subclasses should invoke __super__ 's implementation before performing their own validation, and should combine any exception returned by __super__ 's implementation with their own:

> ```
> - (NSException *)validateForSave
> {
>     NSException *exception = [super validateForDelete];
>
>     if ([balance intValue] != 0) {
>         NSException *validationExample = [NSException
>             validationExceptionWithFormat:@"The balance must be zero."];
>       if (!exception)
>          exception = validationException;
>       else
>          exception = [NSException aggregateExceptionWithExceptions:
>             [NSArray arrayWithObjects:exception, validationException, nil]];
>    }
>    return exception;
> }
> ```

Enterprise objects can implement this method to check that certain relations between properties hold; for example, that the end date of a vacation period follows the begin date. To validate an individual property, you can simply implement a method for it as described under __validateValue:forKey:__ .

__See also:__ [+ __validationExceptionWithFormat:__](NSException%20Additions.md)(NSException Additions), [+ __aggregateExceptionWithExceptions:__](NSException%20Additions.md)(NSException Additions)

---

#### validateForUpdate

- (NSException \*)__validateForUpdate__

Confirms that the receiver can be inserted in its current state, returning __nil__ if it can or an NSException that the sender may raise if it can't. NSObject's implementation simply invokes __validateForSave__ .

The method __validateForSave__ is the generic validation method for when an object is written to the external store. If an object performs validation that isn't specific to updating, it should go in __validateForSave__ .

---

#### validateValue:forKey:

- (NSException \*)__validateValue:__ (id \*)_valuePointer_ __forKey:__ (NSString \*)_key_

Confirms that the value referenced by _valuePointer_ is legal for the receiver's property named by _key_. Returns __nil__ if it can confirm that the value is legal or an NSException that the sender may raise if it can't. The implementation can provide a coerced value by putting the new value into __\*valuePointer__ . This lets you convert strings to dates or numbers or maybe convert strings to an enumerated type value. NSObject's implementation sends a [__validateValue:forKey:__](EOClassDescription-3.md)message to the receiver's EOClassDescription. If that message doesn't return an exception, it checks for a method of the form __validate__ _Key___:__ (for example, __validateBudget:__ for a _key_ of "budget") and invokes it, returning the result.

Enterprise objects can implement individual __validate__ _Key___:__ methods to check limits, test for nonsense values, and otherwise confirm individual properties. To validate multiple properties based on relations among them, override the appropriate __validateFor...__ method.

__See also:__ [+ __validationExceptionWithFormat:__](NSException%20Additions.md)(NSException Additions)

---

[!](EOSortOrderingComparison.md)
[!](EOValidation-4.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
