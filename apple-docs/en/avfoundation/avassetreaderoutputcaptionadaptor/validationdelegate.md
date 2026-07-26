---
title: validationDelegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreaderoutputcaptionadaptor/validationdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/validationdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputcaptionadaptor/validationdelegate.json'
content_hash: 'sha256:95ac05e21b899dfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutputCaptionAdaptor](../avassetreaderoutputcaptionadaptor.md)

# validationDelegate

<sub>Instance Property</sub>

A delegate object that handles callbacks to the caption adaptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
weak var validationDelegate: (any AVAssetReaderCaptionValidationHandling)? { get set }
```

## See Also

### Managing the validation delegate

- [AVAssetReaderCaptionValidationHandling](../avassetreadercaptionvalidationhandling.md) — A protocol that defines the methods for caption validation events.
