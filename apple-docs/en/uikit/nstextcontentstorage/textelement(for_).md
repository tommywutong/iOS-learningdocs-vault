---
title: 'textElement(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentstorage/textelement(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentstorage/textelement(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentstorage/textelement%28for%3A%29.json'
content_hash: 'sha256:aae5ffa9f1da8e9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentStorage](../nstextcontentstorage.md)

# textElement(for:)

<sub>Instance Method</sub>

Returns the text element corresponding to object’s attributed string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textElement(for attributedString: NSAttributedString) -> NSTextElement?
```

## Parameters

- `attributedString` — The attributed string to map into an [NSTextElement](../nstextelement.md).

## Return Value

An [NSTextElement](../nstextelement.md), or `nil`.

## Discussion

Returns `nil` when `attributedString` contains attributes not mappable to [NSTextElement](../nstextelement.md).

## See Also

### Managing text elements

- [- attributedStringForTextElement:](<attributedstring(for_).md>) — Returns a new attributed string for the text element.
