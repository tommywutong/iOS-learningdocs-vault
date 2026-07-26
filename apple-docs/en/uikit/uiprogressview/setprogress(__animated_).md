---
title: 'setProgress(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprogressview/setprogress(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprogressview/setprogress(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprogressview/setprogress%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:b7cd9978ad476f79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIProgressView](../uiprogressview.md)

# setProgress(_:animated:)

<sub>Instance Method</sub>

Adjusts the current progress of the progress view, optionally animating the change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setProgress(_ progress: Float, animated: Bool)
```

## Parameters

- `progress` — The new progress value.

- `animated` — [true](../../swift/true.md) if the change should be animated, [false](../../swift/false.md) if the change should happen immediately.

## Discussion

The current progress is represented by a floating-point value between 0.0 and 1.0, inclusive, where 1.0 indicates the completion of the task. The default value is 0.0. Values less than 0.0 and greater than 1.0 are pinned to those limits.

## See Also

### Managing the progress bar

- [progress](progress.md) — The current progress of the progress view.
- [observedProgress](observedprogress.md) — The progress object to use for updating the progress view.
