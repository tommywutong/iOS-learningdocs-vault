---
title: 'fileManager(_:shouldProceedAfterError:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/filemanager(_:shouldproceedaftererror:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/filemanager(_:shouldproceedaftererror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/filemanager%28_%3Ashouldproceedaftererror%3A%29.json'
content_hash: 'sha256:51ad8a02f8dc2efc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# fileManager(_:shouldProceedAfterError:)

<sub>Instance Method</sub>

An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.

> [!warning] Deprecated
> See delegate methods for copy, move, remove, and link methods.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool
```

## Parameters

- `fm` — The file manager that sent this message.

- `errorInfo` — A dictionary that contains two or three pieces of information (all [NSString](../../foundation/nsstring.md) objects) related to the error: | Key | Value | |---|---| | `@"Path"` | The path related to the error (usually the source path) | | `@"Error"` | A description of the error | | `@"ToPath"` | The destination path (not all errors) |

## Return Value

[YES](../yes.md) if the operation (which is often continuous within a loop) should proceed, otherwise [NO](../no.md).

## Discussion

An `NSFileManager` object, `manager`, sends this message for each error it encounters when copying, moving, removing, or linking files or directories. The return value is passed back to the invoker of [copyPath:toPath:handler:](../../foundation/nsfilemanager/copypath_topath_handler_.md), [movePath:toPath:handler:](../../foundation/nsfilemanager/movepath_topath_handler_.md), [removeFileAtPath:handler:](../../foundation/nsfilemanager/removefileatpath_handler_.md), or [linkPath:toPath:handler:](../../foundation/nsfilemanager/linkpath_topath_handler_.md). If an error occurs and your handler has not implemented this method, the invoking method automatically returns [NO](../no.md).

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
- [- fileManager:willProcessPath:](<filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
