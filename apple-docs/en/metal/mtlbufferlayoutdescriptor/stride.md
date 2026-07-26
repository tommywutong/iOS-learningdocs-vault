---
title: stride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbufferlayoutdescriptor/stride
source_url: 'https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/stride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbufferlayoutdescriptor/stride.json'
content_hash: 'sha256:3d0b61b19c080049'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBufferLayoutDescriptor](../mtlbufferlayoutdescriptor.md)

# stride

<sub>Instance Property</sub>

The number of bytes from one buffer entry to the next.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stride: Int { get set }
```

## Discussion

The default value is `1`. Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Describing fetch behavior

- [stepFunction](stepfunction.md) — Determines how and when compute functions fetch data.
- [stepRate](steprate.md) — How frequently the step function should load data.
- [MTLStepFunction](../mtlstepfunction.md) — The frequency and locations at which a function fetches attribute data.
