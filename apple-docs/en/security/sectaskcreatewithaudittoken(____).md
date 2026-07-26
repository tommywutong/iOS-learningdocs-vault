---
title: 'SecTaskCreateWithAuditToken(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectaskcreatewithaudittoken(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectaskcreatewithaudittoken(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectaskcreatewithaudittoken%28_%3A_%3A%29.json'
content_hash: 'sha256:eb5a28e834ab7ee5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTaskCreateWithAuditToken(_:_:)

<sub>Function</sub>

Creates a task object for the task that sent the Mach message represented by the audit token.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTaskCreateWithAuditToken(_ allocator: CFAllocator?, _ token: audit_token_t) -> SecTask?
```

## Parameters

- `allocator` — An allocator. Pass `NULL` to use the default.

- `token` — The audit token of a Mach message.

## Return Value

A new task, or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this task’s memory when you are done with it.
