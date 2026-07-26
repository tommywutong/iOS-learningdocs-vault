---
title: MTLIOStatus.cancelled
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliostatus/cancelled
source_url: 'https://developer.apple.com/documentation/metal/mtliostatus/cancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliostatus/cancelled.json'
content_hash: 'sha256:25b5e84ce343f8fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOStatus](../mtliostatus.md)

# MTLIOStatus.cancelled

<sub>Case</sub>

Indicates the GPU has successfully abandoned the input/output command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case cancelled
```

## See Also

### I/O command queue states

- [MTLIOStatusPending](pending.md) — Indicates the GPU hasn’t finished executing the input/output command buffer.
- [MTLIOStatusComplete](complete.md) — Indicates the GPU has successfully finished executing the input/output command buffer.
- [MTLIOStatusError](error.md) — Indicates the GPU experienced a problem with the input/output command buffer.
