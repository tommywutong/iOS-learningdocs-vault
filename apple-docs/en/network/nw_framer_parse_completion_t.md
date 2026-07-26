---
title: nw_framer_parse_completion_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_framer_parse_completion_t
source_url: 'https://developer.apple.com/documentation/network/nw_framer_parse_completion_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_parse_completion_t.json'
content_hash: 'sha256:ab68055b393e4002'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_parse_completion_t

<sub>Type Alias</sub>

A handler that examines a range of data being sent or received.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_framer_parse_completion_t = (UnsafeMutablePointer<UInt8>?, Int, Bool) -> Int
```

## Parameters

- `buffer` — The pointer to bytes to parse.

- `buffer_length` — The length of the buffer.

- `is_complete` — A boolean indicating if this span of bytes represents the end of a message.

## Return Value

Return the number of bytes by which to increment the input or output cursor. Once the cursor is moved, previous bytes will no longer be delivered to [nw_framer_parse_input](<nw_framer_parse_input(__________).md>) and [nw_framer_deliver_input_no_copy](<nw_framer_deliver_input_no_copy(________).md>) for input data, or [nw_framer_parse_output](<nw_framer_parse_output(__________).md>) and [nw_framer_write_output_no_copy](<nw_framer_write_output_no_copy(____).md>) for output messages.

## See Also

### Handling Output Data

- [nw_framer_set_output_handler](<nw_framer_set_output_handler(____).md>) — Sets a block to handle new outbound messages.
- [nw_framer_output_handler_t](nw_framer_output_handler_t.md) — A handler that notifies your protocol about a new outbound message.
- [nw_framer_parse_output](<nw_framer_parse_output(__________).md>) — Examines the content of output data while inside your output handler.
- [nw_framer_write_output](<nw_framer_write_output(______).md>) — Sends arbitrary output data in a buffer from your protocol to the next protocol.
- [nw_framer_write_output_data](<nw_framer_write_output_data(____).md>) — Sends arbitrary output data from your protocol to the next protocol.
- [nw_framer_write_output_no_copy](<nw_framer_write_output_no_copy(____).md>) — Sends a specific number of bytes from a message while inside your output handler.
- [nw_framer_pass_through_output](<nw_framer_pass_through_output(__).md>) — Indicates that your protocol no longer needs to handle output data.
