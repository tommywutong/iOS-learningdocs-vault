---
title: 'attributedString(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentstorage/attributedstring(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentstorage/attributedstring(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentstorage/attributedstring%28for%3A%29.json'
content_hash: 'sha256:24b2905154ed87ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentStorage](../nstextcontentstorage.md)

# attributedString(for:)

<sub>Instance Method</sub>

Returns a new attributed string for the text element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func attributedString(for textElement: NSTextElement) -> NSAttributedString?
```

## Parameters

- `textElement` — The [NSTextElement](../nstextelement.md) to map into an attributed string.

## Return Value

An [NSAttributedString](../../foundation/nsattributedstring.md), or `nil`.

## Discussion

Returns `nil` if the method can’t map `textElement` to an [NSAttributedString](../../foundation/nsattributedstring.md).

## See Also

### Managing text elements

- [- textElementForAttributedString:](<textelement(for_).md>) — Returns the text element corresponding to object’s attributed string.
