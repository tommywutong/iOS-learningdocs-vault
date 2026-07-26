---
title: 'textContentManager(_:shouldEnumerate:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentmanagerdelegate/textcontentmanager(_:shouldenumerate:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanagerdelegate/textcontentmanager(_:shouldenumerate:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanagerdelegate/textcontentmanager%28_%3Ashouldenumerate%3Aoptions%3A%29.json'
content_hash: 'sha256:6e2dddf31a8c223d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManagerDelegate](../nstextcontentmanagerdelegate.md)

# textContentManager(_:shouldEnumerate:options:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the framework should skip this text element in the enumeration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textContentManager(_ textContentManager: NSTextContentManager, shouldEnumerate textElement: NSTextElement, options: NSTextContentManager.EnumerationOptions = []) -> Bool
```

## Parameters

- `textContentManager` — The content manager.

- `textElement` — The [NSTextElement](../nstextelement.md) to evaluate.

- `options` — One of the available `NSTextElementProviderEnumerationOptions` options.

## Return Value

A Boolean value that informs the framework to skip this `textElement`  in the enumeration. Returning `false` indicates `textElement` to be skipped; otherwise the element is included in the enumeration.
