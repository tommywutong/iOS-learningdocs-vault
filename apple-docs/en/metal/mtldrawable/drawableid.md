---
title: drawableID
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldrawable/drawableid
source_url: 'https://developer.apple.com/documentation/metal/mtldrawable/drawableid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawable/drawableid.json'
content_hash: 'sha256:81aa05c24411acb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDrawable](../mtldrawable.md)

# drawableID

<sub>Instance Property</sub>

A positive integer that identifies the drawable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var drawableID: Int { get }
```

## Discussion

Drawable objects are usually owned by some other object, such as a [CAMetalLayer](../../quartzcore/cametallayer.md). The owning object gives the first drawable it creates an ID of `0`, and it increments the ID by `1` for each additional drawable it creates.
