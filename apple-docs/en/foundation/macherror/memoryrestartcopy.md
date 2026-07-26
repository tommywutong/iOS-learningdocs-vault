---
title: memoryRestartCopy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/macherror/memoryrestartcopy
source_url: 'https://developer.apple.com/documentation/foundation/macherror/memoryrestartcopy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/macherror/memoryrestartcopy.json'
content_hash: 'sha256:5b27f5796f37922c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MachError](../macherror.md)

# memoryRestartCopy

<sub>Type Property</sub>

A strategic copy was attempted of an object upon which a quicker copy is now possible.  The caller should retry the copy using vm_object_copy_quickly. This error code is seen only by the kernel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var memoryRestartCopy: MachError.Code { get }
```
