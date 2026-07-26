---
title: 'propertyList(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avtextstylerule/propertylist(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avtextstylerule/propertylist(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtextstylerule/propertylist%28for%3A%29.json'
content_hash: 'sha256:8ee7d9e84fc93bbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTextStyleRule](../avtextstylerule.md)

# propertyList(for:)

<sub>Type Method</sub>

Converts one or more text style rules into a serializable property list object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func propertyList(for textStyleRules: [AVTextStyleRule]) -> Any
```

## Parameters

- `textStyleRules` — An array of `AVTextStyleRule` objects to write to the property list.

## Return Value

A property-list object that you can pass to the [PropertyListSerialization](../../foundation/propertylistserialization.md) serialization routines.

## Discussion

The property-list object returned by this method can be written to disk and stored persistently.
