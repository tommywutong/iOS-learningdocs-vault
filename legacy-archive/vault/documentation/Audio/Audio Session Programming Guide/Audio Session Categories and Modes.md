---
title: Audio Session Programming Guide
apple_id: TP40007875
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/AudioSessionCategoriesandModes/AudioSessionCategoriesandModes.html
archived_at: '2026-07-15T05:20:46.210375Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Session Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Audio%20Guidelines%20By%20App%20Type.md)

# Audio Session Categories and Modes

You specify an audio session category to express how you intend to use audio in your app. Table B-1 provides details about each of the available categories. For an explanation of how categories work, see [Configuring an Audio Session](Configuring%20an%20Audio%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzvfvbuqmznknltc).

__Table B-1__  Audio Session category behavior

| Category | Silenced by the Ring/Silent switch and by screen locking see note | Interrupts nonmixable app’s audio | Allows audio input (recording) and output (playback) |
| `AVAudioSessionCategoryAmbient` | Yes | No | Output only |
| `AVAudioSessionCategorySoloAmbient` (Default) | Yes | Yes | Output only |
| `AVAudioSessionCategoryPlayback` | No | Yes by default; no by using override switch | Output only |
| `AVAudioSessionCategoryRecord` | No (recording continues with screen locked) | Yes | Input only |
| `AVAudioSessionCategoryPlayAndRecord` | No | Yes by default; no by using override switch | Input and output |
| `AVAudioSessionCategoryMultiRoute` | No | Yes | Input and output |

Table B-2 provides a list of modes and the categories each mode can be used with.

__Table B-2__  Modes and associated categories

| Mode identifiers | Compatible categories |
| `AVAudioSessionModeDefault` | All |
| `AVAudioSessionModeMoviePlayback` | `AVAudioSessionCategoryPlayback` |
| `AVAudioSessionModeVideoRecording` | `AVAudioSessionCategoryPlayAndRecord`  `AVAudioSessionCategoryRecord` |
| `AVAudioSessionModeVoiceChat` | `AVAudioSessionCategoryPlayAndRecord` |
| `AVAudioSessionModeGameChat` | `AVAudioSessionCategoryPlayAndRecord` |
| `AVAudioSessionModeVideoChat` | `AVAudioSessionCategoryPlayAndRecord` |
| `AVAudioSessionModeSpokenAudio` | `AVAudioSessionCategoryPlayback` |
| `AVAudioSessionModeMeasurement` | `AVAudioSessionCategoryPlayAndRecord`  `AVAudioSessionCategoryRecord`  `AVAudioSessionCategoryPlayback` |

[Next](Document%20Revision%20History.md)[Previous](Audio%20Guidelines%20By%20App%20Type.md)

