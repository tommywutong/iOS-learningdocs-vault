---
title: NSKeyValueCoding
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nskeyvaluecoding
source_url: 'https://developer.apple.com/documentation/objectivec/nskeyvaluecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nskeyvaluecoding.json'
content_hash: 'sha256:24921e7612f88c2c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSKeyValueCoding

<sub>API Collection</sub>

A mechanism by which you can access the properties of an object indirectly by name or key.

## Overview

The basic methods for accessing an object’s values are [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>), which sets the value for the property identified by the specified key, and [- valueForKey:](<nsobject-swift.class/value(forkey_).md>), which returns the value for the property identified by the specified key. Thus, all of an object’s properties can be accessed in a consistent manner.

The default implementation relies on the accessor methods normally implemented by objects (or to access instance variables directly if need be).

## Topics

### Getting Values

- [- valueForKey:](<nsobject-swift.class/value(forkey_).md>) — Returns the value for the property identified by a given key.
- [- valueForKeyPath:](<nsobject-swift.class/value(forkeypath_).md>) — Returns the value for the derived property identified by a given key path.
- [- dictionaryWithValuesForKeys:](<nsobject-swift.class/dictionarywithvalues(forkeys_).md>) — Returns a dictionary containing the property values identified by each of the keys in a given array.
- [- valueForUndefinedKey:](<nsobject-swift.class/value(forundefinedkey_).md>) — Invoked by [- valueForKey:](<nsobject-swift.class/value(forkey_).md>) when it finds no property corresponding to a given key.
- [- mutableArrayValueForKey:](<nsobject-swift.class/mutablearrayvalue(forkey_).md>) — Returns a mutable array proxy that provides read-write access to an ordered to-many relationship specified by a given key.
- [- mutableArrayValueForKeyPath:](<nsobject-swift.class/mutablearrayvalue(forkeypath_).md>) — Returns a mutable array that provides read-write access to the ordered to-many relationship specified by a given key path.
- [- mutableSetValueForKey:](<nsobject-swift.class/mutablesetvalue(forkey_).md>) — Returns a mutable set proxy that provides read-write access to the unordered to-many relationship specified by a given key.
- [- mutableSetValueForKeyPath:](<nsobject-swift.class/mutablesetvalue(forkeypath_).md>) — Returns a mutable set that provides read-write access to the unordered to-many relationship specified by a given key path.
- [- mutableOrderedSetValueForKey:](<nsobject-swift.class/mutableorderedsetvalue(forkey_).md>) — Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key.
- [- mutableOrderedSetValueForKeyPath:](<nsobject-swift.class/mutableorderedsetvalue(forkeypath_).md>) — Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.

### Setting Values

- [- setValue:forKeyPath:](<nsobject-swift.class/setvalue(__forkeypath_).md>) — Sets the value for the property identified by a given key path to a given value.
- [- setValuesForKeysWithDictionary:](<nsobject-swift.class/setvaluesforkeys(__).md>) — Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [- setNilValueForKey:](<nsobject-swift.class/setnilvalueforkey(__).md>) — Invoked by [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) — Sets the property of the receiver specified by a given key to a given value.
- [- setValue:forUndefinedKey:](<nsobject-swift.class/setvalue(__forundefinedkey_).md>) — Invoked by [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) when it finds no property for a given key.

### Changing Default Behavior

- [accessInstanceVariablesDirectly](nsobject-swift.class/accessinstancevariablesdirectly.md) — Returns a Boolean value that indicates whether the key-value coding methods should access the corresponding instance variable directly on finding no accessor method for a property.

### Validation

- [- validateValue:forKey:error:](<nsobject-swift.class/validatevalue(__forkey_).md>) — Indicates whether the value specified by a given pointer is valid, or can be made valid, for the property identified by a given key.
- [- validateValue:forKeyPath:error:](<nsobject-swift.class/validatevalue(__forkeypath_).md>) — Indicates whether the value specified by a given pointer is not valid for a given key path relative to the receiver.

### Deprecated Methods

- [+ useStoredAccessor](<nsobject-swift.class/usestoredaccessor().md>) — Returns `true` if the stored value methods [- storedValueForKey:](<nsobject-swift.class/storedvalue(forkey_).md>) and [- takeStoredValue:forKey:](<nsobject-swift.class/takestoredvalue(__forkey_).md>) should use private accessor methods in preference to public accessors. _(deprecated)_
- [- handleQueryWithUnboundKey:](<nsobject-swift.class/handlequery(withunboundkey_).md>) — Invoked by [- valueForKey:](<nsobject-swift.class/value(forkey_).md>) when it finds no property corresponding to `key`. _(deprecated)_
- [- handleTakeValue:forUnboundKey:](<nsobject-swift.class/handletakevalue(__forunboundkey_).md>) — Invoked by [- takeValue:forKey:](<nsobject-swift.class/takevalue(__forkey_).md>) when it finds no property binding for `key`. _(deprecated)_
- [- storedValueForKey:](<nsobject-swift.class/storedvalue(forkey_).md>) — Returns the property identified by a given key. _(deprecated)_
- [- takeStoredValue:forKey:](<nsobject-swift.class/takestoredvalue(__forkey_).md>) — Sets the value of the property identified by a given key. _(deprecated)_
- [- takeValuesFromDictionary:](<nsobject-swift.class/takevalues(from_).md>) — Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties _(deprecated)_
- [- takeValue:forKeyPath:](<nsobject-swift.class/takevalue(__forkeypath_).md>) — Sets the value for the property identified by `keyPath` to `value`. _(deprecated)_
- [- takeValue:forKey:](<nsobject-swift.class/takevalue(__forkey_).md>) — Sets the value for the property identified by `key` to `value`. _(deprecated)_
- [- unableToSetNilForKey:](<nsobject-swift.class/unabletosetnil(forkey_).md>) — Invoked if `key` is represented by a scalar attribute. _(deprecated)_
- [- valuesForKeys:](<nsobject-swift.class/values(forkeys_).md>) — Returns a dictionary containing as keys the property names in `keys`, with corresponding values being the corresponding property values. _(deprecated)_

### Constants

- [Key Value Coding Exception Names](key-value-coding-exception-names.md) — This constant defines the name of an exception raised when a key value coding operation fails.
- [NSUndefinedKeyException userInfo Keys](nsundefinedkeyexception-userinfo-keys.md) — These constants are keys into an `NSUndefinedKeyException` `userInfo` dictionary
- [NSKeyValueValidationError](../foundation/nskeyvaluevalidationerror-swift.var.md) — A key-value coding validation error.

## See Also

### Related Documentation

- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)

### Key-Value Coding

- [NSKeyValueBindingCreation](nskeyvaluebindingcreation.md) — A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [NSScriptKeyValueCoding](nsscriptkeyvaluecoding.md) — A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — Exceptions raised by key-value coding methods.
