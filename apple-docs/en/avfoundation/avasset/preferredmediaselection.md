---
title: preferredMediaSelection
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（16.0 起废弃）, iPadOS 9.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 2.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/preferredmediaselection
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/preferredmediaselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/preferredmediaselection.json'
content_hash: 'sha256:3164e1db5cfba461'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# preferredMediaSelection

<sub>Instance Property</sub>

The default media selections for this asset’s media selection groups.

> [!warning] Deprecated
> Load the value of [preferredMediaSelection](../avpartialasyncproperty/preferredmediaselection.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var preferredMediaSelection: AVMediaSelection { get }
```

## Discussion

Provides an instance of [AVMediaSelection](../avmediaselection.md) with the default selections for each of the assets media selection groups.
