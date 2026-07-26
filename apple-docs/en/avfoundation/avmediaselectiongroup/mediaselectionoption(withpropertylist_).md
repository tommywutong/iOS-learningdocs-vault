---
title: 'mediaSelectionOption(withPropertyList:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediaselectiongroup/mediaselectionoption(withpropertylist:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/mediaselectionoption(withpropertylist:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectiongroup/mediaselectionoption%28withpropertylist%3A%29.json'
content_hash: 'sha256:a75b8114e1788441'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionGroup](../avmediaselectiongroup.md)

# mediaSelectionOption(withPropertyList:)

<sub>Instance Method</sub>

Returns the media selection options that match the given property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mediaSelectionOption(withPropertyList plist: Any) -> AVMediaSelectionOption?
```

## Parameters

- `plist` — A property list previously obtained from an option in the group using [- propertyList](<../avmediaselectionoption/propertylist().md>) (`AVMediaSelectionOption`).

## Return Value

An [AVMediaSelectionOption](../avmediaselectionoption.md) object containing the properites passed by `plist`. Returns `nil` when no match is found.

## See Also

### Accessing media selection options

- [options](options.md) — A collection of mutually exclusive media selection options
- [defaultOption](defaultoption.md) — The default option in the group.
