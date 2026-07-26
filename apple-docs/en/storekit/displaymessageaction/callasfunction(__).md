---
title: 'callAsFunction(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/displaymessageaction/callasfunction(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/displaymessageaction/callasfunction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/displaymessageaction/callasfunction%28_%3A%29.json'
content_hash: 'sha256:12131c3eac248e85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [DisplayMessageAction](../displaymessageaction.md)

# callAsFunction(_:)

<sub>Instance Method</sub>

Tells StoreKit to display the App Store message, if appropriate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor func callAsFunction(_ message: Message) throws
```

## Parameters

- `message` — The App Store message to display.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [DisplayMessageAction](../displaymessageaction.md) structure using `message` as an argument.

For information about how Swift uses the [callAsFunction()](<../requestreviewaction/callasfunction().md>) method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
