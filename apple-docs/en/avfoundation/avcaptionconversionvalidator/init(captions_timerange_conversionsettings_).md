---
title: 'init(captions:timeRange:conversionSettings:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionconversionvalidator/init(captions:timerange:conversionsettings:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/init(captions:timerange:conversionsettings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionvalidator/init%28captions%3Atimerange%3Aconversionsettings%3A%29.json'
content_hash: 'sha256:6ab97462fd39036f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionValidator](../avcaptionconversionvalidator.md)

# init(captions:timeRange:conversionSettings:)

<sub>Initializer</sub>

Creates an object that validates captions for a conversion operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(captions: [AVCaption], timeRange: CMTimeRange, conversionSettings: [AVCaptionSettingsKey : Any])
```

## Parameters

- `captions` — The array of captions that the system validates.

- `timeRange` — The time range of the media timeline where the captions exist.

- `conversionSettings` — A dictionary that describes the conversion operation.
