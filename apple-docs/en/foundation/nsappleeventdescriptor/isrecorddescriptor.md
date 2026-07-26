---
title: isRecordDescriptor
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor/isrecorddescriptor
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/isrecorddescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/isrecorddescriptor.json'
content_hash: 'sha256:b3159b691d3f470c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# isRecordDescriptor

<sub>Instance Property</sub>

Returns whether or not the receiver is a record-like descriptor.

<sub>macOS</sub>

```swift
var isRecordDescriptor: Bool { get }
```

## Discussion

Record-like descriptors function as records, but may have a `descriptorType` other than `typeAERecord`, such as `typeObjectSpecifier`.
