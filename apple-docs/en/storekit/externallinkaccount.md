---
title: ExternalLinkAccount
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/externallinkaccount
source_url: 'https://developer.apple.com/documentation/storekit/externallinkaccount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externallinkaccount.json'
content_hash: 'sha256:3e49d49e6a551f5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# ExternalLinkAccount

<sub>Enumeration</sub>

Enables qualifying apps to link to an external website for account creation or management.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
enum ExternalLinkAccount
```

## Overview

This functionality is only available to apps with the [com.apple.developer.storekit.external-link.account](../bundleresources/entitlements/com.apple.developer.storekit.external-link.account.md) entitlement. For more information, see [Distributing “reader” apps with a link to your website](https://developer.apple.com/support/reader-apps/).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Linking to external accounts

- [canOpen](externallinkaccount/canopen.md) — A Boolean value that indicates whether the app can open the external link account.
- [open()](<externallinkaccount/open().md>) — Presents a continuation sheet that enables people to choose whether to open your app’s link to an external website for account creation or management.

## See Also

### External accounts

- [com.apple.developer.storekit.external-link.account](../bundleresources/entitlements/com.apple.developer.storekit.external-link.account.md) — A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [SKExternalLinkAccount](../bundleresources/information-property-list/skexternallinkaccount.md) — A dictionary that contains localized URLs to an external website for account creation or management.
