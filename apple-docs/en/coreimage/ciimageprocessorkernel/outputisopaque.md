---
title: outputIsOpaque
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessorkernel/outputisopaque
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/outputisopaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/outputisopaque.json'
content_hash: 'sha256:30795f94ad4eb5c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# outputIsOpaque

<sub>Type Property</sub>

Override this class property if your processor’s output stores 1.0 into the alpha channel of all pixels within the output extent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class var outputIsOpaque: Bool { get }
```

## Discussion

If not overridden, false is returned.

## See Also

### Type Properties

- [outputFormat](outputformat.md) — Override this class property if you want your processor’s output to be in a specific pixel format.
- [synchronizeInputs](synchronizeinputs.md) — Override this class property to return false if you want your processor to be given input objects that have not been synchronized for CPU access.
