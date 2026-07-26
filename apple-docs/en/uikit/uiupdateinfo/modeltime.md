---
title: modelTime
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateinfo/modeltime
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateinfo/modeltime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateinfo/modeltime.json'
content_hash: 'sha256:7db85f95a5d97b5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateInfo](../uiupdateinfo.md)

# modelTime

<sub>Instance Property</sub>

The time interval that represents a reference point for the current time of the UI update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var modelTime: TimeInterval { get }
```

## Discussion

This time provides a reference point for driving time-based model changes, like animations or physics. This property attempts to maintain constant latency between model changes and their onscreen presentation. It uses the same units as [CACurrentMediaTime()](<../../quartzcore/cacurrentmediatime().md>). Numerically, this time is close to the start of the UI update, but its precise relation to the UI update start time might change, depending on frame rate and other UI update parameters.

## See Also

### Getting information about timing

- [completionDeadlineTime](completiondeadlinetime.md) — The time interval that represents the time by which an app needs to finish submitting changes to the render server.
- [estimatedPresentationTime](estimatedpresentationtime.md) — The time interval that represents an estimate for when current UI update changes become visible onscreen.
