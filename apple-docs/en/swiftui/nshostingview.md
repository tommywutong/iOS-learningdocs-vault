---
title: NSHostingView
framework: SwiftUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingview
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingview.json'
content_hash: 'sha256:b4bc9bb232571000'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NSHostingView

<sub>Class</sub>

An AppKit view that hosts a SwiftUI view hierarchy.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency class NSHostingView<Content> where Content : View
```

## Overview

You use `NSHostingView` objects to integrate SwiftUI views into your AppKit view hierarchies. A hosting view is an [NSView](../appkit/nsview.md) object that manages a single SwiftUI view, which may itself contain other SwiftUI views. Because it is an [NSView](../appkit/nsview.md) object, you can integrate it into your existing AppKit view hierarchies to implement portions of your UI. For example, you can use a hosting view to implement a custom control.

A hosting view acts as a bridge between your SwiftUI views and your AppKit interface. During layout, the hosting view reports the content size preferences of your SwiftUI views back to the AppKit layout system so that it can size the view appropriately. The hosting view also coordinates event delivery.

## Relationships

- **Inherits From**: [NSView](../appkit/nsview.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](../appkit/nsdraggingdestination.md), [NSDraggingSource](../appkit/nsdraggingsource.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [NSUserInterfaceValidations](../appkit/nsuserinterfacevalidations.md)

## Topics

### Creating a hosting view

- [init(rootView:)](<nshostingview/init(rootview_).md>) — Creates a hosting view object that wraps the specified SwiftUI view.
- [init(coder:)](<nshostingview/init(coder_).md>) — Creates a hosting view object from the contents of the specified archive.
- [prepareForReuse()](<nshostingview/prepareforreuse().md>)

### Getting the root view

- [rootView](nshostingview/rootview.md) — The root view of the SwiftUI view hierarchy managed by this view controller.

### Configuring the view layout behavior

- [requiresConstraintBasedLayout](nshostingview/requiresconstraintbasedlayout.md)
- [userInterfaceLayoutDirection](nshostingview/userinterfacelayoutdirection.md)
- [isFlipped](nshostingview/isflipped.md)
- [layerContentsRedrawPolicy](nshostingview/layercontentsredrawpolicy.md)
- [updateConstraints()](<nshostingview/updateconstraints().md>)
- [layout()](<nshostingview/layout().md>)
- [safeAreaRegions](nshostingview/safearearegions.md) — The safe area regions that this view controller adds to its view.

### Managing keyboard interaction

- [keyDown(with:)](<nshostingview/keydown(with_).md>) — Called when the user presses a key on the keyboard while this view is in the responder chain.
- [keyUp(with:)](<nshostingview/keyup(with_).md>) — Called when the user releases a key on the keyboard while this view is in the responder chain.
- [performKeyEquivalent(with:)](<nshostingview/performkeyequivalent(with_).md>)
- [insertText(_:)](<nshostingview/inserttext(__).md>)
- [didChangeValue(forKey:)](<nshostingview/didchangevalue(forkey_).md>)
- [makeTouchBar()](<nshostingview/maketouchbar().md>)

### Responding to mouse events

- [mouseDown(with:)](<nshostingview/mousedown(with_).md>)
- [mouseUp(with:)](<nshostingview/mouseup(with_).md>)
- [otherMouseDown(with:)](<nshostingview/othermousedown(with_).md>)
- [otherMouseUp(with:)](<nshostingview/othermouseup(with_).md>)
- [rightMouseDown(with:)](<nshostingview/rightmousedown(with_).md>)
- [rightMouseUp(with:)](<nshostingview/rightmouseup(with_).md>)
- [mouseEntered(with:)](<nshostingview/mouseentered(with_).md>)
- [mouseExited(with:)](<nshostingview/mouseexited(with_).md>)
- [mouseDragged(with:)](<nshostingview/mousedragged(with_).md>)
- [mouseMoved(with:)](<nshostingview/mousemoved(with_).md>)
- [otherMouseDragged(with:)](<nshostingview/othermousedragged(with_).md>)
- [rightMouseDragged(with:)](<nshostingview/rightmousedragged(with_).md>)
- [cursorUpdate(with:)](<nshostingview/cursorupdate(with_).md>)

### Responding to touch events

- [touchesBegan(with:)](<nshostingview/touchesbegan(with_).md>)
- [touchesCancelled(with:)](<nshostingview/touchescancelled(with_).md>)
- [touchesEnded(with:)](<nshostingview/touchesended(with_).md>)
- [touchesMoved(with:)](<nshostingview/touchesmoved(with_).md>)

### Responding to gestures

- [magnify(with:)](<nshostingview/magnify(with_).md>)
- [rotate(with:)](<nshostingview/rotate(with_).md>)
- [scrollWheel(with:)](<nshostingview/scrollwheel(with_).md>)

### Handling drag and drop

- [validRequestor(forSendType:returnType:)](<nshostingview/validrequestor(forsendtype_returntype_).md>)

### Providing a context menu

- [menu(for:)](<nshostingview/menu(for_).md>)

### Responding to actions

- [responds(to:)](<nshostingview/responds(to_).md>)
- [forwardingTarget(for:)](<nshostingview/forwardingtarget(for_).md>)
- [doCommand(by:)](<nshostingview/docommand(by_).md>)

### Configuring the responder behavior

- [acceptsFirstResponder](nshostingview/acceptsfirstresponder.md)
- [needsPanelToBecomeKey](nshostingview/needspaneltobecomekey.md)

### Managing the view hierarchy

- [viewWillMove(toWindow:)](<nshostingview/viewwillmove(towindow_).md>)
- [viewDidMoveToWindow()](<nshostingview/viewdidmovetowindow().md>)
- [viewDidChangeBackingProperties()](<nshostingview/viewdidchangebackingproperties().md>)
- [viewDidChangeEffectiveAppearance()](<nshostingview/viewdidchangeeffectiveappearance().md>)

### Modifying the frame rectangle

- [intrinsicContentSize](nshostingview/intrinsiccontentsize.md)
- [setFrameSize(_:)](<nshostingview/setframesize(__).md>)
- [firstBaselineOffsetFromTop](nshostingview/firstbaselineoffsetfromtop.md)
- [lastBaselineOffsetFromBottom](nshostingview/lastbaselineoffsetfrombottom.md)
- [sizingOptions](nshostingview/sizingoptions.md) — The options for how the hosting view creates and updates constraints based on the size of its SwiftUI content.
- [firstTextLineCenter](nshostingview/firsttextlinecenter.md)

### Testing for hits

- [hitTest(_:)](<nshostingview/hittest(__).md>)

### Managing accessibility behaviors

- [accessibilityFocusedUIElement](nshostingview/accessibilityfocuseduielement.md)
- [accessibilityChildren()](<nshostingview/accessibilitychildren().md>)
- [accessibilityChildrenInNavigationOrder()](<nshostingview/accessibilitychildreninnavigationorder().md>)
- [accessibilityHitTest(_:)](<nshostingview/accessibilityhittest(__).md>)
- [accessibilityRole()](<nshostingview/accessibilityrole().md>)
- [accessibilitySubrole()](<nshostingview/accessibilitysubrole().md>)
- [isAccessibilityElement()](<nshostingview/isaccessibilityelement().md>)

### Bridging with SwiftUI

- [sceneBridgingOptions](nshostingview/scenebridgingoptions.md) — The options for which aspects of the window will be managed by this hosting view.

### Initializers

- [init(coder:rootView:)](<nshostingview/init(coder_rootview_).md>) — Creates a hosting view object from an archive and the specified SwiftUI view.

### Instance Properties

- [clipsToBounds](nshostingview/clipstobounds.md)

### Instance Methods

- [acceptsFirstMouse(for:)](<nshostingview/acceptsfirstmouse(for_).md>)
- [beginDocument()](<nshostingview/begindocument().md>)
- [didAddSubview(_:)](<nshostingview/didaddsubview(__).md>)
- [endDocument()](<nshostingview/enddocument().md>)
- [observeValue(forKeyPath:of:change:context:)](<nshostingview/observevalue(forkeypath_of_change_context_).md>)
- [shouldDelayWindowOrdering(for:)](<nshostingview/shoulddelaywindowordering(for_).md>)
- [viewDidEndLiveResize()](<nshostingview/viewdidendliveresize().md>)
- [viewWillStartLiveResize()](<nshostingview/viewwillstartliveresize().md>)
- [willRemoveSubview(_:)](<nshostingview/willremovesubview(__).md>)

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingController](nshostingcontroller.md) — An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingMenu](nshostingmenu.md) — An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSizingOptions](nshostingsizingoptions.md) — Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneRepresentation](nshostingscenerepresentation.md) — An AppKit type that hosts and can present SwiftUI scenes
- [NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md) — Options for how hosting views and controllers manage aspects of the associated window.
