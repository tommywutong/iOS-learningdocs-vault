---
title: externalContentProtectionStatus
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkey/externalcontentprotectionstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkey/externalcontentprotectionstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkey/externalcontentprotectionstatus.json'
content_hash: 'sha256:d83979faa760fe79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKey](../avcontentkey.md)

# externalContentProtectionStatus

<sub>Instance Property</sub>

The external protection status for the content key based on all attached displays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var externalContentProtectionStatus: AVExternalContentProtectionStatus { get }
```

## Discussion

This property isn’t key-value observable. Instead, use the [- contentKeySession:externalProtectionStatusDidChangeForContentKey:](<../avcontentkeysessiondelegate/contentkeysession(__externalprotectionstatusdidchangefor_).md>) delegate method to monitor changes to this value.

## See Also

### Inspecting protection status

- [- revoke](<revoke().md>)
