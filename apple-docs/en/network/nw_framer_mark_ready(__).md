---
title: 'nw_framer_mark_ready(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_framer_mark_ready(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_framer_mark_ready(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_mark_ready%28_%3A%29.json'
content_hash: 'sha256:e335b1ba601b9389'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_mark_ready(_:)

<sub>Function</sub>

Indicates to a connection that your protocol’s handshake is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_framer_mark_ready(_ framer: nw_framer_t)
```

## See Also

### Related Documentation

- [nw_framer_start_result_will_mark_ready](nw_framer_start_result_will_mark_ready.md) — The protocol will perform a handshake, preventing the overall connection from becoming ready until [nw_framer_mark_ready](<nw_framer_mark_ready(__).md>) is called.

### Managing Instance Lifetime

- [nw_framer_mark_failed_with_error](<nw_framer_mark_failed_with_error(____).md>) — Indicates to a connection that your protocol has encountered an error, or has gracefully closed.
- [nw_framer_prepend_application_protocol](<nw_framer_prepend_application_protocol(____).md>) — Dynamically adds another protocol that will run above your protocol after your protocol calls [nw_framer_mark_ready](<nw_framer_mark_ready(__).md>).
- [nw_framer_set_stop_handler](<nw_framer_set_stop_handler(____).md>) — Sets a block to handle when the connection is being closed.
- [nw_framer_stop_handler_t](nw_framer_stop_handler_t.md) — A handler that requests that your protocol send any final messages to close the connection.
- [nw_framer_set_cleanup_handler](<nw_framer_set_cleanup_handler(____).md>) — Sets a block to handle the final cleanup of allocations made by your protocol instance.
- [nw_framer_cleanup_handler_t](nw_framer_cleanup_handler_t.md) — A handler that tells your protocol to clean up all allocations before being deallocated.
