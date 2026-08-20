---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOKeyValueCoding.html
archived_at: '2026-07-18T01:28:41.195909Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOEnterpriseObject-4.md)
[!](EOKeyValueCoding-4.md)

---

# EOKeyValueCoding

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOKeyValueCoding.h

## Protocol Description

The EOKeyValueCoding informal protocol defines Enterprise Objects Framework's main data transport mechanism, in which the properties of an object are accessed indirectly by name (or _key_), rather than directly through invocation of an accessor method or as instance variables. Thus, all of an object's properties can be accessed in a consistent manner. the Framework additions to NSObject provide default implementations of EOKeyValueCoding, which are sufficient for most purposes.

The basic methods for accessing an object's values are __takeValue:forKey:__ , which sets the value for the property identified by the specified key, and __valueForKey:__ , which returns the value for the property identified by the specified key. The default implementations provided by NSObject use the accessor methods normally implemented by objects (or to access instance variables directly if need be), so that you don't have to write special code simply to integrate your objects into the Enterprise Objects Framework.

The corresponding methods __takeStoredValue:forKey:__ and __storedValueForKey:__ are similar, but they're considered to be a private API, for use by the Framework for transporting data to and from _trusted_ sources. For example, __takeStoredValue:forKey:__ is used to initialize an object's properties with values fetched from the database, whereas __takeValue:forKey:__ is used to modify an object's properties to values provided by a user or other business logic. How these methods work and how they're used by the framework is discussed in more detail in the section "[Stored Value Methods](EOKeyValueCoding-4.md)."

Both the basic and stored value key-value coding methods cache attribute bindings for both accessor methods and instance variables, making lookups efficient. The method __flushAllKeyBindings__ is provided to clear these bindings-as you should when you add or modify a class in the run-time system.

The the methods __accessInstanceVariablesDirectly__ and __useStoredAccessor__ are used by enterprise object classes to modify the behavior of the default implementations of key-value coding methods. The remaining methods, __handleQueryWithUnboundKey:__ , __handleTakeValue:forUnboundKey:__ , and __unableToSetNullForKey:__ , are provided to handle error conditions. The default versions of __handleQueryWithUnboundKey:__ and __handleTakeValue:forUnboundKey:__ raise EOUnknownKeyException, with the target object (_EOTargetObjectUserInfoKey_) and key (_EOUnknownUserInfoKey_) in the user info.

For more information on EOKeyValueCoding, see the sections:

- [Stored Value Methods](EOKeyValueCoding-4.md)
- [Type Checking and Type Conversion](EOKeyValueCoding-4.md)

**Accessing values**

**- storedValueForKey:

**- takeStoredValue:forKey:

**- takeValue:forKey:

**- valueForKey:********

**Changing default behavior**

**+ accessInstanceVariablesDirectly

**+ useStoredAccessor****

**Flushing key bindings**

**+ flushAllKeyBindings**

**Handling error conditions**

**- handleQueryWithUnboundKey:

**- handleTakeValue:forUnboundKey:

**- unableToSetNullForKey:******

---

#### accessInstanceVariablesDirectly

+ (BOOL)__accessInstanceVariablesDirectly__

Returns YES if the key-value coding methods should access the corresponding instance variable directly on finding no accessor method for a property. Returns NO if they shouldn't. NSObject's implementation of this method returns YES. Subclasses can override it to return NO, in which case the key-value coding methods won't access instance variables.

---

#### flushAllKeyBindings

+ (void)__flushAllKeyBindings__

Invalidates the cached key binding information for all classes (caches are kept of key-to-method or instance variable bindings in order to make key-value coding efficient). This method should be invoked whenever a class is modified in or removed from the run-time system.

---

#### useStoredAccessor

+ (BOOL)`useStoredAccessor`

Returns YES if the stored value methods (__storedValueForKey:__ and __takeStoredValue:forKey:__ ) should use private accessor methods in preference to public accessors. Returning NO causes the stored value methods to use the same accessor method-instance variable search order as the corresponding basic key-value coding methods (__valueForKey:__ and __takeValue:forKey:__ ). NSObject's implementation of this method returns YES.

---

#### handleQueryWithUnboundKey:

- (id)__handleQueryWithUnboundKey:__ (NSString \*)_key_

Invoked from __valueForKey:__ when it finds no property binding for _key_. NSObject's implementation raises an EOUnknownKeyException, with the target object (_EOTargetObjectUserInfoKey_) and key (_EOUnknownUserInfoKey_) in the user info. Subclasses can override this method to handle the query in some other way.

---

#### handleTakeValue:forUnboundKey:

- (void)__handleTakeValue:__ (id)_value___forUnboundKey:__ (NSString \*)_key_

Invoked from __takeValue:forKey:__ when it finds no property binding for _key_. NSObject's implementation raises an EOUnknownKeyException, with the target object (_EOTargetObjectUserInfoKey_) and key (_EOUnknownUserInfoKey_) in the user info. Subclasses can override it to handle the request in some other way.

---

#### storedValueForKey:

- (id)__storedValueForKey:__ (NSString \*)_key_

