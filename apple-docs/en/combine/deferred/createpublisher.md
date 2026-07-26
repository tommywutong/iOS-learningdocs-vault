---
title: createPublisher
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/deferred/createpublisher
source_url: 'https://developer.apple.com/documentation/combine/deferred/createpublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/deferred/createpublisher.json'
content_hash: 'sha256:4f887a44ed0e94ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Deferred](../deferred.md)

# createPublisher

<sub>Instance Property</sub>

The closure to execute when this deferred publisher receives a subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let createPublisher: () -> DeferredPublisher
```

## Discussion

The publisher returned by this closure immediately receives the incoming subscription.
