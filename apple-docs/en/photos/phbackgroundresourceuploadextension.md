---
title: PHBackgroundResourceUploadExtension
framework: Photos
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.1+（27.0 起废弃）, iPadOS 26.1+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phbackgroundresourceuploadextension
source_url: 'https://developer.apple.com/documentation/photos/phbackgroundresourceuploadextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phbackgroundresourceuploadextension.json'
content_hash: 'sha256:ad90b46c6b631237'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHBackgroundResourceUploadExtension

<sub>Protocol</sub>

> [!warning] Deprecated
> Adopt PHBackgroundResourceUploadJobExtension instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
protocol PHBackgroundResourceUploadExtension : AppExtension
```

## Relationships

- **Inherits From**: [AppExtension](../extensionfoundation/appextension.md)

## Topics

### Processing upload requests

- [process()](<phbackgroundresourceuploadextension/process().md>) — Request to initiate processing background upload jobs. _(deprecated)_
- [PHBackgroundResourceUploadProcessingResult](phbackgroundresourceuploadprocessingresult.md)

### Handling termination

- [notifyTermination()](<phbackgroundresourceuploadextension/notifytermination().md>) — This notification will be called if the host is going to suspend/terminate the current execution. Extension clients should use this to stop the current execution. When the extension is activated, a new call will be presented by the host. _(deprecated)_

## See Also

### Background resource upload extensions

- [Uploading asset resources in the background](../photokit/uploading-asset-resources-in-the-background.md) — Enable reliable cloud backup for photo library assets with background processing.
- [PHAssetResourceUploadJob](phassetresourceuploadjob.md) — An object that represents a request to upload an asset resource.
- [PHAssetResourceUploadJobChangeRequest](phassetresourceuploadjobchangerequest.md) — Use within an application’s `com.apple.photos.background-upload` extension to create and change [PHAssetResourceUploadJob](phassetresourceuploadjob.md) records.
