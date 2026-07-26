---
title: 'class_getImageName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getimagename(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getimagename(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getimagename%28_%3A%29.json'
content_hash: 'sha256:72d67619cddd8a5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_getImageName(_:)

<sub>Function</sub>

Returns the name of the dynamic library a class originated from.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_getImageName(_ cls: AnyClass?) -> UnsafePointer<CChar>?
```

## Parameters

- `cls` — The class you are inquiring about.

## Return Value

A C string representing the name of the library containing the `cls` class.

## See Also

### Working with Libraries

- [objc_copyImageNames](<objc_copyimagenames(__).md>) — Returns the names of all the loaded Objective-C frameworks and dynamic libraries.
- [objc_copyClassNamesForImage](<objc_copyclassnamesforimage(____).md>) — Returns the names of all the classes within a specified library or framework.
