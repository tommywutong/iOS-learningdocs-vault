---
title: isCancelled
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/iscancelled
source_url: 'https://developer.apple.com/documentation/foundation/thread/iscancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/iscancelled.json'
content_hash: 'sha256:27235b7dec988040'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# isCancelled

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is cancelled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancelled: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver has been cancelled, otherwise [false](../../swift/false.md).

If your thread supports cancellation, it should check this property periodically and exit if it ever returns [true](../../swift/true.md).

## See Also

### Related Documentation

- [- cancel](<cancel().md>) — Changes the cancelled state of the receiver to indicate that it should exit.

### Determining the Thread’s Execution State

- [executing](isexecuting.md) — A Boolean value that indicates whether the receiver is executing.
- [finished](isfinished.md) — A Boolean value that indicates whether the receiver has finished execution.
