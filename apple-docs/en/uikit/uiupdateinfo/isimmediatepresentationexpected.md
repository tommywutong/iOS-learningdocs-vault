---
title: isImmediatePresentationExpected
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateinfo/isimmediatepresentationexpected
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateinfo/isimmediatepresentationexpected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateinfo/isimmediatepresentationexpected.json'
content_hash: 'sha256:6ccc6744984dc135'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateInfo](../uiupdateinfo.md)

# isImmediatePresentationExpected

<sub>Instance Property</sub>

A Boolean value that indicates whether the system presents UI updates immediately upon completion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isImmediatePresentationExpected: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when the system presents UI updates immediately upon completion. Use this information to determine whether to minimize the complexity of the code you run during the UI update. Defer any processing that isn’t critical for the current UI update until after the UI update finishes.

This value can change during the UI update.

## See Also

### Working with low-latency updates

- [lowLatencyEventDispatchConfirmed](islowlatencyeventdispatchconfirmed.md) — A Boolean value that indicates whether the system runs low-latency phases for the UI update.
- [performingLowLatencyPhases](isperforminglowlatencyphases.md) — A Boolean value that indicates whether the UI update is in the low-latency phases.
