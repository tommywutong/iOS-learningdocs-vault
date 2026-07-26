---
title: FileManager.URLRelationship
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/urlrelationship
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/urlrelationship'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/urlrelationship.json'
content_hash: 'sha256:2e1c145f7ab49c36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# FileManager.URLRelationship

<sub>Enumeration</sub>

Constants indicating the relationship between a directory and an item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum URLRelationship
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### URL Relationships

- [NSURLRelationshipContains](urlrelationship/contains.md) — The directory contains the specified item.
- [NSURLRelationshipSame](urlrelationship/same.md) — The directory and the item are the same. This relationship occurs when the value of the [NSURLFileResourceIdentifierKey](../urlresourcekey/fileresourceidentifierkey.md) is the same for the directory and item.
- [NSURLRelationshipOther](urlrelationship/other.md) — The directory does not contain the item and is not the same as the item.

### Initializers

- [init(rawValue:)](<urlrelationship/init(rawvalue_).md>)

## See Also

### Getting the relationship between items

- [- getRelationship:ofDirectoryAtURL:toItemAtURL:error:](<getrelationship(__ofdirectoryat_toitemat_).md>) — Determines the type of relationship that exists between a directory and an item.
- [- getRelationship:ofDirectory:inDomain:toItemAtURL:error:](<getrelationship(__of_in_toitemat_).md>) — Determines the type of relationship that exists between a system directory and the specified item.
