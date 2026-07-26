---
title: stripTextColorFromPreviews
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdragoptions/striptextcolorfrompreviews
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragoptions/striptextcolorfrompreviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragoptions/striptextcolorfrompreviews.json'
content_hash: 'sha256:731814ddcf7efda6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragOptions](../uitextdragoptions.md)

# stripTextColorFromPreviews

<sub>Type Property</sub>

Strips the foreground and background colors for a system-provided text drag preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var stripTextColorFromPreviews: UITextDragOptions { get }
```

## Discussion

When the system creates a preview for a text drag operation, the preview keeps the foreground and background text colors. Using the [UITextDragOptionStripTextColorFromPreviews](striptextcolorfrompreviews.md) option strips away those colors, leaving the preview with black text on a clear background. This option changes only the preview, not the view used to create the preview. Also, this option doesn’t affect any images included in the preview.
