---
title: isOutputObscuredDueToInsufficientExternalProtection
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/isoutputobscuredduetoinsufficientexternalprotection
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/isoutputobscuredduetoinsufficientexternalprotection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/isoutputobscuredduetoinsufficientexternalprotection.json'
content_hash: 'sha256:fc9e0f4c631c3f53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# isOutputObscuredDueToInsufficientExternalProtection

<sub>Instance Property</sub>

A Boolean value that indicates whether output is being obscured because of insufficient external protection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated var isOutputObscuredDueToInsufficientExternalProtection: Bool { get }
```

## Discussion

Items that incorporate copy protection or other forms of security might have their visual content obscured by the player object if the current device configuration does not meet the requirements for protecting the item. This property reports whether the player is currently obscuring the item. If the current item does not require external protection or if the device configuration sufficiently protects the item, the value of this property is set to [false](../../swift/false.md).

You can use this property to determine whether to change your app’s user interface to reflect the change in visibility. You can observe changes to the value of this property using key-value observing.
