---
title: needsInputModeSwitchKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputviewcontroller/needsinputmodeswitchkey
source_url: 'https://developer.apple.com/documentation/uikit/uiinputviewcontroller/needsinputmodeswitchkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputviewcontroller/needsinputmodeswitchkey.json'
content_hash: 'sha256:c206f76ed3dcc078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputViewController](../uiinputviewcontroller.md)

# needsInputModeSwitchKey

<sub>Instance Property</sub>

A Boolean value that indicates whether the keyboard must display an input switcher key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var needsInputModeSwitchKey: Bool { get }
```

## Discussion

The input switcher key allows the user to switch between different keyboards. When this property is true, your custom keyboard should provide such a key.

## See Also

### Configuring the keyboard behaviors

- [hasFullAccess](hasfullaccess.md) — A Boolean value that indicates whether the keyboard has full access.
- [hasDictationKey](hasdictationkey.md) — A Boolean value that indicates whether the keyboard has a dictation key.
