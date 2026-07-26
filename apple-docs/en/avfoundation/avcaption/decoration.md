---
title: AVCaption.Decoration
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaption/decoration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/decoration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/decoration.json'
content_hash: 'sha256:436e39835ed5a3d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# AVCaption.Decoration

<sub>Structure</sub>

Text decorations for caption text.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
struct Decoration
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Decorations

- [AVCaptionDecorationUnderline](decoration/underline.md) — A decoration representing a line under the text.
- [AVCaptionDecorationLineThrough](decoration/linethrough.md) — A decoration representing a line through the text.
- [AVCaptionDecorationOverline](decoration/overline.md) — A decoration representing a line over the text.

### Initializers

- [init(rawValue:)](<decoration/init(rawvalue_).md>) — Creates a caption decoration by using a string.

## See Also

### Accessing font styles

- [fontStyle(at:)](<fontstyle(at_).md>) — Returns the font style and range at the index position.
- [FontStyle](fontstyle.md) — Font styles for caption text.
- [fontWeight(at:)](<fontweight(at_).md>) — Returns the font weight and range at the index position.
- [FontWeight](fontweight.md) — Font weights for a caption.
- [decoration(at:)](<decoration(at_).md>) — Returns the text decoration at the index position.
