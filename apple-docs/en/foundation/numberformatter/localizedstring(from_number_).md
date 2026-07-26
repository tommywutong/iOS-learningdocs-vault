---
title: 'localizedString(from:number:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatter/localizedstring(from:number:)'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/localizedstring(from:number:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/localizedstring%28from%3Anumber%3A%29.json'
content_hash: 'sha256:7ccb25bc961da8b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# localizedString(from:number:)

<sub>Type Method</sub>

Returns a localized number string with the specified style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localizedString(from num: NSNumber, number nstyle: NumberFormatter.Style) -> String
```

## Parameters

- `num` — The number to localize

- `nstyle` — The localization style to use. See [Style](style.md) for the supported values.

## Return Value

An appropriately formatted `NSString`.

## See Also

### Converting Between Numbers and Strings

- [- getObjectValue:forString:range:error:](<getobjectvalue(__for_range_).md>) — Returns by reference a cell-content object after creating it from a range of characters in a given string.
- [- numberFromString:](<number(from_).md>) — Returns an [NSNumber](../nsnumber.md) object created by parsing a given string.
- [- stringFromNumber:](<string(from_).md>) — Returns a string containing the formatted value of the provided number object.
