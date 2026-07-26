---
title: invalidProductIdentifiers
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductsresponse/invalidproductidentifiers
source_url: 'https://developer.apple.com/documentation/storekit/skproductsresponse/invalidproductidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsresponse/invalidproductidentifiers.json'
content_hash: 'sha256:b7596f9fd778f827'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductsResponse](../skproductsresponse.md)

# invalidProductIdentifiers

<sub>Instance Property</sub>

An array of product identifier strings that the App Store doesn’t recognize.

> [!warning] Deprecated
> Get products using Product.products(for:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var invalidProductIdentifiers: [String] { get }
```

## Discussion

The App Store may not recognize your product identifiers unless you meet following criteria, as applicable:

- Agree to the latest Apple Developer Program License Agreement.
- Complete all the financial agreements as described in the [Agreements, Tax, and Banking Overview](https://help.apple.com/itunes-connect/developer/#/devb6df5ee51). When you renew your developer membership, see if you need to make updates to your agreements. When your developer membership expires, your financial agreements expire as well.
- Your app uses an explicit App ID.
- Clear the in-app purchases for sale in App Store Connect. See [Set availability for in-app purchase](https://help.apple.com/app-store-connect/#/dev360aba524).
- Modified in-app purchases are available to the App Store servers.
- The product identifier specified in App Store Connect matches the identifier used by the [SKProductsRequest](../skproductsrequest.md) object in your app.
- Upload the content of your product to App Store Connect.  See [Upload in-app purchase content to App Store Connect](https://help.apple.com/xcode/mac/current/#/dev285fb60ce).

For more troubleshooting information, see [Fetching product information from the App Store](../fetching-product-information-from-the-app-store.md).

## See Also

### Response Information

- [products](products.md) — A list of products, one product for each valid product identifier provided in the original request. _(deprecated)_
