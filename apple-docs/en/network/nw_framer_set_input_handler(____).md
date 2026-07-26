---
title: 'nw_framer_set_input_handler(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_framer_set_input_handler(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_framer_set_input_handler(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_set_input_handler%28_%3A_%3A%29.json'
content_hash: 'sha256:f939361e04dd826d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_set_input_handler(_:_:)

<sub>Function</sub>

Sets a block to handle new inbound data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_framer_set_input_handler(_ framer: nw_framer_t, _ input_handler: @escaping nw_framer_input_handler_t)
```

## See Also

### Handling Input Data

- [nw_framer_input_handler_t](nw_framer_input_handler_t.md) — A handler that notifies your protocol that new inbound data is available to parse.
- [nw_framer_parse_input](<nw_framer_parse_input(__________).md>) — Examines the content of input data while inside your input handler block.
- [nw_framer_parse_completion_t](nw_framer_parse_completion_t.md) — A handler that examines a range of data being sent or received.
- [nw_framer_deliver_input](<nw_framer_deliver_input(__________).md>) — Delivers an inbound message containing arbitrary data from your protocol to the application.
- [nw_framer_deliver_input_no_copy](<nw_framer_deliver_input_no_copy(________).md>) — Delivers an inbound message containing a specific number of next received bytes.
- [nw_framer_pass_through_input](<nw_framer_pass_through_input(__).md>) — Indicates that your protocol no longer needs to handle input data.
