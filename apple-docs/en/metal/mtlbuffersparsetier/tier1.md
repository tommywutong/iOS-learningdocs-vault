---
title: MTLBufferSparseTier.tier1
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbuffersparsetier/tier1
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffersparsetier/tier1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffersparsetier/tier1.json'
content_hash: 'sha256:c81fae8cc8ac4e8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBufferSparseTier](../mtlbuffersparsetier.md)

# MTLBufferSparseTier.tier1

<sub>Case</sub>

Indicates support for sparse buffers tier 1.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case tier1
```

## Discussion

Tier 1 sparse buffers allow the following:

- Partial memory backing at sparse page granularity.
- Defined behavior for accessing an _unbacked_ buffer range.

An unbacked buffer range indicates a range within the buffer that doesn’t have memory backing at a given point in time. Accessing an unbacked buffer range of a sparse buffer produces the following results:

- Reading return zero.
- Writing produces no result.
