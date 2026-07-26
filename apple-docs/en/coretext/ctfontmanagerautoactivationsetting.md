---
title: CTFontManagerAutoActivationSetting
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontmanagerautoactivationsetting
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerautoactivationsetting.json'
content_hash: 'sha256:5dc75ac3bf5b5d7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerAutoActivationSetting

<sub>Enumeration</sub>

Sets the auto-activation for the specified bundle identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTFontManagerAutoActivationSetting
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTFontManagerAutoActivationDefault](ctfontmanagerautoactivationsetting/default.md)
- [kCTFontManagerAutoActivationDisabled](ctfontmanagerautoactivationsetting/disabled.md)
- [kCTFontManagerAutoActivationEnabled](ctfontmanagerautoactivationsetting/enabled.md)
- [kCTFontManagerAutoActivationPromptUser](ctfontmanagerautoactivationsetting/promptuser.md) _(deprecated)_

### Initializers

- [init(rawValue:)](<ctfontmanagerautoactivationsetting/init(rawvalue_).md>)

## See Also

### Enumerations

- [CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md) — Constants that track the progress of font descriptor matching.
- [CTFontManagerError](ctfontmanagererror.md) — Errors that prevent unregistration of fonts for a specified font file URL.
- [CTFontManagerScope](ctfontmanagerscope.md) — Constants that define the scope for font registration.
- [CTLineBoundsOptions](ctlineboundsoptions.md) — Options for getting the bounds of a line of text.
- [CTRubyAlignment](ctrubyalignment.md) — Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [CTRubyOverhang](ctrubyoverhang.md) — Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [CTRubyPosition](ctrubyposition.md) — Constants that specify the position of the ruby text relative to to the base text.
