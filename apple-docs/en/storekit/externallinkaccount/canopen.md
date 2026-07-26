---
title: canOpen
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externallinkaccount/canopen
source_url: 'https://developer.apple.com/documentation/storekit/externallinkaccount/canopen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externallinkaccount/canopen.json'
content_hash: 'sha256:245023878d14c4ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalLinkAccount](../externallinkaccount.md)

# canOpen

<sub>Type Property</sub>

A Boolean value that indicates whether the app can open the external link account.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static var canOpen: Bool { get async }
```

## Discussion

Check this property before showing any user-interface controls that enable people to open the external link account.

Don’t check this property again in response to user input; instead, call [open()](<open().md>) immediately.

> [!important] Important
> Only show user-interface controls that call the [open()](<open().md>) method if this property is `true`. The [open()](<open().md>) method always throws an error when [canOpen](canopen.md) is `false`.

## See Also

### Linking to external accounts

- [open()](<open().md>) — Presents a continuation sheet that enables people to choose whether to open your app’s link to an external website for account creation or management.
