---
title: 'accessibilitySetOverrideValue(_:forAttribute:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.1+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/accessibilitysetoverridevalue(_:forattribute:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitysetoverridevalue(_:forattribute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitysetoverridevalue%28_%3Aforattribute%3A%29.json'
content_hash: 'sha256:08bdacb981f2eb4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilitySetOverrideValue(_:forAttribute:)

<sub>Instance Method</sub>

Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value.

> [!warning] Deprecated
> Use [NSAccessibilityProtocol](../../appkit/nsaccessibilityprotocol.md) instead.

<sub>macOS</sub>

```swift
func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: NSAccessibility.Attribute) -> Bool
```

## Parameters

- `value` — The attribute value to be set.

- `attribute` — The name of the attribute. See [NSAccessibility](../../appkit/nsaccessibility.md) constants for lists of attribute names.

## Return Value

[YES](../yes.md) if the override was successful; otherwise, [NO](../no.md).

## Discussion

This method is for changing the set of attributes on an instance, as an alternative to subclassing.

This method works only on objects whose class already implements the `NSAccessibility` protocol. If the specified attribute is already supported by the object, the value specified by this method wins.

If the specified attribute does not exist, it is created outside the `NSAccessibility` protocol, so `accessibilityAttributeNames` still returns the old list, which does not contain the new attribute. Likewise, `accessibilityAttributeValue` does not return attributes created by the override process nor does it return their overridden values.

The values of overridden attributes are not settable by accessibility clients.

If you need to undo the effect of using this method, call it again, passing `nil` for the value.

Ensure that you invoke this method on the actual object that represents the user interface element. For example, for `NSButton`, use the underlying `NSButtonCell` object. `NSButton` itself is ignored by accessibility.

This method works only on an object representing a single user interface element. So, for example, you cannot use it when a single object represents multiple user interface elements, as with `NSSegmentedCell`, which has only a single object but provides user interface elements for each segment.

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
- [- accessibilitySetValue:forAttribute:](<accessibilitysetvalue(__forattribute_).md>) — Sets the value of the specified attribute in the receiver to the specified value. _(deprecated)_
- [- fileManager:shouldProceedAfterError:](<filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [- fileManager:willProcessPath:](<filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
