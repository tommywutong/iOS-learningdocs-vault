---
title: open()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externallinkaccount/open()
source_url: 'https://developer.apple.com/documentation/storekit/externallinkaccount/open()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externallinkaccount/open%28%29.json'
content_hash: 'sha256:aa5da0a7a788ca3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalLinkAccount](../externallinkaccount.md)

# open()

<sub>Type Method</sub>

Presents a continuation sheet that enables people to choose whether to open your app’s link to an external website for account creation or management.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static func open() async throws
```

## Discussion

Call this method in response to deliberate user interaction, for example, tapping a button. Call [canOpen](canopen.md) to determine whether to display a button or other user-interface control. If [canOpen](canopen.md) is `false`, this method always throws a [StoreKitError](../storekiterror.md) instance.

## See Also

### Linking to external accounts

- [canOpen](canopen.md) — A Boolean value that indicates whether the app can open the external link account.
