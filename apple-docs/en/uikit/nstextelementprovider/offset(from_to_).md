---
title: 'offset(from:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextelementprovider/offset(from:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextelementprovider/offset(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextelementprovider/offset%28from%3Ato%3A%29.json'
content_hash: 'sha256:8db76fd128f4f0dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextElementProvider](../nstextelementprovider.md)

# offset(from:to:)

<sub>Instance Method</sub>

Returns the offset between the two specified locations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int
```

## Parameters

- `from` — A starting location.

- `to` — An ending location.

## Return Value

An `Integer` that represents the offset between the starting and ending locations.

## Discussion

The return value could be positive or negative. This method can return [NSNotFound](../../foundation/nsnotfound-4qp9h.md) when the method can’t represent an offset as an integer value. This can occur, for example, if the locations aren’t in the same document).

## See Also

### Adjusting the range of the text element

- [- adjustedRangeFromRange:forEditingTextSelection:](<adjustedrange(from_foreditingtextselection_).md>) — A method you implement if the location backing store requires manual adjustment after editing.
