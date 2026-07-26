---
title: customPlaygroundQuickLook
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cgrect/customplaygroundquicklook
source_url: 'https://developer.apple.com/documentation/corefoundation/cgrect/customplaygroundquicklook'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgrect/customplaygroundquicklook.json'
content_hash: 'sha256:e8d6e8cce6c0af76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CGRect](../cgrect.md)

# customPlaygroundQuickLook

<sub>Instance Property</sub>

A custom playground Quick Look for this instance.

> [!warning] Deprecated
> CGRect.customPlaygroundQuickLook will be removed in a future Swift version

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var customPlaygroundQuickLook: PlaygroundQuickLook { get }
```

## Discussion

If this type has value semantics, the `PlaygroundQuickLook` instance should be unaffected by subsequent mutations.
