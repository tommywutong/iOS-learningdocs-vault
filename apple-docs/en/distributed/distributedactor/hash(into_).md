---
title: 'hash(into:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedactor/hash(into:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedactor/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactor/hash%28into%3A%29.json'
content_hash: 'sha256:70c0b52da4baf239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActor](../distributedactor.md)

# hash(into:)

<sub>Instance Method</sub>

A distributed actor’s hash and equality is implemented by directly delegating to its [id](id.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func hash(into hasher: inout Hasher)
```

## Discussion

For more details see the “Hashable and Identifiable conformance” section of [DistributedActor](../distributedactor.md).
