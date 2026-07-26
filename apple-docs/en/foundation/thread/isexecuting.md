---
title: isExecuting
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/isexecuting
source_url: 'https://developer.apple.com/documentation/foundation/thread/isexecuting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/isexecuting.json'
content_hash: 'sha256:4eb86f6cdd75b7bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# isExecuting

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isExecuting: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver is executing, otherwise [false](../../swift/false.md).

## See Also

### Determining the Thread’s Execution State

- [finished](isfinished.md) — A Boolean value that indicates whether the receiver has finished execution.
- [cancelled](iscancelled.md) — A Boolean value that indicates whether the receiver is cancelled.
