---
title: keyboardDismissMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/keyboarddismissmode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/keyboarddismissmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/keyboarddismissmode-swift.property.json'
content_hash: 'sha256:d9bd7d7bdb1375d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# keyboardDismissMode

<sub>Instance Property</sub>

The manner in which the system dismisses the keyboard when a drag begins in the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var keyboardDismissMode: UIScrollView.KeyboardDismissMode { get set }
```

## Discussion

The default value is [UIScrollViewKeyboardDismissModeNone](keyboarddismissmode-swift.enum/none.md). See [KeyboardDismissMode](keyboarddismissmode-swift.enum.md) for possible values.

## See Also

### Dismissing the keyboard

- [KeyboardDismissMode](keyboarddismissmode-swift.enum.md) — Constants that determine how the system dismisses the keyboard when a drag begins in the scroll view.
