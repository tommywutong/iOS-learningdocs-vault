---
title: willTerminate()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phbackgroundresourceuploadjobextension/willterminate()
source_url: 'https://developer.apple.com/documentation/photos/phbackgroundresourceuploadjobextension/willterminate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phbackgroundresourceuploadjobextension/willterminate%28%29.json'
content_hash: 'sha256:8650494677930205'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHBackgroundResourceUploadJobExtension](../phbackgroundresourceuploadjobextension.md)

# willTerminate()

<sub>Instance Method</sub>

Called by the host before suspending or terminating the extension process. Extension clients should use this to stop any in-progress work. When the extension is activated again, a new call will be made by the host.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func willTerminate() async
```
