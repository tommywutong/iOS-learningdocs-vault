---
title: hasProtectedContent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/hasprotectedcontent
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/hasprotectedcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/hasprotectedcontent.json'
content_hash: 'sha256:a5e0d4744cb49745'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# hasProtectedContent

<sub>Type Property</sub>

A Boolean value that indicates whether the asset contains protected content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var hasProtectedContent: AVAsyncProperty<Root, Bool> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

Assets that contain protected content may not be playable without successful authorization, even if the value of its [playable](../avasset/isplayable.md) property is [true](../../swift/true.md).
