---
title: CTLineBoundsOptions
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctlineboundsoptions
source_url: 'https://developer.apple.com/documentation/coretext/ctlineboundsoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlineboundsoptions.json'
content_hash: 'sha256:077de4e8b7b7c694'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineBoundsOptions

<sub>Structure</sub>

Options for getting the bounds of a line of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTLineBoundsOptions
```

## Overview

Passing `0` (no options) returns the typographic bounds, including typographic leading and shifts.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Line Bounds Options

- [kCTLineBoundsExcludeTypographicLeading](ctlineboundsoptions/excludetypographicleading.md) — An option to exclude typographic leading.
- [kCTLineBoundsExcludeTypographicShifts](ctlineboundsoptions/excludetypographicshifts.md) — An option to ignore cross-stream shifts due to positioning, such as kerning or baseline alignment.
- [kCTLineBoundsIncludeLanguageExtents](ctlineboundsoptions/includelanguageextents.md) — An option to include additional space based on common glyph sequences for various languages.
- [kCTLineBoundsUseGlyphPathBounds](ctlineboundsoptions/useglyphpathbounds.md) — An option to use glyph path bounds rather than the default typographic bounds.
- [kCTLineBoundsUseHangingPunctuation](ctlineboundsoptions/usehangingpunctuation.md) — An option to enable hanging punctuation.
- [kCTLineBoundsUseOpticalBounds](ctlineboundsoptions/useopticalbounds.md) — An option to use optical bounds.

### Initializers

- [init(rawValue:)](<ctlineboundsoptions/init(rawvalue_).md>) — Creates a line bound options enumeration with the specified raw value.

## See Also

### Enumerations

- [CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md) — Constants that track the progress of font descriptor matching.
- [CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md) — Sets the auto-activation for the specified bundle identifier.
- [CTFontManagerError](ctfontmanagererror.md) — Errors that prevent unregistration of fonts for a specified font file URL.
- [CTFontManagerScope](ctfontmanagerscope.md) — Constants that define the scope for font registration.
- [CTRubyAlignment](ctrubyalignment.md) — Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [CTRubyOverhang](ctrubyoverhang.md) — Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [CTRubyPosition](ctrubyposition.md) — Constants that specify the position of the ruby text relative to to the base text.
