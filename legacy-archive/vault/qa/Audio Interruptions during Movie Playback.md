---
title: Audio Interruptions during Movie Playback
apple_id: DTS40009075
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2009-08-05'
source_url: https://developer.apple.com/library/archive/qa/qa1647/_index.html
archived_at: '2026-07-18T02:33:14.526795Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1647

# Audio Interruptions during Movie Playback

## Q:  I'm playing some audio in my application. If I start a movie playing while my audio is also playing, my audio interruption listener is invoked. However, when the movie stops playing my audio interruption listener is not invoked again. Please explain.

A: I'm playing some audio in my application. If I start a movie playing while my audio is also playing, my audio interruption listener is invoked. However, when the movie stops playing my audio interruption listener is not invoked again. Please explain.

An __audio interruption__ is the deactivation of your application’s audio session and may happen when a competing audio session activates and that session is not categorized to mix with yours. While the primary source of such interruptions is incoming phone calls, as soon as you call the `play` method for a `MPMoviePlayerController` object instance, the player initiates a transition that fades the screen from your current window content to the designated background color of the player and causes your application’s audio session to be deactivated.

Your application's audio session will not be re-activated until the `MPMoviePlayerController` object instance is actually released -- simply stopping the movie playback won't reactivate your session, and you won't be able to continue playing any audio while the `MPMoviePlayerController` object instance is active (this is in case the user decides to play the movie again, or perhaps scrub back and replay just a portion of the movie).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-08-05 | New document that discusses how to handle movie playback interruptions when playing audio. |

