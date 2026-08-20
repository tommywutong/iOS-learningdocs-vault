---
title: Audio Unit Hosting Guide for iOS
apple_id: TP40009492
resource_type: Guide
platform: tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioUnitHostingGuide_iOS/ConstructingAudioUnitApps/ConstructingAudioUnitApps.html
archived_at: '2026-07-15T08:17:18.470560Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Unit Hosting Guide for iOS](About%20Audio%20Unit%20Hosting.md)


[Next](Using%20Specific%20Audio%20Units.md)[Previous](Audio%20Unit%20Hosting%20Fundamentals.md)

# Constructing Audio Unit Apps

Now that you understand how audio unit hosting works, as explained in [Audio Unit Hosting Fundamentals](Audio%20Unit%20Hosting%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmznknltcmi), you are well prepared to build the audio unit portion of your app. The main steps are choosing a design pattern and then writing the code to implement that pattern.

There are a half dozen basic design patterns for hosting audio units in an iOS app. Begin by picking the one that most closely represents what you want your app to do with audio. As you learn each pattern, notice the common features. Every pattern:

- Has exactly one I/O unit.
- Uses a single audio stream format throughout the audio processing graph—although there can be variations on that format, such as mono and stereo streams feeding a mixer unit.
- Requires that you set the stream format, or portions of the stream format, at specific locations.

Setting stream formats correctly is essential to establishing audio data flow. Most of these patterns rely on automatic propagation of audio stream formats from source to destination, as provided by an audio unit connection. Take advantage of this propagation when you can because it reduces the amount of code to write and maintain. At the same time, be sure that you understand where it is required for you to set stream formats. For example, you must set the full stream format on the input _and_ output of an iPod EQ unit. Refer to the usage tables in [Using Specific Audio Units](Using%20Specific%20Audio%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmjxfvjvomi) for all iOS audio unit stream format requirements.

