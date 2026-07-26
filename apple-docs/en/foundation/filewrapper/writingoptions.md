---
title: FileWrapper.WritingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/writingoptions
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/writingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/writingoptions.json'
content_hash: 'sha256:e9dcec0325869318'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# FileWrapper.WritingOptions

<sub>Structure</sub>

Writing options that can be set by the [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>) method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WritingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSFileWrapperWritingAtomic](writingoptions/atomic.md) — Whether writing is done atomically.
- [NSFileWrapperWritingWithNameUpdating](writingoptions/withnameupdating.md) — Whether descendant file wrappers’[filename](filename.md) properties are set if the writing succeeds.

### Initializers

- [init(rawValue:)](<writingoptions/init(rawvalue_).md>)

## See Also

### Constants

- [ReadingOptions](readingoptions.md) — Reading options that can be set by the [- initWithURL:options:error:](<init(url_options_)-70161.md>) and [- readFromURL:options:error:](<read(from_options_).md>) methods.
