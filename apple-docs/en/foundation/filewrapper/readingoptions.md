---
title: FileWrapper.ReadingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/readingoptions
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/readingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/readingoptions.json'
content_hash: 'sha256:dbaec3c7d77403df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# FileWrapper.ReadingOptions

<sub>Structure</sub>

Reading options that can be set by the [- initWithURL:options:error:](<init(url_options_)-70161.md>) and [- readFromURL:options:error:](<read(from_options_).md>) methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ReadingOptions
```

## Overview

You can use the `NSFileWrapperReadingImmediate` and `NSFileWrapperReadingWithoutMapping` reading options together to take an exact snapshot of a file-system hierarchy that is safe from all errors (including the ones mentioned above) once reading has succeeded. If reading with both options succeeds, then subsequent invocations of the methods listed in the comment for the `NSFileWrapperReadingImmediate` reading option to the receiver and all its descendant file wrappers will never fail. However, note that reading with both options together is expensive in terms of both I/O and memory for large files, or directories containing large files, or even directories containing many small files.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSFileWrapperReadingImmediate](readingoptions/immediate.md) — The option to read files immediately after creating a file wrapper.
- [NSFileWrapperReadingWithoutMapping](readingoptions/withoutmapping.md) — Whether file mapping for regular file wrappers is disallowed.

### Initializers

- [init(rawValue:)](<readingoptions/init(rawvalue_).md>)

## See Also

### Constants

- [WritingOptions](writingoptions.md) — Writing options that can be set by the [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>) method.
