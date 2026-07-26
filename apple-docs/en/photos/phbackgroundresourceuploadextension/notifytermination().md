---
title: notifyTermination()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.1+（27.0 起废弃）, iPadOS 26.1+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phbackgroundresourceuploadextension/notifytermination()
source_url: 'https://developer.apple.com/documentation/photos/phbackgroundresourceuploadextension/notifytermination()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phbackgroundresourceuploadextension/notifytermination%28%29.json'
content_hash: 'sha256:5df0d9332e9a0723'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHBackgroundResourceUploadExtension](../phbackgroundresourceuploadextension.md)

# notifyTermination()

<sub>Instance Method</sub>

This notification will be called if the host is going to suspend/terminate the current execution. Extension clients should use this to stop the current execution. When the extension is activated, a new call will be presented by the host.

> [!warning] Deprecated
> Adopt PHBackgroundResourceUploadJobExtension instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func notifyTermination()
```
