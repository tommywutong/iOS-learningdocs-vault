---
title: ITLibraryDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/itlibrarydidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/itlibrarydidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/itlibrarydidchange.json'
content_hash: 'sha256:bc8af2e1a53bd8e5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# ITLibraryDidChange

<sub>Type Property</sub>

A notification the system posts when a library change occurs.

<sub>macOS</sub>

```swift
static let ITLibraryDidChange: NSNotification.Name
```

## Discussion

Call [reloadData()](<../../../ituneslibrary/itlibrary/reloaddata().md>) to retrieve a new view of the library contents.
