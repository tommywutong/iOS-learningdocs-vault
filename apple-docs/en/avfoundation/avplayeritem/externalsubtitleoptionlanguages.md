---
title: externalSubtitleOptionLanguages
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+（9.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayeritem/externalsubtitleoptionlanguages
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/externalsubtitleoptionlanguages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/externalsubtitleoptionlanguages.json'
content_hash: 'sha256:9167afa7b4d589d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# externalSubtitleOptionLanguages

<sub>Instance Property</sub>

<sub>tvOS</sub>

```objc
@property (nonatomic, copy) NSArray<NSString *> * externalSubtitleOptionLanguages;
```

## Discussion

An array of BCP 47 language codes that supplements the list of subtitle options that will be presented to the user.

This list is strictly for non-standard, application-rendered subtitles, that cannot be handled by AVFoundation. Most clients should not need to set this property. The application should implement the playerViewController:didSelectExternalSubtitleOptionLanguage: method of its AVPlayerViewControllerDelegate to be notified when one of these languages has been chosen by the user.

## See Also

### Setting subtitle options

- [selectedExternalSubtitleOptionLanguage](selectedexternalsubtitleoptionlanguage.md) _(deprecated)_
