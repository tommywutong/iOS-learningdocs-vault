---
title: targetTimestamp
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldisplaylink/update/targettimestamp
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update/targettimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylink/update/targettimestamp.json'
content_hash: 'sha256:d5486b89beb6bd36'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Animation](../../../quartzcore.md) · [CAMetalDisplayLink](../../cametaldisplaylink.md) · [Update](../update.md)

# targetTimestamp

<sub>Instance Property</sub>

A deadline that indicates when your app needs to finish rendering to the drawable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var targetTimestamp: CFTimeInterval { get }
```

## Discussion

Your app needs to call the [drawable](drawable.md) instance’s [present()](<../../../metal/mtldrawable/present().md>) method before the deadline. GPU rendering can continue after this time, based on [preferredFrameLatency](../preferredframelatency.md). For more information on timing your app’s rendering, see [- metalDisplayLink:needsUpdate:](<../../cametaldisplaylinkdelegate/metaldisplaylink(__needsupdate_).md>).

## See Also

### Drawing the Next Frame

- [drawable](drawable.md) — The Metal drawable your app uses to render the next frame.
