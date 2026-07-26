---
title: 'objc_copyClassNamesForImage(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_copyclassnamesforimage(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_copyclassnamesforimage(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_copyclassnamesforimage%28_%3A_%3A%29.json'
content_hash: 'sha256:ebe95600a7e2fe97'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_copyClassNamesForImage(_:_:)

<sub>Function</sub>

Returns the names of all the classes within a specified library or framework.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_copyClassNamesForImage(_ image: UnsafePointer<CChar>, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>?
```

## Parameters

- `image` — The library or framework you are inquiring about.

- `outCount` — The number of class names in the returned array.

## Return Value

An array of C strings representing all of the class names within the specified library or framework.

## See Also

### Working with Libraries

- [objc_copyImageNames](<objc_copyimagenames(__).md>) — Returns the names of all the loaded Objective-C frameworks and dynamic libraries.
- [class_getImageName](<class_getimagename(__).md>) — Returns the name of the dynamic library a class originated from.
