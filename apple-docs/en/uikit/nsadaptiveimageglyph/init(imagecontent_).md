---
title: 'init(imageContent:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsadaptiveimageglyph/init(imagecontent:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph/init(imagecontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsadaptiveimageglyph/init%28imagecontent%3A%29.json'
content_hash: 'sha256:a7076bb2f6b933c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSAdaptiveImageGlyph](../nsadaptiveimageglyph.md)

# init(imageContent:)

<sub>Initializer</sub>

Create an adaptive image glyph from previously saved data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(imageContent: Data)
```

## Parameters

- `imageContent` — The raw image data you obtained previously from an adaptive image glyph. Typically, you receive adaptive images from the text system, store their data with the rest of your content, and use the data to recreate the adaptive image later.

## Return Value

A new adaptive image glyph with the identifier and details from the image data.

## Discussion

Use this initializer to create an adaptive image glyph from data you previously saved.

## See Also

### Creating an adaptive image glyph

- [- initWithCoder:](<init(coder_).md>)
