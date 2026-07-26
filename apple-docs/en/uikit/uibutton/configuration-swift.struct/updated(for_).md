---
title: 'updated(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/configuration-swift.struct/updated(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/updated(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/updated%28for%3A%29.json'
content_hash: 'sha256:bda0d4c0c378ec53'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# updated(for:)

<sub>Instance Method</sub>

Returns a copy of the configuration, updated for the given button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updated(for button: UIButton) -> UIButton.Configuration
```

## Parameters

- `button` — A button to use as a basis for the configuration.

## Return Value

An updated configuration. This method preserves custom values set on the configuration, and updates default values based on the button state.

## See Also

### Creating configurations

- [plain()](<plain().md>) — Creates a configuration for a button with a transparent background.
- [gray()](<gray().md>) — Creates a configuration for a button with a gray background.
- [tinted()](<tinted().md>) — Creates a configuration for a button with a tinted background color.
- [filled()](<filled().md>) — Creates a configuration for a button with a background filled with the button’s tint color.
- [borderless()](<borderless().md>) — Creates a configuration for a button that has a borderless style.
- [bordered()](<bordered().md>) — Creates a configuration for a button that has a bordered style.
- [borderedTinted()](<borderedtinted().md>) — Creates a configuration for a button that has a tinted, bordered style.
- [borderedProminent()](<borderedprominent().md>) — Creates a configuration for a button that has a prominent, bordered style.
- [glass()](<glass().md>) — Creates a configuration for a button that has a Liquid Glass style.
- [prominentGlass()](<prominentglass().md>) — Creates a configuration for a button that has a prominent Liquid Glass style.
- [clearGlass()](<clearglass().md>) — Creates a configuration for a button that has a clear Liquid Glass style.
- [prominentClearGlass()](<prominentclearglass().md>) — Creates a configuration for a button that has a prominent, clear Liquid Glass style.
