---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSVal.html
archived_at: '2026-07-15T08:13:56.884804Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSValidation

> **__Package:__**
> : com.webobjects.foundation

---

## Interface Description

---

The NSValidation interface defines a validation mechanism in which the properties of an object are validated indirectly by name (or _key_), rather than directly through invocation of an specific validation method. Thus, all of an object's properties can be validated in a consistent manner. The [validateValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstkzqwy2lemf2gs33of53gc3djmrqxizkwmfwhkzkgn5zewzlz) method confirms that a value is legal for a particular property, and [validateTakeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstkzqwy2lemf2gs33of53gc3djmrqxizkumfvwkvtbnr2wkrtpojfwk6kqmf2gq) performs the validation and assigns the value if it's legal and different from the current value.

The NSValidation interface contains two inner classes, [NSValidation.DefaultImplementation](NSValidation.DefaultImplementation.md#apple-incukr2ejfeei) and [NSValidation.Utility](NSValidation.Utility.md#apple-iraugrcgjfbus). The former provides a default implementation of the interface, making it easy to implement on your own custom classes. The latter is a convenience that allows you to access the properties of NSValidation objects and non-NSValidation objects using the same code.

## Default Implementation

The methods in the [NSValidation.DefaultImplementation](NSValidation.DefaultImplementation.md#apple-incukr2ejfeei) class are just like the methods defined by the NSValidation interface, except they are static methods and they take an extra argument-the object on which the default implementation should operate.

For example, suppose you want to implement an Employee class that implements NSValidation using NSValidation.DefaultImplementation. Employee's [validateValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstkzqwy2lemf2gs33of53gc3djmrqxizkwmfwhkzkgn5zewzlz) method would then look like this:

> ```
> public Object validateValueForKey(Object value, String key) {
>     return NSValidation.DefaultImplementation.validateValueForKey(this, value, key);
> }
> ```

The NSValidation.DefaultImplementation methods search for property specific methods of the form __validate___Key_ and invoke them if they exist. Thus an NSValidation class should implement a validate method for each property that has associated validation logic. For example, a `validateAge` method could check that the value a user enters as an age is within acceptable limits and throw an [NSValidation.ValidationException](NSValidation.ValidationException.md#apple-ijeugssfjjdeg) if it finds an unacceptable value. For a more information on the __validate___Key_ methods, see ["Writing validateKey Methods" (page 375)](#apple-infemrccizeec).

Because you implement custom validation logic in the __validate___Key_ methods, you rarely need to implement the NSValidation methods from scratch. Rather, the default implementation provided by [NSValidation.DefaultImplementation](NSValidation.DefaultImplementation.md#apple-incukr2ejfeei) is generally sufficient.

|  |
| --- |
| __Note:__ Always use the default implementation of NSValidation provided by the foundation package. The default implementations have significant performance optimizations. To benefit from them, implement NSValidation on a custom class as shown above by using the methods in [NSValidation.DefaultImplementation](NSValidation.DefaultImplementation.md#apple-incukr2ejfeei); or if your class inherits from an WebObjects class that implements NSValidation, don't override the inherited implementation. Using a custom implementation incurs significant performance penalties. |

## Utility

Recall that the [NSValidation.Utility](NSValidation.Utility.md#apple-iraugrcgjfbus) class is a convenience that allows you to access the properties of NSValidation objects and non-NSValidation objects using the same code.

Utility's methods are similar to DefaultImplementation's methods in that they are static methods and they take an extra argument-the object on which the method should operate. However, Utility's methods simply check to see if the object on which they operate is an NSValidation object and invoke the corresponding NSValidation method on the object if it is. Otherwise, they invoke the corresponding DefaultImplementation method, passing the object on which to operate.

For example, suppose that you want to access an object with the NSValidation API but you don't know if the object is an NSValidation object. To do so, you simply use the corresponding Utility API, as in the following line of code:

> ```
> theValue = NSValidation.Utility.validateValueForKey(object, value, key);
> ```

The above line of code is simply a short-cut for the following:

> ```
> if (object instanceof NSValidation) {
>     theValue = ((NSValidation)object).validateValueForKey(key);
> } else {
>     theValue = validateValueForKey.DefaultImplementation.validateValueForKey(
>             object, value, key);
> }
> ```

## Writing validateKey Methods

To implement validation logic in an NSValidation class, you create a __validate___Key_ method for each property needing validation. The default implementations of NSValidation's methods look for these __validate___Key_ methods and use them to perform the actual validation.

A class's __validate___Key_ methods should have the following form:

> ```
> public Object validateKey(Object aValue) throws NSValidation.ValidationException
> ```

The implementation should confirm that the value passed in is legal and throw an [NSValidation.ValidationException](NSValidation.ValidationException.md#apple-ijeugssfjjdeg) if it's not. It should also __coerce__ the argument to the proper type, if necessary. Note that a __validate___Key_ method's argument type is Object, and not specifically the class of the corresponding property (String, Integer, or NSTimestamp, for example). Thus, a __validate___Key_ method needs to check the type of the argument and convert it to a different type if necessary. The return type of a __validate___Key_ method doesn't have to be Object. In fact, it's a good idea to specify the class of the value the method returns, which is generally the class of the corresponding property. The argument type, on the other hand, should generally be Object. For more information, see ["The validateKey Argument Type" (page 376)](#apple-infemskejfdue).

The following __validateAge__ method is an example that validates values for a property named `age` that's stored as an Integer. The method handles arguments of type String and Number. If the argument is an instance of any other class, the method throws a NSValidation.ValidationException.

> ```
> public Number validateAge(Object aValue) throws NSValidation.ValidationException {
>     Integer numberValue;
>     int age;
>
>     if (aValue instanceof String) {
>         // Convert the String to an Integer.
>         try {
>             numberValue = new Integer((String)aValue);
>         } catch (NumberFormatException numberFormatException) {
>         throw new NSValidation.ValidationException(
>             "Validation exception: Unable to convert the String " + aValue
>             + " to an Integer");
>         }
>     } else if (aValue instanceof Number) {
>         numberValue = new Integer(((Number)aValue).intValue());
>     } else {
>         throw new NSValidation.ValidationException
>             ("Validation exception: Unable to convert the Object " + aValue
>             + "to an Integer");
>     }
>
>     age = numberValue.intValue();
>     if (age < 16) {
>         throw new NSValidation.ValidationException
>             ("Age of " + age + " is below minimum.", this, "age");
>     }
>     return numberValue;
> }
> ```

The __validateAge__ method checks the argument's class. If the argument is a String or Number, it creates an Integer from the argument and validates it. If the Integer fails the validation test (if the value is less than 16), the method throws a [NSValidation.ValidationException](NSValidation.ValidationException.md#apple-ijeugssfjjdeg) inserting the NSValidation object and the key into the exception's userInfo dictionary by providing them to the constructor. On the other hand, if the Integer passes the validation test, the method returns the Integer.

The code that invokes the validation process is expected to use the value returned from the __validate___Key_ method instead of the original value it provided. Thus, a __validate___Key_ method has an opportunity to coerce a value into a type it prefers. As another example of coercion, a __validate___Key_ method can return `null`. A method might do this, for example, if it is invoked with the empty string as the argument.

## The validateKey Argument Type

The argument type of a __validate___Key_ method doesn't have to be specifically Object; it can be Object or any subclass. However, generally Object is the most appropriate type for a __validate___Key_ method's argument (the one exception is described later in this section). As explained in ["Writing validateKey Methods" (page 375)](#apple-infemrccizeec), a __validate___Key_ method should be able to handle any reasonable argument type. You _can_ type the argument to the common superclass of all reasonable arguments, but this is frequently Object.

You should not overload a __validate___Key_ method for a particular property, creating different __validate___Key_ methods for each argument type. Instead you should create one version of the validateKey method for the property that takes Object as its argument (or at least a superclass of all the possible argument types). The method's implementation should test the argument's type and coerce it appropriately.

There's one situation in which the argument type should be more specific than Object. If the property corresponding to the __validate___Key_ method is a to-one relationship to an enterprise object, the argument's type should be EOEnterpriseObject.

## Instance Methods

---

### validateTakeValueForKeyPath

`public Object validateTakeValueForKeyPath( Object value, String keyPath) throws NSValidation.ValidationException`

Confirms that _value_ is legal for the receiver's property named by _keyPath_, and assigns the value to the property if it's legal (and if _value_ is different from the current value), or throws an [NSValidation.ValidationException](NSValidation.ValidationException.md#apple-ijeugssfjjdeg) if _value_ isn't legal. A key path has the form _relationship.property_ (with one or more relationships); for example "movieRole.roleName" or "movieRole.talent.lastName".

The default implementation of this method (provided by [NSValidation.DefaultImplementation](NSValidation.DefaultImplementation.md#apple-incukr2ejfeei)) gets the destination object for each relationship using [valueForKey](NSKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe), and sends the final object a __validateValueForKey__ message with _value_ and _property_.

---

### validateValueForKey

`public Object validateValueForKey( Object value, String key) throws NSValidation.ValidationException`

Confirms that _value_ is legal for the receiver's property named by _key_, and returns the validated value if it's legal, or throws an [NSValidation.ValidationException](NSValidation.ValidationException.md#apple-ijeugssfjjdeg) if it isn't. Note that the value returned from this method can be different than the one passed as an argument.

The default implementation of this method (provided by [NSValidation.DefaultImplementation](NSValidation.DefaultImplementation.md#apple-incukr2ejfeei)) checks for a method of the form __validate___Key_ (for example, __validateBudget__ for a key of "budget"). If such a method exists, it invokes it and returns the result. Thus, NSValidation objects can implement individual __validate___Key_ methods to check limits, test for nonsense values, and coerce values (convert strings to dates or numbers, for example). For more information on __validate___Key_ methods, see ["Writing validateKey Methods" (page 375)](#apple-infemrccizeec).

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
