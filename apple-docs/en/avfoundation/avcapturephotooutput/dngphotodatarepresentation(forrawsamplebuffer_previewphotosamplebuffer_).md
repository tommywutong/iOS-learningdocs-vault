---
title: 'dngPhotoDataRepresentation(forRawSampleBuffer:previewPhotoSampleBuffer:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+（11.0 起废弃）, iPadOS 10.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avcapturephotooutput/dngphotodatarepresentation(forrawsamplebuffer:previewphotosamplebuffer:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/dngphotodatarepresentation(forrawsamplebuffer:previewphotosamplebuffer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/dngphotodatarepresentation%28forrawsamplebuffer%3Apreviewphotosamplebuffer%3A%29.json'
content_hash: 'sha256:6374e5763f056534'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# dngPhotoDataRepresentation(forRawSampleBuffer:previewPhotoSampleBuffer:)

<sub>Type Method</sub>

Returns data in digital negative (DNG) format corresponding to the captured RAW photo in the specified sample buffer.

> [!warning] Deprecated
> In iOS 11 and later, implement the [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method in your capture delegate and use the [- fileDataRepresentation](<../avcapturephoto/filedatarepresentation().md>) method of the resulting [AVCapturePhoto](../avcapturephoto.md) object.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func dngPhotoDataRepresentation(forRawSampleBuffer rawSampleBuffer: CMSampleBuffer, previewPhotoSampleBuffer: CMSampleBuffer?) -> Data?
```

## Parameters

- `rawSampleBuffer` — A sample buffer containing the RAW photo capture result to be formatted for output.

- `previewPhotoSampleBuffer` — An optional additional sample buffer containing a preview-resolution version of the photo capture result, to be added to the DNG output as a thumbnail image. Pass `nil` to skip adding a preview image to the output.

## Return Value

A data object containing a DNG representation of the requested photo capture results, or `nil` if the sample buffers cannot be packaged for output.

## Discussion

After you request a photo capture with the [- capturePhotoWithSettings:delegate:](<capturephoto(with_delegate_).md>) method, the photo capture output delivers results to your delegate as one or more [CMSampleBuffer](../../coremedia/cmsamplebuffer.md) objects. (See the [- captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingrawphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) method.) To repackage the sample buffer’s content for output as a DNG file, use this class method. Optionally, you can include metadata in the resulting DNG output by attaching it to the sample buffer before calling this method.

> [!important] Important
> The `rawSampleBuffer` parameter must reference a sample buffer from a RAW capture. See the [rawPhotoPixelFormatType](../avcapturephotosettings/rawphotopixelformattype.md) property for photo capture settings.

## See Also

### Getting formatted output

- [+ JPEGPhotoDataRepresentationForJPEGSampleBuffer:previewPhotoSampleBuffer:](<jpegphotodatarepresentation(forjpegsamplebuffer_previewphotosamplebuffer_).md>) — Returns data in JPEG format corresponding to the captured photo in the specified sample buffer. _(deprecated)_
