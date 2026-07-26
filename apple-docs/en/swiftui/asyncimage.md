---
title: AsyncImage
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/asyncimage
source_url: 'https://developer.apple.com/documentation/swiftui/asyncimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/asyncimage.json'
content_hash: 'sha256:0741978f13f58f30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AsyncImage

<sub>Structure</sub>

A view that asynchronously loads and displays an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct AsyncImage<Content> where Content : View
```

## Overview

This view uses the shared [URLSession](../foundation/urlsession.md) instance to load an image from a URL that you specify, and then display it. For example, you can display an icon that’s stored on a server:

```swift
AsyncImage(url: URL(string: "https://example.com/icon.png"))
    .frame(width: 200, height: 200)
```

Until the image loads, the view displays a standard placeholder that fills the available space. After the load completes successfully, the view updates to display the image. In the example above, the icon is smaller than the frame, and so appears smaller than the placeholder.

![A diagram that shows a grey box on the left, the SwiftUI icon on the](../../../attachments/7a8d82fa0ae80e1c40ba9a151d56c704/AsyncImage-1@2x.png)

> [!important] Important
> You can’t apply image-specific modifiers, like [resizable(capInsets:resizingMode:)](<image/resizable(capinsets_resizingmode_).md>), directly to an `AsyncImage`. Instead, apply them to the [Image](image.md) instance that your `content` closure gets when defining the view’s appearance.

You can manipulate the loaded image in the `content` parameter using [init(url:scale:content:placeholder:)](<asyncimage/init(url_scale_content_placeholder_).md>). For example, you can add a modifier to make the loaded image resizable:

```swift
AsyncImage(url: URL(string: "https://example.com/icon.png")) { image in
    image.resizable()
} placeholder: {
    ProgressView()
}
.frame(width: 50, height: 50)
```

With this initializer, you can also specify a custom placeholder. In the code in the previous example, SwiftUI shows a [ProgressView](progressview.md) first, and then the image scaled to fit in the specified frame:

![A diagram that shows a progress view on the left, the SwiftUI icon on the](../../../attachments/d288fdb7e0fd01131459d0fa071516aa/AsyncImage-2@2x.png)

If you use an [Image](image.md) as a placeholder view and it doesn’t load, SwiftUI doesn’t show anything as a placeholder and doesn’t report an error.

To gain more control over the loading process, use the [init(url:scale:transaction:content:)](<asyncimage/init(url_scale_transaction_content_).md>) initializer, which takes a `content` closure that receives an [AsyncImagePhase](asyncimagephase.md) to indicate the state of the loading operation. Return a view that’s appropriate for the current phase:

```swift
AsyncImage(url: URL(string: "https://example.com/icon.png")) { phase in
    if let image = phase.image {
        image // Displays the loaded image.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        Color.blue // Acts as a placeholder.
    }
}
```

In iOS 27, macOS 27, watchOS 27, tvOS 27, and visionOS 27 and later, `AsyncImage` caches downloaded image data following the transport protocol. The system creates the cache with a default [URLSessionConfiguration](../foundation/urlsessionconfiguration.md). To change the cache policy, specify the change in [URLRequest](../foundation/urlrequest.md), and pass it to [init(request:scale:transaction:content:)](<asyncimage/init(request_scale_transaction_content_).md>). To customize the download process in a specific view hierarchy, use [asyncImageURLSession(_:)](<view/asyncimageurlsession(__).md>) to specify a [URLSession](../foundation/urlsession.md). `AsyncImage` uses this session to perform data tasks when downloading the image data.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Loading an image

- [init(url:scale:)](<asyncimage/init(url_scale_).md>) — Loads and displays an image from the specified URL.
- [init(url:scale:content:placeholder:)](<asyncimage/init(url_scale_content_placeholder_).md>) — Loads and displays a modifiable image from the specified URL using a custom placeholder until the image loads.

### Loading an image in phases

- [init(url:scale:transaction:content:)](<asyncimage/init(url_scale_transaction_content_).md>) — Loads and displays a modifiable image from the specified URL in phases.

### Loading an image with a URL request

- [init(request:scale:)](<asyncimage/init(request_scale_).md>) — Loads and displays an image from the specified URL load request. _(beta)_
- [init(request:scale:content:placeholder:)](<asyncimage/init(request_scale_content_placeholder_).md>) — Loads and displays a modifiable image from the specified URL load request using a custom placeholder until the image loads. _(beta)_
- [init(request:scale:transaction:content:)](<asyncimage/init(request_scale_transaction_content_).md>) — Loads and displays a modifiable image from the specified URL load request in phases. _(beta)_

## See Also

### Loading images asynchronously

- [AsyncImagePhase](asyncimagephase.md) — The current phase of the asynchronous image loading operation.
