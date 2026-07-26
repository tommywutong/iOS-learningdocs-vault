---
title: NSStringFromDirectionalEdgeInsets
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringfromdirectionaledgeinsets
source_url: 'https://developer.apple.com/documentation/uikit/nsstringfromdirectionaledgeinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringfromdirectionaledgeinsets.json'
content_hash: 'sha256:9ce1081d11f9a6b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSStringFromDirectionalEdgeInsets

<sub>Function</sub>

Returns a string formatted to contain the data from a directional edge insets structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString *NSStringFromDirectionalEdgeInsets(NSDirectionalEdgeInsets insets);
```

## Parameters

- `insets` — A directional edge insets data structure.

## Return Value

A string that corresponds to insets. See [NSDirectionalEdgeInsetsFromString](nsdirectionaledgeinsetsfromstring.md) for a discussion of the string format.

## See Also

### Converting to and from strings

- [NSDirectionalEdgeInsetsFromString](nsdirectionaledgeinsetsfromstring.md) — Returns a directional edge insets structure based on data in the specified string.
