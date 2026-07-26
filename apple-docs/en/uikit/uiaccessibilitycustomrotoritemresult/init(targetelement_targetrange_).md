---
title: 'init(targetElement:targetRange:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilitycustomrotoritemresult/init(targetelement:targetrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult/init(targetelement:targetrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomrotoritemresult/init%28targetelement%3Atargetrange%3A%29.json'
content_hash: 'sha256:72b51bb425bd3dda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomRotorItemResult](../uiaccessibilitycustomrotoritemresult.md)

# init(targetElement:targetRange:)

<sub>Initializer</sub>

Creates a rotor item result from the specified target element and text range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(targetElement: any NSObjectProtocol, targetRange: UITextRange?)
```

## Parameters

- `targetElement` — The target element of the rotor.

- `targetRange` — The text range for an element that contains text, such as a text view.

## Return Value

An initialized rotor item result.
