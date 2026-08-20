---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/FWAUserLib.html
archived_at: '2026-07-18T02:52:24.376024Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# FWAUserLib Changes

## FWAUserLib

Added FWACreateDeviceRec.init()Added FWACreateDeviceRec.init(vendorID: UInt32, deviceName:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), guidStr:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added FWACreateFWAudioPlugRec.init()Added FWACreateFWAudioPlugRec.init(owningAudioStreamRef: UInt32, channelID: UInt32, plugName:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), plugIdent:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), plugIdentIsNull: Bool)Added FWACreateMIDIDeviceNubRec.init()Added FWACreateMIDIDeviceNubRec.init(owningDevice: UInt32, vendorID: UInt32, modelID: UInt32, deviceName:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), guidStr:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), iconFilePath:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), editorPath:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added FWACreateMIDIPlugRec.init()Added FWACreateMIDIPlugRec.init(owningMIDIStreamRef: UInt32, mpxID: UInt32, plugName:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), plugIdent:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), plugIdentIsNull: Bool)Added FWACreateStreamRec.init()Added FWACreateStreamRec.init(owningIsochStreamRef: UInt32, channelNumber: UInt32, direction: UInt32, numAudioChannels: UInt32, streamName:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), streamIdent:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), streamIdentIsNull: Bool)Added FWADeviceStatus.init()Added FWADeviceStatus.init(version: UInt32, sampleCounter: UInt32, inputSampleFrame: UInt32, outputSampleFrame: UInt32, inputClipSampleFrame: UInt32, outputClipSampleFrame: UInt32, meterData:(UInt32))Added FWAGetPropertyRec.init()Added FWAMIDIInputBufferWithTimeStamp.init()Added FWAMIDIInputBufferWithTimeStamp.init(timeStamp: UInt64, midiBuffer:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added FWAMIDIOutputBufferWithTimeStamp.init()Added FWAMIDIOutputBufferWithTimeStamp.init(timeStamp: UInt64, midiBuffer:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added FWAMIDIReadBuffer.init()Added FWAMIDIReadBuffer.init(bufSize: UInt32, mrBuf:(UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added FWASetPlugPropertyRec.init()Added FWASetPluginPathRec.init()Added FWASetPluginPathRec.init(owningEngineRef: UInt32, vendorID: UInt32, modelID: UInt32, pluginPath:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), pluginPathIsNull: Bool, cacheValues: Bool)Modified FWACreateDeviceRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWACreateDeviceRec {     var vendorID: UInt32     var deviceName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var guidStr: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct FWACreateDeviceRec {     var vendorID: UInt32     var deviceName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var guidStr: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(vendorID vendorID: UInt32, deviceName deviceName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), guidStr guidStr: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified FWACreateFWAudioPlugRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWACreateFWAudioPlugRec {     var owningAudioStreamRef: UInt32     var channelID: UInt32     var plugName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var plugIdent: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var plugIdentIsNull: Bool } ``` |
| To | ``` struct FWACreateFWAudioPlugRec {     var owningAudioStreamRef: UInt32     var channelID: UInt32     var plugName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var plugIdent: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var plugIdentIsNull: Bool     init()     init(owningAudioStreamRef owningAudioStreamRef: UInt32, channelID channelID: UInt32, plugName plugName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), plugIdent plugIdent: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), plugIdentIsNull plugIdentIsNull: Bool) } ``` |

Modified FWACreateMIDIDeviceNubRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWACreateMIDIDeviceNubRec {     var owningDevice: UInt32     var vendorID: UInt32     var modelID: UInt32     var deviceName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var guidStr: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var iconFilePath: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var editorPath: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ```  ``` |

Modified FWACreateMIDIPlugRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWACreateMIDIPlugRec {     var owningMIDIStreamRef: UInt32     var mpxID: UInt32     var plugName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var plugIdent: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var plugIdentIsNull: Bool } ``` |
| To | ``` struct FWACreateMIDIPlugRec {     var owningMIDIStreamRef: UInt32     var mpxID: UInt32     var plugName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var plugIdent: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var plugIdentIsNull: Bool     init()     init(owningMIDIStreamRef owningMIDIStreamRef: UInt32, mpxID mpxID: UInt32, plugName plugName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), plugIdent plugIdent: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), plugIdentIsNull plugIdentIsNull: Bool) } ``` |

Modified FWACreateStreamRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWACreateStreamRec {     var owningIsochStreamRef: UInt32     var channelNumber: UInt32     var direction: UInt32     var numAudioChannels: UInt32     var streamName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var streamIdent: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var streamIdentIsNull: Bool } ``` |
| To | ``` struct FWACreateStreamRec {     var owningIsochStreamRef: UInt32     var channelNumber: UInt32     var direction: UInt32     var numAudioChannels: UInt32     var streamName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var streamIdent: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var streamIdentIsNull: Bool     init()     init(owningIsochStreamRef owningIsochStreamRef: UInt32, channelNumber channelNumber: UInt32, direction direction: UInt32, numAudioChannels numAudioChannels: UInt32, streamName streamName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), streamIdent streamIdent: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), streamIdentIsNull streamIdentIsNull: Bool) } ``` |

Modified FWADeviceStatus [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWADeviceStatus {     var version: UInt32     var sampleCounter: UInt32     var inputSampleFrame: UInt32     var outputSampleFrame: UInt32     var inputClipSampleFrame: UInt32     var outputClipSampleFrame: UInt32     var meterData: (UInt32) } ``` |
| To | ``` struct FWADeviceStatus {     var version: UInt32     var sampleCounter: UInt32     var inputSampleFrame: UInt32     var outputSampleFrame: UInt32     var inputClipSampleFrame: UInt32     var outputClipSampleFrame: UInt32     var meterData: (UInt32)     init()     init(version version: UInt32, sampleCounter sampleCounter: UInt32, inputSampleFrame inputSampleFrame: UInt32, outputSampleFrame outputSampleFrame: UInt32, inputClipSampleFrame inputClipSampleFrame: UInt32, outputClipSampleFrame outputClipSampleFrame: UInt32, meterData meterData: (UInt32)) } ``` |

Modified FWAMIDIInputBufferWithTimeStamp [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWAMIDIInputBufferWithTimeStamp {     var timeStamp: UInt64     var midiBuffer: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct FWAMIDIInputBufferWithTimeStamp {     var timeStamp: UInt64     var midiBuffer: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(timeStamp timeStamp: UInt64, midiBuffer midiBuffer: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified FWAMIDIOutputBufferWithTimeStamp [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWAMIDIOutputBufferWithTimeStamp {     var timeStamp: UInt64     var midiBuffer: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct FWAMIDIOutputBufferWithTimeStamp {     var timeStamp: UInt64     var midiBuffer: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(timeStamp timeStamp: UInt64, midiBuffer midiBuffer: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified FWAMIDIReadBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWAMIDIReadBuffer {     var bufSize: UInt32     var mrBuf: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct FWAMIDIReadBuffer {     var bufSize: UInt32     var mrBuf: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(bufSize bufSize: UInt32, mrBuf mrBuf: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified FWASetPluginPathRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FWASetPluginPathRec {     var owningEngineRef: UInt32     var vendorID: UInt32     var modelID: UInt32     var pluginPath: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var pluginPathIsNull: Bool     var cacheValues: Bool } ``` |
| To | ```  ``` |

Modified CreateAsyncWakePort(FWARef, UnsafeMutablePointer<mach_port_t>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CreateAsyncWakePort(_ inRef: FWA!, _ notifyPort: UnsafePointer<mach_port_t>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CreateAsyncWakePort(_ inRef: FWARef, _ notifyPort: UnsafeMutablePointer<mach_port_t>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAAttachFWAudioMIDIStream(FWARef, FWAMIDIStreamRef, FWAIsochStreamRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAAttachFWAudioMIDIStream(_ inRef: FWA!, _ streamRef: FWAMIDIStream!, _ isochChannel: FWAIsochStream!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAAttachFWAudioMIDIStream(_ inRef: FWARef, _ streamRef: FWAMIDIStreamRef, _ isochChannel: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAAttachFWAudioStream(FWARef, FWAAudioStreamRef, FWAIsochStreamRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAAttachFWAudioStream(_ inRef: FWA!, _ streamRef: FWAAudioStream!, _ isochChannel: FWAIsochStream!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAAttachFWAudioStream(_ inRef: FWARef, _ streamRef: FWAAudioStreamRef, _ isochChannel: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAAudioPlugRef

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAAudioPlugRef = FWAAudioPlug ``` |
| To | ``` typealias FWAAudioPlugRef = COpaquePointer ``` |

Modified FWAAudioStreamRef

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAAudioStreamRef = FWAAudioStream ``` |
| To | ``` typealias FWAAudioStreamRef = COpaquePointer ``` |

Modified FWAClose(FWARef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAClose(_ inRef: FWA!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAClose(_ inRef: FWARef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACountDevices(UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func FWACountDevices(_ deviceNodeIDArray: UnsafePointer<UInt16>, _ deviceCount: UnsafePointer<UInt16>) -> OSStatus ``` |
| To | ``` func FWACountDevices(_ deviceNodeIDArray: UnsafeMutablePointer<UInt16>, _ deviceCount: UnsafeMutablePointer<UInt16>) -> OSStatus ``` |

Modified FWACreateAudioStream(FWARef, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateAudioStream(_ inRef: FWA!, _ audioIO: UInt32, _ audioStreamRef: UnsafePointer<UInt32>, _ sequenceNum: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateAudioStream(_ inRef: FWARef, _ audioIO: UInt32, _ audioStreamRef: UnsafeMutablePointer<UInt32>, _ sequenceNum: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateDeviceRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWACreateDeviceRecPtr = UnsafePointer<FWACreateDeviceRec> ``` |
| To | ``` typealias FWACreateDeviceRecPtr = UnsafeMutablePointer<FWACreateDeviceRec> ``` |

Modified FWACreateFWAudioDevice(FWARef, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UnsafeMutablePointer<FWADeviceRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateFWAudioDevice(_ inRef: FWA!, _ deviceName: ConstUnsafePointer<Int8>, _ vendorID: UInt32, _ guid: ConstUnsafePointer<Int8>, _ device: UnsafePointer<Unmanaged<FWADevice>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateFWAudioDevice(_ inRef: FWARef, _ deviceName: UnsafePointer<Int8>, _ vendorID: UInt32, _ guid: UnsafePointer<Int8>, _ device: UnsafeMutablePointer<FWADeviceRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateFWAudioEngine(FWARef, FWADeviceRef, Bool, Bool, UnsafeMutablePointer<FWAEngineRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateFWAudioEngine(_ inRef: FWA!, _ owningDevice: FWADevice!, _ hasInput: Bool, _ hasOutput: Bool, _ engine: UnsafePointer<Unmanaged<FWAEngine>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateFWAudioEngine(_ inRef: FWARef, _ owningDevice: FWADeviceRef, _ hasInput: Bool, _ hasOutput: Bool, _ engine: UnsafeMutablePointer<FWAEngineRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateFWAudioMIDIDeviceNub(FWARef, FWADeviceRef, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UnsafeMutablePointer<FWAMIDIDeviceNubRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateFWAudioMIDIDeviceNub(_ inRef: FWA!, _ owningDevice: FWADevice!, _ deviceName: ConstUnsafePointer<Int8>, _ vendorID: UInt32, _ guid: ConstUnsafePointer<Int8>, _ iconFilePath: ConstUnsafePointer<Int8>, _ modelID: UInt32, _ editorPath: ConstUnsafePointer<Int8>, _ device: UnsafePointer<Unmanaged<FWAMIDIDeviceNub>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateFWAudioMIDIDeviceNub(_ inRef: FWARef, _ owningDevice: FWADeviceRef, _ deviceName: UnsafePointer<Int8>, _ vendorID: UInt32, _ guid: UnsafePointer<Int8>, _ iconFilePath: UnsafePointer<Int8>, _ modelID: UInt32, _ editorPath: UnsafePointer<Int8>, _ device: UnsafeMutablePointer<FWAMIDIDeviceNubRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateFWAudioMIDIPlug(FWARef, FWAMIDIStreamRef, UInt8, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<FWAMIDIPlugRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateFWAudioMIDIPlug(_ inRef: FWA!, _ owningMIDIStreamRef: FWAMIDIStream!, _ mpxID: UInt8, _ plugName: UnsafePointer<Int8>, _ plugIdent: UnsafePointer<UInt8>, _ streamRef: UnsafePointer<Unmanaged<FWAMIDIPlug>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateFWAudioMIDIPlug(_ inRef: FWARef, _ owningMIDIStreamRef: FWAMIDIStreamRef, _ mpxID: UInt8, _ plugName: UnsafeMutablePointer<Int8>, _ plugIdent: UnsafeMutablePointer<UInt8>, _ streamRef: UnsafeMutablePointer<FWAMIDIPlugRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateFWAudioMIDIStream(FWARef, FWAIsochStreamRef, UInt32, UInt32, UnsafeMutablePointer<FWAMIDIStreamRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateFWAudioMIDIStream(_ inRef: FWA!, _ owningIsochStreamRef: FWAIsochStream!, _ sequenceNumber: UInt32, _ direction: UInt32, _ streamRef: UnsafePointer<Unmanaged<FWAMIDIStream>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateFWAudioMIDIStream(_ inRef: FWARef, _ owningIsochStreamRef: FWAIsochStreamRef, _ sequenceNumber: UInt32, _ direction: UInt32, _ streamRef: UnsafeMutablePointer<FWAMIDIStreamRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateFWAudioPlug(FWARef, FWAAudioStreamRef, UInt32, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<FWAAudioPlugRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateFWAudioPlug(_ inRef: FWA!, _ owningStream: FWAAudioStream!, _ channelID: UInt32, _ plugName: UnsafePointer<Int8>, _ plugIdent: UnsafePointer<UInt8>, _ streamRef: UnsafePointer<Unmanaged<FWAAudioPlug>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateFWAudioPlug(_ inRef: FWARef, _ owningStream: FWAAudioStreamRef, _ channelID: UInt32, _ plugName: UnsafeMutablePointer<Int8>, _ plugIdent: UnsafeMutablePointer<UInt8>, _ streamRef: UnsafeMutablePointer<FWAAudioPlugRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateFWAudioPlugRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWACreateFWAudioPlugRecPtr = UnsafePointer<FWACreateFWAudioPlugRec> ``` |
| To | ``` typealias FWACreateFWAudioPlugRecPtr = UnsafeMutablePointer<FWACreateFWAudioPlugRec> ``` |

Modified FWACreateFWAudioStream(FWARef, FWAIsochStreamRef, UInt32, UInt32, UInt32, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<FWAAudioStreamRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateFWAudioStream(_ inRef: FWA!, _ owningIsochStreamRef: FWAIsochStream!, _ channelNumber: UInt32, _ direction: UInt32, _ numAudioChannels: UInt32, _ streamName: UnsafePointer<Int8>, _ streamIdent: UnsafePointer<UInt8>, _ streamRef: UnsafePointer<Unmanaged<FWAAudioStream>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateFWAudioStream(_ inRef: FWARef, _ owningIsochStreamRef: FWAIsochStreamRef, _ channelNumber: UInt32, _ direction: UInt32, _ numAudioChannels: UInt32, _ streamName: UnsafeMutablePointer<Int8>, _ streamIdent: UnsafeMutablePointer<UInt8>, _ streamRef: UnsafeMutablePointer<FWAAudioStreamRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateIsochStream(FWARef, UInt32, FWAStreamDirection, UInt32, UInt32, UnsafeMutablePointer<FWAIsochStreamRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateIsochStream(_ inRef: FWA!, _ channelNumber: UInt32, _ direction: FWAStreamDirection, _ numAudioChannels: UInt32, _ numMIDIChannels: UInt32, _ isochStreamRef: UnsafePointer<Unmanaged<FWAIsochStream>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateIsochStream(_ inRef: FWARef, _ channelNumber: UInt32, _ direction: FWAStreamDirection, _ numAudioChannels: UInt32, _ numMIDIChannels: UInt32, _ isochStreamRef: UnsafeMutablePointer<FWAIsochStreamRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateMIDIDeviceNubRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWACreateMIDIDeviceNubRecPtr = UnsafePointer<FWACreateMIDIDeviceNubRec> ``` |
| To | ``` typealias FWACreateMIDIDeviceNubRecPtr = UnsafeMutablePointer<FWACreateMIDIDeviceNubRec> ``` |

Modified FWACreateMIDIPlugRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWACreateMIDIPlugRecPtr = UnsafePointer<FWACreateMIDIPlugRec> ``` |
| To | ``` typealias FWACreateMIDIPlugRecPtr = UnsafeMutablePointer<FWACreateMIDIPlugRec> ``` |

Modified FWACreateMIDIStream(FWARef, UInt32, UInt32, UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWACreateMIDIStream(_ inRef: FWA!, _ midiIO: UInt32, _ bufSizeInBytes: UInt32, _ buf: UnsafePointer<()>, _ sequenceNum: UInt32, _ midiStreamRef: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWACreateMIDIStream(_ inRef: FWARef, _ midiIO: UInt32, _ bufSizeInBytes: UInt32, _ buf: UnsafeMutablePointer<Void>, _ sequenceNum: UInt32, _ midiStreamRef: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWACreateStreamRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWACreateStreamRecPtr = UnsafePointer<FWACreateStreamRec> ``` |
| To | ``` typealias FWACreateStreamRecPtr = UnsafeMutablePointer<FWACreateStreamRec> ``` |

Modified FWADeviceRef

|  | Declaration |
| --- | --- |
| From | ``` typealias FWADeviceRef = FWADevice ``` |
| To | ``` typealias FWADeviceRef = COpaquePointer ``` |

Modified FWADeviceStatusRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWADeviceStatusRecPtr = UnsafePointer<FWADeviceStatus> ``` |
| To | ``` typealias FWADeviceStatusRecPtr = UnsafeMutablePointer<FWADeviceStatus> ``` |

Modified FWADisposeAudioStream(FWARef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeAudioStream(_ inRef: FWA!, _ audioStreamRef: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeAudioStream(_ inRef: FWARef, _ audioStreamRef: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWADisposeFWAudioDevice(FWARef, FWADeviceRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeFWAudioDevice(_ inRef: FWA!, _ device: FWADevice!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeFWAudioDevice(_ inRef: FWARef, _ device: FWADeviceRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWADisposeFWAudioEngine(FWARef, FWAEngineRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeFWAudioEngine(_ inRef: FWA!, _ engine: FWAEngine!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeFWAudioEngine(_ inRef: FWARef, _ engine: FWAEngineRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWADisposeFWAudioMIDIDeviceNub(FWARef, FWAMIDIDeviceNubRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeFWAudioMIDIDeviceNub(_ inRef: FWA!, _ device: FWAMIDIDeviceNub!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeFWAudioMIDIDeviceNub(_ inRef: FWARef, _ device: FWAMIDIDeviceNubRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWADisposeFWAudioMIDIPlug(FWARef, FWAMIDIPlugRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeFWAudioMIDIPlug(_ inRef: FWA!, _ plugRef: FWAMIDIPlug!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeFWAudioMIDIPlug(_ inRef: FWARef, _ plugRef: FWAMIDIPlugRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWADisposeFWAudioMIDIStream(FWARef, FWAMIDIStreamRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeFWAudioMIDIStream(_ inRef: FWA!, _ streamRef: FWAMIDIStream!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeFWAudioMIDIStream(_ inRef: FWARef, _ streamRef: FWAMIDIStreamRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWADisposeFWAudioPlug(FWARef, FWAAudioPlugRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeFWAudioPlug(_ inRef: FWA!, _ plugRef: FWAAudioPlug!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeFWAudioPlug(_ inRef: FWARef, _ plugRef: FWAAudioPlugRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWADisposeFWAudioStream(FWARef, FWAAudioStreamRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeFWAudioStream(_ inRef: FWA!, _ streamRef: FWAAudioStream!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeFWAudioStream(_ inRef: FWARef, _ streamRef: FWAAudioStreamRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWADisposeIsochStream(FWARef, FWAIsochStreamRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeIsochStream(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeIsochStream(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWADisposeMIDIStream(FWARef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWADisposeMIDIStream(_ inRef: FWA!, _ midiStreamRef: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWADisposeMIDIStream(_ inRef: FWARef, _ midiStreamRef: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAEngineRef

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAEngineRef = FWAEngine ``` |
| To | ``` typealias FWAEngineRef = COpaquePointer ``` |

Modified FWAExecuteAVC(FWARef, UnsafeMutablePointer<UInt8>, UInt32, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAExecuteAVC(_ inRef: FWA!, _ cmd: UnsafePointer<UInt8>, _ cmdSize: UInt32, _ response: UnsafePointer<UInt8>, _ responseSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAExecuteAVC(_ inRef: FWARef, _ cmd: UnsafeMutablePointer<UInt8>, _ cmdSize: UInt32, _ response: UnsafeMutablePointer<UInt8>, _ responseSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetAEvntSource(FWARef) -> Unmanaged<CFRunLoopSource>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetAEvntSource(_ inRef: FWA!) -> Unmanaged<CFRunLoopSource>! ``` | OS X 10.10 |
| To | ``` func FWAGetAEvntSource(_ inRef: FWARef) -> Unmanaged<CFRunLoopSource>! ``` | OS X 10.10.3 |

Modified FWAGetClockSource(FWARef, UnsafeMutablePointer<FWAIsochStreamRef>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetClockSource(_ inRef: FWA!, _ streamRef: UnsafePointer<Unmanaged<FWAIsochStream>?>, _ sequence: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetClockSource(_ inRef: FWARef, _ streamRef: UnsafeMutablePointer<FWAIsochStreamRef>, _ sequence: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetCurrentIsochStreamRefs(FWARef, UnsafeMutablePointer<FWAIsochStreamRef>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetCurrentIsochStreamRefs(_ inRef: FWA!, _ isochStreamRef: UnsafePointer<Unmanaged<FWAIsochStream>?>, _ count: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetCurrentIsochStreamRefs(_ inRef: FWARef, _ isochStreamRef: UnsafeMutablePointer<FWAIsochStreamRef>, _ count: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetCycleTimeOffset(FWARef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetCycleTimeOffset(_ inRef: FWA!, _ cycleTimeOffset: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetCycleTimeOffset(_ inRef: FWARef, _ cycleTimeOffset: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetDeviceName(FWARef, UnsafeMutablePointer<Int8>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetDeviceName(_ inRef: FWA!, _ name: UnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetDeviceName(_ inRef: FWARef, _ name: UnsafeMutablePointer<Int8>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetDeviceSampleRate(FWARef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetDeviceSampleRate(_ inRef: FWA!, _ rate: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetDeviceSampleRate(_ inRef: FWARef, _ rate: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetDeviceSendMode(FWARef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetDeviceSendMode(_ inRef: FWA!, _ mode: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetDeviceSendMode(_ inRef: FWARef, _ mode: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetDeviceStatus(FWARef, UnsafeMutablePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetDeviceStatus(_ inRef: FWA!, _ outData: UnsafePointer<()>, _ inSize: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetDeviceStatus(_ inRef: FWARef, _ outData: UnsafeMutablePointer<Void>, _ inSize: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetDeviceStreamInfo(FWARef, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetDeviceStreamInfo(_ inRef: FWA!, _ audioStreamRef: UInt32, _ numInput: UnsafePointer<UInt32>, _ inputIsochChan: UnsafePointer<UInt32>, _ numOutput: UnsafePointer<UInt32>, _ outputIsochChan: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetDeviceStreamInfo(_ inRef: FWARef, _ audioStreamRef: UInt32, _ numInput: UnsafeMutablePointer<UInt32>, _ inputIsochChan: UnsafeMutablePointer<UInt32>, _ numOutput: UnsafeMutablePointer<UInt32>, _ outputIsochChan: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetFWAudioMIDIPlugChannel(FWARef, FWAMIDIPlugRef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetFWAudioMIDIPlugChannel(_ inRef: FWA!, _ streamRef: FWAMIDIPlug!, _ channelID: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetFWAudioMIDIPlugChannel(_ inRef: FWARef, _ streamRef: FWAMIDIPlugRef, _ channelID: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetFWAudioPlugChannel(FWARef, FWAAudioPlugRef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetFWAudioPlugChannel(_ inRef: FWA!, _ streamRef: FWAAudioPlug!, _ channelID: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetFWAudioPlugChannel(_ inRef: FWARef, _ streamRef: FWAAudioPlugRef, _ channelID: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetGUID(FWARef, UnsafeMutablePointer<UInt64>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetGUID(_ inRef: FWA!, _ guid: UnsafePointer<UInt64>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetGUID(_ inRef: FWARef, _ guid: UnsafeMutablePointer<UInt64>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIndexedFWAudioMIDIPlug(FWARef, FWAMIDIDeviceNubRef, UInt32, UInt32, UnsafeMutablePointer<FWAMIDIPlugRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIndexedFWAudioMIDIPlug(_ inRef: FWA!, _ device: FWAMIDIDeviceNub!, _ index: UInt32, _ dir: UInt32, _ plugRef: UnsafePointer<Unmanaged<FWAMIDIPlug>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIndexedFWAudioMIDIPlug(_ inRef: FWARef, _ device: FWAMIDIDeviceNubRef, _ index: UInt32, _ dir: UInt32, _ plugRef: UnsafeMutablePointer<FWAMIDIPlugRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIndexedFWAudioPlug(FWARef, FWADeviceRef, UInt32, UInt32, UnsafeMutablePointer<FWAAudioPlugRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIndexedFWAudioPlug(_ inRef: FWA!, _ device: FWADevice!, _ index: UInt32, _ dir: UInt32, _ plugRef: UnsafePointer<Unmanaged<FWAAudioPlug>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIndexedFWAudioPlug(_ inRef: FWARef, _ device: FWADeviceRef, _ index: UInt32, _ dir: UInt32, _ plugRef: UnsafeMutablePointer<FWAAudioPlugRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIsochStreamAudioSequenceCount(FWARef, FWAIsochStreamRef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIsochStreamAudioSequenceCount(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ numAudioSequence: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIsochStreamAudioSequenceCount(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ numAudioSequence: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIsochStreamAudioType(FWARef, FWAIsochStreamRef, UnsafeMutablePointer<FWAudioType>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIsochStreamAudioType(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ type: UnsafePointer<FWAudioType>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIsochStreamAudioType(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ type: UnsafeMutablePointer<FWAudioType>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIsochStreamChannelID(FWARef, FWAIsochStreamRef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIsochStreamChannelID(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ channelID: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIsochStreamChannelID(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ channelID: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIsochStreamDirection(FWARef, FWAIsochStreamRef, UnsafeMutablePointer<FWAStreamDirection>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIsochStreamDirection(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ direction: UnsafePointer<FWAStreamDirection>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIsochStreamDirection(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ direction: UnsafeMutablePointer<FWAStreamDirection>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIsochStreamMIDISequenceCount(FWARef, FWAIsochStreamRef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIsochStreamMIDISequenceCount(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ numMIDISequence: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIsochStreamMIDISequenceCount(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ numMIDISequence: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIsochStreamOutputSpeed(FWARef, FWAIsochStreamRef, UnsafeMutablePointer<IOFWSpeed>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIsochStreamOutputSpeed(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ speed: UnsafePointer<IOFWSpeed>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIsochStreamOutputSpeed(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ speed: UnsafeMutablePointer<IOFWSpeed>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIsochStreamSampleRate(FWARef, FWAIsochStreamRef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIsochStreamSampleRate(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ rate: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIsochStreamSampleRate(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ rate: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetIsochStreamState(FWARef, FWAIsochStreamRef, UnsafeMutablePointer<FWAStreamState>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetIsochStreamState(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ state: UnsafePointer<FWAStreamState>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetIsochStreamState(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ state: UnsafeMutablePointer<FWAStreamState>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetMacGUID(FWARef, UnsafeMutablePointer<UInt64>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetMacGUID(_ inRef: FWA!, _ guid: UnsafePointer<UInt64>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetMacGUID(_ inRef: FWARef, _ guid: UnsafeMutablePointer<UInt64>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetMaxIsochChannels(FWARef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetMaxIsochChannels(_ inRef: FWA!, _ inChannels: UnsafePointer<UInt32>, _ outChannels: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetMaxIsochChannels(_ inRef: FWARef, _ inChannels: UnsafeMutablePointer<UInt32>, _ outChannels: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetMaxSequences(FWARef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetMaxSequences(_ inRef: FWA!, _ numSequences: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetMaxSequences(_ inRef: FWARef, _ numSequences: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetMaxSpeed(FWARef, UnsafeMutablePointer<IOFWSpeed>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetMaxSpeed(_ inRef: FWA!, _ speed: UnsafePointer<IOFWSpeed>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetMaxSpeed(_ inRef: FWARef, _ speed: UnsafeMutablePointer<IOFWSpeed>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetNodeID(FWARef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetNodeID(_ inRef: FWA!, _ outNodeID: UnsafePointer<UInt32>, _ outGeneration: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetNodeID(_ inRef: FWARef, _ outNodeID: UnsafeMutablePointer<UInt32>, _ outGeneration: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetNumAudioInputPlugs(FWARef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetNumAudioInputPlugs(_ inRef: FWA!, _ plugs: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetNumAudioInputPlugs(_ inRef: FWARef, _ plugs: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetNumAudioOutputPlugs(FWARef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetNumAudioOutputPlugs(_ inRef: FWA!, _ plugs: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetNumAudioOutputPlugs(_ inRef: FWARef, _ plugs: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetNumMIDIInputPlugs(FWARef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetNumMIDIInputPlugs(_ inRef: FWA!, _ plugs: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetNumMIDIInputPlugs(_ inRef: FWARef, _ plugs: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetNumMIDIOutputPlugs(FWARef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetNumMIDIOutputPlugs(_ inRef: FWA!, _ plugs: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetNumMIDIOutputPlugs(_ inRef: FWARef, _ plugs: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetProperty(FWARef, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetProperty(_ inRef: FWA!, _ propertyID: UInt32, _ data: UnsafePointer<()>, _ size: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetProperty(_ inRef: FWARef, _ propertyID: UInt32, _ data: UnsafeMutablePointer<Void>, _ size: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetPropertyRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAGetPropertyRecPtr = UnsafePointer<FWAGetPropertyRec> ``` |
| To | ``` typealias FWAGetPropertyRecPtr = UnsafeMutablePointer<FWAGetPropertyRec> ``` |

Modified FWAGetSessionRef(FWARef, UnsafeMutablePointer<IOFireWireSessionRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetSessionRef(_ inRef: FWA!, _ sessionRef: UnsafePointer<Unmanaged<IOFireWireSession>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetSessionRef(_ inRef: FWARef, _ sessionRef: UnsafeMutablePointer<IOFireWireSessionRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetSupportedAudioTypes(FWARef, UnsafeMutablePointer<FWAudioType>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetSupportedAudioTypes(_ inRef: FWA!, _ audioTypes: UnsafePointer<FWAudioType>, _ count: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetSupportedAudioTypes(_ inRef: FWARef, _ audioTypes: UnsafeMutablePointer<FWAudioType>, _ count: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetSupportedSampleRates(FWARef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetSupportedSampleRates(_ inRef: FWA!, _ sampleRates: UnsafePointer<UInt32>, _ count: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetSupportedSampleRates(_ inRef: FWARef, _ sampleRates: UnsafeMutablePointer<UInt32>, _ count: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetVendorID(FWARef, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetVendorID(_ inRef: FWA!, _ vendorID: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetVendorID(_ inRef: FWARef, _ vendorID: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAGetVendorName(FWARef, UnsafeMutablePointer<Int8>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAGetVendorName(_ inRef: FWA!, _ name: UnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAGetVendorName(_ inRef: FWARef, _ name: UnsafeMutablePointer<Int8>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAInitAEvntSource(FWARef, UnsafeMutablePointer<Unmanaged<CFRunLoopSource>?>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAInitAEvntSource(_ inRef: FWA!, _ source: UnsafePointer<Unmanaged<CFRunLoopSource>?>, _ refcon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAInitAEvntSource(_ inRef: FWARef, _ source: UnsafeMutablePointer<Unmanaged<CFRunLoopSource>?>, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAIsMIDICapable(FWARef, UnsafeMutablePointer<Bool>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAIsMIDICapable(_ inRef: FWA!, _ supportsMIDI: UnsafePointer<Bool>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAIsMIDICapable(_ inRef: FWARef, _ supportsMIDI: UnsafeMutablePointer<Bool>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAIsochStreamRef

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAIsochStreamRef = FWAIsochStream ``` |
| To | ``` typealias FWAIsochStreamRef = COpaquePointer ``` |

Modified FWAMIDIDeviceNubAttachMIDIPlug(FWARef, FWAMIDIDeviceNubRef, FWAMIDIPlugRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAMIDIDeviceNubAttachMIDIPlug(_ inRef: FWA!, _ midiDeviceNub: FWAMIDIDeviceNub!, _ midiPlug: FWAMIDIPlug!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAMIDIDeviceNubAttachMIDIPlug(_ inRef: FWARef, _ midiDeviceNub: FWAMIDIDeviceNubRef, _ midiPlug: FWAMIDIPlugRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAMIDIDeviceNubDetachMIDIPlug(FWARef, FWAMIDIPlugRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAMIDIDeviceNubDetachMIDIPlug(_ inRef: FWA!, _ midiPlug: FWAMIDIPlug!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAMIDIDeviceNubDetachMIDIPlug(_ inRef: FWARef, _ midiPlug: FWAMIDIPlugRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAMIDIDeviceNubRef

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAMIDIDeviceNubRef = FWAMIDIDeviceNub ``` |
| To | ``` typealias FWAMIDIDeviceNubRef = COpaquePointer ``` |

Modified FWAMIDIPlugRef

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAMIDIPlugRef = FWAMIDIPlug ``` |
| To | ``` typealias FWAMIDIPlugRef = COpaquePointer ``` |

Modified FWAMIDIStreamRef

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAMIDIStreamRef = FWAMIDIStream ``` |
| To | ``` typealias FWAMIDIStreamRef = COpaquePointer ``` |

Modified FWAOpen(UInt32, UnsafeMutablePointer<FWARef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAOpen(_ nodeID: UInt32, _ outRef: UnsafePointer<Unmanaged<FWA>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAOpen(_ nodeID: UInt32, _ outRef: UnsafeMutablePointer<FWARef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAOpenLocal(UnsafeMutablePointer<FWARef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAOpenLocal(_ outRef: UnsafePointer<Unmanaged<FWA>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAOpenLocal(_ outRef: UnsafeMutablePointer<FWARef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAOpenLocalWithInterface(UInt64, UInt32, UnsafeMutablePointer<FWARef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAOpenLocalWithInterface(_ guid: UInt64, _ options: UInt32, _ outRef: UnsafePointer<Unmanaged<FWA>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAOpenLocalWithInterface(_ guid: UInt64, _ options: UInt32, _ outRef: UnsafeMutablePointer<FWARef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAOpenWithService(io_service_t, UInt32, UnsafeMutablePointer<FWARef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAOpenWithService(_ _: io_service_t, _ options: UInt32, _ outRef: UnsafePointer<Unmanaged<FWA>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAOpenWithService(_ _: io_service_t, _ options: UInt32, _ outRef: UnsafeMutablePointer<FWARef>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWARead(FWARef, UInt8, UInt8, Int, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWARead(_ inRef: FWA!, _ inAddress: UInt8, _ inSubAddress: UInt8, _ inDataSize: ByteCount, _ inDataPtr: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWARead(_ inRef: FWARef, _ inAddress: UInt8, _ inSubAddress: UInt8, _ inDataSize: Int, _ inDataPtr: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAReadBlock(FWARef, FWAddressPtr, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt8>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAReadBlock(_ inRef: FWA!, _ address: FWAddressPtr, _ size: UnsafePointer<UInt32>, _ outData: UnsafePointer<UInt8>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAReadBlock(_ inRef: FWARef, _ address: FWAddressPtr, _ size: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UInt8>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAReadMIDIData(FWARef, UInt32, UnsafeMutablePointer<FWAMIDIReadBuf>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAReadMIDIData(_ inRef: FWA!, _ midiStreamRef: UInt32, _ buf: UnsafePointer<FWAMIDIReadBuf>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAReadMIDIData(_ inRef: FWARef, _ midiStreamRef: UInt32, _ buf: UnsafeMutablePointer<FWAMIDIReadBuf>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAReadMIDIDataAsync(FWARef, UInt32, UInt32, IOAsyncCallback2, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAReadMIDIDataAsync(_ inRef: FWA!, _ midiStreamRef: UInt32, _ readBufSize: UInt32, _ callback: IOAsyncCallback2, _ refCon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAReadMIDIDataAsync(_ inRef: FWARef, _ midiStreamRef: UInt32, _ readBufSize: UInt32, _ callback: IOAsyncCallback2, _ refCon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAReadQuadlet(FWARef, FWAddressPtr, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAReadQuadlet(_ inRef: FWA!, _ address: FWAddressPtr, _ outData: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAReadQuadlet(_ inRef: FWARef, _ address: FWAddressPtr, _ outData: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWARef

|  | Declaration |
| --- | --- |
| From | ``` typealias FWARef = FWA ``` |
| To | ``` typealias FWARef = COpaquePointer ``` |

Modified FWAReserveIsochSequences(FWARef, FWAIsochStreamRef, FWAudioType, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAReserveIsochSequences(_ inRef: FWA!, _ isochStream: FWAIsochStream!, _ type: FWAudioType, _ count: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAReserveIsochSequences(_ inRef: FWARef, _ isochStream: FWAIsochStreamRef, _ type: FWAudioType, _ count: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetAutoLoad(FWARef, Bool) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetAutoLoad(_ inRef: FWA!, _ enable: Bool) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetAutoLoad(_ inRef: FWARef, _ enable: Bool) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetClockSource(FWARef, FWAIsochStreamRef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetClockSource(_ inRef: FWA!, _ streamRef: FWAIsochStream!, _ sequence: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetClockSource(_ inRef: FWARef, _ streamRef: FWAIsochStreamRef, _ sequence: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetCycleTimeOffset(FWARef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetCycleTimeOffset(_ inRef: FWA!, _ cycleTimeOffset: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetCycleTimeOffset(_ inRef: FWARef, _ cycleTimeOffset: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetDeviceStreamInfo(FWARef, UInt32, UInt32, UInt32, UInt32, UInt32, Bool) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetDeviceStreamInfo(_ inRef: FWA!, _ audioStreamRef: UInt32, _ numInput: UInt32, _ inputIsochChan: UInt32, _ numOutput: UInt32, _ outputIsochChan: UInt32, _ update: Bool) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetDeviceStreamInfo(_ inRef: FWARef, _ audioStreamRef: UInt32, _ numInput: UInt32, _ inputIsochChan: UInt32, _ numOutput: UInt32, _ outputIsochChan: UInt32, _ update: Bool) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetFWAudioMIDIPlugChannel(FWARef, FWAMIDIPlugRef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetFWAudioMIDIPlugChannel(_ inRef: FWA!, _ streamRef: FWAMIDIPlug!, _ channelID: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetFWAudioMIDIPlugChannel(_ inRef: FWARef, _ streamRef: FWAMIDIPlugRef, _ channelID: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetFWAudioMIDIPlugProperty(FWARef, FWAMIDIPlugRef, UnsafePointer<Int8>, UnsafePointer<Int8>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetFWAudioMIDIPlugProperty(_ inRef: FWA!, _ plugRef: FWAMIDIPlug!, _ keyname: ConstUnsafePointer<Int8>, _ keyvalue: ConstUnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetFWAudioMIDIPlugProperty(_ inRef: FWARef, _ plugRef: FWAMIDIPlugRef, _ keyname: UnsafePointer<Int8>, _ keyvalue: UnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetFWAudioPlugChannel(FWARef, FWAAudioPlugRef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetFWAudioPlugChannel(_ inRef: FWA!, _ streamRef: FWAAudioPlug!, _ channelID: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetFWAudioPlugChannel(_ inRef: FWARef, _ streamRef: FWAAudioPlugRef, _ channelID: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetFWAudioPlugProperty(FWARef, FWAAudioPlugRef, UnsafePointer<Int8>, UnsafePointer<Int8>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetFWAudioPlugProperty(_ inRef: FWA!, _ plugRef: FWAAudioPlug!, _ keyname: ConstUnsafePointer<Int8>, _ keyvalue: ConstUnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetFWAudioPlugProperty(_ inRef: FWARef, _ plugRef: FWAAudioPlugRef, _ keyname: UnsafePointer<Int8>, _ keyvalue: UnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetIsochStreamAudioSequenceCount(FWARef, FWAIsochStreamRef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetIsochStreamAudioSequenceCount(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ numAudioSequence: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetIsochStreamAudioSequenceCount(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ numAudioSequence: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetIsochStreamAudioType(FWARef, FWAIsochStreamRef, FWAudioType) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetIsochStreamAudioType(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ type: FWAudioType) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetIsochStreamAudioType(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ type: FWAudioType) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetIsochStreamChannelID(FWARef, FWAIsochStreamRef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetIsochStreamChannelID(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ channelID: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetIsochStreamChannelID(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ channelID: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetIsochStreamMIDISequenceCount(FWARef, FWAIsochStreamRef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetIsochStreamMIDISequenceCount(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ numMIDISequence: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetIsochStreamMIDISequenceCount(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ numMIDISequence: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetIsochStreamOutputSpeed(FWARef, FWAIsochStreamRef, IOFWSpeed) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetIsochStreamOutputSpeed(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ speed: IOFWSpeed) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetIsochStreamOutputSpeed(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ speed: IOFWSpeed) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetIsochStreamSampleRate(FWARef, FWAIsochStreamRef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetIsochStreamSampleRate(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!, _ rate: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetIsochStreamSampleRate(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ rate: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetNumMIDIInputPlugs(FWARef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetNumMIDIInputPlugs(_ inRef: FWA!, _ plugs: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetNumMIDIInputPlugs(_ inRef: FWARef, _ plugs: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetNumMIDIOutputPlugs(FWARef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetNumMIDIOutputPlugs(_ inRef: FWA!, _ plugs: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetNumMIDIOutputPlugs(_ inRef: FWARef, _ plugs: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetPlugPropertyRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWASetPlugPropertyRecPtr = UnsafePointer<FWASetPlugPropertyRec> ``` |
| To | ``` typealias FWASetPlugPropertyRecPtr = UnsafeMutablePointer<FWASetPlugPropertyRec> ``` |

Modified FWASetPluginPath(FWARef, FWAEngineRef, UInt32, UInt32, UnsafePointer<Int8>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetPluginPath(_ inRef: FWA!, _ engine: FWAEngine!, _ vendorID: UInt32, _ modelID: UInt32, _ pluginPath: ConstUnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetPluginPath(_ inRef: FWARef, _ engine: FWAEngineRef, _ vendorID: UInt32, _ modelID: UInt32, _ pluginPath: UnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWASetPluginPathRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWASetPluginPathRecPtr = UnsafePointer<FWASetPluginPathRec> ``` |
| To | ``` typealias FWASetPluginPathRecPtr = UnsafeMutablePointer<FWASetPluginPathRec> ``` |

Modified FWASetProperty(FWARef, UInt32, UnsafeMutablePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASetProperty(_ inRef: FWA!, _ propertyID: UInt32, _ data: UnsafePointer<()>, _ size: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASetProperty(_ inRef: FWARef, _ propertyID: UInt32, _ data: UnsafeMutablePointer<Void>, _ size: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAStartFWAudioDevice(FWARef, FWADeviceRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAStartFWAudioDevice(_ inRef: FWA!, _ device: FWADevice!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAStartFWAudioDevice(_ inRef: FWARef, _ device: FWADeviceRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAStartIsochStream(FWARef, FWAIsochStreamRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAStartIsochStream(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAStartIsochStream(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAStopFWAudioDevice(FWARef, FWADeviceRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAStopFWAudioDevice(_ inRef: FWA!, _ device: FWADevice!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAStopFWAudioDevice(_ inRef: FWARef, _ device: FWADeviceRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAStopIsochStream(FWARef, FWAIsochStreamRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAStopIsochStream(_ inRef: FWA!, _ isochStreamRef: FWAIsochStream!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAStopIsochStream(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAStreamNotificationProc

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAStreamNotificationProc = CFunctionPointer<((UInt32, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias FWAStreamNotificationProc = CFunctionPointer<((UInt32, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified FWASyncUpDevice(FWARef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWASyncUpDevice(_ inRef: FWA!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWASyncUpDevice(_ inRef: FWARef) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAWrite(FWARef, UInt8, UInt8, Int, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAWrite(_ inRef: FWA!, _ inAddress: UInt8, _ inSubAddress: UInt8, _ inDataSize: ByteCount, _ inDataPtr: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAWrite(_ inRef: FWARef, _ inAddress: UInt8, _ inSubAddress: UInt8, _ inDataSize: Int, _ inDataPtr: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAWriteBlock(FWARef, FWAddressPtr, UInt32, UnsafePointer<UInt8>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAWriteBlock(_ inRef: FWA!, _ address: FWAddressPtr, _ size: UInt32, _ data: ConstUnsafePointer<UInt8>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAWriteBlock(_ inRef: FWARef, _ address: FWAddressPtr, _ size: UInt32, _ data: UnsafePointer<UInt8>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAWriteMIDIData(FWARef, UInt32, UInt32, UnsafeMutablePointer<UInt8>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAWriteMIDIData(_ inRef: FWA!, _ midiStreamRef: UInt32, _ writeMsgLength: UInt32, _ buf: UnsafePointer<UInt8>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAWriteMIDIData(_ inRef: FWARef, _ midiStreamRef: UInt32, _ writeMsgLength: UInt32, _ buf: UnsafeMutablePointer<UInt8>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAWriteMIDIDataAsync(FWARef, UInt32, UInt32, IOAsyncCallback1, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAWriteMIDIDataAsync(_ inRef: FWA!, _ midiStreamRef: UInt32, _ writeMsgLength: UInt32, _ callback: IOAsyncCallback1, _ refCon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAWriteMIDIDataAsync(_ inRef: FWARef, _ midiStreamRef: UInt32, _ writeMsgLength: UInt32, _ callback: IOAsyncCallback1, _ refCon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAWriteQuadlet(FWARef, FWAddressPtr, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FWAWriteQuadlet(_ inRef: FWA!, _ address: FWAddressPtr, _ data: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FWAWriteQuadlet(_ inRef: FWARef, _ address: FWAddressPtr, _ data: UInt32) -> OSStatus ``` | OS X 10.10.3 |

Modified FWAudioTypePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAudioTypePtr = UnsafePointer<FWAudioType> ``` |
| To | ``` typealias FWAudioTypePtr = UnsafeMutablePointer<FWAudioType> ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
