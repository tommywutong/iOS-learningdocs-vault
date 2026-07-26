---
title: inputViewStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputview/inputviewstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiinputview/inputviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputview/inputviewstyle.json'
content_hash: 'sha256:b6f296b4bc230d94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputView](../uiinputview.md)

# inputViewStyle

<sub>Instance Property</sub>

The style for the content of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var inputViewStyle: UIInputView.Style { get }
```

## Discussion

The style applies both to the current view and to any subviews that adopt the [UIAppearance](../uiappearance.md) protocol, which includes all standard system views.

## See Also

### Getting the input style

- [Style](style.md) — Constants that indicate the appearance changes for an input view.
