---
title: layers
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciazteccodegenerator/layers
source_url: 'https://developer.apple.com/documentation/coreimage/ciazteccodegenerator/layers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciazteccodegenerator/layers.json'
content_hash: 'sha256:89d60321ba4b5862'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIAztecCodeGenerator](../ciazteccodegenerator.md)

# layers

<sub>Instance Property</sub>

The number of Aztec layers, a value from 1 to 32.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layers: Float { get set }
```

## Discussion

Set to `nil` for automatic.

## See Also

### Instance Properties

- [compactStyle](compactstyle.md) — A Boolean that specifies whether to force a compact style Aztec code.
- [correctionLevel](correctionlevel.md) — The Aztec error correction, a value from 5 to 95.
- [message](message.md) — The message to encode in the Aztec barcode.
