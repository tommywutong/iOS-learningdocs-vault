---
title: memoryDataMoved
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/macherror/memorydatamoved
source_url: 'https://developer.apple.com/documentation/foundation/macherror/memorydatamoved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/macherror/memorydatamoved.json'
content_hash: 'sha256:618c7a544a10a299'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MachError](../macherror.md)

# memoryDataMoved

<sub>Type Property</sub>

A page was requested of a memory manager via memory_object_data_request for an object using a MEMORY_OBJECT_COPY_CALL strategy, with the VM_PROT_WANTS_COPY flag being used to specify that the page desired is for a copy of the object, and the memory manager has detected the page was pushed into a copy of the object while the kernel was walking the shadow chain from the copy to the object. This error code is delivered via memory_object_data_error and is handled by the kernel (it forces the kernel to restart the fault). It will not be seen by users.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var memoryDataMoved: MachError.Code { get }
```
