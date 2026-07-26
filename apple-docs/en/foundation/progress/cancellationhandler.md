---
title: cancellationHandler
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/cancellationhandler
source_url: 'https://developer.apple.com/documentation/foundation/progress/cancellationhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/cancellationhandler.json'
content_hash: 'sha256:e327008cbf618b1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# cancellationHandler

<sub>Instance Property</sub>

The block to invoke when canceling progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var cancellationHandler: (@Sendable () -> Void)? { get set }
```

## Discussion

If the receiver is a suboperation of another progress object, the system invokes the [cancellationHandler](cancellationhandler.md) block when canceling the containing progress object.

### Special Considerations

You’re responsible for canceling any work for the progress object.

You can invoke the cancellation handler on any queue. If you must do work on a specific queue, dispatch to that queue from within the cancellation handler block.

## See Also

### Reporting Progress

- [totalUnitCount](totalunitcount.md) — The total number of tracked units of work for the current progress.
- [completedUnitCount](completedunitcount.md) — The number of completed units of work for the current job.
- [localizedDescription](localizeddescription.md) — A localized description of tracked progress for the receiver.
- [localizedAdditionalDescription](localizedadditionaldescription.md) — A more specific localized description of tracked progress for the receiver.
- [cancellable](iscancellable.md) — A Boolean value that indicates whether the receiver is tracking work that you can cancel.
- [cancelled](iscancelled.md) — A Boolean value that Indicates whether the receiver is tracking canceled work.
- [pausable](ispausable.md) — A Boolean value that indicates whether the receiver is tracking work that you can pause.
- [paused](ispaused.md) — A Boolean value that indicates whether the receiver is tracking paused work.
- [pausingHandler](pausinghandler.md) — The block to invoke when pausing progress.
