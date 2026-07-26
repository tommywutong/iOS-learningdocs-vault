---
title: cancel()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/cancel()
source_url: 'https://developer.apple.com/documentation/foundation/progress/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/cancel%28%29.json'
content_hash: 'sha256:79aa78412be4c5ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# cancel()

<sub>Instance Method</sub>

Cancels progress tracking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

This method invokes the block for [cancellationHandler](cancellationhandler.md), if there is one, and ensures that any subsequent reads of the [cancelled](iscancelled.md) property return [true](../../swift/true.md).

If the receiver has suboperations, the system cancels their progress as well.

## See Also

### Controlling Progress

- [- pause](<pause().md>) — Pauses progress tracking.
- [- resume](<resume().md>) — Resumes progress tracking.
- [resumingHandler](resuminghandler.md) — The block to invoke when progress resumes.
