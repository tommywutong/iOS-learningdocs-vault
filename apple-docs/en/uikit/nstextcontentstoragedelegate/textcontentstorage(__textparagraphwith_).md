---
title: 'textContentStorage(_:textParagraphWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentstoragedelegate/textcontentstorage(_:textparagraphwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentstoragedelegate/textcontentstorage(_:textparagraphwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentstoragedelegate/textcontentstorage%28_%3Atextparagraphwith%3A%29.json'
content_hash: 'sha256:f2c9eb4040b61482'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentStorageDelegate](../nstextcontentstoragedelegate.md)

# textContentStorage(_:textParagraphWith:)

<sub>Instance Method</sub>

Returns a custom paragraph for a range that you provide from the object’s attributed string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textContentStorage(_ textContentStorage: NSTextContentStorage, textParagraphWith range: NSRange) -> NSTextParagraph?
```

## Parameters

- `textContentStorage` — The object’s content manager.

- `range` — The [NSRange](../../foundation/nsrange-c.struct.md) that describes the extent of the string.

## Return Value

A new [NSTextParagraph](../nstextparagraph.md), or `nil`.

## Discussion

When non-`nil`, `textContentStorage` uses the text paragraph instead of creating the standard [NSTextParagraph](../nstextparagraph.md) with the attributed substring in `range`. The attributed string for a custom text paragraph must have a length of `range.length`.
