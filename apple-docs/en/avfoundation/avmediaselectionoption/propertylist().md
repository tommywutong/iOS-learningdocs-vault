---
title: propertyList()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption/propertylist()
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/propertylist()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/propertylist%28%29.json'
content_hash: 'sha256:31f9206d94ecda4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# propertyList()

<sub>Instance Method</sub>

Returns a serializable property list that’s sufficient to identify the option within its group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func propertyList() -> Any
```

## Return Value

A serializable property list that you can use to obtain an instance of [AVMediaSelectionOption](../avmediaselectionoption.md) representing the same option as the receiver using [- mediaSelectionOptionWithPropertyList:](<../avmediaselectiongroup/mediaselectionoption(withpropertylist_).md>).

## Discussion

You can serialize the returned property list using [PropertyListSerialization](../../foundation/propertylistserialization.md).
