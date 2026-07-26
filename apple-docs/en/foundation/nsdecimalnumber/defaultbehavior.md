---
title: defaultBehavior
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumber/defaultbehavior
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/defaultbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/defaultbehavior.json'
content_hash: 'sha256:daf6a0fed852cdd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# defaultBehavior

<sub>Type Property</sub>

The way arithmetic methods round off and handle error conditions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var defaultBehavior: any NSDecimalNumberBehaviors { get set }
```

## Discussion

By default, the arithmetic methods use the `NSRoundPlain` behavior; that is, the methods round to the closest possible return value. The methods assume your need for precision does not exceed 38 significant digits and raise exceptions when they try to divide by 0 or produce a number too big or too small to be represented.

If this default behavior doesn’t suit your application, you should use methods that let you specify the behavior, like [- decimalNumberByAdding:withBehavior:](<adding(__withbehavior_).md>). If you find yourself using a particular behavior consistently, you can specify a different default behavior with `setDefaultBehavior(_:)`.

The default behavior is maintained separately for each thread in your app.

## See Also

### Managing Behavior

- [NSDecimalNumberBehaviors](../nsdecimalnumberbehaviors.md) — A protocol that declares three methods that control the discretionary aspects of working with decimal numbers.
- [NSDecimalNumberHandler](../nsdecimalnumberhandler.md) — A class that adopts the decimal number behaviors protocol.
