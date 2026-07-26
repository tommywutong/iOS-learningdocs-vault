---
title: 'init(contentTimeForTransition:title:previewImage:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcontentproposal/init(contenttimefortransition:title:previewimage:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposal/init(contenttimefortransition:title:previewimage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposal/init%28contenttimefortransition%3Atitle%3Apreviewimage%3A%29.json'
content_hash: 'sha256:8c13d01e77c1a30f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposal](../avcontentproposal.md)

# init(contentTimeForTransition:title:previewImage:)

<sub>Initializer</sub>

Creates a new content proposal with the specified transition time, title, and preview image.

<sub>tvOS</sub>

```swift
init(contentTimeForTransition: CMTime, title: String, previewImage: UIImage?)
```

## Parameters

- `contentTimeForTransition` — A [CMTime](../../coremedia/cmtime.md) value at which to present the content propsal within the media’s timeline.

- `title` — The title of the proposed content.

- `previewImage` — The preview image for the proposed item.

## Return Value

A new instance of [AVContentProposal](../avcontentproposal.md).

## Discussion

You specify the content proposal’s presentation time within the asset’s timeline. For instance, if you wanted to present the next content proposal 15 seconds before the end of the currently playing asset, you could create the next content proposal as follows:

```swift
let episode1Asset = // Currently presented asset for Episode 1
// Subtract 15 seconds from the current episode's duration
let time = episode1Asset.duration - CMTime(value: 15, timescale: 1)
let title = "My Series: Episode 2"
let image = UIImage(named: "myseries_ep2")
let proposal = AVContentProposal(contentTimeForTransition: time,
                                 title: title,
                                 previewImage: image)
// Set the proposal as the nextContentProposal of the current player item
currentPlayerItem.nextContentProposal = proposal
```
