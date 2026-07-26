---
title: 'textContentManager(_:textElementAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentmanagerdelegate/textcontentmanager(_:textelementat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanagerdelegate/textcontentmanager(_:textelementat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanagerdelegate/textcontentmanager%28_%3Atextelementat%3A%29.json'
content_hash: 'sha256:3b973a4d31e20792'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManagerDelegate](../nstextcontentmanagerdelegate.md)

# textContentManager(_:textElementAt:)

<sub>Instance Method</sub>

The method the framework calls to return the text element at a specific location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textContentManager(_ textContentManager: NSTextContentManager, textElementAt location: any NSTextLocation) -> NSTextElement?
```

## Parameters

- `textContentManager` — The content manager.

- `location` — The location of the element.

## Return Value

An [NSTextElement](../nstextelement.md).

## Discussion

When non-`nil`, `textContentManager` uses the text element you specify instead of creating one based on its standard mapping logic.
