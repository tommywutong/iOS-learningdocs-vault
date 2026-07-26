---
title: 'paste(itemProviders:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteconfigurationsupporting/paste(itemproviders:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfigurationsupporting/paste(itemproviders:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfigurationsupporting/paste%28itemproviders%3A%29.json'
content_hash: 'sha256:14b76931f1e4778e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfigurationSupporting](../uipasteconfigurationsupporting.md)

# paste(itemProviders:)

<sub>Instance Method</sub>

Performs a paste operation on the responder object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func paste(itemProviders: [NSItemProvider])
```

## Parameters

- `itemProviders` — An array of [NSItemProvider](../../foundation/nsitemprovider.md) objects.

## Discussion

This method performs a paste operation on the responder object, pasting the data provided by specified item providers.

## See Also

### Performing a paste operation

- [- canPasteItemProviders:](<canpaste(__).md>) — Returns a Boolean value that determines whether the responder object can perform a paste operation using data provided by the item providers.
