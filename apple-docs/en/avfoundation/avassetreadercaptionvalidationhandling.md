---
title: AVAssetReaderCaptionValidationHandling
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreadercaptionvalidationhandling
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadercaptionvalidationhandling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadercaptionvalidationhandling.json'
content_hash: 'sha256:095c33ceb89064b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetReaderCaptionValidationHandling

<sub>Protocol</sub>

A protocol that defines the methods for caption validation events.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
protocol AVAssetReaderCaptionValidationHandling : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Validating captions

- [- captionAdaptor:didVendCaption:skippingUnsupportedSourceSyntaxElements:](<avassetreadercaptionvalidationhandling/captionadaptor(__didvendcaption_skippingunsupportedsourcesyntaxelements_).md>) — Tells the delegate that the adaptor ignored one or more syntax elements when it created the caption object.

## See Also

### Managing the validation delegate

- [validationDelegate](avassetreaderoutputcaptionadaptor/validationdelegate.md) — A delegate object that handles callbacks to the caption adaptor.
