---
title: NSURLHandle.Status
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlhandle/status-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/status-swift.enum.json'
content_hash: 'sha256:187d4940aa605e04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# NSURLHandle.Status

<sub>Enumeration</sub>

These following constants are defined by `NSURLHandle` and are returned by [status](status-c.method.md).

<sub>Mac Catalyst, macOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSURLHandleNotLoaded](status-swift.enum/notloaded.md) — The resource data has not been loaded. _(deprecated)_
- [NSURLHandleLoadSucceeded](status-swift.enum/loadsucceeded.md) — The resource data was successfully loaded. _(deprecated)_
- [NSURLHandleLoadInProgress](status-swift.enum/loadinprogress.md) — The resource data is in the process of loading. _(deprecated)_
- [NSURLHandleLoadFailed](status-swift.enum/loadfailed.md) — The resource data failed to load. _(deprecated)_

### Initializers

- [init(rawValue:)](<status-swift.enum/init(rawvalue_).md>)
