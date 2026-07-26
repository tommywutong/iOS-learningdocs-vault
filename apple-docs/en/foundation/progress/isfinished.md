---
title: isFinished
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/isfinished
source_url: 'https://developer.apple.com/documentation/foundation/progress/isfinished'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/isfinished.json'
content_hash: 'sha256:289da4c9ff2a823f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# isFinished

<sub>Instance Property</sub>

A Boolean value that indicates the progress object is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFinished: Bool { get }
```

## Discussion

A progress object finishes when the [completedUnitCount](completedunitcount.md) equals or exceeds the [totalUnitCount](totalunitcount.md).

By default, [Progress](../progress.md) is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

## See Also

### Observing Progress

- [indeterminate](isindeterminate.md) — A Boolean value that indicates whether the tracked progress is indeterminate.
- [fractionCompleted](fractioncompleted.md) — The fraction of the overall work that the progress object completes, including work from its suboperations.
