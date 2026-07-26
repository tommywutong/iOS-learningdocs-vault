---
title: estimatedPresentationTime
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateinfo/estimatedpresentationtime
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateinfo/estimatedpresentationtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateinfo/estimatedpresentationtime.json'
content_hash: 'sha256:25ec43a8c2e6a0b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateInfo](../uiupdateinfo.md)

# estimatedPresentationTime

<sub>Instance Property</sub>

The time interval that represents an estimate for when current UI update changes become visible onscreen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var estimatedPresentationTime: TimeInterval { get }
```

## Discussion

This time is an estimate, so the actual time when changes become visible might differ.

## See Also

### Getting information about timing

- [modelTime](modeltime.md) — The time interval that represents a reference point for the current time of the UI update.
- [completionDeadlineTime](completiondeadlinetime.md) — The time interval that represents the time by which an app needs to finish submitting changes to the render server.
