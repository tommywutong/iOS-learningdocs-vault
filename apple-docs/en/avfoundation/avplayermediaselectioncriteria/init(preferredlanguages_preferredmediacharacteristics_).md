---
title: 'init(preferredLanguages:preferredMediaCharacteristics:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayermediaselectioncriteria/init(preferredlanguages:preferredmediacharacteristics:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/init(preferredlanguages:preferredmediacharacteristics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayermediaselectioncriteria/init%28preferredlanguages%3Apreferredmediacharacteristics%3A%29.json'
content_hash: 'sha256:25714dab2196abca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerMediaSelectionCriteria](../avplayermediaselectioncriteria.md)

# init(preferredLanguages:preferredMediaCharacteristics:)

<sub>Initializer</sub>

Creates media selection criteria with the preferred languages and media characteristics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(preferredLanguages: [String]?, preferredMediaCharacteristics: [AVMediaCharacteristic]?)
```

## Parameters

- `preferredLanguages` — An array of language identifier strings, in order of preference. This value may be `nil`.

- `preferredMediaCharacteristics` — An array of media characteristics, in order of preference. This value may be `nil`.

## See Also

### Creating media selection criteria

- [- initWithPrincipalMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:](<init(principalmediacharacteristics_preferredlanguages_preferredmediacharacteristics_).md>) — Creates media selection criteria with the principal media characteristics, and preferred languages and media characteristics.
