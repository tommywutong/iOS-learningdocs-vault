---
title: extensionName
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaextensionproperties/extensionname
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaextensionproperties/extensionname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaextensionproperties/extensionname.json'
content_hash: 'sha256:df964e0c0f232a57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaExtensionProperties](../avmediaextensionproperties.md)

# extensionName

<sub>Instance Property</sub>

The name of the Media Extension.

<sub>macOS</sub>

```swift
var extensionName: String { get }
```

## Discussion

This value corresponds to the extension’s [CFBundleDisplayName](../../bundleresources/information-property-list/cfbundledisplayname.md).

## See Also

### Inspecting the extension

- [containingBundleName](containingbundlename.md) — The name of the containing app bundle.
- [extensionIdentifier](extensionidentifier.md)
- [extensionURL](extensionurl.md) — The file URL of the Media Extension bundle.
- [containingBundleURL](containingbundleurl.md) — The file URL of the host application for the Media Extension.
