---
title: synchronizeInputs
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessorkernel/synchronizeinputs
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/synchronizeinputs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/synchronizeinputs.json'
content_hash: 'sha256:e81e90202c790c38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# synchronizeInputs

<sub>Type Property</sub>

Override this class property to return false if you want your processor to be given input objects that have not been synchronized for CPU access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class var synchronizeInputs: Bool { get }
```

## Discussion

Generally, if your subclass uses the GPU your should override this method to return false. If not overridden, true is returned.

## See Also

### Type Properties

- [outputFormat](outputformat.md) — Override this class property if you want your processor’s output to be in a specific pixel format.
- [outputIsOpaque](outputisopaque.md) — Override this class property if your processor’s output stores 1.0 into the alpha channel of all pixels within the output extent.
