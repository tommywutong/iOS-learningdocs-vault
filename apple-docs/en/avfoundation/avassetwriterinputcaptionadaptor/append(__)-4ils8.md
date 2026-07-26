---
title: 'append(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinputcaptionadaptor/append(_:)-4ils8'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputcaptionadaptor/append(_:)-4ils8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputcaptionadaptor/append%28_%3A%29-4ils8.json'
content_hash: 'sha256:b850c12ed80cd53e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputCaptionAdaptor](../avassetwriterinputcaptionadaptor.md)

# append(_:)

<sub>Instance Method</sub>

Appends a caption group that the system writes to the output.

> [!warning] Deprecated
> Use AVAssetWriter.inputCaptionReceiver(for:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func append(_ captionGroup: AVCaptionGroup) -> Bool
```

## Parameters

- `captionGroup` — The caption group that the system writes to the output.

## Return Value

A Boolean value that indicates whether the operation succeeded.

## See Also

### Appending captions

- [- appendCaption:](<append(__)-910lp.md>) — Appends a caption to the writer input. _(deprecated)_
