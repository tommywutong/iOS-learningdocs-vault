---
title: NSFileAccessIntent
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileaccessintent
source_url: 'https://developer.apple.com/documentation/foundation/nsfileaccessintent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileaccessintent.json'
content_hash: 'sha256:09c8ca3cf4e31ebf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileAccessIntent

<sub>Class</sub>

The details of a coordinated-read or coordinated-write operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSFileAccessIntent
```

## Overview

Use this class when performing asynchronous operations with a file coordinator using the coordinator’s [- coordinateAccessWithIntents:queue:byAccessor:](<nsfilecoordinator/coordinate(with_queue_byaccessor_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a File Access Intent

- [+ readingIntentWithURL:options:](<nsfileaccessintent/readingintent(with_options_).md>) — Returns a file access intent object for reading the given URL with the provided options.
- [+ writingIntentWithURL:options:](<nsfileaccessintent/writingintent(with_options_).md>) — Returns a file access intent object for writing to the given URL with the provided options.

### Accessing the Current URL

- [URL](nsfileaccessintent/url.md) — The current URL for the item managed by the file access intent instance. (read-only)

## See Also

### Coordinated file access

- [NSFilePresenter](nsfilepresenter.md) — The interface a file coordinator uses to inform an object presenting a file about changes to that file made elsewhere in the system.
- [NSFileCoordinator](nsfilecoordinator.md) — An object that coordinates the reading and writing of files and directories among file presenters.
