---
title: totalUnitCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/totalunitcount
source_url: 'https://developer.apple.com/documentation/foundation/progress/totalunitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/totalunitcount.json'
content_hash: 'sha256:e015647f78d6469f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# totalUnitCount

<sub>Instance Property</sub>

The total number of tracked units of work for the current progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var totalUnitCount: Int64 { get set }
```

## Discussion

For an [Progress](../progress.md) with a kind of [NSProgressKindFile](../progresskind/file.md), the unit of this property is bytes, and the [NSProgressFileTotalCountKey](../progressuserinfokey/filetotalcountkey.md) and [NSProgressFileCompletedCountKey](../progressuserinfokey/filecompletedcountkey.md) keys in the `userInfo` dictionary report the overall count of files.

For any other kind of [Progress](../progress.md), the unit of measurement doesn’t matter as long as it’s consistent. You can report the values to the user in the [localizedDescription](localizeddescription.md) and [localizedAdditionalDescription](localizedadditionaldescription.md).

## See Also

### Related Documentation

- [fractionCompleted](fractioncompleted.md) — The fraction of the overall work that the progress object completes, including work from its suboperations.

### Reporting Progress

- [completedUnitCount](completedunitcount.md) — The number of completed units of work for the current job.
- [localizedDescription](localizeddescription.md) — A localized description of tracked progress for the receiver.
- [localizedAdditionalDescription](localizedadditionaldescription.md) — A more specific localized description of tracked progress for the receiver.
- [cancellable](iscancellable.md) — A Boolean value that indicates whether the receiver is tracking work that you can cancel.
- [cancelled](iscancelled.md) — A Boolean value that Indicates whether the receiver is tracking canceled work.
- [cancellationHandler](cancellationhandler.md) — The block to invoke when canceling progress.
- [pausable](ispausable.md) — A Boolean value that indicates whether the receiver is tracking work that you can pause.
- [paused](ispaused.md) — A Boolean value that indicates whether the receiver is tracking paused work.
- [pausingHandler](pausinghandler.md) — The block to invoke when pausing progress.
