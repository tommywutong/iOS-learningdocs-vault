---
title: arrowHeight()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverbackgroundviewmethods/arrowheight()
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods/arrowheight()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverbackgroundviewmethods/arrowheight%28%29.json'
content_hash: 'sha256:2936320ddbf1678d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverBackgroundViewMethods](../uipopoverbackgroundviewmethods.md)

# arrowHeight()

<sub>Type Method</sub>

The height of the arrow (measured in points) from its base to its tip.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static func arrowHeight() -> CGFloat
```

## Discussion

Use this method to return the height of the arrow used by your popover background content. The arrow height must be the same for all possible directions and that height must not change.

## See Also

### Accessing the arrow metrics

- [+ arrowBase](<arrowbase().md>) — The width of the arrow triangle at its base.
