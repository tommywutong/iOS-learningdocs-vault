---
title: cancelContentEditing()
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.11+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phcontenteditingcontroller/cancelcontentediting()
source_url: 'https://developer.apple.com/documentation/photosui/phcontenteditingcontroller/cancelcontentediting()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phcontenteditingcontroller/cancelcontentediting%28%29.json'
content_hash: 'sha256:64fac3ed4cba75e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHContentEditingController](../phcontenteditingcontroller.md)

# cancelContentEditing()

<sub>Instance Method</sub>

Tells your extension to cancel editing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func cancelContentEditing()
```

## Discussion

Photos may call this method at any time after your extension view controller’s view appears, including while your app is preparing the editing output.

At this time, your extension should clean up any resources related to your edit and cancel any background work. If the user cancels editing while your app is preparing output, do not call the `completionHandler` block that Photos provided in the [- finishContentEditingWithCompletionHandler:](<finishcontentediting(completionhandler_).md>) method.

## See Also

### Canceling an Edit

- [shouldShowCancelConfirmation](shouldshowcancelconfirmation.md) — A Boolean value that determines whether Photos should prompt the user when canceling the editing session.
