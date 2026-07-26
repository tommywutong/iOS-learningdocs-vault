---
title: UIFontMetrics
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontmetrics
source_url: 'https://developer.apple.com/documentation/uikit/uifontmetrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontmetrics.json'
content_hash: 'sha256:7cc6a266d5c59404'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFontMetrics

<sub>Class</sub>

A utility object for obtaining custom fonts that scale to support Dynamic Type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class UIFontMetrics
```

## Overview

Use a [UIFontMetrics](uifontmetrics.md) object to support scalable custom fonts in your app. You create a font metrics object that specifies the font style—for example, body or title—that you want to use in your app. You then pass your custom font to the [- scaledFontForFont:](<uifontmetrics/scaledfont(for_).md>) method (or one of the other methods of this class) to obtain a font object that is based on your custom font, has the appropriate style information, and automatically scales to match the current Dynamic Type settings.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Font Metrics Object

- [- initForTextStyle:](<uifontmetrics/init(fortextstyle_).md>) — Creates a font metrics object for the specified text style.
- [defaultMetrics](uifontmetrics/default.md) — The default font metrics object for content.
- [TextStyle](uifont/textstyle.md) — Constants that describe the preferred styles for fonts.

### Creating Scaled Fonts

- [Scaling fonts automatically](scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [- scaledFontForFont:](<uifontmetrics/scaledfont(for_).md>) — Returns a version of the specified font that adopts the current font metrics.
- [- scaledFontForFont:compatibleWithTraitCollection:](<uifontmetrics/scaledfont(for_compatiblewith_).md>) — Returns a version of the specified font that adopts the current font metrics and supports the specified traits.
- [- scaledFontForFont:maximumPointSize:](<uifontmetrics/scaledfont(for_maximumpointsize_).md>) — Returns a version of the specified font that adopts the current font metrics and is constrained to the specified maximum size.
- [- scaledFontForFont:maximumPointSize:compatibleWithTraitCollection:](<uifontmetrics/scaledfont(for_maximumpointsize_compatiblewith_).md>) — Returns a version of the specified font that adopts the current font metrics and is constrained to the specified traits and size.

### Scaling Layout Values

- [- scaledValueForValue:](<uifontmetrics/scaledvalue(for_).md>) — Scales an arbitrary layout value based on the current Dynamic Type settings.
- [- scaledValueForValue:compatibleWithTraitCollection:](<uifontmetrics/scaledvalue(for_compatiblewith_).md>) — Scales an arbitrary layout value based on the current Dynamic Type settings and the specified traits.

## See Also

### Fonts

- [Scaling fonts automatically](scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Adding a custom font to your app](adding-a-custom-font-to-your-app.md) — Add a custom font to your app and use it in your app’s interface.
- [UIFont](uifont.md) — An object that provides access to the font’s characteristics.
- [UIFontDescriptor](uifontdescriptor.md) — A collection of attributes that describes a font.
- [SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
