---
title: SKStoreReviewController
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.3+（18.0 起废弃）, iPadOS 10.3+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14+（15.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skstorereviewcontroller
source_url: 'https://developer.apple.com/documentation/storekit/skstorereviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstorereviewcontroller.json'
content_hash: 'sha256:e89c23db246f6c67'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreReviewController

<sub>Class</sub>

An object that controls the process of requesting App Store ratings and reviews from customers.

> [!warning] Deprecated
> Use [RequestReviewAction](requestreviewaction.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class SKStoreReviewController
```

## Overview

Use the [+ requestReviewInScene:](<skstorereviewcontroller/requestreview(in_).md>) method to indicate when it makes sense within the logic of your app to ask the customer for ratings and reviews.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Indicating an appropriate time for a review

- [+ requestReviewInScene:](<skstorereviewcontroller/requestreview(in_).md>) — Tells StoreKit to ask the customer to rate or review the app, if appropriate, using the specified scene. _(deprecated)_
- [+ requestReview](<skstorereviewcontroller/requestreview().md>) — Tells StoreKit to ask the customer to rate or review your app, if appropriate. _(deprecated)_

## See Also

### Reviews

- [Requesting App Store reviews](requesting-app-store-reviews.md) — Implement best practices for prompting users to review your app in the App Store.
- [RequestReviewAction](requestreviewaction.md) — An instance that tells StoreKit to request an App Store rating or review, if appropriate.
