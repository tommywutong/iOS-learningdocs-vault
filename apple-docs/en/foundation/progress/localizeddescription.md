---
title: localizedDescription
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/localizeddescription
source_url: 'https://developer.apple.com/documentation/foundation/progress/localizeddescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/localizeddescription.json'
content_hash: 'sha256:4abb03fc84074392'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# localizedDescription

<sub>Instance Property</sub>

A localized description of tracked progress for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedDescription: String! { get set }
```

## Discussion

If you don’t specify your own custom value for this property, [Progress](../progress.md) uses the value of the [kind](kind.md) property to determine how to use the values of other properties, as well as values in the user info dictionary, to return an automatically computed string. If it fails to do that, it returns an empty string.

The `localizedDescription` represents a general description of the work the receiver tracks. Depending on the kind of progress, the completed and total unit counts, and other parameters, localized descriptions resemble the following:

- Copying 10 files…
- 30% completed
- Copying “TextEdit”…

By default, [Progress](../progress.md) is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

## See Also

### Reporting Progress

- [totalUnitCount](totalunitcount.md) — The total number of tracked units of work for the current progress.
- [completedUnitCount](completedunitcount.md) — The number of completed units of work for the current job.
- [localizedAdditionalDescription](localizedadditionaldescription.md) — A more specific localized description of tracked progress for the receiver.
- [cancellable](iscancellable.md) — A Boolean value that indicates whether the receiver is tracking work that you can cancel.
- [cancelled](iscancelled.md) — A Boolean value that Indicates whether the receiver is tracking canceled work.
- [cancellationHandler](cancellationhandler.md) — The block to invoke when canceling progress.
- [pausable](ispausable.md) — A Boolean value that indicates whether the receiver is tracking work that you can pause.
- [paused](ispaused.md) — A Boolean value that indicates whether the receiver is tracking paused work.
- [pausingHandler](pausinghandler.md) — The block to invoke when pausing progress.
