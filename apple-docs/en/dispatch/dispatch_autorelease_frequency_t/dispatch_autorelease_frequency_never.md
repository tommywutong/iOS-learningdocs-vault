---
title: DISPATCH_AUTORELEASE_FREQUENCY_NEVER
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_never
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_never'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_never.json'
content_hash: 'sha256:8a66c40277c0174f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [dispatch_autorelease_frequency_t](../dispatch_autorelease_frequency_t.md)

# DISPATCH_AUTORELEASE_FREQUENCY_NEVER

<sub>Enumeration Case</sub>

The queue does not set up an autorelease pool around executed blocks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
DISPATCH_AUTORELEASE_FREQUENCY_NEVER
```

## Discussion

This option is the default behavior for the system-defined global queues.

## See Also

### Autorelease Frequency Options

- [DISPATCH_AUTORELEASE_FREQUENCY_INHERIT](dispatch_autorelease_frequency_inherit.md) — The queue inherits its autorelease frequency from its target queue.
- [DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM](dispatch_autorelease_frequency_work_item.md) — The queue configures an autorelease pool before the execution of a block and releases the objects in that pool after the block finishes executing.
