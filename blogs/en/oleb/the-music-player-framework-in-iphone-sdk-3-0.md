---
title: The Music Player Framework in iPhone SDK 3.0
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/07/the-music-player-framework-in-the-iphone-sdk/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f37cc02b9cbb708b'
translated: false
---

> 原文：[The Music Player Framework in iPhone SDK 3.0](https://oleb.net/blog/2009/07/the-music-player-framework-in-the-iphone-sdk/)　·　Ole Begemann

# The Music Player Framework in iPhone SDK 3.0

In version 3.0 of the iPhone SDK, Apple gave us access to the iPod library on the iPhone and and easy-to-use interface to control music playback. In this post, I want to give an overview of these APIs and how I used them in the development of [Songtext](http://songtextapp.com).

# Getting started: MPMusicPlayerController

You need to add `MediaPlayer.framework` to your target in Xcode and `#import <MediaPlayer/MediaPlayer.h>`. To control music playback, we use an instance of `MPMusicPlayerController`. There are two types of music players. The `iPodMusicPlayer` is a reference to the music player instance used by the iPod app. Any settings you change, such as the shuffle or repeat modes, will be changed in the iPod app, too. If the iPod is playing when your application starts, the music will continue playing and you can access the current song and skip back and forward through the currently active playlist. When your app quits, the music will continue playing. I imagine this mode is very handy for most utility apps that try to improve your music listening experience by interacting with the iPod.

In contrast, `applicationMusicPlayer` gives you a music player whose settings you can change independently of the iPod app. This is probably the way to go if your app is a game and you want to give the user the ability to choose the background music from their library. In Songtext, we’ll use `iPodMusicPlayer` because we want to know which song is playing when our app launches:

```
@property (nonatomic, retain) MPMusicPlayerController *musicPlayer;
...
self.musicPlayer = [MPMusicPlayerController iPodMusicPlayer];
```

The music player uses [notifications](http://developer.apple.com/library/ios/#DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSNotification_Class/Reference/Reference.html) to inform you about changes of:

- ),
- ), or
- ).

So the next thing you typically do is to register yourself as an observer for the notifications you are interested in, e.g. in `viewDidLoad`. We want to receive all 3 notifications:

```
// Register for music player notifications
NSNotificationCenter *notificationCenter = [NSNotificationCenter defaultCenter];
[notificationCenter addObserver:self
                       selector:@selector(handleNowPlayingItemChanged:)
                           name:MPMusicPlayerControllerNowPlayingItemDidChangeNotification
                         object:self.musicPlayer];
[notificationCenter addObserver:self
                       selector:@selector(handlePlaybackStateChanged:)
                           name:MPMusicPlayerControllerPlaybackStateDidChangeNotification
                         object:self.musicPlayer];
[notificationCenter addObserver:self
                       selector:@selector(handleExternalVolumeChanged:)
                           name:MPMusicPlayerControllerVolumeDidChangeNotification
                         object:self.musicPlayer];
[self.musicPlayer beginGeneratingPlaybackNotifications];
```

There is one other related notification that is sent by the iPod media library when the contents of the library change, e.g. when you sync your device with iTunes. You must listen to this notification if your app creates its playlists that need to be updated after library changes. To do so, register yourself as an observer for `MPMediaLibraryDidChangeNotification` notifications and call:

```
[[MPMediaLibrary defaultMediaLibrary] beginGeneratingLibraryChangeNotifications]
```

The notification handlers are where you update your UI in response to changes in the player’s state:

```
// When the now playing item changes, update song info labels and artwork display.
- (void)handleNowPlayingItemChanged:(id)notification {
    // Ask the music player for the current song.
    MPMediaItem *currentItem = self.musicPlayer.nowPlayingItem;

    // Display the artist, album, and song name for the now-playing media item.
    // These are all UILabels.
    self.songLabel.text   = [currentItem valueForProperty:MPMediaItemPropertyTitle];
    self.artistLabel.text = [currentItem valueForProperty:MPMediaItemPropertyArtist];
    self.albumLabel.text  = [currentItem valueForProperty:MPMediaItemPropertyAlbumTitle];

    // Display album artwork. self.artworkImageView is a UIImageView.
    CGSize artworkImageViewSize = self.artworkImageView.bounds.size;
    MPMediaItemArtwork *artwork = [currentItem valueForProperty:MPMediaItemPropertyArtwork];
    if (artwork != nil) {
        self.artworkImageView.image = [artwork imageWithSize:artworkImageViewSize];
    } else {
        self.artworkImageView.image = nil;
    }
}

// When the playback state changes, set the play/pause button appropriately.
- (void)handlePlaybackStateChanged:(id)notification {
    MPMusicPlaybackState playbackState = self.musicPlayer.playbackState;
    if (playbackState == MPMusicPlaybackStatePaused || playbackState == MPMusicPlaybackStateStopped) {
        [self.playPauseButton setTitle:@"Play" forState:UIControlStateNormal];
    } else if (playbackState == MPMusicPlaybackStatePlaying) {
        [self.playPauseButton setTitle:@"Pause" forState:UIControlStateNormal];
    }
}

// When the volume changes, sync the volume slider
- (void)handleExternalVolumeChanged:(id)notification {
    // self.volumeSlider is a UISlider used to display music volume.
    // self.musicPlayer.volume ranges from 0.0 to 1.0.
    [self.volumeSlider setValue:self.musicPlayer.volume animated:YES];
}
```

