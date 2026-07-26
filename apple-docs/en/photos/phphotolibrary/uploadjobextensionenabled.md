---
title: uploadJobExtensionEnabled
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phphotolibrary/uploadjobextensionenabled
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/uploadjobextensionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/uploadjobextensionenabled.json'
content_hash: 'sha256:78939827cad7ae0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# uploadJobExtensionEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether background asset resource uploading is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var uploadJobExtensionEnabled: Bool { get }
```

## Discussion

The value is `true` if the extension is enabled and active, and is `false` otherwise.

The extension’s host app uses this property to determine the background processing status. See [PHAssetResourceUploadJob](../phassetresourceuploadjob.md) and ````PHAssetResourceUploadJobChangeRequest`` for more information.

## See Also

### Enabling an Upload Job Extension

- [- setUploadJobExtensionEnabled:error:](<setuploadjobextensionenabled(__).md>) — Enables or disables the background asset resource upload job feature.
