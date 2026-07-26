---
title: currentInputModeDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputmode/currentinputmodedidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputmode/currentinputmodedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputmode/currentinputmodedidchangenotification.json'
content_hash: 'sha256:230162ac4e52a0b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputMode](../uitextinputmode.md)

# currentInputModeDidChangeNotification

<sub>Type Property</sub>

A notification that posts when the current input mode changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let currentInputModeDidChangeNotification: NSNotification.Name
```

## Discussion

The posting object is a [UITextInputMode](../uitextinputmode.md) instance.
