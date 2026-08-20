---
title: Audio Session Programming Guide
apple_id: TP40007875
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/OptimizingForDeviceHardware/OptimizingForDeviceHardware.html
archived_at: '2026-07-15T05:20:48.160153Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Session Programming Guide](Introduction.md)


[Next](Protecting%20User%20Privacy.md)[Previous](Responding%20to%20Route%20Changes.md)

# Configuring Device Hardware

Using audio session properties, you can optimize your app’s audio behavior for device hardware at runtime. Doing this lets your code adapt to the characteristics of the device it’s running on, as well as to changes made by the user (such as plugging in a headset or docking the device) as your app runs.

Use `AVAudioSession` to:

- Specify your preferred hardware settings for sample rate and I/O buffer duration
- Query many hardware characteristics, such as input and output latency, input and output channel count, hardware sample rate, hardware volume setting, and availability of audio input

Use the audio session to specify your preferred device settings, such as sample rate and hardware I/O buffer duration. Table 5-1 describes the benefits and costs of these preferences.

__Table 5-1__  Choosing preferred hardware values

| Setting | Preferred sample rate | Preferred I/O buffer duration |
| _High value_ | _Example: 48 kHz_  __+__ High audio quality  __–__ Large file or buffer size | _Example: 500 mS_  __+__ Less-frequent file access  __–__ Longer latency |
| _Low value_ | _Example: 8 kHz_  __+__ Small file or buffer size  __–__ Low audio quality | _Example: 5 mS_  __+__ Low latency  __–__ Frequent file access |

For example, you might specify a preference for a high sample rate if audio quality is very important in your app, and if large file or buffer size is not a significant issue.

Set preferred hardware values before you activate your audio session. If you're already running an audio session, deactivate it. Changes to preferred values take effect after the audio session is activated, and you can verify the changes at that time. Listing 5-1 shows how to set preferred hardware values and how to verify them.

__Listing 5-1__  Setting and verifying audio hardware values

```
let session = AVAudioSession.sharedInstance()

// Configure category and mode
do {
    try session.setCategory(AVAudioSessionCategoryRecord, mode: AVAudioSessionModeDefault)
} catch let error as NSError {
    print("Unable to set category:  \(error.localizedDescription)")
}

// Set preferred sample rate
do {
    try session.setPreferredSampleRate(44_100)
} catch let error as NSError {
    print("Unable to set preferred sample rate:  \(error.localizedDescription)")
}

// Set preferred I/O buffer duration
do {
    try session.setPreferredIOBufferDuration(0.005)
} catch let error as NSError {
    print("Unable to set preferred I/O buffer duration:  \(error.localizedDescription)")
}

// Activate the audio session
do {
    try session.setActive(true)
} catch let error as NSError {
    print("Unable to activate session. \(error.localizedDescription)")
}

// Query the audio session's ioBufferDuration and sampleRate properties
// to determine if the preferred values were set
print("Audio Session ioBufferDuration: \(session.ioBufferDuration), sampleRate: \(session.sampleRate)")
```


On devices with two or more built-in microphones, iOS automatically selects a microphone through the use of audio session modes. A mode specifies the digital signal processing (DSP) used for input, and the possible routes. The input and routes are optimized for each mode's use case. Setting a mode may also affect other aspects of the route being used.

Developers can also manually select microphones and even select a preferred microphone polar pattern if the hardware supports it.

To discover built-in or connected input ports, use the audio session’s [availableInputs](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616557-availableinputs) property. This property returns an array of [AVAudioSessionPortDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription) objects that describe the device’s available input ports. Ports can be identified by their [portType](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616445-porttype) property. To set a preferred input port (built-in microphone, wired microphone, USB input, and so on) use the audio session’s [setPreferredInput:error:](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616491-setpreferredinput) method.

