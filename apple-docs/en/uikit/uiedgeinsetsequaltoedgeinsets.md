---
title: UIEdgeInsetsEqualToEdgeInsets
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiedgeinsetsequaltoedgeinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiedgeinsetsequaltoedgeinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiedgeinsetsequaltoedgeinsets.json'
content_hash: 'sha256:90bd40b44b58eb18'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIEdgeInsetsEqualToEdgeInsets

<sub>Function</sub>

Returns a Boolean value indicating whether the two edge insets are the same.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
static BOOL UIEdgeInsetsEqualToEdgeInsets(UIEdgeInsets insets1, UIEdgeInsets insets2);
```

## Parameters

- `insets1` — An edge inset to compare with `insets2`.

- `insets2` — An edge inset to compare with `insets1`.

## Return Value

[true](../swift/true.md) if the edge insets are the same; otherwise, [false](../swift/false.md).

## See Also

### Related Documentation

- [UIEdgeInsetsMake](<uiedgeinsets/init(top_left_bottom_right_)-1s1t9.md>) — Creates an edge insets structure with the specified edges.
