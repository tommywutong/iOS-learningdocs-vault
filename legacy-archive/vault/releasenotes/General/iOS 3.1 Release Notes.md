---
title: iOS 3.1 Release Notes
apple_id: TP40008407
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2010-09-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iPhoneSDK-3/index.html
archived_at: '2026-07-18T02:54:42.638188Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 3.1

#### Contents:

- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dimbxfvbuqmjnknltg)
- [Known Issues and Fixes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dimbxfvbuqmjnknlte)
- [HTTP Live Streaming Additions in iOS 3.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dimbxfvbuqmjnknltcmq)
- [Enhancements to Core Audio in iOS 3.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dimbxfvbuqmjnknltcnq)
- [New Feature in iOS 3.1: Instruments over Wi-Fi](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dimbxfvbuqmjnknltcny)
- [New Feature in iOS 3.1 with Snow Leopard: VM Tracker](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dimbxfvbuqmjnknltcoa)

### Bug Reporting

Please report any bugs not mentioned in the "Known Issues" using the Apple Bug Reporter on the Developer Connection website at: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/).

- For issues with your application, please provide a sample application that demonstrates the issue you are experiencing.
- When reporting any bug, please provide the OS and/or SDK version you are using and the specific hardware you are experiencing it on.
- When reporting crashing issues, include any pertinent crash logs. Crash logs can be retrieved after syncing with iTunes.

  Macintosh users can find crash logs in `~/Library/Logs/CrashReporter/MobileDevice/`<iPhone name>

  Windows users can find crash logs in `Application Data\Apple Computer\Logs\CrashReporter\MobileDevice\`<iPhone name>
- If you discover a bug on an earlier release when a later release is available, please update your device to the latest release and verify that it still occurs, as your bug may have been addressed in the newer release.

### Known Issues and Fixes

### Xcode/Developer Tools

- _FIXED:_Occasional errors when attempting to restore application data from the Xcode organizer.
- After installing the iOS 3.1 SDK on Snow Leopard, the static analyzer will not return results for iPhone projects building against a device SDK. To enable the static analyzer, you will need to make the following configuration change:

```
Open /Developer/Platforms/iOS.platform/Developer/Library/Xcode/Plug-ins/iOS Build System Support.xcplugin/Contents/Resources/iPhoneClangOptions.xcspec in a text editor.
change line 14:
Architectures = (__SUPPORTED_IPHONEOS_ARCHS_GCC42__);
to read:
Architectures = (armv7, armv6, armv5);
and quit and relaunch Xcode.
```
- Changing an iPhone Executable's working directory from “Build Products directory” may cause the application not to install properly with the error message “The Info.plist for application at (null) specifies a CFBundleExecutable of (null), which does not exist.”
- Xcode only searches for codesigning certificate identities in the default keychain as selected in Keychain Access.
- You may only use `.png` files for application icons for the device.
- The iOS SDK is designed for Intel-based Macs and is not supported on PPC-based Macs.
- Xcode and the iOS SDK only work in 32-bit mode; 64-bit mode is not supported.
- When running and debugging on a device, be sure to turn off Passcode lock.
- Trying to debug two applications at the same time on the same device fails with a broken pipe error in the debugger console.

### Camera API additions

The following interfaces have been added to the [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) class to allow more customized interactions with the camera.

- [showsCameraControls](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619129-showscameracontrols) property
- [cameraOverlayView](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619113-cameraoverlayview) property
- [cameraViewTransform](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619142-cameraviewtransform) property
- [takePicture](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619160-takepicture) method

The following methods have been added to the [UIVideoEditorControllerDelegate](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate) protocol for video camera interaction (iPhone 3GS only):

- [videoEditorController:didFailWithError:](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622342-videoeditorcontroller) method
- [videoEditorController:didSaveEditedVideoToPath:](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622336-videoeditorcontroller) method

For information about these new interfaces, please see the class reference documentation. Please also refer to the iOS 3.1 API diffs on the iPhone Developer Portal.

### Core Data

- [NSFetchedResultsController](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller) no longer crashes when fetch request has no sort descriptors. It’s still invalid to initialize an `NSFetchedResultsController` without sort descriptors, but a proper exception is now raised.
- In 3.1, an `NSFetchedResultsController` object whose [sectionNameKeyPath](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622285-sectionnamekeypath) property is `nil` will always return 1 for its number of sections (even if it contains no objects). Controllers whose [sectionNameKeyPath](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622285-sectionnamekeypath) property is not `nil` will add/remove sections as required.
- The memory leak of an `NSConcreteMutableData` instance when processing object changes has been fixed.
- `NSFetchedResultsController` no longer reports a message to a freed object if used before [performFetch:](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622305-performfetch) is called. It is still invalid to use the controller without calling `performFetch:` first, but the message to the freed object has been fixed.
- `NSFetchedResultsController` not updating [sectionIndexTitles](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622299-sectionindextitles) has been fixed. Workarounds are no longer necessary, as the result of `sectionIndexTitles` is properly set after object updates.

### GameKit

- A[GKPeerPickerController](https://developer.apple.com/documentation/gamekit/gkpeerpickercontroller) object can now be released immediately after the [show](https://developer.apple.com/documentation/gamekit/gkpeerpickercontroller/1622159-show) method is called, much like [UIAlertView](https://developer.apple.com/documentation/uikit/uialertview). Previously developers were required to release inside a delegate method (or methods).

### Interface Builder

- _FIXED:_ If you use Interface Builder's [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller) inspector to add a [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) to a tab bar controller, the navigation controller will be set up to show its toolbar. The toolbar won't be visible in Interface Builder, but will be visible at runtime, which is surprising. The workaround is to select the `UINavigationController` and uncheck "Shows Toolbar" in the inspector.
- In some upgrade scenarios from beta SDK releases, Interface Builder may be left with duplicate files, which causes errors such as: "Two plug-ins both integrate a class description for the class X." Removing `/Developer/Platforms/iOS Simulator.platform/Developer/Library/Interface\ Builder` and re-installing corrects the issue.
- Applications that specify a minimum iOS version of 3.1 will benefit from performance improvements in the nib unarchiving mechanism, which will improve load times for a number of data types.

### UITableView

- The [accessoryAction](https://developer.apple.com/documentation/uikit/uitableviewcell/1623249-accessoryaction) property of [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell) is deprecated. Instead, implement the [tableView:accessoryButtonTappedForRowWithIndexPath:](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614996-tableview) method in your table view delegate.

### UIViewController

- In releases prior to 3.0, the implementation of [dealloc](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/dealloc) in [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) released its view by calling `setView:` (the setter method for the `view` property) with a `nil` parameter. For applications linked on or after 3.0, the view controller still releases the view during deallocation but now does so directly and does not explicitly call the `setView:` setter method.

### HTTP Live Streaming Additions in iOS 3.1

### Failover support for HTTP live streaming

If the device fails to reload a playlist file when playing a stream (due to a 404 or a network error), it will remove the playlist URL from the list provided in the variant playlist and attempt to switch to the most suitable variant among those that remain. (If the variant playlist contains multiple variants with the same bitrate attribute, they are preferred in the order that they appear in the playlist.)

For example, a variant playlist might look like this:

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=200000
http://one.example.com/lo/prog_index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=200000
http://two.example.com/lo/prog_index.m3u8

#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=500000
http://one.example.com/md/prog_index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=500000
http://two.example.com/md/prog_index.m3u8
```

