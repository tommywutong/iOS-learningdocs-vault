---
title: audioOptions
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacemediaselectioncontrollable/audiooptions
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemediaselectioncontrollable/audiooptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemediaselectioncontrollable/audiooptions.json'
content_hash: 'sha256:d12b37cfb26eae31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceMediaSelectionControllable](../avinterfacemediaselectioncontrollable.md)

# audioOptions

<sub>Instance Property</sub>

Array of available audio track options for selection. This includes all audio streams provided by the media source such as different languages, audio descriptions, director’s commentary, and alternative audio mixes. Options are ordered by preference with the primary language or default audio track typically appearing first. May be empty for content without selectable audio options. Must be key-value observable.

<sub>tvOS, visionOS</sub>

```objc
@property (nonatomic, copy, readonly) NSArray<AVInterfaceMediaSelectionOptionSource *> * audioOptions;
```

## See Also

### Inspecting media selection options

- [currentAudioOption](currentaudiooption.md) — Currently selected audio track for playback. Setting this property changes the active audio stream. This includes language variants, audio descriptions, director’s commentary, and other audio content. Must be key-value observable.
- [legibleOptions](legibleoptions.md) — Array of available subtitle and caption track options for selection. This includes text overlays in different languages, closed captions for accessibility, forced narrative subtitles, and sign language interpretation tracks. May be empty for content without text tracks. Must be key-value observable.
- [currentLegibleOption](currentlegibleoption.md) — Currently selected subtitle or caption track. Setting this property controls text overlay presentation. This includes subtitles in different languages, closed captions, and forced narrative text. Set to nil to disable text display. Must be key-value observable.
