---
title: AVAudioSession - Microphone Selection
apple_id: DTS40013720
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2014-01-21'
source_url: https://developer.apple.com/library/archive/qa/qa1799/_index.html
archived_at: '2026-07-18T02:34:51.766236Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1799

# AVAudioSession - Microphone Selection

## Q:  How can I choose a specific built-in microphone when recording?

A: iOS 6 automatically selects the choice of built-in microphone (on devices that have two or more built-in microphones) through the use of audio session modes. Modes affect possible routes and the digital signal processing used for input. It is important to note that they are optimized for the use case specified by each mode and setting a mode may also affect other aspects of the route being used. For example, when recording video setting the `AVAudioSessionModeVideoRecording` audio session mode will select the "top" microphone instead of the default "bottom" microphone on iPhone 4/4S, and on iPhone 5 the "front" and "back" microphones will be used to provide directional noise reduction through beam forming processing.

iOS 7 offers developers more flexibility in terms of selecting specific built-in microphones.

Using APIs introduced in iOS 7, developers can perform tasks such as locating a port description that represents the built-in microphone, locating specific microphones like the "front", "back" or "bottom", setting your choice of microphone as the preferred data source, setting the built-in microphone port as the preferred input and even selecting a preferred microphone polar pattern if the hardware supports it. See `AVAudioSession.h`.

To discover what input ports are connected (or built-in) use the `AVAudioSession` property `availableInputs`. This property returns an `NSArray` of `AVAudioSessionPortDescription` objects.


```objc
/* Get the set of input ports that are available for routing. Note that this property only applies to the session's current category and mode.
   For example, if the session's current category is AVAudioSessionCategoryPlayback, there will be no available inputs. */

@property(readonly) NSArray * availableInputs NS_AVAILABLE_IOS(7_0); /* NSArray of AVAudioSessionPortDescription objects. */
```


Ports (`AVAudioSessionPortDescription` objects) can be identified by their `portType` property, for example `AVAudioSessionPortBuiltInMic`, `AVAudioSessionPortHeadsetMic` and so on. See `AVAudioSession.h` for further details.

To set a preferred input port (built-in mic, wired mic, USB input, etc.) use the `AVAudioSession` `setPreferredInput:error:` method. This method takes a `AVAudioSessionPortDescription` object.


```objc
/* Select a preferred input port for audio routing. If the input port is already part of the current audio route, this will have no effect.
   Otherwise, selecting an input port for routing will initiate a route change to use the preferred input port, provided that the application's
   session controls audio routing. */

- (BOOL) setPreferredInput:(AVAudioSessionPortDescription*)inPort error:(NSError **)outError NS_AVAILABLE_IOS(7_0);
```


For ports that support data sources (built-in microphone, some USB accessories), applications can discover what data sources are available by querying the `AVAudioSessionPortDescription`'s `dataSources` property. In the case of "built-in microphone", the returned description represents each individual microphone. Different devices will return different data source information. The iPhone 4 and 4S have two microphones; "bottom" and "top". The iPhone 5 has 3 microphones; "bottom", "front", and "back".


```objc
/* Array of AVAudioSessionDataSourceDescription objects. Will be nil if there are no selectable data sources. */

@property(readonly) NSArray *	dataSources NS_AVAILABLE_IOS(7_0);
```

Individual built-in microphones may be identified by a combination of a `AVAudioSessionDataSourceDescription`'s `location` property (`AVAudioSessionLocationUpper`, `AVAudioSessionLocationLower`) and `orientation` property (`AVAudioSessionOrientationTop`, `AVAudioSessionOrientationFront` and so on). See AVAudioSession.h for further details.

Applications may set a preferred data source by using the `setPreferredDataSource:error:` method of a `AVAudioSessionPortDescription` object. This method takes a `AVAudioSessionDataSourceDescription` object.


```objc
/* Select the preferred data source for this port. The input dataSource parameter must be one of the dataSources exposed by the dataSources property.
Note: if the port is part of the active audio route, changing the data source will likely
result in a route reconfiguration. If the port is not part of the active route, selecting a new data source will
not result in an immediate route reconfiguration. Use AVAudioSession's setPreferredInput:error: method to activate the port. */

- (BOOL) setPreferredDataSource:(AVAudioSessionDataSourceDescription *)dataSource error:(NSError **)outError NS_AVAILABLE_IOS(7_0);
```


Some iOS devices support getting and setting microphone polar patterns for some of the built-in microphones. The iPhone 5 supports setting the preferred polar pattern for the "front" and "back" built-in microphones. Available patterns are returned using the `supportedPolarPatterns` property of a `AVAudioSessionDataSourceDescription`. This property will either return an array of supported polar patterns for the data source, for example `AVAudioSessionPolarPatternCardioid`, `AVAudioSessionPolarPatternOmnidirectional` and so on, or `nil` when no selectable patterns are available.


```objc
/* Array of one or more NSStrings describing the supported polar patterns for a data source. Will be nil for data sources that have no selectable patterns. */

@property(readonly) NSArray *	supportedPolarPatterns NS_AVAILABLE_IOS(7_0);
```


If the data source has a number of supported polar patters, you can set the preferred polar pattern by using the `AVAudioSessionDataSourceDescription`'s `setPreferredPolarPattern:error:` method.