If a device playing `one.example.com/lo/` fails to reload `prog_index.m3u8` it will remove `http://one.example.com/lo/prog_index.m3u8` from the variant list and attempt to switch to `http://two.example.com/lo/prog_index.m3u8` .

If it was playing `one.example.com/md/` it would attempt to switch to `http://two.example.com/md/prog_index.m3u8` (assuming the current bandwidth measure supports it).

The switch should be seamless if one and two are serving segment files created from the same encoded stream. If they are serving segments from different encoders there will be a glitch similar to one found when two variants do not have the same audio stream.

Playback will stop if all variant playlists have been removed.

### Discontinuity tag

The `EXT-X-DISCONTINUITY` tag indicates that the media file following it has different characteristics than the one that preceded it. The set of characteristics that _may_ change is:

- file format
- number and type of tracks
- encoding parameters
- encoding sequence
- timestamp sequence

For the iPhone, we do not recommend changing encoding parameters.

### Audio-only with poster image

It's now possible to deploy an audio-only stream that carries a poster-image that the player will display in lieu of video. The audio-only stream would carry a JPEG or PNG image within an APIC frame in an ID3 tag, preferably at the start of each segment. The APIC frame must have Picture Type of $10 (Movie/Video screen capture).

### Enhancements to Core Audio in iOS 3.1

Core Audio now includes the following capabilities:

