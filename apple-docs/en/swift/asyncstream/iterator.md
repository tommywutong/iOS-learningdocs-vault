---
title: AsyncStream.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncstream/iterator
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/iterator.json'
content_hash: 'sha256:93ee5dadd99f8eb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncStream](../asyncstream.md)

# AsyncStream.Iterator

<sub>Structure</sub>

The asynchronous iterator for iterating an asynchronous stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Iterator
```

## Overview

This type doesn’t conform to `Sendable`. Don’t use it from multiple concurrent contexts. It is a programmer error to invoke `next()` from a concurrent context that contends with another such call, which results in a call to `fatalError()`.

## Relationships

- **Conforms To**: [AsyncIteratorProtocol](../asynciteratorprotocol.md)

## Topics

### Iterating over Elements

- [next()](<iterator/next().md>) — The next value from the asynchronous stream.

### Instance Methods

- [next(isolation:)](<iterator/next(isolation_).md>) — The next value from the asynchronous stream.

### Default Implementations

- [AsyncIteratorProtocol Implementations](iterator/asynciteratorprotocol-implementations.md)

## See Also

### Creating an Iterator

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
