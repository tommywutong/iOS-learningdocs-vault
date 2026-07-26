---
title: cancel()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnectiongroup/cancel()
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/cancel%28%29.json'
content_hash: 'sha256:cf7bfe1bbb649369'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# cancel()

<sub>Instance Method</sub>

Cancels the connection group object and leaves the network group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func cancel()
```

## See Also

### Managing Groups

- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives connection group state updates.
- [State](state-swift.enum.md) — States that indicate whether you can use a connection group to send and receive messages.
- [state](state-swift.property.md) — The current state of the connection group.
