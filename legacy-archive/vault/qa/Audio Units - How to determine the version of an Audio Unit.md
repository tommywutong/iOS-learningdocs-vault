---
title: Audio Units - How to determine the version of an Audio Unit
apple_id: DTS10003489
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2013-07-30'
source_url: https://developer.apple.com/library/archive/qa/qa1408/_index.html
archived_at: '2026-07-18T02:30:31.958680Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1408

# Audio Units - How to determine the version of an Audio Unit

## Q:  How do I determine the version of an Audio Unit I am using?

A: Core Audio uses the Audio Component API to make Audio Units available as a system-wide resource. After obtaining a valid instance of an Audio Unit, you can use `AudioComponentGetVersion` to get the version number.

This can be useful when you require a specific version of an Audio Unit with updated or different features and you want to determine which version is installed before using the Audio Unit.

Listing 1 demonstrates how to ensure you have at least version 2.0 of the 3D Mixer audio unit installed.

__Listing 1__  Checking the 3D Mixer Version.

```
// The Version format is 0xMMMMmmbb
// The digits M/m/b are stored in BCD (Binary Coded Decimal) format for numbers greater than 9
// A version number for 10.3.1 would be: 0x100301
// A version number for 2.3.1 would be: 0x20301

#define kPreferredMixerVersion  0x20400
#define kMinimumMixerVersion    0x20000

...

    // if the returned version is less than 0x20000
    // it's not the 3DMixer we're looking for, move along...
    UInt32 mixerVersion = kMinimumMixerVersion;

    if ( Is3DMixerVersionValid(&mixerVersion) ) {
        // yes, we can work with it

        // your code here...
        printf("Version Number Returned 0x%x", (unsigned int)mixerVersion);
    }

...

bool Is3DMixerVersionValid(UInt32 *ioVersionNumber)
{
    bool isVersionValid = false;
    UInt32 theVersionNumber = 0;

    if (NULL == ioVersionNumber) return false;

    AudioComponentDescription mixer3D_desc = { kAudioUnitType_Mixer,
                                               kAudioUnitSubType_3DMixer,
                                               kAudioUnitManufacturer_Apple,
                                               0, 0 };


    AudioComponent mixer3D_component = AudioComponentFindNext(0, &mixer3D_desc);
    if (NULL == mixer3D_component) return false;

    if (AudioComponentGetVersion(mixer3D_component, &theVersionNumber)) return false;

    if (theVersionNumber >= *ioVersionNumber){
        isVersionValid = true;
        *ioVersionNumber = theVersionNumber; // validated this pointer on entry
    }

    return isVersionValid;
}
```

See `AudioComponent.h` for more information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-07-30 | Updated to use Audio Component API. Updated description of version format & added examples. |
| 2005-03-07 | Changed code of Is3DMixerVersionValid(). Added information about Version format (BCD). |
| 2005-02-03 | New document that demonstrates how to find the version number of an Audio Unit. |

