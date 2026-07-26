---
title: 'SecTaskCreateFromSelf(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectaskcreatefromself(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectaskcreatefromself(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectaskcreatefromself%28_%3A%29.json'
content_hash: 'sha256:a8f4aa37deca16f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTaskCreateFromSelf(_:)

<sub>Function</sub>

Creates a task object for the current task.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTaskCreateFromSelf(_ allocator: CFAllocator?) -> SecTask?
```

## Parameters

- `allocator` — An allocator. Pass `NULL` to use the default.

## Return Value

A new task, or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this task’s memory when you are done with it.
