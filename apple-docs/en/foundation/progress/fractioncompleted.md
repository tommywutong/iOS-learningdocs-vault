---
title: fractionCompleted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/fractioncompleted
source_url: 'https://developer.apple.com/documentation/foundation/progress/fractioncompleted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/fractioncompleted.json'
content_hash: 'sha256:c782f9f43cacb68d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# fractionCompleted

<sub>Instance Property</sub>

The fraction of the overall work that the progress object completes, including work from its suboperations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fractionCompleted: Double { get }
```

## Discussion

If the receiver object doesn’t have any suboperations, [fractionCompleted](fractioncompleted.md) is generally the result of dividing [completedUnitCount](completedunitcount.md) by [totalUnitCount](totalunitcount.md). Setting both [totalUnitCount](totalunitcount.md) and [completedUnitCount](completedunitcount.md) properties to zero indicates that there is no progress to track. In this case, the [indeterminate](isindeterminate.md) property returns [false](../../swift/false.md) and the [fractionCompleted](fractioncompleted.md) property returns `0.0`.

If the receiver does have suboperations, [fractionCompleted](fractioncompleted.md) reflects progress from those progress objects in addition to its own [completedUnitCount](completedunitcount.md). When the suboperations finish, the [completedUnitCount](completedunitcount.md) of the containing progress object updates.

## See Also

### Observing Progress

- [indeterminate](isindeterminate.md) — A Boolean value that indicates whether the tracked progress is indeterminate.
- [finished](isfinished.md) — A Boolean value that indicates the progress object is complete.
