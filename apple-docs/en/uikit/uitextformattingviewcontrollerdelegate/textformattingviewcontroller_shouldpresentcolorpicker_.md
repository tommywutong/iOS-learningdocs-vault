---
title: 'textFormattingViewController:shouldPresentColorPicker:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller:shouldpresentcolorpicker:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller:shouldpresentcolorpicker:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller%3Ashouldpresentcolorpicker%3A.json'
content_hash: 'sha256:7f54e93db5f2e74e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFormattingViewControllerDelegate](../uitextformattingviewcontrollerdelegate.md)

# textFormattingViewController:shouldPresentColorPicker:

<sub>Instance Method</sub>

If implemented, text formatting will call this method before presenting color picker controller. Use this method to make any presentation modifications or to prevent presentation altogether.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) textFormattingViewController:(UITextFormattingViewController *) viewController shouldPresentColorPicker:(UIColorPickerViewController *) colorPicker;
```

## Parameters

- `viewController` — Text formatting controller that is attempting to present font picker controller

- `colorPicker` — Color picker controller that will be presented.

## Return Value

Flag indicating if text formatting controller should present font picker.

## Discussion

You may decide to prevent presentation of color picker via text formatting controller. In that case, you may present provided color picker controller yourself, but you will have to handle any actions in that controller separately.
