---
title: 'outputCaptionProvider(for:validationDelegate:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreader/outputcaptionprovider(for:validationdelegate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/outputcaptionprovider(for:validationdelegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/outputcaptionprovider%28for%3Avalidationdelegate%3A%29.json'
content_hash: 'sha256:e1d32f3f7b370da2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# outputCaptionProvider(for:validationDelegate:)

<sub>Instance Method</sub>

Attaches the output to the reader and returns an output provider for reading caption groups.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func outputCaptionProvider(for output: AVAssetReaderTrackOutput, validationDelegate: (any AVAssetReaderCaptionValidationHandling)? = nil) -> sending AVAssetReaderOutput.Provider<AVCaptionGroup>
```

## Parameters

- `output` — The output to be attached to the reader.

## Return Value

A reader output provider with an interface for reading caption groups.

## See Also

### Accessing output providers

- [outputProvider(for:)](<outputprovider(for_).md>) — Attaches the output to the reader and returns an output provider for reading sample buffers.
- [outputProviderWithRandomAccess(for:)](<outputproviderwithrandomaccess(for_).md>) — Attaches the output to the reader and returns a tuple with an output provider for reading sample buffers, and an associated random access controller.
- [outputCaptionProviderWithRandomAccess(for:validationDelegate:)](<outputcaptionproviderwithrandomaccess(for_validationdelegate_).md>) — Attaches the output to the reader and returns a tuple with an output provider for reading caption groups, and an associated random access controller.
- [outputMetadataProvider(for:)](<outputmetadataprovider(for_).md>) — Attaches the output to the reader and returns an output provider for reading timed metadata groups.
- [outputMetadataProviderWithRandomAccess(for:)](<outputmetadataproviderwithrandomaccess(for_).md>) — Attaches the output to the reader and returns a tuple with an output provider for timed metadata groups buffers, and an associated random access controller.
