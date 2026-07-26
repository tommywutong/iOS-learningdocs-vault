---
title: 'init(url:fileType:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/init(url:filetype:)-xt34'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/init(url:filetype:)-xt34'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/init%28url%3Afiletype%3A%29-xt34.json'
content_hash: 'sha256:010b9c83d4036346'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# init(url:fileType:)

<sub>Initializer</sub>

Returns a new object that writes media data to a container file at the output URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(url outputURL: URL, fileType outputFileType: AVFileType) throws
```

## Parameters

- `outputURL` — The location of the file to write.

- `outputFileType` — The type of container file to write.

## Return Value

A new asset writer.

## Discussion

Writing fails if a file already exists at the output URL.

## See Also

### Creating an asset writer

- [- initWithURL:fileType:error:](<init(outputurl_filetype_).md>) — Creates an object that writes media data to a container file at the output URL.
- [- initWithContentType:](<init(contenttype_).md>) — Creates an object that outputs segment data in a specified container format.
