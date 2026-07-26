---
title: borderless()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/borderless()
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/borderless()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/borderless%28%29.json'
content_hash: 'sha256:9f0971de86cdc7a2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# borderless()

<sub>Type Method</sub>

Creates a configuration for a button that has a borderless style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func borderless() -> UIButton.Configuration
```

## Return Value

A new configuration object.

## Discussion

This style provides an alternative name for the [plain()](<plain().md>) style.

## See Also

### Creating configurations

- [plain()](<plain().md>) — Creates a configuration for a button with a transparent background.
- [gray()](<gray().md>) — Creates a configuration for a button with a gray background.
- [tinted()](<tinted().md>) — Creates a configuration for a button with a tinted background color.
- [filled()](<filled().md>) — Creates a configuration for a button with a background filled with the button’s tint color.
- [bordered()](<bordered().md>) — Creates a configuration for a button that has a bordered style.
- [borderedTinted()](<borderedtinted().md>) — Creates a configuration for a button that has a tinted, bordered style.
- [borderedProminent()](<borderedprominent().md>) — Creates a configuration for a button that has a prominent, bordered style.
- [glass()](<glass().md>) — Creates a configuration for a button that has a Liquid Glass style.
- [prominentGlass()](<prominentglass().md>) — Creates a configuration for a button that has a prominent Liquid Glass style.
- [clearGlass()](<clearglass().md>) — Creates a configuration for a button that has a clear Liquid Glass style.
- [prominentClearGlass()](<prominentclearglass().md>) — Creates a configuration for a button that has a prominent, clear Liquid Glass style.
- [updated(for:)](<updated(for_).md>) — Returns a copy of the configuration, updated for the given button.
