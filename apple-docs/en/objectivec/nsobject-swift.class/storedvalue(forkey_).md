---
title: 'storedValue(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/storedvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/storedvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/storedvalue%28forkey%3A%29.json'
content_hash: 'sha256:1d571a124daa534a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# storedValue(forKey:)

<sub>Instance Method</sub>

Returns the property identified by a given key.

> [!warning] Deprecated
> If you are using the `NSManagedObject` class, use [primitiveValue(forKey:)](<../../coredata/nsmanagedobject/primitivevalue(forkey_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func storedValue(forKey key: String) -> Any?
```

## Discussion

This method is used when the value is retrieved for storage in an object store (generally, this storage is ultimately in a database) or for inclusion in a snapshot. The default implementation is similar to the implementation of [- valueForKey:](<value(forkey_).md>), but it resolves `key` with a different method/instance variable search order:

1. Searches for a private accessor method based on `key` (a method preceded by an underbar). For example, with a `key` of “lastName”, [- storedValueForKey:](<storedvalue(forkey_).md>) looks for a method named `_getLastName` or `_lastName`.
2. If a private accessor is not found, searches for an instance variable based on `key` and returns its value directly. For example, with a `key` of “lastName”, [- storedValueForKey:](<storedvalue(forkey_).md>) looks for an instance variable named `_lastName` or `lastName`.
3. If neither a private accessor nor an instance variable is found, [- storedValueForKey:](<storedvalue(forkey_).md>) searches for a public accessor method based on `key`. For the `key` “lastName”, this would be `getLastName` or `lastName`.
4. If `key` is unknown, [- storedValueForKey:](<storedvalue(forkey_).md>) calls [- handleTakeValue:forUnboundKey:](<handletakevalue(__forunboundkey_).md>).

This different search order allows an object to bypass processing that is performed before returning a value through a public API. However, if you always want to use the search order in [- valueForKey:](<value(forkey_).md>), you can implement the class method [+ useStoredAccessor](<usestoredaccessor().md>) to return [NO](../no.md). And as with [- valueForKey:](<value(forkey_).md>), you can prevent direct access of an instance variable with the class method [accessInstanceVariablesDirectly](accessinstancevariablesdirectly.md).

## See Also

### Deprecated Methods

- [- accessibilityAttributeNames](<accessibilityattributenames().md>) — Returns an array of attribute names supported by the receiver. _(deprecated)_
- [- accessibilityAttributeValue:](<accessibilityattributevalue(__).md>) — Returns the value of the specified attribute in the receiver. _(deprecated)_
- [- accessibilityAttributeValue:forParameter:](<accessibilityattributevalue(__forparameter_).md>) — Returns the value of the receiver’s parameterized attribute corresponding to the specified attribute name and parameter. _(deprecated)_
- [- accessibilityActionDescription:](<accessibilityactiondescription(__).md>) — Returns a localized description of the specified action. _(deprecated)_
- [- accessibilityActionNames](<accessibilityactionnames().md>) — Returns an array of action names supported by the accessibility element. _(deprecated)_
- [- accessibilityArrayAttributeCount:](<accessibilityarrayattributecount(__).md>) — Returns the count of the specified accessibility array attribute. _(deprecated)_
- [- accessibilityArrayAttributeValues:index:maxCount:](<accessibilityarrayattributevalues(__index_maxcount_).md>) — Returns a subarray of values of an accessibility array attribute. _(deprecated)_
- [- accessibilityIndexOfChild:](<accessibilityindex(ofchild_).md>) — Returns the index of the specified accessibility child in the parent. _(deprecated)_
- [- accessibilityIsAttributeSettable:](<accessibilityisattributesettable(__).md>) — Returns a Boolean value that indicates whether the value for the specified attribute in the receiver can be set. _(deprecated)_
- [- accessibilityIsIgnored](<accessibilityisignored().md>) — Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy. _(deprecated)_
- [- accessibilityParameterizedAttributeNames](<accessibilityparameterizedattributenames().md>) — Returns a list of parameterized attribute names supported by the receiver. _(deprecated)_
- [- accessibilityPerformAction:](<accessibilityperformaction(__).md>) — Performs the action associated with the specified action. _(deprecated)_
- [- accessibilitySetOverrideValue:forAttribute:](<accessibilitysetoverridevalue(__forattribute_).md>) — Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value. _(deprecated)_
- [- accessibilitySetValue:forAttribute:](<accessibilitysetvalue(__forattribute_).md>) — Sets the value of the specified attribute in the receiver to the specified value. _(deprecated)_
- [- fileManager:shouldProceedAfterError:](<filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
