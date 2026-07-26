---
title: NSTextViewportLayoutControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextviewportlayoutcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontrollerdelegate.json'
content_hash: 'sha256:7d47598882247f0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextViewportLayoutControllerDelegate

<sub>Protocol</sub>

Optional methods that delegates implement to respond to viewport layout changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextViewportLayoutControllerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UITextView](uitextview.md)

## Topics

### Responding to changes in the viewport

- [- textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:](<nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(__configurerenderingsurfacefor_).md>) — The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [- textViewportLayoutControllerDidLayout:](<nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout(__).md>) — The method the framework calls when the text viewport layout controller finishes its layout process.
- [- textViewportLayoutControllerWillLayout:](<nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout(__).md>) — The method the framework calls before the text viewport layout controller starts its layout process.
- [- textViewportLayoutControllerReceivedSetNeedsLayout:](<nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerreceivedsetneedslayout(__).md>) — Triggers relayout of the view.
- [- viewportBoundsForTextViewportLayoutController:](<nstextviewportlayoutcontrollerdelegate/viewportbounds(for_).md>) — Returns the current viewport, which is the view visible bounds plus the overdraw area.

### Storing rendering surfaces

- [- textViewportLayoutController:cacheRenderingSurface:forKey:](<nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(__cacherenderingsurface_for_).md>) — Asks the delegate to cache a rendering surface for later retrieval.
- [- textViewportLayoutController:retrieveCachedRenderingSurfaceForKey:](<nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(__retrievecachedrenderingsurfacefor_).md>) — Asks the delegate to return a previously cached rendering surface.

## See Also

### Responding to changes in viewport layout

- [delegate](nstextviewportlayoutcontroller/delegate.md) — The delegate for the text layout manager object.
