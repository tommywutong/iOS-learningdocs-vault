---
title: ProductIconPhase.unavailable
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/producticonphase/unavailable
source_url: 'https://developer.apple.com/documentation/storekit/producticonphase/unavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/producticonphase/unavailable.json'
content_hash: 'sha256:c9befc898bc81b1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductIconPhase](../producticonphase.md)

# ProductIconPhase.unavailable

<sub>Case</sub>

The promotional image isn’t available for download.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case unavailable
```

## Discussion

You set up promotional images for in-app purchases in App Store Connect.

## See Also

### Getting the promotional image’s load phases

- [ProductIconPhase.loading](loading.md) — The promotional image is in the process of loading.
- [ProductIconPhase.success(_:)](<success(__).md>) — The promotional image successfully loaded.
- [ProductIconPhase.failure(_:)](<failure(__).md>) — The promotional image failed to load, with an error.
