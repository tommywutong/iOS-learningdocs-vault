---
title: Audio Session Programming Guide
apple_id: TP40007875
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/AudioGuidelinesByAppType/AudioGuidelinesByAppType.html
archived_at: '2026-07-15T05:20:45.338378Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Session Programming Guide](Introduction.md)


[Next](Audio%20Session%20Categories%20and%20Modes.md)[Previous](Protecting%20User%20Privacy.md)

# Audio Guidelines By App Type

The latest driving game does not have the same audio requirements as a real-time video chat app. The following sections provide design guidelines for different types of audio apps.

Most games require user interaction for anything to happen in the game. Use the [AVAudioSessionCategoryAmbient](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryambient) or [AVAudioSessionCategorySoloAmbient](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategorysoloambient) categories when designing games. When users bring up another app or lock the screen, they do not expect the app to continue playing. Often they want the audio from another app to continue playing while the game app plays.

Here are some recommended guidelines:

- Activate your audio session in the app delegate’s [applicationDidBecomeActive:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622956-applicationdidbecomeactive) method.
- Play app sound effects while allowing another app’s audio to play.
- Play app soundtrack audio when other audio is not playing, otherwise allow the previous audio to play.
- Always attempt to reactivate and resume playback of sound effects after an end interruption event.
- Query the audio session’s [secondaryAudioShouldBeSilencedHint](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616600-secondaryaudioshouldbesilencedhi) property to determine if you should resume playback of your game’s soundtrack.
- Ignore all route changes unless the app specifically needs to pay attention to them.
- Set the audio category before displaying a video splash on app launch.

Recording apps and playback apps such as Pandora and Netflix have similar guidelines. These types of apps use the [AVAudioSessionCategoryRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616451-record), [AVAudioSessionCategoryPlayAndRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616568-playandrecord), or [AVAudioSessionCategoryPlayback](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryplayback) categories and typically interrupt other system audio when their audio sessions are activated. The UI will include a play/pause button or a record/pause button.

Here are some recommended guidelines:

- When the app enters the foreground, wait for the user to press the Play or Record button before activating the audio session.
- While the app is in the foreground, keep the audio session active unless it’s interrupted.
- If the app is not actively playing or recording audio when it transitions to the background, deactivate its audio session. This prevents its audio session from being interrupted by another nonmixable app or by the system in response to the app being suspended.
- Update the UI to indicate that playback or recording has paused when it’s interrupted. Do not deactivate the audio session.
- Observe notifications of type [AVAudioSessionInterruptionNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616596-interruptionnotification) to be notified of audio session interruptions. When an interruption ends, don’t start playing or recording audio again unless the app was doing so prior to the interruption.
- Pause playback or recording if a route change is caused by an unplug event, but keep the audio session active.
- Assume the app’s audio session is inactive when it transitions from a suspended to foreground state. Reactivate the audio session when the user presses the Play or Record button.
- Ensure that the audio `[UIBackgroundModes](../../../../General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xvkskcmfrwwz3sn52w4zcnn5sgk4y)` flag is set.
- Register for remote control events (see [MPRemoteCommandCenter](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter)) and provide the appropriate Now Playing information for your media (see [MPNowPlayingInfoCenter](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter)).
- Use an [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview) object to present the system volume slider and route picker.
- Use a background task instead of streaming silence to keep the app from being suspended.
- Ask the user for permission to record input using the [requestRecordPermission:](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616601-requestrecordpermission) method. Don’t rely on the operating system to prompt the user.
- For recording apps, use the [AVAudioSessionCategoryPlayAndRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616568-playandrecord) category instead of the [AVAudioSessionCategoryRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616451-record) category. The recording-only category silences virtually all system output and is usually too restrictive for most apps.

VoIP and chat apps require that both input and output routes are available. These types of apps use the [AVAudioSessionCategoryPlayAndRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616568-playandrecord) category and do not mix with other apps.

Here are some recommended guidelines:

