---
title: NSNull
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnull
source_url: 'https://developer.apple.com/documentation/foundation/nsnull'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnull.json'
content_hash: 'sha256:99390276a4fc17ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNull

<sub>Class</sub>

A singleton object used to represent null values in collection objects that don’t allow `nil` values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSNull
```

## Overview

[NSNull](nsnull.md) is “toll-free bridged” with its Core Foundation counterpart, [CFNull](../corefoundation/cfnull.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CAAction](../quartzcore/caaction.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(coder:)](<nsnull/init(coder_).md>)

## See Also

### Special Semantic Values

- [NSNotFound](nsnotfound-9t5v2.md)
- [NSNotFound](nsnotfound-4qp9h.md) — A value indicating that a requested item couldn’t be found or doesn’t exist.
