---
title: AUSampler - Loading Instruments
apple_id: DTS40011217
resource_type: Technical Note
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2015-07-13'
source_url: https://developer.apple.com/library/archive/technotes/tn2283/_index.html
archived_at: '2026-07-26T19:54:10.104366Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2283

# AUSampler - Loading Instruments

The Sampler Audio Unit (AUSampler) is a audio unit instrument available with OS X Lion and iOS 5.0 or newer systems. This technical note discusses how to load instrument presets into the AUSampler audio unit.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrg4wugsbrfvke4vcbi4yq)[Loading an instrument from a AUSampler Preset File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrg4wugsbrfvke4vcbi4za)[Loading an instrument from a DLS2 sound bank or SoundFont File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrg4wugsbrfvke4vcbi4zq)[Creating a Custom Preset from Individual Audio Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrg4wugsbrfvbverkbkreu4r27ifpugvktkrhu2x2qkjcvgrkul5dfet2nl5eu4rcjkzeuivkbjrpucvkejfhv6rsjjrcvg)[Referencing External Audio Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrg4wugsbrfvke4vcbi43q)[EXS24 Instrument Files (iOS 6 or later & OS X 10.8 or later)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrg4wugsbrfvke4vcbi44a)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Instruments sit at the top of any branch of an audio unit graph and generate audio output in response to commands sent to it via the `MusicDevice` APIs for example, MIDI note on, MIDI note off, volume adjustments and so on. See `MusicDevice.h`, which part of the AudioUnit framework for more information.

Samplers are a type of instrument that organize a set of sound recordings (or "samples") into a conherent playable instrument. For example, you could load in a collection of samples representing a drum kit, acoustic piano or even some arbitrary collection of sound effects and so on.

