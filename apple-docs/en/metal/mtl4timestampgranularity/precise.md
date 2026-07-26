---
title: MTL4TimestampGranularity.precise
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4timestampgranularity/precise
source_url: 'https://developer.apple.com/documentation/metal/mtl4timestampgranularity/precise'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4timestampgranularity/precise.json'
content_hash: 'sha256:1ff08e7f96e12073'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4TimestampGranularity](../mtl4timestampgranularity.md)

# MTL4TimestampGranularity.precise

<sub>Case</sub>

A timestamp as precise as possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case precise
```

## Discussion

Using this granularity may incur in a performance penalty, for example, it may cause splitting of command encoders.
