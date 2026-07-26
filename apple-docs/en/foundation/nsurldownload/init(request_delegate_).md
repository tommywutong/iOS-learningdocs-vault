---
title: 'init(request:delegate:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.3+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurldownload/init(request:delegate:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownload/init(request:delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownload/init%28request%3Adelegate%3A%29.json'
content_hash: 'sha256:635175c49b562ae4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownload](../nsurldownload.md)

# init(request:delegate:)

<sub>Initializer</sub>

Returns an initialized URL download for a URL request and begins to download the data for the request.

> [!warning] Deprecated
> Use NSURLSession downloadTask (see NSURLSession.h)

<sub>macOS</sub>

```swift
init(request: URLRequest, delegate: (any NSURLDownloadDelegate)?)
```

## Parameters

- `request` — The URL request to download. The `request` object is deep-copied as part of the initialization process. Changes made to `request` after this method returns do not affect the request that is used for the loading process.

- `delegate` — The delegate for the download. This object will receive delegate messages as the download progresses. Delegate messages will be sent on the thread which calls this method. For the download to work correctly the calling thread’s run loop must be operating in the default run loop mode. The `NSURLDownload` class maintains a strong reference to this delegate object.

## Return Value

An initialized NSURLDownload object for `request`.

## See Also

### Related Documentation

- [URL Loading System](../url-loading-system.md) — Interact with URLs and communicate with servers using standard Internet protocols.

### Creating and configuring a download instance

- [- setDestination:allowOverwrite:](<setdestination(__allowoverwrite_).md>) — Sets the destination path of the downloaded file.
