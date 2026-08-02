---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOValidation.html
archived_at: '2026-07-15T08:11:43.589114Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOValidation

> __(informal protocol)__

> __Declared in:__ : EOControl/EOClassDescription.h

---

## Protocol Description

---

The EOValidation informal protocol defines the way that enterprise
objects validate their values. The validation methods check for
illegal value types, values outside of established limits, illegal relationships,
and so on. The Framework additions to NSObject provide default implementations
of EOValidation, which are described in detail in this specification.

There are two kinds of validation methods. The first validates
individual properties, and the second validates an entire object
to see if it's ready for a specific operation (inserting, updating,
and deleting). The two different types are discussed in more detail
in the sections ["Validating Individual Properties"](EOValidation-4.md#apple-infemrccizeec) and ["Validating Before an Operation"](EOValidation-4.md#apple-infemrkbifbuu).

## Instance Methods

---

### validateForDelete

`- (NSException *)validateForDelete`

Confirms that the receiver can be deleted in
its current state, returning `nil` if
it can or an NSException that the sender may raise if it can't.
For example, an object can't be deleted if it has a relationship
with a delete rule of [EODeleteRuleDeny](EOClassDescription-3.md#apple-ijaucrchivdeo) and that relationship
has a destination object.

NSObject's implementation sends the receiver's EOClassDescription
a message (which performs basic checking based on the presence or
absence of values). Subclasses should invoke __super__'s
implementation before performing their own validation, and should
combine any exception returned by __super__'s implementation
with their own:

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

__See Also:__
[- propagateDeleteWithEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5yhe33qmftwc5dfirswyzlumvlws5diivsgs5djnztug33oorsxq5b2) (EOEnterpriseObject), [+ validationExceptionWithFormat:](NSException%20Additions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjzjuk6ddmvyhi2lpnyqeczdenf2gs33oomxxmylmnfsgc5djn5xek6ddmvyhi2lpnzlws5diizxxe3lboq5a) (NSException
Additions)

---

### validateForInsert

`- (NSException *)validateForInsert`

Confirms that the receiver can be inserted in
its current state, returning `nil` if
it can or an NSException that the sender may raise if it can't. NSObject's
implementation simply invokes [validateForSave](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojjwc5tf).

The method __validateForSave__ is the
generic validation method for when an object is written to the external
store. If an object performs validation that isn't specific to
insertion, it should go in __validateForSave__.

---

### validateForSave

`- (NSException *)validateForSave`

Confirms that the receiver can be saved in its
current state, returning `nil` if
it can or an NSException that the sender may raise if it can't. NSObject's
implementation sends the receiver's EOClassDescription a [validateObjectForSave:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of53gc3djmrqxizkpmjvgky3uizxxeu3bozstu) message,
then iterates through all of the receiver's properties, invoking [validateValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkvtbnr2wkotgn5zewzlzhi) for
each one. If this results in more than one exception, the exception
returned contains the additional ones in its __userInfo__ dictionary
under the AdditionalExceptionsKey. Subclasses
should invoke __super__'s implementation
before performing their own validation, and should combine any exception returned by __super__'s
implementation with their own:
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

Enterprise objects can implement this method to check that
certain relations between properties hold; for example, that the
end date of a vacation period follows the begin date. To validate
an individual property, you can simply implement a method for it
as described under __validateValue:forKey:__.

__See Also:__
[+ validationExceptionWithFormat:](NSException%20Additions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjzjuk6ddmvyhi2lpnyqeczdenf2gs33oomxxmylmnfsgc5djn5xek6ddmvyhi2lpnzlws5diizxxe3lboq5a) (NSException
Additions), [+ aggregateExceptionWithExceptions:](NSException%20Additions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjzjuk6ddmvyhi2lpnyqeczdenf2gs33oomxwcz3hojswoylumvcxqy3fob2gs33ok5uxi2cfpbrwk4dunfxw44z2) (NSException
Additions)

---

### validateForUpdate

`- (NSException *)validateForUpdate`

Confirms that the receiver can be inserted in
its current state, EOreturning `nil` if
it can or an NSException that the sender may raise if it can't NSObject's
implementation simply invokes [validateForSave](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojjwc5tf).

The method __validateForSave__ is the
generic validation method for when an object is written to the external
store. If an object performs validation that isn't specific to
updating, it should go in __validateForSave__.

---

### validateValue:forKey:

`- (NSException *)validateValue:(id
*)valuePointer
forKey:(NSString *)key`

Confirms that the
value referenced by _valuePointer_ is
legal for the receiver's property named by _key_. Returns `nil` if
it can confirm that the value is legal or an NSException that the
sender may raise if it can't. The implementation can provide a
coerced value by putting the new value into `*`_valuePointer_.
This lets you convert strings to dates or numbers or maybe convert
strings to an enumerated type value. NSObject's implementation
sends a [validateValue:forKey:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of53gc3djmrqxizkwmfwhkzj2mzxxes3fpe5a) message
to the receiver's EOClassDescription. If that message doesn't
return an exception, it checks for a method of the form __validateKey:__ (for
example, __validateBudget:__ for a key of "budget")
and invokes it, returning the result.

Enterprise objects can implement individual __validate___Key___:__ methods
to check limits, test for nonsense values, and otherwise confirm
individual properties. To validate multiple properties based on
relations among them, override the appropriate __validateFor...__ method.

__See Also:__
[+ validationExceptionWithFormat:](NSException%20Additions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjzjuk6ddmvyhi2lpnyqeczdenf2gs33oomxxmylmnfsgc5djn5xek6ddmvyhi2lpnzlws5diizxxe3lboq5a) (NSException
Additions)

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
