---
title: iTunesController
apple_id: DTS10003879
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-02-23'
source_url: https://developer.apple.com/library/archive/samplecode/iTunesController/Listings/GetiTunesInfo_applescript.html
archived_at: '2026-07-18T03:29:45.848208Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iTunesController](iTunesController.md)


[Next](Document%20Revision%20History.md)[Previous](main.c.md)

# GetiTunesInfo.applescript

```
-- GetiTunesInfo.applescript

set savedTextItemDelimiters to AppleScript's text item delimiters
set AppleScript's text item delimiters to {"**"}

tell application "iTunes"
    set playerState to player state
    if playerState is playing then
        set theStreamTitle to current stream title
        set theTrack to current track
        set theTrackTitle to name of theTrack
        set theTrackArtist to artist of theTrack
        set theTrackAlbum to album of theTrack
        set theInfo to {playerState, theStreamTitle, theTrackTitle, theTrackArtist, theTrackAlbum} as string
    else
        set the info to playerState
    end if
end tell
```

[Next](Document%20Revision%20History.md)[Previous](main.c.md)

