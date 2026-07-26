---
title: intents
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 14.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/purchaseintent/intents
source_url: 'https://developer.apple.com/documentation/storekit/purchaseintent/intents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/purchaseintent/intents.json'
content_hash: 'sha256:cb90fd3c0b4a9186'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [PurchaseIntent](../purchaseintent.md)

# intents

<sub>Type Property</sub>

The asynchronous sequence that emits a purchase intent when customers initiate a purchase outside of the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static var intents: PurchaseIntent.PurchaseIntents { get }
```

## Discussion

Your app receives a purchase intent when customers initiate a purchase outside of your app by selecting a promoted product on the App Store, or redeeming a win-back offer. Use the [product](product.md) object to complete your app’s purchase workflow, including finishing the purchase, unlocking the product, and any other workflows specific to your app.

The following example code receives the purchase intent, and calls a method to complete the purchase workflow:

```swift
func purchaseProduct(_ product: Product) async {
    // Complete the purchase workflow.
    do {
        try await product.purchase()
    }
    catch {
        // Add your code to handle errors.
    }
    // Add your code for the remaining purchase workflow.
}

for await purchaseIntent in PurchaseIntent.intents {
    // Receive the purchase intent and then complete the purchase workflow.
    await purchaseProduct(purchaseIntent.product)
}

```

## See Also

### Getting purchase intents

- [PurchaseIntents](purchaseintents.md) — An asynchronous sequence of purchase intents for purchases that customers initiate outside of the app.
