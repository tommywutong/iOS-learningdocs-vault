---
title: 'noOptions(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/nooptions(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/nooptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/nooptions%28_%3A%29.json'
content_hash: 'sha256:01fd71bfcab8876d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# noOptions(_:)

<sub>Instance Method</sub>

Enable no-options mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func noOptions(_ noOptions: Bool) -> TCP
```

## Parameters

- `noOptions` — True to use no-options mode, false otherwise.

## Discussion

A boolean indicating that TCP should use no-options mode (`TCP_NOOPT`).
