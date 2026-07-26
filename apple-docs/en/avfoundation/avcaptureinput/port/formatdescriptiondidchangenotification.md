---
title: formatDescriptionDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification.json'
content_hash: 'sha256:00bc15aca12b58c4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureInput](../../avcaptureinput.md) · [Port](../port.md)

# formatDescriptionDidChangeNotification

<sub>Type Property</sub>

A notification the system posts when the capture input port’s format description changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class let formatDescriptionDidChangeNotification: NSNotification.Name
```

## Discussion

The notification’s [object](../../../foundation/notification/object.md) property contains the [Port](../port.md) object whose format changed.
