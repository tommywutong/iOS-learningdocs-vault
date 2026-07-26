---
title: 'loadTransferable(type:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/photospickeritem/loadtransferable(type:)'
source_url: 'https://developer.apple.com/documentation/photosui/photospickeritem/loadtransferable(type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospickeritem/loadtransferable%28type%3A%29.json'
content_hash: 'sha256:8eb9d8be3e8854d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PhotosPickerItem](../photospickeritem.md)

# loadTransferable(type:)

<sub>Instance Method</sub>

Attempts to load an instance of the type you specify from the item provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func loadTransferable<T>(type: T.Type) async throws -> sending T? where T : Transferable
```

## Parameters

- `type` — A conforming type to load from an item provider.

## Return Value

A `Progress` object that reports the loading progress; otherwise, `nil` if the system doesn’t find a supported content type.

## See Also

### Loading the provider’s contents

- [loadTransferable(type:completionHandler:)](<loadtransferable(type_completionhandler_).md>) — Attempts to load an instance of the type you specify from the item provider, with a completion handler.
