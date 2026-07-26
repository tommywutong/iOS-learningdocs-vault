---
title: PHBackgroundResourceUploadJobExtension
framework: Photos
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phbackgroundresourceuploadjobextension
source_url: 'https://developer.apple.com/documentation/photos/phbackgroundresourceuploadjobextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phbackgroundresourceuploadjobextension.json'
content_hash: 'sha256:e36355f9e77b02ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHBackgroundResourceUploadJobExtension

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
protocol PHBackgroundResourceUploadJobExtension : AppExtension
```

## Relationships

- **Inherits From**: [AppExtension](../extensionfoundation/appextension.md)

## Topics

### Instance Methods

- [processJobs()](<phbackgroundresourceuploadjobextension/processjobs().md>) — Request to initiate processing background upload jobs. _(beta)_
- [willTerminate()](<phbackgroundresourceuploadjobextension/willterminate().md>) — Called by the host before suspending or terminating the extension process. Extension clients should use this to stop any in-progress work. When the extension is activated again, a new call will be made by the host. _(beta)_
