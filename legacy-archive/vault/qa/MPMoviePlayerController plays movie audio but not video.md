---
title: MPMoviePlayerController plays movie audio but not video
apple_id: DTS40010190
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2010-07-20'
source_url: https://developer.apple.com/library/archive/qa/qa1240/_index.html
archived_at: '2026-07-18T02:30:17.676066Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1240

# MPMoviePlayerController plays movie audio but not video

## Q:  I'm able to successfully play movies using `MPMoviePlayerController` on iOS 3.1.3. When I run this same code on the iPad and on the iPhone with iOS 4 I can hear the movie audio, but the video is no longer displayed. What's going on?

A: Starting with iPhone iOS 3.2, calling the `-play:` method still starts playback of the movie but it does not ensure that the movie is visible. In order to display a movie, you must get the new `view` property from your `MPMoviePlayerController` object and add that view to your view hierarchy. Here's a code snippet:

__Listing 1__  How to add the `MPMoviePlayerController` view property to your view hierarchy to play a movie.

```objc
#import <UIKit/UIKit.h>
#import <MediaPlayer/MediaPlayer.h>

MPMoviePlayerController *player = [[MPMoviePlayerController alloc] initWithContentURL:movieURL];
[[player view] setFrame:[myView bounds]]; // size to fit parent view exactly
[myView addSubview:[player view]];
[player play];
```

See [Important Porting Tip for Using the Media Player Framework](https://developer.apple.com/iphone/library/documentation/General/Conceptual/iPadProgrammingGuide/StartingYourProject/StartingYourProject.html#//apple_ref/doc/uid/TP40009370-CH9-SW10) and the [MPMoviePlayerController Class Reference](https://developer.apple.com/iphone/library/documentation/MediaPlayer/Reference/MPMoviePlayerController_Class/MPMoviePlayerController/MPMoviePlayerController.html) for more information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-07-20 | New document that describes how to play movies using MPMoviePlayerController on the iPad and on the iPhone with iOS 4 |

