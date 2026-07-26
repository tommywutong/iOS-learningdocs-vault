---
title: AVMutableCaption
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablecaption
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecaption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecaption.json'
content_hash: 'sha256:bf540897a8f0774d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableCaption

<sub>Class</sub>

A mutable caption subclass that you use to create new captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVMutableCaption
```

## Relationships

- **Inherits From**: [AVCaption](avcaption.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Configuring text and timing

- [text](avmutablecaption/text.md) — The caption text.
- [timeRange](avmutablecaption/timerange.md) — The time range over which the system presents the caption.

### Configuring the region

- [region](avmutablecaption/region.md) — The region in which the caption exists.

### Configuring font styles

- [FontStyle](avcaption/fontstyle.md) — Font styles for caption text.
- [setFontStyle(_:in:)](<avmutablecaption/setfontstyle(__in_).md>) — Sets the font style for a range of text.
- [removeFontStyle(in:)](<avmutablecaption/removefontstyle(in_).md>) — Removes a font style from a range of text.
- [FontWeight](avcaption/fontweight.md) — Font weights for a caption.
- [setFontWeight(_:in:)](<avmutablecaption/setfontweight(__in_).md>) — Sets the font weight for a range of text.
- [removeFontWeight(in:)](<avmutablecaption/removefontweight(in_).md>) — Removes a font weight from a range of text.
- [Decoration](avcaption/decoration.md) — Text decorations for caption text.
- [setDecoration(_:in:)](<avmutablecaption/setdecoration(__in_).md>) — Sets a decoration for a range of text.
- [removeDecoration(in:)](<avmutablecaption/removedecoration(in_).md>) — Removes a decoration from a range of text.

### Configuring colors

- [setTextColor(_:in:)](<avmutablecaption/settextcolor(__in_).md>) — Sets the text color for a range of text.
- [removeTextColor(in:)](<avmutablecaption/removetextcolor(in_).md>) — Removes the text color for a range of text.
- [setBackgroundColor(_:in:)](<avmutablecaption/setbackgroundcolor(__in_).md>) — Sets the background color for a range of text.
- [removeBackgroundColor(in:)](<avmutablecaption/removebackgroundcolor(in_).md>) — Removes a background color from a range of text.

### Configuring alignment

- [textAlignment](avmutablecaption/textalignment.md) — The alignment of the caption text.
- [TextAlignment](avcaption/textalignment-swift.enum.md) — Text alignment options for a caption.

### Configuring animation

- [animation](avmutablecaption/animation.md) — Animations to apply to the caption text.
- [Animation](avcaption/animation-swift.enum.md) — Animation options for a caption.

### Configuring advanced typography

- [Ruby](avcaption/ruby.md) — An object that presents ruby characters.
- [setRuby(_:in:)](<avmutablecaption/setruby(__in_).md>) — Sets ruby text for a range.
- [removeRuby(in:)](<avmutablecaption/removeruby(in_).md>) — Removes ruby text from a range.
- [TextCombine](avcaption/textcombine.md) — The caption’s supported rendering policy options.
- [setTextCombine(_:in:)](<avmutablecaption/settextcombine(__in_).md>) — Sets text combine for a range.
- [removeTextCombine(in:)](<avmutablecaption/removetextcombine(in_).md>) — Removes text combine from a range.

## See Also

### Captions

- [AVCaption](avcaption.md) — An object that represents text to present over a time range.
