---
title: commonModes
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopmode/commonmodes
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopmode/commonmodes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopmode/commonmodes.json'
content_hash: 'sha256:15ea936ae4a7ebfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopMode](../cfrunloopmode.md)

# commonModes

<sub>Type Property</sub>

Objects added to a run loop using this value as the mode are monitored by all run loop modes that have been declared as a member of the set of “common” modes with [CFRunLoopAddCommonMode](<../cfrunloopaddcommonmode(____).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let commonModes: CFRunLoopMode!
```
