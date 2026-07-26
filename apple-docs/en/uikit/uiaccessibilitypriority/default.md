---
title: default
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitypriority/default
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitypriority/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitypriority/default.json'
content_hash: 'sha256:e50dcccedf3790f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityPriority](../uiaccessibilitypriority.md)

# default

<sub>Type Property</sub>

A default-priority announcement that interrupts existing speech, but is interruptible if a new speech utterance starts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let `default`: UIAccessibilityPriority
```

## See Also

### Choosing a priority

- [UIAccessibilityPriorityHigh](high.md) — A high-priority announcement that interrupts other speech and isn’t interruptible after it starts.
- [UIAccessibilityPriorityLow](low.md) — A low-priority announcement that the system queues and speaks after other speech utterances are complete.
