---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/More/EOValidation.html
archived_at: '2026-07-15T08:11:43.633948Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)

# EOValidation

## Validating Individual Properties

The most general method for validating individual properties, [validateValue:forKey:](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkvtbnr2wkotgn5zewzlzhi), validates
a property indirectly by name (or key). This method is responsible
for two things: coercing the value into an appropriate type for
the object, and validating it according to the object's rules.
The default implementation provided by NSObject consults the object's
EOClassDescription (using the EOEnterpriseObject informal protocol method [classDescription](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyyltoncgk43dojuxa5djn5xa)) to coerce the value
and to check for basic errors, such as a __null__ value
when that isn't allowed. If no basic errors exist, this default implementation
then validates the value according to the object itself. It searches
for a method of the form __validate___Key_: and
invokes it if it exists. These are the methods that your custom
classes can implement to validate individual properties, such as `validateAge`: to
check that the value the user entered is within acceptable limits. The `validateAge:` method
should return `nil`, indicating
the value is acceptable, or an NSException created by calling the
NSException method [validationExceptionWithFormat:](NSException%20Additions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjzjuk6ddmvyhi2lpnyqeczdenf2gs33oomxxmylmnfsgc5djn5xek6ddmvyhi2lpnzlws5diizxxe3lboq5a).

Coercion is performed automatically for you (by the EOClassDescription),
so all you need handle is validation itself. Since you can implement
custom validation logic in the __validate___Key_: methods,
you rarely need to override the EOValidation method [validateValue:forKey:](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkvtbnr2wkotgn5zewzlzhi). Rather, the
default implementation provided by NSObject is generally sufficient.

As an example of how validating a single property works, suppose
that Member objects have an __age__ attribute
stored as an integer. This attribute has a lower limit of 16, defined
by the Member class. Now, suppose a user types "12" into a text
field for the age of a member. The value comes into the Framework as
a string. When __validateValue:forKey:__ is
invoked to validate the new value, the method uses its EOClassDescription
to convert the string "12" into an NSNumber, then invokes __validateAge:__ with
that NSNumber. The __validateAge:__ method
compares the age to its limit of 16 and returns an exception to indicate
that the new value is not acceptable.

> ```
> - (NSException *)validateAge:(NSNumber *)age
> {
>     if ([age intValue] < 16) {
>         return [NSException
>             validationExceptionWithFormat:@"Age of %@ is below minimum.", age];
>     }
>     return nil;
> }
> ```

The method [validationExceptionWithFormat:](NSException%20Additions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpjzjuk6ddmvyhi2lpnyqeczdenf2gs33oomxxmylmnfsgc5djn5xek6ddmvyhi2lpnzlws5diizxxe3lboq5a) used
in the above example is a method that the Framework adds to NSException
for convenient creation of validation exceptions.

## When Properties are Validated

The Framework validates all of an object's properties before
the object is saved to an external source-either inserted or updated.
Additionally, you can design your application so that changes to
a property's value are validated immediately, as soon as a user
attempts to leave an editable field in the user interface (in Java
Client and Application Kit applications only). Whenever an EODisplayGroup sets
a value in an object, it sends the object a __validateValue:forKey:__ message,
allowing the object to coerce the value's type, perform any additional
validation, and return an exception if the value isn't valid. By
default, the display group leaves validation errors to be handled
when the object is saved, using __validateValue:forKey:__ only
for type coercion. However, you can use the EODisplayGroup method __setValidatesChangesImmediately:__ with
an argument of YES to tell the display group to immediately present
an attention panel whenever a validation error is encountered.

## Validating Before an Operation

The remaining EOValidation methods- [validateForInsert](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojew443foj2a), [validateForUpdate](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojkxazdborsq), [validateForSave](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojjwc5tf), and [validateForDelete](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojcgk3dforsq)-validate an entire
object to see if it's valid for a particular operation. These methods
are invoked automatically by the Framework when the associated operation
is initiated. NSObject provides default implementations, so you
only have to implement them yourself when special validation logic
is required. For example, you can override these methods in your
custom enterprise object classes to allow or refuse the operation
based on property values. For example, a Fee object might refuse
to be deleted if it hasn't been paid yet. Or you can override
these methods to perform delayed validation of properties or to
compare multiple properties against one another; for example, you
might verify that a pair of dates is in the proper temporal order.

> ```
> - (NSException *)validateForSave
> {
>     NSException *exception = [super validateForSave];
>     NSException *myException = nil;
>
>     if ([startDate compare:endDate] == NSOrderedDescending) {
>         myException = [NSException
>             validationExceptionWithFormat:@"Start date must precede end date."];
>     }
>     if (exception && myException) {
>         exception = [NSException aggregateExceptionWithExceptions:
>             [NSArray arrayWithObjects:exception, myException, nil]];
>     } else if (myException) {
>         exception = myException;
>     }
>     return exception;
> }
> ```

Note that this method also invokes __super__'s
implementation. This is important, as the default implementations
of the __validateFor...__ methods pass the
check on to the object's EOClassDescription, which performs basic
checking among properties, including invoking [validateValue:forKey:](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkvtbnr2wkotgn5zewzlzhi) for each property.
The access layer's EOEntityClassDescription class verifies constraints
based on an EOModel, such as delete rules. For example, the delete
rule for a Department object might state that it can't be deleted
if it still contains Employee objects.

The method __validateForSave__ is the
generic validation method for when an object is written to the external
store. The default implementations of __validateForInsert__, [validateForUpdate](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojkxazdborsq) both invoke it.
If an object performs validation that isn't specific to insertion
or to updating, it should go in __validateForSave__.

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
