---
title: 'enumerateObjects(options:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/enumerateobjects(options:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/enumerateobjects(options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/enumerateobjects%28options%3Ausing%3A%29.json'
content_hash: 'sha256:ae116c1c887f323d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# enumerateObjects(options:using:)

<sub>Instance Method</sub>

Executes a given closure or block using each object in the array with the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateObjects(options opts: NSEnumerationOptions = [], using block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `opts` — The options for the enumeration. For possible values, see [NSEnumerationOptions](../nsenumerationoptions.md).

- `block` — A closure or block to execute for each object in the array, taking three arguments: - The object. - The index of the object in the array. - A reference to a Boolean value, which the closure can set to [true](../../swift/true.md) in order to stop further enumeration of the array. If a closure stops further enumeration, that closure continues to run until it’s finished. When the [NSEnumerationConcurrent](../nsenumerationoptions/concurrent.md) enumeration option is specified, enumeration stops after all of the currently running closures finish.

## Discussion

This method executes synchronously. By default, the enumeration starts with the first object and continues serially through the array to the last object. You can specify [NSEnumerationConcurrent](../nsenumerationoptions/concurrent.md) and/or [NSEnumerationReverse](../nsenumerationoptions/reverse.md) as enumeration options to modify this behavior.

## See Also

### Sending Messages to Elements

- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [- enumerateObjectsAtIndexes:options:usingBlock:](<enumerateobjects(at_options_using_).md>) — Executes a given block using the objects in the array at the specified indexes.
