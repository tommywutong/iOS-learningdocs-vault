---
title: 'objc_copyImageHeaders(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/objectivec/objc_copyimageheaders(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_copyimageheaders(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_copyimageheaders%28_%3A%29.json'
content_hash: 'sha256:98749b45eab57c54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_copyImageHeaders(_:)

<sub>Function</sub>

Returns the Mach headers of all the images loaded into the current process that contain Objective-C or Swift code.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func objc_copyImageHeaders(_ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<OpaquePointer>
```

<sub>Mac Catalyst, macOS</sub>

```swift
func objc_copyImageHeaders(_ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<mach_header>>
```

## Parameters

- `outCount` — The number of image headers returned.

## Return Value

An array of @c mach_header pointers. The array contains @c *outCount pointers followed by a @c NULL terminator. You must free the array with
