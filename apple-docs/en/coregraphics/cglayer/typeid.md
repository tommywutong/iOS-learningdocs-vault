---
title: typeID
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglayer/typeid
source_url: 'https://developer.apple.com/documentation/coregraphics/cglayer/typeid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglayer/typeid.json'
content_hash: 'sha256:648720d02ea12442'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGLayer](../cglayer.md)

# typeID

<sub>Type Property</sub>

Returns the unique type identifier used for [CGLayer](../cglayer.md) objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var typeID: CFTypeID { get }
```

## Discussion

A type identifier is an integer that identifies the opaque type to which a Core Foundation object belongs. You use type IDs in various contexts, such as when you are operating on heterogeneous collections.
