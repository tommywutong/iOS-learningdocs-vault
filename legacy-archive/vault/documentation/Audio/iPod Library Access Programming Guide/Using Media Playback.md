---
title: iPod Library Access Programming Guide
apple_id: TP40008765
resource_type: Guide
platform: tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Audio/Conceptual/iPodLibraryAccess_Guide/UsingMediaPlayback/UsingMediaPlayback.html
archived_at: '2026-07-15T05:20:53.866867Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iPod Library Access Programming Guide](Introduction.md)


[Next](Using%20the%20Media%20Item%20Picker.md)[Previous](About%20iPod%20Library%20Access.md)

# Using Media Playback

To play songs, audio books, and audio podcasts from a device iPod library, you use a music player—an instance of the [MPMusicPlayerController](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller) class. In a nutshell, the steps to perform are as follows:

1. Register to receive music player notifications, and turn on notifications
2. Create a music player
3. Set up a playback queue for the music player
4. Configure the playback options
5. Invoke playback

This chapter describes how to implement these steps. It also provides guidance for handling some scenarios you may encounter when using a music player, such as appending to an existing playback queue while music is playing. There are expanded versions of the code examples from this chapter in the _[AddMusic](../../../samplecode/AddMusic/AddMusic.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobugu)_ sample application.

If you provide music player playback control, or if you display information about the now-playing item, you must register for music player notifications as shown in Listing 2-1.

__Listing 2-1__  Registering for and activating music player notifications

```
NSNotificationCenter *notificationCenter = [NSNotificationCenter defaultCenter];

[notificationCenter
    addObserver: self
    selector:    @selector (handle_NowPlayingItemChanged:)
    name:        MPMusicPlayerControllerNowPlayingItemDidChangeNotification
    object:      musicPlayer];

[notificationCenter
    addObserver: self
    selector:    @selector (handle_PlaybackStateChanged:)
    name:        MPMusicPlayerControllerPlaybackStateDidChangeNotification
    object:      musicPlayer];

[musicPlayer beginGeneratingPlaybackNotifications];
```

You implement the methods provided to the _selector:_ parameters shown here. For example implementations, see the _[AddMusic](../../../samplecode/AddMusic/AddMusic.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobugu)_ sample.

Before deallocating a music player, unregister for notifications and then turn them off as shown in Listing 2-2.

__Listing 2-2__  Unregistering and deactivating music player notifications

```
[[NSNotificationCenter defaultCenter]
    removeObserver: self
    name:           MPMusicPlayerControllerNowPlayingItemDidChangeNotification
    object:         musicPlayer];

[[NSNotificationCenter defaultCenter]
    removeObserver: self
    name:           MPMusicPlayerControllerPlaybackStateDidChangeNotification
    object:         musicPlayer];

[musicPlayer endGeneratingPlaybackNotifications];
```


To create an application music player, just call the [applicationMusicPlayer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624156-applicationmusicplayer) class method as shown in the first line of Listing 2-3.

__Listing 2-3__  Creating an application music player

```
MPMusicPlayerController* appMusicPlayer =
    [MPMusicPlayerController applicationMusicPlayer];

[appMusicPlayer setShuffleMode: MPMusicShuffleModeOff];
[appMusicPlayer setRepeatMode: MPMusicRepeatModeNone];
```

As the listing shows, you may also want to configure shuffle and repeat modes so that they do not take on the iPod app’s modes—which they would do by default.

The various shuffle and repeat modes are described in _[MPMusicPlayerController Class Reference](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller)_.

Creating an iPod music player has an extra step because you have access to the built-in iPod application’s state and there may be a now-playing item as your application launches. Listing 2-4 shows how to test for a now-playing item when the iPod app is playing an item from the device iPod library.

__Listing 2-4__  Creating an iPod music player

```
MPMusicPlayerController* iPodMusicPlayer =
    [MPMusicPlayerController iPodMusicPlayer];

if ([iPodMusicPlayer nowPlayingItem]) {
    // Update the UI (artwork, song name, volume indicator, etc.)
    //        to reflect the iPod state
}
```

As shown in the listing, your application can update its user interface and state based on the now-playing item.

There are two main ways to set up a playback queue for a music player:

- Use a media item collection
- Use a media query, which implicitly defines a collection

You get a collection by using the database access classes or by employing the media item picker. Either way, applying the collection to a music player involves a single method call, shown here:

```
[musicPlayer setQueueWithItemCollection: userMediaItemCollection];
```

Alternatively, you can set up a queue using a media query—which, in turn, implicitly defines a collection, as shown here:

```
[musicPlayer setQueueWithQuery: [MPMediaQuery songsQuery]];
```

You can, of course, specify a more complex query as an argument to the `setQueueWithQuery:` method. For more on queries, see [Using the iPod Library](Using%20the%20iPod%20Library.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donrvfvbuqmjqgewvgvzr).

Listing 2-5 shows a practical playback queue setup—one that accounts for playback state, whether a new collection should replace the player’s queue or append to it, and so on.

__Listing 2-5__  Setting up a playback queue in context

```objc
- (void) updateQueueWithCollection: (MPMediaItemCollection *) collection {

    // Add 'collection' to the music player's playback queue, but only if
    //    the user chose at least one song to play.
    if (collection) {

        // If there's no playback queue yet...
        if (userMediaItemCollection == nil) {
            [self setUserMediaItemCollection: collection];
            [musicPlayer setQueueWithItemCollection: userMediaItemCollection];
            [musicPlayer play];

        // Obtain the music player's state so it can be restored after
        //    updating the playback queue.
        } else {
            BOOL wasPlaying = NO;
            if (musicPlayer.playbackState == MPMusicPlaybackStatePlaying) {
                wasPlaying = YES;
            }

            // Save the now-playing item and its current playback time.
            MPMediaItem *nowPlayingItem        = musicPlayer.nowPlayingItem;
            NSTimeInterval currentPlaybackTime = musicPlayer.currentPlaybackTime;

            // Combine the previously-existing media item collection with
            //    the new one
            NSMutableArray *combinedMediaItems =
                [[userMediaItemCollection items] mutableCopy];
            NSArray *newMediaItems = [mediaItemCollection items];
            [combinedMediaItems addObjectsFromArray: newMediaItems];

            [self setUserMediaItemCollection:
                [MPMediaItemCollection collectionWithItems:
                    (NSArray *) combinedMediaItems]];

            [musicPlayer setQueueWithItemCollection: userMediaItemCollection];

            // Restore the now-playing item and its current playback time.
            musicPlayer.nowPlayingItem      = nowPlayingItem;
            musicPlayer.currentPlaybackTime = currentPlaybackTime;

            if (wasPlaying) {
                [musicPlayer play];
            }
        }
    }
}
```

This method branches according to whether or not there is a preexisting playback queue, and ensures that the playback state is preserved when appending to a playback queue.

Playback control for music players is straightforward, as described in _[MPMusicPlayerController Class Reference](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller)_. You can play, pause, stop, seek forward and back, and skip forward and back.

In addition, the `currentPlaybackTime` property is read/write; you can use it to set the playback point within the now-playing item’s timeline.

For example, you could let the user set the playback point in a media item’s timeline by providing a [UISlider](https://developer.apple.com/documentation/uikit/uislider) object in the application interface. In the following example, such a slider is assumed to be connected to a `timelineSlider` instance variable.

```objc
- (IBAction) setTimelinePosition: (id) sender {
    [musicPlayer setCurrentPlaybackTime: [timelineSlider value]];
}
```

[Next](Using%20the%20Media%20Item%20Picker.md)[Previous](About%20iPod%20Library%20Access.md)

