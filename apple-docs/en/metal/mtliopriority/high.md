---
title: MTLIOPriority.high
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliopriority/high
source_url: 'https://developer.apple.com/documentation/metal/mtliopriority/high'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliopriority/high.json'
content_hash: 'sha256:d79a87f6b25fe94f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOPriority](../mtliopriority.md)

# MTLIOPriority.high

<sub>Case</sub>

Sets a new input/output command queue’s priority to a high priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case high
```

## Discussion

Create a command queue with a high priority to load important assets or those your app needs quickly. For example, a game that plays sound effects that match its animations can load its audio assets with low latency with a high priority queue.

## See Also

### I/O command queue priorities

- [MTLIOPriorityNormal](normal.md) — Designates the normal priority for a new input/output command queue.
- [MTLIOPriorityLow](low.md) — Designates the low priority for a new input/output command queue.
