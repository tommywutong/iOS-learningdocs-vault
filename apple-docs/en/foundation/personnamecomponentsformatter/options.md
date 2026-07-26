---
title: PersonNameComponentsFormatter.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/personnamecomponentsformatter/options
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponentsformatter/options.json'
content_hash: 'sha256:a05ee9387e2b107e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponentsFormatter](../personnamecomponentsformatter.md)

# PersonNameComponentsFormatter.Options

<sub>Structure</sub>

Options for formatting person name components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSPersonNameComponentsFormatterPhonetic](options/phonetic.md) — The formatter should format the component object’s `phoneticRepresentation` components instead of its own components.

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>)

## See Also

### Constants

- [Style](style-swift.enum.md) — The formatting styles for person name components.
- [Attributed String Key](../attributed-string-key.md) — This constant is used as a key for person name component attributes in attributed strings returned by the [- annotatedStringFromPersonNameComponents:](<annotatedstring(from_).md>) method
- [Attributed String Components](../attributed-string-components.md) — These constants are used to identify individual components of attributed strings returned by the [- annotatedStringFromPersonNameComponents:](<annotatedstring(from_).md>) method.
- [Component Delimiter](../component-delimiter.md) — This constant defines the delimiter used to separate name components.
