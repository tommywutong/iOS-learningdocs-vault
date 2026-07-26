---
title: NSQueryGenerationToken
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsquerygenerationtoken
source_url: 'https://developer.apple.com/documentation/coredata/nsquerygenerationtoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsquerygenerationtoken.json'
content_hash: 'sha256:c1b83576e43d499d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSQueryGenerationToken

<sub>Class</sub>

A token that indicates which generation of the persistent store is being accessed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSQueryGenerationToken
```

## Overview

When a managed object context is pinned to a specific generation of the app data, a query generation token will be associated with that context.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Identifying Generations of App Data

- [currentQueryGenerationToken](nsquerygenerationtoken/current.md) — A token that informs a context to use the current generation.

### Initializers

- [init(coder:)](<nsquerygenerationtoken/init(coder_).md>)

## See Also

### Conflict Management

- [NSConstraintConflict](nsconstraintconflict.md) — An encapsulation of conflicts that occur during an attempt to save a managed object.
- [NSMergeConflict](nsmergeconflict.md) — An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.
- [NSMergePolicy](nsmergepolicy.md) — A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.
