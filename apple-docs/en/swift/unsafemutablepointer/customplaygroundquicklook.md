---
title: customPlaygroundQuickLook
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swift/unsafemutablepointer/customplaygroundquicklook
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/customplaygroundquicklook'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/customplaygroundquicklook.json'
content_hash: 'sha256:44507b57e425f037'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# customPlaygroundQuickLook

<sub>Instance Property</sub>

A custom playground Quick Look for this instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var customPlaygroundQuickLook: PlaygroundQuickLook { get }
```

## Discussion

If this type has value semantics, the `PlaygroundQuickLook` instance should be unaffected by subsequent mutations.
