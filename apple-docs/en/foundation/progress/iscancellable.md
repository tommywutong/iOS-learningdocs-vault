---
title: isCancellable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/iscancellable
source_url: 'https://developer.apple.com/documentation/foundation/progress/iscancellable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/iscancellable.json'
content_hash: 'sha256:6ed37e93ec8fa1f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# isCancellable

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is tracking work that you can cancel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancellable: Bool { get set }
```

## Discussion

By default, [Progress](../progress.md) objects are cancelable.

You typically use this property to communicate whether controls for canceling appear in a progress-reporting user interface. [Progress](../progress.md) itself doesn’t do anything with this property other than help pass the value from progress reporters to progress observers.

If an [Progress](../progress.md) is cancelable, implement the ability to cancel progress either by setting a block for the [cancellationHandler](cancellationhandler.md) property, or by polling the [cancelled](iscancelled.md) property periodically while performing the relevant work.

It’s valid for the value of this property to change during the lifetime of an [Progress](../progress.md) object. By default, [Progress](../progress.md) is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

## See Also

### Related Documentation

- [- cancel](<cancel().md>) — Cancels progress tracking.

### Reporting Progress

- [totalUnitCount](totalunitcount.md) — The total number of tracked units of work for the current progress.
- [completedUnitCount](completedunitcount.md) — The number of completed units of work for the current job.
- [localizedDescription](localizeddescription.md) — A localized description of tracked progress for the receiver.
- [localizedAdditionalDescription](localizedadditionaldescription.md) — A more specific localized description of tracked progress for the receiver.
- [cancelled](iscancelled.md) — A Boolean value that Indicates whether the receiver is tracking canceled work.
- [cancellationHandler](cancellationhandler.md) — The block to invoke when canceling progress.
- [pausable](ispausable.md) — A Boolean value that indicates whether the receiver is tracking work that you can pause.
- [paused](ispaused.md) — A Boolean value that indicates whether the receiver is tracking paused work.
- [pausingHandler](pausinghandler.md) — The block to invoke when pausing progress.
