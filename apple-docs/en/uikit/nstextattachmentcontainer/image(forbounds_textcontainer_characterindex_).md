---
title: 'image(forBounds:textContainer:characterIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachmentcontainer/image(forbounds:textcontainer:characterindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentcontainer/image(forbounds:textcontainer:characterindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentcontainer/image%28forbounds%3Atextcontainer%3Acharacterindex%3A%29.json'
content_hash: 'sha256:9d3bb92b47b87dc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentContainer](../nstextattachmentcontainer.md)

# image(forBounds:textContainer:characterIndex:)

<sub>Instance Method</sub>

Returns the image object that the layout manager renders in the specified image bounds rectangle inside the text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func image(forBounds imageBounds: CGRect, textContainer: NSTextContainer?, characterIndex charIndex: Int) -> UIImage?
```

## Parameters

- `imageBounds` — The rectangle in which the image is laid out.

- `textContainer` — The text container in which the image is laid out.

- `charIndex` — The character location inside the text storage for the attachment character.

## Return Value

The image rendered in the bounds rectangle.

## Discussion

The method should return an image appropriate for the target rendering context derived by arguments passed into this method. The `NSTextAttachment` implementation returns the text attachment’s [image](../nstextattachment/image.md) when non-`nil`. If the image is `nil`, it returns an image based on the text attachment’s [contents](../nstextattachment/contents.md) and [fileType](../nstextattachment/filetype.md) properties.
