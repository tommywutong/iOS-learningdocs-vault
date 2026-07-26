---
title: open()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchaselink/open()
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchaselink/open()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchaselink/open%28%29.json'
content_hash: 'sha256:1b47a3a70f60d291'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchaseLink](../externalpurchaselink.md)

# open()

<sub>Type Method</sub>

Presents a continuation sheet that enables people to choose whether your app shows its link for external purchases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func open() async throws
```

## Discussion

Use this method if your app configures the [SKExternalPurchaseLink](../../bundleresources/information-property-list/skexternalpurchaselink.md) property list key.

Call this asynchronous method to have the system attempt to open the external purchase link, as shown below:

```swift
try await ExternalPurchaseLink.open()
```

To use this method, follow these steps:

1. Call [canOpen](canopen.md) to determine whether to display a button or other user-interface controls that enable you to call [open()](<open().md>). If it returns `true`, your app can display the user-interface controls to enable deliberate user interaction.
2. In response to deliberate user interaction, such as tapping a button, call [open()](<open().md>). The system displays the continuation sheet that enables the user to choose whether to continue to view your app’s external purchase URL. This asynchronous method returns before the system presents the continuation sheet, and throws an error if [canOpen](canopen.md) is `false`.

If the person chooses to continue, this method opens the current storefront’s destination URL that you configure in the [SKExternalPurchaseLink](../../bundleresources/information-property-list/skexternalpurchaselink.md) property list key and appends an external purchase token and the app’s bundleID to the URL. For example, StoreKit opens the following URL on the default browser if your destination URL is `https://site.example.com`:

```http
https://site.example.com?externalPurchaseToken=ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIgp9&bundleId=com.example

```

> [!important] Important
> Record and use the external purchase token to report the customer’s external purchases to Apple. For more information, see [External Purchase Server API](../../externalpurchaseserverapi.md).

### Handle errors

This method throws a [StoreKitError](../storekiterror.md) if any of the following are true:

- Your app doesn’t have the [com.apple.developer.storekit.external-purchase-link](../../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.md) entitlement.
- You haven’t configured external purchases for the current App Store storefront in [SKExternalPurchaseLink](../../bundleresources/information-property-list/skexternalpurchaselink.md).
- The current App Store storefront doesn’t support external purchases.
- The person is ineligible to make external purchases.
- A network or system error occurs.

For more information about App Store storefronts, see [Storefront](../storefront.md).

## See Also

### Getting a single external purchase link

- [SKExternalPurchaseLink](../../bundleresources/information-property-list/skexternalpurchaselink.md) — A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [canOpen](canopen.md) — A Boolean value that indicates whether the app can successfully open the configured external purchase link in the current App Store storefront.
