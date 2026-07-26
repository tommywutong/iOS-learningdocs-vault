---
title: 'setUploadJobExtensionEnabled(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/setuploadjobextensionenabled(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/setuploadjobextensionenabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/setuploadjobextensionenabled%28_%3A%29.json'
content_hash: 'sha256:ba8e0f31c807bd89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# setUploadJobExtensionEnabled(_:)

<sub>Instance Method</sub>

Enables or disables the background asset resource upload job feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func setUploadJobExtensionEnabled(_ enable: Bool) throws
```

## Parameters

- `enable` — `true` allows calls to the extension’s host application; you can fulfill that protocol to create [PHAssetResourceUploadJob](../phassetresourceuploadjob.md) objects. `false` stops calls to the extension’s host application.

## Discussion

You must call this function before you create [PHAssetResourceUploadJob](../phassetresourceuploadjob.md) in the extension’s host application.

To enable background uploads, you must have both full library access and register the extension with the extension point: “com.apple.photos.background-upload”.

## See Also

### Enabling an Upload Job Extension

- [uploadJobExtensionEnabled](uploadjobextensionenabled.md) — A Boolean value that indicates whether background asset resource uploading is enabled.
