---
title: prominentGlass()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/prominentglass()
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/prominentglass()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/prominentglass%28%29.json'
content_hash: 'sha256:6db32ef26618bfcd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# prominentGlass()

<sub>Type Method</sub>

Creates a configuration for a button that has a prominent Liquid Glass style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static func prominentGlass() -> UIButton.Configuration
```

## Discussion

In tvOS, this button style applies a Liquid Glass effect regardless of whether the button has focus.

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
- [clearGlass()](<clearglass().md>) — Creates a configuration for a button that has a clear Liquid Glass style.
- [prominentClearGlass()](<prominentclearglass().md>) — Creates a configuration for a button that has a prominent, clear Liquid Glass style.
- [updated(for:)](<updated(for_).md>) — Returns a copy of the configuration, updated for the given button.
