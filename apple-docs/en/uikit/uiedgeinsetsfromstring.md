---
title: UIEdgeInsetsFromString
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiedgeinsetsfromstring
source_url: 'https://developer.apple.com/documentation/uikit/uiedgeinsetsfromstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiedgeinsetsfromstring.json'
content_hash: 'sha256:1fc49aace0a4cb87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIEdgeInsetsFromString

<sub>Function</sub>

Returns a UIKit edge insets structure based on the data in the specified string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern UIEdgeInsets UIEdgeInsetsFromString(NSString *string);
```

## Parameters

- `string` — A string whose contents are of the form “{_top_, _left_, _bottom_, _right_}”, where _top_, _left_, _bottom_, _right_ are the floating-point component values of the [UIEdgeInsets](uiedgeinsets.md) structure. An example of a valid string is @”{3.0,8.0,3.0,5.0}”. The string is not localized, so items are always separated with a comma.

## Return Value

An edge insets data structure. If the string is not well-formed, the function returns [UIEdgeInsetsZero](uiedgeinsets/zero.md).

## Discussion

In general, you should use this function only to convert strings that were previously created using the [NSStringFromUIEdgeInsets](nsstringfromuiedgeinsets.md) function.

## See Also

### Converting to and from strings

- [NSStringFromUIEdgeInsets](nsstringfromuiedgeinsets.md) — Returns a string formatted to contain the data from an edge insets structure.
