---
title: textFormattingConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/textformattingconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/textformattingconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/textformattingconfiguration.json'
content_hash: 'sha256:8119d311255a42f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# textFormattingConfiguration

<sub>Instance Property</sub>

For text views that have flag `allowsEditingTextAttributes` set, this configuration will be used for `UITextFormattingViewController` when its presentation is requested.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var textFormattingConfiguration: UITextFormattingViewController.Configuration? { get set }
```

## Discussion

It has a non-nil default value.
