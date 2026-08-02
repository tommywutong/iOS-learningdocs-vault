---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_AUBase_AUPlugInDispatch_h.html
archived_at: '2026-07-26T19:54:12.338786Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-AUBase-AUOutputElement.cpp.md)[Previous](AUPublic-AUBase-AUBase.cpp.md)

# AUPublic/AUBase/AUPlugInDispatch.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUBase Classes
*/

#ifndef __AUPlugInBase_h__
#define __AUPlugInBase_h__

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <AudioUnit/AudioComponent.h>
    #if !CA_BASIC_AU_FEATURES
        #include <AudioUnit/MusicDevice.h>
    #endif
#else
    #include "AudioComponent.h"
    #include "MusicDevice.h"
#endif

#include "ComponentBase.h"

struct AUBaseLookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUBaseFactory : public APFactory<AUBaseLookup, Implementor>
{
};

struct AUOutputLookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUOutputBaseFactory : public APFactory<AUOutputLookup, Implementor>
{
};

struct AUComplexOutputLookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUOutputComplexBaseFactory : public APFactory<AUComplexOutputLookup, Implementor>
{
};

struct AUBaseProcessLookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUBaseProcessFactory : public APFactory<AUBaseProcessLookup, Implementor>
{
};

struct AUBaseProcessMultipleLookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUBaseProcessMultipleFactory : public APFactory<AUBaseProcessMultipleLookup, Implementor>
{
};

struct AUBaseProcessAndMultipleLookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUBaseProcessAndMultipleFactory : public APFactory<AUBaseProcessAndMultipleLookup, Implementor>
{
};

#if !CA_BASIC_AU_FEATURES
struct AUMIDILookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUMIDIEffectFactory : public APFactory<AUMIDILookup, Implementor>
{
};

struct AUMIDIProcessLookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUMIDIProcessFactory : public APFactory<AUMIDIProcessLookup, Implementor>
{
};

struct AUMusicLookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUMusicDeviceFactory : public APFactory<AUMusicLookup, Implementor>
{
};

struct AUAuxBaseLookup {
    static AudioComponentMethod Lookup (SInt16 selector);
};
template <class Implementor>
class AUAuxBaseFactory : public APFactory<AUAuxBaseLookup, Implementor>
{
};
#endif // CA_BASIC_AU_FEATURES

#endif // __AUPlugInBase_h__
```

[Next](AUPublic-AUBase-AUOutputElement.cpp.md)[Previous](AUPublic-AUBase-AUBase.cpp.md)

