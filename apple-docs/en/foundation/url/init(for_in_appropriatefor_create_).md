---
title: 'init(for:in:appropriateFor:create:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(for:in:appropriatefor:create:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(for:in:appropriatefor:create:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28for%3Ain%3Aappropriatefor%3Acreate%3A%29.json'
content_hash: 'sha256:df0c76ffcbd49b83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(for:in:appropriateFor:create:)

<sub>Initializer</sub>

Creates a file URL for a common directory in a domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(for directory: FileManager.SearchPathDirectory, in domain: FileManager.SearchPathDomainMask, appropriateFor url: URL? = nil, create shouldCreate: Bool = false) throws
```

## Parameters

- `directory` — The search path for the commonly used directory, such as [NSDesktopDirectory](../filemanager/searchpathdirectory/desktopdirectory.md) or [NSDownloadsDirectory](../filemanager/searchpathdirectory/downloadsdirectory.md).

- `domain` — The file system domain to search, which the values in [SearchPathDomainMask](../filemanager/searchpathdomainmask.md) define. Specify only one domain for this parameter. You may not specify [NSAllDomainsMask](../filemanager/searchpathdomainmask/alldomainsmask.md) with this initializer.

- `url` — The file URL for determining the location of the returned URL. Only the volume of this parameter is relevant. The initializer ignores this parameter unless the directory parameter contains the value [NSItemReplacementDirectory](../filemanager/searchpathdirectory/itemreplacementdirectory.md) and the domain parameter contains the value [NSUserDomainMask](../filemanager/searchpathdomainmask/userdomainmask.md).

- `shouldCreate` — A Boolean value that indicates whether the initializer creates the directory if it doesn’t already exist.

## See Also

### Creating a file URL for a common directory

- [SearchPathDirectory](../filemanager/searchpathdirectory.md) — The location of significant directories.
- [SearchPathDomainMask](../filemanager/searchpathdomainmask.md) — Domain constants specifying base locations to use when you search for significant directories.
