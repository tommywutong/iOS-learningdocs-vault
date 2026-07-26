---
title: resume()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/resume()
source_url: 'https://developer.apple.com/documentation/foundation/progress/resume()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/resume%28%29.json'
content_hash: 'sha256:5733c9e0541c0ba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# resume()

<sub>Instance Method</sub>

Resumes progress tracking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume()
```

## Discussion

This method invokes the block for [resumingHandler](resuminghandler.md), if there is one, and ensures that any subsequent reads of the [paused](ispaused.md) property return [false](../../swift/false.md).

If the receiver has suboperations, the system resumes their progress as well.

## See Also

### Controlling Progress

- [- cancel](<cancel().md>) — Cancels progress tracking.
- [- pause](<pause().md>) — Pauses progress tracking.
- [resumingHandler](resuminghandler.md) — The block to invoke when progress resumes.
