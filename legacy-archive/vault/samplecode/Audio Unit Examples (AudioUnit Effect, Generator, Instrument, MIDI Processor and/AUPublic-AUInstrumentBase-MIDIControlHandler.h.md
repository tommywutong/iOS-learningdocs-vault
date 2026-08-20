---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_AUInstrumentBase_MIDIControlHandler_h.html
archived_at: '2026-07-26T19:54:12.701632Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-AUInstrumentBase-SynthElement.h.md)[Previous](AUPublic-AUInstrumentBase-SynthNoteList.h.md)

# AUPublic/AUInstrumentBase/MIDIControlHandler.h

```swift
#ifndef __MIDICONTROLHANDLER_H__
#define __MIDICONTROLHANDLER_H__

#include <CoreAudio/CoreAudio.h>

/*! Abstract interface base class for classes which handle all incoming MIDI data */

class MIDIControlHandler
{
public:
    virtual         ~MIDIControlHandler() {}
    virtual void    Reset() = 0;                                //! Restore all state to defaults
    virtual bool    SetProgramChange(UInt16 inProgram) = 0;
    virtual bool    SetPitchWheel(UInt16 inValue) = 0;
    virtual bool    SetChannelPressure(UInt8 inValue) = 0;
    virtual bool    SetPolyPressure(UInt8 inKey, UInt8 inValue) = 0;
    virtual bool    SetController(UInt8 inControllerNumber, UInt8 inValue) = 0;
    virtual bool    SetSysex(void *inSysexMsg) = 0;

    virtual float   GetPitchBend() const = 0;

    /*! Default controller values.  These represent MSB values unless indicated in the name */

    enum
    {
        kDefault_Midpoint               = 0x40,     //! Used for all center-null-point controllers
        kDefault_Volume             = 100,
        kDefault_Pan                    = kDefault_Midpoint,
        kDefault_ModWheel               = 0,
        kDefault_Pitch                  = kDefault_Midpoint,
        kDefault_Expression         = 0x7f,
        kDefault_ChannelPressure    = 0,
        kDefault_ReverbSend         = 40,
        kDefault_ChorusSend         = 0,

        kDefault_RPN_LSB                = 0x7f,
        kDefault_RPN_MSB                = 0x7f,
        kDefault_PitchBendRange     = 2,
        kDefault_FineTuning         = kDefault_Midpoint,
        kDefault_CoarseTuning       = kDefault_Midpoint,
        kDefault_ModDepthRange      = 0,
        kDefault_ModDepthRangeLSB   = kDefault_Midpoint
    };
};

#endif  // __MIDICONTROLHANDLER_H__
```

[Next](AUPublic-AUInstrumentBase-SynthElement.h.md)[Previous](AUPublic-AUInstrumentBase-SynthNoteList.h.md)

