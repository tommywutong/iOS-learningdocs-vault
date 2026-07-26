---
title: error
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/producticonphase/error
source_url: 'https://developer.apple.com/documentation/storekit/producticonphase/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/producticonphase/error.json'
content_hash: 'sha256:7114530788ae24ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductIconPhase](../producticonphase.md)

# error

<sub>Instance Property</sub>

The error value that indicates the reason a promotional image failed to load.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

The [error](error.md) value is `nil` while the icon is loading, if the icon successfully loads, or if you haven’t set up a promotional image for the in-app purchase in App Store Connect. Use this value as a convenience to access the error value in code that assumes you’ve set up a promotional image.
