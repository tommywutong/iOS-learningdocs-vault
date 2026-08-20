---
title: Media Playback Programming Guide
apple_id: TP40016757
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/MediaPlaybackGuide/Contents/Resources/en.lproj/ConfiguringAudioSettings/ConfiguringAudioSettings.html
archived_at: '2026-07-15T05:21:17.786286Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Media Playback Programming Guide](About%20Media%20Playback.md)


[Next](Exploring%20AVFoundation.md)[Previous](Building%20a%20Basic%20Playback%20App.md)

# Configuring Audio Settings for iOS and tvOS

Media playback apps for iOS and tvOS require you to perform some configuration of your audio session to enable certain behaviors and capabilities. This chapter discusses how to perform this configuration to ensure that you provide the best possible playback experience to your users.

An audio session acts as an intermediary between your app and the operating system—and in turn, the underlying audio hardware. You use it to communicate to the operating system the _nature_ of your app’s audio without detailing the specific behavior or required interactions with the audio hardware. This delegates the management of those details to the audio session, which ensures that the operating system can best manage the user’s audio experience.

All iOS and tvOS apps have a default audio session that comes preconfigured as follows:

- Audio playback is supported, but audio recording is disallowed (audio recording is not supported in tvOS).
- In iOS, setting the Ring/Silent switch to silent mode silences any audio being played by the app.
- In iOS, when the device is locked, the app's audio is silenced.
- When the app plays audio, any other background audio is silenced.

You get a lot of useful behavior from the default audio session, but it isn’t the behavior you need when building a media playback app. To change this behavior, you configure your app’s audio session _category_.

An audio session category defines the general audio behavior your app requires. There are seven possible categories you can use (see [Audio Session Categories and Modes](https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/AudioSessionCategoriesandModes/AudioSessionCategoriesandModes.html#//apple_ref/doc/uid/TP40007875-CH10)), but the one needed by most playback apps is called [AVAudioSessionCategoryPlayback](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryplayback). This category indicates that audio playback is a central feature of your app. When you specify this category, your app’s audio continues with the Ring/Silent switch set to silent mode (iOS only). With this category, your app can also play background audio if you're using the Audio, AirPlay, and Picture in Picture background mode. For more information, see [Enabling Background Audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3donjxfvbuqojnknlti).

You use an [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession) object to configure your app’s audio session. This is a singleton object used to set the audio session category as well as perform other configuration settings. You can interact with the audio session throughout your app’s life cycle, but it’s often useful to perform this configuration at app launch as shown in the following example:

```swift
func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]?) -> Bool {
    let audioSession = AVAudioSession.sharedInstance()
    do {
        try audioSession.setCategory(AVAudioSessionCategoryPlayback)
    } catch {
        print("Setting category to AVAudioSessionCategoryPlayback failed.")
    }
    // Other project setup
    return true
}
}
```

This category is used when you activate the audio session using the [setActive:error:](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616597-setactive) or [setActive:withOptions:error:](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616627-setactive) method.

Setting the category is the minimal interaction you’ll need to have with `AVAudioSession`, but there are many other configuration options and features you can use as well. See _[Audio Session Programming Guide](../../Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_ to learn more about using audio sessions.

iOS and tvOS apps require you to enable certain capabilities for some background operations. A common capability required by playback apps is to play background audio. With this capability enabled, your app’s audio can continue when users switch to another app or when they lock their iOS devices. This capability is also required for enabling advanced playback features like AirPlay streaming and Picture in Picture playback in iOS.

The simplest way to configure these capabilities is by using Xcode. Select your app’s target in Xcode and select the Capabilities tab. Under the Capabilities tab, set the Background Modes switch to ON and select the “Audio, AirPlay, and Picture in Picture” option under the list of available modes.

![../Art/background_modes.shot/Resources/shot_2x.png](attachments/Art/background_modes_2x.png)![../Art/background_modes.shot/Resources/shot_2x.png](attachments/Art/background_modes_2x.png)

With this mode enabled and your audio session configured, your app is ready to play background audio.

[Next](Exploring%20AVFoundation.md)[Previous](Building%20a%20Basic%20Playback%20App.md)

