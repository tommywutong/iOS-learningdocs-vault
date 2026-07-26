---
title: 'noPush(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/nopush(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/nopush(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/nopush%28_%3A%29.json'
content_hash: 'sha256:f517b02a08c72ad6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# noPush(_:)

<sub>Instance Method</sub>

Enable no-push mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func noPush(_ noPush: Bool) -> TCP
```

## Parameters

- `noPush` — True to use no-push mode, false otherwise.

## Discussion

A boolean indicating that TCP should use no-push mode (`TCP_NOPUSH`).
