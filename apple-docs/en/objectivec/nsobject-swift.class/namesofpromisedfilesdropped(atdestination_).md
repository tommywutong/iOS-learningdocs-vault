---
title: 'namesOfPromisedFilesDropped(atDestination:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/namesofpromisedfilesdropped(atdestination:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/namesofpromisedfilesdropped(atdestination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/namesofpromisedfilesdropped%28atdestination%3A%29.json'
content_hash: 'sha256:ea8a6658fa9c1fb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# namesOfPromisedFilesDropped(atDestination:)

<sub>Instance Method</sub>

Returns the names of the files that the receiver promises to create at a specified location.

> [!warning] Deprecated
> Use NSFilePromiseProvider objects instead

<sub>macOS</sub>

```swift
func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?
```

## Parameters

- `dropDestination` — A URL object that identifies the location at which the promised files will be created.

## Return Value

An array of the names of files (not full paths) that the receiver promises to create at `dropDestination`.

## Discussion

This method is invoked when the drop has been accepted by the destination and the destination, in the case of another Cocoa application, invokes the NSDraggingInfo method [namesOfPromisedFilesDropped(atDestination:)](<../../appkit/nsdragginginfo/namesofpromisedfilesdropped(atdestination_).md>). For long operations, you can cache `dropDestination` and defer the creation of the files until the `draggedImage:endedAt:operation:` method to avoid blocking the destination application.

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
