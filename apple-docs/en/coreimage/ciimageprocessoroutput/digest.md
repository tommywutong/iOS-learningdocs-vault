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
doc_path: /documentation/coreimage/ciimageprocessoroutput/digest
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/digest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessoroutput/digest.json'
content_hash: 'sha256:b176beb04066f686'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorOutput](../ciimageprocessoroutput.md)

# digest

<sub>Instance Property</sub>

A 64-bit digest that uniquely describes the contents of the output of a processor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var digest: UInt64 { get }
```

## Discussion

This digest will change if the graph up to and including the output of the processor changes in any way.
