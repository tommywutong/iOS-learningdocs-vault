---
title: App organization
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/app-organization
source_url: 'https://developer.apple.com/documentation/swiftui/app-organization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/app-organization.json'
content_hash: 'sha256:fbddcc403622a756'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# App organization

<sub>API Collection</sub>

Define the entry point and top-level structure of your app.

## Overview

Describe your app’s structure declaratively, much like you declare a view’s appearance. Create a type that conforms to the [App](app.md) protocol and use it to enumerate the [Scenes](scenes.md) that represent aspects of your app’s user interface.

![](../../../attachments/37814b39f4f1ecc76cd13f967145c10e/app-organization-hero@2x.png)

SwiftUI enables you to write code that works across all of Apple’s platforms. However, it also enables you to tailor your app to the specific capabilities of each platform. For example, if you need to respond to the callbacks that the system traditionally makes on a UIKit, AppKit, or WatchKit app’s delegate, define a delegate object and instantiate it in your app structure using an appropriate delegate adaptor property wrapper, like [UIApplicationDelegateAdaptor](uiapplicationdelegateadaptor.md).

For platform-specific design guidance, see [Getting started](../design/human-interface-guidelines/getting-started.md) in the Human Interface Guidelines.

## Topics

### Creating an app

- [Destination Video](../visionos/destination-video.md) — Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Hello World](../visionos/world.md) — Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Backyard Birds: Building an app with SwiftData and widgets](backyard-birds-sample.md) — Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
- [Food Truck: Building a SwiftUI multiplatform app](food-truck-building-a-swiftui-multiplatform-app.md) — Create a single codebase and app target for Mac, iPad, and iPhone.
- [Fruta: Building a feature-rich app with SwiftUI](../appclip/fruta-building-a-feature-rich-app-with-swiftui.md) — Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- [Migrating to the SwiftUI life cycle](migrating-to-the-swiftui-life-cycle.md) — Use a scene-based life cycle in SwiftUI while keeping your existing codebase.
- [App](app.md) — A type that represents the structure and behavior of an app.

### Targeting iOS and iPadOS

- [UILaunchScreen](../bundleresources/information-property-list/uilaunchscreen.md) — The user interface to show while an app launches.
- [UILaunchScreens](../bundleresources/information-property-list/uilaunchscreens.md) — The user interfaces to show while an app launches in response to different URL schemes.
- [UIApplicationDelegateAdaptor](uiapplicationdelegateadaptor.md) — A property wrapper type that you use to create a UIKit app delegate.

### Targeting macOS

- [NSApplicationDelegateAdaptor](nsapplicationdelegateadaptor.md) — A property wrapper type that you use to create an AppKit app delegate.

### Targeting watchOS

- [WKApplicationDelegateAdaptor](wkapplicationdelegateadaptor.md) — A property wrapper that is used in `App` to provide a delegate from WatchKit.
- [WKExtensionDelegateAdaptor](wkextensiondelegateadaptor.md) — A property wrapper type that you use to create a WatchKit extension delegate. _(deprecated)_

### Targeting tvOS

- [Creating a tvOS media catalog app in SwiftUI](creating-a-tvos-media-catalog-app-in-swiftui.md) — Build standard content lockups and rows of content shelves for your tvOS app.

### Handling system recenter events

- [WorldRecenterPhase](worldrecenterphase.md) — A type that represents information associated with a phase of a system recenter event. Values of this type are passed to the closure specified in View.onWorldRecenter(action:).

## See Also

### App structure

- [Scenes](scenes.md) — Declare the user interface groupings that make up the parts of your app.
- [Windows](windows.md) — Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md) — Display unbounded content in a person’s surroundings.
- [Documents](documents.md) — Enable people to open and manage documents.
- [Navigation](navigation.md) — Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md) — Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md) — Provide immediate access to frequently used commands and controls.
- [Search](search.md) — Enable people to search for text or other content within your app.
- [App extensions](app-extensions.md) — Extend your app’s basic functionality to other parts of the system, like by adding a Widget.
