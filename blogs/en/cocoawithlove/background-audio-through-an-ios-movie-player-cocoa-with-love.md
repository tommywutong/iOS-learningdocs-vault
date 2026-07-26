---
title: 'Background audio through an iOS movie player | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/04/background-audio-through-ios-movie.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:5999b254fa29b435'
translated: false
---

> 原文：[Background audio through an iOS movie player | Cocoa with Love](https://www.cocoawithlove.com/2011/04/background-audio-through-ios-movie.html)　·　Cocoa with Love (Matt Gallagher)

Background audio in iOS is supposed to be as simple as entering a setting in your Info.plist and making sure your `kAudioSessionProperty_AudioCategory` is appropriate. This is true unless your audio is part of a movie file or is played in a movie player that has just played video — suddenly it becomes fiddly, hard to test, unreliable and changeable from version to version of iOS.

## Introduction

I was not sure I wanted to write this post. It runs the risk of pointing out that I'm not perfect. But all programs have bugs and my programs are no different.

And anyway, as both Han Solo and Lando Calrissian validly said of the Millenium Falcon's failure to reach light speed, "it's not my fault". Of course, as it was in Star Wars, so it is in real life: your users don't care whose fault it is, they just want it fixed.

Obviously, I develop and sell a product named [StreamToMe, available through the iOS App Store](http://itunes.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=325327899&mt=8), that plays video and music and lists "Background audio" as one of its features. In this post, I'm going to talk about why background audio has worked and then not worked, been fixed and then not worked again only to be mostly fixed with some issues outstanding.

How can a feature that is simple, according to Apple's documentation, cause such a quality headache in a program?

In this post I'll be looking at playing background audio through the iOS movie playing APIs (either `MPMoviePlayerController` or `AVPlayer`/`AVQueuePlayer`). I've recently written a post on the [history of iOS media APIs](https://www.cocoawithlove.com/2011/03/history-of-ios-media-apis-iphone-os-20.html) but as you'll see in this post, background audio is functionality that relates to the implications of the APIs, not the APIs themselves. You need to discover the "de facto" behavior yourself and hope you're correct.

Specific points will include:

- why an application that also plays video has so much more difficulty with background audio than other kinds of applications
- why background audio has broken multiple times in StreamToMe since iOS 4 was released, despite using no undocumented functionality and despite the documented API remaining nominally unchanged
- why background audio is affected by seemingly unrelated choices like Apple's HTTP live streaming and 3G network

I'll also briefly look at quality management on a complicated program and how the largely undocumented behaviors of Apple's video APIs make perfect testing impossible.

## Apple's documentation for background audio in iOS

Apple's documentation for background audio makes it sound very simple. It is 4 paragraphs long under the heading "Playing Background Audio" on the [Executing Code in the Background](http://developer.apple.com/library/ios/#documentation/iphone/conceptual/iphoneosprogrammingguide/BackgroundExecution/BackgroundExecution.html) page.

Additionally, [Technical Q&A QA1668](http://developer.apple.com/library/ios/#qa/qa1668/_index.html) discusses "How to play audio in the background with MPMoviePlayerController" by ensuring the Audio Session Category is correct.

Background audio is mentioned in a few other pages but it mostly repeats the information found in these two locations.

It all sounds pretty simple: it seems like background audio should "just work".

## What happens to a file that contains video?

The movie players in iOS are explicitly capable of working in the background

But in the above linked Technical Q&A QA1668, the question explicitly mentions "audio-only movies and other audio files". There is no mention of what happens to files that have a video track.

In fact, there is no mention anywhere in the iOS documentation that I could find about what happens to a video file when you switch into the background.

All we can do is examine the behaviors experimentally. The following are the behaviors I've noticed in iOS 4.3 when switching video into the background.

This pause is sent from the `CALayer` displaying the video frames. This is a private class for an `MPMoviePlayerController` and is your own `AVPlayerLayer` for an `AVPlayer`.

You can't really control this — even in the situation where it's your own `AVPlayerLayer` — the pause is sent from private methods (so you can't legally override them), during a private "UIApplicationDidSuspendNotification" (so you can't legally block or intercept this). This notification occurs between the `UIApplicationWillResignActiveNotification` and the `UIApplicationDidEnterBackgroundNotification`.

Nor can you simply disconnect the `AVPlayerLayer` of an `AVPlayer` to avoid the pause being sent — this actually leads to a crash if the file is still playing for reasons that are not explained and could be either a bug in iOS or expected behavior (it's not at all clear).

While a video file started in the foreground will simply pause, a video file started in the background will actually give an error abort playback entirely.

This can even occur for a file that was pausing on entering the background but which you attempt to resume.

The video system in iOS has a degree of latency between commands you request and actual changes in playback.

My guess (again, none of this is explained in the documentation) is that this latency occurs because your video commands need to be sent to the separate mediaserverd process in iOS that handles all media playback. This process then makes the required changes and sends back response notifications.

This seems to create a situation where if you cancel the playback of a file and immediately start a new file, some of the properties of the old file will remain for a time.

In the case of playing an audio-only file immediately after a video file, this latency appears to be long enough for the audio-only file to be rejected with an error as though it was a file with video.

If you're using an `AVPlayer` or `AVQueuePlayer`, you can disable all the video tracks any time after the `AVPlayerItemStatusReadyToPlay` notification is sent using the following code:

```objc
for (AVPlayerItemTrack *track in player.currentItem.tracks)
{
    if ([track.assetTrack.mediaType isEqual:AVMediaTypeVideo])
    {
        track.enabled = NO;
    }
}
```

This will stop the tracks playing but despite the tracks being disabled, the effect on background play remains the same: presence of video in the file still causes the player to pause.

## How StreamToMe has handled video in the background

As you can tell by the summary of experimentally determined functionality above, iOS really strongly doesn't want you to play video in the background.

Frankly, iOS's restrictions in this area are contrary to what people want.

Where iOS makes a huge distinction between audio-only media and media with both video and audio, many users do not. We are accustomed to Quicktime and iTunes and VLC and MPlayer and most other media applications being able to perform all the same tasks with either video or audio.

Even for users who only use StreamToMe to play music, it's hard to avoid video in StreamToMe because StreamToMe puts a still image for the album artwork into a video track to display artwork for music files — in the eyes of iOS, basically every files StreamToMe plays counts as video.

It was necessary to find a way around these restrictions. And so begins the story of half a dozen application updates over 3 major iOS updates.

### iOS 4.0

In iOS 4.0, StreamToMe used `MPMoviePlayerController` and was able, through a bizarre sequence of layer manipulation operations in the `MPMovieMediaTypesAvailableNotification` method (basically removing the video render layer and reinserting at the right time), to convince the `MPMoviePlayerController` to proceed, even when it was playing video in the background.

Technically, you didn't need to remove the layer to get it to play in the background (all you needed was to resume after the "UIApplicationDidSuspendNotification" pause) but if you didn't remove the video layer, video frames would still be rendered and queued for display, leading to out of memory problems or weird speedy video quirks when the video came back to the foreground.

I'm not going to share the code that did this: it was messy, not advisable and doesn't work anymore. I was fully aware that this was a bizarre thing to do and that I would need to keep a really close eye on iOS updates to ensure that it kept working.

### iOS 4.2

From the betas of iOS 4.2, it became apparent that the layer manipulation would no longer work to allow background video to work smoothly and no combination of actions I could find would make it work again. Playing the audio from a file also containing video looking like it would be impossible.

Fortunately, with StreamToMe, I control both ends of the client-server communication and there was another solution: upon entering the background, StreamToMe could reload the stream from the server with the video track stripped off by the server.

This server reconnection results in a second pause or so (more over 3G) while the new stream was started and sometimes a jump back to the start of the previous HTTP live stream segment but otherwise the experience is tolerable.

However, there was a catch: `MPMoviePlayerController` didn't like being torn down and recreated in a short space of time. In iOS 4.2, doing this would actually result in an error.

But the new `AVQueuePlayer` API introduced in iOS 4.1 _did_ support queuing a new stream and then switching to it. In fact, it did it pretty well (after all, that's what the whole "queue" is about). Unfortunately, switching to `AVQueuePlayer` from `MPMoviePlayerController` is not a small task: `AVQueuePlayer` offers no user interface (you have to implement one entirely for yourself) and the entire property observation model is completely different.

The following code sample shows how a switch to a background track was managed in the `UIApplicationDidEnterBackgroundNotification`. A new "background" variant of the URL for the current item is generated by the `STMQueuePlayerController` (the StreamToMe class that relates the StreamToMe representation of files to the `AVQueuePlayer` represenation) is generated, seeked to the same point as the current file, inserted into the queue and played.

```objc
if (resyncTask)
{
    [[UIApplication sharedApplication] endBackgroundTask:resyncTask];
}
resyncTask = [[UIApplication sharedApplication]
    beginBackgroundTaskWithExpirationHandler:^{resyncTask = 0;}];

AVPlayerItem *backgroundItem =
    [[AVPlayerItem alloc]
        initWithURL:[[STMQueuePlayerController sharedPlayerController]
            urlForFile:[[STMQueuePlayerController sharedPlayerController] currentFile]
            inBackground:YES
            offset:CMTimeGetSeconds(player.currentTime)]];
[backgroundItem                              // seek the item, not the player
    seekToTime:player.currentTime
    toleranceBefore:kCMTimeZero
    toleranceAfter:kCMTimeZero];
[player insertItem:backgroundItem afterItem:currentItem];

[self stopObservingPlayerItem:currentItem];  // stop observing the old AVPlayerItem
[currentItem release];
currentItem = [backgroundItem retain];
[self startObservingPlayerItem:currentItem]; // begin observing the new AVPlayerItem

[player advanceToNextItem];
[player play];
```

The `resyncTask` is ended when this new file sends an `AVPlayerItemStatusReadyToPlay` and is used to ensure that we don't get suspended while restarting the playback.

Needing to rewrite the code for `AVQueuePlayer` left a brief gap at the start of iOS 4.2 until StreamToMe 3.3 was released, where background audio was broken in StreamToMe.

## iOS 4.3

But iOS 4.3 turned out to be a bit of a one-two punch. On paper, the big change was AirPlay video — the new feature in iOS 4.3 that didn't work with `AVQueuePlayer` (seriously) — but it turns out that iOS 4.3 also changed how movie players were paused when going into the background. This change to pausing behavior was not clear to me until _after_ iOS 4.3 was released, so StreamToMe's background behavior broke again.

What happened is that StreamToMe used to read whether the stream was currently playing (i.e. not paused) and only transition to the background version of the stream if it was actively playing. Unfortunately, the `-[AVPlayer rate]` which previously returned `1.0` for a previously playing video stream during the `UIApplicationDidEnterBackgroundNotification` would now return `0.0` (i.e. reporting that the stream was paused).

The fix is pretty simple: when we receive `UIApplicationWillResignActiveNotification` we needed to record whether the current file was playing or paused and use that information later in the `UIApplicationDidEnterBackgroundNotification` (the private "UIApplicationDidSuspendNotification" that pauses the file occurs between these two notifications).

Unfortunately, I didn't realize until the last moment on an update that the `AVPlayerLayer` had also started pausing audio-only files, not just files with video. To me, this seems like a significant change in behavior; why should an audio-only file suddenly start getting paused when the application enters the background? It's not my fault but I need to fix it anyway — unfortuntely due to the slowness in realizing this problem, this separate fix for audio-only files in StreamToMe (files with neither video nor album artwork in a video track) had to be held over until the 3.5.4 update.

> iOS 4.3 actually broke background video for Apple's apps too. While Apple's apps (iPod, Movies, Safari, YouTube) have always paused the current video when switching into the background, you used to be able to resume the video from the multitasking bar, lock screen or headphones.
> 
> From iOS 4.3, this behavior has been blocked
> 
> ; the video may play for a fraction of a second but then will immediately stop again.

### 3G and slow WiFi affecting background audio?

Even after fixing these problems it turns out iOS 4.3 had one more suprise. It now appears that the code I showed above that handles the track change:

```objc
[player insertItem:backgroundItem afterItem:currentItem];
[player advanceToNextItem];
[player play];
```

will work on a local WiFi network but on a high latency WiFi or 3G connection can cause the proper, background-safe version of the file (which is the "next item" loaded here) to be rejected.

Why on earth would the speed of the network affect this?

I'm not entirely certain but it appears that when the network is fast enough, the command:

```objc
[player insertItem:backgroundItem afterItem:currentItem];
```

actually fetches the first segment of the stream and updates all the track information, so it correctly realizes that there is no video track.

But on a slower network, this first segment of the stream is not loaded so the call to `[player play];` immediately results in an error and the file being rejected from the stream.

The fix for this is that you need to defer the call to `[player play];` until after a `AVPlayerItemStatusReadyToPlay` notification is sent for the new file.

Yuck.

## Why was this not caught in testing?

As I write this, the current version of StreamToMe is 3.5.4 and it still contains this 3G/slow WiFi problem.

Yes, I know what the cause of the bug is. Yes, I already have a fix for it. Unfortunately, the agony of release cycles and the nuisance of the App Store approval process means that I'm going to sit on this fix until I've finished the other features I wanted to include in the next update — the background audio over 3G/slow WiFi is simply too narrow a niche to justify an update right now.

However, there's one thing I've noticed about media application users: people seem to use their media within specific niches and if their specific niche isn't working, they're prepared to eviscerate you.

### How StreamToMe and ServeToMe are tested

As an independent developer, it is very difficult to handle quality assurance. I don't have a dedicated tester; I have a few people who help me test but they're all volunteers and tend to use the application however they feel. They're not really robust testers. While I use the application all day, I don't really exercise the whole application: on any given day, I focus on pretty specific issues.

Despite these resource limitations, I do have a pretty extensive set of tests. Unfortunately, the scope of the application means that the tests are arguably too extensive for my ability to run them all.

For file compatibility, I have 280 different test files in a regression suite that I run (literally media files in a folder that I run through the program and process the log file to ensure no unexpected errors). This takes 8 hours.

For server functionality, I have a test harness that tests every server command (fortunately, this takes just 30 seconds).

For client functionality, I have a 166 step, user-operated test script. This takes about an hour to perform, sitting in front of the application, pressing buttons in order.

Just 10 hours for these steps but it only tests 1 version of the program.

If you include all the different platforms for which there is platform-specific code, there are 4 versions of the server that need testing (Windows XP, Windows 7, Mac OS X 10.5, Mac OS X 10.6) and 6 versions of the client (iOS 3 on any iOS device, iOS 3.2 iPad, iOS 4 on iPhone 3G, iOS 4 on iPhone 3Gs, iOS 4 on iPhone 4, iOS 4 on iPad).

You should realize that just running this suite in these testing environments would take me about a week. And that's if I worked non-stop on StreamToMe, which I don't.

### But the bug slips through: how do you fix it?

It is unreasonable for me to fully test minor releases and sometimes minor issues slip through. Needing to limit testing so that it is manageable has resulted in some minor bugs but it does not describe why this latest 3G/slow-WiFi problem escaped testing.

Even if I had run my full test suite on version 3.5.4 of StreamToMe, it would not have detected the problem between 3G and background audio. This is because the test script tested background audio on local WiFi — you don't generally insert repeats of tests into your script unless you suspect something about the repeat in a new context will actually affect the test. In this case, I had no reason to suspect that the two ideas would be connected.

An interesting thought to consider here: _the code coverage through my program is identical on local WiFi and 3G_. The difference is either somewhere in Apple's code or purely a timing problem.

All you can do in these situations is add the scenario to your test cases, fix the bug and makes sure it keeps getting tested in new releases.

## Conclusion

I hope you can see that even when APIs are documented, the usage and implications of the API can be unknown and subject to misunderstandings and change over time. The fact that video cannot play in the background is barely mentioned by the documentation but the details of video being paused, stopped or rejected with an error is completely absent from documentation (you will only discover this by experimentation).

Lack of information is always hard to deal with in testing. You can only exercise documented or otherwise suspected behavior, and even so, you need to be practical. You can't simply say: test everything about background audio. You need to formulate your tests based on what you think is likely to have different effects.

The decision by Apple to forbid video in the background is frustrating and puzzling from my perspective. Why can't iOS simply ignore video packets in the background — particularly for disabled tracks? I can only presume that there's a technical reason for this behavior but since we haven't been informed of the boundaries, it remains frustrating.

Additionally, the entire iOS environment makes this type of problem exceptionally difficult to characterize and test. UI automation is insanely difficult in iOS and even if it improved (I'm keeping my eye on [Cucumber](http://cukes.info/)+[Frank](http://blog.thepete.net/2010/07/frank-automated-acceptance-tests-for.html)) it probably wouldn't be able to exercise background switches and realtime and network issues easily.
