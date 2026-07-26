---
title: 'init(propertiesOfMetadataItem:valueLoadingHandler:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/init(propertiesofmetadataitem:valueloadinghandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/init(propertiesofmetadataitem:valueloadinghandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/init%28propertiesofmetadataitem%3Avalueloadinghandler%3A%29.json'
content_hash: 'sha256:db4ccb4595a272b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# init(propertiesOfMetadataItem:valueLoadingHandler:)

<sub>Initializer</sub>

Creates a metadata item whose value loads on an on-demand basis only.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(propertiesOfMetadataItem metadataItem: AVMetadataItem, valueLoadingHandler handler: @escaping @Sendable (AVMetadataItemValueRequest) -> Void)
```

## Parameters

- `metadataItem` — The metadata item that provides the [identifier](identifier.md), [extendedLanguageTag](extendedlanguagetag.md), and other property values that you want the newly created metadata item to share. The system ignores the value of this template metadata item.

- `handler` — A callback the system invokes to load the value for the metadata item.

## Return Value

A newly created instance of [AVMetadataItem](../avmetadataitem.md).

## Discussion

Use this method to create metadata items for optional display purposes. For example, a metadata item that provides a large image, should only load the image when the system requests it.

When you load the [value](../avpartialasyncproperty/value.md) of a metadata item you created with this initializer, the closure you provide as the value loading handler executes on an arbitrary dispatch queue, off the main thread. The handler can perform I/O and other necessary operations to obtain the value. If loading of the value succeeds, provide the value by calling [- respondWithValue:](<../avmetadataitemvaluerequest/respond(value_).md>). If loading of the value fails, provide an instance an error object that describes the failure by calling [- respondWithError:](<../avmetadataitemvaluerequest/respond(error_).md>).

```swift
// A template metadata item that provides supporting data.
let templateItem = AVMetadataItem()
let artworkItem = AVMetadataItem(propertiesOf: templateItem) { request in
    if let image = UIImage(named: "large_artwork"), let data = image.pngData() {
        request.respond(value: NSData(data: data))
    } else {
        request.respond(error: AppError.imageLoadingError)
    }
}
```

> [!note] Note
> Don’t use this method to create metadata items whose values you need immediately, such as those you create for immediate display or serialization.

## See Also

### Creating a metadata item

- [AVMetadataItemValueRequest](../avmetadataitemvaluerequest.md) — An object that responds to a request to load the value of a metadata item.
