---
title: retries
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/retry/retries
source_url: 'https://developer.apple.com/documentation/combine/publishers/retry/retries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/retry/retries.json'
content_hash: 'sha256:67ca6665dd02c1a6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Retry](../retry.md)

# retries

<sub>Instance Property</sub>

The maximum number of retry attempts to perform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let retries: Int?
```

## Discussion

If `nil`, this publisher attempts to reconnect with the upstream publisher an unlimited number of times.

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