Some ports, such as the built-in microphone and some USB accessories, support data sources. Apps can discover available data sources by querying the port description’s [dataSources](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616570-datasources) property. In the case of the built-in microphone, the returned data source description objects represent each individual microphone. Different devices return different values for the built-in mic. For instance, the iPhone 4 and iPhone 4S have two microphones: bottom and top. The iPhone 5 has three microphones: bottom, front, and back.

Individual built-in microphones may be identified by a combination of a data source description’s [location](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616495-location) property (upper, lower) and [orientation](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616456-orientation) property (front, back, and so on). Apps may set a preferred data source by using the [setPreferredDataSource:error:](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616554-setpreferreddatasource) method of an `AVAudioSessionPortDescription` object.

Some iOS devices support configuring microphone polar patterns for some of the built-in microphones. A microphone’s polar pattern defines its sensitivity to sound relative to the direction of the sound source. Current-generation iPhones support setting the preferred polar pattern for the front and back built-in microphones. Available patterns are returned using the [supportedPolarPatterns](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616450-supportedpolarpatterns) property of a data source description object. This property returns either an array of supported polar patterns for the data source, such as cardioid or omnidirectional, or `nil` when no selectable patterns are available. If the data source has a number of supported polar patterns, you can set the preferred polar pattern by using the data source description’s [setPreferredPolarPattern:error:](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616516-setpreferredpolarpattern) method.

The following code provides a simple example illustrating how to select a particular microphone and set its polar pattern.

```swift
// Preferred Mic = Front, Preferred Polar Pattern = Cardioid
let preferredMicOrientation = AVAudioSessionOrientationFront
let preferredPolarPattern = AVAudioSessionPolarPatternCardioid

// Retrieve your configured and activated audio session
let session = AVAudioSession.sharedInstance()

// Get available inputs
guard let inputs = session.availableInputs else { return }

// Find built-in mic
guard let builtInMic = inputs.first(where: {
    $0.portType == AVAudioSessionPortBuiltInMic
}) else { return }

// Find the data source at the specified orientation
guard let dataSource = builtInMic.dataSources?.first (where: {
    $0.orientation == preferredMicOrientation
}) else { return }

// Set data source's polar pattern
do {
    try dataSource.setPreferredPolarPattern(preferredPolarPattern)
} catch let error as NSError {
    print("Unable to preferred polar pattern: \(error.localizedDescription)")
}

// Set the data source as the input's preferred data source
do {
    try builtInMic.setPreferredDataSource(dataSource)
} catch let error as NSError {
    print("Unable to preferred dataSource: \(error.localizedDescription)")
}

// Set the built-in mic as the preferred input
// This call will be a no-op if already selected
do {
    try session.setPreferredInput(builtInMic)
} catch let error as NSError {
    print("Unable to preferred input: \(error.localizedDescription)")
}

// Print Active Configuration
session.currentRoute.inputs.forEach { portDesc in
    print("Port: \(portDesc.portType)")
    if let ds = portDesc.selectedDataSource {
        print("Name: \(ds.dataSourceName)")
        print("Polar Pattern: \(ds.selectedPolarPattern ?? "[none]")")
    }
}
```

Running this code on an iPhone 6s produces the following console output:

```
Port: MicrophoneBuiltIn
Name: Front
Polar Pattern: Cardioid
```


When you add audio session support to your app, you can run your app in Simulator or on a device. However, Simulator does not simulate most interactions between audio sessions in different processes or audio route changes. When running your app in Simulator, you cannot:

- Invoke an interruption
- Simulate plugging in or unplugging a headset
- Change the setting of the Silent switch
- Simulate screen lock
- Test audio mixing behavior—that is, playing your audio along with audio from another app (such as the Music app)

Because of the characteristics of Simulator, you may want to conditionalize your code to allow partial testing in Simulator. Listing 5-2 shows how to do this.

__Listing 5-2__  Using a conditional compilation block

```
#if arch(i386) || arch(x86_64)
    // Execute subset of code that works in the Simulator
#else
    // Execute device-only code as well as the other code
#endif
```

[Next](Protecting%20User%20Privacy.md)[Previous](Responding%20to%20Route%20Changes.md)