In most cases, the design patterns in this chapter employ an audio processing graph (of type [AUGraph](https://developer.apple.com/documentation/audiotoolbox/augraph)). You could implement any one of these patterns without using a graph, but using one simplifies the code and supports dynamic reconfiguration, as described in [Audio Processing Graphs Manage Audio Units](Audio%20Unit%20Hosting%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmznknltemy).

The I/O pass-through pattern sends incoming audio directly to the output hardware, with no option to work with the audio data. Although this isn’t of much practical value, building an audio unit hosting app based on this pattern is a good way to verify and cement your understanding of audio unit concepts. Figure 2-1 illustrates this pattern.

__Figure 2-1__  Simultaneous I/O pass through

!

As you can see in the figure, the audio input hardware imposes its stream format on the outward-facing side of the Remote I/O unit’s input element. You, in turn, specify the format that you want to use on the inward-facing side of this element. The audio unit performs format conversion as needed. To avoid unnecessary sample rate conversion, be sure to use the audio hardware sample rate when defining your stream format.

The input element is disabled by default, so be sure to enable it; otherwise, audio cannot flow.

The pattern shown in Figure 2-1 takes advantage of the audio unit connection between the two Remote I/O elements. Specifically, you do not set a stream format on the input scope of the audio unit’s output element. The connection propagates the format you specified for the input element.

The outward-facing side of the output element takes on the audio output hardware’s stream format, and the output element performs format conversion for the outgoing audio as needed.

Using this pattern, you need not configure any audio data buffers.

Adding one or more other audio units between the Remote I/O unit’s elements lets you construct a more interesting app. For example, you could use a Multichannel Mixer unit to position the incoming microphone audio in a stereo field or to provide output volume control. In this design pattern, there is still no callback function in play, as shown in Figure 2-2. This simplifies the pattern but limits its utility. Without a render callback function you don’t have a means to manipulate the audio directly.

__Figure 2-2__  Simultaneous I/O without a render callback function

!!

In this pattern, you configure both elements of the Remote I/O unit just as you do in the pass-through pattern. To set up the Multichannel Mixer unit, you must set the sample rate of your stream format on the mixer output, as indicated in Figure 2-2.

The mixer’s input stream format is established automatically by propagation from the output of the Remote I/O unit’s input element, by way of the audio unit connection. Similarly, the stream format for the input scope of the Remote I/O unit’s output element is established by the audio unit connection, thanks to propagation from the mixer unit output.

In any instance of this pattern—indeed, whenever you use other audio units in addition to an I/O unit—you must set the [kAudioUnitProperty_MaximumFramesPerSlice](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_maximumframesperslice) property as described in _[Audio Unit Properties Reference](https://developer.apple.com/documentation/audiounit/audio_unit_properties)_.

As with the pass-through pattern, you need not configure any audio data buffers.

By placing a render callback function between the input and output elements of a Remote I/O unit, you can manipulate incoming audio before it reaches the output hardware. In a very simple case, you could use the render callback function to adjust output volume. However, you could add tremolo, ring-modulation, echo, or other effects. By making use of the Fourier transforms and convolution functions available in the Accelerate framework (see _[Accelerate Framework Reference](https://developer.apple.com/documentation/accelerate)_), your possibilities are endless. This pattern is depicted in Figure 2-3.

__Figure 2-3__  Simultaneous I/O with a render callback function

!

As you can see in the figure, this pattern uses both elements of the Remote I/O unit, as in the previous patterns in this chapter. Attach your render callback function to the input scope of the output element. When that element needs another set of audio sample values, it invokes your callback. Your callback, in turn, obtains fresh samples by invoking the render callback function of the Remote I/O unit’s input element.

Just as for the other I/O patterns, you must explicitly enable input on the Remote I/O unit, because input is disabled by default. And, as for the other I/O patterns, you need not configure any audio data buffers.

Notice that when you establish an audio path from one audio unit to another using a render callback function, as in this pattern, the callback takes the place of an audio unit connection.

Choose this pattern for musical games and synthesizers—apps for which you are generating sounds and need maximum responsiveness. At its simplest, this pattern involves one render callback function connected directly to the input scope of a Remote I/O unit’s output element, as shown in Figure 2-4.

__Figure 2-4__  Output-only with a render callback function

!

You can use this same pattern to build an app with a more complex audio structure. For example, you might want to generate several sounds, mix them together, and then play them through the device’s output hardware. Figure 2-5 shows such a case. Here, the pattern employs an audio processing graph and two additional audio units, a Multichannel Mixer and an iPod EQ.

__Figure 2-5__  A more complex example of output-only with a render callback function

!!

In the figure, notice that the iPod EQ requires you to set your full stream format on both input and output. The Multichannel Mixer, on the other hand, needs only the correct sample rate to be set on its output. The full stream format is then propagated by the audio unit connection from the mixer’s output to the input scope of the Remote I/O unit’s output element. These usage details, and other specifics of using the various iOS audio units, are described in [Using Specific Audio Units](Using%20Specific%20Audio%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmjxfvjvomi).

For each of the Multichannel Mixer unit inputs, as you see in Figure 2-5, the full stream format is set. For input 0, you set it explicitly. For input 1, the format is propagated by the audio unit connection from the output of the iPod EQ unit. In general, you must account for the stream-format needs of each audio unit individually.

There are two other main design patterns for audio units hosting. To record or analyze audio, create an input-only app with a render callback function. The callback function is invoked by your application, and it in turn invokes the render method of the Remote I/O unit’s input element. However, in most cases, a better choice for an app like this is to use an input audio queue object (of type [AudioQueueRef](https://developer.apple.com/documentation/audiotoolbox/audioqueueref) instantiated using the [AudioQueueNewInput](https://developer.apple.com/documentation/audiotoolbox/1501687-audioqueuenewinput) function), as explained in _[Audio Queue Services Programming Guide](../Audio%20Queue%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbt)_. Using an audio queue object provides a great deal more flexibility because its render callback function is not on a realtime thread.

To perform offline audio processing, use a Generic Output unit. Unlike the Remote I/O unit, this audio unit does not connect to the device’s audio hardware. When you use it to send audio to your application, it depends on your application to invoke its render method.

No matter which design pattern you choose, the steps for constructing an audio unit hosting app are basically the same:

1. Configure your audio session.
2. Specify audio units.
3. Create an audio processing graph, then obtain the audio units.
4. Configure the audio units.
5. Connect the audio unit nodes.
6. Provide a user interface.
7. Initialize and then start the audio processing graph.

The first step in building an audio unit application is the same step as for any iOS audio application: You configure the audio session. The characteristics of the audio session largely determine your app’s audio capabilities as well as its interactivity with the rest of the system. Start by specifying the sample rate you want to use in your application, as shown here:

```
self.graphSampleRate = 44100.0; // Hertz
```

Next, employ the audio session object to request that the system use your preferred sample rate as the device hardware sample rate, as shown in Listing 2-1. The intent here is to avoid sample rate conversion between the hardware and your app. This maximizes CPU performance and sound quality, and minimizes battery drain.

__Listing 2-1__  Configuring an audio session

```
NSError *audioSessionError = nil;
AVAudioSession *mySession = [AVAudioSession sharedInstance];     // 1
[mySession setPreferredHardwareSampleRate: graphSampleRate       // 2
                                    error: &audioSessionError];
[mySession setCategory: AVAudioSessionCategoryPlayAndRecord      // 3
                                    error: &audioSessionError];
[mySession setActive: YES                                        // 4
               error: &audioSessionError];
self.graphSampleRate = [mySession currentHardwareSampleRate];    // 5
```

The preceding lines do the following:

1. Obtain a reference to the singleton audio session object for your application.
2. Request a hardware sample rate. The system may or may not be able to grant the request, depending on other audio activity on the device.
3. Request the audio session category you want. The “play and record” category, specified here, supports audio input and output.
4. Request activation of your audio session.
5. After audio session activation, update your own sample rate variable according to the actual sample rate provided by the system.

There’s one other hardware characteristic you may want to configure: audio hardware I/O buffer duration. The default duration is about 23 ms at a 44.1 kHz sample rate, equivalent to a slice size of 1,024 samples. If I/O latency is critical in your app, you can request a smaller duration, down to about 0.005 ms (equivalent to 256 samples), as shown here:

```
self.ioBufferDuration = 0.005;
[mySession setPreferredIOBufferDuration: ioBufferDuration
                                  error: &audioSessionError];
```

For a complete explanation of how to configure and use the audio session object, see _[Audio Session Programming Guide](../../Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_.

At runtime, after your audio session configuration code has run, your app has not yet acquired audio units. You specify each one that you want by using an [AudioComponentDescription](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription) structure. See [Use Identifiers to Specify and Obtain Audio Units](Audio%20Unit%20Hosting%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmznknltcoi) for how to do this. The identifier keys for each iOS audio unit are listed in [Identifier Keys for Audio Units](Using%20Specific%20Audio%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmjxfvjvomju).

Audio unit specifiers in hand, you then build an audio processing graph according to the pattern you’ve picked.

In this step, you create the skeleton of one of the design patterns explained in the first part of this chapter. Specifically, you:

1. Instantiate an [AUGraph](https://developer.apple.com/documentation/audiotoolbox/augraph) opaque type. The instance represents the audio processing graph.
2. Instantiate one or more [AUNode](https://developer.apple.com/documentation/audiotoolbox/aunode) opaque types, each of which represents one audio unit in the graph.
3. Add the nodes to the graph.
4. Open the graph and instantiate the audio units.
5. Obtain references to the audio units.

Listing 2-2 shows how to perform these steps for a graph that contains a Remote I/O unit and a Multichannel Mixer unit. It assumes you’ve already defined an [AudioComponentDescription](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription) structure for each of these audio units.

__Listing 2-2__  Building an audio processing graph

```
AUGraph processingGraph;
NewAUGraph (&processingGraph);

AUNode ioNode;
AUNode mixerNode;

AUGraphAddNode (processingGraph, &ioUnitDesc, &ioNode);
AUGraphAddNode (processingGraph, &mixerDesc, &mixerNode);
```

The [AUGraphAddNode](https://developer.apple.com/documentation/audiotoolbox/1501671-augraphaddnode) function calls make use of the audio unit specifiers _ioUnitDesc_ and _mixerDesc_. At this point, the graph is instantiated and owns the nodes that you’ll use in your app. To open the graph and instantiate the audio units, call [AUGraphOpen](https://developer.apple.com/documentation/audiotoolbox/1502571-augraphopen):


```
AUGraphOpen (processingGraph);
```

Then, obtain references to the audio unit instances by way of the [AUGraphNodeInfo](https://developer.apple.com/documentation/audiotoolbox/1502407-augraphnodeinfo) function, as shown here:

```
AudioUnit ioUnit;
AudioUnit mixerUnit;

AUGraphNodeInfo (processingGraph, ioNode, NULL, &ioUnit);
AUGraphNodeInfo (processingGraph, mixerNode, NULL, &mixerUnit);
```

The `ioUnit` and `mixerUnit` variables now hold references to the audio unit instances in the graph, allowing you to configure and then interconnect the audio units.

Each iOS audio unit requires its own configuration, as described in [Using Specific Audio Units](Using%20Specific%20Audio%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmjxfvjvomi). However, some configurations are common enough that all iOS audio developers should be familiar with them.

The Remote I/O unit, by default, has output enabled and input disabled. If your app performs simultaneous I/O, or uses input only, you must reconfigure the I/O unit accordingly. For details, see the [kAudioOutputUnitProperty_EnableIO](https://developer.apple.com/documentation/audiotoolbox/1534116-i_o_audio_unit_properties/kaudiooutputunitproperty_enableio) property in _[Audio Unit Properties Reference](https://developer.apple.com/documentation/audiounit/audio_unit_properties)_.

All iOS audio units, with the exception of the Remote I/O and Voice-Processing I/O units, need their `kAudioUnitProperty_MaximumFramesPerSlice` property configured. This property ensures that the audio unit is prepared to produce a sufficient number of frames of audio data in response to a render call. For details, see [kAudioUnitProperty_MaximumFramesPerSlice](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_maximumframesperslice) in _[Audio Unit Properties Reference](https://developer.apple.com/documentation/audiounit/audio_unit_properties)_.

All audio units need their audio stream format defined on input, output, or both. For an explanation of audio stream formats, see [Audio Stream Formats Enable Data Flow](Audio%20Unit%20Hosting%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmznknltima). For the specific stream format requirements of the various iOS audio units, see [Using Specific Audio Units](Using%20Specific%20Audio%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmjxfvjvomi).

For design patterns that employ render callback functions, you must write those functions and then attach them at the correct points. [Render Callback Functions Feed Audio to Audio Units](Audio%20Unit%20Hosting%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmznknlteny) describes what these callbacks do and explains how they work. For examples of working callbacks, view the various audio unit sample code projects in the iOS Reference Library including _Audio Mixer (MixerHost)_ and _[aurioTouch](../../../samplecode/aurioTouch/aurioTouch.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonzxga)_, and _SynthHost_.

When audio is not flowing, you can attach a render callback immediately by using the audio unit API, as shown in Listing 2-3.

__Listing 2-3__  Attaching a render callback immediately

```
AURenderCallbackStruct callbackStruct;
callbackStruct.inputProc        = &renderCallback;
callbackStruct.inputProcRefCon  = soundStructArray;

AudioUnitSetProperty (
    myIOUnit,
    kAudioUnitProperty_SetRenderCallback,
    kAudioUnitScope_Input,
    0,                 // output element
    &callbackStruct,
    sizeof (callbackStruct)
);
```

You can attach a render callback in a thread-safe manner, even when audio is flowing, by using the audio processing graph API. Listing 2-4 shows how.

__Listing 2-4__  Attaching a render callback in a thread-safe manner

```
AURenderCallbackStruct callbackStruct;
callbackStruct.inputProc        = &renderCallback;
callbackStruct.inputProcRefCon  = soundStructArray;

AUGraphSetNodeInputCallback (
    processingGraph,
    myIONode,
    0,                 // output element
    &callbackStruct
);
// ... some time later
Boolean graphUpdated;
AUGraphUpdate (processingGraph, &graphUpdated);
```


In most cases, it’s best—and easier—to establish or break connections between audio units using the [AUGraphConnectNodeInput](https://developer.apple.com/documentation/audiotoolbox/1502636-augraphconnectnodeinput) and [AUGraphDisconnectNodeInput](https://developer.apple.com/documentation/audiotoolbox/1502008-augraphdisconnectnodeinput) functions in the audio processing graph API. These functions are thread-safe and avoid the coding overhead of defining connections explicitly, as you must do when not using a graph.

Listing 2-5 shows how to connect the output of a mixer node to the input of an I/O unit output element using the audio processing graph API.

__Listing 2-5__  Connecting two audio unit nodes using the audio processing graph API

```
AudioUnitElement mixerUnitOutputBus  = 0;
AudioUnitElement ioUnitOutputElement = 0;

AUGraphConnectNodeInput (     processingGraph,     mixerNode,           // source node     mixerUnitOutputBus,  // source node bus     iONode,              // destination node     ioUnitOutputElement  // desinatation node element );
```

You can, alternatively, establish and break connections between audio units directly by using the audio unit property mechanism. To do so, use the [AudioUnitSetProperty](https://developer.apple.com/documentation/audiotoolbox/1440371-audiounitsetproperty) function along with the [kAudioUnitProperty_MakeConnection](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_makeconnection) property, as shown in Listing 2-6. This approach requires that you define an [AudioUnitConnection](https://developer.apple.com/documentation/audiotoolbox/audiounitconnection) structure for each connection to serve as its property value.

__Listing 2-6__  Connecting two audio units directly

```
AudioUnitElement mixerUnitOutputBus  = 0;
AudioUnitElement ioUnitOutputElement = 0;

AudioUnitConnection mixerOutToIoUnitIn;
mixerOutToIoUnitIn.sourceAudioUnit    = mixerUnitInstance;
mixerOutToIoUnitIn.sourceOutputNumber = mixerUnitOutputBus;
mixerOutToIoUnitIn.destInputNumber    = ioUnitOutputElement;

AudioUnitSetProperty (
    ioUnitInstance,                     // connection destination
    kAudioUnitProperty_MakeConnection,  // property key
    kAudioUnitScope_Input,              // destination scope
    ioUnitOutputElement,                // destination element
    &mixerOutToIoUnitIn,                // connection definition
    sizeof (mixerOutToIoUnitIn)
);
```


At this point in constructing your app, the audio units—and, typically, the audio processing graph—are fully built and configured. In many cases, you’ll then want to provide a user interface to let your users fine-tune the audio behavior. You tailor the user interface to allow the user to adjust specific audio unit parameters and, in some unusual cases, audio unit properties. In either case, the user interface should also provide visual feedback regarding the current settings.

[Use Parameters and UIKit to Give Users Control](Audio%20Unit%20Hosting%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmznknltemi) explains the basics of constructing a user interface to let a user control a parameter value. For a working example, view the sample code project _Audio Mixer (MixerHost)_.

The iPod EQ unit is one of the unusual cases in that, to change its active equalization curve, you change the value of the [kAudioUnitProperty_PresentPreset](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_presentpreset) property. You can do this whether or not audio is running. For a working example, view the sample code project _[Mixer iPodEQ AUGraph Test](../../../samplecode/Mixer%20iPodEQ%20AUGraph%20Test/Mixer%20iPodEQ%20AUGraph%20Test.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnjvgu)_.

Before you can start audio flow, an audio processing graph must be initialized by calling the [AUGraphInitialize](https://developer.apple.com/documentation/audiotoolbox/1503251-augraphinitialize) function. This critical step:

- Initializes the audio units owned by the graph by automatically invoking the [AudioUnitInitialize](https://developer.apple.com/documentation/audiotoolbox/1439851-audiounitinitialize) function individually for each one. (If you were to construct a processing chain without using a graph, you would have to explicitly initialize each audio unit in turn.)
- Validates the graph’s connections and audio data stream formats.
- Propagates stream formats across audio unit connections.

Listing 2-7 shows how to use [AUGraphInitialize](https://developer.apple.com/documentation/audiotoolbox/1503251-augraphinitialize).

__Listing 2-7__  Initializing and starting an audio processing graph

```
OSStatus result = AUGraphInitialize (processingGraph);
// Check for error. On successful initialization, start the graph...
AUGraphStart (processingGraph);

// Some time later
AUGraphStop (processingGraph);
```


Whenever a Core Audio function provides a return value, capture that value and check for success or failure. On failure, make use of Xcode’s debugging features as described in _[Xcode Debugging Guide](../../Developer%20Tools/Xcode%20Debugging%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjx)_. If using an Objective-C method in your app, such as for configuring your audio session, take advantage the _error_ parameter in the same way.

Be aware of dependencies between function calls. For example, you can start an audio processing graph only after you successfully initialize it. Check the return value of `AUGraphInitialize`. If the function returns successfully, you can start the graph. If it fails, determine what went wrong. Check that all of your audio unit function calls leading up to initialization returned successfully. For an example of how to do this, look at the `-configureAndInitializeAudioProcessingGraph` method in the sample code project _Audio Mixer (MixerHost)_.

Second, if graph initialization is failing, take advantage of the [CAShow](https://developer.apple.com/documentation/audiotoolbox/1475988-cashow) function. This function prints out the state of the graph to the Xcode console. The sample code project _Audio Mixer (MixerHost)_ demonstrates this technique as well.

Ensure that you are initializing each of your [AudioStreamBasicDescription](https://developer.apple.com/documentation/coreaudio/audiostreambasicdescription) structures to 0, as follows:

```
AudioStreamBasicDescription stereoStreamFormat = {0};
```

Initializing the fields of an ASBD to 0 ensures that no fields contain garbage data. (In the case of declaring a data structure in external storage—for example, as an instance variable in a class declaration—its fields are automatically initialized to 0 and you need not initialize them yourself.)

To print out the field values of an `AudioStreamBasicDescription` structure to the Xcode console, which can be very useful during development, use code like that shown in Listing 2-8.

__Listing 2-8__  A utility method to print field values for an `AudioStreamBasicDescription` structure

```objc
- (void) printASBD: (AudioStreamBasicDescription) asbd {

    char formatIDString[5];
    UInt32 formatID = CFSwapInt32HostToBig (asbd.mFormatID);
    bcopy (&formatID, formatIDString, 4);
    formatIDString[4] = '\0';

    NSLog (@"  Sample Rate:         %10.0f",  asbd.mSampleRate);
    NSLog (@"  Format ID:           %10s",    formatIDString);
    NSLog (@"  Format Flags:        %10X",    asbd.mFormatFlags);
    NSLog (@"  Bytes per Packet:    %10d",    asbd.mBytesPerPacket);
    NSLog (@"  Frames per Packet:   %10d",    asbd.mFramesPerPacket);
    NSLog (@"  Bytes per Frame:     %10d",    asbd.mBytesPerFrame);
    NSLog (@"  Channels per Frame:  %10d",    asbd.mChannelsPerFrame);
    NSLog (@"  Bits per Channel:    %10d",    asbd.mBitsPerChannel);
}
```

This utility method can quickly reveal problems in an ASBD.

When defining an ASBD for an audio unit stream format, take care to ensure you are following the "Recommended stream format attributes” and “Stream format notes” in the usage tables in [Using Specific Audio Units](Using%20Specific%20Audio%20Units.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojsfvbuqmjxfvjvomi). Do not deviate from those recommendations unless you have a specific reason to.

[Next](Using%20Specific%20Audio%20Units.md)[Previous](Audio%20Unit%20Hosting%20Fundamentals.md)

