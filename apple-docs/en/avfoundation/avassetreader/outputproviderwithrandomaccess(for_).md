---
title: 'outputProviderWithRandomAccess(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreader/outputproviderwithrandomaccess(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/outputproviderwithrandomaccess(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/outputproviderwithrandomaccess%28for%3A%29.json'
content_hash: 'sha256:7cb093247b2968d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# outputProviderWithRandomAccess(for:)

<sub>Instance Method</sub>

Attaches the output to the reader and returns a tuple with an output provider for reading sample buffers, and an associated random access controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func outputProviderWithRandomAccess(for output: AVAssetReaderOutput) -> sending (AVAssetReaderOutput.Provider<CMReadySampleBuffer<CMSampleBuffer.DynamicContent>>, AVAssetReaderOutput.RandomAccessController)
```

## Parameters

- `output` — The output to be attached to the reader.

## Return Value

A tuple with an output provider for reading sample buffers, and an associated random access controller.

## See Also

### Accessing output providers

- [outputProvider(for:)](<outputprovider(for_).md>) — Attaches the output to the reader and returns an output provider for reading sample buffers.
- [outputCaptionProvider(for:validationDelegate:)](<outputcaptionprovider(for_validationdelegate_).md>) — Attaches the output to the reader and returns an output provider for reading caption groups.
- [outputCaptionProviderWithRandomAccess(for:validationDelegate:)](<outputcaptionproviderwithrandomaccess(for_validationdelegate_).md>) — Attaches the output to the reader and returns a tuple with an output provider for reading caption groups, and an associated random access controller.
- [outputMetadataProvider(for:)](<outputmetadataprovider(for_).md>) — Attaches the output to the reader and returns an output provider for reading timed metadata groups.
- [outputMetadataProviderWithRandomAccess(for:)](<outputmetadataproviderwithrandomaccess(for_).md>) — Attaches the output to the reader and returns a tuple with an output provider for timed metadata groups buffers, and an associated random access controller.
