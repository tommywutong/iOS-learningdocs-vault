---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSKVC.html
archived_at: '2026-07-15T08:13:56.815032Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Interface Description

---

The NSKeyValueCoding interface defines a data transport mechanism in which the properties of an object are accessed indirectly by name (or _key_), rather than directly through invocation of an accessor method or as instance variables. Thus, all of an object's properties can be accessed in a consistent manner. The [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) method sets the value for an object's property, and [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) returns the value for an object's property.

The NSKeyValueCoding interface contains an inner interface, NSKeyValueCoding.ErrorHandling, that defines an extension to the basic NSKeyValueCoding interface for handling errors that occur during key-value coding (see the [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo) interface specification).

Additionally, NSKeyValueCoding contains two inner classes, [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui) and [NSKeyValueCoding.Utility](NSKeyValueCoding.Utility.md#apple-iraugrsjifeec). The former provides a default implementation of the interface, making it easy to implement NSKeyValueCoding on your own custom classes. The latter is a convenience that allows you to access the properties of NSKeyValueCoding objects and non-NSKeyValueCoding objects using the same code. Both the DefaultImplementation class and the Utility class provide NSKeyValueCoding.ErrorHandling API in addition to basic NSKeyValueCoding API.

## Default Implementation

The methods in the [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui) class are just like the methods defined by the NSKeyValueCoding interface (and the NSKeyValueCoding.ErrorHandling interface), except they are static methods and they take an extra argument-the object on which the default implementation should operate.

For example, suppose you want to implement an Employee class that implements NSKeyValueCoding using NSKeyValueCoding. DefaultImplementation. Employee's [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) method would then look like this:

> ```
> public Object valueForKey(String key) {
>     return NSKeyValueCoding.DefaultImplementation.valueForKey(this, key);
> }
> ```

The NSKeyValueCoding. DefaultImplementation methods use accessor methods normally implemented by objects (such as `set`_Key_ and _key_), or they access instance variables directly if no accessors for a key exist (see ["Directly Accessing Instance Variables"](#apple-ineucqsdijfes)). For detailed information, see the [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) and [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) method descriptions, which describe the default behavior provided by NSKeyValueCoding. DefaultImplementation. Additionally, see the method descriptions in the NSKeyValueCoding.ErrorHandling interface specification to see how the DefaultImplementation class handles errors.

|  |
| --- |
| __Note:__ Always use the default implementation of NSKeyValueCoding provided by the foundation package. The default implementations have significant performance optimizations. To benefit from them, implement NSKeyValueCoding on a custom class as shown above by using the methods in NSKeyValueCoding. DefaultImplementation; or if your class inherits from an WebObjects class that implements NSKeyValueCoding, don't override the inherited implementation. Using a custom implementation incurs significant performance penalties. |

## Utility

Recall that the [NSKeyValueCoding.Utility](NSKeyValueCoding.Utility.md#apple-iraugrsjifeec) class is a convenience that allows you to access the properties of NSKeyValueCoding objects and non-NSKeyValueCoding objects using the same code.

Utility's methods are similar to DefaultImplementation's methods in that they are static methods and they take an extra argument-the object on which the method should operate. However, Utility's methods simply check to see if the object on which they operate is an NSKeyValueCoding object and invoke the corresponding NSKeyValueCoding method on the object if it is. Otherwise, they invoke the corresponding DefaultImplementation method, passing the object on which to operate.

For example, suppose that you want to access an object with the NSKeyValueCoding API but you don't know if the object is an NSKeyValueCoding object. To do so, you simply use the corresponding Utility API, as in the following line of code:

> ```
> theValue = NSKeyValueCoding.Utility.valueForKey(object, value, key);
> ```

The above line of code is simply a short-cut for the following:

> ```
> if (object instanceof NSKeyValueCoding) {
>     theValue = ((NSKeyValueCoding)object).valueForKey(key);
> } else {
>     theValue = NSKeyValueCoding.DefaultImplementation.valueForKey(object, key);
> }
> ```

## Directly Accessing Instance Variables

By default, key-value coding methods directly access instance variables if there are no accessor methods for setting and retrieving values. However, you can modify this behavior without overriding the default implementation. To instruct the default implementation not to directly access instance variables, implement the static method [canAccessFieldsDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSKVC.html#//apple_ref/java/intfm/NSKeyValueCoding/canAccessFieldsDirectly) on your NSKeyValueCoding class to return `false`.

## Constants

---

[NSKeyValueCoding](#apple-ineucscjjjeeu) defines the following constant:

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| NullValue | [NSKeyValueCoding.Null](NSKeyValueCoding.Null.md#apple-ijceqrsgivduc) | A shared instance of [NSKeyValueCoding.Null](NSKeyValueCoding.Null.md#apple-ijceqrsgivduc). |

## Static Methods

---

### canAccessFieldsDirectly

`public static boolean canAccessFieldsDirectly()`

Returns `true` if the key-value coding methods can access the corresponding field value directly on finding no accessor method for a property. Returns `false` if they shouldn't.

An NSKeyValueCoding class doesn't have to implement this method. It's an optional method that allows a class to tailor key-value coding behavior. By default, the key-value implementation provided by [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui) accesses fields directly if it can't find corresponding accessor methods. An NSKeyValueCoding class can override this behavior by implementing this method to return `false`, in which case the key-value coding methods don't access fields directly.

This method isn't strictly part of this interface because static methods can't be formally declared in an interface. However, this method is so closely related to the interface as to be considered part of it.

---

## Instance Methods

---

### takeValueForKey

`public void takeValueForKey( Object value, String key)`

Sets the receiver's value for the property identified by _key_ to _value_.

The default implementation provided by [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui) works as follows:

1. Searches for a public accessor method of the form `set`_Key_, and invokes it if there is one.
2. If a public accessor method isn't found, searches for a private accessor method of the form ___set___Key_, and invokes it if there is one.
3. If an accessor method isn't found and the static method [canAccessFieldsDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSKVC.html#//apple_ref/java/intfm/NSKeyValueCoding/canAccessFieldsDirectly) returns `true`, searches for an instance variable based on _key_ and sets its value directly. For the key "lastName", this would be ___lastName__ or __lastName__. (See ["Directly Accessing Instance Variables"](#apple-ineucqsdijfes).)
4. If neither an accessor method nor an instance variable is found, it's an error condition. It invokes [handleTakeValueForUnboundKey](NSKeyValueCoding.ErrorHandling.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzoivzhe33sjbqw4zdmnfxgol3imfxgi3dfkrqwwzkwmfwhkzkgn5zfk3tcn52w4zclmv4q) if the object implements [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo) or throws [NSKeyValueCoding. UnknownKeyException](NSKeyValueCoding.UnknownKeyException.md#apple-incemscfineeq) if the object doesn't.

|  |
| --- |
| __Note:__ Always use the default implementation of NSKeyValueCoding provided by the foundation package. The default implementations have significant performance optimizations. To benefit from them, implement NSKeyValueCoding on a custom class as shown above by using the methods in NSKeyValueCoding. DefaultImplementation; or if your class inherits from an WebObjects class that implements NSKeyValueCoding, don't override the inherited implementation. Using a custom implementation incurs significant performance penalties. |

---

### valueForKey

`public Object valueForKey(String key)`

Returns the receiver's value for the property identified by _key_.

The default implementation provided by [NSKeyValueCoding. DefaultImplementation](NSKeyValueCoding.DefaultImplementation.md#apple-iraumrkki5cui) works as follows:

1. Searches for a public accessor method based on _key_. For example, with a key of "lastName", the method looks for a method named __getLastName__ or __lastName__.
2. If a public accessor method isn't found, searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", the method looks for a method named ___getLastName__ or ___lastName__.
3. If an accessor method isn't found and the static method [canAccessFieldsDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSKVC.html#//apple_ref/java/intfm/NSKeyValueCoding/canAccessFieldsDirectly) returns `true`, the method searches for an instance variable based on _key_ and returns its value directly. For the key "lastName", this would be ___lastName__ or __lastName__. (See ["Directly Accessing Instance Variables"](#apple-ineucqsdijfes).)
4. If neither an accessor method nor an instance variable is found, the method invokes [handleQueryWithUnboundKey](NSKeyValueCoding.ErrorHandling.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzoivzhe33sjbqw4zdmnfxgol3imfxgi3dfkf2wk4tzk5uxi2cvnzrg65lomrfwk6i) (defined in [NSKeyValueCoding.ErrorHandling](NSKeyValueCoding.ErrorHandling.md#apple-irauur2hjbcuo)).

|  |
| --- |
| __Note:__ Always use the default implementation of NSKeyValueCoding provided by the foundation package. The default implementations have significant performance optimizations. To benefit from them, implement NSKeyValueCoding on a custom class as shown above by using the methods in NSKeyValueCoding. DefaultImplementation; or if your class inherits from an WebObjects class that implements NSKeyValueCoding, don't override the inherited implementation. Using a custom implementation incurs significant performance penalties. |

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