Returns the property identified by _key_. This method is used when the value is retrieved for storage in an object store (generally, this is ultimately in a database) or for inclusion in a snapshot. The default implementation provided by the Framework additions to NSObject is similar to the implementation of __valueForKey:__ , but it resolves _key_ with a different method-instance variable search order:

- Searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __storedValueForKey:__ looks for a method named `_getLastName` or `_lastName.`
- If a private accessor isn't found, searches for an instance variable based on _key_ and returns its value directly. For example, with a key of "lastName", __storedValueForKey:__ looks for an instance variable named ___lastName__ or __lastName__ .
- If neither a private accessor or an instance variable is found, __storedValueForKey:__ searches for a public accessor method based on _key_. For the key "lastName", this would be `getLastName` or `lastName`.
- If _key_ is unknown, __storedValueForKey:__ calls __handleTakeValue:forUnboundKey:__ .

This different search order allows an object to bypass processing that is performed before returning a value through public API. However, if you always want to use the search order in __valueForKey:__ , you can implement the class method __useStoredAccessor__ to return NO. And as with __valueForKey:__ , you can prevent direct access of an instance variable with the method the class method __accessInstanceVariablesDirectly__ .

---

#### takeStoredValue:forKey:

- (void)`takeStoredValue:`(id)_value_`forKey:`(NSString \*)_key_

Sets the property identified by _key_ to _value_. This method is used to initialize the receiver with values from an object store (generally, this is ultimately from a database) or to restore a value from a snapshot. The default implementation provided by the Framework additions to NSObject is similar to the implementation of __takeValue:forKey:__ , but it resolves _key_ with a different method-instance variable search order:

- Searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __takeStoredValue:forKey:__ looks for a method named `_setLastName`:`.`
- If a private accessor isn't found, searches for an instance variable based on _key_ and and sets its value directly. For example, with a key of "lastName", __takeStoredValue:forKey:__ looks for an instance variable named ___lastName__ or __lastName__ .
- If neither a private accessor or an instance variable is found, __takeStoredValue:forKey:__ searches for a public accessor method based on _key_. For the key "lastName", this would be `setLastName`:.
- If _key_ is unknown, __storedValueForKey:__ calls __handleTakeValue:forUnboundKey:__ .

This different search order allows an object to bypass processing that is performed before setting a value through public API. However, if you always want to use the search order in __takeValue:forKey:__ , you can implement the class method __useStoredAccessor__ to return NO. And as with __valueForKey:__ , you can prevent direct access of an instance variable with the method the class method __accessInstanceVariablesDirectly__ .

---

#### takeValue:forKey:

- (void)__takeValue:__ (id)_value___forKey:__ (NSString \*)_key_

Sets the value for the property identified by _key_ to _value_, invoking __handleTakeValue:forUnboundKey:__ if the receiver doesn't recognize _key_ and __unableToSetNullForKey:__ if _value_ is __nil__ and _key_ identifies a scalar property.

The default implementation provided by the Framework additions to NSObject works as follows:

- Searches for a public accessor method of the form __set__ _Key___:__ , invoking it if there is one.
- If a public accessor method isn't found, searches for a private accessor method of the form ___set__ _Key___:__ , invoking it if there is one.
- If an accesor method isn't found and the class method __accessInstanceVariablesDirectly__ returns YES, __takeValue:forKey:__ searches for an instance variable based on _key_ and sets the value directly, autoreleasing the old value and retaining the new one. For the key "lastName", this would be ___lastName__ or __lastName__ .
- If neither an accessor method nor an instance variable is found, the default implementation invokes __handleTakeValue:forUnboundKey:__ .

---

#### unableToSetNullForKey:

- (void)__unableToSetNilForKey:__ (NSString \*)_key_

Invoked from __takeValue:forKey:__ (and __takeStoredValue:forKey:__ ) when it's given a __nil__ value for a scalar property (such as an __int__ or a __float__ ). NSObject's implementation raises an NSInvalidArgumentException. Subclasses can override it to handle the request in some other way, such as by substituting zero or a sentinel value and invoking __takeValue:forKey:__ again.

---

#### valueForKey:

- (id)__valueForKey:__ (NSString \*)_key_

Returns the value for the property identified by _key_, invoking __handleQueryWithUnboundKey:__ if the receiver doesn't recognize _key_.

The default implementation provided by the Framework additions to NSObject works as follows:

- Searches for a public accessor method based on _key_. For example, with a key of "lastName", __valueForKey:__ looks for a method named `getLastName` or `lastName`.
- If a public accessor method isn't found, searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __valueForKey:__ looks for a method named `_getLastName` or `_lastName.`
- If an accesor method isn't found and the class method __accessInstanceVariablesDirectly__ returns YES, __valueForKey:__ searches for an instance variable based on _key_ and returns its value directly. For the key "lastName", this would be `_lastName` or `lastName`.
- If neither an accessor method nor an instance variable is found, the default implementation invokes __handleQueryWithUnboundKey:__ .

---

[!](EOEnterpriseObject-4.md)
[!](EOKeyValueCoding-4.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
