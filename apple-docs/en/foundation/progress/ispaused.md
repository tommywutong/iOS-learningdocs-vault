---
title: isPaused
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/ispaused
source_url: 'https://developer.apple.com/documentation/foundation/progress/ispaused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/ispaused.json'
content_hash: 'sha256:6abe2be2ef8e9d42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# isPaused

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is tracking paused work.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPaused: Bool { get }
```

## Discussion

By default, `NSProgress` is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

If the receiver has a paused containing progress object, the receiver reports a paused status.

## See Also

### Reporting Progress

- [totalUnitCount](totalunitcount.md) — The total number of tracked units of work for the current progress.
- [completedUnitCount](completedunitcount.md) — The number of completed units of work for the current job.
- [localizedDescription](localizeddescription.md) — A localized description of tracked progress for the receiver.
- [localizedAdditionalDescription](localizedadditionaldescription.md) — A more specific localized description of tracked progress for the receiver.
- [cancellable](iscancellable.md) — A Boolean value that indicates whether the receiver is tracking work that you can cancel.
- [cancelled](iscancelled.md) — A Boolean value that Indicates whether the receiver is tracking canceled work.
- [cancellationHandler](cancellationhandler.md) — The block to invoke when canceling progress.
- [pausable](ispausable.md) — A Boolean value that indicates whether the receiver is tracking work that you can pause.
- [pausingHandler](pausinghandler.md) — The block to invoke when pausing progress.
