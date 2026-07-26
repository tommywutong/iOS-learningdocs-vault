---
title: prominentGlassButtonConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/prominentglassbuttonconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/prominentglassbuttonconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/prominentglassbuttonconfiguration.json'
content_hash: 'sha256:5b189c9532a83184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# prominentGlassButtonConfiguration

<sub>Type Method</sub>

Creates a configuration for a button that has a prominent Liquid Glass style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) prominentGlassButtonConfiguration;
```

## Discussion

In tvOS, this button style applies a Liquid Glass effect regardless of whether the button has focus.

## See Also

### Creating configurations

- [plainButtonConfiguration](plainbuttonconfiguration.md) — Creates a configuration for a button with a transparent background.
- [grayButtonConfiguration](graybuttonconfiguration.md) — Creates a configuration for a button with a gray background.
- [tintedButtonConfiguration](tintedbuttonconfiguration.md) — Creates a configuration for a button with a tinted background color.
- [filledButtonConfiguration](filledbuttonconfiguration.md) — Creates a configuration for a button with a background filled with the button’s tint color.
- [borderlessButtonConfiguration](borderlessbuttonconfiguration.md) — Creates a configuration for a button that has a borderless style.
- [borderedButtonConfiguration](borderedbuttonconfiguration.md) — Creates a configuration for a button that has a bordered style.
- [borderedTintedButtonConfiguration](borderedtintedbuttonconfiguration.md) — Creates a configuration for a button that has a tinted, bordered style.
- [borderedProminentButtonConfiguration](borderedprominentbuttonconfiguration.md) — Creates a configuration for a button that has a prominent, bordered style.
- [glassButtonConfiguration](glassbuttonconfiguration.md) — Creates a configuration for a button that has a Liquid Glass style.
- [clearGlassButtonConfiguration](clearglassbuttonconfiguration.md) — Creates a configuration for a button that has a clear Liquid Glass style.
- [prominentClearGlassButtonConfiguration](prominentclearglassbuttonconfiguration.md) — Creates a configuration for a button that has a prominent, clear Liquid Glass style.
- [updatedConfigurationForButton:](updatedconfigurationforbutton_.md) — Returns a copy of the configuration, updated for the given button.
