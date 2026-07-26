---
title: UIImage.SymbolVariableValueMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/symbolvariablevaluemode
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolvariablevaluemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolvariablevaluemode.json'
content_hash: 'sha256:52ac5e28c0b602a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# UIImage.SymbolVariableValueMode

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum SymbolVariableValueMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UIImageSymbolVariableValueModeAutomatic](symbolvariablevaluemode/automatic.md) — Automatically selects an appropriate variable value mode for the symbol.
- [UIImageSymbolVariableValueModeColor](symbolvariablevaluemode/color.md) — The “color” variable value mode. Sets the opacity of each variable layer to either on or off depending on how its threshold compared to the current value.
- [UIImageSymbolVariableValueModeDraw](symbolvariablevaluemode/draw.md) — The “draw” variable value mode. Changes the drawn length of each variable layer to either based on how its range relates to the current value.

### Initializers

- [init(rawValue:)](<symbolvariablevaluemode/init(rawvalue_).md>)

## See Also

### Creating a symbol configuration

- [+ configurationWithPointSize:](<symbolconfiguration-swift.class/init(pointsize_).md>) — Creates a configuration object with the specified point-size information.
- [+ configurationWithPointSize:weight:](<symbolconfiguration-swift.class/init(pointsize_weight_).md>) — Creates a configuration object with the specified point-size and weight information.
- [+ configurationWithPointSize:weight:scale:](<symbolconfiguration-swift.class/init(pointsize_weight_scale_).md>) — Creates a configuration object with the specified point-size, weight, and scale information.
- [+ configurationWithScale:](<symbolconfiguration-swift.class/init(scale_).md>) — Creates a configuration object with the specified scale information.
- [+ configurationWithTextStyle:](<symbolconfiguration-swift.class/init(textstyle_).md>) — Creates a configuration object with the specified font text style information.
- [+ configurationWithTextStyle:scale:](<symbolconfiguration-swift.class/init(textstyle_scale_).md>) — Creates a configuration object with the specified font text style and scale information.
- [+ configurationWithWeight:](<symbolconfiguration-swift.class/init(weight_).md>) — Creates a configuration object with the specified weight information.
- [+ configurationWithFont:](<symbolconfiguration-swift.class/init(font_).md>) — Creates a configuration object with the specified font information.
- [+ configurationWithFont:scale:](<symbolconfiguration-swift.class/init(font_scale_).md>) — Creates a configuration object with the specified font and scale information.
- [SymbolScale](symbolscale.md) — Constants that indicate which scale variant of a symbol image to use.
- [SymbolWeight](symbolweight.md) — Constants that indicate which weight variant of a symbol image to use.
- [SymbolColorRenderingMode](symbolcolorrenderingmode.md)
