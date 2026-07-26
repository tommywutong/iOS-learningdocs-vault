---
title: NSDirectionalEdgeInsetsEqualToDirectionalEdgeInsets
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdirectionaledgeinsetsequaltodirectionaledgeinsets
source_url: 'https://developer.apple.com/documentation/uikit/nsdirectionaledgeinsetsequaltodirectionaledgeinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdirectionaledgeinsetsequaltodirectionaledgeinsets.json'
content_hash: 'sha256:cee946575156e914'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDirectionalEdgeInsetsEqualToDirectionalEdgeInsets

<sub>Function</sub>

Compares two directional edge insets to determine if they’re the same.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
static BOOL NSDirectionalEdgeInsetsEqualToDirectionalEdgeInsets(NSDirectionalEdgeInsets insets1, NSDirectionalEdgeInsets insets2);
```

## Parameters

- `insets1` — An edge inset to compare with insets2.

- `insets2` — An edge inset to compare with insets1.

## Return Value

[true](../swift/true.md) if the edge insets are the same; otherwise, [false](../swift/false.md).
