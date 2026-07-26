---
title: 'persistTimeout(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/persisttimeout(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/persisttimeout(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/persisttimeout%28_%3A%29.json'
content_hash: 'sha256:a7dc19ba29418d65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# persistTimeout(_:)

<sub>Instance Method</sub>

Set the TCP persist timeout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func persistTimeout(_ timeout: UInt32) -> TCP
```

## Parameters

- `timeout` — The persist timeout, in seconds.

## Discussion

The TCP persist timeout, in seconds (`PERSIST_TIMEOUT`). See RFC 6429.
