---
title: NSStringFromUIEdgeInsets
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringfromuiedgeinsets
source_url: 'https://developer.apple.com/documentation/uikit/nsstringfromuiedgeinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringfromuiedgeinsets.json'
content_hash: 'sha256:ae91c454468301d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSStringFromUIEdgeInsets

<sub>Function</sub>

Returns a string formatted to contain the data from an edge insets structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString *NSStringFromUIEdgeInsets(UIEdgeInsets insets);
```

## Parameters

- `insets` — A UIKit edge insets data structure.

## Return Value

A string that corresponds to `insets`. See [UIEdgeInsetsFromString](uiedgeinsetsfromstring.md) for a discussion of the string format.

## See Also

### Converting to and from strings

- [UIEdgeInsetsFromString](uiedgeinsetsfromstring.md) — Returns a UIKit edge insets structure based on the data in the specified string.
