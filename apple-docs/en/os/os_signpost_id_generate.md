---
title: os_signpost_id_generate
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_signpost_id_generate
source_url: 'https://developer.apple.com/documentation/os/os_signpost_id_generate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost_id_generate.json'
content_hash: 'sha256:9f0ca2413f5f128e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_signpost_id_generate

<sub>Function</sub>

Creates a signpost identifier that’s unique among signposts logged to a specified log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_signpost_id_t os_signpost_id_generate(os_log_t log);
```

## See Also

### Creating a Signpost Identifier

- [os_signpost_id_make_with_pointer](os_signpost_id_make_with_pointer.md) — Creates a signpost identifier that’s unique among signposts logging to the specified log, using a pointer value to generate the unique value.
