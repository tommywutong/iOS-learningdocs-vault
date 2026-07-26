---
title: stepRate
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbufferlayoutdescriptor/steprate
source_url: 'https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/steprate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbufferlayoutdescriptor/steprate.json'
content_hash: 'sha256:3a78041949ab5c03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBufferLayoutDescriptor](../mtlbufferlayoutdescriptor.md)

# stepRate

<sub>Instance Property</sub>

How frequently the step function should load data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stepRate: Int { get set }
```

## Discussion

The interpretation of this value depends on the setting of `stepFunction`.

## See Also

### Describing fetch behavior

- [stride](stride.md) — The number of bytes from one buffer entry to the next.
- [stepFunction](stepfunction.md) — Determines how and when compute functions fetch data.
- [MTLStepFunction](../mtlstepfunction.md) — The frequency and locations at which a function fetches attribute data.
