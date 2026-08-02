---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPublic_AUBase_AUPlugInDispatch_h.html
archived_at: '2026-07-18T02:59:49.418083Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPublic-AUBase-AUScopeElement.cpp.md)[Previous](AUPublic-AUBase-AUPlugInDispatch.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPublic/AUBase/AUPlugInDispatch.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
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
#endif // CA_BASIC_AU_FEATURES

#endif // __AUPlugInBase_h__
```

[Next](AUPublic-AUBase-AUScopeElement.cpp.md)[Previous](AUPublic-AUBase-AUPlugInDispatch.cpp.md)

