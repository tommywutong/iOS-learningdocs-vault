---
title: CTFontDescriptorMatchingState
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontdescriptormatchingstate
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptormatchingstate.json'
content_hash: 'sha256:b6f64b97eac7af42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorMatchingState

<sub>Enumeration</sub>

Constants that track the progress of font descriptor matching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTFontDescriptorMatchingState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTFontDescriptorMatchingDidBegin](ctfontdescriptormatchingstate/didbegin.md) — A state that indicates matching is about to begin.
- [kCTFontDescriptorMatchingDidFinish](ctfontdescriptormatchingstate/didfinish.md) — A state that indicates matching is done.
- [kCTFontDescriptorMatchingWillBeginQuerying](ctfontdescriptormatchingstate/willbeginquerying.md) — A state that indicates communication with the server is about to begin.
- [kCTFontDescriptorMatchingStalled](ctfontdescriptormatchingstate/stalled.md) — A state that indicates that matching is stalled, such as while waiting for a server response.
- [kCTFontDescriptorMatchingWillBeginDownloading](ctfontdescriptormatchingstate/willbegindownloading.md) — A state that indicates downloading is about to begin.
- [kCTFontDescriptorMatchingDownloading](ctfontdescriptormatchingstate/downloading.md) — A state that indicates downloading is in progress.
- [kCTFontDescriptorMatchingDidFinishDownloading](ctfontdescriptormatchingstate/didfinishdownloading.md) — A state that indicates downloading is done.
- [kCTFontDescriptorMatchingDidMatch](ctfontdescriptormatchingstate/didmatch.md) — A state that indicates the font descriptor match is successful.
- [kCTFontDescriptorMatchingDidFailWithError](ctfontdescriptormatchingstate/didfailwitherror.md) — A state that indicates an error.

### Initializers

- [init(rawValue:)](<ctfontdescriptormatchingstate/init(rawvalue_).md>)

## See Also

### Enumerations

- [CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md) — Sets the auto-activation for the specified bundle identifier.
- [CTFontManagerError](ctfontmanagererror.md) — Errors that prevent unregistration of fonts for a specified font file URL.
- [CTFontManagerScope](ctfontmanagerscope.md) — Constants that define the scope for font registration.
- [CTLineBoundsOptions](ctlineboundsoptions.md) — Options for getting the bounds of a line of text.
- [CTRubyAlignment](ctrubyalignment.md) — Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [CTRubyOverhang](ctrubyoverhang.md) — Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [CTRubyPosition](ctrubyposition.md) — Constants that specify the position of the ruby text relative to to the base text.
