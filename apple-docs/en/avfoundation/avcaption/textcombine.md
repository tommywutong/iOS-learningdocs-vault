---
title: AVCaption.TextCombine
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaption/textcombine
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/textcombine'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/textcombine.json'
content_hash: 'sha256:eecdd66f5dd83b9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# AVCaption.TextCombine

<sub>Enumeration</sub>

The caption’s supported rendering policy options.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum TextCombine
```

## Overview

Text combine is a special rendering policy that combines multiple characters into one unit and presents it in upright position in a vertical text flow. This presentation achieves a horizontal-in-vertical layout (or Tate-Chu-Yoko layout), which lets the caption render a horizontal text string in vertical text.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Text combine options

- [AVCaptionTextCombineAll](textcombine/all.md) — An option that combines all of the characters.
- [AVCaptionTextCombineNone](textcombine/none.md) — An option that doesn’t combine text upright.
- [AVCaptionTextCombineOneDigit](textcombine/onedigit.md) — An option that makes one digit upright.
- [AVCaptionTextCombineTwoDigits](textcombine/twodigits.md) — An option that combines two consecutive digits.
- [AVCaptionTextCombineThreeDigits](textcombine/threedigits.md) — An option that combines three consecutive digits.
- [AVCaptionTextCombineFourDigits](textcombine/fourdigits.md) — An option that combines four consecutive digits.

### Initializers

- [init(rawValue:)](<textcombine/init(rawvalue_).md>)

## See Also

### Accessing advanced typography

- [ruby(at:)](<ruby(at_).md>) — Returns the ruby text at the index position.
- [Ruby](ruby.md) — An object that presents ruby characters.
- [textCombine(at:)](<textcombine(at_).md>) — Returns the text combine at the index position.
