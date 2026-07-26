---
title: 'outputProvider(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreader/outputprovider(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/outputprovider(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/outputprovider%28for%3A%29.json'
content_hash: 'sha256:e04ee1ec80a298e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# outputProvider(for:)

<sub>Instance Method</sub>

Attaches the output to the reader and returns an output provider for reading sample buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func outputProvider(for output: AVAssetReaderOutput) -> sending AVAssetReaderOutput.Provider<CMReadySampleBuffer<CMSampleBuffer.DynamicContent>>
```

## Parameters

- `output` — The output to be attached to the reader.

## Return Value

A reader output provider with an interface for reading sample buffers.

## See Also

### Accessing output providers

- [outputProviderWithRandomAccess(for:)](<outputproviderwithrandomaccess(for_).md>) — Attaches the output to the reader and returns a tuple with an output provider for reading sample buffers, and an associated random access controller.
- [outputCaptionProvider(for:validationDelegate:)](<outputcaptionprovider(for_validationdelegate_).md>) — Attaches the output to the reader and returns an output provider for reading caption groups.
- [outputCaptionProviderWithRandomAccess(for:validationDelegate:)](<outputcaptionproviderwithrandomaccess(for_validationdelegate_).md>) — Attaches the output to the reader and returns a tuple with an output provider for reading caption groups, and an associated random access controller.
- [outputMetadataProvider(for:)](<outputmetadataprovider(for_).md>) — Attaches the output to the reader and returns an output provider for reading timed metadata groups.
- [outputMetadataProviderWithRandomAccess(for:)](<outputmetadataproviderwithrandomaccess(for_).md>) — Attaches the output to the reader and returns a tuple with an output provider for timed metadata groups buffers, and an associated random access controller.
