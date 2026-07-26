---
title: completionDeadlineTime
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateinfo/completiondeadlinetime
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateinfo/completiondeadlinetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateinfo/completiondeadlinetime.json'
content_hash: 'sha256:c22dcd0ff9b8d3a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateInfo](../uiupdateinfo.md)

# completionDeadlineTime

<sub>Instance Property</sub>

The time interval that represents the time by which an app needs to finish submitting changes to the render server.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var completionDeadlineTime: TimeInterval { get }
```

## Discussion

Missing this completion deadline results in a presentation delay.

## See Also

### Getting information about timing

- [modelTime](modeltime.md) — The time interval that represents a reference point for the current time of the UI update.
- [estimatedPresentationTime](estimatedpresentationtime.md) — The time interval that represents an estimate for when current UI update changes become visible onscreen.
