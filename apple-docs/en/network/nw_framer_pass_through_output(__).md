---
title: 'nw_framer_pass_through_output(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_framer_pass_through_output(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_framer_pass_through_output(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_pass_through_output%28_%3A%29.json'
content_hash: 'sha256:e1ac9204693d9c65'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_pass_through_output(_:)

<sub>Function</sub>

Indicates that your protocol no longer needs to handle output data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_framer_pass_through_output(_ framer: nw_framer_t)
```

## See Also

### Handling Output Data

- [nw_framer_set_output_handler](<nw_framer_set_output_handler(____).md>) — Sets a block to handle new outbound messages.
- [nw_framer_output_handler_t](nw_framer_output_handler_t.md) — A handler that notifies your protocol about a new outbound message.
- [nw_framer_parse_output](<nw_framer_parse_output(__________).md>) — Examines the content of output data while inside your output handler.
- [nw_framer_parse_completion_t](nw_framer_parse_completion_t.md) — A handler that examines a range of data being sent or received.
- [nw_framer_write_output](<nw_framer_write_output(______).md>) — Sends arbitrary output data in a buffer from your protocol to the next protocol.
- [nw_framer_write_output_data](<nw_framer_write_output_data(____).md>) — Sends arbitrary output data from your protocol to the next protocol.
- [nw_framer_write_output_no_copy](<nw_framer_write_output_no_copy(____).md>) — Sends a specific number of bytes from a message while inside your output handler.
