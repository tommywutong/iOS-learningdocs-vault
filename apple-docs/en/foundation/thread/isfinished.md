---
title: isFinished
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/isfinished
source_url: 'https://developer.apple.com/documentation/foundation/thread/isfinished'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/isfinished.json'
content_hash: 'sha256:0e0e331ea9152633'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# isFinished

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver has finished execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFinished: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver has finished execution, otherwise [false](../../swift/false.md).

## See Also

### Determining the Thread’s Execution State

- [executing](isexecuting.md) — A Boolean value that indicates whether the receiver is executing.
- [cancelled](iscancelled.md) — A Boolean value that indicates whether the receiver is cancelled.
