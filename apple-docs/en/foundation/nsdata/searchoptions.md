---
title: NSData.SearchOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/searchoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/searchoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/searchoptions.json'
content_hash: 'sha256:136c538939ade22b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# NSData.SearchOptions

<sub>Structure</sub>

Options for method used to search data objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SearchOptions
```

## Overview

These options are used with the [- rangeOfData:options:range:](<range(of_options_in_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<searchoptions/init(rawvalue_).md>)

### Constants

- [NSDataSearchBackwards](searchoptions/backwards.md) — Search from the end of the data object.
- [NSDataSearchAnchored](searchoptions/anchored.md) — Search is limited to start (or end, if searching backwards) of the data object.

## See Also

### Finding Data

- [- subdataWithRange:](<subdata(with_).md>) — Returns a new data object containing the data object’s bytes that fall within the limits specified by a given range.
- [- rangeOfData:options:range:](<range(of_options_in_).md>) — Finds and returns the range of the first occurrence of the given data, within the given range, subject to given options.
