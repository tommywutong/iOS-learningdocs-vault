---
title: 'init(contentType:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/init(contenttype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/init(contenttype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/init%28contenttype%3A%29.json'
content_hash: 'sha256:72111eba322085be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# init(contentType:)

<sub>Initializer</sub>

Creates an object that outputs segment data in a specified container format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(contentType outputContentType: UTType)
```

## Parameters

- `outputContentType` — A type that indicates the format of the segment data to output.

## Discussion

Use this initializer to create an asset writer that outputs segment data to an adopter of the [AVAssetWriterDelegate](../avassetwriterdelegate.md) protocol. For example, you can create an asset writer object to write an MPEG-4 file as shown below:

```swift
// Create a UTType for the MP4 file type.
guard let contentType = UTType(AVFileType.mp4.rawValue) else { return }
let assetWriter = AVAssetWriter(contentType: contentType)
```

## See Also

### Creating an asset writer

- [+ assetWriterWithURL:fileType:error:](<init(url_filetype_)-xt34.md>) — Returns a new object that writes media data to a container file at the output URL.
- [- initWithURL:fileType:error:](<init(outputurl_filetype_).md>) — Creates an object that writes media data to a container file at the output URL.
