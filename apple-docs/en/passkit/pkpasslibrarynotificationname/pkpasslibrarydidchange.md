---
title: PKPassLibraryDidChange
framework: PassKit (Apple Pay and Wallet)
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.12+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/passkit/pkpasslibrarynotificationname/pkpasslibrarydidchange
source_url: 'https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname/pkpasslibrarydidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/pkpasslibrarynotificationname/pkpasslibrarydidchange.json'
content_hash: 'sha256:008158984f4ac043'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PassKit (Apple Pay and Wallet)](../../passkit.md) · [PKPassLibraryNotificationName](../pkpasslibrarynotificationname.md)

# PKPassLibraryDidChange

<sub>Type Property</sub>

A notification that PassKit posts when the pass library changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let PKPassLibraryDidChange: PKPassLibraryNotificationName
```

## Discussion

PassKit posts this notification on an arbitary queue, and only does so if an instance of `PKPassLibrary` exists. The notification’s user info dictionary describes the changes. See [PKPassLibrary](../pkpasslibrary.md) for the keys it uses.

## See Also

### Notification names

- [PKPassLibraryRemotePaymentPassesDidChangeNotification](pkpasslibraryremotepaymentpassesdidchange.md) — A notification that PassKit posts when it adds or removes a pass on a paired remote device.
