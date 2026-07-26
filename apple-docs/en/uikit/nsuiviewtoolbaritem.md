---
title: NSUIViewToolbarItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsuiviewtoolbaritem
source_url: 'https://developer.apple.com/documentation/uikit/nsuiviewtoolbaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsuiviewtoolbaritem.json'
content_hash: 'sha256:037df69d3a2a0966'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSUIViewToolbarItem

<sub>Class</sub>

An item in a window’s toolbar that hosts a custom UIKit view.

<sub>Mac Catalyst</sub>

```swift
class NSUIViewToolbarItem
```

## Overview

The [NSUIViewToolbarItem](nsuiviewtoolbaritem.md) class lets you display a [UIView](uiview.md) in an [NSToolbar](../appkit/nstoolbar.md). Use this class if you have a custom UIKit view you want to appear as a control in a toolbar when you build your app with Mac Catalyst.

For UIKit controls that support behavioral styles, set [preferredBehavioralStyle](uibutton/preferredbehavioralstyle.md) to [UIBehavioralStyleMac](uibehavioralstyle/mac.md) if you want them to appear in the toolbar with the appearance and behavior of AppKit controls.

## Relationships

- **Inherits From**: [NSToolbarItem](../appkit/nstoolbaritem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## Topics

### Creating a toolbar item

- [- initWithItemIdentifier:uiView:](<nsuiviewtoolbaritem/init(itemidentifier_uiview_).md>) — Creates a toolbar item with the identifier and underlying UIKit view you specify.

### Managing the view

- [uiView](nsuiviewtoolbaritem/uiview.md) — The UIKit view to host in an AppKit toolbar.

## See Also

### Items

- [NSToolbarItem](../appkit/nstoolbaritem.md) — A single item that appears in a window’s toolbar.
- [NSToolbarItemGroup](../appkit/nstoolbaritemgroup.md) — A group of subitems in a toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](../appkit/nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [NSToolbarItemGroup.SelectionMode](../appkit/nstoolbaritemgroup/selectionmode-swift.enum.md) — A value that indicates how a grouped toolbar item selects its subitems.
- [NSMenuToolbarItem](../appkit/nsmenutoolbaritem.md) — A control that presents a menu in a window’s toolbar.
- [NSSearchToolbarItem](../appkit/nssearchtoolbaritem.md) — A toolbar item that contains a search field optimized for performing text-based searches.
- [NSTrackingSeparatorToolbarItem](../appkit/nstrackingseparatortoolbaritem.md) — A toolbar separator that aligns with the vertical split view in the same window.
