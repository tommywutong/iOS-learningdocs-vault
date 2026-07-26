---
title: 'textFormattingViewController:shouldPresentFontPicker:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller:shouldpresentfontpicker:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller:shouldpresentfontpicker:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller%3Ashouldpresentfontpicker%3A.json'
content_hash: 'sha256:8c55f20fe7f73116'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFormattingViewControllerDelegate](../uitextformattingviewcontrollerdelegate.md)

# textFormattingViewController:shouldPresentFontPicker:

<sub>Instance Method</sub>

If implemented, text formatting will call this method before presenting font picker controller. Use this method to make any presentation modifications or to prevent presentation altogether.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) textFormattingViewController:(UITextFormattingViewController *) viewController shouldPresentFontPicker:(UIFontPickerViewController *) fontPicker;
```

## Parameters

- `viewController` — Text formatting controller that is attempting to present font picker controller

- `fontPicker` — Font picker controller that will be presented.

## Return Value

Flag indicating if text formatting controller should present font picker.

## Discussion

If you decide to prevent presentation of font picker via text formatting controller, you may present provided font picker yourself. In this case, you will have to handle any font picker actions independently.
