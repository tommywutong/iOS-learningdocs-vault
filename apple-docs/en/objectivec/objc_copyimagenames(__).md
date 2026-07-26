---
title: 'objc_copyImageNames(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_copyimagenames(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_copyimagenames(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_copyimagenames%28_%3A%29.json'
content_hash: 'sha256:3cdec85ef4b4e845'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_copyImageNames(_:)

<sub>Function</sub>

Returns the names of all the loaded Objective-C frameworks and dynamic libraries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_copyImageNames(_ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>
```

## Parameters

- `outCount` — The number of names in the returned array.

## Return Value

An array of C strings representing the names of all the loaded Objective-C frameworks and dynamic libraries.

## See Also

### Working with Libraries

- [class_getImageName](<class_getimagename(__).md>) — Returns the name of the dynamic library a class originated from.
- [objc_copyClassNamesForImage](<objc_copyclassnamesforimage(____).md>) — Returns the names of all the classes within a specified library or framework.
