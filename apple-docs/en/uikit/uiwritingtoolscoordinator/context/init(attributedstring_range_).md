---
title: 'init(attributedString:range:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/context/init(attributedstring:range:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/context/init(attributedstring:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/context/init%28attributedstring%3Arange%3A%29.json'
content_hash: 'sha256:b74b431adc1aa8fd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Context](../context.md)

# init(attributedString:range:)

<sub>Initializer</sub>

Creates a context object with the specified attributed string and range information.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(attributedString: NSAttributedString, range: NSRange)
```

## Parameters

- `attributedString` — A string that contains some or all of the content from your view’s text storage. This initializer makes a copy of the string you provide, so you can discard the original when you’re done.

- `range` — The portion of `attributedString` you want Writing Tools to evaluate. If you want Writing Tools to evaluate the entire string you provided, specify a range with a location of `0` and a length equal to your string’s length. If you want Writing Tools to evaluate only part of the string, provide the appropriate range in this parameter. Writing Tools suggests changes only to the range of text you specify, but it can consider text outside that range during the evaluation process.

## Discussion

When Writing Tools asks for your view’s current selection, it’s best to create a string that includes text before and after that selection. During the evaluation process, Writing Tools can use the additional text you provided to improve the results it delivers. If you do provide additional text, set the `range` parameter to the portion of `attributedString` with the current selection. Don’t use the `range` parameter to specify the location of the text in your view’s text storage.
