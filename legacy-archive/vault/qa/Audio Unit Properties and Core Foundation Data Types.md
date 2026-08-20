---
title: Audio Unit Properties and Core Foundation Data Types
apple_id: DTS40009582
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2010-03-03'
source_url: https://developer.apple.com/library/archive/qa/qa1684/_index.html
archived_at: '2026-07-18T02:33:47.708848Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1684

# Audio Unit Properties and Core Foundation Data Types

## Q:  When working with Audio Unit properties that take and return Core Foundation Data Types, who is responsible for retaining or releasing.

A: When working with Audio Unit properties that take and return Core Foundation Data Types, who is responsible for retaining or releasing.

Whenever an Audio Unit host is working with Audio Unit properties that are Core Foundation Data Types, the caller almost always owns the reference and is therefore responsible for releasing it as required.

- `kAudioUnitProperty_ClassInfo` - Takes a `CFDictionaryRef` valid on global scope.
- `kAudioUnitProperty_ElementName` - Takes a `CFStringRef` valid on any scope.
- `kAudioUnitProperty_PresentPreset` - Takes an `AUPreset` struct valid on global scope. `presetName` is a `CFStringRef` containing the preset name owned by the caller after getting this property.

All Core Foundation objects returned by `AudioUnitGetProperty` follow Core Foundation Copy semantics and are therefore owned by the caller. It is the callers responsibility to relinquish ownership (using `CFRelease`) when done with the returned value.

- `kAudioUnitProperty_ClassInfo` - Returns a `CFDictionaryRef`.
- `kAudioUnitProperty_ParameterValueStrings` - Returns a `CFArrayRef`.
- `kAudioUnitProperty_FactoryPresets` - Returns a `CFArrayRef`.
- `kAudioUnitProperty_ElementName` - Returns a `CFStringRef`.
- `kAudioUnitOfflineProperty_PreflightName` - Returns a `CFStringRef`.
- `kMusicDeviceProperty_BankName` - Returns a `CFStringRef`.

- `kAudioUnitProperty_PresentPreset` - Returns an `AUPreset`, where `presetName` is a `CFStringRef` containing the preset name.
- `kAudioUnitProperty_ParameterStringFromValue` - Returns a `AudioUnitParameterStringFromValue` struct where `outString` is a `CFStringRef` (may be `NULL`).
- `kAudioUnitProperty_ParameterIDName` - Returns a `AudioUnitParameterNameInfo` struct where `outName` is a `CFStringRef`.
- `kAudioUnitProperty_ParameterClumpName` - Returns a `AudioUnitParameterNameInfo` struct where `outName` is a `CFStringRef`.
- `kAudioUnitProperty_CocoaUI` - Returns a `AudioUnitCocoaViewInfo` struct where the `CFStringRef` class name(s) are returned in the `mCocoaAUViewClass` field.

The number of class names in the `mCocoaAUViewClass` field can be found by using the following code. `dataSize` is the maximum size of the property returned by calling `AudioUnitGetPropertyInfo` for the `kAudioUnitProperty_CocoaUI` property.


```
UInt32 numberOfClasses = (dataSize - sizeof(CFURLRef)) / sizeof(CFStringRef);
```


Ownership is based on the `kAudioUnitParameterFlag_CFNameRelease` flag. This flag is normally always set.

- `kAudioUnitProperty_ParameterInfo` - Returns a `AudioUnitParameterInfo` struct. Only release `unitName` and `cfNameString` `CFStringRefs` if the `kAudioUnitParameterFlag_CFNameRelease` flag is set. See Listing 1.

The Audio Unit Host should check for this flag and if set, should release the audio unit parameter name when it is done using it. If this flag is not set, the Host can assume that the Audio Unit will release its parameter names.

__Listing 1__  Illustrating use of `kAudioUnitParameterFlag_CFNameRelease`.

```
AudioUnitParameterInfo auinfo; UInt32 propertySize = sizeof(AudioUnitParameterInfo); OSStatus err = AudioUnitGetProperty(mAudioUnit,                                     kAudioUnitProperty_ParameterInfo,                                     mScope,                                     mParameterID,                                     &auinfo,                                     &propertySize); if (err) { // handle error };  ...   if (auinfo.flags & kAudioUnitParameterFlag_CFNameRelease) {     if (auinfo.flags & kAudioUnitParameterFlag_HasCFNameString && auinfo.cfNameString != NULL)         CFRelease(auinfo.cfNameString);     if (auinfo.unit == kAudioUnitParameterUnit_CustomUnit && auinfo.unitName != NULL)         CFRelease(auinfo.unitName); }
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-03-03 | New document that describes the ownership of CF data types when Getting/Setting AU properties. |

