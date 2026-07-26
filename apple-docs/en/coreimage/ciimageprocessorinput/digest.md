---
title: digest
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessorinput/digest
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/digest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorinput/digest.json'
content_hash: 'sha256:6574957d25fbf4d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorInput](../ciimageprocessorinput.md)

# digest

<sub>Instance Property</sub>

A 64-bit digest that uniquely describes the contents of the input to a processor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var digest: UInt64 { get }
```

## Discussion

This digest will change if the graph of the input changes in any way.

## See Also

### Instance Properties

- [roiTileCount](roitilecount.md) — This property tells a tiled-input processor how many input tiles will be processed.
- [roiTileIndex](roitileindex.md) — This property tells a tiled-input processor which input tile index is being processed.
