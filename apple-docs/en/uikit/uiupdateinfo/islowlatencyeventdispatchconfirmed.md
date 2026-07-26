---
title: isLowLatencyEventDispatchConfirmed
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateinfo/islowlatencyeventdispatchconfirmed
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateinfo/islowlatencyeventdispatchconfirmed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateinfo/islowlatencyeventdispatchconfirmed.json'
content_hash: 'sha256:65ece2adbc2e4f91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateInfo](../uiupdateinfo.md)

# isLowLatencyEventDispatchConfirmed

<sub>Instance Property</sub>

A Boolean value that indicates whether the system runs low-latency phases for the UI update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isLowLatencyEventDispatchConfirmed: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when the system runs low-latency event dispatch during the UI update. Use this information to determine whether to avoid doing the same work more than once. For example, when considering whether to render a pencil-drawing stroke in [afterEventDispatch](../uiupdateactionphase/aftereventdispatch.md), if this property is `true`, but [performingLowLatencyPhases](isperforminglowlatencyphases.md) is `false`, you might consider waiting until after low-latency event dispatch to render the stroke.

This value can change from `false` to `true` during the UI update, but not from `true` to `false`.

> [!important] Important
> Checking the value of this property can cause the system to commit to low-latency event dispatch unnecessarily. Check this property only when you have an intention to act on its value.

## See Also

### Working with low-latency updates

- [immediatePresentationExpected](isimmediatepresentationexpected.md) — A Boolean value that indicates whether the system presents UI updates immediately upon completion.
- [performingLowLatencyPhases](isperforminglowlatencyphases.md) — A Boolean value that indicates whether the UI update is in the low-latency phases.
