---
title: auval - Invalid Selector For AU Type Error on Mac OS X 10.7
apple_id: DTS40010885
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/qa/qa1737/_index.html
archived_at: '2026-07-18T02:34:32.269289Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1737

# auval - Invalid Selector For AU Type Error on Mac OS X 10.7

## Q:  When testing our Audio Units on Mac OS X 10.7, we are seeing `auval` errors that were not present on previous version of Mac OS X. For example, we now get `ERROR: MusicDeviceSendMIDI should be invalid selector for AU type - noErr was returned`. What does this mean?

A: There are a couple of things implied by the returned error message:

The `auval` test itself is predicated on two things:

- An Audio Unit of type `kAudioUnitType_Effect` (`'aufx'`) does __NOT__ support the MIDI selectors.
- If an Audio Unit of type `kAudioUnitType_Effect` (`'aufx'`) __does__ support MIDI selectors (which is incorrect according to the Audio Unit Specification), there is no way to determine if the Audio Unit actually implements the selectors or not.

Therefore, to clarify this ambiguity from the Audio Unit host's perspective, `auval` will now perform this test and fail an Audio Unit it is propagating this ambiguity.

When `auval` gets back a `noErr` from an Audio Unit in this case, the unit must be supporting the `kMusicDeviceMIDIEventSelect` selector somewhere in the Component Dispatch function.

If the Audio Unit is a subclass of `AUBase` or `AUEffectBase` then by default it would not have support for the MIDI selectors. If it is a subclass of `AUMIDIBase` however, then the entry point is overridden and can be found in `AUMIDIBase.cpp`:

__Listing 1__

```swift
ComponentResult AUMIDIBase::ComponentEntryDispatch(ComponentParameters *params, AUMIDIBase *This) {     if (This == NULL) return paramErr;      ComponentResult result;      switch (params->what) {     case kMusicDeviceMIDIEventSelect:         {             PARAM(UInt32, pbinStatus, 0, 4);             PARAM(UInt32, pbinData1, 1, 4);             PARAM(UInt32, pbinData2, 2, 4);             PARAM(UInt32, pbinOffsetSampleFrame, 3, 4);             result = This->MIDIEvent(pbinStatus, pbinData1, pbinData2, pbinOffsetSampleFrame);         }         break;     case kMusicDeviceSysExSelect:         {             PARAM(const UInt8 *, pbinData, 0, 2);             PARAM(UInt32, pbinLength, 1, 2);             result = This->SysEx(pbinData, pbinLength);         }         break;      default:         result = badComponentSelector;         break;     }      return result; }
```

Search for `kMusicDeviceMIDIEventSelect` and `kMusicDeviceSysExSelect` as the dispatch code must be accepting these as valid selectors.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-04-13 | New document that describes a new error auval may return Mac OS X 10.7 when no error was previously returned. |

