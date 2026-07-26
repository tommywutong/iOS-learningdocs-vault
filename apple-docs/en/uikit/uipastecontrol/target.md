---
title: target
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipastecontrol/target
source_url: 'https://developer.apple.com/documentation/uikit/uipastecontrol/target'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipastecontrol/target.json'
content_hash: 'sha256:756e71f8822fca34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteControl](../uipastecontrol.md)

# target

<sub>Instance Property</sub>

The UI control that receives pasted content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var target: (any UIPasteConfigurationSupporting)? { get set }
```

## Discussion

For example, you can assign this property a reference to a [UITextView](../uitextview.md).
