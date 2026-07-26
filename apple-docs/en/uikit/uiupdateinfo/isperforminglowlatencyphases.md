---
title: isPerformingLowLatencyPhases
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateinfo/isperforminglowlatencyphases
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateinfo/isperforminglowlatencyphases'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateinfo/isperforminglowlatencyphases.json'
content_hash: 'sha256:905c42b65674d545'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateInfo](../uiupdateinfo.md)

# isPerformingLowLatencyPhases

<sub>Instance Property</sub>

A Boolean value that indicates whether the UI update is in the low-latency phases.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isPerformingLowLatencyPhases: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) between the [beforeLowLatencyEventDispatch](../uiupdateactionphase/beforelowlatencyeventdispatch.md) and [afterLowLatencyCATransactionCommit](../uiupdateactionphase/afterlowlatencycatransactioncommit.md) UI update phases. Keep any code you run in this part of the UI update as minimal as possible, especially when [immediatePresentationExpected](isimmediatepresentationexpected.md) is `true`. Defer any processing that isn’t critical for the current UI update until [afterLowLatencyCATransactionCommit](../uiupdateactionphase/afterlowlatencycatransactioncommit.md).

## See Also

### Working with low-latency updates

- [immediatePresentationExpected](isimmediatepresentationexpected.md) — A Boolean value that indicates whether the system presents UI updates immediately upon completion.
- [lowLatencyEventDispatchConfirmed](islowlatencyeventdispatchconfirmed.md) — A Boolean value that indicates whether the system runs low-latency phases for the UI update.
