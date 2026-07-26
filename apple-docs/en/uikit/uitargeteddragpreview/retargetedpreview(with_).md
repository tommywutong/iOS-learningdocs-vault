---
title: 'retargetedPreview(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitargeteddragpreview/retargetedpreview(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitargeteddragpreview/retargetedpreview(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitargeteddragpreview/retargetedpreview%28with%3A%29.json'
content_hash: 'sha256:aa81170e54ac3324'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITargetedDragPreview](../uitargeteddragpreview.md)

# retargetedPreview(with:)

<sub>Instance Method</sub>

Returns a new targeted drag item preview based on an existing one, but with a new geometric target.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func retargetedPreview(with newTarget: UIDragPreviewTarget) -> UITargetedDragPreview
```

## Parameters

- `newTarget` — A new drag item preview target.

## Return Value

A new targeted drag preview.

## Discussion

You can use this method in the drop interaction delegate’s implementation of the [- dropInteraction:previewForDroppingItem:withDefault:](<../uidropinteractiondelegate/dropinteraction(__previewfordropping_withdefault_).md>) method to replace the current targeted drag item preview with a different one.
