---
title: 'captionAdaptor(_:didVendCaption:skippingUnsupportedSourceSyntaxElements:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreadercaptionvalidationhandling/captionadaptor(_:didvendcaption:skippingunsupportedsourcesyntaxelements:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadercaptionvalidationhandling/captionadaptor(_:didvendcaption:skippingunsupportedsourcesyntaxelements:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadercaptionvalidationhandling/captionadaptor%28_%3Adidvendcaption%3Askippingunsupportedsourcesyntaxelements%3A%29.json'
content_hash: 'sha256:af884d0cace20dc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderCaptionValidationHandling](../avassetreadercaptionvalidationhandling.md)

# captionAdaptor(_:didVendCaption:skippingUnsupportedSourceSyntaxElements:)

<sub>Instance Method</sub>

Tells the delegate that the adaptor ignored one or more syntax elements when it created the caption object.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func captionAdaptor(_ adaptor: AVAssetReaderOutputCaptionAdaptor, didVendCaption caption: AVCaption, skippingUnsupportedSourceSyntaxElements syntaxElements: [String])
```

## Parameters

- `adaptor` — The adaptor object.

- `caption` — The vended caption.

- `syntaxElements` — The array of unsupported syntax elements that the adaptor object skipped.
