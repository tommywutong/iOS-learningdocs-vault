---
title: AVMovieExporter
apple_id: DTS40011364
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2011-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/AVMovieExporter/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:00:25.629031Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMovieExporter](AVMovieExporter.md)


[Next](AVMovieExporter-AssetItem.h.md)[Previous](AVMovieExporter.md)

# ReadMe.txt

```
AVMovieExporter

Description

This universal sample application reads movie files from the asset and media library then 
exports them to a new media file with user defined settings. The user can adjust the exported file 
in the following ways:
    - Export presets can be chosen which influence the size and quality of the output.  
    - The file type can be changed.
    - Tracks and existing metadata can be inspected.
    - Metadata can be inserted or deleted.

Files of Interest

AVMovieExporter/: The core AVMovieExporter code.
AVMovieExporter/main.m: Creates the app object and the application delegate and sets up the event cycle.
AVMovieExporter/Sydney-iPhone.*: Samples video files that can be used in the project.
AVMovieExporter/VideoLibrary.*: Code that loads movie files from the app bundle, asset library, and media library.
AVMovieExporter/AssetItem.*: Code that loads an AVAsset, edits metadata, and performs the export.
AVMovieExporter/CommonMetadata.*: Code that uses AVMutableMetadataItem.

Notes of Interest

The sample starts by displaying all of the video content in the app bundle, asset Library, and media 
library. Tapping on one of the movie files in the table view shows detailed track and metadata 
information about the movie, as well as show export information. Tapping on one of the tracks or metadata 
items will show even more detailed information about that item. Tapping "Edit" while inspecting a movie 
will allow metadata to be deleted. Metadata in the file can be replaced with predefined metadata keys.

Limitations

The sample code only shows a small portion of the information one can obtain about tracks, and metadata. 
The settings do not allow a time range on the export to be set.

Apple Media APIs used

AssetsLibrary.framework
ALAssetsFilter
ALAssetsLibrary
ALAssetsLibraryChangedNotification

MediaPlayer.framework
MPMediaItemPropertyMediaType
MPMediaItemPropertyAssetURL
MPMediaPropertyPredicate
MPMediaQuery

AVFoundation.framework
AVAssetExportSession
AVMutableMetadataItem
AVURLAsset
```

[Next](AVMovieExporter-AssetItem.h.md)[Previous](AVMovieExporter.md)

