---
title: UNNotificationSound
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsound
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsound.json'
content_hash: 'sha256:64ccf0e48b55ec40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationSound

<sub>Class</sub>

The sound played upon delivery of a notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class UNNotificationSound
```

## Overview

Create a [UNNotificationSound](unnotificationsound.md) object when you want the system to play a specific sound when it delivers with your notification. To play the default system sound, create your sound object using the [defaultSound](unnotificationsound/default.md) method. If you want to play a custom sound, create a new sound object and specify the name of the audio file that you want to play.

For local notifications, assign the sound object to the [sound](unmutablenotificationcontent/sound.md) property of your [UNMutableNotificationContent](unmutablenotificationcontent.md) object. For a remote notification, assign the name of your sound file to the `sound` key in the `aps` dictionary. You can also use a notification service app extension to add a sound file to a notification shortly before delivery. In your extension, create a [UNNotificationSound](unnotificationsound.md) object and add it to your notification content in the same way that you’d for a local notification.

Audio files must already be on the user’s device before the system can play them. If you use a predefined set of sounds for your notifications, include the audio files in your app’s bundle. For all other sounds, the [UNNotificationSound](unnotificationsound.md) object looks only in the following locations:

- The `/Library/Sounds` directory of the app’s container directory.
- The `/Library/Sounds` directory of one of the app’s shared group container directories.
- The main bundle of the current executable.

### Prepare Sound Resources

The system sound facility plays custom alert sounds, so they must be in one of the following audio data formats:

- Linear PCM
- MA4 (IMA/ADPCM)
- µLaw
- aLaw

You can package the audio data in an `aiff`, `wav`, or `caf` file. Sound files must be less than 30 seconds in length. If the sound file is longer than 30 seconds, the system plays the default sound instead.

You can use the `afconvert` command-line tool to convert sounds. For example, to convert the system sound `Submarine.aiff` to IMA4 audio in a CAF file, use the following command in Terminal:

`afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v`

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating Notification Sounds

- [defaultSound](unnotificationsound/default.md) — Returns an object representing the default sound for notifications.
- [+ soundNamed:](<unnotificationsound/init(named_).md>) — Creates a sound object that represents a custom sound file.

### Getting Critical Sounds

- [defaultCriticalSound](unnotificationsound/defaultcritical.md) — The default sound used for critical alerts.
- [+ defaultCriticalSoundWithAudioVolume:](<unnotificationsound/defaultcriticalsound(withaudiovolume_).md>) — Creates a sound object that plays the default critical alert sound at the volume you specify.
- [+ criticalSoundNamed:](<unnotificationsound/criticalsoundnamed(__).md>) — Creates a custom sound object for critical alerts.
- [+ criticalSoundNamed:withAudioVolume:](<unnotificationsound/criticalsoundnamed(__withaudiovolume_).md>) — Creates a custom sound object for critical alerts with the volume you specify.

### Type Properties

- [defaultRingtoneSound](unnotificationsound/defaultringtone.md)

### Type Methods

- [+ ringtoneSoundNamed:](<unnotificationsound/ringtonesoundnamed(__).md>)

### Initializers

- [init(coder:)](<unnotificationsound/init(coder_).md>)

## See Also

### Notification content

- [Implementing communication notifications](implementing-communication-notifications.md) — Configure and display your app’s communication notifications by using intents.
- [UNNotificationContentProviding](unnotificationcontentproviding.md) — A protocol the system uses to provide context relevant to user notifications.
- [UNNotificationActionIcon](unnotificationactionicon.md) — An icon associated with an action.
- [UNMutableNotificationContent](unmutablenotificationcontent.md) — The editable content for a notification.
- [UNNotificationContent](unnotificationcontent.md) — The uneditable content of a notification.
- [UNNotificationAttachment](unnotificationattachment.md) — A media file associated with a notification.
- [UNNotificationSoundName](unnotificationsoundname.md) — A string providing the name of a sound file.
