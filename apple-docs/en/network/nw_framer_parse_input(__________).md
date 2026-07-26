---
title: 'nw_framer_parse_input(_:_:_:_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_framer_parse_input(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_framer_parse_input(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_parse_input%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0232f667de1da1b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_parse_input(_:_:_:_:_:)

<sub>Function</sub>

Examines the content of input data while inside your input handler block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_framer_parse_input(_ framer: nw_framer_t, _ minimum_incomplete_length: Int, _ maximum_length: Int, _ temp_buffer: UnsafeMutablePointer<UInt8>?, _ parse: (UnsafeMutablePointer<UInt8>?, Int, Bool) -> Int) -> Bool
```

## Parameters

- `framer` — A network framer instance.

- `minimum_incomplete_length` — The minimum number of bytes that should be delivered to the parse completion.

- `maximum_length` — The maximum number of bytes that should be delivered to the parse completion.

- `temp_buffer` — An optional buffer into which the parser will copy bytes. Use this if you need to make guarantees about byte alignment.

- `parse` — A completion handler that will be called inline to examine a region of bytes.

## Return Value

Returns true if the requested length was available to parse, or false if the conditions could not be met.

## See Also

### Handling Input Data

- [nw_framer_set_input_handler](<nw_framer_set_input_handler(____).md>) — Sets a block to handle new inbound data.
- [nw_framer_input_handler_t](nw_framer_input_handler_t.md) — A handler that notifies your protocol that new inbound data is available to parse.
- [nw_framer_parse_completion_t](nw_framer_parse_completion_t.md) — A handler that examines a range of data being sent or received.
- [nw_framer_deliver_input](<nw_framer_deliver_input(__________).md>) — Delivers an inbound message containing arbitrary data from your protocol to the application.
- [nw_framer_deliver_input_no_copy](<nw_framer_deliver_input_no_copy(________).md>) — Delivers an inbound message containing a specific number of next received bytes.
- [nw_framer_pass_through_input](<nw_framer_pass_through_input(__).md>) — Indicates that your protocol no longer needs to handle input data.
