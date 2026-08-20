---
title: Audio Session Programming Guide
apple_id: TP40007875
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/RequestingPermission/RequestingPermission.html
archived_at: '2026-07-15T05:20:48.172574Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Session Programming Guide](Introduction.md)


[Next](Audio%20Guidelines%20By%20App%20Type.md)[Previous](Configuring%20Device%20Hardware.md)

# Protecting User Privacy

To protect user privacy, your app must ask and receive permission from the user before recording audio. If the user does not grant permission, then only silence is recorded. The system automatically prompts the user for permission when you use a category that supports recording and the app attempts to use an input route.

Instead of waiting for the system to prompt the user for permission to record, you can use the [requestRecordPermission:](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616601-requestrecordpermission) method to manually ask for permission. Using this method allows your app to get permission without interrupting the natural flow of the app, resulting in a better user experience.

```swift
AVAudioSession.sharedInstance().requestRecordPermission { granted in
    if granted {
        // User granted access. Present recording interface.
    } else {
        // Present message to user indicating that recording
        // can't be performed until they change their preference
        // under Settings -> Privacy -> Microphone
    }
}
```

[Next](Audio%20Guidelines%20By%20App%20Type.md)[Previous](Configuring%20Device%20Hardware.md)

