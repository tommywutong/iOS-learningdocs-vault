---
title: allowsEmptySelection
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectiongroup/allowsemptyselection
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/allowsemptyselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectiongroup/allowsemptyselection.json'
content_hash: 'sha256:1c4fa6779dada0da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionGroup](../avmediaselectiongroup.md)

# allowsEmptySelection

<sub>Instance Property</sub>

A Boolean value that indicates whether it’s possible to present none of the options in the group when an associated player item is played.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsEmptySelection: Bool { get }
```

## Discussion

If the value of this property is [true](../../swift/true.md), you can deselect all of the available media options in the group by passing `nil` as the specified [AVMediaSelectionOption](../avmediaselectionoption.md) object to [- selectMediaOption:inMediaSelectionGroup:](<../avplayeritem/select(__in_).md>).
