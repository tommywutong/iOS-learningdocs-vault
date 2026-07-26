---
title: 'jpegPhotoDataRepresentation(forJPEGSampleBuffer:previewPhotoSampleBuffer:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+（11.0 起废弃）, iPadOS 10.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avcapturephotooutput/jpegphotodatarepresentation(forjpegsamplebuffer:previewphotosamplebuffer:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/jpegphotodatarepresentation(forjpegsamplebuffer:previewphotosamplebuffer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/jpegphotodatarepresentation%28forjpegsamplebuffer%3Apreviewphotosamplebuffer%3A%29.json'
content_hash: 'sha256:8a73408243f3d184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# jpegPhotoDataRepresentation(forJPEGSampleBuffer:previewPhotoSampleBuffer:)

<sub>Type Method</sub>

Returns data in JPEG format corresponding to the captured photo in the specified sample buffer.

> [!warning] Deprecated
> In iOS 11 and later, implement the [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method in your capture delegate and use the [- fileDataRepresentation](<../avcapturephoto/filedatarepresentation().md>) method of the resulting [AVCapturePhoto](../avcapturephoto.md) object.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func jpegPhotoDataRepresentation(forJPEGSampleBuffer JPEGSampleBuffer: CMSampleBuffer, previewPhotoSampleBuffer: CMSampleBuffer?) -> Data?
```

## Parameters

- `JPEGSampleBuffer` — A sample buffer containing the JPEG photo capture result to be formatted for output.

- `previewPhotoSampleBuffer` — An optional additional sample buffer containing a preview-resolution version of the photo capture result, to be added to the JPEG output as a thumbnail image. Pass `nil` to skip adding a preview image to the output.

## Return Value

A data object containing a JPEG representation of the requested photo capture results, or `nil` if the sample buffers cannot be packaged for output.

## Discussion

After you request a photo capture with the [- capturePhotoWithSettings:delegate:](<capturephoto(with_delegate_).md>) method, the photo capture output delivers results to your delegate as one or more [CMSampleBuffer](../../coremedia/cmsamplebuffer.md) objects. (See the [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) method.) To repackage the sample buffer’s content for output as a JPEG file, use this class method. Optionally, you can include metadata in the resulting JPEG output by attaching it to the sample buffer before calling this method.

> [!important] Important
> The `jpegSampleBuffer` parameter must reference a sample buffer from a JPEG capture. See the [format](../avcapturephotosettings/format.md) property for photo capture settings.

## See Also

### Getting formatted output

- [+ DNGPhotoDataRepresentationForRawSampleBuffer:previewPhotoSampleBuffer:](<dngphotodatarepresentation(forrawsamplebuffer_previewphotosamplebuffer_).md>) — Returns data in digital negative (DNG) format corresponding to the captured RAW photo in the specified sample buffer. _(deprecated)_
