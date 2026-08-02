---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/More/EOKeyValueCoding.html
archived_at: '2026-07-15T08:11:43.618221Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)

# EOKeyValueCoding

## Stored Value Methods

The stored value methods, [storedValueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3torxxezlekzqwy5lfizxxes3fpe5a) and [takeStoredValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwku3un5zgkzcwmfwhkzj2mzxxes3fpe5a), are used
by the framework to store and restore an enterprise object's properties,
either from the database or from an in-memory snapshot. This access
is considered private to the enterprise object and is invoked by
the framework to effect persistence on the object's behalf.

On the other hand, the basic key-value coding methods, [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi)and [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi), are the public
API to an enterprise object. They are invoked by clients external
to the object, such as for interactions with the user interface
or with other enterprise objects.

All of the key-value coding methods access an object's properties
by invoking property-specific accessor methods or by directly accessing
instance variables. The basic methods resolve the specified property
key as follows:

1. Search for a public accessor method based on
   the specified key, invoking it if there is one. For example, with
   a key of "lastName", __takeValue:forKey:__ looks
   for a method named __set___Key___:__,
   and __valueForKey:__looks
   for a method named getLastName or lastName.
2. If a public accessor method isn't found and [useStoredAccessor](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/useStoredAccessor) returns YES,
   the basic methods search for a private accessor method based on
   the key. For example, with a key of "lastName", __takeValue:forKey:__ looks
   for a method named ___set___Key___:__,
   and __valueForKey:__looks
   for a method named _getLastName or _lastName.
3. If an accessor method isn't found, the basic methods search
   for an instance variable based on the key and set the value directly.
   For the key "lastName", this would be ___lastName__ or __lastName__.
   Note that ___lastName__ is used only if [useStoredAccessor](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/useStoredAccessor) returns YES.

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
to update a total whenever an object's __bonus__ property
is set:

> ```
> - (void)setBonus:(double)newBonus {
>     [self willChange];
>     _total += (newBonus - _bonus);
>     _bonus = newBonus;
> }
> ```

This total-updating code should be activated when the object
is updated with values provided by a user (through the user interface),
but not when the __bonus__ property is restored
from the database. Since the Framework restores the property using [takeStoredValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwku3un5zgkzcwmfwhkzj2mzxxes3fpe5a)and
since this method accesses the ___bonus__ instance
variable in preference to calling the public accessor, the unnecessary
(and possibly harmful) recomputation of ___total__ is
avoided. If the object actually wants to intervene when a property is
set from the database, it has two options:

- Implement ___setBonus:.__
- Replace the Framework's default stored value search order
  with the same search order used by the basic methods by overriding
  the class method [useStoredAccessor](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/useStoredAccessor) to
  return NO.

## Type Checking and Type Conversion

The default implementations of the key-value coding methods
accept any object as a value, and do no type checking or type conversion
among object classes. It's possible, for example, to pass an NSString to [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi) as the value for
a property the receiver expects to be an NSDate. The sender of a key-value
coding message is thus responsible for ensuring that a value is
of the proper class, typically by using the [validateValue:forKey:](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkvtbnr2wkotgn5zewzlzhi) method to coerce
it to the proper type. The interface layer's EODisplayGroup uses
this on all values received from interface user objects, for example,
as well as relying on number and date formatters to interpret string
values typed by the user. For more information on the __validateValue:forKey:__ method,
see the [EOValidation](EOValidation-3.md#apple-infemqsfifcui) informal
protocol specification.

The key-value coding methods handle one special case with
regard to value types. For enterprise objects that access numeric
values as C scalar types, these methods automatically convert between
the scalar types and NSNumber objects. For example, suppose your
enterprise object defines these accessor methods:

> ```
> - (void)setSalary:(unsigned int)salary
> - (unsigned int)salary
> ```

For the __setSalary:__ method, __takeValue:forKey:__ converts
the object value it receives as the argument for the "salary"
key to an __unsigned int__ and passes it as _salary_ to __setSalary:__.
Similarly, [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi) converts the return
value of the __salary__ method to an NSNumber and
returns that.

The default implementations of the key-value coding methods
support the following scalar types:

|  |  |
| --- | --- |
| `char` | `unsigned char` |
| `short` | `unsigned short` |
| `int` | `unsigned int` |
| `long` | `unsigned long` |
| `float` | `double` |

Object values are converted to these types with the standard
messages __charValue, intValue__, __floatValue__,
and so on. Note that the key-value coding methods don't check
that an object value actually responds to these messages; this can
result in a run-time error if the object doesn't respond to the appropriate
message.

One type of conversion these methods can't perform is that
from nil to a scalar value. C scalar values define no equivalent
of a database system's NULL value, so these must be handled by
the object itself. Upon encountering nil while setting a scalar
value, __takeValue:forKey:__ invokes [unableToSetNullForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3vnzqwe3dfkrxvgzlujz2wy3cgn5zewzlzhi), which by
default simply raises an exception. Enterprise object classes that
use scalar values which may be NULL in the database should override
this method to substitute the appropriate scalar value for nil,
reinvoking __takeValue:forKey:__ to set the
substitute value.

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
