---
title: showsSelectionIndicator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipickerview/showsselectionindicator
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview/showsselectionindicator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview/showsselectionindicator.json'
content_hash: 'sha256:fad3c038be151396'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerView](../uipickerview.md)

# showsSelectionIndicator

<sub>Instance Property</sub>

A Boolean value that determines whether the selection indicator is displayed.

> [!warning] Deprecated
> In iOS 7 and later, you can’t customize the picker view’s selection indicator. The selection indicator is always shown, so setting this property to [false](../../swift/false.md) has no effect.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var showsSelectionIndicator: Bool { get set }
```

## Discussion

If the value of the property is [true](../../swift/true.md), the picker view shows a clear overlay across the current row. The default value of this property is [false](../../swift/false.md).
