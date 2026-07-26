---
title: automaticallyUpdateForSelection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/automaticallyupdateforselection
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/automaticallyupdateforselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/automaticallyupdateforselection.json'
content_hash: 'sha256:cdb33ca15d750bed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# automaticallyUpdateForSelection

<sub>Instance Property</sub>

A Boolean value that determines whether the style automatically updates when the button is in a selected state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) BOOL automaticallyUpdateForSelection;
```

## Discussion

The default value is [true](../../swift/true.md) for the [plainButtonConfiguration](plainbuttonconfiguration.md), [grayButtonConfiguration](graybuttonconfiguration.md), and [tintedButtonConfiguration](tintedbuttonconfiguration.md) configurations. Set this value to [false](../../swift/false.md) to customize the selection behavior.
