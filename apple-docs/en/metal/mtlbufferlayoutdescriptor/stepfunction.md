---
title: stepFunction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbufferlayoutdescriptor/stepfunction
source_url: 'https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/stepfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbufferlayoutdescriptor/stepfunction.json'
content_hash: 'sha256:fa80bac46dd5bd1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBufferLayoutDescriptor](../mtlbufferlayoutdescriptor.md)

# stepFunction

<sub>Instance Property</sub>

Determines how and when compute functions fetch data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stepFunction: MTLStepFunction { get set }
```

## See Also

### Describing fetch behavior

- [stride](stride.md) — The number of bytes from one buffer entry to the next.
- [stepRate](steprate.md) — How frequently the step function should load data.
- [MTLStepFunction](../mtlstepfunction.md) — The frequency and locations at which a function fetches attribute data.