- Only activate an audio session when the user answers or initiates a call.
- Update the UI to reflect that the call’s audio has been interrupted after an interruption notification.
- Do not activate an audio session after an interruption until the user answers or initiates a call.
- Deactivate the audio session after a call ends, using the [AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions/avaudiosessionsetactiveoptionnotifyothersondeactivation) constant.
- Ignore all route changes unless the app specifically needs to pay attention to them. For instance, route changes may result in changes to the session’s sample rate, buffer duration, or latency. If these values are relevant to your app, query them after a route change to get their latest state.
- For VoIP apps, use Apple's Voice Processing I/O audio unit.
- Ensure that the audio `[UIBackgroundModes](../../../../General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xvkskcmfrwwz3sn52w4zcnn5sgk4y)` flag is set.
- Use an [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview) object for the volume slide and route picker.
- Ask the user for permission to record input, using the [requestRecordPermission:](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616601-requestrecordpermission) method. Don’t rely on the operating system to prompt the user.

Starting in iOS 10, to build VoIP apps with the same features and capabilities found in built-in telephony apps (Phone and FaceTime apps), use the CallKit framework. For more information, see _[CallKit Framework Reference](https://developer.apple.com/documentation/callkit)_.

Metering apps need the minimal amount of system-supplied signal processing applied to the input and output routes. Set the [AVAudioSessionCategoryPlayAndRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616568-playandrecord) category and the measurement mode to minimize signal processing. Also, apps of this type do not mix with other apps.

Here are some recommended guidelines:

- Always attempt to reactivate and resume playback after an end interruption event.
- Ignore all route changes unless the app specifically needs to pay attention to them.
- Set the audio category before displaying a video splash on app launch.
- Ask the user for permission to record input, using the [requestRecordPermission:](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616601-requestrecordpermission) method. Don’t rely on the operating system to prompt the user.

Social media or other browser-like apps often play short videos. They use the [AVAudioSessionCategoryPlayback](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryplayback) category and do not obey the ringer switch. These apps also do not mix with other apps.

Here are some recommended guidelines:

- Always wait for the user to initiate playback.
- Deactivate the audio session after a video ends, using the [AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions/avaudiosessionsetactiveoptionnotifyothersondeactivation) constant.
- Pause the audio session due to a route change caused by an unplug event, but keep the audio session active.
- Register for remote control events while video is playing, and unregister when the video ends.
- Update the UI when the app receives a begin interruption event.
- Wait for the user to initiate playback after receiving an end interruption event.

Navigation and workout apps use the [AVAudioSessionCategoryPlayback](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryplayback) or [AVAudioSessionCategoryPlayAndRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616568-playandrecord) categories. The audio from these apps typically consists of short voice prompts. When played, these prompts interrupt spoken audio, such as a podcast or an audio book, and mix with (and duck) other audio, such as playback from the Music app.

Here are some recommended guidelines:

- Activate your audio session using both the [AVAudioSessionCategoryOptionInterruptSpokenAudioAndMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616534-interruptspokenaudioandmixwithot) and [AVAudioSessionCategoryOptionDuckOthers](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionduckothers) options.
- Do not activate the audio session until a prompt is needed.
- Always deactivate the audio session after a prompt is played.
- Don’t attempt to resume playback of a prompt that was interrupted.

Cooperative music apps are designed to play while other apps are playing. These types of apps use the [AVAudioSessionCategoryPlayback](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryplayback) or [AVAudioSessionCategoryPlayAndRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616568-playandrecord) category and mix with other apps.

Here are some recommended guidelines:

- Activate your audio session using the [AVAudioSessionCategoryOptionMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionmixwithothers) option.
- If the app’s UI does not provide a start/stop button, follow the guidelines for game apps.
- If the app’s UI provides a start/stop button, only activate the audio session when the user presses the play button.
- Do not sign up for remote control events.
- Ensure that the audio `[UIBackgroundModes](../../../../General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xvkskcmfrwwz3sn52w4zcnn5sgk4y)` flag is set.
- If the app records user input, ask the user for permission to record input, using the [requestRecordPermission:](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616601-requestrecordpermission) method. Don’t rely on the operating system to prompt the user.

[Next](Audio%20Session%20Categories%20and%20Modes.md)[Previous](Protecting%20User%20Privacy.md)

