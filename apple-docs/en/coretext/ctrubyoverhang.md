---
title: CTRubyOverhang
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrubyoverhang
source_url: 'https://developer.apple.com/documentation/coretext/ctrubyoverhang'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrubyoverhang.json'
content_hash: 'sha256:718b3560690a4d2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRubyOverhang

<sub>Enumeration</sub>

Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTRubyOverhang
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTRubyOverhangAuto](ctrubyoverhang/auto.md) — The ruby text can overhang adjacent text on both sides.
- [kCTRubyOverhangStart](ctrubyoverhang/start.md) — The ruby text can overhang the text that precedes it.
- [kCTRubyOverhangEnd](ctrubyoverhang/end.md) — The ruby text can overhang the text that follows it.
- [kCTRubyOverhangNone](ctrubyoverhang/none.md) — The ruby text can’t overhang the preceding or following text.
- [kCTRubyOverhangInvalid](ctrubyoverhang/invalid.md) — The overhang specification is invalid.

### Initializers

- [init(rawValue:)](<ctrubyoverhang/init(rawvalue_).md>)

## See Also

### Enumerations

- [CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md) — Constants that track the progress of font descriptor matching.
- [CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md) — Sets the auto-activation for the specified bundle identifier.
- [CTFontManagerError](ctfontmanagererror.md) — Errors that prevent unregistration of fonts for a specified font file URL.
- [CTFontManagerScope](ctfontmanagerscope.md) — Constants that define the scope for font registration.
- [CTLineBoundsOptions](ctlineboundsoptions.md) — Options for getting the bounds of a line of text.
- [CTRubyAlignment](ctrubyalignment.md) — Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [CTRubyPosition](ctrubyposition.md) — Constants that specify the position of the ruby text relative to to the base text.
