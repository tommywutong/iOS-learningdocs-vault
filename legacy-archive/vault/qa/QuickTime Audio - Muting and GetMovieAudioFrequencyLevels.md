---
title: QuickTime Audio - Muting and GetMovieAudioFrequencyLevels
apple_id: DTS10004473
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2007-09-28'
source_url: https://developer.apple.com/library/archive/qa/qa1556/_index.html
archived_at: '2026-07-18T02:32:18.148074Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1556

# QuickTime Audio - Muting and GetMovieAudioFrequencyLevels

## Q:  QuickTime 7.2 seems to have changed the way `GetMovieAudioFrequencyLevels` behaves. Muting and Volume changes now attenuate the returned frequency levels. Was this intended?

A: Yes, this was an intentional change. As of QuickTime 7.2 any Movie Volume, Balance or Muting in the audio chain is applied __before__ the spectral analyzer that provides data for the `GetMovieAudioFrequencyLevels` API.

This change was made in order to more accurately reflect the actual mixed Movie output when returning the requested frequency levels.

If your application has a requirement to see frequency metering while a Movie is muted, the legacy Media Handler `MediaSetSoundEqualizerBands` / `MediaGetSoundEqualizerBandLevels` API pair may be used. Additionally, if simple volume levels are sufficient (as opposed to a frequency spectrum), you can use the newer `SetTrackAudioVolumeMeteringEnabled` / `GetTrackAudioVolumeLevels` pair of APIs introduced in QuickTime 7.0.

- [Technical Q&A QA1459, 'QuickTime Audio - Easy Frequency Level Metering with MovieAudio APIs'](https://developer.apple.com/qa/qa2005/qa1459.html)
- [Sample Code 'SillyFrequencyLevels'](https://developer.apple.com/samplecode/SillyFrequencyLevels/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-09-28 | New document that discusses the change made to the GetMovieAudioFrequencyLevels API with QuickTime 7.2. |

