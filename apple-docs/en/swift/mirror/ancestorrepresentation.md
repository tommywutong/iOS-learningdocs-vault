---
title: Mirror.AncestorRepresentation
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mirror/ancestorrepresentation
source_url: 'https://developer.apple.com/documentation/swift/mirror/ancestorrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/ancestorrepresentation.json'
content_hash: 'sha256:6cddc0866f6e93f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Mirror](../mirror.md)

# Mirror.AncestorRepresentation

<sub>Enumeration</sub>

The representation to use for ancestor classes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AncestorRepresentation
```

## Overview

A class that conforms to the `CustomReflectable` protocol can control how its mirror represents ancestor classes by initializing the mirror with an `AncestorRepresentation`. This setting has no effect on mirrors reflecting value type instances.

## Topics

### Enumeration Cases

- [Mirror.AncestorRepresentation.customized(_:)](<ancestorrepresentation/customized(__).md>) — Uses the nearest ancestor’s implementation of `customMirror` to create a mirror for that ancestor.
- [Mirror.AncestorRepresentation.generated](ancestorrepresentation/generated.md) — Generates a default mirror for all ancestor classes.
- [Mirror.AncestorRepresentation.suppressed](ancestorrepresentation/suppressed.md) — Suppresses the representation of all ancestor classes.
