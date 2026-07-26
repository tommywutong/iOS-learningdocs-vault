---
title: UIDocumentBrowserTransitionController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowsertransitioncontroller
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowsertransitioncontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowsertransitioncontroller.json'
content_hash: 'sha256:c6efa44b18f32433'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentBrowserTransitionController

<sub>Class</sub>

An object that implements the standard loading and transition animations for a document browser.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDocumentBrowserTransitionController
```

## Overview

Each transition controller is associated with a document in the document browser. The transition controller can provide two separate animation sequences for this document:

- If you set the [loadingProgress](uidocumentbrowsertransitioncontroller/loadingprogress.md) property, the document browser shows the loading progress in the document’s thumbnail.
- If you set the [targetView](uidocumentbrowsertransitioncontroller/targetview.md) property, the transition controller acts as a [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md) object, providing a custom transition between the document’s thumbnail and the target view. This transitioning object can be used both when presenting and when dismissing the document.

You don’t instantiate instances of [UIDocumentBrowserTransitionController](uidocumentbrowsertransitioncontroller.md) yourself. Instead, call the document browser’s [- transitionControllerForDocumentURL:](<uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl_).md>) method to get a transition controller for the specified document.

> [!note] Note
> In Mac apps built with Mac Catalyst, the transition controller doesn’t trigger animations because the macOS design doesn’t use animations for opening or closing documents.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md)

## Topics

### Animating transitions

- [loadingProgress](uidocumentbrowsertransitioncontroller/loadingprogress.md) — A progress object that tracks a document as it loads.
- [targetView](uidocumentbrowsertransitioncontroller/targetview.md) — The target view for transition animations when presenting or dismissing the transition controller’s document.

## See Also

### Related Documentation

- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — A view controller for browsing and performing actions on documents that you store locally and in the cloud.

### Animating transitions

- [- transitionControllerForDocumentAtURL:](<uidocumentbrowserviewcontroller/transitioncontroller(fordocumentat_).md>) — Creates a transition controller that provides the standard system-loading and segue animations for the document browser.
