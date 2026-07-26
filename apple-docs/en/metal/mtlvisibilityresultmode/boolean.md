---
title: MTLVisibilityResultMode.boolean
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvisibilityresultmode/boolean
source_url: 'https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/boolean'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvisibilityresultmode/boolean.json'
content_hash: 'sha256:d16a422ff036e672'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVisibilityResultMode](../mtlvisibilityresultmode.md)

# MTLVisibilityResultMode.boolean

<sub>Case</sub>

The result records whether any samples passed depth and stencil tests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case boolean
```

## Discussion

The GPU writes a 64-bit integer to the visibility result buffer that is nonzero if at least one fragment passed depth and stencil tests, and zero if no fragments passed the tests.

## See Also

### Result modes

- [MTLVisibilityResultModeDisabled](disabled.md) — The result doesn’t contain any data because visibility testing was disabled.
- [MTLVisibilityResultModeCounting](counting.md) — The result records how many samples passed depth and stencil tests.
