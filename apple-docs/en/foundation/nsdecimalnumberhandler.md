---
title: NSDecimalNumberHandler
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumberhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumberhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumberhandler.json'
content_hash: 'sha256:55b3fda90420bcbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalNumberHandler

<sub>Class</sub>

A class that adopts the decimal number behaviors protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSDecimalNumberHandler
```

## Overview

This class allows you to set the way an [NSDecimalNumber](nsdecimalnumber.md) object rounds off and handles errors, without having to create a custom class.

You can use an instance of this class as an argument to any of the [NSDecimalNumber](nsdecimalnumber.md) methods that end with `...Behavior:`. If you don’t think you need special behavior, you probably don’t need this class—it is likely that [NSDecimalNumber](nsdecimalnumber.md)’s default behavior will suit your needs.

For more information, see the [NSDecimalNumberBehaviors](nsdecimalnumberbehaviors.md) protocol specification.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSDecimalNumberBehaviors](nsdecimalnumberbehaviors.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Decimal Number Handler

- [defaultDecimalNumberHandler](nsdecimalnumberhandler/default.md) — Returns the default instance of `NSDecimalNumberHandler`.

### Initializing a decimal number handler

- [- initWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:](<nsdecimalnumberhandler/init(roundingmode_scale_raiseonexactness_raiseonoverflow_raiseonunderflow_raiseondividebyzero_).md>) — Returns an `NSDecimalNumberHandler` object initialized so it behaves as specified by the method’s arguments.

### Initializers

- [init(coder:)](<nsdecimalnumberhandler/init(coder_).md>)

## See Also

### Configuring Rounding Behavior

- [roundingBehavior](numberformatter/roundingbehavior.md) — The rounding behavior used by the receiver.
- [roundingIncrement](numberformatter/roundingincrement.md) — The rounding increment used by the receiver.
- [roundingMode](numberformatter/roundingmode-swift.property.md) — The rounding mode used by the receiver.
