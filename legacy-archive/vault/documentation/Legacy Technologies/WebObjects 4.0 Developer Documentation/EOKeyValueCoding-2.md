---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/More/EOKeyValueCoding_m.html
archived_at: '2026-07-18T01:28:33.685727Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOKeyValueCoding.md)
[!](EOKeyValueCodingAdditions.md)

---

# EOKeyValueCoding

---

### Stored Value Methods

The stored value methods, [__storedValueForKey__](EOKeyValueCoding.md)and [__takeStoredValueForKey__](EOKeyValueCoding.md), are used by the framework to store and restore an enterprise object's properties, either from the database or from an in-memory snapshot. This access is considered private to the enterprise object and is invoked by the framework to effect persistence on the object's behalf.

On the other hand, the basic key-value coding methods, [__valueForKey__](EOKeyValueCoding.md)and [__takeValueForKey__](EOKeyValueCoding.md), are the public API to an enterprise object. They are invoked by clients external to the object, such as for interactions with the user interface or with other enterprise objects.

All of the key-value coding methods access an object's properties by invoking property-specific accessor methods or by directly accessing instance variables. The basic methods resolve the specified property key as follows:

- Search for a public accessor method based on the specified key, invoking it if there is one. For example, with a key of "lastName", [__takeValueForKey__](EOKeyValueCoding.md)looks for a method named __set__ _Key___:__ , and [__valueForKey__](EOKeyValueCoding.md)looks for a method named `getLastName` or `lastName`.
- If a public accessor method isn't found the basic methods search for a private accessor method based on the key. For example, with a key of "lastName", [__takeValueForKey__](EOKeyValueCoding.md)looks for a method named ___set__ _Key___:__ , and [__valueForKey__](EOKeyValueCoding.md)looks for a method named `_getLastName` or `_lastName`.
- If an accesor method isn't found, the basic methods search for an instance variable based on the key and set the value directly. For the key "lastName", this would be ___lastName__ or __lastName__ .

The stored value methods use a different search order for resolving the property key: they search for a private accessor first, then for an instance variable, and finally for a public accessor. Enterprise object classes can take advantage of this distinction to simply set or get values when properties are accessed through the private API (on behalf of a trusted source) and to perform additional processing when properties are accessed through the public API. Put another way, the stored value methods allow you bypass the logic in your public accessor methods, whereas the basic key-value coding methods execute that logic.

The stored value methods are especially useful in cases where property values are interdependent. For example, suppose you need to update a total whenever an object's __bonus__ property is set:

> ```
> void setBonus(double newBonus) {
>     willChange();
>     _total += (newBonus - _bonus);
>     _bonus = newBonus;
> }
> ```

This total-updating code should be activated when the object is updated with values provided by a user (through the user interface), but not when the __bonus__ property is restored from the database. Since the Framework restores the property using [__takeStoredValueForKey__](EOKeyValueCoding.md)and since this method accesses the ___bonus__ instance variable in preference to calling the public accessor, the unnecessary (and possibly harmful) recomputation of ___total__ is avoided. If the object actually wants to intervene when a property is set from the database, it has two options:

- Implement ___setBonus.__
- Replace the Framework's default stored value search order with the same search order used by the basic methods by overriding the static method [__useStoredAccessor__](EOCustomObject.md)to return __false__ .

---

### Type Checking and Type Conversion

The default implementations of the key-value coding methods accept any object as a value, and do no type checking or type conversion among object classes. It's possible, for example, to pass a String to __[takeValueForKey](EOKeyValueCoding.md)__ as the value for a property the receiver expects to be an NSDate. The sender of a key-value coding message is thus responsible for ensuring that a value is of the proper class, typically by using the [__validateValueForKey__](EOValidation.md)method to coerce it to the proper type. The interface layer's EODisplayGroup uses this on all values received from interface user objects, for example, as well as relying on number and date formatters to interpret string values typed by the user. For more information on the [__validateValueForKey__](EOValidation.md)method, see the [EOValidation](EOValidation.md) interface specification.

The key-value coding methods handle one special case with regard to value types. For enterprise objects that access numeric values as scalar types, these methods automatically convert between the scalar types and java.lang.Number objects. For example, suppose your enterprise object defines these accessor methods:

public void setSalary(int _salary_)

public int salary()

For the __setSalary__ method, __[takeValueForKey](EOKeyValueCoding.md)__ converts the object value it receives as the argument for the "salary" key to an __int__ and passes it as _salary_ to __setSalary__ . Similarly, __[valueForKey](EOKeyValueCoding.md)__ converts the return value of the __salary__ method to a java.lang.Number and returns that.

The default implementations of the key-value coding methods support the scalar types __int__ , __float__ , and __double__ . Object values are converted to these types with the standard messages __intValue__ , __floatValue__ , and so on. Note that the key-value coding methods don't check that an object value actually responds to these messages; this can result in a run-time error if the object doesn't respond to the appropriate message.

One type of conversion these methods can't perform is that from __null__ to a scalar value. Scalar values define no equivalent of a database system's NULL value, so these must be handled by the object itself. Upon encountering __null__ while setting a scalar value, __[takeValueForKey](EOKeyValueCoding.md)__ invokes [__unableToSetNullForKey__](EOKeyValueCoding.md), which by default simply throws an exception. Enterprise object classes that use scalar values which may be NULL in the database should override this method to substitute the appropriate scalar value for __null__ , reinvoking __[takeValueForKey](EOKeyValueCoding.md)__ to set the substitute value.

---

[!](EOKeyValueCoding.md)
[!](EOKeyValueCodingAdditions.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
