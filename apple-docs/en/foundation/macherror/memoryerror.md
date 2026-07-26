---
title: memoryError
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/macherror/memoryerror
source_url: 'https://developer.apple.com/documentation/foundation/macherror/memoryerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/macherror/memoryerror.json'
content_hash: 'sha256:3e02d63b7fbf3960'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MachError](../macherror.md)

# memoryError

<sub>Type Property</sub>

During a page fault, the memory object indicated that the data could not be returned.  This failure may be temporary; future attempts to access this same data may succeed, as defined by the memory object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var memoryError: MachError.Code { get }
```
