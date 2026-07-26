---
title: 'CTParagraphStyleCreate(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctparagraphstylecreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctparagraphstylecreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctparagraphstylecreate%28_%3A_%3A%29.json'
content_hash: 'sha256:ecae4e5b7ea2d1d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTParagraphStyleCreate(_:_:)

<sub>Function</sub>

Creates an immutable paragraph style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTParagraphStyleCreate(_ settings: UnsafePointer<CTParagraphStyleSetting>?, _ settingCount: Int) -> CTParagraphStyle
```

## Parameters

- `settings` — The settings with which to preload the paragraph style. If you want to specify the default set of settings, set this parameter to `NULL`.

- `settingCount` — The number of settings that you have specified in the `settings` parameter. This must be greater than or equal to `0`.

## Return Value

A valid reference to an immutable CTParagraphStyle object, If the paragraph style creation was successful; otherwise, `NULL`.

## Discussion

Using this function is the easiest and most efficient way to create a paragraph style. Paragraph styles should be kept immutable for totally lock-free operation. If an invalid paragraph style setting specifier is passed into the `settings` parameter, nothing bad will happen, but you will be unable to query for this value. The reason is to allow backward compatibility with style setting specifiers that may be introduced in future versions.

## See Also

### Creating Paragraph Styles

- [CTParagraphStyleCreateCopy](<ctparagraphstylecreatecopy(__).md>) — Creates an immutable copy of a paragraph style.
