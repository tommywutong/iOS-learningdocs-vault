---
title: 'updatedConfigurationForButton:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibuttonconfiguration/updatedconfigurationforbutton:'
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/updatedconfigurationforbutton:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/updatedconfigurationforbutton%3A.json'
content_hash: 'sha256:be38a1265c7d3d3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# updatedConfigurationForButton:

<sub>Instance Method</sub>

Returns a copy of the configuration, updated for the given button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) updatedConfigurationForButton:(UIButton *) button;
```

## Parameters

- `button` — A button to use as a basis for the configuration.

## Return Value

An updated configuration. This method preserves custom values set on the configuration, and updates default values based on the button state.

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
- [prominentGlassButtonConfiguration](prominentglassbuttonconfiguration.md) — Creates a configuration for a button that has a prominent Liquid Glass style.
- [clearGlassButtonConfiguration](clearglassbuttonconfiguration.md) — Creates a configuration for a button that has a clear Liquid Glass style.
- [prominentClearGlassButtonConfiguration](prominentclearglassbuttonconfiguration.md) — Creates a configuration for a button that has a prominent, clear Liquid Glass style.
