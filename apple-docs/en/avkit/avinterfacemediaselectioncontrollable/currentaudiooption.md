---
title: currentAudioOption
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacemediaselectioncontrollable/currentaudiooption
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemediaselectioncontrollable/currentaudiooption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemediaselectioncontrollable/currentaudiooption.json'
content_hash: 'sha256:2661bca01202af50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceMediaSelectionControllable](../avinterfacemediaselectioncontrollable.md)

# currentAudioOption

<sub>Instance Property</sub>

Currently selected audio track for playback. Setting this property changes the active audio stream. This includes language variants, audio descriptions, director’s commentary, and other audio content. Must be key-value observable.

<sub>tvOS, visionOS</sub>

```objc
@property (nonatomic, strong, readwrite, nullable) AVInterfaceMediaSelectionOptionSource * currentAudioOption;
```

## See Also

### Inspecting media selection options

- [audioOptions](audiooptions.md) — Array of available audio track options for selection. This includes all audio streams provided by the media source such as different languages, audio descriptions, director’s commentary, and alternative audio mixes. Options are ordered by preference with the primary language or default audio track typically appearing first. May be empty for content without selectable audio options. Must be key-value observable.
- [legibleOptions](legibleoptions.md) — Array of available subtitle and caption track options for selection. This includes text overlays in different languages, closed captions for accessibility, forced narrative subtitles, and sign language interpretation tracks. May be empty for content without text tracks. Must be key-value observable.
- [currentLegibleOption](currentlegibleoption.md) — Currently selected subtitle or caption track. Setting this property controls text overlay presentation. This includes subtitles in different languages, closed captions, and forced narrative text. Set to nil to disable text display. Must be key-value observable.
