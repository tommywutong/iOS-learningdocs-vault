---
title: MTL4TimestampGranularity.relaxed
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4timestampgranularity/relaxed
source_url: 'https://developer.apple.com/documentation/metal/mtl4timestampgranularity/relaxed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4timestampgranularity/relaxed.json'
content_hash: 'sha256:37e5d2eac4c2c599'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4TimestampGranularity](../mtl4timestampgranularity.md)

# MTL4TimestampGranularity.relaxed

<sub>Case</sub>

A minimally-invasive timestamp which may be less precise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case relaxed
```

## Discussion

Using this granularity incurs in the lowest overhead, at the cost of precision. For example, it may sample at command encoder boundaries.
