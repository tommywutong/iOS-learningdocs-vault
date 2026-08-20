---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/More/EOKeyValueCoding.html
archived_at: '2026-07-15T08:11:39.091276Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)

# EOKeyValueCoding

## Stored Value Methods

The stored value methods, [storedValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpon2g64tfmrlgc3dvmvdg64slmv4q) and [takeStoredValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe), are used by
the framework to store and restore an enterprise object's properties,
either from the database or from an in-memory snapshot. This access
is considered private to the enterprise object and is invoked by
the framework to effect persistence on the object's behalf.

On the other hand, the basic key-value coding methods, [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe)and [takeValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz), are the public API
to an enterprise object. They are invoked by clients external to
the object, such as for interactions with the user interface or
with other enterprise objects.

All of the key-value coding methods access an object's properties
by invoking property-specific accessor methods or by directly accessing
instance variables. The basic methods resolve the specified property
key as follows:

1. Search for a public accessor method based on
   the specified key, invoking it if there is one. For example, with
   a key of "lastName", `takeValueForKey` looks
   for a method named `set` _Key_ `:`,
   and `valueForKey`looks
   for a method named getLastName or lastName.
2. If a public accessor method isn't found and useStoredAccessor returns true,
   the basic methods search for a private accessor method based on
   the key. For example, with a key of "lastName", `takeValueForKey` looks
   for a method named `_set` _Key_ `:`,
   and `valueForKey`looks
   for a method named _getLastName or _lastName.
3. If an accessor method isn't found, the basic methods search
   for an instance variable based on the key and set the value directly.
   For the key "lastName", this would be `_lastName` or `lastName`.
   Note that `_lastName` is used only if useStoredAccessor returns true.

The stored value methods use a different search order for
resolving the property key: they search for a private accessor first,
then for an instance variable, and finally for a public accessor.
Enterprise object classes can take advantage of this distinction
to simply set or get values when properties are accessed through
the private API (on behalf of a trusted source) and to perform additional
processing when properties are accessed through the public API.
Put another way, the stored value methods allow you bypass the logic
in your public accessor methods, whereas the basic key-value coding
methods execute that logic.

The stored value methods are especially useful in cases where
property values are interdependent. For example, suppose you need
to update a total whenever an object's `bonus` property
is set:

> ```
> void setBonus(double newBonus) {
>     willChange();
>     _total += (newBonus - _bonus);
>     _bonus = newBonus;
> }
> ```

This total-updating code should be activated when the object
is updated with values provided by a user (through the user interface),
but not when the `bonus` property is restored
from the database. Since the Framework restores the property using [takeStoredValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe)and
since this method accesses the `_bonus` instance
variable in preference to calling the public accessor, the unnecessary
(and possibly harmful) recomputation of `_total` is
avoided. If the object actually wants to intervene when a property is
set from the database, it has two options:

- Implement `_setBonus.`
- Replace the Framework's default stored value search order
  with the same search order used by the basic methods by overriding
  the static method [useStoredAccessor](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf52xgzktorxxezleifrwgzltonxxe) to return false.

## Type Checking and Type Conversion

The default implementations of the key-value coding methods
accept any object as a value, and do no type checking or type conversion
among object classes. It's possible, for example, to pass a String to [takeValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) as the value for
a property the receiver expects to be an NSDate. The sender of a key-value
coding message is thus responsible for ensuring that a value is
of the proper class, typically by using the [validateValueForKey](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkwmfwhkzkgn5zewzlz) method to coerce
it to the proper type. The interface layer's EODisplayGroup uses
this on all values received from interface user objects, for example,
as well as relying on number and date formatters to interpret string
values typed by the user. For more information on the `validateValueForKey` method,
see the [EOValidation](EOValidation.md#apple-infemqsfifcui) interface specification.

The key-value coding methods handle one special case with
regard to value types. For enterprise objects that access numeric
values as scalar types, these methods automatically convert between
the scalar types and Number objects. For example, suppose your enterprise
object defines these accessor methods:

> ```
> public void setSalary(int salary)
> public int salary()
> ```

For the `setSalary` method, `takeValueForKey` converts
the object value it receives as the argument for the "salary"
key to an `int` and passes it as _salary_ to `setSalary`.
Similarly, [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) converts the return value
of the `salary` method to a Number and returns
that.

The default implementations of the key-value coding methods
support the scalar types `int`, `float`,
and `double`. Object values
are converted to these types with the standard messages `intValue`, `floatValue`, and
so on. Note that the key-value coding methods don't check that
an object value actually responds to these messages; this can result
in a run-time error if the object doesn't respond to the appropriate message.

One type of conversion these methods can't perform is that
from null to a scalar value. Scalar values define no equivalent
of a database system's NULL value, so these must be handled by
the object itself. Upon encountering null while setting a scalar
value, `takeValueForKey` invokes [unableToSetNullForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpovxgcytmmvkg6u3forhhk3dmizxxes3fpe), which by default
simply throws an exception. Enterprise object classes that use scalar
values which may be NULL in the database should override this method
to substitute the appropriate scalar value for null, reinvoking `takeValueForKey` to
set the substitute value.

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
