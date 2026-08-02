---
title: AVFoundation Programming Guide
apple_id: TP40010188
resource_type: Guide
platform: tvOS|iOS|macOS
topic: null
technology: AVFoundation
published: '2015-06-30'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/02_Playback.html
archived_at: '2026-07-15T05:20:55.671385Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AVFoundation Programming Guide](About%20AVFoundation.md)


[Next](Editing.md)[Previous](Using%20Assets.md)

# Playback

To control the playback of assets, you use an `AVPlayer` object. During playback, you can use an [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) instance to manage the presentation state of an asset as a whole, and an [AVPlayerItemTrack](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack) object to manage the presentation state of an individual track. To display video, you use an [AVPlayerLayer](https://developer.apple.com/documentation/avfoundation/avplayerlayer) object.

A player is a controller object that you use to manage playback of an asset, for example starting and stopping playback, and seeking to a particular time. You use an instance of [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) to play a single asset. You can use an [AVQueuePlayer](https://developer.apple.com/documentation/avfoundation/avqueueplayer) object to play a number of items in sequence (`AVQueuePlayer` is a subclass of `AVPlayer`). On OS X you have the option of the using the AVKit framework’s `AVPlayerView` class to play the content back within a view.

A player provides you with information about the state of the playback so, if you need to, you can synchronize your user interface with the player’s state. You typically direct the output of a player to a specialized Core Animation layer (an instance of [AVPlayerLayer](https://developer.apple.com/documentation/avfoundation/avplayerlayer) or [AVSynchronizedLayer](https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer)). To learn more about layers, see _[Core Animation Programming Guide](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_.

Although ultimately you want to play an asset, you don’t provide assets directly to an `AVPlayer` object. Instead, you provide an instance of [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem). A player item manages the presentation state of an asset with which it is associated. A player item contains player item tracks—instances of [AVPlayerItemTrack](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack)—that correspond to the tracks in the asset. The relationship between the various objects is shown in Figure 2-1.

__Figure 2-1__  Playing an asset

!

This abstraction means that you can play a given asset using different players simultaneously, but rendered in different ways by each player. Figure 2-2 shows one possibility, with two different players playing the same asset, with different settings. Using the item tracks, you can, for example, disable a particular track during playback (for example, you might not want to play the sound component).

__Figure 2-2__  Playing the same asset in different ways

!

You can initialize a player item with an existing asset, or you can initialize a player item directly from a URL so that you can play a resource at a particular location (`AVPlayerItem` will then create and configure an asset for the resource). As with `AVAsset`, though, simply initializing a player item doesn’t necessarily mean it’s ready for immediate playback. You can observe (using [key-value observing](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/KVO.html#//apple_ref/doc/uid/TP40009448-CH16)) an item’s [status](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389493-status) property to determine if and when it’s ready to play.

The way you configure an asset for playback may depend on the sort of asset you want to play. Broadly speaking, there are two main types: file-based assets, to which you have random access (such as from a local file, the camera roll, or the Media Library), and stream-based assets (HTTP Live Streaming format).

__To load and play a file-based asset.__ There are several steps to playing a file-based asset:

- Create an asset using [AVURLAsset](https://developer.apple.com/documentation/avfoundation/avurlasset).
- Create an instance of `AVPlayerItem` using the asset.
- Associate the item with an instance of `AVPlayer`.
- Wait until the item’s `status` property indicates that it’s ready to play (typically you use [key-value observing](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/KVO.html#//apple_ref/doc/uid/TP40009448-CH16) to receive a notification when the status changes).

This approach is illustrated in [Putting It All Together: Playing a Video File Using AVPlayerLayer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmznknlte).

__To create and prepare an HTTP live stream for playback.__ Initialize an instance of `AVPlayerItem` using the URL. (You cannot directly create an `AVAsset` instance to represent the media in an HTTP Live Stream.)

```
NSURL *url = [NSURL URLWithString:@"<#Live stream URL#>];
// You may find a test stream at <http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8>.
self.playerItem = [AVPlayerItem playerItemWithURL:url];
[playerItem addObserver:self forKeyPath:@"status" options:0 context:&ItemStatusContext];
self.player = [AVPlayer playerWithPlayerItem:playerItem];
```

When you associate the player item with a player, it starts to become ready to play. When it is ready to play, the player item creates the `AVAsset` and `AVAssetTrack` instances, which you can use to inspect the contents of the live stream.

To get the duration of a streaming item, you can observe the [duration](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389386-duration) property on the player item. When the item becomes ready to play, this property updates to the correct value for the stream.

If you simply want to play a live stream, you can take a shortcut and create a player directly using the URL use the following code:

```
self.player = [AVPlayer playerWithURL:<#Live stream URL#>];
[player addObserver:self forKeyPath:@"status" options:0 context:&PlayerStatusContext];
```

As with assets and items, initializing the player does not mean it’s ready for playback. You should observe the player’s [status](https://developer.apple.com/documentation/avfoundation/avplayer/1388096-status) property, which changes to [AVPlayerStatusReadyToPlay](https://developer.apple.com/documentation/avfoundation/avplayerstatus/avplayerstatusreadytoplay) when it is ready to play. You can also observe the [currentItem](https://developer.apple.com/documentation/avfoundation/avplayer/1387569-currentitem) property to access the player item created for the stream.

__If you don’t know what kind of URL you have,__ follow these steps:

1. Try to initialize an `AVURLAsset` using the URL, then load its `tracks` key.

   If the tracks load successfully, then you create a player item for the asset.
2. If 1 fails, create an `AVPlayerItem` directly from the URL.

   Observe the player’s [status](https://developer.apple.com/documentation/avfoundation/avplayer/1388096-status) property to determine whether it becomes playable.

If either route succeeds, you end up with a player item that you can then associate with a player.

To start playback, you send a [play](https://developer.apple.com/documentation/avfoundation/avplayer/1386726-play) message to the player.

```objc
- (IBAction)play:sender {
    [player play];
}
```

In addition to simply playing, you can manage various aspects of the playback, such as the rate and the location of the playhead. You can also monitor the play state of the player; this is useful if you want to, for example, synchronize the user interface to the presentation state of the asset—see [Monitoring Playback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmznknltq).

You change the rate of playback by setting the player’s [rate](https://developer.apple.com/documentation/avfoundation/avplayer/1388846-rate) property.

```
aPlayer.rate = 0.5;
aPlayer.rate = 2.0;
```

A value of 1.0 means “play at the natural rate of the current item”. Setting the rate to 0.0 is the same as pausing playback—you can also use [pause](https://developer.apple.com/documentation/avfoundation/avplayer/1387895-pause).

Items that support reverse playback can use the rate property with a negative number to set the reverse playback rate. You determine the type of reverse play that is supported by using the playerItem properties [canPlayReverse](https://developer.apple.com/documentation/avfoundation/avplayeritem/1385591-canplayreverse) (supports a rate value of -1.0), [canPlaySlowReverse](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390598-canplayslowreverse) (supports rates between 0.0 and -1.0) and [canPlayFastReverse](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390493-canplayfastreverse) (supports rate values less than -1.0).

To move the playhead to a particular time, you generally use [seekToTime:](https://developer.apple.com/documentation/avfoundation/avplayer/1385953-seek) as follows:

```
CMTime fiveSecondsIn = CMTimeMake(5, 1);
[player seekToTime:fiveSecondsIn];
```

The `seekToTime:` method, however, is tuned for performance rather than precision. If you need to move the playhead precisely, instead you use [seekToTime:toleranceBefore:toleranceAfter:](https://developer.apple.com/documentation/avfoundation/avplayer/1387741-seektotime) as in the following code fragment:

```
CMTime fiveSecondsIn = CMTimeMake(5, 1);
[player seekToTime:fiveSecondsIn toleranceBefore:kCMTimeZero toleranceAfter:kCMTimeZero];
```

Using a tolerance of zero may require the framework to decode a large amount of data. You should use zero only if you are, for example, writing a sophisticated media editing application that requires precise control.

After playback, the player’s head is set to the end of the item and further invocations of `play` have no effect. To position the playhead back at the beginning of the item, you can register to receive an [AVPlayerItemDidPlayToEndTimeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386566-avplayeritemdidplaytoendtime) notification from the item. In the notification’s callback method, you invoke `seekToTime:` with the argument `kCMTimeZero`.

```objc
// Register with the notification center after creating the player item.
    [[NSNotificationCenter defaultCenter]
        addObserver:self
        selector:@selector(playerItemDidReachEnd:)
        name:AVPlayerItemDidPlayToEndTimeNotification
        object:<#The player item#>];

- (void)playerItemDidReachEnd:(NSNotification *)notification {
    [player seekToTime:kCMTimeZero];
}
```


You can use an [AVQueuePlayer](https://developer.apple.com/documentation/avfoundation/avqueueplayer) object to play a number of items in sequence. The `AVQueuePlayer` class is a subclass of `AVPlayer`. You initialize a queue player with an array of player items.

```
NSArray *items = <#An array of player items#>;
AVQueuePlayer *queuePlayer = [[AVQueuePlayer alloc] initWithItems:items];
```

You can then play the queue using [play](https://developer.apple.com/documentation/avfoundation/avplayer/1386726-play), just as you would an `AVPlayer` object. The queue player plays each item in turn. If you want to skip to the next item, you send the queue player an [advanceToNextItem](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1389318-advancetonextitem) message.

You can modify the queue using [insertItem:afterItem:](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1388543-insertitem), [removeItem:](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1387400-remove), and [removeAllItems](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1385788-removeallitems). When adding a new item, you should typically check whether it can be inserted into the queue, using [canInsertItem:afterItem:](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1387289-caninsertitem). You pass `nil` as the second argument to test whether the new item can be appended to the queue.

```
AVPlayerItem *anItem = <#Get a player item#>;
if ([queuePlayer canInsertItem:anItem afterItem:nil]) {
    [queuePlayer insertItem:anItem afterItem:nil];
}
```


You can monitor a number of aspects of both the presentation state of a player and the player item being played. This is particularly useful for state changes that are not under your direct control. For example:

- If the user uses multitasking to switch to a different application, a player’s [rate](https://developer.apple.com/documentation/avfoundation/avplayer/1388846-rate) property will drop to `0.0`.
- If you are playing remote media, a player item’s [loadedTimeRanges](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389953-loadedtimeranges) and [seekableTimeRanges](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386155-seekabletimeranges) properties will change as more data becomes available.

  These properties tell you what portions of the player item’s timeline are available.
- A player’s [currentItem](https://developer.apple.com/documentation/avfoundation/avplayer/1387569-currentitem) property changes as a player item is created for an HTTP live stream.
- A player item’s [tracks](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386361-tracks) property may change while playing an HTTP live stream.

  This may happen if the stream offers different encodings for the content; the tracks change if the player switches to a different encoding.
- A player or player item’s [status](https://developer.apple.com/documentation/avfoundation/avplayer/1388096-status) property may change if playback fails for some reason.

You can use [key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) to monitor changes to values of these properties.

When a player or player item’s status changes, it emits a key-value observing change notification. If an object is unable to play for some reason (for example, if the media services are reset), the status changes to [AVPlayerStatusFailed](https://developer.apple.com/documentation/avfoundation/avplayer/status/failed) or [AVPlayerItemStatusFailed](https://developer.apple.com/documentation/avfoundation/avplayeritemstatus/avplayeritemstatusfailed) as appropriate. In this situation, the value of the object’s `error` property is changed to an error object that describes why the object is no longer be able to play.

AV Foundation does not specify what thread that the notification is sent on. If you want to update the user interface, you must make sure that any relevant code is invoked on the main thread. This example uses [dispatch_async](https://developer.apple.com/documentation/dispatch/1453057-dispatch_async) to execute code on the main thread.

```objc
- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object
                        change:(NSDictionary *)change context:(void *)context {

    if (context == <#Player status context#>) {
        AVPlayer *thePlayer = (AVPlayer *)object;
        if ([thePlayer status] == AVPlayerStatusFailed) {
            NSError *error = [<#The AVPlayer object#> error];
            // Respond to error: for example, display an alert sheet.
            return;
        }
        // Deal with other status change if appropriate.
    }
    // Deal with other change notifications if appropriate.
    [super observeValueForKeyPath:keyPath ofObject:object
           change:change context:context];
    return;
}
```


You can [observe](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/KVO.html#//apple_ref/doc/uid/TP40009448-CH16) an [AVPlayerLayer](https://developer.apple.com/documentation/avfoundation/avplayerlayer) object’s [readyForDisplay](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1389748-isreadyfordisplay) property to be notified when the layer has user-visible content. In particular, you might insert the player layer into the layer tree only when there is something for the user to look at and then perform a transition from.

To track changes in the position of the playhead in an `AVPlayer` object, you can use [addPeriodicTimeObserverForInterval:queue:usingBlock:](https://developer.apple.com/documentation/avfoundation/avplayer/1385829-addperiodictimeobserver) or [addBoundaryTimeObserverForTimes:queue:usingBlock:](https://developer.apple.com/documentation/avfoundation/avplayer/1388027-addboundarytimeobserver). You might do this to, for example, update your user interface with information about time elapsed or time remaining, or perform some other user interface synchronization.

- With [addPeriodicTimeObserverForInterval:queue:usingBlock:](https://developer.apple.com/documentation/avfoundation/avplayer/1385829-addperiodictimeobserver), the block you provide is invoked at the interval you specify, if time jumps, and when playback starts or stops.
- With [addBoundaryTimeObserverForTimes:queue:usingBlock:](https://developer.apple.com/documentation/avfoundation/avplayer/1388027-addboundarytimeobserver), you pass an array of `CMTime` structures contained in `NSValue` objects. The block you provide is invoked whenever any of those times is traversed.

Both of the methods return an opaque object that serves as an observer. You must keep a strong reference to the returned object as long as you want the time observation block to be invoked by the player. You must also balance each invocation of these methods with a corresponding call to [removeTimeObserver:](https://developer.apple.com/documentation/avfoundation/avplayer/1387552-removetimeobserver).

With both of these methods, AV Foundation does not guarantee to invoke your block for every interval or boundary passed. AV Foundation does not invoke a block if execution of a previously invoked block has not completed. You must make sure, therefore, that the work you perform in the block does not overly tax the system.

```
// Assume a property: @property (strong) id playerObserver;

Float64 durationSeconds = CMTimeGetSeconds([<#An asset#> duration]);
CMTime firstThird = CMTimeMakeWithSeconds(durationSeconds/3.0, 1);
CMTime secondThird = CMTimeMakeWithSeconds(durationSeconds*2.0/3.0, 1);
NSArray *times = @[[NSValue valueWithCMTime:firstThird], [NSValue valueWithCMTime:secondThird]];

self.playerObserver = [<#A player#> addBoundaryTimeObserverForTimes:times queue:NULL usingBlock:^{

    NSString *timeDescription = (NSString *)
        CFBridgingRelease(CMTimeCopyDescription(NULL, [self.player currentTime]));
    NSLog(@"Passed a boundary at %@", timeDescription);
}];
```


You can register to receive an [AVPlayerItemDidPlayToEndTimeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386566-avplayeritemdidplaytoendtime) [notification](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35) when a player item has completed playback.

```
[[NSNotificationCenter defaultCenter] addObserver:<#The observer, typically self#>
                                         selector:@selector(<#The selector name#>)
                                             name:AVPlayerItemDidPlayToEndTimeNotification
                                           object:<#A player item#>];
```


This brief code example illustrates how you can use an [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) object to play a video file. It shows how to:

- Configure a view to use an `AVPlayerLayer` layer
- Create an `AVPlayer` object
- Create an `AVPlayerItem` object for a file-based asset and use key-value observing to observe its status
- Respond to the item becoming ready to play by enabling a button
- Play the item and then restore the player’s head to the beginning

For a conceptual introduction to playback, skip to [Playing Assets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmznknlti).

To play the visual component of an asset, you need a view containing an [AVPlayerLayer](https://developer.apple.com/documentation/avfoundation/avplayerlayer) layer to which the output of an [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) object can be directed. You can create a simple subclass of [UIView](https://developer.apple.com/documentation/uikit/uiview) to accommodate this:

```objc
#import <UIKit/UIKit.h>
#import <AVFoundation/AVFoundation.h>

@interface PlayerView : UIView
@property (nonatomic) AVPlayer *player;
@end

@implementation PlayerView
+ (Class)layerClass {
    return [AVPlayerLayer class];
}
- (AVPlayer*)player {
    return [(AVPlayerLayer *)[self layer] player];
}
- (void)setPlayer:(AVPlayer *)player {
    [(AVPlayerLayer *)[self layer] setPlayer:player];
}
@end
```


Assume you have a simple view controller, declared as follows:

```objc
@class PlayerView;
@interface PlayerViewController : UIViewController

@property (nonatomic) AVPlayer *player;
@property (nonatomic) AVPlayerItem *playerItem;
@property (nonatomic, weak) IBOutlet PlayerView *playerView;
@property (nonatomic, weak) IBOutlet UIButton *playButton;
- (IBAction)loadAssetFromFile:sender;
- (IBAction)play:sender;
- (void)syncUI;
@end
```

The `syncUI` method synchronizes the button’s state with the player’s state:

```objc
- (void)syncUI {
    if ((self.player.currentItem != nil) &&
        ([self.player.currentItem status] == AVPlayerItemStatusReadyToPlay)) {
        self.playButton.enabled = YES;
    }
    else {
        self.playButton.enabled = NO;
    }
}
```

You can invoke `syncUI` in the view controller’s [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) method to ensure a consistent user interface when the view is first displayed.

```objc
- (void)viewDidLoad {
    [super viewDidLoad];
    [self syncUI];
}
```

The other properties and methods are described in the remaining sections.

You create an asset from a URL using [AVURLAsset](https://developer.apple.com/documentation/avfoundation/avurlasset). (The following example assumes your project contains a suitable video resource.)

```objc
- (IBAction)loadAssetFromFile:sender {

    NSURL *fileURL = [[NSBundle mainBundle]
        URLForResource:<#@"VideoFileName"#> withExtension:<#@"extension"#>];

    AVURLAsset *asset = [AVURLAsset URLAssetWithURL:fileURL options:nil];
    NSString *tracksKey = @"tracks";

    [asset loadValuesAsynchronouslyForKeys:@[tracksKey] completionHandler:
     ^{
         // The completion block goes here.
     }];
}
```

In the completion block, you create an instance of [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) for the asset and set it as the player for the player view. As with creating the asset, simply creating the player item does not mean it’s ready to use. To determine when it’s ready to play, you can [observe](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) the item’s `status` property. You should configure this observing before associating the player item instance with the player itself.

You trigger the player item’s preparation to play when you associate it with the player.

```
// Define this constant for the key-value observation context.
static const NSString *ItemStatusContext;

// Completion handler block.
         dispatch_async(dispatch_get_main_queue(),
            ^{
                NSError *error;
                AVKeyValueStatus status = [asset statusOfValueForKey:tracksKey error:&error];

                if (status == AVKeyValueStatusLoaded) {
                    self.playerItem = [AVPlayerItem playerItemWithAsset:asset];
                     // ensure that this is done before the playerItem is associated with the player
                    [self.playerItem addObserver:self forKeyPath:@"status"
                                options:NSKeyValueObservingOptionInitial context:&ItemStatusContext];
                    [[NSNotificationCenter defaultCenter] addObserver:self
                                                              selector:@selector(playerItemDidReachEnd:)
                                                                  name:AVPlayerItemDidPlayToEndTimeNotification
                                                                object:self.playerItem];
                    self.player = [AVPlayer playerWithPlayerItem:self.playerItem];
                    [self.playerView setPlayer:self.player];
                }
                else {
                    // You should deal with the error appropriately.
                    NSLog(@"The asset's tracks were not loaded:\n%@", [error localizedDescription]);
                }
            });
```


When the player item’s status changes, the view controller receives a key-value observing change notification. AV Foundation does not specify what thread that the notification is sent on. If you want to update the user interface, you must make sure that any relevant code is invoked on the main thread. This example uses [dispatch_async](https://developer.apple.com/documentation/dispatch/1453057-dispatch_async) to queue a message on the main thread to synchronize the user interface.

```objc
- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object
                        change:(NSDictionary *)change context:(void *)context {

    if (context == &ItemStatusContext) {
        dispatch_async(dispatch_get_main_queue(),
                       ^{
                           [self syncUI];
                       });
        return;
    }
    [super observeValueForKeyPath:keyPath ofObject:object
           change:change context:context];
    return;
}
```


Playing the item involves sending a [play](https://developer.apple.com/documentation/avfoundation/avplayer/1386726-play) message to the player.

```objc
- (IBAction)play:sender {
    [player play];
}
```

The item is played only once. After playback, the player’s head is set to the end of the item, and further invocations of the `play` method will have no effect. To position the playhead back at the beginning of the item, you can register to receive an [AVPlayerItemDidPlayToEndTimeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386566-avplayeritemdidplaytoendtime) from the item. In the notification’s callback method, invoke [seekToTime:](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390153-seektotime) with the argument [kCMTimeZero](https://developer.apple.com/documentation/coremedia/cmtime/1400875-zero).

```objc
// Register with the notification center after creating the player item.
    [[NSNotificationCenter defaultCenter]
        addObserver:self
        selector:@selector(playerItemDidReachEnd:)
        name:AVPlayerItemDidPlayToEndTimeNotification
        object:[self.player currentItem]];

- (void)playerItemDidReachEnd:(NSNotification *)notification {
    [self.player seekToTime:kCMTimeZero];
}
```

[Next](Editing.md)[Previous](Using%20Assets.md)

