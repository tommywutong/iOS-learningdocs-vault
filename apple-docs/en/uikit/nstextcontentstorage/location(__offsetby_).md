---
title: 'location(_:offsetBy:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentstorage/location(_:offsetby:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentstorage/location(_:offsetby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentstorage/location%28_%3Aoffsetby%3A%29.json'
content_hash: 'sha256:0b273bb3a72e3f3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentStorage](../nstextcontentstorage.md)

# location(_:offsetBy:)

<sub>Instance Method</sub>

Returns a new text location object based on an existing location and offset you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func location(_ location: any NSTextLocation, offsetBy offset: Int) -> (any NSTextLocation)?
```

## Parameters

- `location` — The starting location. For example, you might specify the beginning or end of the document as the starting location.

- `offset` — The number of characters from the starting location. Specify a positive integer to create a location object that comes after the starting location. Specify a negative number to create a location object that comes before the starting location.

## Return Value

An [NSTextLocation](../nstextlocation.md) object that corresponds to the new location, or `nil` if the new location exceeds the bounds of the text.

## Discussion

You can get [NSTextLocation](../nstextlocation.md) objects for the start and end of the text storage from the [documentRange](../nstextelementprovider/documentrange.md) property of the [NSTextElementProvider](../nstextelementprovider.md) protocol, which [NSTextContentStorage](../nstextcontentstorage.md) implements. If you provide an [NSTextLocation](../nstextlocation.md) object doesn’t match the type of the ones in the [documentRange](../nstextelementprovider/documentrange.md) property, this method throws an exception.

## See Also

### Finding ranges, locations, and offsets

- [- offsetFromLocation:toLocation:](<offset(from_to_).md>) — Returns the number of characters between the specified locations.
- [- adjustedRangeFromRange:forEditingTextSelection:](<adjustedrange(from_foreditingtextselection_).md>) — Returns the text range, if any, in the backing store that required manual adjustment after editing.
