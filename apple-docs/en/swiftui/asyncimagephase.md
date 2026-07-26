---
title: AsyncImagePhase
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/asyncimagephase
source_url: 'https://developer.apple.com/documentation/swiftui/asyncimagephase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/asyncimagephase.json'
content_hash: 'sha256:6587fbc89a613387'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AsyncImagePhase

<sub>Enumeration</sub>

The current phase of the asynchronous image loading operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AsyncImagePhase
```

## Overview

When you create an [AsyncImage](asyncimage.md) instance with the [init(url:scale:transaction:content:)](<asyncimage/init(url_scale_transaction_content_).md>) initializer, you define the appearance of the view using a `content` closure. SwiftUI calls the closure with a phase value at different points during the load operation to indicate the current state. Use the phase to decide what to draw. For example, you can draw the loaded image if it exists, a view that indicates an error, or a placeholder:

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

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting load phases

- [AsyncImagePhase.empty](asyncimagephase/empty.md) — No image is loaded.
- [AsyncImagePhase.success(_:)](<asyncimagephase/success(__).md>) — An image successfully loaded.
- [AsyncImagePhase.failure(_:)](<asyncimagephase/failure(__).md>) — An image failed to load with an error.

### Getting the image

- [image](asyncimagephase/image.md) — The loaded image, if any.

### Getting the error

- [error](asyncimagephase/error.md) — The error that occurred when attempting to load an image, if any.

## See Also

### Loading images asynchronously

- [AsyncImage](asyncimage.md) — A view that asynchronously loads and displays an image.
