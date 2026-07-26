---
title: 'setDecoration(_:in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecaption/setdecoration(_:in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecaption/setdecoration(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecaption/setdecoration%28_%3Ain%3A%29.json'
content_hash: 'sha256:8d228e56314534c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCaption](../avmutablecaption.md)

# setDecoration(_:in:)

<sub>Instance Method</sub>

Sets a decoration for a range of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func setDecoration(_ decoration: AVCaption.Decoration, in range: NSRange)
```

## Parameters

- `decoration` — The decoration.

- `range` — The range to which this decoration applies.

## See Also

### Configuring font styles

- [FontStyle](../avcaption/fontstyle.md) — Font styles for caption text.
- [setFontStyle(_:in:)](<setfontstyle(__in_).md>) — Sets the font style for a range of text.
- [removeFontStyle(in:)](<removefontstyle(in_).md>) — Removes a font style from a range of text.
- [FontWeight](../avcaption/fontweight.md) — Font weights for a caption.
- [setFontWeight(_:in:)](<setfontweight(__in_).md>) — Sets the font weight for a range of text.
- [removeFontWeight(in:)](<removefontweight(in_).md>) — Removes a font weight from a range of text.
- [Decoration](../avcaption/decoration.md) — Text decorations for caption text.
- [removeDecoration(in:)](<removedecoration(in_).md>) — Removes a decoration from a range of text.
