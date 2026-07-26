---
title: PKPassLibraryRemotePaymentPassesDidChange
framework: PassKit (Apple Pay and Wallet)
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.12+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/passkit/pkpasslibrarynotificationname/pkpasslibraryremotepaymentpassesdidchange
source_url: 'https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname/pkpasslibraryremotepaymentpassesdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/pkpasslibrarynotificationname/pkpasslibraryremotepaymentpassesdidchange.json'
content_hash: 'sha256:2953408d2b6cd731'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PassKit (Apple Pay and Wallet)](../../passkit.md) · [PKPassLibraryNotificationName](../pkpasslibrarynotificationname.md)

# PKPassLibraryRemotePaymentPassesDidChange

<sub>Type Property</sub>

A notification that PassKit posts when it adds or removes a pass on a paired remote device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let PKPassLibraryRemotePaymentPassesDidChange: PKPassLibraryNotificationName
```

## Discussion

PassKit posts this notification on an arbitary queue, and only does so if an instance of `PKPassLibrary` exists. The notification’s user info dictionary describes the changes. See [PKPassLibrary](../pkpasslibrary.md) for the keys it uses.

## See Also

### Notification names

- [PKPassLibraryDidChangeNotification](pkpasslibrarydidchange.md) — A notification that PassKit posts when the pass library changes.
