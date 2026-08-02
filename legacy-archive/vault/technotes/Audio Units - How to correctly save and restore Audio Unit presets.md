---
title: Audio Units - How to correctly save and restore Audio Unit presets.
apple_id: DTS40011953
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2013-08-09'
source_url: https://developer.apple.com/library/archive/technotes/tn2157/_index.html
archived_at: '2026-07-26T19:54:10.197051Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2157

# Audio Units - How to correctly save and restore Audio Unit presets.

Applications that host Audio Units can take advantage of the Audio Unit preset mechanism. Presets give users a quick method of choosing a combination of settings for an audio unit, without going through the hassle of making adjustments everytime an Audio Unit gets loaded.

An Audio Unit can have a specific state at any given time. The state of an audio unit refers to the internal values that can affect its behavior; in most cases, these are the parameters. Audio Units tend to have large amounts of these internal values, making it is useful to allow these values to be saved and restored as presets for later use.

These states can be either shipped with an Audio Unit, or saved in a file format, that can be loaded by a hosting application.

Factory Presets are a set of pre-defined audio unit settings that are shipped with an Audio Unit. They usually define common settings that an Audio Unit will ordinarily use. For example, a reverb Audio Unit might want to include several factory presets such as a small room or a large hall.

User states are custom settings that can be created by a user. Essentially, a user state is a snapshot of the current settings on an audio unit at any given time, which could be stored in a file format.

[Finding presets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvgmwugsbrfvdestsekbjeku2fkrjq)[Factory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvgmwugsbrfvddc)[Custom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvgmwugsbrfvdfami)[Restoring a preset from file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvgmwugsbrfvjeku2uj5jek)[Saving Custom User Presets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvgmwugsbrfvbuyqktkncecvcb)[Conclusion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvgmwugsbrfvbu6tsd)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Finding presets

### Factory

Factory presets can be retrieved from an audio unit by using the method `AudioUnitGetProperty` with the `kAudioUnitProperty_FactoryPresets` property.

__Listing 1__  Factory Presets

```
 CFArrayRef presets = NULL;
    propertySize = sizeof(presets);
    err = AudioUnitGetProperty(SomeAudioUnit,
                               kAudioUnitProperty_FactoryPresets,
                               kAudioUnitScope_Global,
                               0,
                               &presets,
                               &propertySize);
```

### Custom

Presets can also be read off disk and used to set the state of an audio unit. These presets are stored on disk in one of these three locations with the extension .aupreset:

- User Domain - ~/Library/Audio/Presets/
- Local Domain - /Library/Audio/Presets/
- Network Domain - /Network/Library/Audio/Presets/

Presets stored within these directories must be organized in deeper directories by manufacturer name and Audio Unit name. This is the only way to associate a preset with it's accompanying Audio Unit. For example, the presets of the SampleEffect Audio Unit included the Core Audio SDK are stored in:

- ~/Library/Audio/Presets/Acme Inc/SampleEffectUnit/MyPreset.aupreset

__Important:__ Applications can use CAFileHandling class included in the CoreAudio SDK to scan, locate, and save .aupreset files.

[Back to Top](#)

## Restoring a preset from file

The class info property represents the current state of an audio unit. This property is stored in a `CFPropertyListRef`, which is an XML format, which can be cast to a `CFDictionaryRef` or an `NSDictionary`. After locating and obtaining audio unit state information from an .aupreset file, you can restore the audio unit with the state information by using the method `AudioUnitSetProperty` with `kAudioUnitProperty_ClassInfo`.

__Listing 2__  Restoring Presets

```
 AudioUnitSetProperty(theAudioUnit,
                            kAudioUnitProperty_ClassInfo,
                            kAudioUnitScope_Global,
                            0,
                            &inClassInfo,
                            sizeof(inClassInfo)));

    // now that we've potentially changed the values of the parameter we
    // should notify any listeners of this change:
    AudioUnitParameter changedUnit;
    changedUnit.mAudioUnit = theAudioUnit;
    changedUnit.mParameterID = kAUParameterListener_AnyParameter;
    RequireNoErr (AUParameterListenerNotify (NULL, NULL, &changedUnit));
```

__Important:__ Be sure to notify all parameter listeners that the values of the audio unit has changed.

[Back to Top](#)

## Saving Custom User Presets

To save an audio unit state to an .aupreset file, you must set the audio unit to reflect the new preset and obtain the class info to be saved to disk.

Before retrieving the current state, you must create a new AUPreset and set it as the present preset using the property ID `kAudioUnitProperty_PresentPreset`. The AUPreset should have a name and have a preset number less than zero. Setting this property will name the new preset you are creating and will be included when you fetch the audio unit state information later to save as a file.

__Listing 3__  Saving Presets

```
 AUPreset myPreset;
    myPreset.presetNumber = -1; //should be less than zero ,(user preset)
    myPreset.presetName = CFSTR("Name of New Preset");

    AudioUnitSetProperty(SomeAudioUnit,
                         kAudioUnitProperty_PresentPreset,
                         kAudioUnitScope_Global,
                         0,
                         &myPreset,
                         sizeof(AUPreset));
```

To obtain the current state from an audio unit, use `AudioUnitGetProperty` with the `kAudioUnitProperty_ClassInfo` property. An example is below:

__Listing 4__  Getting the class info (current settings)

```
 CFPropertyListRef  myClassData;

    UInt32 size = sizeof(CFPropertyListRef);
    AudioUnitGetProperty(SomeAudioUnit,
                         kAudioUnitProperty_ClassInfo,
                         kAudioUnitScope_Global,
                         0,
                         &myClassData,
                         &size);
```

After retrieving the current state information, save this data as an .aupreset file in the local, user, or network domain as described above.

[Back to Top](#)

## Conclusion

Audio Unit Presets eases the burden put on users to manually reset the state of an audio unit every time it is loaded. Presets make using audio units and their hosting application much easier for users.

- [Audio Components and the Application Sandbox](https://developer.apple.com/library/mac/#technotes/tn2247/_index.html#//apple_ref/doc/uid/DTS40012567)
- [Audio Documentation](https://developer.apple.com/library/mac/navigation/index.html#section=Topics&topic=Audio%20%26amp%3B%20Video)
- [Audio Unit Programming Guide](https://developer.apple.com/documentation/MusicAudio/Conceptual/AudioUnitProgrammingGuide/index.html)
- [Core Audio Overview](https://developer.apple.com/library/mac/#documentation/MusicAudio/Conceptual/CoreAudioOverview/Introduction/Introduction.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-09 | Corrected minor bug in Listing 3 that would cause it to return a kAudioUnitErr_InvalidPropertyValue. |
| 2012-03-06 | New document that illustrates how applications hosting Audio Units correctly save and restore audio unit presets. |