```objc
/* Select the desired polar pattern from the set of available patterns. Note: if the owning port and data source are part of the active audio route,
   changing the polar pattern will likely result in a route reconfiguration. If the owning port and data source are not part of the active route,
   selecting a polar pattern will not result in an immediate route reconfiguration. Use AVAudioSession's setPreferredInput:error: method
   to activate the port. Use setPreferredDataSource:error: to active the data source on the port. */

- (BOOL) setPreferredPolarPattern:(NSString *)pattern error:(NSError **)outError NS_AVAILABLE_IOS(7_0);
```

Listing 1 demonstrates how applications can find the `AVAudioSessionPortDescription` that represents the built-in microphone, locate the front microphone (on iPhone 5 or another device that has a front facing microphone), set the front microphone as the preferred data source and set the built-in microphone port as the preferred input.

__Listing 1__  Demonstrate Input Selection.

```objc
#import <AVFoundation/AVAudioSession.h>

- (void) demonstrateInputSelection
{
    NSError* theError = nil;
    BOOL result = YES;

    AVAudioSession* myAudioSession = [AVAudioSession sharedInstance];

    result = [myAudioSession setCategory:AVAudioSessionCategoryPlayAndRecord error:&theError];
    if (!result)
    {
        NSLog(@"setCategory failed");
    }

    result = [myAudioSession setActive:YES error:&theError];
    if (!result)
    {
        NSLog(@"setActive failed");
    }

    // Get the set of available inputs. If there are no audio accessories attached, there will be
    // only one available input -- the built in microphone.
    NSArray* inputs = [myAudioSession availableInputs];

    // Locate the Port corresponding to the built-in microphone.
    AVAudioSessionPortDescription* builtInMicPort = nil;
    for (AVAudioSessionPortDescription* port in inputs)
    {
        if ([port.portType isEqualToString:AVAudioSessionPortBuiltInMic])
        {
            builtInMicPort = port;
            break;
        }
    }

    // Print out a description of the data sources for the built-in microphone
    NSLog(@"There are %u data sources for port :\"%@\"", (unsigned)[builtInMicPort.dataSources count], builtInMicPort);
    NSLog(@"%@", builtInMicPort.dataSources);

    // loop over the built-in mic's data sources and attempt to locate the front microphone
    AVAudioSessionDataSourceDescription* frontDataSource = nil;
    for (AVAudioSessionDataSourceDescription* source in builtInMicPort.dataSources)
    {
        if ([source.orientation isEqual:AVAudioSessionOrientationFront])
        {
            frontDataSource = source;
            break;
        }
    } // end data source iteration

    if (frontDataSource)
    {
        NSLog(@"Currently selected source is \"%@\" for port \"%@\"", builtInMicPort.selectedDataSource.dataSourceName, builtInMicPort.portName);
        NSLog(@"Attempting to select source \"%@\" on port \"%@\"", frontDataSource, builtInMicPort.portName);

        // Set a preference for the front data source.
        theError = nil;
        result = [builtInMicPort setPreferredDataSource:frontDataSource error:&theError];
        if (!result)
        {
            // an error occurred. Handle it!
            NSLog(@"setPreferredDataSource failed");
        }
    }

    // Make sure the built-in mic is selected for input. This will be a no-op if the built-in mic is
    // already the current input Port.
    theError = nil;
    result = [myAudioSession setPreferredInput:builtInMicPort error:&theError];
    if (!result)
    {
        // an error occurred. Handle it!
        NSLog(@"setPreferredInput failed");
    }

}
```

Listing 1 will produce the following console output when run on an iPhone 5:


```
There are 3 data sources for port :"<AVAudioSessionPortDescription: 0x14d935a0, type = MicrophoneBuiltIn; name = iPhone Microphone; UID = Built-In Microphone; selectedDataSource = Bottom>"
(
    "<AVAudioSessionDataSourceDescription: 0x14d93800, ID = 1835216945; name = Bottom>",
    "<AVAudioSessionDataSourceDescription: 0x14d938d0, ID = 1835216946; name = Front>",
    "<AVAudioSessionDataSourceDescription: 0x14d93a10, ID = 1835216947; name = Back>"
)
Currently selected source is "Bottom" for port "iPhone Microphone"
Attempting to select source "<AVAudioSessionDataSourceDescription: 0x14d938d0, ID = 1835216946; name = Front>" on port "iPhone Microphone”
```

To change the output side of the audio route, applications may include a `MPVolumeView` to easily give users access to the route picker.

Applications may set the audio session option `AVAudioSessionCategoryOptionDefaultToSpeaker` or use the `AVAudioSessionPortOverrideSpeaker` override for speakerphone functionality. See [Q&A QA1754](https://developer.apple.com/library/ios/qa/qa1754/_index.html#//apple_ref/doc/uid/DTS40011281) for details.

The preferred method for overriding to the speaker instead of the receiver for speakerphone functionality is through the use of `MPVolumeView`.

If an application uses the `setPreferredInput:error:` method to select a Bluetooth HFP input, the output will __automatically__ be changed to the Bluetooth HFP output. Moreover, selecting a Bluetooth HFP output using the `MPVolumeView`'s route picker will __automatically__ change the input to the Bluetooth HFP input. Therefore both the input and output will always end up on the Bluetooth HFP device even though only the input or output was set individually.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-01-21 | Editorial |
| 2013-09-03 | New document that describes how to choose a specific microphone "Front", "Bottom", "Rear" and so on when available on a device. |

