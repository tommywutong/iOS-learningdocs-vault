---
title: NSDirectionalEdgeInsetsFromString
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdirectionaledgeinsetsfromstring
source_url: 'https://developer.apple.com/documentation/uikit/nsdirectionaledgeinsetsfromstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdirectionaledgeinsetsfromstring.json'
content_hash: 'sha256:85a5166cb20b2d18'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDirectionalEdgeInsetsFromString

<sub>Function</sub>

Returns a directional edge insets structure based on data in the specified string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSDirectionalEdgeInsets NSDirectionalEdgeInsetsFromString(NSString *string);
```

## Parameters

- `string` — A string whose contents are of the form “{top, leading, bottom, trailing}”, where top, leading, bottom, trailing are the floating-point component values of the [NSDirectionalEdgeInsets](nsdirectionaledgeinsets.md) structure. An example of a valid string is “`{3.0,8.0,3.0,5.0}`”. The string is not localized, so items are always separated with a comma.

## Return Value

A directional edge insets data structure. If the string is not well-formed, the function returns [NSDirectionalEdgeInsetsZero](nsdirectionaledgeinsets/zero.md).

## See Also

### Converting to and from strings

- [NSStringFromDirectionalEdgeInsets](nsstringfromdirectionaledgeinsets.md) — Returns a string formatted to contain the data from a directional edge insets structure.
