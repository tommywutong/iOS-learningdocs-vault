---
title: borderedButtonConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/borderedbuttonconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/borderedbuttonconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/borderedbuttonconfiguration.json'
content_hash: 'sha256:93efaf9db25661f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# borderedButtonConfiguration

<sub>Type Method</sub>

Creates a configuration for a button that has a bordered style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) borderedButtonConfiguration;
```

## Return Value

A new configuration object.

## Discussion

This style provides an alternative name for the [grayButtonConfiguration](graybuttonconfiguration.md) style.

## See Also

### Creating configurations

- [plainButtonConfiguration](plainbuttonconfiguration.md) — Creates a configuration for a button with a transparent background.
- [grayButtonConfiguration](graybuttonconfiguration.md) — Creates a configuration for a button with a gray background.
- [tintedButtonConfiguration](tintedbuttonconfiguration.md) — Creates a configuration for a button with a tinted background color.
- [filledButtonConfiguration](filledbuttonconfiguration.md) — Creates a configuration for a button with a background filled with the button’s tint color.
- [borderlessButtonConfiguration](borderlessbuttonconfiguration.md) — Creates a configuration for a button that has a borderless style.
- [borderedTintedButtonConfiguration](borderedtintedbuttonconfiguration.md) — Creates a configuration for a button that has a tinted, bordered style.
- [borderedProminentButtonConfiguration](borderedprominentbuttonconfiguration.md) — Creates a configuration for a button that has a prominent, bordered style.
- [glassButtonConfiguration](glassbuttonconfiguration.md) — Creates a configuration for a button that has a Liquid Glass style.
- [prominentGlassButtonConfiguration](prominentglassbuttonconfiguration.md) — Creates a configuration for a button that has a prominent Liquid Glass style.
- [clearGlassButtonConfiguration](clearglassbuttonconfiguration.md) — Creates a configuration for a button that has a clear Liquid Glass style.
- [prominentClearGlassButtonConfiguration](prominentclearglassbuttonconfiguration.md) — Creates a configuration for a button that has a prominent, clear Liquid Glass style.
- [updatedConfigurationForButton:](updatedconfigurationforbutton_.md) — Returns a copy of the configuration, updated for the given button.
