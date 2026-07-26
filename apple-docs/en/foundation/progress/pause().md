---
title: pause()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/pause()
source_url: 'https://developer.apple.com/documentation/foundation/progress/pause()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/pause%28%29.json'
content_hash: 'sha256:5d5607dd5a9f0988'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# pause()

<sub>Instance Method</sub>

Pauses progress tracking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pause()
```

## Discussion

This method invokes the block for [pausingHandler](pausinghandler.md), if there is one, and ensures that any subsequent reads of the [paused](ispaused.md) property return [true](../../swift/true.md).

If the receiver has suboperations, the system pauses their progress as well.

## See Also

### Controlling Progress

- [- cancel](<cancel().md>) — Cancels progress tracking.
- [- resume](<resume().md>) — Resumes progress tracking.
- [resumingHandler](resuminghandler.md) — The block to invoke when progress resumes.
