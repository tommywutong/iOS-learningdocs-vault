---
title: options
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectiongroup/options
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectiongroup/options.json'
content_hash: 'sha256:32b57efe86437c78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionGroup](../avmediaselectiongroup.md)

# options

<sub>Instance Property</sub>

A collection of mutually exclusive media selection options

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var options: [AVMediaSelectionOption] { get }
```

## Discussion

The value of the property is an array of [AVMediaSelectionOption](../avmediaselectionoption.md) objects.

## See Also

### Accessing media selection options

- [- mediaSelectionOptionWithPropertyList:](<mediaselectionoption(withpropertylist_).md>) — Returns the media selection options that match the given property list.
- [defaultOption](defaultoption.md) — The default option in the group.
