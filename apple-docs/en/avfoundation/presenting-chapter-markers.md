---
title: Presenting chapter markers
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/presenting-chapter-markers
source_url: 'https://developer.apple.com/documentation/avfoundation/presenting-chapter-markers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/presenting-chapter-markers.json'
content_hash: 'sha256:e330f6a8ec433213'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media playback](media-playback.md)

# Presenting chapter markers

<sub>Article</sub>

Add chapter markers to enable users to quickly navigate your content.

## Overview

Chapter markers enable users to quickly navigate your content. [AVPlayerViewController](../avkit/avplayerviewcontroller.md) automatically presents a chapter-selection interface if it finds chapter markers in the currently played asset. You can also directly retrieve this data whenever you want to create your own custom chapter-selection interface.

### Retrieve the timed metadata

Chapter markers are a type of timed metadata that apply only to ranges of time within the asset’s timeline. You retrieve an asset’s chapter metadata using either the [- chapterMetadataGroupsBestMatchingPreferredLanguages:](<avasset/chaptermetadatagroups(bestmatchingpreferredlanguages_).md>) or [- chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](<avasset/chaptermetadatagroups(withtitlelocale_containingitemswithcommonkeys_).md>) methods. These methods become callable without blocking after you asynchronously load the value of the asset’s [availableChapterLocales](avasset/availablechapterlocales.md) key.

```swift
let asset = AVAsset(url: <# Asset URL #>)
let chapterLocalesKey = "availableChapterLocales"
 
asset.loadValuesAsynchronously(forKeys: [chapterLocalesKey]) {
    var error: NSError?
    let status = asset.statusOfValue(forKey: chapterLocalesKey, error: &error)
    if status == .loaded {
        let languages = Locale.preferredLanguages
        let chapterMetadata = asset.chapterMetadataGroups(bestMatchingPreferredLanguages: languages)
        // Process chapter metadata.
    }
    else {
        // Handle other status cases.
    }
}
```

### Convert timed metadata into chapter data

The value returned from the methods described above is an array of [AVTimedMetadataGroup](avtimedmetadatagroup.md) objects, each representing an individual chapter marker. An [AVTimedMetadataGroup](avtimedmetadatagroup.md) object contains a [CMTimeRange](../coremedia/cmtimerange.md), defining the time range to which its metadata applies, an array of [AVMetadataItem](avmetadataitem.md) objects representing the chapter’s title, and optionally, its thumbnail image. The following example shows how to convert the [AVTimedMetadataGroup](avtimedmetadatagroup.md) data into an array of custom model objects, called `Chapter`, to pass to the app’s view layer.

```swift
func convertTimedMetadataGroupsToChapters(groups: [AVTimedMetadataGroup]) -> [Chapter] {
    return groups.map { group in
        // Retrieve the title metadata items.
        let titleItems = AVMetadataItem.metadataItems(from: group.items,
                                                      filteredByIdentifier: .commonIdentifierTitle)

        // Retrieve the artwork metadata items.
        let artworkItems = AVMetadataItem.metadataItems(from: group.items,
                                                        filteredByIdentifier: .commonIdentifierArtwork)

        var title = "Default Title"
        var image = UIImage(named: "placeholder")!

        if let titleValue = titleItems.first?.stringValue {
            title = titleValue
        }

        if let imgData = artworkItems.first?.dataValue, let imageValue = UIImage(data: imgData) {
            image = imageValue
        }

        return Chapter(time: group.timeRange.start, title: title, image: image)
    }
}
```

With the relevant data converted, you can build a chapter-selection interface and use the time value of the chapter object to seek the current presentation using an [AVPlayer](avplayer.md) object’s [- seekToTime:](<avplayer/seek(to_)-87h2r.md>) method.

## See Also

### Timed metadata

- [AVMetadataGroup](avmetadatagroup.md) — A collection of metadata items associated with a timeline segment.
- [AVTimedMetadataGroup](avtimedmetadatagroup.md) — A collection of metadata items that are valid for use during a specific time range.
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md) — A mutable collection of metadata items that are valid for use during a specific time range.
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md) — A collection of metadata items that are valid for use within a specific date range.
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md) — A mutable collection of metadata items that are valid for use within a specific range of dates.
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md) — The abstract base for media data collectors.
- [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md) — An object used to capture the date range metadata defined for an HTTP Live Streaming asset.
