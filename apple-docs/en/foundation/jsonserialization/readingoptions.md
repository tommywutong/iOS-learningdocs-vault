---
title: JSONSerialization.ReadingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonserialization/readingoptions
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/readingoptions.json'
content_hash: 'sha256:19f1ed1f9aee4ba0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONSerialization](../jsonserialization.md)

# JSONSerialization.ReadingOptions

<sub>Structure</sub>

Options used when creating Foundation objects from JSON data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ReadingOptions
```

## Overview

Use these options when parsing JSON with [+ JSONObjectWithData:options:error:](<jsonobject(with_options_)-8demi.md>) and [+ JSONObjectWithStream:options:error:](<jsonobject(with_options_)-3afap.md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating a Reading Options Instance

- [init(rawValue:)](<readingoptions/init(rawvalue_).md>) — Creates a set of JSON formatting options from an integer that represents those options.

### Reading Options

- [NSJSONReadingMutableContainers](readingoptions/mutablecontainers.md) — Specifies that arrays and dictionaries in the returned object are mutable.
- [NSJSONReadingMutableLeaves](readingoptions/mutableleaves.md) — Specifies that leaf strings in the JSON object graph are mutable.
- [NSJSONReadingFragmentsAllowed](readingoptions/fragmentsallowed.md) — Specifies that the parser allows top-level objects that aren’t arrays or dictionaries.
- [NSJSONReadingJSON5Allowed](readingoptions/json5allowed.md) — Specifies that reading serialized JSON data supports the JSON5 syntax.
- [NSJSONReadingTopLevelDictionaryAssumed](readingoptions/topleveldictionaryassumed.md) — Specifies that the parser assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with curly braces.
- [NSJSONReadingAllowFragments](readingoptions/allowfragments.md) — A deprecated option that specifies that the parser should allow top-level objects that aren’t arrays or dictionaries. _(deprecated)_

## See Also

### Creating a JSON Object

- [+ JSONObjectWithData:options:error:](<jsonobject(with_options_)-8demi.md>) — Returns a Foundation object from given JSON data.
- [+ JSONObjectWithStream:options:error:](<jsonobject(with_options_)-3afap.md>) — Returns a Foundation object from JSON data in a given stream.
