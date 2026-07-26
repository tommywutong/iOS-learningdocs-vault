---
title: roiTileCount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessorinput/roitilecount
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/roitilecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorinput/roitilecount.json'
content_hash: 'sha256:19165fe5a38647e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorInput](../ciimageprocessorinput.md)

# roiTileCount

<sub>Instance Property</sub>

This property tells a tiled-input processor how many input tiles will be processed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var roiTileCount: Int { get }
```

## Discussion

This property is only relevant if your processor implements `/CIImageProcessorKernel/roiTileArrayForInput:arguments:outputRect:`

This can be useful if the processor needs to do work [CIImageProcessorOutput](../ciimageprocessoroutput.md) after the last tile is processed.

## See Also

### Instance Properties

- [digest](digest.md) — A 64-bit digest that uniquely describes the contents of the input to a processor.
- [roiTileIndex](roitileindex.md) — This property tells a tiled-input processor which input tile index is being processed.
