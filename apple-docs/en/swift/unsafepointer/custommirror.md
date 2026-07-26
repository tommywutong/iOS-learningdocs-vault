---
title: customMirror
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafepointer/custommirror
source_url: 'https://developer.apple.com/documentation/swift/unsafepointer/custommirror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafepointer/custommirror.json'
content_hash: 'sha256:a2d76e018cafc2c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafePointer](../unsafepointer.md)

# customMirror

<sub>Instance Property</sub>

The custom mirror for this instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var customMirror: Mirror { get }
```

## Discussion

If this type has value semantics, the mirror should be unaffected by subsequent mutations of the instance.
