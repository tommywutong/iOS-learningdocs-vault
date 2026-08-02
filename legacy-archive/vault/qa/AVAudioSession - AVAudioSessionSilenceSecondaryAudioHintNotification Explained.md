---
title: AVAudioSession - AVAudioSessionSilenceSecondaryAudioHintNotification Explained
apple_id: DTS40015063
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-01-08'
source_url: https://developer.apple.com/library/archive/qa/qa1882/_index.html
archived_at: '2026-07-18T02:35:16.159450Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1882

# AVAudioSession - AVAudioSessionSilenceSecondaryAudioHintNotification Explained

## Q:  Can you explain the purpose of the AVAudioSessionSilenceSecondaryAudioHintNotification notification.

A: iOS 8 introduced a new property called `secondaryAudioShouldBeSilencedHint` and a new notification `AVAudioSessionSilenceSecondaryAudioHintNotification` which are meant to be used together to replace the use of `isOtherAudioPlaying` when managing __Secondary audio__ playback for most applications.


```objc
/* Will be true when another application with a non-mixable audio session is playing audio. Applications may use
this property as a hint to silence audio that is secondary to the functionality of the application. For example, a game app
using AVAudioSessionCategoryAmbient may use this property to decide to mute its soundtrack while leaving its sound effects unmuted.
Note: This property is closely related to AVAudioSessionSilenceSecondaryAudioHintNotification.
*/
@property(readonly) BOOL secondaryAudioShouldBeSilencedHint  NS_AVAILABLE_IOS(8_0);
```



```
/* Registered listeners that are currently in the foreground and have active audio sessions will be notified
 when primary audio from other applications starts and stops. Check the notification's userInfo dictionary
 for the notification type -- either begin or end.
 Foreground applications may use this notification as a hint to enable or disable audio that is secondary
 to the functionality of the application. For more information, see the related property secondaryAudioShouldBeSilencedHint.
*/
AVF_EXPORT NSString *const AVAudioSessionSilenceSecondaryAudioHintNotification NS_AVAILABLE_IOS(8_0);
```


__Primary audio__ - Audio that is absolutely required by an application. This audio should always play regardless of any other audio being played by other applications running on the system.

__Secondary audio__ - Audio that can enhance an application but is not absolutely required. This audio may be turned off when other applications are already playing audio on the system.

For example, a game may classify its primary audio as sound effects; explosions, bleeps & bloops, short bits of dialog and so on. This is the audio that is absolutely required for gameplay and should always play even if music is being played elsewhere on the system by some other application. The user would expect this primary audio to mix in with the other system audio that is already playing.

This same game would classify secondary audio as its music soundtrack. While the music soundtrack would enhance gameplay, it's not considered mandatory. If the user was previously listening to their own music or podcast the game could choose to mute its own music soundtrack.

By using the `secondaryAudioShouldBeSilencedHint` property and the `AVAudioSessionSilenceSecondaryAudioHintNotification` notification, the game can decide when to mute or un-mute its secondary audio soundtrack.

You can think of the `AVAudioSessionSilenceSecondaryAudioHintNotification` as a voluntary interruption. iOS informs your application that another application is playing audio thereby letting your application decide when to mute or un-mute some or all of its audio in response to another application playing audio. This notification provides a `AVAudioSessionSilenceSecondaryAudioHintType` dictionary key containing a value indicating the type of notification. A begin event called `AVAudioSessionSilenceSecondaryAudioHintTypeBegin` or an end event called `AVAudioSessionSilenceSecondaryAudioHintTypeEnd`.


```
/* keys for AVAudioSessionSilenceSecondaryAudioHintNotification */
/* value is an NSNumber representing an AVAudioSessionSilenceSecondaryAudioHintType */
AVF_EXPORT NSString *const AVAudioSessionSilenceSecondaryAudioHintTypeKey NS_AVAILABLE_IOS(8_0);

/* Used in AVAudioSessionSilenceSecondaryAudioHintNotification to indicate whether optional secondary audio muting should begin or end */
typedef NS_ENUM(NSUInteger, AVAudioSessionSilenceSecondaryAudioHintType)
{
    AVAudioSessionSilenceSecondaryAudioHintTypeBegin = 1,  /* the system is indicating that another application's primary audio has started */
    AVAudioSessionSilenceSecondaryAudioHintTypeEnd = 0,    /* the system is indicating that another application's primary audio has stopped */
} NS_AVAILABLE_IOS(8_0);
```

When your application is notified of the begin event it is a good time mute your secondary audio. When your application receives the end event it is a good time to resume playback of your secondary audio. The application is in control of what it would like to do when using these hints, there are no behaviors forced upon your application by the audio system.

[What's New In Core Audio WWDC 2014](https://developer.apple.com/videos/wwdc/2014/#501)

See AVAudioSession.h which is part of AVFoundation for complete details.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-01-08 | Editorial |
| 2014-12-03 | New document that discusses the new AVAudioSessionSilenceSecondaryAudioHintNotification notification and secondaryAudioShouldBeSilencedHint property of AVAudioSession. |

