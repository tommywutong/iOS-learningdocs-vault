---
title: Core Foundation URL Access Utilities
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/core-foundation-url-access-utilities
source_url: 'https://developer.apple.com/documentation/corefoundation/core-foundation-url-access-utilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/core-foundation-url-access-utilities.json'
content_hash: 'sha256:a206e817b90a3ed8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# Core Foundation URL Access Utilities

<sub>API Collection</sub>

## Overview

Core Foundation URL Access Utilities give you convenient system-independent methods of creating, reading, updating, or deleting a URL resource.

Given a [CFURL](cfurl.md) object that holds either a file or http URL, you can read the resource’s data with the [CFURLCreateDataAndPropertiesFromResource](<cfurlcreatedataandpropertiesfromresource(____________).md>) function. You can write data to the URL resource, possibly creating a new file, with the [CFURLWriteDataAndPropertiesToResource](<cfurlwritedataandpropertiestoresource(________).md>) function. Finally, you can destroy, or delete, the resource pointed to by the URL with the [CFURLDestroyResource](<cfurldestroyresource(____).md>) function.

## Topics

### Core Foundation URL Access Utilities Miscellaneous Functions

- [CFURLCreateDataAndPropertiesFromResource](<cfurlcreatedataandpropertiesfromresource(____________).md>) — Loads the data and properties referred to by a given URL. _(deprecated)_
- [CFURLCreatePropertyFromResource](<cfurlcreatepropertyfromresource(________).md>) — Returns a given property specified by a given URL and property string. _(deprecated)_
- [CFURLDestroyResource](<cfurldestroyresource(____).md>) — Destroys a resource indicated by a given URL. _(deprecated)_
- [CFURLWriteDataAndPropertiesToResource](<cfurlwritedataandpropertiestoresource(________).md>) — Writes the given data and properties to a given URL. _(deprecated)_

### Constants

- [CFURLError](cfurlerror.md) — `CFURL` error codes. _(deprecated)_
- [File URL Properties](file-url-properties.md) — Properties for file URL resources.
- [HTTP URL Properties](http-url-properties.md) — Properties for HTTP URL resources.

## See Also

### Utilities

- [Base Utilities](base-utilities.md)
- [Byte-Order Utilities](byte-order-utilities.md)
- [Preferences Utilities](preferences-utilities.md)
- [Socket Name Server Utilities](socket-name-server-utilities.md)
- [Time Utilities](time-utilities.md)
