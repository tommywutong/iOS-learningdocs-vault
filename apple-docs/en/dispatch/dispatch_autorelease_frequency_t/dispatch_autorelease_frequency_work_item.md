---
title: DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_work_item
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_work_item'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_work_item.json'
content_hash: 'sha256:eeff4d2bef703dd1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [dispatch_autorelease_frequency_t](../dispatch_autorelease_frequency_t.md)

# DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM

<sub>Enumeration Case</sub>

The queue configures an autorelease pool before the execution of a block and releases the objects in that pool after the block finishes executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM
```

## See Also

### Autorelease Frequency Options

- [DISPATCH_AUTORELEASE_FREQUENCY_INHERIT](dispatch_autorelease_frequency_inherit.md) — The queue inherits its autorelease frequency from its target queue.
- [DISPATCH_AUTORELEASE_FREQUENCY_NEVER](dispatch_autorelease_frequency_never.md) — The queue does not set up an autorelease pool around executed blocks.
