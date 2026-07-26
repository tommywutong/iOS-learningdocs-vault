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
doc_path: '/documentation/uikit/nstextelementprovider/location(_:offsetby:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextelementprovider/location(_:offsetby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextelementprovider/location%28_%3Aoffsetby%3A%29.json'
content_hash: 'sha256:909610ee8d47b18a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextElementProvider](../nstextelementprovider.md)

# location(_:offsetBy:)

<sub>Instance Method</sub>

Returns a new location from location with offset you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func location(_ location: any NSTextLocation, offsetBy offset: Int) -> (any NSTextLocation)?
```

## Parameters

- `location` — An [NSTextLocation](../nstextlocation.md) in the text element.

- `offset` — An offset of the number of characters to or from `location`.

## Return Value

An new `NSTextLocation`, or `nil` of the offset exceeds the bounds of the text.

## See Also

### Accessing and updating the text

- [- enumerateTextElementsFromLocation:options:usingBlock:](<enumeratetextelements(from_options_using_).md>) — Enumerates text elements starting at the text location you provide.
- [EnumerationOptions](../nstextlayoutfragment/enumerationoptions.md) — Values that describe options for enumerating text layout fragments.
- [- replaceContentsInRange:withTextElements:](<replacecontents(in_with_).md>) — Replaces the characters specified by range with the text elements you provide.
