---
title: supportsAdaptiveImageGlyph
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/supportsadaptiveimageglyph
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/supportsadaptiveimageglyph'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/supportsadaptiveimageglyph.json'
content_hash: 'sha256:9ae41f885bd62ee1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# supportsAdaptiveImageGlyph

<sub>Instance Property</sub>

A Boolean value that indicates whether the document supports adaptive images in the input.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var supportsAdaptiveImageGlyph: Bool { get set }
```

## Discussion

When this property is [false](../../swift/false.md), the input system doesn’t allow the text input to contain adaptive images. Set the value of this property to [true](../../swift/true.md) only if your document supports adaptive images and handles them properly. For more information, see [NSAdaptiveImageGlyph](../nsadaptiveimageglyph.md)

## See Also

### Supporting adaptive images

- [- insertAdaptiveImageGlyph:replacementRange:](<insert(__replacementrange_).md>) — Inserts an adaptive image into the text at the specifed location.
