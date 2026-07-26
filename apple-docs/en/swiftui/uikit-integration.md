---
title: UIKit integration
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uikit-integration
source_url: 'https://developer.apple.com/documentation/swiftui/uikit-integration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uikit-integration.json'
content_hash: 'sha256:cbacfc35dccf3bbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIKit integration

<sub>API Collection</sub>

Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.

## Overview

Integrate SwiftUI with your app’s existing content using hosting controllers to add SwiftUI views into UIKit interfaces. A hosting controller wraps a set of SwiftUI views in a form that you can then add to your storyboard-based app.

![](../../../attachments/74ee52cce15bcc5332715296b5d568d9/uikit-integration-hero@2x.png)

You can also add UIKit views and view controllers to your SwiftUI interfaces. A representable object wraps the designated view or view controller, and facilitates communication between the wrapped object and your SwiftUI views.

For design guidance, see the following sections in the Human Interface Guidelines:

- [Designing for iOS](../design/human-interface-guidelines/designing-for-ios.md)
- [Designing for iPadOS](../design/human-interface-guidelines/designing-for-ipados.md)
- [Designing for tvOS](../design/human-interface-guidelines/designing-for-tvos.md)

## Topics

### Displaying SwiftUI views in UIKit

- [Using SwiftUI with UIKit](../uikit/using-swiftui-with-uikit.md) — Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [UIHostingController](uihostingcontroller.md) — A UIKit view controller that manages a SwiftUI view hierarchy.
- [UIHostingControllerSizingOptions](uihostingcontrollersizingoptions.md) — Options for how a hosting controller tracks its content’s size.
- [UIHostingConfiguration](uihostingconfiguration.md) — A content configuration suitable for hosting a hierarchy of SwiftUI views.
- [UIHostingSceneDelegate](uihostingscenedelegate.md) — Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.

### Adding UIKit views to SwiftUI view hierarchies

- [UIViewRepresentable](uiviewrepresentable.md) — A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [UIViewRepresentableContext](uiviewrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your UIKit view.
- [UIViewControllerRepresentable](uiviewcontrollerrepresentable.md) — A view that represents a UIKit view controller.
- [UIViewControllerRepresentableContext](uiviewcontrollerrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your UIKit view controller.

### Adding UIKit gesture recognizers into SwiftUI view hierarchies

- [UIGestureRecognizerRepresentable](uigesturerecognizerrepresentable.md) — A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [UIGestureRecognizerRepresentableContext](uigesturerecognizerrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update a represented gesture recognizer.
- [UIGestureRecognizerRepresentableCoordinateSpaceConverter](uigesturerecognizerrepresentablecoordinatespaceconverter.md) — A proxy structure used to convert locations to/from coordinate spaces in the hierarchy of the SwiftUI view associated with a [UIGestureRecognizerRepresentable](uigesturerecognizerrepresentable.md).

### Sharing configuration information

- [UITraitBridgedEnvironmentKey](uitraitbridgedenvironmentkey.md)

### Hosting an ornament in UIKit

- [UIHostingOrnament](uihostingornament.md) — A model that represents an ornament suitable for being hosted in UIKit.
- [UIOrnament](uiornament.md) — The abstract base class that represents an ornament.

## See Also

### Framework integration

- [AppKit integration](appkit-integration.md) — Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.
- [WatchKit integration](watchkit-integration.md) — Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.
- [Technology-specific views](technology-specific-views.md) — Use SwiftUI views that other Apple frameworks provide.
