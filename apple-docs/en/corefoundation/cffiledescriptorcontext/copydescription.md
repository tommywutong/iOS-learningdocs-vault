---
title: copyDescription
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cffiledescriptorcontext/copydescription
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/copydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptorcontext/copydescription.json'
content_hash: 'sha256:f9d76176677b9aa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFFileDescriptorContext](../cffiledescriptorcontext.md)

# copyDescription

<sub>Instance Property</sub>

The callback used to create a descriptive string representation of the CFFileDescriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!
```
