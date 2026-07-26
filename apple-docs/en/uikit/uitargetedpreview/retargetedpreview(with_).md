---
title: 'retargetedPreview(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitargetedpreview/retargetedpreview(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitargetedpreview/retargetedpreview(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitargetedpreview/retargetedpreview%28with%3A%29.json'
content_hash: 'sha256:f91d6843cf18135b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITargetedPreview](../uitargetedpreview.md)

# retargetedPreview(with:)

<sub>Instance Method</sub>

Returns a targeted preview object with the same view and parameters, but with a different target container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func retargetedPreview(with newTarget: UIPreviewTarget) -> UITargetedPreview
```

## Parameters

- `newTarget` — The new target for the existing view.

## Return Value

A new targeted preview object containing the specified target and the current view.
