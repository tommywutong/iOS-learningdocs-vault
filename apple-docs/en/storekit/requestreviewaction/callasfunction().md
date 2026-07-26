---
title: callAsFunction()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/requestreviewaction/callasfunction()
source_url: 'https://developer.apple.com/documentation/storekit/requestreviewaction/callasfunction()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/requestreviewaction/callasfunction%28%29.json'
content_hash: 'sha256:9cf44c8e3c81333d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [RequestReviewAction](../requestreviewaction.md)

# callAsFunction()

<sub>Instance Method</sub>

Tells StoreKit to ask the user to rate or review your app, if appropriate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor func callAsFunction()
```

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [RequestReviewAction](../requestreviewaction.md) instance that you get from the [requestReview](../../swiftui/environmentvalues/requestreview.md) environment value.

For information about how Swift uses the [callAsFunction()](<callasfunction().md>)method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
