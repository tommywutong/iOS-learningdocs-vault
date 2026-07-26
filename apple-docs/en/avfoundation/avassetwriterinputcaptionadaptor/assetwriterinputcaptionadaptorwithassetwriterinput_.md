---
title: 'assetWriterInputCaptionAdaptorWithAssetWriterInput:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinputcaptionadaptor/assetwriterinputcaptionadaptorwithassetwriterinput:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputcaptionadaptor/assetwriterinputcaptionadaptorwithassetwriterinput:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputcaptionadaptor/assetwriterinputcaptionadaptorwithassetwriterinput%3A.json'
content_hash: 'sha256:bb715b2089fa413d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputCaptionAdaptor](../avassetwriterinputcaptionadaptor.md)

# assetWriterInputCaptionAdaptorWithAssetWriterInput:

<sub>Type Method</sub>

A class method that creates a new caption adaptor that writes to the specified asset writer input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetWriterInputCaptionAdaptorWithAssetWriterInput:(AVAssetWriterInput *) input;
```

## Parameters

- `input` — The asset writer input.

## Return Value

A new instance of [AVAssetWriterInputCaptionAdaptor](../avassetwriterinputcaptionadaptor.md)

## See Also

### Creating a caption adaptor

- [- initWithAssetWriterInput:](<init(assetwriterinput_).md>) — Creates a new caption adaptor that writes to the specified asset writer input. _(deprecated)_
