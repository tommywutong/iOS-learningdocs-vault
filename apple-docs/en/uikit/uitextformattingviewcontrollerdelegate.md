---
title: UITextFormattingViewControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextformattingviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingviewcontrollerdelegate.json'
content_hash: 'sha256:13004a1ed4e00ae7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextFormattingViewControllerDelegate

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UITextFormattingViewControllerDelegate <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Methods

- [textFormattingDidFinish:](uitextformattingviewcontrollerdelegate/textformattingdidfinish_.md) — Informs the delegate that user has dismissed text formatting view controller.
- [textFormattingViewController:didChangeValue:](uitextformattingviewcontrollerdelegate/textformattingviewcontroller_didchangevalue_.md) — Delegate method that will be invoked on any text formatting changes.
- [textFormattingViewController:shouldPresentColorPicker:](uitextformattingviewcontrollerdelegate/textformattingviewcontroller_shouldpresentcolorpicker_.md) — If implemented, text formatting will call this method before presenting color picker controller. Use this method to make any presentation modifications or to prevent presentation altogether.
- [textFormattingViewController:shouldPresentFontPicker:](uitextformattingviewcontrollerdelegate/textformattingviewcontroller_shouldpresentfontpicker_.md) — If implemented, text formatting will call this method before presenting font picker controller. Use this method to make any presentation modifications or to prevent presentation altogether.
