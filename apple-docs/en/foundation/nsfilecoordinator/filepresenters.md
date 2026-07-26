---
title: filePresenters
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/filepresenters
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/filepresenters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/filepresenters.json'
content_hash: 'sha256:9da2c33c0c917ee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# filePresenters

<sub>Type Property</sub>

Returns an array containing the currently registered file presenter objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var filePresenters: [any NSFilePresenter] { get }
```

## Return Value

An array of objects that conform to the [NSFilePresenter](../nsfilepresenter.md) protocol.

## See Also

### Managing File Presenters

- [+ addFilePresenter:](<addfilepresenter(__).md>) — Registers the specified file presenter object so that it can receive notifications.
- [+ removeFilePresenter:](<removefilepresenter(__).md>) — Unregisters the specified file presenter object.
- [purposeIdentifier](purposeidentifier.md) — A string that uniquely identifies the file access that was performed by this file coordinator.
