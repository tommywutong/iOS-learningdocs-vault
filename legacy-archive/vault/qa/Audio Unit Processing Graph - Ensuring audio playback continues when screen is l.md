---
title: Audio Unit Processing Graph - Ensuring audio playback continues when screen
  is locked
apple_id: DTS40009413
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2010-03-15'
source_url: https://developer.apple.com/library/archive/qa/qa1606/_index.html
archived_at: '2026-07-18T02:32:42.009437Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1606

# Audio Unit Processing Graph - Ensuring audio playback continues when screen is locked

## Q:  I'm using an AUGraph and I'd like my audio to continue playing during screen lock. Is there anything else I need to configure in addition to the Audio Session kAudioSessionCategory_MediaPlayback category to allow my AURenderCallback to continue being called?

A: I'm using an AUGraph and I'd like my audio to continue playing during screen lock. Is there anything else I need to configure in addition to the Audio Session kAudioSessionCategory_MediaPlayback category to allow my AURenderCallback to continue being called?

When an Audio Unit Processing Graph is used for __Output__ only, the default I/O render size is changed from 22 milliseconds (1024 samples @ 44.1kHz) to 88 milliseconds (4096 samples @ 44.1kHz) when the screen is locked. This is done to conserve power since there is no user interaction with the screen once the screen goes dark.

If an application does not account for this change, any Audio Unit asked to provide 4096 samples will return an error since its `kAudioUnitProperty_MaximumFramesPerSlice` setting will be less than this value.

The Remote I/O Audio Unit by default is already configured for 4096 maximum frames per slice, the issue affects all other Audio Units used in the graph.

If an application intends to continue playback when the screen is locked, it is the clients responsibility to change the `kAudioUnitProperty_MaximumFramesPerSlice` property appropriately for each Audio Unit being used to handle requests for 4096 samples.

__Listing 1__  Typical Audio Unit Graph setup configuring the kAudioUnitProperty_MaximumFramesPerSlice property for the mixer.

```
// audio render procedure static OSStatus renderProc(void *inRefCon, AudioUnitRenderActionFlags *ioActionFlags,                            const AudioTimeStamp *inTimeStamp, UInt32 inBusNumber,                            UInt32 inNumberFrames, AudioBufferList *ioData) {     // your audio render code here      return noErr; }  AUGraph   mGraph; AudioUnit mMixer;  - (void)initializeAUGraph {     // create two AudioComponentDescriptions for the AUs we want in the graph     // output unit     AudioComponentDescription output_desc = {kAudioUnitType_Output, kAudioUnitSubType_RemoteIO,                                              kAudioUnitManufacturer_Apple, 0, 0};      // multichannel mixer unit     AudioComponentDescription mixer_desc = {kAudioUnitType_Mixer, kAudioUnitSubType_MultiChannelMixer,                                             kAudioUnitManufacturer_Apple, 0, 0};     AUNode outputNode;     AUNode mixerNode;     CAStreamBasicDescription desc;      // create a new AUGraph     NewAUGraph(&mGraph);      // create a node in the graph that is an AudioUnit, using the supplied AudioComponentDescription     // to find and open that unit     AUGraphAddNode(mGraph, &output_desc, &outputNode);     AUGraphAddNode(mGraph, &mixer_desc, &mixerNode);      // connect a node's output to a node's input     AUGraphConnectNodeInput(mGraph, mixerNode, 0, outputNode, 0);      // open the graph AudioUnits are open but not initialized (no resource allocation occurs here)     AUGraphOpen(mGraph);      // get the mixer audio unit since we need to configure it     AUGraphNodeInfo(mGraph, mixerNode, NULL, &mMixer);      // set bus count     UInt32 numbuses = 1;      AudioUnitSetProperty(mMixer, kAudioUnitProperty_ElementCount, kAudioUnitScope_Input, 0, &numbuses,                          sizeof(numbuses));      // setup render callback struct     AURenderCallbackStruct rcbs;     rcbs.inputProc = &renderProc;     rcbs.inputProcRefCon = self;      // Set a callback for the specified node's specified input     AUGraphSetNodeInputCallback(mGraph, mixerNode, 0, &rcbs);      // set input stream format to what we want     UInt32 size = sizeof(desc);     AudioUnitGetProperty(mMixer, kAudioUnitProperty_StreamFormat, kAudioUnitScope_Input, 0, &desc, &size);      desc.ChangeNumberChannels(2, false);      desc.mSampleRate = 44100.0;      AudioUnitSetProperty(mMixer, kAudioUnitProperty_StreamFormat, kAudioUnitScope_Input, 0, &desc,                          sizeof(desc));      // set output stream format to what we want     AudioUnitGetProperty(mMixer, kAudioUnitProperty_StreamFormat, kAudioUnitScope_Output, 0, &desc, &size);      desc.ChangeNumberChannels(2, false);      desc.mSampleRate = 44100.0;      AudioUnitSetProperty(mMixer, kAudioUnitProperty_StreamFormat, kAudioUnitScope_Output, 0, &desc,                          sizeof(desc));      // set the mixer unit to handle 4096 samples per slice since we want to keep rendering during screen lock     UInt32 maxFPS = 4096;     AudioUnitSetProperty(mMixer, kAudioUnitProperty_MaximumFramesPerSlice, kAudioUnitScope_Global, 0,                          &maxFPS, sizeof(maxFPS));      // now that we've set everything up we can initialize the graph, this will also validate the connections     AUGraphInitialize(mGraph); }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-03-15 | Editorial. |
| 2010-01-14 | Corrected value for default AU maximum frames per slice. |
| 2009-12-14 | Editorial |
| 2009-12-09 | New document that discusses how to ensure audio playback while the phone is locked when using multiple Audio Units. |

