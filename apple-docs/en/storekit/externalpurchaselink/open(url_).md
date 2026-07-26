---
title: 'open(url:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, tvOS 17.5+, visionOS 1.2+, watchOS 10.5+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/externalpurchaselink/open(url:)'
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchaselink/open(url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchaselink/open%28url%3A%29.json'
content_hash: 'sha256:96e705e5cae43945'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchaseLink](../externalpurchaselink.md)

# open(url:)

<sub>Type Method</sub>

Presents a continuation sheet that enables people to choose whether your app shows the indicated URL link for external purchases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func open(url: URL) async throws
```

## Parameters

- `url` — An eligible external purchase link that you select from the [eligibleURLs](eligibleurls.md) array.

## Discussion

Call this method if your app configures the [SKExternalPurchaseMultiLink](../../bundleresources/information-property-list/skexternalpurchasemultilink.md) property list key to attempt to open the eligible external purchase link, `url`. Call this asynchronous method as shown below:

```swift
if let eligibleURLs = await ExternalPurchaseLink.eligibleURLs {
    let url = chooseTheUrl(eligibleURLs) // Supply a function to choose one of the eligible URLs.
    try await ExternalPurchaseLink.open(url: url)
  }
```

To use this method, follow these steps:

1. Check the [eligibleURLs](eligibleurls.md) array. If the array contains one or more links, your app can display the user-interface controls to enable deliberate user interaction before offering an external purchase link.
2. Select one of the eligible links.
3. In response to deliberate user interaction, such as tapping a button, call [open(url:)](<open(url_).md>) with the link you select.

The system displays the continuation sheet that enables the user to choose whether to continue to view the external purchase link. This asynchronous method returns before the system presents the continuation sheet, and can throw an error.

If the person chooses to continue, this method opens the link that you provide in the `url` parameter, and appends an external purchase token and the app’s bundleID to the URL. For example, StoreKit opens the following link on the default browser if your destination URL is `https://site.example.com`:

```http
https://site.example.com?externalPurchaseToken=ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIgp9&bundleId=com.example
```

> [!important] Important
> Record and use the external purchase token to report the customer’s external purchases to Apple. For more information, see [External Purchase Server API](../../externalpurchaseserverapi.md).

### Handle errors

This method throws a [StoreKitError](../storekiterror.md) if any of the following are true:

- Your app doesn’t have the  [com.apple.developer.storekit.external-purchase-link](../../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.md) entitlement.
- You haven’t configured external purchase links for the current App Store storefront in the [SKExternalPurchaseMultiLink](../../bundleresources/information-property-list/skexternalpurchasemultilink.md) property list key.
- The current App Store storefront doesn’t support external purchases.
- The person is ineligible to make external purchases.
- A network or system error occurs.

For more information about App Store storefronts, see [Storefront](../storefront.md).

## See Also

### Getting multiple external purchase links

- [SKExternalPurchaseMultiLink](../../bundleresources/information-property-list/skexternalpurchasemultilink.md) — A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [eligibleURLs](eligibleurls.md) — An array of external purchase links for the current storefront that the app configured and from which it chooses.
