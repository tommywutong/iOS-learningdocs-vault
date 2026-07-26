---
title: NSData.ReadingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/readingoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/readingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/readingoptions.json'
content_hash: 'sha256:32a906ddabfffb8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# NSData.ReadingOptions

<sub>Structure</sub>

Options for methods used to read data objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ReadingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<readingoptions/init(rawvalue_).md>)

### Constants

- [NSDataReadingMappedIfSafe](readingoptions/mappedifsafe.md) — A hint indicating the file should be mapped into virtual memory, if possible and safe.
- [NSDataReadingUncached](readingoptions/uncached.md) — A hint indicating the file should not be stored in the file-system caches.
- [NSDataReadingMappedAlways](readingoptions/alwaysmapped.md) — Hint to map the file in if possible.

### Legacy Constants

- [NSDataReadingMapped](readingoptions/datareadingmapped.md) — Deprecated name for [NSDataReadingMappedIfSafe](readingoptions/mappedifsafe.md). _(deprecated)_
- [NSMappedRead](readingoptions/mappedread.md) — Deprecated name for [NSDataReadingMapped](readingoptions/datareadingmapped.md). _(deprecated)_
- [NSUncachedRead](readingoptions/uncachedread.md) — Deprecated name for [NSDataReadingUncached](readingoptions/uncached.md). _(deprecated)_

## See Also

### Reading Data from a File

- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a data object with the content of the file at a given path.
- [- initWithContentsOfFile:options:error:](<init(contentsoffile_options_).md>) — Initializes a data object with the content of the file at a given path.
- [- initWithContentsOfMappedFile:](<init(contentsofmappedfile_).md>) — Initializes a data object with the contents of the mapped file specified by a given path. _(deprecated)_
- [+ dataWithContentsOfMappedFile:](<datawithcontentsofmappedfile(__).md>) — Creates a data object from the mapped file at a given path. _(deprecated)_
