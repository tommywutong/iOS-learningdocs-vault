---
title: nw_framer_output_handler_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_framer_output_handler_t
source_url: 'https://developer.apple.com/documentation/network/nw_framer_output_handler_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_output_handler_t.json'
content_hash: 'sha256:600286ee0641258b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_output_handler_t

<sub>Type Alias</sub>

A handler that notifies your protocol about a new outbound message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_framer_output_handler_t = (nw_framer_t, nw_framer_message_t, Int, Bool) -> Void
```

## Parameters

- `framer` — The framer instance associated with the connection.

- `message` — The framer message passed by the application.

- `message_length` — The length of the message content being sent.

- `is_complete` — A boolean indicating if this the last chunk of a message.

## Discussion

The output handler is your opportunity to encapsulate or encode a signle application message. You should write any output using [nw_framer_write_output](<nw_framer_write_output(______).md>), [nw_framer_write_output_data](<nw_framer_write_output_data(____).md>), or [nw_framer_write_output_no_copy](<nw_framer_write_output_no_copy(____).md>) before returning from the output handler. If you do not write a message, the application message will be discarded.

## See Also

### Handling Output Data

- [nw_framer_set_output_handler](<nw_framer_set_output_handler(____).md>) — Sets a block to handle new outbound messages.
- [nw_framer_parse_output](<nw_framer_parse_output(__________).md>) — Examines the content of output data while inside your output handler.
- [nw_framer_parse_completion_t](nw_framer_parse_completion_t.md) — A handler that examines a range of data being sent or received.
- [nw_framer_write_output](<nw_framer_write_output(______).md>) — Sends arbitrary output data in a buffer from your protocol to the next protocol.
- [nw_framer_write_output_data](<nw_framer_write_output_data(____).md>) — Sends arbitrary output data from your protocol to the next protocol.
- [nw_framer_write_output_no_copy](<nw_framer_write_output_no_copy(____).md>) — Sends a specific number of bytes from a message while inside your output handler.
- [nw_framer_pass_through_output](<nw_framer_pass_through_output(__).md>) — Indicates that your protocol no longer needs to handle output data.
