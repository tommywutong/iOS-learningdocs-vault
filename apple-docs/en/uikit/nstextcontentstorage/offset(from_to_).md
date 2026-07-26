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
doc_path: '/documentation/uikit/nstextcontentstorage/offset(from:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentstorage/offset(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentstorage/offset%28from%3Ato%3A%29.json'
content_hash: 'sha256:ea66d2bcc9817323'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentStorage](../nstextcontentstorage.md)

# offset(from:to:)

<sub>Instance Method</sub>

Returns the number of characters between the specified locations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int
```

## Parameters

- `from` — The starting location in the text storage. For example, you might specify the beginning of the document as the starting location.

- `to` — The end location in the text storage.

## Return Value

The number of characters between the start and end locations. If the to location comes before the from location, the returned value is negative.

## Discussion

You can get [NSTextLocation](../nstextlocation.md) objects for the start and end of the text storage from the [documentRange](../nstextelementprovider/documentrange.md) property of the [NSTextElementProvider](../nstextelementprovider.md) protocol, which [NSTextContentStorage](../nstextcontentstorage.md) implements. If you provide an [NSTextLocation](../nstextlocation.md) object doesn’t match the type of the ones in the [documentRange](../nstextelementprovider/documentrange.md) property, this method throws an exception.

## See Also

### Finding ranges, locations, and offsets

- [- locationFromLocation:withOffset:](<location(__offsetby_).md>) — Returns a new text location object based on an existing location and offset you provide.
- [- adjustedRangeFromRange:forEditingTextSelection:](<adjustedrange(from_foreditingtextselection_).md>) — Returns the text range, if any, in the backing store that required manual adjustment after editing.
