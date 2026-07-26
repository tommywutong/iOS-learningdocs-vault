---
title: isPausable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/ispausable
source_url: 'https://developer.apple.com/documentation/foundation/progress/ispausable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/ispausable.json'
content_hash: 'sha256:5e56eec3c7a2a50d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# isPausable

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is tracking work that you can pause.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPausable: Bool { get set }
```

## Discussion

By default, [Progress](../progress.md) objects aren’t pausable.

You typically use this property to communicate whether controls for pausing appear in a progress-reporting user interface. [Progress](../progress.md) itself doesn’t do anything with this property other than help pass the value from progress reporters to progress observers.

If an `NSProgress` is pausable, implement the ability to pause either by setting a block for the [pausingHandler](pausinghandler.md) property, or by polling the [paused](ispaused.md) property periodically while performing the relevant work.

It’s valid for the value of this property to change during the lifetime of an `NSProgress` object. By default, `NSProgress` is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

## See Also

### Reporting Progress

- [totalUnitCount](totalunitcount.md) — The total number of tracked units of work for the current progress.
- [completedUnitCount](completedunitcount.md) — The number of completed units of work for the current job.
- [localizedDescription](localizeddescription.md) — A localized description of tracked progress for the receiver.
- [localizedAdditionalDescription](localizedadditionaldescription.md) — A more specific localized description of tracked progress for the receiver.
- [cancellable](iscancellable.md) — A Boolean value that indicates whether the receiver is tracking work that you can cancel.
- [cancelled](iscancelled.md) — A Boolean value that Indicates whether the receiver is tracking canceled work.
- [cancellationHandler](cancellationhandler.md) — The block to invoke when canceling progress.
- [paused](ispaused.md) — A Boolean value that indicates whether the receiver is tracking paused work.
- [pausingHandler](pausinghandler.md) — The block to invoke when pausing progress.
