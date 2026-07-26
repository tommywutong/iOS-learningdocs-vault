---
title: UIToolTipConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitooltipconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipconfiguration.json'
content_hash: 'sha256:06a055f8e6edbf09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIToolTipConfiguration

<sub>Class</sub>

An object that a tooltip interaction delegate uses to describe the tooltip settings.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIToolTipConfiguration
```

## Overview

Use a tooltip configuration to specify:

- The text that appears in the tooltip.
- The region that the pointer must hover over to trigger the appearance of the tooltip.

A [UIToolTipInteraction](uitooltipinteraction.md) object asks for a configuration from its [delegate](uitooltipinteraction/delegate.md) by calling the delegate method [- toolTipInteraction:configurationAtPoint:](<uitooltipinteractiondelegate/tooltipinteraction(__configurationat_).md>).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a tooltip configuration

- [+ configurationWithToolTip:](<uitooltipconfiguration/init(tooltip_).md>) — Creates a tooltip configuration and sets the tooltip text.
- [+ configurationWithToolTip:inRect:](<uitooltipconfiguration/init(tooltip_in_).md>) — Creates a tooltip configuration, and sets the tooltip text and hover region within the view or control.

### Accessing the configuration settings

- [toolTip](uitooltipconfiguration/tooltip.md) — The text to display in the tooltip.
- [sourceRect](uitooltipconfiguration/sourcerect-8zvo1.md) — The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.

### Initializers

- [init(toolTip:inRect:)](<uitooltipconfiguration/init(tooltip_inrect_).md>)

## See Also

### Providing a tooltip configuration

- [- toolTipInteraction:configurationAtPoint:](<uitooltipinteractiondelegate/tooltipinteraction(__configurationat_).md>) — Asks the delegate for a tooltip configuration that describes the tooltip settings.
