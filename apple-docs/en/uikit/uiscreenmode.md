---
title: UIScreenMode
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreenmode
source_url: 'https://developer.apple.com/documentation/uikit/uiscreenmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreenmode.json'
content_hash: 'sha256:33f2b2ea3da2cc5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScreenMode

<sub>Class</sub>

A possible set of attributes that can apply to a screen object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class UIScreenMode
```

## Overview

A screen mode object encapsulates information about the size of the screen’s underlying display buffer and the aspect ratio it uses for individual pixels. Most developers should never need to use the information provided by this class and should simply use the bounds provided by the [UIScreen](uiscreen.md) object for their drawing space. The bounds of screen and window objects automatically take the pixel aspect ratio and underlying drawing hardware into consideration. However, developers that work with pixel-level information more directly may use the information in the current screen mode object to tailor their code for the target screen.

You don’t create instances of this class directly. Instead, you get the screen modes supported by a given screen from the corresponding [UIScreen](uiscreen.md) object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the screen mode attributes

- [size](uiscreenmode/size.md) — The screen size, measured in pixels.
- [pixelAspectRatio](uiscreenmode/pixelaspectratio.md) — The aspect ratio of a single pixel.

## See Also

### Screens

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md) — Fill connected displays with additional content from your app.
- [UIScreen](uiscreen.md) — An object that defines the properties associated with a hardware-based display.
