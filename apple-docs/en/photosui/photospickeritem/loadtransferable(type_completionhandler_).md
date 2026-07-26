---
title: 'loadTransferable(type:completionHandler:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/photospickeritem/loadtransferable(type:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/photosui/photospickeritem/loadtransferable(type:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospickeritem/loadtransferable%28type%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:d7542b71b650055b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PhotosPickerItem](../photospickeritem.md)

# loadTransferable(type:completionHandler:)

<sub>Instance Method</sub>

Attempts to load an instance of the type you specify from the item provider, with a completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@discardableResult @preconcurrency func loadTransferable<T>(type: T.Type, completionHandler: @escaping @Sendable (Result<T?, any Error>) -> Void) -> Progress where T : Transferable
```

## Parameters

- `type` — A conforming type to load from an item provider.

- `completionHandler` — The completion callback handler with a result object that contains an instance if the system finds a supported content type; otherwise, `nil`.

## See Also

### Loading the provider’s contents

- [loadTransferable(type:)](<loadtransferable(type_).md>) — Attempts to load an instance of the type you specify from the item provider.
