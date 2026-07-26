---
title: 'captureTextFromCamera(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/capturetextfromcamera(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/capturetextfromcamera(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/capturetextfromcamera%28_%3A%29.json'
content_hash: 'sha256:b6fbf1bd21a43d37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# captureTextFromCamera(_:)

<sub>Instance Method</sub>

Starts scanning text using the device’s camera.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func captureTextFromCamera(_ sender: Any?)
```

## Parameters

- `sender` — The object that invokes this method.

## Discussion

To receive callbacks from the data scanner, the responder should conform to either the [UIKeyInput](../uikeyinput.md) or [UITextInput](../uitextinput.md) protocol. If it conforms to [UIKeyInput](../uikeyinput.md), the scanner calls the [insertText:](../../appkit/nstextinput/inserttext_.md) protocol method. If it conforms to [UITextInput](../uitextinput.md), the scanner calls the [- setMarkedText:selectedRange:](<../uitextinput/setmarkedtext(__selectedrange_).md>) and [- unmarkText](<../uitextinput/unmarktext().md>) protocol methods.

To determine whether the data scanner runs on the user’s device, pass [- captureTextFromCamera:](<capturetextfromcamera(__).md>) to the [- canPerformAction:withSender:](<canperformaction(__withsender_).md>) method.

## See Also

### Related Documentation

- [Scanning data with the camera](../../visionkit/scanning-data-with-the-camera.md) — Enable Live Text data scanning of text and codes that appear in the camera’s viewfinder.
