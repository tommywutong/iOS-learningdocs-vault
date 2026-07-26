---
title: 'noDelay(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/nodelay(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/nodelay(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/nodelay%28_%3A%29.json'
content_hash: 'sha256:5496eb91e8b8ee85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# noDelay(_:)

<sub>Instance Method</sub>

Disable Nagle’s algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func noDelay(_ noDelay: Bool) -> TCP
```

## Parameters

- `noDelay` — True to disable Nagle’s algorithm, false otherwise.

## Discussion

A boolean indicating that TCP should disable Nagle’s algorithm (`TCP_NODELAY`).