- The ability to enable Bluetooth input for [kAudioSessionCategory_PlayAndRecord](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_playandrecord) and [kAudioSessionCategory_RecordAudio](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_recordaudio) audio categories.

  Set the [kAudioSessionProperty_OverrideCategoryEnableBluetoothInput](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_overridecategoryenablebluetoothinput) property on the audio session. See the _[Audio Session Services Reference](https://developer.apple.com/documentation/audiotoolbox/audio_session_services)_ and _[Audio Session Programming Guide](../../documentation/Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_ for more information on usage.
- The ability to default audio output to the built-in speaker instead of the receiver for [kAudioSessionCategory_PlayAndRecord](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_playandrecord) audio category.

  Set the [kAudioSessionProperty_OverrideCategoryDefaultToSpeaker](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_overridecategorydefaulttospeaker) property on the audio session. See `<AudioToolbox/AudioServices.h>` for more information on usage.
- The ability to perform hardware assisted audio encoding (such as AAC encoding) on supported devices:

  - Checking for availability:

    - To determine availability at runtime, query [kAudioFormatProperty_Encoders](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_encoders) to see if the encoder is present and whether it is a hardware assisted encoder, by comparing the manufacturer with [kAppleHardwareAudioCodecManufacturer](https://developer.apple.com/documentation/audiotoolbox/kapplehardwareaudiocodecmanufacturer). See `<AudioToolbox/AudioFormat.h>` for more information on usage.
    - In the event of an audio interruption, a hardware assisted encoder may be interrupted. To determine at runtime if the device can resume encoding after an interruption, query [kAudioConverterPropertyCanResumeFromInterruption](https://developer.apple.com/documentation/audiotoolbox/1624333-anonymous/kaudioconverterpropertycanresumefrominterruption). See `<AudioToolbox/AudioConverter.h>` for more information on usage.
  - Setting the Audio Session

    - You must initialize an Audio Session and set a category that permits the use of hardware assisted codecs.

      - If you are recording or playing audio at the same time you are encoding, use the same Audio Session category that you would normally.
      - If you are not recording or playing audio, set the Audio Session category to [kAudioSessionCategory_AudioProcessing](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_audioprocessing).
      - See the _[Audio Session Services Reference](https://developer.apple.com/documentation/audiotoolbox/audio_session_services)_ and _[Audio Session Programming Guide](../../documentation/Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_ for more information on usage.
    - As with other uses of the audio system, you must ensure that the Audio Sessions is active during the encoding operation (including setting it active after an audio interruption).
  - Hardware assisted audio encoding is available through the Extended Audio File APIs.

    - if an audio session interruption occurs, you will need to handle any errors and resume conversion after the interruption ends.
    - See the _[Extended Audio File Services Reference](https://developer.apple.com/documentation/audiotoolbox/extended_audio_file_services)_ and _[Audio Session Programming Guide](../../documentation/Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_ for more information on usage.

### New Feature in iOS 3.1: Instruments over Wi-Fi

As of iOS SDK 3.1, it is now possible to connect to your developer devices from Instruments (on your Leopard or Snow Leopard OS X machine) using Wi-Fi rather than the USB tether. The Wi-Fi connection is 100% fully featured and supports all of the instrumentation you would normally get over the tether. It is intended for use by developers who need to attach other USB devices to their iOS-based device while doing their performance analysis. The feature may also be used in situations where having the USB tether is simply impractical or inconvenient.

If you do not need to attach other USB devices, the USB connection is still preferred for general usage. The Wi-Fi connection is slower than the USB connection and requires more power from the device to accommodate the heavy Wi-Fi traffic that can come from Instruments. As a result, using the Wi-Fi connection will drain the device's battery more rapidly than other scenarios. In addition, you cannot install applications on your device from Xcode over Wi-Fi, nor can you debug them over Wi-Fi using Xcode. You must still use the USB tether to connect to the device using Xcode.

To use this Instruments feature, both your Macintosh computer and your iOS device must have Wi-Fi enabled and must be connected to the same Wi-Fi access point. This access point must be enabled for Bonjour services. Once these conditions are met, you may establish a Wi-Fi connection using the steps described in the following sections.

### Enabling Wireless Connectivity

To enable wireless connectivity to your device, do the following:

1. Connect a USB cable from your Macintosh computer to your device. (Your computer must have the iOS 3.1 Developer SDK installed.)
2. Launch Instruments if it is not already running.
3. Open a new trace document or template.
4. While holding down the "Option/Alt" key, mouse click on the target chooser popup in the upper left of the Instruments Trace Document window.
5. The iPhone device should display as "Enable <Your device name> - Wireless" which you should select. If you do not see this, it is likely that the device does not have a Wi-Fi connection active.
6. Wait a few moments for a new device to be displayed in the target chooser, named "<Your device name> Wireless." This may take several seconds depending on the device and Wi-Fi connection, and the new device entry may be shown as disabled until the connection is fully established. If the device entry does not become enabled after several seconds it is likely that your Wi-Fi access point is not enabled for Bonjour traffic.
7. At this point, you have two Instruments servers running on your device: one running over Wi-Fi and one running over the USB tether. Because both servers consume memory, you should disconnect the USB tether as soon as you have your application installed on the device. (Disconnecting the tether terminates the USB-based Instruments server.)
8. You are now ready to start using Instruments over Wi-Fi.

### Using Instruments Wirelessly

After establishing a wireless connection, you may use your device with Instruments as if it was connected over USB. (You may also continue using the USB connection with Instruments if you did not disconnect it.) If you quit Instruments or put your device to sleep, you will still be able to re-connect to Instruments wirelessly later as needed. Simply relaunch Instruments and make sure the network connectivity conditions described earlier are present.

When you are done using the wireless connection, you should either reboot your device or use Instruments to disable the "Wireless" connection in order to reclaim the memory used by the server and reduce the power consumption. Either course of action will turn off the "Wireless" feature and server until you re-enable it from Instruments.

### Disabling Wireless Connectivity

To disable wireless connectivity from Instruments, do the following:

1. Open a new trace document or template.
2. While holding down the "Option/Alt" key, mouse click on the target chooser popup in the upper left of the Instruments Trace Document window.
3. The iPhone "Wireless" device should appear as "Disable <Your device name> - Wireless". Select this entry to disable the wireless connection. After a few seconds the "Wireless" entry in the target chooser will dim, at which point the "Wireless" connection and server is terminated. If you do not see this entry, it is likely that the device does not have an active Wi-Fi connection.

### Known Issues with Wireless Instruments

If wireless connectivity has been enabled and you quickly quit and then restart Instruments, the wireless device may not show up immediately. You may need to disable and then reenable wireless connectivity for the device in question.

### New Feature in iOS 3.1 with Snow Leopard: VM Tracker

Instruments in SnowLeopard introduces a new memory analysis instrument for both Mac and iPhone: VM Tracker. If you are using iOS 3.1 with Snow Leopard, you will be able to use this new feature.

The VM Tracker instrument is designed to report on a target process' virtual memory space, showing all of the regions mapped into the address space along with information and statistics relevant to the mapping type. For example, a region that is a memory-mapped file via an `mmap` call will show as a "mapped file" region and display the path for the file it references. Instruments shows size statistics for each region as well: virtual, resident, and dirty.

### Views

The VM Tracker instrument provides two top-level views:

1. __Summary view__ - This view shows the total amount of memory by region type. Individual regions are grouped by region type and show their contribution to the type's overall usage statistics. This view is primarily useful as an overview of how a process' memory is being used, and it is recommended that special attention is paid to the "dirty" sizes, as these represent memory that must be paged to disk under memory pressure on Mac OS X and are completely unreclaimable memory on iOS.
2. __Regions Map view__ - This view displays the regions in the target process individually by address, showing type, address, protections, and sizes for the regions. This view helps reveal the layout of regions in the process' address space and provides similar information as the command-line tool `vmmap`—for more details about this tool, see the `vmmap` man page (`man 1 vmmap`). Each region's address field in the Regions Map view has a focus button; focusing on a region will provide a list of pages in that region along with whether or not they're resident, dirty, speculative, or swapped.

The track view for the VM Tracker instrument shows a stacked display of Dirty and Resident sizes, with an alternate display available for showing the number of regions in the process.

### Instrumentation Impact

VM Tracker is completely external to the target process and gathers its information by periodically taking a snapshot of the process' virtual memory. This means that it doesn't interfere with the target's execution except during the snapshotting period; while a snapshot is being taken, the target must be completely suspended.

### Usage

This instrument is now included in the "Object Allocations" template to help provide a high-level view of a process' total active memory usage; the ObjectAlloc instrument in this template tracks `malloc` type memory exclusively. However, due to the necessary suspension of the target's execution for the duration of the snapshot, the "Automatically Snapshot" feature of the VM Tracker instrument is off by default in this template. Users wishing to acquire information with this instrument will need to manually click "Snapshot Now" or enable the automatic snapshot feature.

### Also...

VM Tracker is also available from the Instruments library and can be added to any document when targeting a single process on Mac OS X, the iOS, or the iOS Simulator platforms. When added from the library, the "Automatically Snapshot" feature is enabled by default with a starting interval of snapshotting every three seconds.

For more information, consult the man pages for `vmmap(1)`, `mmap(2)`, and the headers `<mach/vm_map.h>`, `<mach/vm_statistics.h>`.
