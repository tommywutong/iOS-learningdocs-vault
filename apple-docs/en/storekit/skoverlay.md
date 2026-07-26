---
title: SKOverlay
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skoverlay
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay.json'
content_hash: 'sha256:09a975aac6b8b625'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKOverlay

<sub>Class</sub>

A class that displays an overlay you can use to recommend another app or an App Clip’s corresponding full app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class SKOverlay
```

## Overview

By displaying an overlay, you can recommend another app to users and enable them to download it immediately. To recommend media that’s not an app, or to display a product page within your app, use [SKStoreProductViewController](skstoreproductviewcontroller.md).

> [!important] Important
> If you display an overlay in your App Clip, you may only recommend the App Clip’s corresponding full app and need to initialize the overlay with an [AppClipConfiguration](skoverlay/appclipconfiguration.md) object. For more information, see [Recommending your app to App Clip users](../appclip/recommending-your-app-to-app-clip-users.md).

If you’re using SwiftUI, make use of the `appStoreOverlay(isPresented:configuration:)` modifier. For example usage, see [Fruta: Building a feature-rich app with SwiftUI](../appclip/fruta-building-a-feature-rich-app-with-swiftui.md).

To display an App Store overlay in an app that uses [UIKit](../uikit.md):

1. Create an [AppConfiguration](skoverlay/appconfiguration.md) with the iTunes identifier of the app you want to recommend.
2. Initialize `SKOverlay` with the configuration object.
3. Present the overlay.

The following code displays an overlay at the bottom of the visible scene:

```swift
func displayOverlay() {
    guard let scene = view.window?.windowScene else { return }

    let config = SKOverlay.AppConfiguration(appIdentifier: "The iTunes identifier of another app.", position: .bottom)
    let overlay = SKOverlay(configuration: config)
    overlay.present(in: scene)
}
```

To respond to the overlay’s appearance, dismissal, or failure to load, set the [delegate](skoverlay/delegate.md) and implement the methods defined in [SKOverlayDelegate](skoverlaydelegate.md).

> [!note] Note
> App extensions can’t display an overlay.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an overlay

- [- initWithConfiguration:](<skoverlay/init(configuration_).md>) — Creates an overlay you use to recommend another app on the App Store.
- [configuration](skoverlay/configuration-swift.property.md) — An overlay’s attributes; for example, its position on the screen.
- [AppConfiguration](skoverlay/appconfiguration.md) — An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [AppClipConfiguration](skoverlay/appclipconfiguration.md) — An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
- [Configuration](skoverlay/configuration-swift.class.md) — The abstract superclass for all classes that represent an overlay’s attributes.

### Presenting an overlay

- [- presentInScene:](<skoverlay/present(in_).md>) — Presents an overlay in a window scene.

### Dismissing an overlay

- [+ dismissOverlayInScene:](<skoverlay/dismiss(in_).md>) — Dismisses an App Store overlay.

### Setting a delegate

- [delegate](skoverlay/delegate.md) — The overlay’s delegate.
- [SKOverlayDelegate](skoverlaydelegate.md) — Methods for responding to the overlay’s appearance, dismissal, or failure to load.

## See Also

### Recommendations

- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md) — Allow users to purchase media in the App Store from within your app.
- [SKStoreProductViewController](skstoreproductviewcontroller.md) — A view controller that provides a page where customers can purchase media from the App Store.
