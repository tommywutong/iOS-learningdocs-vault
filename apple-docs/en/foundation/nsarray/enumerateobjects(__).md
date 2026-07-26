---
title: 'enumerateObjects(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/enumerateobjects(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/enumerateobjects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/enumerateobjects%28_%3A%29.json'
content_hash: 'sha256:cd1cf65babb1fd86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# enumerateObjects(_:)

<sub>Instance Method</sub>

Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateObjects(_ block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `block` — A closure or block to execute for each object in the array, taking three arguments: - The object. - The index of the object in the array. - A reference to a Boolean value, which the closure can set to [true](../../swift/true.md) in order to stop further enumeration of the array. If a closure stops further enumeration, that closure continues to run until it’s finished.

## Discussion

This method executes synchronously. Values allocated within the block are deallocated after the block is executed.

## See Also

### Sending Messages to Elements

- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes a given closure or block using each object in the array with the specified options.
- [- enumerateObjectsAtIndexes:options:usingBlock:](<enumerateobjects(at_options_using_).md>) — Executes a given block using the objects in the array at the specified indexes.
