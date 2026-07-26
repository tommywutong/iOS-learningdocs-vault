---
title: observedProgress
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprogressview/observedprogress
source_url: 'https://developer.apple.com/documentation/uikit/uiprogressview/observedprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprogressview/observedprogress.json'
content_hash: 'sha256:5f2508421111339b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIProgressView](../uiprogressview.md)

# observedProgress

<sub>Instance Property</sub>

The progress object to use for updating the progress view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var observedProgress: Progress? { get set }
```

## Discussion

When this property is set, the progress view updates its progress value automatically using information it receives from the [Progress](../../foundation/progress.md) object. (Progress updates are animated.) Set the property to `nil` when you want to update the progress manually. The default value of this property is `nil`.

For more information about configuring a progress object to manage progress information, see [Progress](../../foundation/progress.md).

## See Also

### Managing the progress bar

- [progress](progress.md) — The current progress of the progress view.
- [- setProgress:animated:](<setprogress(__animated_).md>) — Adjusts the current progress of the progress view, optionally animating the change.
