---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSKVCAdd.html
archived_at: '2026-07-15T08:13:56.835075Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCodingAdditions

> **__Implements:__**
> : NSKeyValueCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Interface Description

---

The NSKeyValueCodingAdditions interface defines an extension to the basic NSKeyValueCoding interface. The pair of methods in NSKeyValueCodingAdditions- [takeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3umfvwkvtbnr2wkrtpojfwk6kqmf2gq) and [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3wmfwhkzkgn5zewzlzkbqxi2a)-give access to properties across relationships with __key paths__ of the form _relationship.property_; for example, "department.name". For more information on the basic key-value coding, see the [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) interface specification.

The NSKeyValueCodingAdditions interface contains two inner classes, [NSKeyValueCodingAdditions. DefaultImplementation](NSKeyValueCodingAdditions.DefaultImplementation.md#apple-iraumrkki5cui) and [NSKeyValueCodingAdditions.Utility](NSKeyValueCodingAdditions.Utility.md#apple-inbecqski5buu). The former provides a default implementation of the interface, making it easy to implement on your own custom classes. The latter is a convenience that allows you to access the properties of [NSKeyValueCodingAdditions](#apple-inbemssiinbek) objects and non-__NSKeyValueCodingAdditions__ objects using the same code.

## Default Implementation

The methods in the [NSKeyValueCodingAdditions. DefaultImplementation](NSKeyValueCodingAdditions.DefaultImplementation.md#apple-iraumrkki5cui) class are just like the methods defined by the NSKeyValueCodingAdditions interface, except they are static methods and they take an extra argument-the object on which the default implementation should operate.

For example, suppose you want to implement an Employee class that implements NSKeyValueCodingAdditions using NSKeyValueCodingAdditions. DefaultImplementation. Employee's [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3wmfwhkzkgn5zewzlzkbqxi2a) method would then look like this:

> ```
> public Object valueForKeyPath(String keyPath) {
>     return NSKeyValueCodingAdditions.DefaultImplementation.valueForKeyPath(
>         this,
>         keyPath);
> }
> ```

## Utility

Recall that the [NSKeyValueCodingAdditions.Utility](NSKeyValueCodingAdditions.Utility.md#apple-inbecqski5buu) class is a convenience that allows you to access the properties of __NSKeyValueCodingAdditions__ objects and non-NSKeyValueCodingAdditions objects using the same code.

Utility's methods are similar to DefaultImplementation's methods in that they are static methods and they take an extra argument-the object on which the method should operate. However, Utility's methods simply check to see if the object on which they operate is an NSKeyValueCodingAdditions object and invoke the corresponding NSKeyValueCodingAdditions method on the object if it is. Otherwise, they invoke the corresponding DefaultImplementation method, passing the object on which to operate.

For example, suppose that you want to access an object with the NSKeyValueCodingAdditions API but you don't know if the object is an NSKeyValueCodingAdditions object. To do so, you simply use the corresponding Utility API, as in the following line of code:

> ```
> theValue = NSKeyValueCodingAdditions.Utility.valueForKeyPath(object, keyPath);
> ```

The above line of code is essentially a short-cut for the following:

> ```
> if (object instanceof NSKeyValueCodingAdditions) {
>     theValue = ((NSKeyValueCodingAdditions)object).valueForKeyPath(keyPath);
> } else {
>     theValue = NSKeyValueCodingAdditions.DefaultImplementation.valueForKeyPath(
>             object, keyPath);
> }
> ```

## Constants

---

NSKeyValueCodingAdditions defines the following constant:

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| KeyPathSeparator | String | The string used to separate components of a key path-a period (.). |

## Instance Methods

---

### takeValueForKeyPath

`public void takeValueForKeyPath( Object value, String keyPath)`

Sets the value for the property identified by _keyPath_ to _value_. A key path has the form _relationship.property_ (with one or more relationships); for example "movieRole.roleName" or "movieRole.talent.lastName". The default implementation of this method (provided by [NSKeyValueCodingAdditions. DefaultImplementation](NSKeyValueCodingAdditions.DefaultImplementation.md#apple-iraumrkki5cui)) gets the destination object for each relationship using [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe), and sends the final object a [takeValueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) message with _value_ and _property_.

---

### valueForKeyPath

`public Object valueForKeyPath(String keyPath)`

Returns the value for the derived property identified by _keyPath_. A key path has the form _relationship.property_ (with one or more relationships); for example "movieRole.roleName" or "movieRole.talent.lastName". The default implementation of this method (provided by [NSKeyValueCodingAdditions. DefaultImplementation](NSKeyValueCodingAdditions.DefaultImplementation.md#apple-iraumrkki5cui)) gets the destination object for each relationship using [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe), and returns the result of a __valueForKey__ message to the final object.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
