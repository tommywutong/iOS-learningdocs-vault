---
title: 'init(outputURL:fileType:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/init(outputurl:filetype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/init(outputurl:filetype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/init%28outputurl%3Afiletype%3A%29.json'
content_hash: 'sha256:ee7dcb7afda8cede'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# init(outputURL:fileType:)

<sub>Initializer</sub>

Creates an object that writes media data to a container file at the output URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(outputURL: URL, fileType outputFileType: AVFileType) throws
```

## Parameters

- `outputURL` — The location of the file to write.

- `outputFileType` — The type of container file to write.

## Discussion

Writing fails if a file already exists at the output URL.

## See Also

### Creating an asset writer

- [+ assetWriterWithURL:fileType:error:](<init(url_filetype_)-xt34.md>) — Returns a new object that writes media data to a container file at the output URL.
- [- initWithContentType:](<init(contenttype_).md>) — Creates an object that outputs segment data in a specified container format.
