---
title: nw_ws_opcode_cont
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_ws_opcode_cont
source_url: 'https://developer.apple.com/documentation/network/nw_ws_opcode_cont'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_ws_opcode_cont.json'
content_hash: 'sha256:496be3bb44ca3c30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_ws_opcode_cont

<sub>Global Variable</sub>

A continuation message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_ws_opcode_cont: nw_ws_opcode_t { get }
```

## Discussion

Continuations are handled automatically, and should not be manually sent.

## See Also

### Data Types

- [nw_ws_opcode_binary](nw_ws_opcode_binary.md) — A binary data message.
- [nw_ws_opcode_text](nw_ws_opcode_text.md) — A text data message.
