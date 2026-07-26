---
title: NSTextContainer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer.json'
content_hash: 'sha256:b6f8ec798d71e65b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextContainer

<sub>Class</sub>

A region where text layout occurs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextContainer
```

## Overview

An [NSLayoutManager](nslayoutmanager.md) uses [NSTextContainer](nstextcontainer.md) to determine where to break lines, lay out portions of text, and so on. An [NSTextContainer](nstextcontainer.md) object typically defines rectangular regions, but you can define exclusion paths inside the text container to create regions where text doesn’t flow. You can also subclass to create text containers with nonrectangular regions, such as circular regions, regions with holes in them, or regions that flow alongside graphics.

You can access instances of the [NSTextContainer](nstextcontainer.md), [NSLayoutManager](nslayoutmanager.md), and [NSTextStorage](nstextstorage.md) classes from threads other than the main thread as long as the app guarantees access from only one thread at a time.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)

## Topics

### Creating a text container

- [- initWithSize:](<nstextcontainer/init(size_).md>) — Initializes a text container with a specified bounding rectangle.
- [- initWithCoder:](<nstextcontainer/init(coder_).md>) — Creates a text container from data in an unarchiver.

### Managing text components

- [layoutManager](nstextcontainer/layoutmanager.md) — The text container’s layout manager.
- [textLayoutManager](nstextcontainer/textlayoutmanager.md) — The [NSTextLayoutManager](nstextlayoutmanager.md) owning the text container.
- [- replaceLayoutManager:](<nstextcontainer/replacelayoutmanager(__).md>) — Replaces the layout manager for the group of text system objects that contains the text container.
- [textView](../appkit/nstextcontainer/textview.md) — The text container’s text view.

### Defining the container shape

- [size](nstextcontainer/size.md) — The size of the text container’s bounding rectangle.
- [exclusionPaths](nstextcontainer/exclusionpaths.md) — An array of path objects that represents the regions where text doesn’t display in the text container.
- [lineBreakMode](nstextcontainer/linebreakmode.md) — The behavior of the last line inside the text container.
- [widthTracksTextView](nstextcontainer/widthtrackstextview.md) — A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.
- [heightTracksTextView](nstextcontainer/heighttrackstextview.md) — A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.

### Constraining text layout

- [maximumNumberOfLines](nstextcontainer/maximumnumberoflines.md) — The maximum number of lines that the text container can store.
- [lineFragmentPadding](nstextcontainer/linefragmentpadding.md) — The value for the text inset within line fragment rectangles.
- [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<nstextcontainer/linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>) — Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.
- [simpleRectangularTextContainer](nstextcontainer/issimplerectangulartextcontainer.md) — A Boolean that indicates whether the text container’s region is a rectangle with no holes or gaps, and whose edges are parallel to the text view’s coordinate system axes.

### Deprecated

- [init(containerSize:)](<../appkit/nstextcontainer/init(containersize_).md>) — Initializes a text container with a specified bounding rectangle. _(deprecated)_
- [lineFragmentRect(forProposedRect:sweepDirection:movementDirection:remaining:)](<../appkit/nstextcontainer/linefragmentrect(forproposedrect_sweepdirection_movementdirection_remaining_).md>) — Calculates and returns the longest rectangle available in the proposed rectangle for displaying text. _(deprecated)_
- [contains(_:)](<../appkit/nstextcontainer/contains(__).md>) — Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle. _(deprecated)_
- [containerSize](../appkit/nstextcontainer/containersize.md) — The size of the text container’s bounding rectangle. _(deprecated)_

## See Also

### Layout

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md) — Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md) — Lay out text in a custom-shaped container and apply glyph substitutions.
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — Customize layout and preserve attachment views in your text view subclass.
- [NSTextLayoutManager](nstextlayoutmanager.md) — The primary class that you use to manage text layout and presentation for custom text displays.
- [NSTextLayoutFragment](nstextlayoutfragment.md) — A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [NSTextLineFragment](nstextlinefragment.md) — A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — Manages the layout process inside the viewport interacting with its delegate.
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — A protocol that identifies a view or layer as a drawable element for a text layout fragment. _(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — A set of methods that define the orientation of text for an object.
