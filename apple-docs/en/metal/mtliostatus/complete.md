---
title: MTLIOStatus.complete
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliostatus/complete
source_url: 'https://developer.apple.com/documentation/metal/mtliostatus/complete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliostatus/complete.json'
content_hash: 'sha256:7b0f9a5c0a184deb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOStatus](../mtliostatus.md)

# MTLIOStatus.complete

<sub>Case</sub>

Indicates the GPU has successfully finished executing the input/output command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case complete
```

## See Also

### I/O command queue states

- [MTLIOStatusPending](pending.md) — Indicates the GPU hasn’t finished executing the input/output command buffer.
- [MTLIOStatusCancelled](cancelled.md) — Indicates the GPU has successfully abandoned the input/output command buffer.
- [MTLIOStatusError](error.md) — Indicates the GPU experienced a problem with the input/output command buffer.
