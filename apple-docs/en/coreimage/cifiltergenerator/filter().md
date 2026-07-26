---
title: filter()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifiltergenerator/filter()
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/filter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/filter%28%29.json'
content_hash: 'sha256:4b7a867b7a38e06f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# filter()

<sub>Instance Method</sub>

Creates a filter object based on the filter chain.

<sub>macOS</sub>

```swift
func filter() -> CIFilter
```

## Return Value

A `CIFilter` object.

## Discussion

The topology of the filter chain is immutable, meaning that any changes you make to the filter chain are not reflected in the filter. The returned filter holds the export input and output keys.
