---
title: wantsExtendedDynamicRangeContent
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.11+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/wantsextendeddynamicrangecontent
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/wantsextendeddynamicrangecontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/wantsextendeddynamicrangecontent.json'
content_hash: 'sha256:7eaccabda1326981'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# wantsExtendedDynamicRangeContent

<sub>Instance Property</sub>

Enables extended dynamic range values onscreen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var wantsExtendedDynamicRangeContent: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). If any onscreen layer has this property set to [true](../../swift/true.md), all rendered content is clamped to the screen’s [maximumExtendedDynamicRangeColorComponentValue](../../appkit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md) value rather than `1.0`.

## See Also

### Related Documentation

- [maximumExtendedDynamicRangeColorComponentValue](../../appkit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md) — The current maximum color component value for the screen.

### Configuring Extended Dynamic Range Behavior

- [EDRMetadata](edrmetadata.md) — Metadata describing the tone mapping to apply to the extended dynamic range (EDR) values in the layer.
