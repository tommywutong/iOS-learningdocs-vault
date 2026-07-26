---
title: NSMachPort.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmachport/options
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/options.json'
content_hash: 'sha256:74cc9d436ebe2ce5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPort](../nsmachport.md)

# NSMachPort.Options

<sub>Structure</sub>

Used to remove access rights to a mach port when the `NSMachPort` object is invalidated or destroyed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSMachPortDeallocateReceiveRight](options/deallocatereceiveright.md) — Remove a receive right when the `NSMachPort` object is invalidated or destroyed.
- [NSMachPortDeallocateSendRight](options/deallocatesendright.md) — Deallocate a send right when the `NSMachPort` object is invalidated or destroyed.

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>)
