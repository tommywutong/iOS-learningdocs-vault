---
title: UIEdgeInsetsInsetRect
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiedgeinsetsinsetrect
source_url: 'https://developer.apple.com/documentation/uikit/uiedgeinsetsinsetrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiedgeinsetsinsetrect.json'
content_hash: 'sha256:2f9d785e96245a28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIEdgeInsetsInsetRect

<sub>Function</sub>

Adjusts a rectangle by the given edge insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
static CGRect UIEdgeInsetsInsetRect(CGRect rect, UIEdgeInsets insets);
```

## Parameters

- `rect` — The rectangle to be adjusted.

- `insets` — The edge insets to be applied to the adjustment.

## Return Value

A rectangle that is adjusted by the `UIEdgeInsets` structure passed in insets.

## Discussion

This inline function increments the origin of `rect` and decrements the size of `rect` by applying the appropriate member values of the `UIEdgeInsets` structure.

## See Also

### Related Documentation

- [UIEdgeInsetsMake](<uiedgeinsets/init(top_left_bottom_right_)-1s1t9.md>) — Creates an edge insets structure with the specified edges.
