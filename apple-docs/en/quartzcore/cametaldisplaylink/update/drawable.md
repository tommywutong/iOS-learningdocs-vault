---
title: drawable
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldisplaylink/update/drawable
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update/drawable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylink/update/drawable.json'
content_hash: 'sha256:ac52f7ac883dd0ee'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Animation](../../../quartzcore.md) · [CAMetalDisplayLink](../../cametaldisplaylink.md) · [Update](../update.md)

# drawable

<sub>Instance Property</sub>

The Metal drawable your app uses to render the next frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var drawable: any CAMetalDrawable { get }
```

## See Also

### Drawing the Next Frame

- [targetTimestamp](targettimestamp.md) — A deadline that indicates when your app needs to finish rendering to the drawable.
