---
title: 'textFormattingViewController:didChangeValue:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller:didchangevalue:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller:didchangevalue:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller%3Adidchangevalue%3A.json'
content_hash: 'sha256:3e7fcb9446764d2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFormattingViewControllerDelegate](../uitextformattingviewcontrollerdelegate.md)

# textFormattingViewController:didChangeValue:

<sub>Instance Method</sub>

Delegate method that will be invoked on any text formatting changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) textFormattingViewController:(UITextFormattingViewController *) viewController didChangeValue:(UITextFormattingViewControllerChangeValue *) changeValue;
```

## Parameters

- `viewController` — Text formatting controller in which action was performed.

- `changeValue` — Object describing the change made via view controller.
