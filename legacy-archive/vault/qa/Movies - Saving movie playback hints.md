---
title: Movies - Saving movie playback hints
apple_id: DTS10003382
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2004-09-14'
source_url: https://developer.apple.com/library/archive/qa/qa1366/_index.html
archived_at: '2026-07-18T02:30:26.441341Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1366

# Movies - Saving movie playback hints

## Q:  I'd like my application to offer the user an option to turn on/off the High Quality preference for the Video Track and save the preference so QuickTime player will respect it when these movies are later opened. Using `SetMoviePlayHints` doesn't seem to do this.

A: There's four APIs you'll need to use to do this. They are `SetMediaPlayHints`, `GetTrackLoadSettings`, `SetTrackLoadSettings` and `UpdateMovieInStorage` (or `UpdateMovieResource` on Windows).

__Listing 1__  Turning High Quality on and off.

```
// toggle HQ on/off - remember to update the Movie storage to save the setting
void ToggleHighQualityOnOff(Track inTrack)
{
    long trackHints;
    long ignore1, ignore2, ignore3;

    GetTrackLoadSettings(inTrack, &ignore1, &ignore2, &ignore3, &trackHints);
    trackHints ^= hintsHighQuality; // on/off and so on or off

    SetTrackLoadSettings(inTrack, ignore1, ignore2, ignore3, trackHints);
    SetMediaPlayHints(GetTrackMedia(inTrack), trackHints, hintsHighQuality);
}
```

The above listing will toggle the High Quality hint for playback and modify the load settings but will not save the setting. To actually save the setting, you'll need to update the Movie by calling `UpdateMovieInStorage` or `UpdateMovieResource` sometime after calling this function as is appropriate for your application.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-09-14 | New document that explains how to save and load media play hints from Movie files. |

