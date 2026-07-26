---
title: CTRubyPosition
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrubyposition
source_url: 'https://developer.apple.com/documentation/coretext/ctrubyposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrubyposition.json'
content_hash: 'sha256:cfdaf6eb266f0d68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRubyPosition

<sub>Enumeration</sub>

Constants that specify the position of the ruby text relative to to the base text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTRubyPosition
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTRubyPositionBefore](ctrubyposition/before.md) — The ruby text is positioned before the base text, appearing above horizontal text and to the right of vertical text.
- [kCTRubyPositionAfter](ctrubyposition/after.md) — The ruby text is positioned after the base text, appearing below horizontal text and to the left of vertical text.
- [kCTRubyPositionInterCharacter](ctrubyposition/intercharacter.md) — The ruby text is positioned to the right of the base text, regardless of whether it’s horizontal or vertical.
- [kCTRubyPositionInline](ctrubyposition/inline.md) — The ruby text follows the base text with no special styling.
- [kCTRubyPositionCount](ctrubyposition/count.md) — A constant that accounts for all ruby positions during ruby annotation creation.

### Initializers

- [init(rawValue:)](<ctrubyposition/init(rawvalue_).md>)

## See Also

### Enumerations

- [CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md) — Constants that track the progress of font descriptor matching.
- [CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md) — Sets the auto-activation for the specified bundle identifier.
- [CTFontManagerError](ctfontmanagererror.md) — Errors that prevent unregistration of fonts for a specified font file URL.
- [CTFontManagerScope](ctfontmanagerscope.md) — Constants that define the scope for font registration.
- [CTLineBoundsOptions](ctlineboundsoptions.md) — Options for getting the bounds of a line of text.
- [CTRubyAlignment](ctrubyalignment.md) — Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [CTRubyOverhang](ctrubyoverhang.md) — Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
