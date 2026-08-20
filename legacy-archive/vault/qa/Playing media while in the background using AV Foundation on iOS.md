---
title: Playing media while in the background using AV Foundation on iOS
apple_id: DTS40010209
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-07-31'
source_url: https://developer.apple.com/library/archive/qa/qa1668/_index.html
archived_at: '2026-07-27T07:25:59.498068Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1668

# Playing media while in the background using AV Foundation on iOS

## Q:  How do I ensure my media will continue playing when using AV Foundation while my application is in the background?

A: You must declare your app plays audible content while in the background, assign an appropriate category to your audio session (`AVAudioSession`), and make sure your app has an active audio session before entering the background. See also [Special Considerations for Video Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamrqhewugsbrfvlesrcfj4).

## Declare your app plays Audible Content while in the Background

You must configure your app’s capabilities to enable it to play audible content while in the background. With this capability enabled, your app’s audio can continue when users switch to another app or when they lock their iOS devices. This capability is also required for enabling advanced playback features like AirPlay streaming and Picture in Picture playback in iOS.

The learn how to configure your app’s capabilities to enable it to play background audio, see [Enabling Background Audio](../documentation/Audio/Audio%20Session%20Programming%20Guide/Configuring%20an%20Audio%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzvfvbuqmznknltg).

[Back to Top](#)

## Setting the Audio Session Category

You must assign an appropriate category to your audio session to ensure your audio plays even with the screen locked and with the Ring/Silent switch set to silent. You cannot rely on the default audio session, whose category is `AVAudioSessionCategorySoloAmbient`.

For playback to continue when the screen locks, or when the Ring/Silent switch is set to silent, use the `AVAudioSessionCategoryPlayback` category. See [Configuring an Audio Session](../documentation/Audio/Audio%20Session%20Programming%20Guide/Configuring%20an%20Audio%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzvfvbuqmznknlto).

[Back to Top](#)

## Make sure you app has an active Audio Session before entering the Background

Your app must have an active audio session before entering the background. If your app's audio session is deactivated when the app enters the background your app will be suspended, because as far as the system knows, your app is no longer playing audio.

To learn how to activate an audio session, see [Activating an Audio Session](../documentation/Audio/Audio%20Session%20Programming%20Guide/Activating%20an%20Audio%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzvfvbuqmrnknltc).

[Back to Top](#)

## Special Considerations for Video Media

If the `AVPlayer`'s current item is displaying __video__ on the device's display, playback of the `AVPlayer` is automatically paused when the app is sent to the background. There are two ways to prevent this pause:

- Disable the video tracks in the player item (file-based content only). See Listing 1.
- Remove the `AVPlayerLayer` from its associated `AVPlayer` (set the `AVPlayerLayer` `player` property to nil). See Listing 2.

__Important:__ These changes must be in effect __before__ the application is actually switched to the background. Otherwise, the `AVPlayer` will be paused. An app delegate's `applicationDidEnterBackground` method is convenient for this purpose. If you disable any video tracks, these must be reenabled again when the app transitions to the foreground or the video will not resume playback. Similarly, you must reattach any `AVPlayerLayer`'s to the `AVPlayer`. The application delegate `applicationDidBecomeActive` method is convenient for this purpose.

__Note:__ You can prevent playback of an HTTP Live Stream containing video from being paused when your application is sent to the background by removing the `AVPlayerLayer` from the `AVPlayer` (set the `AVPlayerLayer` `player` property to nil). Disabling the video tracks is effective only for file-based content.

__Listing 1__  Disabling the video tracks in the player item.

```
import AVFoundation

let playerItem = <#Your player item#>

let tracks = playerItem.tracks
for playerItemTrack in tracks {

    // Find the video tracks.
    if playerItemTrack.assetTrack.hasMediaCharacteristic(AVMediaCharacteristicVisual) {

        // Disable the track.
        playerItemTrack.isEnabled = false
    }
}
```

__Listing 2__  Remove/Restore the `AVPlayerLayer` and its associated `AVPlayer`.

```swift
import UIKit
import AVFoundation

...

// A `UIView` subclass that is backed by an `AVPlayerLayer` layer.
class PlayerView: UIView {
    var player: AVPlayer? {
        get {
            return playerLayer.player
        }

        set {
            playerLayer.player = newValue
        }
    }

    var playerLayer: AVPlayerLayer {
        return layer as! AVPlayerLayer
    }

    override class var layerClass: AnyClass {
        return AVPlayerLayer.self
    }
}

...

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    @IBOutlet weak var playerView: PlayerView!

    /*
     Remove the AVPlayerLayer from its associated AVPlayer
     once the app is in the background.
     */
    func applicationDidEnterBackground(_ application: UIApplication) {

        // Remove the player.
        playerView.player = nil
    }

    // Restore the AVPlayer when the app is active again.
    func applicationDidBecomeActive(_ application: UIApplication) {

        // Restore the player.
        playerView.player = <#Your player#>
    }
}
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-07-31 | Remove outdated information. Added references to Audio Session Programming Guide, plus information about having an active audio session before the app enters the background. Converted code snippets to Swift. |
| 2014-02-12 | Added code snippet showing how to remove an AVPlayer from an AVPlayerLayer. Specified use of app delegate applicationDidEnterBackground as the recommended method for adding code to prevent video pause. Reorganization of some of the Q&A material. Other miscellaneous changes. |
| 2013-04-29 | Updated special considerations for playback of HTTP Live Streams. |
| 2013-04-11 | Provided code snippets to show how to disable a player item's video tracks. Added special considerations for playback of HTTP Live Streams. Other miscellaneous changes. |
| 2012-03-06 | Updated to include AirPlay information. |
| 2010-07-27 | New document that discusses playing media while in the background using AV Foundation on iOS |
