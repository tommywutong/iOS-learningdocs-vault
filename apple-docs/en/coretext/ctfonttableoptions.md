---
title: CTFontTableOptions
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfonttableoptions
source_url: 'https://developer.apple.com/documentation/coretext/ctfonttableoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfonttableoptions.json'
content_hash: 'sha256:05a7ac565164cdf5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontTableOptions

<sub>Structure</sub>

Constants that describe font table options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTFontTableOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [init(rawValue:)](<ctfonttableoptions/init(rawvalue_).md>) — Creates a font table options structure with the specified raw value.
- [kCTFontTableOptionExcludeSynthetic](ctfonttableoptions/excludesynthetic.md) — The font table excludes synthetic font data. _(deprecated)_

## See Also

### Enumerations

- [CTFontUIFontType](ctfontuifonttype.md) — Constants that represent the specific user-interface purpose to specify for font creation.
- [CTFontTableTag](ctfonttabletag.md) — Font table tags provide access to font table data.
- [CTFontOptions](ctfontoptions.md) — Options for font creation and descriptor matching.
