---
title: Apple Media Service Reference
apple_id: TP40014716
resource_type: Guide
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreBluetooth
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/CoreBluetooth/Reference/AppleMediaService_Reference/Appendix/Appendix.html
archived_at: '2026-07-15T07:22:04.113032Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Media Service Reference](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](The%20Apple%20Media%20Service.md)

# Reference

The following tables list important ID and flag values used in the AMS.

__Table A-1__  RemoteCommandID values

| Name | Value |
| `RemoteCommandIDPlay` | 0 |
| `RemoteCommandIDPause` | 1 |
| `RemoteCommandIDTogglePlayPause` | 2 |
| `RemoteCommandIDNextTrack` | 3 |
| `RemoteCommandIDPreviousTrack` | 4 |
| `RemoteCommandIDVolumeUp` | 5 |
| `RemoteCommandIDVolumeDown` | 6 |
| `RemoteCommandIDAdvanceRepeatMode` | 7 |
| `RemoteCommandIDAdvanceShuffleMode` | 8 |
| `RemoteCommandIDSkipForward` | 9 |
| `RemoteCommandIDSkipBackward` | 10 |
| `RemoteCommandIDLikeTrack` | 11 |
| `RemoteCommandIDDislikeTrack` | 12 |
| `RemoteCommandIDBookmarkTrack` | 13 |
| Reserved | 14-255 |

__Table A-2__  EntityID values

| Name | Value |
| `EntityIDPlayer` | 0 |
| `EntityIDQueue` | 1 |
| `EntityIDTrack` | 2 |
| Reserved | 3-255 |

__Table A-3__  EntityUpdateFlags

| Name | Value |
| `EntityUpdateFlagTruncated` | (1 << 0) |
| Reserved | (1 << 1) - (1 << 7) |

__Table A-4__  PlayerAttributeID values

| Name | Value | Format |
| `PlayerAttributeIDName` | 0 | A string containing the localized name of the app. |
| `PlayerAttributeIDPlaybackInfo` | 1 | A concatenation of three comma-separated values:   - __PlaybackState:__ a string that represents the integer value of the playback state:    - `PlaybackStatePaused` = 0   - `PlaybackStatePlaying` = 1   - `PlaybackStateRewinding` = 2   - `PlaybackStateFastForwarding` = 3 - __PlaybackRate:__ a string that represents the floating point value of the playback rate. - __ElapsedTime:__ a string that represents the floating point value of the elapsed time of the current track, in seconds, at the moment the value was sent to the MR. |
| `PlayerAttributeIDVolume` | 2 | A string that represents the floating point value of the volume, ranging from 0 (silent) to 1 (full volume). |
| Reserved | 3-255 |  |

Using the following formula at any time, the MR can calculate from the Playback Rate and Elapsed Time how much time has elapsed during the playback of the track:

`CurrentElapsedTime` = `ElapsedTime` + ((`TimeNow` – `TimePlaybackInfoWasReceived`) \* `PlaybackRate`)

This lets MRs implement and display a UI scrubber without needing to poll the MS for continuous updates.

__Table A-5__  QueueAttributeID values

| Name | Value | Format |
| `QueueAttributeIDIndex` | 0 | A string containing the integer value of the queue index, zero-based. |
| `QueueAttributeIDCount` | 1 | A string containing the integer value of the total number of items in the queue. |
| `QueueAttributeIDShuffleMode` | 2 | A string containing the integer value of the shuffle mode. [Table A-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2domjwfvbuqmznknltsoa) lists the shuffle mode constants. |
| `QueueAttributeIDRepeatMode` | 3 | A string containing the integer value value of the repeat mode. [Table A-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2domjwfvbuqmznknltsoi) lists the repeat mode constants. |
| Reserved | 4-255 |  |

__Table A-6__  Shuffle Mode constants

| Name | Value |
| `ShuffleModeOff` | 0 |
| `ShuffleModeOne` | 1 |
| `ShuffleModeAll` | 2 |
| Reserved | 3-255 |

__Table A-7__  Repeat Mode constants

| Name | Value |
| `RepeatModeOff` | 0 |
| `RepeatModeOne` | 1 |
| `RepeatModeAll` | 2 |
| Reserved | 3-255 |

__Table A-8__  TrackAttributeID values

| Name | Value | Format |
| `TrackAttributeIDArtist` | 0 | A string containing the name of the artist. |
| `TrackAttributeIDAlbum` | 1 | A string containing the name of the album. |
| `TrackAttributeIDTitle` | 2 | A string containing the title of the track. |
| `TrackAttributeIDDuration` | 3 | A string containing the floating point value of the total duration of the track in seconds. |
| Reserved | 4-255 |  |

[Next](Document%20Revision%20History.md)[Previous](The%20Apple%20Media%20Service.md)