For a comprehensive introduction to the AUSampler and how to work with audio units, see [WWDC 2011 Session #411 - Music in iOS and Mac OS X](https://developer.apple.com/videos/wwdc/2011/index.php).

[Back to Top](#)

## Loading an instrument from a AUSampler Preset File

The AUSampler has a very lightweight native property list preset format stored as a text file (.aupreset) which makes it very easy to transfer saved instruments created and auditioned on the desktop to other desktop or iOS applications.

Listing 1 presents a method to load a AUSampler preset file (.aupreset) created and saved using AULab using the `kAUSamplerProperty_LoadInstrument` property. AULab is a Apple Audio Development Tool installed with Xcode and located in the `Developer/Applications/Audio` folder.

__Listing 1__  Load an .aupreset file.

```objc
// this method assumes the class has a member called mySamplerUnit
// which is an instance of an AUSampler
-(OSStatus) loadFromPresetURL: (NSURL *)presetURL {

    OSStatus result = noErr;

    AUSamplerInstrumentData auPreset = {0};

    auPreset.fileURL = (CFURLRef) presetURL;
    auPreset.instrumentType = kInstrumentType_AUPreset;

    result = AudioUnitSetProperty(self.mySamplerUnit,
                              kAUSamplerProperty_LoadInstrument,
                              kAudioUnitScope_Global,
                              0,
                              &auPreset,
                              sizeof(auPreset));

    return result;
}
```

[Back to Top](#)

## Loading an instrument from a DLS2 sound bank or SoundFont File

The AUSampler has the ability to translate DLS and SoundFont2 preset formats into its own native internal format leveraging the large number of preexisting instruments.

The AUSampler uses the  `AUSamplerInstrumentData`structure to describe the preset to load. Three numbers are needed to identify a specific instrument in a DLS or SoundFont2 bank -- two numbers describe the bank variation and one number is used for the preset number. To select a particular instrument, the following description would be used: A most-significant and least-significant byte (MSB and LSB) for the bank, plus the preset number. All three numbers must be between 0 and 127.

__Note:__ The MSB/LSB for the bank plus a preset number are the same three values used if you were selecting a bank and preset via MIDI.

For most existing General MIDI and General Standard compatible banks, the `bankMSB` member should be set to `kAUSampler_DefaultMelodicBankMSB` to load melodic instruments, and `kAUSampler_DefaultPercussionBankMSB` for percussion instruments. The `bankLSB` member can be set to `kAUSampler_DefaultBankLSB` to load from the default bank variation (variation 0). If you know the bank contains other variations, you may use those values.

The `instrumentType` member can be `kInstrumentType_DLSPreset` or `kInstrumentType_SF2Preset` as required however note that both enums are defined as the same value.

Listing 2 presents a method to load a DLS or SoundFont bank.

__Listing 2__  Load a DLS or SoundFont Bank.

```objc
// this method assumes the class has a member called mySamplerUnit
// which is an instance of an AUSampler
-(OSStatus) loadFromDLSOrSoundFont: (NSURL *)bankURL withPatch: (int)presetNumber {

    OSStatus result = noErr;

    // fill out a instrument data structure
    AUSamplerInstrumentData instdata;
    instdata.bankURL  = (CFURLRef) bankURL;
    instdata.instrumentType = kInstrumentType_DLSPreset;
    instdata.bankMSB  = kAUSampler_DefaultMelodicBankMSB;
    instdata.bankLSB  = kAUSampler_DefaultBankLSB;
    instdata.presetID = (UInt8) presetNumber;

    // set the kAUSamplerProperty_LoadPresetFromBank property
    result = AudioUnitSetProperty(self.mySamplerUnit,
                                  kAUSamplerProperty_LoadInstrument,
                                  kAudioUnitScope_Global,
                                  0,
                                  &instdata,
                                  sizeof(instdata));

    // check for errors
    NSCAssert (result == noErr,
               @"Unable to set the preset property on the Sampler. Error code:%d '%.4s'",
               (int) result,
               (const char *)&result);

    return result;
}
```

[Back to Top](#)

## Creating a Custom Preset from Individual Audio Files

The AUSampler also allows you to load a custom preset created from a set of individual audio sample files.

To successfully create a custom preset requires some preparation of each of the audio files being used. Each audio file should have been edited appropriately to contain instrument data (for example key range, velocity range, root key) and looping information (if the audio is to be looped). The AUSampler will read this information out of the files and use it to place each file within the new instrument preset.

Listing 3 presents a method to create a preset from an array of individual audio file paths. `urlArray` should be an array of NSURLs to the audio files you wish to use.

__Listing 3__  Creating a Preset from Individual Audio Files.

```objc
// this method assumes the class has a member called mySamplerUnit
// which is an instance of an AUSampler
-(OSStatus) createPresetFromSamples: (NSArray *)urlArray {

    CFArrayRef urlArrayRef = (CFArrayRef)urlArray;

    return result = AudioUnitSetProperty(self.mySamplerUnit,
                                         kAUSamplerProperty_LoadAudioFiles,
                                         kAudioUnitScope_Global,
                                         0,
                                         &urlArrayRef,
                                         sizeof(urlArrayRef));
}
```

__Note:__ Developers who would like to create audio sample files containing instrument data and looping information for use with the AUSampler (and any other application using samples or loops) should become familiar with the [Core Audio File Format Specification](https://developer.apple.com/library/mac/#documentation/MusicAudio/Reference/CAFSpec/CAF_intro/CAF_intro.html#//apple_ref/doc/uid/TP40001862-CH203-DontLinkElementID_61).

The Instrument Chunk `kCAF_InstrumentChunkID` is part of the Music Metadata Chunks. See the `CAFInstrumentChunk` structure in `CAFile.h`. The Audio File `AudioFileSetUserData` API may be used to set this data.

Looping is specified using a Region List property (`kAudioFilePropertyRegionList`) describing a segment of looped audio data and can be set with the `AudioFileSetProperty` API.

See `AudioFile.h` for more information.

[Back to Top](#)

## Referencing External Audio Files

When the AUSampler attempts to load audio files via the paths provided in the external file refs portion of an .aupreset file or a set of individual file URLs, it will use the following rules to resolve each path:

- If the audio file is found at the original path, it is loaded.
- If the audio file is __NOT__ found, the AUSampler looks to see if a path includes a portion matching "`/Sounds/`", "`/Sampler Files/`" or "`/Apple Loops/`" in that order.
- If the path __DOES NOT__ include one of the listed sub-paths, an error is returned.
- If the path __DOES__ include one of the listed sub-paths, the portion of the path preceding the sub-path is removed and the following directory location constants are substituted in the following order:

1. `Bundle Directory`
2. `NSLibraryDirectory` (__NOTE:__ Only on OS X)
3. `NSDocumentDirectory`
4. `NSDownloadsDirectory`

For example, in an __iOS application__ if the original path was `/Users/geddy/Library/Audio/Sounds/MyFavoriteHeadacheSound.caf` and this path was not found, the AUSampler would then search for the audio file in the following four places:

```
<Bundle_Directory>/Sounds/MyFavoriteHeadacheSound.caf
<NSDocumentDirectory>/Sounds/MyFavoriteHeadacheSound.caf
<NSDownloadsDirectory>/Sounds/MyFavoriteHeadacheSound.caf
```

Therefore using the above example, if you were moving a preset created on the Desktop to an iOS application you must place the MyFavoriteHeadacheSound.caf file in a folder called __Sounds__ within your application bundle and the AUSampler will find the audio file referenced by the preset.

[Back to Top](#)

## EXS24 Instrument Files (iOS 6 or later & OS X 10.8 or later)

EXS24 instrument files contain an internal list of the audio sample files that need to be loaded for each instrument. This internal list uses full paths for each sample file, for example Garage Band instrument paths all start with `/Library/Application Support/GarageBand/Instrument Library/Sampler/Sampler Files/...`.

In order for the AUSampler to remap these files, a directory tree must be created within your application bundle that matches the __instrument specific__ part of the path where the audio files were located.

__Note:__ The same basic path rules discussed in the Referencing External Audio Files section of this document apply for EXS24 samples. The difference is that the directory __Sounds__ is replaced with the __instrument specific__ part of a EXS24 instrument path.

Using an EXS24 instrument that was reading audio sample files from:

```
/Library/Application Support/Logic/EXS Factory Samples/10 Legacy Instruments/02 Guitars/Steel String Acoustic 2/...
```

Would require placing those same audio files in the instrument specific directory tree within your applications bundle that looks like this:

```
EXS Factory Samples/10 Legacy Instruments/02 Guitars/Steel String Acoustic 2/...
```

For example, in an iOS application if the original desktop path for the instrument was `/Library/Application Support/Logic/EXS Factory Samples/10 Legacy Instruments/02 Guitars/Steel String Acoustic 2/`, the AUSampler will remap what it finds in the EXS24 instrument lists as long as the path looks the same from `EXS Factory Samples/` on down.

```
<Bundle_Directory>/EXS Factory Samples/10 Legacy Instruments/02 Guitars/Steel String Acoustic 2/...
```

This is true for GarageBand instruments as well (those that are installed in the GarageBand directory and not the Logic directory). In the GarageBand case the instrument specific part of the path is specified by a directory tree starting with __Sampler Files__ instead of __EXS Factory Samples__.

```
<Bundle_Directory>/Sampler Files/Pop Brass Section/...
```

__Important:__ For Logic Pro X the EXS24 sampler format has been extended to include a few new features/parameters used to build __some__ complex instruments for the Logic Pro X library. Due to the nature of these new extended features (for example Audio File Tail), the AUSampler will not be able to load or use these instruments correctly.

When the AUSampler cannot support a specific feature/parameter which negatively impacts instrument use, attempting to load the instrument will return a  `kAudioUnitErr_FormatNotSupported -10868` error.

However __not all versions__ of the AUSampler will return the format error for files that parse correctly even if the AUSampler cannot handle a feature/parameter. The only indication of an issue is a warning message to the system log as the AUSampler parses and attempts to run the instrument the best it can.

__AUSampler Instrument Support:__

- All Logic Pro 9 factory instruments

- A large number of the factory Logic Pro X EXS24 files, however __some complex instruments may not__ work.

- Any EXS24 instrument created in Logic Pro 9, or Logic Pro X not making use of new features/parameters.

The above should not adversely impact developers using the AUSampler to play original content created in Logic Pro X or Logic Pro 9.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-07-13 | Updated Referencing External Audio Files section |
| 2015-03-25 | Updated listing 1 to use kAUSamplerProperty_LoadInstrument, listing 2 to use AUSamplerInstrumentData and added information regarding Logic Pro X EXS24 instrument compatibility. |
| 2014-05-06 | Editorial |
| 2012-12-05 | Added EXS24 section for iOS 6.0 & OS X 10.8+ |
| 2011-09-09 | New document that discusses and demonstrates how to load instrument presets into the AUSampler audio unit. |

