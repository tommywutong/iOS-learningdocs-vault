---
title: JSONSerialization.WritingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonserialization/writingoptions
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/writingoptions.json'
content_hash: 'sha256:39aab7398e6dce40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONSerialization](../jsonserialization.md)

# JSONSerialization.WritingOptions

<sub>Structure</sub>

Options for writing JSON data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WritingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating a Writing Options Instance

- [init(rawValue:)](<writingoptions/init(rawvalue_).md>) — Creates a set of JSON formatting options from an integer that represents those options.

### Formatting JSON

- [NSJSONWritingFragmentsAllowed](writingoptions/fragmentsallowed.md) — Specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.
- [NSJSONWritingPrettyPrinted](writingoptions/prettyprinted.md) — Specifies that the output uses white space and indentation to make the resulting data more readable.
- [NSJSONWritingSortedKeys](writingoptions/sortedkeys.md) — Specifies that the output sorts keys in lexicographic order.
- [NSJSONWritingWithoutEscapingSlashes](writingoptions/withoutescapingslashes.md) — Specifies that the output doesn’t prefix slash characters with escape characters.

## See Also

### Creating JSON Data

- [+ dataWithJSONObject:options:error:](<data(withjsonobject_options_).md>) — Returns JSON data from a Foundation object.
- [+ writeJSONObject:toStream:options:error:](<writejsonobject(__to_options_error_).md>) — Writes a given JSON object to a stream.
- [+ isValidJSONObject:](<isvalidjsonobject(__).md>) — Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.
