---
title: AVCaption
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaption
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption.json'
content_hash: 'sha256:172bfe13c0a5123d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaption

<sub>Class</sub>

An object that represents text to present over a time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaption
```

## Overview

A caption contains a cue, which is a single sentence or paragraph of text for a time range in the video timeline. Within the active range, the caption may animate (for example, Karaoke lyrics) by rolling-up, changing visibility, or using other dynamic styling.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMutableCaption](avmutablecaption.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a caption

- [- initWithText:timeRange:](<avcaption/init(__timerange_).md>) — Creates a caption that contains text and a time range.

### Accessing text and timing

- [text](avcaption/text.md) — The caption text.
- [timeRange](avcaption/timerange.md) — The time range over which the system presents the caption.

### Accessing the region

- [region](avcaption/region.md) — The region in which the caption exists.

### Accessing font styles

- [fontStyle(at:)](<avcaption/fontstyle(at_).md>) — Returns the font style and range at the index position.
- [FontStyle](avcaption/fontstyle.md) — Font styles for caption text.
- [fontWeight(at:)](<avcaption/fontweight(at_).md>) — Returns the font weight and range at the index position.
- [FontWeight](avcaption/fontweight.md) — Font weights for a caption.
- [decoration(at:)](<avcaption/decoration(at_).md>) — Returns the text decoration at the index position.
- [Decoration](avcaption/decoration.md) — Text decorations for caption text.

### Accessing colors

- [textColor(at:)](<avcaption/textcolor(at_).md>) — Returns the text color at the index position.
- [backgroundColor(at:)](<avcaption/backgroundcolor(at_).md>) — Returns the background color at the index position.

### Accessing alignment

- [textAlignment](avcaption/textalignment-swift.property.md) — The alignment for the caption text.
- [TextAlignment](avcaption/textalignment-swift.enum.md) — Text alignment options for a caption.

### Accessing animation

- [animation](avcaption/animation-swift.property.md) — The animation that the system applies to this caption.
- [Animation](avcaption/animation-swift.enum.md) — Animation options for a caption.

### Accessing advanced typography

- [ruby(at:)](<avcaption/ruby(at_).md>) — Returns the ruby text at the index position.
- [Ruby](avcaption/ruby.md) — An object that presents ruby characters.
- [textCombine(at:)](<avcaption/textcombine(at_).md>) — Returns the text combine at the index position.
- [TextCombine](avcaption/textcombine.md) — The caption’s supported rendering policy options.

### Initializers

- [init(coder:)](<avcaption/init(coder_).md>)
- [init(text:timeRange:)](<avcaption/init(text_timerange_).md>)

## See Also

### Captions

- [AVMutableCaption](avmutablecaption.md) — A mutable caption subclass that you use to create new captions.
