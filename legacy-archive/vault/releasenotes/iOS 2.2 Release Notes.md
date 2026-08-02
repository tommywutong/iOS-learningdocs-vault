---
title: iOS 2.2 Release Notes
apple_id: TP40007428
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2010-09-08'
source_url: https://developer.apple.com/library/archive/releasenotes/iPhone/RN-iPhoneSDK/index.html
archived_at: '2026-07-18T02:59:12.978904Z'
---
> 导航：[总目录](../README.md) · [releasenotes](../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 2.2

#### Contents:

- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3timryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Notes of Interest](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3timryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3timryfvbuqmjnknlte)

### Bug Reporting

Please report any bugs not mentioned in the "Known Issues" using the Apple Bug Reporter on the Developer Connection website at: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/).

- For issues with your application, please provide a sample application that demonstrates the issue you are experiencing.
- When reporting any bug, please provide the OS and/or SDK version you are using and the specific hardware you are experiencing it on.
- When reporting crashing issues, include any pertinent crash logs. Crash logs can be retrieved after syncing with iTunes.

  Macintosh users can find crash logs in `~/Library/Logs/CrashReporter/MobileDevice/`<iPhone name>

  Windows users can find crash logs in `Application Data\Apple Computer\Logs\CrashReporter\MobileDevice\`<iPhone name>
- If you discover a bug on an earlier release when a later release is available, please update your device to the latest release and verify that it still occurs, as your bug may have been addressed in the newer release.

### Notes of Interest

### Media

- Line-in accessories are now supported in the SDK. Applications will be able to receive audio input on all devices. You should use the `kAudioSessionProperty_AudioInputAvailable` to determine if audio input is available at any given time.
- By default, third party applications now respect the ringer switch position. If you want to play audio even when the ringer switch is in the silent position, use AudioSession APIs and set an appropriate category.
- `kAudioSessionCategory_SoloAmbient` is a new audio session category that respects the ringer switch like `kAudioSessionCategory_Ambient`. However, unlike `kAudioSessionCategory_Ambient`, which mixes in with songs, it interrupts all other audio playback, allowing the application to use the hardware audio codecs (MP3, AAC, Apple Lossless).
- By default, audio will no longer play when the screen is locked. To play audio in this state, use the `kAudioSessionCategory_MediaPlayback` audio session category.
- Audio silenced when the screen is locked will remain silent even after the phone is woken up. To play audio after the phone sleeps and wakes up, set up an audio session and, when you hear the interruption end, restart your audio.
- `AVAudioPlayer` is a new audio object in AVFoundation for playing audio files that provides the following:

  - Simple commands for play, stop, pause, setting time and volume.
  - Will play any audio file recognized by `AudioFile` and `AudioQueue` (the objects used to implement this class).
  - Provides a delegate to handle interruptions that form part of the services of `AudioSession`.
  - User can enable metering and use the resulting values to present a visual display of the audio levels being played at any given time.

  The user of the object still controls the overall behavior and interaction of the audio player through the audio session APIs and categories.
- `kAudioFormatProperty_FirstPlayableFormatFromList`='fpfl' is a new property added to audio format. This property can be used to take a format list from one of these file formats and return from that list the first format in the list that can be played on any given device. This is based on the availability of decoders and other factors in the specification that may influence the ability of a given implementation to render the contents of a bitstream. If the format list from the audio file/stream has more than one entry in it, or the `FirstPlayableFormat` property is implemented, do the following:

  - Pass that format list to this property to get back the index of the actual format you should use to create an audio queue.
  - If the property is not implemented (earlier iOS for example) then just take the last item in the format list (this is the most compatible) to create an audio queue.

### UIViewController

- If a nil NIB name is passed to `-initWithNibName:bundle:` and `-loadView` is not overridden for the view controller subclass, the view controller will attempt to load a NIB with a name matching the view controller.
- The `UIInterfaceOrientation` property in an application's `Info.plist` is now respected for view controller-based applications. To launch an application in landscape, set the `UIInterfaceOrientation` property in the property list and make sure the view controller returns `YES` for the desired orientation in `-shouldAutorotateToInterfaceOrientation:`.
- When presenting or dismissing a view controller modally, the appear & disappear methods will be called exactly once for a modal present or dismiss, with the correct animation parameters.
- Setting the first responder to a `UITextField` or `UITextView` in `-viewWillAppear:` is now supported. Doing this will animate the keyboard in to match a push, pop, modal present or modal dismiss.

### Known Issues

### iOS Simulator

- iOS Simulator does not support network home directories.
- The version of Foundation in the simulator platform includes functionality not included in iOS. To ensure functionality is not used that is not present on iPhone, check the documentation for availability information.

### UIDatePicker

- Toggling between 11AM and 12PM may result in the Date Picker showing 12AM rather than 12PM.

### UIImage

- You have to specify the image extension to `-imageNamed:` to get results.

### UILabel

- Including the degree character in a format string disables text updates to a `UILabel` object.
- `UILabel` ignores its `contentMode` property.

### UIScrollView

- After zooming, content inset is ignored and content is left in the wrong position.

### UIStringDrawing

- `UILineBreakModeTruncateHead` and `UILineBreakModeMiddleTruncation` do not work properly for multiline text.

### UITableView

- UITableView ignores `separatorStyle` and `separatorColor`.
- `UITextView` objects embedded inside a `UITableViewCell` never receive touches.
- It is very, very expensive to customize row heights (via `tableView:heightForRowAtIndexPath:`).
- Unable to resize table wider than the screen.

### UITextField

- `UITextField` cannot be made to resign first responder once offscreen.

### UITextView

- Setting `UITextView.editable` to `YES` should not automatically show the keyboard.

### UIToolbarController

- `-[UIToolbarController setSelectionIndex]` doesn't work for members of the `viewControllers` array that are offscreen.

### UITouch

- `UITouch` is not adjusted when a layer has a transform applied to it.
- `UITouch` does not properly handle multiple taps from multiple fingers.
- An application will not receive `UITouchPhaseBegan` if a swipe begins on or above the status bar.

### UIView

- Many UIKit controls cannot be resized properly if initialized with a `CGRectZero` frame.
- `animationDidEnd` fires too soon and can cause animations to stutter if you do too much work in the callback.
- If a view subclass implements `-drawRect:` then the background color for that view subclass cannot be animated.

### UIViewController

- `UINavigationController` won't resize content view automatically if `barStyle` is changed to/from `UIBarStyleBlackTranslucent`.
- If a view is detached from a given `UIViewController` as a top-level nib object, but connected as an outlet, the view's origin is incorrectly moved upwards by approximately 24 pixels.

### UIWebView

- Links don't highlight when WebKit is single threaded.

### Xcode/Developer Tools

- You may only use `.png` files for application icons for the device.
- The iOS SDK is designed for Intel-based Macs and is not supported on PPC-based Macs.
- Xcode and the iOS SDK only work in 32-bit mode; 64-bit mode is not supported.
- When running and debugging on a device, be sure to turn off Passcode lock.
- __FIXED:__ Using the Xcode menu Run > Start with Performance Tool > <instrument> does not work even though it is enabled. The application is not uploaded to the device. When the application is already present, Instruments targets the local machine and "Target failed to start" appears in the tracks.
- Trying to debug two applications at the same time on the same device fails with a broken pipe error in the debugger console.
- __FIXED:__ Instruments will act unpredictably with multiple devices attached.
