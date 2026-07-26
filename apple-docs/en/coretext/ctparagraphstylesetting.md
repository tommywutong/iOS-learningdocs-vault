---
title: CTParagraphStyleSetting
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctparagraphstylesetting
source_url: 'https://developer.apple.com/documentation/coretext/ctparagraphstylesetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctparagraphstylesetting.json'
content_hash: 'sha256:d67c22073590042e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTParagraphStyleSetting

<sub>Structure</sub>

This structure is used to alter the paragraph style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTParagraphStyleSetting
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init(spec:valueSize:value:)](<ctparagraphstylesetting/init(spec_valuesize_value_).md>)

### Instance Properties

- [spec](ctparagraphstylesetting/spec.md) — The specifier of the setting. See [CTParagraphStyleSpecifier](ctparagraphstylespecifier.md) for possible values.
- [value](ctparagraphstylesetting/value.md) — A reference to the value of the setting specified by the `spec` field. The value must be in the proper range for the `spec` value and at least as large as the size specified in `valueSize`.
- [valueSize](ctparagraphstylesetting/valuesize.md) — The size of the value pointed to by the `value` field. This value must match the size of the value required by the `CTParagraphStyleSpecifier` set in the `spec` field.
