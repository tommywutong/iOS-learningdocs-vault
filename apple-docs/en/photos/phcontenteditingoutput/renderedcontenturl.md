---
title: renderedContentURL
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditingoutput/renderedcontenturl
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditingoutput/renderedcontenturl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditingoutput/renderedcontenturl.json'
content_hash: 'sha256:aea475a29a3a3a94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingOutput](../phcontenteditingoutput.md)

# renderedContentURL

<sub>Instance Property</sub>

The URL at which to write a file containing edited asset content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var renderedContentURL: URL { get }
```

## Discussion

Read this property to find a URL for writing edited asset content. Then, if editing a photo asset, write the altered photo image to a file in JPEG format at this URL. If editing a video asset, export the video to a QuickTime (`.mov`) file at this URL.

> [!important] Important
> Edited asset content must incorporate (or “bake in”) the intended orientation of the asset. That is, the orientation metadata (if any) that you write in the output image or video file must declare the “up” orientation, and the image or video data must appear right-side up when presented without orientation metadata.

For Live Photo content, you don’t write output to this URL. Instead, pass the editing output object to the [- saveLivePhotoToOutput:options:completionHandler:](<../phlivephotoeditingcontext/savelivephoto(to_options_completionhandler_).md>) method.

## See Also

### Providing Edit and Adjustment Data

- [adjustmentData](adjustmentdata.md) — An object describing the changes made to the asset.
