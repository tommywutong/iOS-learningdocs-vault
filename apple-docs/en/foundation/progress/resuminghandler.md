---
title: resumingHandler
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/resuminghandler
source_url: 'https://developer.apple.com/documentation/foundation/progress/resuminghandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/resuminghandler.json'
content_hash: 'sha256:58ce239e449d639e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# resumingHandler

<sub>Instance Property</sub>

The block to invoke when progress resumes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resumingHandler: (@Sendable () -> Void)? { get set }
```

## Discussion

If the receiver is a suboperation of another progress object, the system invokes the [resumingHandler](resuminghandler.md) block when pausing the containing progress object.

### Special Considerations

You’re responsible for resuming any work for the progress object.

You can invoke the resuming handler on any queue. If you must do work on a specific queue, dispatch to that queue from within the resuming handler block.

## See Also

### Controlling Progress

- [- cancel](<cancel().md>) — Cancels progress tracking.
- [- pause](<pause().md>) — Pauses progress tracking.
- [- resume](<resume().md>) — Resumes progress tracking.
