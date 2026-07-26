---
title: 'insert(_:replacementRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/insert(_:replacementrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/insert(_:replacementrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/insert%28_%3Areplacementrange%3A%29.json'
content_hash: 'sha256:48eeb98d2861b4fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# insert(_:replacementRange:)

<sub>Instance Method</sub>

Inserts an adaptive image into the text at the specifed location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func insert(_ adaptiveImageGlyph: NSAdaptiveImageGlyph, replacementRange: UITextRange)
```

## Parameters

- `adaptiveImageGlyph` — The adaptive image to add to the text.

- `replacementRange` — The text range at which to insert the image.

## See Also

### Supporting adaptive images

- [supportsAdaptiveImageGlyph](supportsadaptiveimageglyph.md) — A Boolean value that indicates whether the document supports adaptive images in the input.
