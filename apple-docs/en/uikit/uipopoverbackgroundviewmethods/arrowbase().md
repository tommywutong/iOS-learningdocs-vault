---
title: arrowBase()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverbackgroundviewmethods/arrowbase()
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods/arrowbase()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverbackgroundviewmethods/arrowbase%28%29.json'
content_hash: 'sha256:c6e78681b38f4f23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverBackgroundViewMethods](../uipopoverbackgroundviewmethods.md)

# arrowBase()

<sub>Type Method</sub>

The width of the arrow triangle at its base.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static func arrowBase() -> CGFloat
```

## Discussion

Use this method to return the width of your popover’s arrow at its base. The arrow width must be the same for all possible directions and that width must not change.

## See Also

### Accessing the arrow metrics

- [+ arrowHeight](<arrowheight().md>) — The height of the arrow (measured in points) from its base to its tip.
