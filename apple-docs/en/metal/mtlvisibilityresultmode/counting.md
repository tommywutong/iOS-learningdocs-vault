---
title: MTLVisibilityResultMode.counting
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvisibilityresultmode/counting
source_url: 'https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/counting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvisibilityresultmode/counting.json'
content_hash: 'sha256:6fc5c2ece8a91799'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVisibilityResultMode](../mtlvisibilityresultmode.md)

# MTLVisibilityResultMode.counting

<sub>Case</sub>

The result records how many samples passed depth and stencil tests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case counting
```

## Discussion

The GPU writes a 64-bit integer to the visibility result buffer that is the number of samples that passed depth and stencil tests; this can be zero. Counting is not supported by all GPUs. Check the following documents to see whether a GPU family supports _counting occlusion_ queries:

- [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [Metal feature set tables (Numbers)](https://developer.apple.com/metal/metal-feature-set-tables.zip)

## See Also

### Result modes

- [MTLVisibilityResultModeDisabled](disabled.md) — The result doesn’t contain any data because visibility testing was disabled.
- [MTLVisibilityResultModeBoolean](boolean.md) — The result records whether any samples passed depth and stencil tests.
