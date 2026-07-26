---
title: MirrorPath
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mirrorpath
source_url: 'https://developer.apple.com/documentation/swift/mirrorpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirrorpath.json'
content_hash: 'sha256:c785949749500346'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# MirrorPath

<sub>Protocol</sub>

A protocol for legitimate arguments to `Mirror`’s `descendant` method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MirrorPath
```

## Overview

Do not declare new conformances to this protocol; they will not work as expected.

## Relationships

- **Conforming Types**: [Int](int.md), [String](string.md)

## See Also

### Querying Descendants

- [descendant(_:_:)](<mirror/descendant(____).md>) — Returns a specific descendant of the reflected subject, or `nil` if no such descendant exists.
