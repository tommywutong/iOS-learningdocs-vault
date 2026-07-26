---
title: memoryFailure
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/macherror/memoryfailure
source_url: 'https://developer.apple.com/documentation/foundation/macherror/memoryfailure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/macherror/memoryfailure.json'
content_hash: 'sha256:b5c8c25194eca5dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MachError](../macherror.md)

# memoryFailure

<sub>Type Property</sub>

During a page fault, the target address refers to a memory object that has been destroyed.  This failure is permanent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var memoryFailure: MachError.Code { get }
```
