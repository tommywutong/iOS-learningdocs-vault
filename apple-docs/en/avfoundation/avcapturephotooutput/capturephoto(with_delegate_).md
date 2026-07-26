---
title: 'capturePhoto(with:delegate:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotooutput/capturephoto(with:delegate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/capturephoto(with:delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/capturephoto%28with%3Adelegate%3A%29.json'
content_hash: 'sha256:f28166120ba09889'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# capturePhoto(with:delegate:)

<sub>Instance Method</sub>

Initiates a photo capture using the specified settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func capturePhoto(with settings: AVCapturePhotoSettings, delegate: any AVCapturePhotoCaptureDelegate)
```

## Parameters

- `settings` — The settings for the photo capture, such as the output pixel format and flash mode. This method copies the provided [AVCapturePhotoSettings](../avcapturephotosettings.md) object, so future changes to that object do not affect the capture in progress. > [!important] Important > It is illegal to reuse a [AVCapturePhotoSettings](../avcapturephotosettings.md) instance for multiple captures. Calling this method throws an exception ([invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md)) if the `settings` object’s [uniqueID](../avcapturephotosettings/uniqueid.md) value matches that of any previously used settings object.

- `delegate` — A delegate object to receive messages about capture progress and results. The photo output calls your delegate methods as the photo advances from capture to processing to delivery of finished images.

## Discussion

Use this method for all variations of still photography, including single photo capture,  RAW format capture (with or without a secondary format such as JPEG), bracketed capture of multiple images, and Live Photo capture.

When you call this method, the photo output validates the properties of your `settings` object to ensure deterministic behavior. For example, the [flashMode](../avcapturephotosettings/flashmode.md) setting must specify a value that is present in the photo output’s [supportedFlashModes](supportedflashmodes-4u69s.md) array. See each property’s description in the [AVCapturePhotoSettings](../avcapturephotosettings.md) class reference for detailed validation rules.
