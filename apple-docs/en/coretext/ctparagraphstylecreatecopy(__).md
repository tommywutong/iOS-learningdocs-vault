---
title: 'CTParagraphStyleCreateCopy(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctparagraphstylecreatecopy(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctparagraphstylecreatecopy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctparagraphstylecreatecopy%28_%3A%29.json'
content_hash: 'sha256:35a131b143be1152'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTParagraphStyleCreateCopy(_:)

<sub>Function</sub>

Creates an immutable copy of a paragraph style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTParagraphStyleCreateCopy(_ paragraphStyle: CTParagraphStyle) -> CTParagraphStyle
```

## Parameters

- `paragraphStyle` — The style to copy. This parameter may not be `NULL`.

## Return Value

A valid reference to an immutable CTParagraphStyle object that is a copy of the one passed into `paragraphStyle`, If the `paragraphStyle` reference is valid; otherwise `NULL`, if any error occurred, including being supplied with an invalid reference.

## See Also

### Creating Paragraph Styles

- [CTParagraphStyleCreate](<ctparagraphstylecreate(____).md>) — Creates an immutable paragraph style.
