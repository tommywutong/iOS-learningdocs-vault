---
title: selectedExternalSubtitleOptionLanguage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+（9.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayeritem/selectedexternalsubtitleoptionlanguage
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/selectedexternalsubtitleoptionlanguage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/selectedexternalsubtitleoptionlanguage.json'
content_hash: 'sha256:a7c7f78c90b73d7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# selectedExternalSubtitleOptionLanguage

<sub>Instance Property</sub>

<sub>tvOS</sub>

```objc
@property (nonatomic, copy) NSString * selectedExternalSubtitleOptionLanguage;
```

## Discussion

Specifies BCP 47 language code of the external subtitle option language marked in the user interface.

If anything other than an external subtitle option is selected (including “Off”), then this property should be set to an empty string. If the value is not an empty string, it should be an element of the externalSubtitleOptionLanguages array.

## See Also

### Setting subtitle options

- [externalSubtitleOptionLanguages](externalsubtitleoptionlanguages.md) _(deprecated)_
