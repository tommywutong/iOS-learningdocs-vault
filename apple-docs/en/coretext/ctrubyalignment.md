---
title: CTRubyAlignment
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrubyalignment
source_url: 'https://developer.apple.com/documentation/coretext/ctrubyalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrubyalignment.json'
content_hash: 'sha256:0e59416bef98f715'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRubyAlignment

<sub>Enumeration</sub>

Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTRubyAlignment
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTRubyAlignmentAuto](ctrubyalignment/auto.md) — Core Text automatically determines the alignment.
- [kCTRubyAlignmentStart](ctrubyalignment/start.md) — Aligns the ruby text with the starting edge of the base text.
- [kCTRubyAlignmentCenter](ctrubyalignment/center.md) — Centers the ruby text within the width of the base text.
- [kCTRubyAlignmentEnd](ctrubyalignment/end.md) — Aligns the ruby text with the ending edge of the base text.
- [kCTRubyAlignmentDistributeLetter](ctrubyalignment/distributeletter.md) — Distributes the ruby text evenly over the width of the base text, aligning the first and last characters of the ruby text with the first and last characters of the base text.
- [kCTRubyAlignmentDistributeSpace](ctrubyalignment/distributespace.md) — Distributes the ruby text evenly over the width of the base text, adding space before the first and after the last character.
- [kCTRubyAlignmentLineEdge](ctrubyalignment/lineedge.md) — Aligns the ruby text to an adjacent line edge.
- [kCTRubyAlignmentInvalid](ctrubyalignment/invalid.md) — The alignment is invalid.

### Initializers

- [init(rawValue:)](<ctrubyalignment/init(rawvalue_).md>)

## See Also

### Enumerations

- [CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md) — Constants that track the progress of font descriptor matching.
- [CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md) — Sets the auto-activation for the specified bundle identifier.
- [CTFontManagerError](ctfontmanagererror.md) — Errors that prevent unregistration of fonts for a specified font file URL.
- [CTFontManagerScope](ctfontmanagerscope.md) — Constants that define the scope for font registration.
- [CTLineBoundsOptions](ctlineboundsoptions.md) — Options for getting the bounds of a line of text.
- [CTRubyOverhang](ctrubyoverhang.md) — Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [CTRubyPosition](ctrubyposition.md) — Constants that specify the position of the ruby text relative to to the base text.
