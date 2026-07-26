---
title: 'textPasteConfigurationSupporting(_:transform:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:transform:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting%28_%3Atransform%3A%29.json'
content_hash: 'sha256:5be12fa07f08a483'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextPasteDelegate](../uitextpastedelegate.md)

# textPasteConfigurationSupporting(_:transform:)

<sub>Instance Method</sub>

Tells the delegate to transform the pasted or dropped text item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textPasteConfigurationSupporting(_ textPasteConfigurationSupporting: any UITextPasteConfigurationSupporting, transform item: any UITextPasteItem)
```

## Parameters

- `textPasteConfigurationSupporting` — The object that received the paste or drop request.

- `item` — The text paste item included in the paste or drop operation.

## Discussion

This method is called for each text paste item during a paste or drop operation. You’re required to call one of the `setResult` methods (see Setting a text paste item’s result value) on `item`, but the call doesn’t have to be within the scope of the transform method. It can, for example, be part of the asynchronous handling code for the [itemProvider](../uitextpasteitem/itemprovider.md), or it can be part of a completion block. You can make the call whenever you prefer.

It’s safe to use the provided [UITextPasteItem](../uitextpasteitem.md) object on any thread, but the transform method is always called on the main thread.
