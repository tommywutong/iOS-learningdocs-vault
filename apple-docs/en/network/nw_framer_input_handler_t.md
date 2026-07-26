---
title: nw_framer_input_handler_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_framer_input_handler_t
source_url: 'https://developer.apple.com/documentation/network/nw_framer_input_handler_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_input_handler_t.json'
content_hash: 'sha256:e0e439afc8367978'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_input_handler_t

<sub>Type Alias</sub>

A handler that notifies your protocol that new inbound data is available to parse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_framer_input_handler_t = (nw_framer_t) -> Int
```

## See Also

### Handling Input Data

- [nw_framer_set_input_handler](<nw_framer_set_input_handler(____).md>) — Sets a block to handle new inbound data.
- [nw_framer_parse_input](<nw_framer_parse_input(__________).md>) — Examines the content of input data while inside your input handler block.
- [nw_framer_parse_completion_t](nw_framer_parse_completion_t.md) — A handler that examines a range of data being sent or received.
- [nw_framer_deliver_input](<nw_framer_deliver_input(__________).md>) — Delivers an inbound message containing arbitrary data from your protocol to the application.
- [nw_framer_deliver_input_no_copy](<nw_framer_deliver_input_no_copy(________).md>) — Delivers an inbound message containing a specific number of next received bytes.
- [nw_framer_pass_through_input](<nw_framer_pass_through_input(__).md>) — Indicates that your protocol no longer needs to handle input data.
