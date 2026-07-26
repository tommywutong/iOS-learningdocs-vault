---
title: 'attachmentBounds(for:proposedLineFragment:glyphPosition:characterIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachmentcontainer/attachmentbounds(for:proposedlinefragment:glyphposition:characterindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentcontainer/attachmentbounds(for:proposedlinefragment:glyphposition:characterindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentcontainer/attachmentbounds%28for%3Aproposedlinefragment%3Aglyphposition%3Acharacterindex%3A%29.json'
content_hash: 'sha256:61bdd6a5b0d9e228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentContainer](../nstextattachmentcontainer.md)

# attachmentBounds(for:proposedLineFragment:glyphPosition:characterIndex:)

<sub>Instance Method</sub>

Returns the layout bounds of the text attachment to the layout manager.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func attachmentBounds(for textContainer: NSTextContainer?, proposedLineFragment lineFrag: CGRect, glyphPosition position: CGPoint, characterIndex charIndex: Int) -> CGRect
```

## Parameters

- `textContainer` — The text container for the text being laid out.

- `lineFrag` — The line fragment containing the text attachment.

- `position` — The glyph location inside `lineFrag` which is the origin of the returned bounds rectangle.

- `charIndex` — The character location inside the text storage for the attachment character.

## Return Value

The [bounds](../nstextattachment/bounds.md) rectangle of the text attachment if not [CGRectZero](../../coregraphics/cgrectzero.md); otherwise, the rectangle of the [size](../uiimage/size.md) property of the attachment’s [image](../nstextattachment/image.md) property.

## Discussion

Conforming objects can implement more sophisticated logic for negotiating the attachment bounds based on the available container space and proposed line fragment rectangle.
