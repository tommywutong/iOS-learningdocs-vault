---
title: NSPersistentHistoryToken
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorytoken
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorytoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorytoken.json'
content_hash: 'sha256:43bae2505f86f9f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentHistoryToken

<sub>Class</sub>

A bookmark for keeping track the most recent history that you’ve processed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentHistoryToken
```

## Overview

You can save a token to disk and fetch history when your app loads based on that token. See [Keep track of the most recent history](consuming-relevant-store-changes.md#Keep-track-of-the-most-recent-history) in [Consuming relevant store changes](consuming-relevant-store-changes.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(coder:)](<nspersistenthistorytoken/init(coder_).md>)
