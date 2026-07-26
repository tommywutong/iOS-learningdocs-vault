---
title: DISPATCH_BLOCK_ASSIGN_CURRENT
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_block_flags_t/dispatch_block_assign_current
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_assign_current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_block_flags_t/dispatch_block_assign_current.json'
content_hash: 'sha256:f1f79117a18a1365'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [dispatch_block_flags_t](../dispatch_block_flags_t.md)

# DISPATCH_BLOCK_ASSIGN_CURRENT

<sub>Enumeration Case</sub>

Set the attributes of the work item to match the attributes of the current execution context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
DISPATCH_BLOCK_ASSIGN_CURRENT
```

## Discussion

Indicates that a dispatch block should be assigned the execution context attributes that are current at the time the block object is created. This applies to attributes such as QoS class, os_activity_t, and properties of the current IPC request, if any. If invoked directly, the block will apply these attributes to the calling thread for the duration of the block body. If the block is submitted to a queue, this flag replaces the default behavior of associating the submitted block instance with the execution context attributes that are current at the time of submission. If a specific QoS class is assigned with [DISPATCH_BLOCK_NO_QOS_CLASS](dispatch_block_no_qos_class.md) or the [dispatch_block_create_with_qos_class](../dispatch_block_create_with_qos_class.md) function, that QoS class takes precedence over the QoS class assignment indicated by this flag.

## See Also

### Flags

- [DISPATCH_BLOCK_BARRIER](dispatch_block_barrier.md) — Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [DISPATCH_BLOCK_DETACHED](dispatch_block_detached.md) — Disassociate the work item’s attributes from the current execution context.
- [DISPATCH_BLOCK_ENFORCE_QOS_CLASS](dispatch_block_enforce_qos_class.md) — Prefer the quality-of-service class associated with the block.
- [DISPATCH_BLOCK_INHERIT_QOS_CLASS](dispatch_block_inherit_qos_class.md) — Prefer the quality-of-service class associated with the current execution context.
- [DISPATCH_BLOCK_NO_QOS_CLASS](dispatch_block_no_qos_class.md) — Execute the work item without assigning a quality-of-service class.
