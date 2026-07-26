---
title: CFRange
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrange
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrange.json'
content_hash: 'sha256:ff4ed4ef316fef12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRange

<sub>Structure</sub>

A structure representing a range of sequential items in a container, such as characters in a buffer or elements in a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFRange
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfrange/init().md>)
- [init(location:length:)](<cfrange/init(location_length_).md>)

### Instance Properties

- [length](cfrange/length.md) — An integer representing the number of items in the range. For type compatibility with the rest of the system, `LONG_MAX` is the maximum value you should use for length.
- [location](cfrange/location.md) — An integer representing the starting location of the range. For type compatibility with the rest of the system, `LONG_MAX` is the maximum value you should use for location.

## See Also

### Data Types

- [CFIndex](cfindex.md) — Priority values used for kAXPriorityKey
- [CFOptionFlags](cfoptionflags.md) — A bitfield used for passing special allocation and other requests into Core Foundation functions.
