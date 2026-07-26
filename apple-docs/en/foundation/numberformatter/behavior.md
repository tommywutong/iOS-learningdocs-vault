---
title: NumberFormatter.Behavior
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/behavior
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/behavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/behavior.json'
content_hash: 'sha256:0f2807f6b938c3d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# NumberFormatter.Behavior

<sub>Enumeration</sub>

These constants specify the behavior of a number formatter. These constants are returned by the [+ defaultFormatterBehavior](<defaultformatterbehavior().md>) class method and the [formatterBehavior](formatterbehavior.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Behavior
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSNumberFormatterBehaviorDefault](behavior/default.md) — The number-formatter behavior set as the default for new instances. You can set the default formatter behavior with the class method [+ setDefaultFormatterBehavior:](<setdefaultformatterbehavior(__).md>).
- [NSNumberFormatterBehavior10_0](behavior/behavior10_0.md) — The number-formatter behavior as it existed prior to macOS 10.4.
- [NSNumberFormatterBehavior10_4](behavior/behavior10_4.md) — The number-formatter behavior since macOS 10.4.

### Initializers

- [init(rawValue:)](<behavior/init(rawvalue_).md>)

## See Also

### Constants

- [Style](style.md) — The predefined number format styles used by the [numberStyle](numberstyle.md) property.
- [PadPosition](padposition.md) — These constants are used to specify how numbers should be padded. These constants are used by the [paddingPosition](paddingposition.md) property.
- [RoundingMode](roundingmode-swift.enum.md) — These constants are used to specify how numbers should be rounded. These constants are used by the [roundingMode](roundingmode-swift.property.md) property.
