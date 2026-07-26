---
title: 'ProductIconPhase.failure(_:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/producticonphase/failure(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/producticonphase/failure(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/producticonphase/failure%28_%3A%29.json'
content_hash: 'sha256:db44f4caf6b2160f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductIconPhase](../producticonphase.md)

# ProductIconPhase.failure(_:)

<sub>Case</sub>

The promotional image failed to load, with an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failure(any Error)
```

## Parameters

- `Error` — The reason that the promotional image failed to load.

## See Also

### Getting the promotional image’s load phases

- [ProductIconPhase.loading](loading.md) — The promotional image is in the process of loading.
- [ProductIconPhase.success(_:)](<success(__).md>) — The promotional image successfully loaded.
- [ProductIconPhase.unavailable](unavailable.md) — The promotional image isn’t available for download.