# Accessing song metadata: MPMediaItem

![MPMediaPickerController in single-selection mode](https://oleb.net/media/MPMediaPickerController-single-selection-mode-213x320.png)

<sub>MPMediaPickerController in single-selection mode. Unfortunately, Apple does not provide context information about the selected song.</sub>

A song is represented by an instance of the `MPMediaItem` class. As you see in the code above, we access the song metadata with the `valueForProperty:`method. Available properties include pretty much all the data that is available in iTunes: title, artist, album title and artist, genre, composer, duration, track/disc number, album artwork, rating, lyrics, last played date, and play and skip counts. The [complete list of properties](http://developer.apple.com/iphone/library/documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/doc/constant_group/General_Media_Item_Property_Keys) is available in the documentation. That’s a huge amount of data for all kinds of interesting statistics or organizing apps. I am sure we will see a lot of those on the App Store in the coming months.

## No write access to iPod library

Unfortunately, we won’t see apps that require write access to the iPod library anytime soon. The entire `MPMediaItem` API is read-only at the moment. That is also the reason why Songtext cannot write the lyrics it downloads into the song files themselves to make them available outside the application. I hope Apple gives us write access in a future version of the SDK.

## Unreliable access to lyrics

While `MPMediaItem` provides access to the lyrics of a song stored in the iTunes library, I found this to be unreliable. Songtext checks if a song already has lyrics attached and if so, does not try to download them from the web. Unfortunately, this does not work all the time as sometimes, `-[MPMediaItem valueForProperty:MPMediaItemPropertyLyrics]` returns `nil` even if lyrics are present. I was not able to reproduce the exact conditions under which this error occurs. So beware if you rely on this to work properly.

# A song selection UI: MPMediaPickerController

Similar to the built-in image picker, Apple provides a complete user interface to select songs from the media library. All we need to do is create an instance of `MPMediaPickerController`, present it to the user as a modal view controller and implement the `MPMediaPickerControllerDelegate` protocol:

```
// MusicPlayerDemoViewController.h
@interface MusicPlayerDemoViewController : UIViewController <MPMediaPickerControllerDelegate> {
...
}
...
// This action should open the media picker
- (IBAction)openMediaPicker:(id)sender;

@end

// MusicPlayerDemoViewController.m
- (IBAction)openMediaPicker:(id)sender {
    MPMediaPickerController *mediaPicker = [[MPMediaPickerController alloc] initWithMediaTypes:MPMediaTypeMusic];
    mediaPicker.delegate = self;
    mediaPicker.allowsPickingMultipleItems = NO; // this is the default
    [self presentModalViewController:mediaPicker animated:YES];
    [mediaPicker release];
}

// Media picker delegate methods
- (void)mediaPicker: (MPMediaPickerController *)mediaPicker didPickMediaItems:(MPMediaItemCollection *)mediaItemCollection {
    // We need to dismiss the picker
    [self dismissModalViewControllerAnimated:YES];

    // Assign the selected item(s) to the music player and start playback.
    [self.musicPlayer stop];
    [self.musicPlayer setQueueWithItemCollection:mediaItemCollection];
    [self.musicPlayer play];
}

- (void)mediaPickerDidCancel:(MPMediaPickerController *)mediaPicker {
    // User did not select anything
    // We need to dismiss the picker
    [self dismissModalViewControllerAnimated:YES];
}
```

# Limitations of the media picker

![MPMediaPickerController in multiple-selection mode](https://oleb.net/media/MPMediaPickerController-multiple-selection-mode-213x320.png)

<sub>MPMediaPickerController in multiple-selection mode. This works like the editing of the On-The-Go playlist in the iPod app.</sub>

This is all great and simple. The media picker has one huge drawback, though: it does not provide the context from which a song was picked. It is impossible to tell whether the user selected a song from a certain playlist, from an album, or from the Songs tab. All you get back is the single MPMediaItem the user tapped. Therefore, we cannot construct a play queue in the way the iPod does, depending on the context from which the user picked the song. The Next/Previous buttons will not work as expected anymore, and the user would have to pick another song each time the current one ends (the player will just stop at the end of the song). I think this can be very confusing for the user because your app functions differently, depending on whether the user selected a song in the iPod or directly in your app. And that is the reason why Songtext does not have the capability of selecting a new song from inside the app at the moment. Let’s hope Apple improves the media picker in the future.

The media picker also has a multiple selection mode that can be enabled by setting its `allowsPickingMultipleItems` property to `YES`. This mode works like the editing of the On-The-Go playlist in the iPod app and can also be quite confusing for the user in my opinion.

# Querying the iPod library with MPMediaQuery

If you want to build a custom media picker UI or select songs programmatically without user interaction, you can do so by building queries with `MPMediaQuery` and `MPMediaPropertyPredicate`. I will cover these classes in a future post.

# Download the demo project

I have prepared a little demo project that implements most of the things I have talked about in this post: [Download MusicPlayerDemo.zip](https://oleb.net/media/MusicPlayerDemo.zip). You can do whatever you want with the code, no strings attached.

**Update October 28, 2009:** Jóhann observed that `MPMediaQuery` seems to be painfully slow. I have found the same. I don’t know of any alternative, short of maintaining your own cached song database (e.g. with Core Data). I believe the iPod app does something like that.
