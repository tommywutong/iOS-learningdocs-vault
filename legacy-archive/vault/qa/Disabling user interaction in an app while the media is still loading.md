---
title: Disabling user interaction in an app while the media is still loading
apple_id: DTS40009076
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2013-09-03'
source_url: https://developer.apple.com/library/archive/qa/qa1656/_index.html
archived_at: '2026-07-18T02:33:17.491070Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1656

# Disabling user interaction in an app while the media is still loading

## Q:  I am creating a `MPMoviePlayerController` object and calling the `play` method, but playback doesn't always begin right away when streaming media on a slow network. How can I prevent the user from continuing to work with my application while the media is loading?

A: To prevent the user from interacting with the application while the media is still loading, after calling the `MPMoviePlayerController` `play` method you can set the attribute `userInteractionEnabled = NO` on your view. This will cause user events to be ignored by the view. Once the actual movie playback begins, `MPMoviePlayerController` will put the movie player window and controls on top of your view, allowing the user to interact with the movie controls. When the movie playback finishes (or the user presses the Done button), you will get the `MPMoviePlayerPlaybackDidFinishNotification` notification, at which time you can set the attribute `userInteractionEnabled=YES` on your view to allow the handling of user events again.

Alternately, just after calling the `MPMoviePlayerController` `play` method you can add a new view with attribute `userInteractionEnabled = NO` __on top__ of your regular application user interface . This will also prevent any user interaction with your application. Then once the movie finishes playing, simply remove the view.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-09-03 | Minor content update. |
| 2009-08-05 | New document that discusses how to disablel user interaction within your app while the media is still loading |

