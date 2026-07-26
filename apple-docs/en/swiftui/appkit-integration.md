---
title: AppKit integration
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/appkit-integration
source_url: 'https://developer.apple.com/documentation/swiftui/appkit-integration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/appkit-integration.json'
content_hash: 'sha256:0f3518b898d916aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AppKit integration

<sub>API Collection</sub>

Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.

## Overview

Integrate SwiftUI with your app’s existing content using hosting controllers to add SwiftUI views into AppKit interfaces. A hosting controller wraps a set of SwiftUI views in a form that you can then add to your storyboard-based app.

![](../../../attachments/afddaf77e2520d7c1a298575a9bbf6d5/appkit-integration-hero@2x.png)

You can also add AppKit views and view controllers to your SwiftUI interfaces. A representable object wraps the designated view or view controller, and facilitates communication between the wrapped object and your SwiftUI views.

For design guidance, see [Designing for macOS](../design/human-interface-guidelines/designing-for-macos.md) in the Human Interface Guidelines.

## Topics

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingController](nshostingcontroller.md) — An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingView](nshostingview.md) — An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingMenu](nshostingmenu.md) — An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSizingOptions](nshostingsizingoptions.md) — Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneRepresentation](nshostingscenerepresentation.md) — An AppKit type that hosts and can present SwiftUI scenes
- [NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md) — Options for how hosting views and controllers manage aspects of the associated window.

### Adding AppKit views to SwiftUI view hierarchies

- [NSViewRepresentable](nsviewrepresentable.md) — A wrapper that you use to integrate an AppKit view into your SwiftUI view hierarchy.
- [NSViewRepresentableContext](nsviewrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your AppKit view.
- [NSViewControllerRepresentable](nsviewcontrollerrepresentable.md) — A wrapper that you use to integrate an AppKit view controller into your SwiftUI interface.
- [NSViewControllerRepresentableContext](nsviewcontrollerrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your AppKit view controller.

### Adding AppKit gesture recognizers into SwiftUI view hierarchies

- [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) — A wrapper for an `NSGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [NSGestureRecognizerRepresentableContext](nsgesturerecognizerrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update a represented gesture recognizer.
- [NSGestureRecognizerRepresentableCoordinateSpaceConverter](nsgesturerecognizerrepresentablecoordinatespaceconverter.md) — A structure used to convert locations to and from coordinate spaces in the hierarchy of the SwiftUI view associated with an [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md).

## See Also

### Framework integration

- [UIKit integration](uikit-integration.md) — Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.
- [WatchKit integration](watchkit-integration.md) — Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.
- [Technology-specific views](technology-specific-views.md) — Use SwiftUI views that other Apple frameworks provide.
