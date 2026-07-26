---
title: SKAdNetwork 1 release notes
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadnetwork-1-release-notes
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork-1-release-notes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork-1-release-notes.json'
content_hash: 'sha256:4539c6d32e3d31b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [Ad network attribution](ad-network-attribution.md) · [SKAdNetwork](skadnetwork.md) · [SKAdNetwork release notes](skadnetwork-release-notes.md)

# SKAdNetwork 1 release notes

<sub>Article</sub>

A version of SKAdNetwork available in iOS 11.3 and later.

## Overview

You’re eligible to receive a version 1.0 postback when any of these conditions are met:

- The source app uses iOS 13.7 SDK or earlier.
- The advertised app is App Store-signed and running on a device with iOS 14 or earlier.

The original install-validation postback doesn’t include a version number. For more information, see [Combining parameters for previous SKAdNetwork postback versions](combining-parameters-for-previous-skadnetwork-postback-versions.md).

When verifying an install-validation postback for version 1.0, use the following Apple P-192 public key:

```
MEkwEwYHKoZIzj0CAQYIKoZIzj0DAQEDMgAEMyHD625uvsmGq4C43cQ9BnfN2xslVT5V1nOmAMP6qaRRUll3PB1JYmgSm+62sosG
```

For more information, see [Verifying an install-validation postback](verifying-an-install-validation-postback.md).

### New features

This is the original version of SKAdNetwork.

## See Also

### SKAdNetwork versions

- [SKAdNetwork 4 release notes](skadnetwork-4-release-notes.md) — A version of SKAdNetwork available in iOS 16.1 and later.
- [SKAdNetwork 3 release notes](skadnetwork-3-release-notes.md) — A version of SKAdNetwork available in iOS 14.6 and later.
- [SKAdNetwork 2.2 release notes](skadnetwork-2-2-release-notes.md) — A version of SKAdNetwork available in iOS 14.5 and later.
- [SKAdNetwork 2.1 release notes](skadnetwork-2-1-release-notes.md) — A version of SKAdNetwork available in iOS 14 and later.
- [SKAdNetwork 2 release notes](skadnetwork-2-release-notes.md) — A version of SKAdNetwork available in iOS 14 and later.
