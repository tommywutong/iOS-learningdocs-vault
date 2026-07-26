---
title: UISplitViewController.SplitBehavior
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum.json'
content_hash: 'sha256:7a4c3a71c3119b57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# UISplitViewController.SplitBehavior

<sub>Enumeration</sub>

Constants that describe the possible ways that the child view controllers appear in relation to each other.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum SplitBehavior
```

## Overview

A split view controller’s split behavior controls how its secondary view controller appears in relation to the others. You can configure this behavior so that the secondary view controller always appears side-by-side with the others, so that it’s partially obscured by the others, or so that it’s displaced offscreen opposite the others to make space for them.

A split view controller’s split behavior affects its possible display mode ([displayMode](displaymode-swift.property.md)). For more information, see [DisplayMode](displaymode-swift.enum.md).

| Split Behavior | Possible Display Modes |
|---|---|
| Tile | [UISplitViewControllerDisplayModeSecondaryOnly](displaymode-swift.enum/secondaryonly.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UISplitViewControllerDisplayModeOneBesideSecondary](displaymode-swift.enum/onebesidesecondary.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UISplitViewControllerDisplayModeTwoBesideSecondary](displaymode-swift.enum/twobesidesecondary.md) |
| Overlay | [UISplitViewControllerDisplayModeSecondaryOnly](displaymode-swift.enum/secondaryonly.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UISplitViewControllerDisplayModeOneOverSecondary](displaymode-swift.enum/oneoversecondary.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UISplitViewControllerDisplayModeTwoOverSecondary](displaymode-swift.enum/twooversecondary.md) |
| Displace | [UISplitViewControllerDisplayModeSecondaryOnly](displaymode-swift.enum/secondaryonly.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UISplitViewControllerDisplayModeOneBesideSecondary](displaymode-swift.enum/onebesidesecondary.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UISplitViewControllerDisplayModeTwoDisplaceSecondary](displaymode-swift.enum/twodisplacesecondary.md) |

![Diagram showing a triple-column split view interface using the tile, overlay, and displace split behaviors.](../../../../attachments/21d48e2a49ece64105122059913f0374/UISplitViewController-4@2x.png)

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UISplitViewControllerSplitBehaviorAutomatic](splitbehavior-swift.enum/automatic.md) — The split view controller automatically decides the most appropriate split behavior based on the device and the current app size.
- [UISplitViewControllerSplitBehaviorTile](splitbehavior-swift.enum/tile.md) — The sidebars and secondary view controller appear tiled side-by-side.
- [UISplitViewControllerSplitBehaviorOverlay](splitbehavior-swift.enum/overlay.md) — The sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewControllerSplitBehaviorDisplace](splitbehavior-swift.enum/displace.md) — The sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.

### Initializers

- [init(rawValue:)](<splitbehavior-swift.enum/init(rawvalue_).md>)

## See Also

### Managing the split behavior

- [preferredSplitBehavior](preferredsplitbehavior.md) — The preferred behavior that determines how the child view controllers appear in relation to each other.
- [splitBehavior](splitbehavior-swift.property.md) — The current behavior that determines how the child view controllers appear in relation to each other.
