---
title: progress
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprogressview/progress
source_url: 'https://developer.apple.com/documentation/uikit/uiprogressview/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprogressview/progress.json'
content_hash: 'sha256:652f65422cdb3eec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIProgressView](../uiprogressview.md)

# progress

<sub>Instance Property</sub>

The current progress of the progress view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var progress: Float { get set }
```

## Discussion

The current progress is represented by a floating-point value between 0.0 and 1.0, inclusive, where 1.0 indicates the completion of the task. The default value is 0.0. Values less than 0.0 and greater than 1.0 are pinned to those limits.

## See Also

### Managing the progress bar

- [- setProgress:animated:](<setprogress(__animated_).md>) — Adjusts the current progress of the progress view, optionally animating the change.
- [observedProgress](observedprogress.md) — The progress object to use for updating the progress view.
