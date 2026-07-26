---
title: MTLIOStatus.error
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliostatus/error
source_url: 'https://developer.apple.com/documentation/metal/mtliostatus/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliostatus/error.json'
content_hash: 'sha256:faa824e75a2a5da1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOStatus](../mtliostatus.md)

# MTLIOStatus.error

<sub>Case</sub>

Indicates the GPU experienced a problem with the input/output command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case error
```

## See Also

### I/O command queue states

- [MTLIOStatusPending](pending.md) — Indicates the GPU hasn’t finished executing the input/output command buffer.
- [MTLIOStatusComplete](complete.md) — Indicates the GPU has successfully finished executing the input/output command buffer.
- [MTLIOStatusCancelled](cancelled.md) — Indicates the GPU has successfully abandoned the input/output command buffer.
