---
title: CTFontManagerScope
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontmanagerscope
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerscope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerscope.json'
content_hash: 'sha256:85bd8fb2e29898c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerScope

<sub>Enumeration</sub>

Constants that define the scope for font registration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTFontManagerScope
```

## Overview

On macOS, a user session refers to a login session. On iOS, a user session refers to the current booted session.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTFontManagerScopeNone](ctfontmanagerscope/none.md) — No scope is defined.
- [kCTFontManagerScopeProcess](ctfontmanagerscope/process.md) — The font is available to the current process for the duration of the process unless directly unregistered.
- [kCTFontManagerScopePersistent](ctfontmanagerscope/persistent.md) — The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
- [kCTFontManagerScopeSession](ctfontmanagerscope/session.md) — The font is available to the current user session but won’t be available in subsequent sessions.
- [kCTFontManagerScopeUser](ctfontmanagerscope/user.md) — The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.

### Initializers

- [init(rawValue:)](<ctfontmanagerscope/init(rawvalue_).md>)

## See Also

### Enumerations

- [CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md) — Constants that track the progress of font descriptor matching.
- [CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md) — Sets the auto-activation for the specified bundle identifier.
- [CTFontManagerError](ctfontmanagererror.md) — Errors that prevent unregistration of fonts for a specified font file URL.
- [CTLineBoundsOptions](ctlineboundsoptions.md) — Options for getting the bounds of a line of text.
- [CTRubyAlignment](ctrubyalignment.md) — Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [CTRubyOverhang](ctrubyoverhang.md) — Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [CTRubyPosition](ctrubyposition.md) — Constants that specify the position of the ruby text relative to to the base text.
