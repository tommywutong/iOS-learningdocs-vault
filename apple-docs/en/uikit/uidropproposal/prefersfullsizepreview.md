---
title: prefersFullSizePreview
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropproposal/prefersfullsizepreview
source_url: 'https://developer.apple.com/documentation/uikit/uidropproposal/prefersfullsizepreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropproposal/prefersfullsizepreview.json'
content_hash: 'sha256:3e1b99fea90e05b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropProposal](../uidropproposal.md)

# prefersFullSizePreview

<sub>Instance Property</sub>

A Boolean value that indicates that the drag item preview should be shown at its full, original size.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var prefersFullSizePreview: Bool { get set }
```

## Discussion

Set [prefersFullSizePreview](prefersfullsizepreview.md) to [true](../../swift/true.md) to show the preview at its original size, not scaled down to a smaller size. For example, you might set this property to [true](../../swift/true.md) when the user moves items from a nearby view and scaling down the preview is distracting.

This property applies only to drag and drop activities performed within the same app.

## See Also

### Configuring a drop proposal

- [precise](isprecise.md) — A Boolean value that proposes that the drop interaction define the drop location precisely, such as at a specific point within existing text.
