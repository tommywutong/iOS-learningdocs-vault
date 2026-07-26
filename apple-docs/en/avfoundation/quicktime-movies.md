---
title: QuickTime movies
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/quicktime-movies
source_url: 'https://developer.apple.com/documentation/avfoundation/quicktime-movies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/quicktime-movies.json'
content_hash: 'sha256:ad42a4263d34e7fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# QuickTime movies

<sub>API Collection</sub>

Access the contents of a QuickTime movie file, and perform sample-level edits of its media tracks.

## Topics

### Movies

- [AVMovie](avmovie.md) — An object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.
- [AVMovieTrack](avmovietrack.md) — A track in a movie that conforms to the QuickTime or ISO base media file format.

### Mutable movies

- [AVMutableMovie](avmutablemovie.md) — A mutable object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.
- [AVMutableMovieTrack](avmutablemovietrack.md) — A mutable track that conforms to the QuickTime or ISO base media file format.

### Fragmented movies

- [AVFragmentedMovie](avfragmentedmovie.md) — An object that represents a fragmented movie file.
- [AVFragmentedMovieTrack](avfragmentedmovietrack.md) — An object that represents a track in a fragmented movie.
- [AVFragmentedMovieMinder](avfragmentedmovieminder.md) — An object that checks whether a fragmented movie appends additional movie fragments.
- [AVFragmentMinding](avfragmentminding.md) — A protocol that defines whether an asset supports fragment minding.

### Sample cursors

- [AVSampleCursor](avsamplecursor.md) — An object that provides information about the media sample at the cursor’s current position.
- [AVSampleCursorSyncInfo](avsamplecursorsyncinfo.md) — A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md) — A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [AVSampleCursorAudioDependencyInfo](avsamplecursoraudiodependencyinfo.md) — A structure that describes the independent decodability of audio samples.
- [AVSampleCursorStorageRange](avsamplecursorstoragerange.md) — A structure that indicates the offset and length of storage for a media sample or its chunk.
- [AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md) — A value that provides information about a chunk of media samples.

### Media data storage

- [AVMediaDataStorage](avmediadatastorage.md) — An object that represents the media sample data storage file.

## See Also

### Editing

- [Composite assets](composite-assets.md) — Combine tracks and segments of tracks from multiple assets into a composite asset that you can play or process.
- [Video effects](video-effects.md) — Define standard video transition effects, synchronize layer animations with media timing, and create custom video compositors.
- [Audio mixing](audio-mixing.md) — Define how to mix the audio levels from multiple audio tracks over an asset’s duration.
