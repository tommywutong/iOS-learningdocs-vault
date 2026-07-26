---
title: CTFontOptions
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontoptions
source_url: 'https://developer.apple.com/documentation/coretext/ctfontoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontoptions.json'
content_hash: 'sha256:f7c55605dfc2d2c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontOptions

<sub>Structure</sub>

Options for font creation and descriptor matching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTFontOptions
```

## Overview

Use these options with the functions [CTFontCreateWithNameAndOptions](<ctfontcreatewithnameandoptions(________).md>) and [CTFontCreateWithFontDescriptorAndOptions](<ctfontcreatewithfontdescriptorandoptions(________).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCTFontOptionsPreventAutoActivation](ctfontoptions/preventautoactivation.md) — Prevents automatic font activation.
- [kCTFontOptionsPreferSystemFont](ctfontoptions/prefersystemfont.md) — Font matching prefers to match Apple system fonts.

### Initializers

- [init(rawValue:)](<ctfontoptions/init(rawvalue_).md>) — Creates a font options structure with the specified raw value.

### Type Properties

- [kCTFontOptionsPreventAutoDownload](ctfontoptions/preventautodownload.md)

## See Also

### Enumerations

- [CTFontUIFontType](ctfontuifonttype.md) — Constants that represent the specific user-interface purpose to specify for font creation.
- [CTFontTableTag](ctfonttabletag.md) — Font table tags provide access to font table data.
- [CTFontTableOptions](ctfonttableoptions.md) — Constants that describe font table options.
