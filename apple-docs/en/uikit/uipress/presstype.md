---
title: UIPress.PressType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/presstype
source_url: 'https://developer.apple.com/documentation/uikit/uipress/presstype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/presstype.json'
content_hash: 'sha256:0351df189511da1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPress](../uipress.md)

# UIPress.PressType

<sub>Enumeration</sub>

Constants that represent buttons that a person can press.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum PressType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Actions

- [UIPressTypePlayPause](presstype/playpause.md) — A constant that represents the play/pause button.
- [UIPressTypeSelect](presstype/select.md) — A constant that represents the select button.
- [UIPressTypeMenu](presstype/menu.md) — A constant that represents the menu button.

### Navigation

- [UIPressTypeUpArrow](presstype/uparrow.md) — A constant that represents the up arrow button.
- [UIPressTypeDownArrow](presstype/downarrow.md) — A constant that represents the down arrow button.
- [UIPressTypeLeftArrow](presstype/leftarrow.md) — A constant that represents the left arrow button.
- [UIPressTypeRightArrow](presstype/rightarrow.md) — A constant that represents the right arrow button.
- [UIPressTypePageDown](presstype/pagedown.md) — A constant that represents the page down button.
- [UIPressTypePageUp](presstype/pageup.md) — A constant that represents the page up button.

### Enumeration Cases

- [UIPressTypeTVRemoteFourColors](presstype/tvremotefourcolors.md) — Represents a button on a TV remote labeled with four colors, analogous to the four separate color buttons found on some TV remotes. When this button is pressed, an app should perform the appropriate color action or if there are multiple color actions available provide UI to choose the specific color.
- [UIPressTypeTVRemoteOneTwoThree](presstype/tvremoteonetwothree.md) — Represents a button on a TV remote labeled with 123. When this button is pressed, an app should provide UI to enter a specific channel number if channel numbers are available. If no channel numbers exist the app should provide UI to toggle channel category filters, search for channels by name or search for currently airing shows.

### Initializers

- [init(rawValue:)](<presstype/init(rawvalue_).md>)

## See Also

### Constants

- [Phase](phase-swift.enum.md) — Constants that represent the phases of a button press.
