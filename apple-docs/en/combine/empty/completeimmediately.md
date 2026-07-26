---
title: completeImmediately
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/empty/completeimmediately
source_url: 'https://developer.apple.com/documentation/combine/empty/completeimmediately'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/empty/completeimmediately.json'
content_hash: 'sha256:8fd83322b0febc18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Empty](../empty.md)

# completeImmediately

<sub>Instance Property</sub>

A Boolean value that indicates whether the publisher immediately sends a completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let completeImmediately: Bool
```

## Discussion

If `true`, the publisher finishes immediately after sending a subscription to the subscriber. If `false`, it never completes.
