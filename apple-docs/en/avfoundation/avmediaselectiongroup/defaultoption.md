---
title: defaultOption
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectiongroup/defaultoption
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/defaultoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectiongroup/defaultoption.json'
content_hash: 'sha256:47abe69f275c40f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionGroup](../avmediaselectiongroup.md)

# defaultOption

<sub>Instance Property</sub>

The default option in the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var defaultOption: AVMediaSelectionOption? { get }
```

## Discussion

The default option is intended for use in the absence of a specific end-user selection or preference. Can be `nil`, indicating that without a specific end-user selection or preference, no option in the group is intended to be selected.

## See Also

### Accessing media selection options

- [options](options.md) — A collection of mutually exclusive media selection options
- [- mediaSelectionOptionWithPropertyList:](<mediaselectionoption(withpropertylist_).md>) — Returns the media selection options that match the given property list.
