---
title: descriptor
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifier/descriptor
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/descriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/descriptor.json'
content_hash: 'sha256:bb51fbd11a2ddda7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# descriptor

<sub>Instance Property</sub>

Returns an Apple event descriptor that represents the receiver.

<sub>macOS</sub>

```swift
@NSCopying var descriptor: NSAppleEventDescriptor? { get }
```

## Return Value

An Apple event descriptor of type `typeObjectSpecifier`.

## Discussion

If the receiver was created with [+ objectSpecifierWithDescriptor:](<init(descriptor_).md>), the passed-in descriptor is returned. Otherwise, a new descriptor is created and returned, autoreleased.
