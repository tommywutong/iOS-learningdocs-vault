---
title: AVCaption.Ruby
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaption/ruby
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/ruby'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/ruby.json'
content_hash: 'sha256:2915c32cfba72f2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# AVCaption.Ruby

<sub>Class</sub>

An object that presents ruby characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class Ruby
```

## Overview

Ruby characters are small annotations, typically used in Japanese content, that render alongside the base text.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCoding](../../foundation/nscoding.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [NSSecureCoding](../../foundation/nssecurecoding.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Ruby text

- [- initWithText:](<ruby/init(text_).md>) — Creates ruby text.
- [- initWithText:position:alignment:](<ruby/init(text_position_alignment_).md>) — Creates ruby text with position and alignment.

### Accessing text properties

- [text](ruby/text.md) — The ruby text.
- [position](ruby/position-swift.property.md) — The ruby text position.
- [Position](ruby/position-swift.enum.md) — Constants that indicate ruby text positions.
- [alignment](ruby/alignment-swift.property.md) — The ruby text alignment.
- [Alignment](ruby/alignment-swift.enum.md) — Constants that indicate ruby text alignments.

### Initializers

- [init(coder:)](<ruby/init(coder_).md>)

## See Also

### Accessing advanced typography

- [ruby(at:)](<ruby(at_).md>) — Returns the ruby text at the index position.
- [textCombine(at:)](<textcombine(at_).md>) — Returns the text combine at the index position.
- [TextCombine](textcombine.md) — The caption’s supported rendering policy options.
