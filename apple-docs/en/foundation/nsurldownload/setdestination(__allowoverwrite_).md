---
title: 'setDestination(_:allowOverwrite:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownload/setdestination(_:allowoverwrite:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownload/setdestination(_:allowoverwrite:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownload/setdestination%28_%3Aallowoverwrite%3A%29.json'
content_hash: 'sha256:d3594d14a3f04c4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownload](../nsurldownload.md)

# setDestination(_:allowOverwrite:)

<sub>Instance Method</sub>

Sets the destination path of the downloaded file.

<sub>macOS</sub>

```swift
func setDestination(_ path: String, allowOverwrite: Bool)
```

## Parameters

- `path` — The path for the downloaded file.

- `allowOverwrite` — [true](../../swift/true.md) if an existing file at `path` can be replaced, [false](../../swift/false.md) otherwise.

## Discussion

If `allowOverwrite` is [false](../../swift/false.md) and a file already exists at `path`, a unique filename will be created for the downloaded file by appending a number to the filename. The delegate can implement the [- download:didCreateDestination:](<../nsurldownloaddelegate/download(__didcreatedestination_).md>) delegate method to determine the filename used when the file is written to disk.

### Special Considerations

An `NSURLDownload` instance ignores multiple calls to this method.

## See Also

### Related Documentation

- [- download:decideDestinationWithSuggestedFilename:](<../nsurldownloaddelegate/download(__decidedestinationwithsuggestedfilename_).md>) — The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [- download:didCreateDestination:](<../nsurldownloaddelegate/download(__didcreatedestination_).md>) — Sent when the destination file is created.

### Creating and configuring a download instance

- [- initWithRequest:delegate:](<init(request_delegate_).md>) — Returns an initialized URL download for a URL request and begins to download the data for the request. _(deprecated)_
