---
title: ExternalPurchaseCustomLink.NoticeType.browser
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.1+, iPadOS 18.1+, macOS 15.1+, tvOS 18.1+, visionOS 2.1+, watchOS 11.1+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externalpurchasecustomlink/noticetype/browser
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticetype/browser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchasecustomlink/noticetype/browser.json'
content_hash: 'sha256:66b3f7035d50418b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [ExternalPurchaseCustomLink](../../externalpurchasecustomlink.md) · [NoticeType](../noticetype.md)

# ExternalPurchaseCustomLink.NoticeType.browser

<sub>Case</sub>

A notice type that indicates your app displays external purchases in a destination of your choice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case browser
```

## Discussion

After displaying a notice with this notice type using [showNotice(type:)](<../shownotice(type_).md>), if the customer chooses to continue, the app goes to the background and presents external purchases in a destination outside of the app.

## See Also

### Getting notice types

- [ExternalPurchaseCustomLink.NoticeType.withinApp](withinapp.md) — A notice type that indicates that you display the destination in a web view or native experience within the app.
