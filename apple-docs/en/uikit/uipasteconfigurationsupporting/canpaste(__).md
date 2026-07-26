---
title: 'canPaste(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteconfigurationsupporting/canpaste(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfigurationsupporting/canpaste(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfigurationsupporting/canpaste%28_%3A%29.json'
content_hash: 'sha256:42562316e3ecdb35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfigurationSupporting](../uipasteconfigurationsupporting.md)

# canPaste(_:)

<sub>Instance Method</sub>

Returns a Boolean value that determines whether the responder object can perform a paste operation using data provided by the item providers.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func canPaste(_ itemProviders: [NSItemProvider]) -> Bool
```

## Parameters

- `itemProviders` — An array of [NSItemProvider](../../foundation/nsitemprovider.md) objects.

## Return Value

[true](../../swift/true.md) if the responder object can perform a paste operation using specified item providers; otherwise, [false](../../swift/false.md).

## See Also

### Performing a paste operation

- [- pasteItemProviders:](<paste(itemproviders_).md>) — Performs a paste operation on the responder object.
