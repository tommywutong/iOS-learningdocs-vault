---
title: AVLegibleMediaOptionsMenuController.MenuContents
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avlegiblemediaoptionsmenucontroller/menucontents
source_url: 'https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/menucontents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avlegiblemediaoptionsmenucontroller/menucontents.json'
content_hash: 'sha256:980e753a5810d932'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVLegibleMediaOptionsMenuController](../avlegiblemediaoptionsmenucontroller.md)

# AVLegibleMediaOptionsMenuController.MenuContents

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct MenuContents
```

## Overview

```
		An option set, describing the different contents of legible option menus.
```

```
		Describes the legible contents of a legible options menu
```

```
		Describes the caption appearance contents of a legible options menu.
```

```
		Describes all the contents of a legible options menu.
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating menu contents

- [init(rawValue:)](<menucontents/init(rawvalue_).md>)

### Menu Content Options

- [AVLegibleMediaOptionsMenuContentsAll](menucontents/all.md)
- [AVLegibleMediaOptionsMenuContentsCaptionAppearance](menucontents/captionappearance.md)
- [AVLegibleMediaOptionsMenuContentsLegible](menucontents/legible.md)

## See Also

### Managing the menu

- [- menuWithContents:](<menu(contents_).md>)
- [menuState](menustate.md)
- [AVLegibleMediaOptionsMenuState](../avlegiblemediaoptionsmenustate.md)
- [StateChangeReason](statechangereason.md)
