---
title: SKStoreProductParameterITunesItemIdentifier
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteritunesitemidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteritunesitemidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteritunesitemidentifier.json'
content_hash: 'sha256:2cb0585ed534a492'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterITunesItemIdentifier

<sub>Global Variable</sub>

The key representing the iTunes identifier for the item you want the store to display when the view controller is presented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
let SKStoreProductParameterITunesItemIdentifier: String
```

## Discussion

The value for this key, an iTunes item identifier, is an instance of [NSNumber](../foundation/nsnumber.md).

To find a product’s iTunes identifier, go to [linkmaker.itunes.apple.com](http://linkmaker.itunes.apple.com/us/) and search for the product, then locate the iTunes identifier in the link URL. For example, the iTunes identifier for the iBooks app is 364709193.
