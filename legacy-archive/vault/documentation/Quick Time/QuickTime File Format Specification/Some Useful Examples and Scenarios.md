---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFChap5/qtff5.html
archived_at: '2026-07-27T06:57:06.697212Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](QuickTime%20Image%20File%20Format.md)[Previous](Basic%20Data%20Types.md)

# Some Useful Examples and Scenarios

This chapter contains a number of examples that can help you pull together all of the material in this book by examining the atom structure that results from a number of different scenarios.

The chapter is divided into the following topics:

- [Creating, Copying, and Disposing of Atom Containers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsg43q) discusses the various ways you can work with atom containers, along with illustrations and sample code that show usage.
- [Preparing Sound and Subtitle Alternate Groups for Use with Apple Devices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzu) discusses how multiple tracks with different languages can be associated with each other.
- [Creating an Effect Description](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojshayq) discusses how you create an effect description by creating an atom container, inserting a QT atom that specifies the effect, and inserting a set of QT atoms that set its parameters.
- [Creating Movies with Modifier Tracks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsha2q) provides sample code showing you how to create a movie with modifier tracks.
- [Authoring Movies with External Movie Targets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsha4q) discusses how to author movies with external targets.
- [Creating Video Tracks at 30 Frames per Second](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojshe3q) discusses creating 30 fps video.
- [Creating Video Tracks at 29.97 Frames per Second](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtgazq) describes creating 29.97 fps video.
- [Creating Sound Tracks at 44.1 kHz](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtga3q) provides an example of creating a sound track.
- [Creating a Timecode Track for 29.97 FPS Video](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtgeyq) presents a timecode track example.
- [Playing with Edit Lists](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtge2q) discusses how to interpret edit list data.
- [Interleaving Movie Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtge4q) shows how a movie’s tracks are interleaved in the movie data file.
- [Referencing Two Data Files With a Single Track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtgizq) shows how track data may reside in more than one file.
- [Getting the Name of a QuickTime VR Node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtgi3q) discusses how you can use standard QuickTime atom container functions to retrieve the information in a QuickTime VR node header atom.
- [Adding Custom Atoms in a QuickTime VR Movie](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtgmyq) describes how to add custom atoms to either the QuickTime VR world or node information atom containers.
- [Adding Atom Containers in a QuickTime VR Movie](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtgm2q) shows the code you would use to add VR world and node information atom containers to a QTVR track.
- [Optimizing QuickTime VR Movies for Web Playback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojtgm4q) describes how to use the QTVR Flattener, a movie export component that converts an existing QuickTime VR single node movie into a new movie that is optimized for viewing on the Web.

## Creating, Copying, and Disposing of Atom Containers

Before you can add atoms to an atom container, you must first create the container by calling `QTNewAtomContainer`. The code sample shown in [Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbsgi3q) calls `QTNewAtomContainer` to create an atom container.

__Listing 6-1__  Creating a new atom container

```
QTAtomContainer spriteData;
OSErr err
// create an atom container to hold a sprite’s data
err=QTNewAtomContainer (&spriteData);
```

When you have finished using an atom container, you should dispose of it by calling the `QTDisposeAtomContainer` function. The sample code shown in [Listing 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbsgm4a) calls `QTDisposeAtomContainer` to dispose of the `spriteData` atom container.

__Listing 6-2__  Disposing of an atom container

```
if (spriteData)
    QTDisposeAtomContainer (spriteData);
```

### Creating New Atoms

You can use the `QTInsertChild` function to create new atoms and insert them in a QT atom container. The `QTInsertChild` function creates a new child atom for a parent atom. The caller specifies an atom type and atom ID for the new atom. If you specify a value of 0 for the atom ID, `QTInsertChild` assigns a unique ID to the atom.

`QTInsertChild` inserts the atom in the parent’s child list at the index specified by the `index` parameter; any existing atoms at the same index or greater are moved toward the end of the child list. If you specify a value of 0 for the `index` parameter, `QTInsertChild` inserts the atom at the end of the child list.

The code sample in [Listing 6-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbsguzq) creates a new QT atom container and calls `QTInsertChild` to add an atom. The resulting QT atom container is shown in [Figure 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsga3q). The offset value 10 is returned in the `firstAtom` parameter.

__Listing 6-3__  Creating a new QT atom container and calling `QTInsertChild` to add an atom.

```
QTAtom firstAtom;
QTAtomContainer container;
OSErr err
err = QTNewAtomContainer (&container);
if (!err)
    err = QTInsertChild (container, kParentAtomIsContainer, 'abcd',
        1000, 1, 0, nil, &firstAtom);
```

__Figure 6-1__  QT atom container after inserting an atom

（原归档配图获取待重试：`qtml_07.gif`）

The following code sample calls `QTInsertChild` to create a second child atom. Because a value of 1 is specified for the `index` parameter, the second atom is inserted in front of the first atom in the child list; the index of the first atom is changed to 2. The resulting QT atom container is shown in [Figure 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsgeyq).

```
QTAtom secondAtom;

FailOSErr (QTInsertChild (container, kParentAtomIsContainer, 'abcd',
    2000, 1, 0, nil, &secondAtom));
```

__Figure 6-2__  QT atom container after inserting a second atom

（原归档配图获取待重试：`qtml_08.gif`）

You can call the `QTFindChildByID` function to retrieve the changed offset of the first atom that was inserted, as shown in the following example. In this example, the `QTFindChildByID` function returns an offset of 20.

```
firstAtom = QTFindChildByID (container, kParentAtomIsContainer,  'abcd',
    1000, nil);
```

[Listing 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbsg4ya) shows how the `QTInsertChild` function inserts a leaf atom into the atom container `sprite`. The new leaf atom contains a sprite image index as its data.

__Listing 6-4__  Inserting a child atom

```
if ((propertyAtom = QTFindChildByIndex (sprite, kParentAtomIsContainer,
    kSpritePropertyImageIndex, 1, nil)) == 0)

    FailOSErr (QTInsertChild (sprite, kParentAtomIsContainer,
        kSpritePropertyImageIndex, 1, 1, sizeof(short),&imageIndex,
        nil));
```

### Copying Existing Atoms

QuickTime provides several functions for copying existing atoms within an atom container. The `QTInsertChildren` function inserts a container of atoms as children of a parent atom in another atom container. [Figure 6-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsge2q) shows two example QT atom containers, A and B.

__Figure 6-3__  Two QT atom containers, A and B

（原归档配图获取待重试：`qtml_09.gif`）

The following code sample calls `QTFindChildByID` to retrieve the offset of the atom in container A. Then, the code sample calls the `QTInsertChildren` function to insert the atoms in container B as children of the atom in container A. [Figure 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsge4q) shows what container A looks like after the atoms from container B have been inserted.

```
QTAtom targetAtom;

targetAtom = QTFindChildByID (containerA, kParentAtomIsContainer,  'abcd',
    1000, nil);

FailOSErr (QTInsertChildren (containerA, targetAtom, containerB));
```

__Figure 6-4__  QT atom container after child atoms have been inserted

（原归档配图获取待重试：`qtml_10.gif`）

In [Listing 6-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbshayq), the `QTInsertChild` function inserts a parent atom into the atom container `theSample`. Then, the code calls `QTInsertChildren` to insert the container `theSprite` into the container `theSample`. The parent atom is `newSpriteAtom`.

__Listing 6-5__  Inserting a container into another container

```
FailOSErr (QTInsertChild (theSample, kParentAtomIsContainer,
    kSpriteAtomType, spriteID, 0, 0, nil, &newSpriteAtom));

FailOSErr (QTInsertChildren (theSample, newSpriteAtom, theSprite));
```

QuickTime provides three other functions you can use to manipulate atoms in an atom container. The `QTReplaceAtom` function replaces an atom and its children with a different atom and its children. You can call the `QTSwapAtoms` function to swap the contents of two atoms in an atom container; after swapping, the ID and index of each atom remains the same. The `QTCopyAtom` function copies an atom and its children to a new atom container.

### Retrieving Atoms From an Atom Container

QuickTime provides functions you can use to retrieve information about the types of a parent atom’s children, to search for a specific atom, and to retrieve a leaf atom’s data.

You can use the `QTCountChildrenOfType` and `QTGetNextChildType` functions to retrieve information about the types of an atom’s children. The `QTCountChildrenOfType` function returns the number of children of a given atom type for a parent atom. The `QTGetNextChildType` function returns the next atom type in the child list of a parent atom.

You can use the `QTFindChildByIndex`, `QTFindChildByID`, and `QTNextChildAnyType` functions to retrieve an atom. You call the `QTFindChildByIndex` function to search for and retrieve a parent atom’s child by its type and index within that type.

[Listing 6-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbsheza) shows the sample code function `SetSpriteData`, which updates an atom container that describes a sprite. (For more information about sprites and the Sprite Toolbox, refer to the book Programming With Wired Movies and Sprite Animation, available at `http://developer.apple.com/techpubs/quicktime/qtdevdocs/RM/PDF.htm`.) For each property of the sprite that needs to be updated, `SetSpriteData` calls `QTFindChildByIndex` to retrieve the appropriate atom from the atom container. If the atom is found, `SetSpriteData` calls `QTSetAtomData` to replace the atom’s data with the new value of the property. If the atom is not found, `SetSpriteData` calls `QTInsertChild` to add a new atom for the property.

__Listing 6-6__  Finding a child atom by index

```
OSErr SetSpriteData (QTAtomContainer sprite, Point *location,
    short *visible, short *layer, short *imageIndex)
{
    OSErr err = noErr;
    QTAtom propertyAtom;

    // if the sprite’s visible property has a new value
    if (visible)
    {
        // retrieve the atom for the visible property --
        // if none exists, insert one
        if ((propertyAtom = QTFindChildByIndex (sprite,
            kParentAtomIsContainer, kSpritePropertyVisible, 1,
            nil)) == 0)
            FailOSErr (QTInsertChild (sprite, kParentAtomIsContainer,
                kSpritePropertyVisible, 1, 1, sizeof(short), visible,
                nil))

        // if an atom does exist, update its data
        else
            FailOSErr (QTSetAtomData (sprite, propertyAtom,
                sizeof(short), visible));
    }

    // ...
    // handle other sprite properties
    // ...
}
```

You can call the `QTFindChildByID` function to search for and retrieve a parent atom’s child by its type and ID. The sample code function `AddSpriteToSample`, shown in [Listing 6-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbtga3q), adds a sprite, represented by an atom container, to a key sample, represented by another atom container. `AddSpriteToSample` calls `QTFindChildByID` to determine whether the atom container `theSample` contains an atom of type `kSpriteAtomType` with the ID `spriteID`. If not, `AddSpriteToSample` calls `QTInsertChild` to insert an atom with that type and ID. A value of 0 is passed for the `index` parameter to indicate that the atom should be inserted at the end of the child list. A value of 0 is passed for the `dataSize` parameter to indicate that the atom does not have any data. Then, `AddSpriteToSample` calls `QTInsertChildren` to insert the atoms in the container `theSprite` as children of the new atom. `FailIf` and `FailOSErr` are macros that exit the current function when an error occurs.

__Listing 6-7__  Finding a child atom by ID

```
OSErr AddSpriteToSample (QTAtomContainer theSample,
    QTAtomContainer theSprite, short spriteID)
{
    OSErr err = noErr;
    QTAtom newSpriteAtom;

    FailIf (QTFindChildByID (theSample, kParentAtomIsContainer,
        kSpriteAtomType, spriteID, nil), paramErr);

    FailOSErr (QTInsertChild (theSample, kParentAtomIsContainer,
        kSpriteAtomType, spriteID, 0, 0, nil, &newSpriteAtom));
    FailOSErr (QTInsertChildren (theSample, newSpriteAtom, theSprite));
}
```

Once you have retrieved a child atom, you can call `QTNextChildAnyType` function to retrieve subsequent children of a parent atom. `QTNextChildAnyType` returns an offset to the next atom of any type in a parent atom’s child list. This function is useful for iterating through a parent atom’s children quickly.

QuickTime also provides functions for retrieving an atom’s type, ID, and data. You can call `QTGetAtomTypeAndID` function to retrieve an atom’s type and ID. You can access an atom’s data in one of three ways.

- To copy an atom’s data to a handle, you can use the `QTCopyAtomDataToHandle` function.
- To copy an atom’s data to a pointer, you can use the `QTCopyAtomDataToPtr` function.
- To access an atom’s data directly, you should lock the atom container in memory by calling `QTLockContainer`. Once the container is locked, you can call `QTGetAtomDataPtr` to retrieve a pointer to an atom’s data. When you have finished accessing the atom’s data, you should call the `QTUnlockContainer` function to unlock the container in memory.

### Modifying Atoms

QuickTime provides functions that you can call to modify attributes or data associated with an atom in an atom container. To modify an atom’s ID, you call the function `QTSetAtomID`.

You use the `QTSetAtomData` function to update the data associated with a leaf atom in an atom container. The `QTSetAtomData` function replaces a leaf atom’s data with new data. The code sample in [Listing 6-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbtgmza) calls `QTFindChildByIndex` to determine whether an atom container contains a sprite’s visible property. If so, the sample calls `QTSetAtomData` to replace the atom’s data with a new visible property.

__Listing 6-8__  Modifying an atom’s data

```
QTAtom propertyAtom;

// if the atom isn’t in the container, add it
if ((propertyAtom = QTFindChildByIndex (sprite, kParentAtomIsContainer,
    kSpritePropertyVisible, 1, nil)) == 0)
    FailOSErr (QTInsertChild (sprite, kParentAtomIsContainer,
        kSpritePropertyVisible, 1, 0, sizeof(short), visible, nil))

// if the atom is in the container, replace its data
else
    FailOSErr (QTSetAtomData (sprite, propertyAtom, sizeof(short),
        visible));
```

### Removing Atoms From an Atom Container

To remove atoms from an atom container, you can use the `QTRemoveAtom` and `QTRemoveChildren` functions. The `QTRemoveAtom` function removes an atom and its children, if any, from a container. The `QTRemoveChildren` function removes an atom’s children from a container, but does not remove the atom itself. You can also use `QTRemoveChildren` to remove all the atoms in an atom container. To do so, you should pass the constant `kParentAtomIsContainer` for the `atom` parameter.

The code sample shown in [Listing 6-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbtgyya) adds override samples to a sprite track to animate the sprites in the sprite track. The `sample` and `spriteData` variables are atom containers. The `spriteData` atom container contains atoms that describe a single sprite. The `sample` atom container contains atoms that describes an override sample.

Each iteration of the `for` loop calls `QTRemoveChildren` to remove all atoms from both the `sample` and the `spriteData` containers. The sample code updates the index of the image to be used for the sprite and the sprite’s location and calls `SetSpriteData` ([Listing 6-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbsheza)), which adds the appropriate atoms to the `spriteData` atom container. Then, the sample code calls `AddSpriteToSample` ([Listing 6-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbtga3q)) to add the `spriteData` atom container to the `sample` atom container. Finally, when all the sprites have been updated, the sample code calls `AddSpriteSampleToMedia` to add the override sample to the sprite track.

__Listing 6-9__  Removing atoms from a container

```
QTAtomContainer sample, spriteData;

// ...
// add the sprite key sample
// ...

// add override samples to make the sprites spin and move
for (i = 1; i <= kNumOverrideSamples; i++)
{
    QTRemoveChildren (sample, kParentAtomIsContainer);
    QTRemoveChildren (spriteData, kParentAtomIsContainer);

    // ...
    // update the sprite:
    // - update the imageIndex
    // - update the location
    // ...

    // add atoms to spriteData atom container
    SetSpriteData (spriteData, &location, nil, nil, &imageIndex);

    // add the spriteData atom container to sample
    err = AddSpriteToSample (sample, spriteData, 2);

    // ...
    // update other sprites
    // ...

    // add the sample to the media
    err = AddSpriteSampleToMedia (newMedia, sample,
        kSpriteMediaFrameDuration, false);
}
```

## Preparing Sound and Subtitle Alternate Groups for Use with Apple Devices

Alternate groups are collections of tracks that all serve the same purpose, where any track in the group can be substituted for another in a movie. Members of the same alternate group have the same identifier value in the alternate group field in the `'tkhd'` (track header) atom; see [Track Reference Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwga2a) for an example of alternate tracks for different languages.

This section provides guidelines for the use of alternate groups in movies to be played on Apple devices.

### General

For each alternate group:

- The group must contain tracks of only one type; for example, only subtitle tracks or only sound tracks.
- All tracks of the same type must be in a single alternate group.
- One track in the group must be enabled; that is, the Track Enabled flag must be set (0x0001) in its track header (`'tkhd'`).
- All other tracks in the group must be disabled.

### Alternate Subtitle Tracks

For an alternate group that contains multiple subtitle (`'sbtl'`) tracks:

- The player must pick a subtitle track even when subtitle display is turned off.
- If any of the requirements stated in [General](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzw) does not hold, players may act as though there is no alternate subtitle track information.

As described in [Subtitle Sample Data](Media%20Data%20Atom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygi), a subtitle track can contain any combination of forced (must be displayed) and non-forced (optionally displayed) subtitle samples, including the possibility of a track that contains only forced subtitle samples. Even if a user indicates, directly or indirectly, that no subtitles should be displayed, any available appropriate subtitle track should be enabled so that any forced subtitles in the track can be displayed. A means by which a player can make a default selection among subtitle alternates in the absence of a user selection is covered in [Relationships Across Alternate Groups](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzz).

For each language in a subtitle alternate group, subtitle tracks can be configured in either of the following ways:

- Single track: Contains any combination of forced and non-forced (regular) subtitle samples.
- Track pairs: One track contains any combination of forced and non-forced (regular) subtitle samples and has a track reference of type `'forc'` that references the second track, which contains only forced samples, as described in [Subtitle Sample Data](Media%20Data%20Atom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygi).

If the user or player picks the language of a track pair, the player application then selects the appropriate track of the pair. It must select the regular subtitle track if subtitle display is on or the forced-only subtitle track if subtitle display is off.

If a track pair is present in a subtitle alternate group, a player that displays the track languages of subtitle tracks may choose to list the language only once. If a player lists both tracks of the pair, the player should display some kind of distinction between the tracks (for example, including the track names from the `'tnam'` user data in a menu).

### Alternate Sound Tracks

For an alternate group that contains multiple sound (`'soun'`) tracks:

- If more than one alternate group contains sound tracks, the alternate group that contains the enabled sound track should be considered to be the primary alternate sound track group. Other alternate groups containing sound tracks should be ignored.
- If there is more than one enabled sound track, or if there is an enabled sound track and a non-sound track inside the same alternate group, the player may act as though there is no alternate sound track information.
- Players may ignore sound tracks that use codecs that are unavailable.

### Relationships Across Alternate Groups

An audio alternate group and subtitle alternate group may need to use different languages because the first is the spoken language and the second is the written language and the BCP 47 language tags may differ. If there is not a need to differentiate, tracks in both alternate groups should use the same language code and optionally extended language tag.

Sound tracks can have a track reference of type `'folw'` (for “follows”) to a single subtitle track; this track is the default to select if the sound track is selected. Use of a `'folw'` reference is a fallback in cases where the language tagging cannot be used for some reason (for example, the written language and spoken language use different extended language tags, as with Norwegian).

All subtitle tracks found in a subtitle track alternate group are candidate tracks for any chosen sound track. No facility to restrict the set of available subtitle tracks for a particular selected sound track is currently defined. However, to guide a player's behavior in making a selection among subtitle alternates in the absence of a user selection or preference, a single subtitle track may be associated with a sound track as follows:

- A sound track may include a `'folw'` (“follows”) track reference to a corresponding subtitle track.
- If a sound track has a `'folw'` track reference to a subtitle track, that referenced subtitle track is the default subtitle track for that sound track.
- Each sound track can have either zero or one 'folw' track references to a subtitle track.
- If a subtitle track pair is to be made the default, the sound track should have a `'folw'` track reference to the forced subtitle track of the track pair.
- If there is no `'folw'` track reference to a subtitle track, a player most commonly determines the default subtitle track by matching aspects of the audio and subtitle tracks, typically by matching the extended language tag (or language code if there is no language tag) in the set of candidate tracks.

  If no match is found by language, a player might choose another candidate track based upon a user preference (for example, from a list of preferred languages). Another player might choose the first track in 'trak' box order in the 'moov' among the candidate tracks. Another player might have another mechanism to choose the default. Possible fall-back approaches are neither enumerated nor restricted here. Note that selecting no subtitle track may be appropriate.
- If the default matching between audio language tagging and subtitle track language tagging cannot be used, a 'folw' track reference must be authored in the media file. (For example, Norwegian as spoken uses a different language tag than the two language tags for Norwegian as written.)

## Creating an Effect Description

An effect description tells QuickTime which effect to execute and contains the parameters that control how the effect behaves at runtime. You create an effect description by creating an atom container, inserting a QT atom that specifies the effect, and inserting a set of QT atoms that set its parameters.

There are support functions you can call to assist you in this process. `QTCreateStandardParameterDialog` returns a complete effect description that you can use, including user-selected settings; you only need to add `kEffectSourceName` atoms to the description for effects that require sources. At a lower level, `QTGetEffectsList` returns a list of the available effects and `ImageCodecGetParameterList` will return a description of the parameters for an effect, including the default value for each parameter in the form of a QT atom that can be inserted directly into an effect description.

### Structure of an Effect Description

An effect description is the sole media sample for an effect track. An effect description is implemented as a `QTAtomContainer` structure, the general QuickTime structure for holding a set of QuickTime atoms. All effect descriptions must contain the set of required atoms, which specify attributes such as which effect component to use. In addition, effect descriptions can contain a variable number of parameter atoms, which hold the values of the parameters for the effect.

Each atom contains either data or a set of child atoms. If a parameter atom contains data, the data is the value of the parameter, and this value remains constant while the effect executes. If a parameter atom contains a set of child atoms, they typically contain a tween entry so the value of the parameter will be interpolated for the duration of the effect.

You assemble an effect description by adding the appropriate set of atoms to a `QTAtomContainer` structure.

You can find out what the appropriate atoms are by making an `ImageCodecGetParameterList` call to the effect component. This fills an atom container with a set of parameter description atoms. These atoms contain descriptions of the effect parameters, such as each parameter’s atom type, data range, default value, and so on. The default value in each description atom is itself a `QTAtom` that can be inserted directly into your effect description.

You can modify the data in the parameter atoms directly, or let the user set them by calling `QTCreateStandardParameterDialog`, which returns a complete effect description (you need to add `kEffectSourceName` atoms for effects that require sources).

You then add the effect description to the media of the effect track.

### Required Atoms of an Effects Description

There are several required atoms that an effect description must contain. The first is the `kParameterWhatName` atom. The `kParameterWhatName` atom contains the name of the effect. This specifies which of the available effects to use.

The code snippet shown in [Listing 6-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbugazq) adds a `kParameterWhatName` atom to the atom container `effectDescription`. The constant `kCrossFadeTransitionType` contains the name of the cross-fade effect.

__Listing 6-10__  Adding a `kParameterWhatName` atom to the atom container `effectDescription`

```
effectCode = kCrossFadeTransitionType;
QTInsertChild(effectDescription, kParentAtomIsContainer,
                kParameterWhatName, kParameterWhatID, 0,
                sizeof(effectCode), &effectCode, nil);
```

In addition to the `kParameterWhatName` atom, the effect description for an effect that uses sources must contain one or more `kEffectSourceName` atoms. Each of these atoms contains the name of one of the effect’s sources. An input map is used to map these names to the actual tracks of the movie that are the sources. [Creating an Input Map](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcnzrgaya) describes how to create the input map.

### Parameter Atoms of an Effects Description

In addition to the required atoms, the effects description contains a variable number of parameter atoms. The number and types of parameter atoms vary from effect to effect. For example, the cross fade effect has only one parameter, while the general convolution filter effect has nine. Some effects have no parameters at all, and do not require any parameter atoms.

You can obtain the list of parameter atoms for a given effect by calling the effect component using `ImageCodecGetParameterList`. The parameter description atoms it returns include default settings for each parameter in the form of parameter atoms that you can insert into your effect description.

The `QTInsertChild` function is used to add these parameters to the effect description, as seen in the code example in [Listing 6-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbugazq).

Consider, for instance, the push effect. Its effect description contains a `kParameterWhatName` atom, two `kEffectSourceName` atoms, and two parameter atoms, one of which is a tween.

The `kParameterWhatName` atom specifies that this is a `'push'` effect.

The two `kEffectSourceName` atoms specify the two sources that this effect will use, in this case `'srcA'` and `'srcB'`. The names correspond to entries in the effect track’s input map.

The `'pcnt'` parameter atom defines which frames of the effect are shown. This parameter contains a tween entry, so that the value of this parameter is interpolated as the effect runs . The interpolation of the `'pcnt'` parameter causes consecutive frames of the effect to be rendered, creating the push effect.

The `'from'` parameter determines the direction of the push. This parameter is set from an enumeration list, with 2 being defined as the bottom of the screen.

In this example, the source `'srcB'` will push in from the bottom, covering the source `'srcA'`.

The `'pcnt'` parameter is normally tweened from 0 to 100, so that the effect renders completely, from 0 to 100 percent. In this example, the `'pcnt'` parameter is tweened from 25 to 75, so the effect will start 25 percent of the way through (with `'srcB'` already partly on screen) and finish 75 percent of the way through (with part of `'srcA'` still visible).

[Figure 6-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsgizq) shows the set of atoms that must be added to the entry description.

__Figure 6-5__  An example effect description for the Push effect

（原归档配图未能恢复：`qt_l_219.jpg`）

An important property of effect parameters is that most can be tweened (and some must be tweened). Tweening is QuickTime’s general purpose interpolation mechanism (see [Tween Media](Media%20Data%20Atom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygu2q) for more information). For many parameters, it is desirable to allow the value of the parameter to change as the effect executes. In the example shown in [Figure 6-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsgizq), the `'pcnt'` parameter must be a tween. This parameter controls which frame of the effect is rendered at any given time, so it must change for the effect to progress. The `'from'` parameter is not a tween in the example above, but it could be if we wanted the direction of the push to change during the course of the effect.

### Creating an Input Map

The input map is another QT atom container that you attach to the effects track. It describes the sources used in the effect and gives a name to each source. This name is used to refer to the source in the effects description.

An input map works in concert with track reference atoms in the source tracks. A track reference atom of type `kTrackModifierReference` is added to each source track, which causes that source track’s output to be redirected to the effects track. An input map is added to the effects track to identify the source tracks and give a name to each source, such as `'srcA'` and `'srcB'`. The effect can then refer to the sources by name, specifying that `'srcB'` should slide in over `'srcA'`, for example.

#### Structure of an Input Map

The input map contains a set of atoms that refer to the tracks used as sources for the effect. Each source track is represented by one track reference atom of type `kTrackModifierInput`.

Each modifier input atom contains two children, one of type `kEffectDataSourceType`, and one of type `kTrackModifierType`, which hold the name and type of the source.

The name of the source is a unique identifier that you create, which is used in the effect description to reference the track. Any four-character name is valid, as long as it is unique in the set of source names.

__Important:__
Apple recommends you adopt the standard naming convention `'srcX'`, where X is a letter of the alphabet. Thus, your first source would be named `'srcA'`, the second `'srcB',` and so forth. This convention is used here in this chapter.

The child atom of type `kTrackModifierType` indicates the type of the track being referenced. For a video track the type is `VideoMediaType`, for a sprite track it is `SpriteMediaType`, and so forth. Video tracks are the most common track type used as sources for effects. Only tracks that have a visible output, such as video and sprite tracks, can be used as sources for an effect. This means, for example, that sound tracks cannot be sources for an effect.

[Figure 6-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsgi3q) shows a completed input map that references two sources. The first source is a video track and is called `'srcA'`. The second source, also a video track, is called `'srcB'`.

You refer to a `kTrackModifierInput` atom by its index number, which is returned by the `AddTrackReference` function when you create the atom.

__Figure 6-6__  An example of an input map referencing two sources

（原归档配图未能恢复：`qt_l_220.gif`）

#### Building Input Maps

The first step in creating an input map is to create a new `QTAtomContainer` to hold the map. You use the standard QuickTime container creation function.

```
QTNewAtomContainer(&inputMap);
```

For each source you are creating, you need to call the `AddTrackReference` function. The track IDs of the effects track and the source track are passed as parameters to `AddTrackReference`, which creates an atom of type `kTrackModifierReference` and returns an index number. You use this index as the ID of the atom when you need to refer to it. You then insert the reference into the input map as an atom of type `kTrackModifierInput`.

The code in [Listing 6-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbugi2q) creates a reference to the track `firstSourceTrack`, and adds it to the input map.

__Listing 6-11__  Adding an input reference atom to an input map

```
AddTrackReference(theEffectsTrack, firstSourceTrack,
                 kTrackModifierReference, &referenceIndex);

QTInsertChild(inputMap, kParentAtomIsContainer,
            kTrackModifierInput, referenceIndex, 0, 0, nil, &inputAtom);
```

The `QTInsertChild` function returns the offset of the new modifier input atom in the `inputAtom` parameter.

You now need to add the name and type of the source track to the modifier input atom. Again, calling the `QTInsertChild` function does this, as shown in the following code snippet:

```
inputType = VideoMediaType;
QTInsertChild(inputMap, inputAtom,
                kTrackModifierType, 1, 0, sizeof(inputType), &inputType,
                nil);

aType = 'srcA';
QTInsertChild(inputMap, inputAtom, kEffectDataSourceType, 1, 0,
            sizeof(aType), &aType, nil);
```

This process is repeated for each source for the effect.

## Creating Movies with Modifier Tracks

QuickTime 2.1 added additional functionality for media handlers. By way of modifier tracks, a media handler can send its data to another media handler rather than presenting its media directly. See [Modifier Tracks](Media%20Data%20Atom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygu4q) for a complete discussion of this feature.

To create a movie with modifier tracks, first you create a movie with all the desired tracks, then you create the modifier track. To link the modifier track to the track that it modifies, you use the `AddTrackReference` function as shown in [Listing 6-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbugm3a).

__Listing 6-12__  Linking a modifier track to the track it modifies

```
long addedIndex;
AddTrackReference(aVideoTrack, aModifierTrack,
                    kTrackModifierReference, &addedIndex);
```

The reference doesn’t completely describe the modifier track’s relationship to the track it modifies. Instead, the reference simply tells the modifier track to send its data to the specified track. The receiving track doesn’t “know” what it should do with that data. A single track may also be receiving data from more than one modifier track.

To describe how each modifier input should be used, each track’s media also has an input map. The media’s input map describes how the data being sent to each input of a track should be interpreted by the receiving track. After creating the reference, it is necessary to update the receiving track’s media input map. When `AddTrackReference` is called, it returns the index of the reference added. That index is the index of the input that needs to be described in the media input map. If the modifier track created above contains regions to change the shape of the video track, the code shown in [Listing 6-13](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenbug43q) updates the input map appropriately.

__Listing 6-13__  Updating the input map

```
QTAtomContainer inputMap;
QTAtom inputAtom;
OSType inputType;

Media aVideoMedia = GetTrackMedia(aVideoTrack);
GetMediaInputMap (aVideoMedia, &inputMap);

QTInsertChild(inputMap, kParentAtomIsContainer, kTrackModifierInput,
        addedIndex, 0,0, nil, &inputAtom);

inputType = kTrackModifierTypeClip;
QTInsertChild (inputMap, inputAtom, kTrackModifierType, 1, 0,
        sizeof(inputType), &inputType, nil);

SetMediaInputMap(aVideoMedia, inputMap);
QTDisposeAtomContainer(inputMap);
```

The media input map allows you to store additional information for each input. In the preceding example, only the type of the input is specified. In other types of references, you may need to specify additional data.

When a modifier track is playing an empty track edit, or is disabled or deleted, all receiving tracks are notified that the track input is inactive. When an input becomes inactive, it is reset to its default value. For example, if a track is receiving data from a clip modifier track and that input becomes inactive, the shape of the track reverts to the shape it would have if there were no clip modifier track.

## Authoring Movies with External Movie Targets

QuickTime 4 enables you to author movies with external movie targets. To specify an action that targets an element of an external movie, you must identify the external movie by either its name or its ID. Two new target atom types have been introduced for this purpose; these atoms are used in addition to the existing target atoms, which you may use to specify that the element is a particular track or object within a track, such as a sprite.

__Note:__ A movie ID may be specified by an expression.

These additional target atoms provided in QuickTime 4:

```
[(ActionTargetAtoms)] =
    <kActionTarget>

        <kTargetMovieName>
            [Pstring MovieName]
        OR
        <kTargetMovieID>
            [long MovieID]
            OR
            [(kExpressionAtoms)]
```

To tag a movie with a name or ID, you add a user data item of type '`plug`' to the movie’s user data. The index of the user data does not matter. The data specifies the name or ID.

You add a user data item of type '`plug`' to the movie’s user data with its data set to

```
"Movieid=MovieName"
```

where `MovieName` is the name of the movie.

You add a user data item of type'`plug`' to the movie’s user data with its data set to

```
"Movieid=MovieID"
```

where the ID is a signed long integer.

The QuickTime plug-in additionally supports `EMBED` tag parameters, which allow you to override a movie’s name or ID within an HTML page.

### Target Atoms for Embedded Movies

QuickTime 4.1 introduced target atoms to accommodate the addition of embedded movies. These target atoms allow for paths to be specified in a hierarchical movie tree.

Target movies may be an external movie, the default movie, or any movie embedded within another movie. Targets are specified by using a movie path that may include parent and child movie relationships, and may additionally include track and track object target atoms as needed.

By using embedded `kActionTarget` atoms along with parent and child movie target atoms, you can build up paths for movie targets. Note that QuickTime looks for these embedded `kActionTarget` atoms only when evaluating a movie target, and any movie target type may contain a sibling `kActionTarget` atom.

Paths begin from the current movie, which is the movie containing the object that is handling an event. You may go up the tree using a `kTargetParentMovie` atom, or down the tree using one of five new child movie atoms. You may use a `kTargetRootMovie` atom as a shortcut to get to the top of the tree containing an embedded movie and may use the `movieByName` and `movieByID` atoms to specify a root external movie.

The target atoms are:

- `kTargetRootMovie` (leaf
  atom, no data). This is the root movie containing the action handler.
- `kTargetParentMovie`
  (leaf atom, no data). This is the parent movie.

Note that there are five ways to specify an embedded child movie. Three of them specify movie track properties. Two specify properties of the currently loaded movie in a movie track.

- `kTargetChildMovieTrackName.` A child movie track specified by track name.
- `kTargetChildMovieTrackID`. A child movie track specified by track ID.
- `kTargetChildMovieTrackIndex`. A child movie track specified by track index.
- `kTargetChildMovieMovieName`. A child movie specified by the currently loaded movie’s movie name. The child movie must contain `movieName` user data with the specified name.
- `kTargetChildMovieMovieID`. A child movie specified by the currently loaded movie’s movie ID. The child movie must contain `movieID` user data with the specified ID.

## Creating Video Tracks at 30 Frames per Second

The duration of a video frame is stored in the time-to-sample atom contained within a sample table atom. This duration cannot be interpreted without the media’s time scale, which defines the units-per-second for the duration. In this example, each frame has the same duration, so the time-to-sample atom has one entry, which applies to all video frames in the media.

As long as the ratio between frame duration and media time scale remains 1:30, any combination of values can be used for the duration and time scale. The larger the time scale the shorter the maximum duration. Since a movie defaults to a time scale of 600, this is a good number to use. It is also the least common multiple for 24, 25, and 30, making it handy for much of the math you are likely to encounter when making a movie.

The movie time scale is independent of the media time scale. Since you want to avoid movie edits that don’t land on frame boundaries, it is a good idea to keep the movie time scale and the media time scale the same, or the movie time scale should be an even multiple of the media time scale. The movie time scale is stored in the movie header atom.

With a time scale of 600 in the media header atom, the time-to-sample atom would contain the data values listed in [Table 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzv).

__Table 6-1__  Example data values for time scale of 600

| Field | Value |
| Atom size | 24 |
| Atom type | `'stts'` |
| Version/Flags | 0 |
| Number of entries | 1 |
| Sample count | n |
| Sample duration | 20 |

## Creating Video Tracks at 29.97 Frames per Second

NTSC color video is not 30 frames per second (fps), but actually 29.97 fps. The previous example showed how the media time scale and the duration of the frames specify the video’s frame rate. By setting the media’s time scale to 2997 units per second and setting the frame durations to 100 units each, the effective rate is 29.97 fps exactly.

In this situation, it is also a good idea to set the movie time scale to 2997 in order to avoid movie edits that don’t land on frame boundaries. The movie’s time scale is stored in the movie header atom.

With a time scale of 2997 in the media header atom, the time-to-sample atom would contain the data values listed in [Table 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzrga).

__Table 6-2__  Example data values for time scale of 2997

| Field | Value |
| Atom size | 24 |
| Atom type | `'stts'` |
| Version/Flags | 0 |
| Number of entries | 1 |
| Sample count | n |
| Sample duration | 100 |

## Creating Sound Tracks at 44.1 kHz

The duration of an audio sample is stored in the time-to-sample atom contained in a sample table atom. This duration cannot be interpreted without the media’s time scale, which defines the units per second for the duration. With audio, the duration of each audio sample is typically 1, so the time-to-sample atom has one entry, which applies to all audio samples.

With a time scale of 44100 in the media header atom, the time-to-sample atom would contain the data values listed in [Table 6-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzrge).

__Table 6-3__  Example data values for time scale of 44100

| Field | Value |
| Atom size | 24 |
| Atom type | `'stts'` |
| Version/Flags | 0 |
| Number of entries | 1 |
| Sample count | n |
| Sample duration | 1 |

This atom does not indicate whether the audio is stereo or mono or whether it contains 8-bit or 16-bit samples. That information is stored in the sound sample description atom, which is contained in the sample table atom.

## Creating a Timecode Track for 29.97 FPS Video

A timecode track specifies timecode information for other tracks. The timecode keeps track of the time codes of the original source of the video and audio. After a movie has been edited, the timecode can be extracted to determine the source tape and the time codes of the frames.

It is important that the timecode track have the same time scale as the video track. Otherwise, the timecode will not tick at the exact same time as the video track.

For each contiguous source tape segment, there is a single timecode sample that specifies the timecode value corresponding to the start of the segment. From this sample, the timecode value can be determined for any point in the segment.

The sample description for a timecode track specifies the timecode system being used (for example, a 30-fps drop frame) and the source information. Each sample is a timecode value.

Since the timecode media handler is a derived from the base media handler, the media information atom starts with a generic media header atom. The timecode atoms would contain the following data values:

|  |  |  |  |
| --- | --- | --- | --- |
| Atom size | 80 |  |  |
| Atom type | `'gmhd'` |  |  |
|  | Atom size | 24 |  |
|  | Atom type | `'gmin'` |  |
|  | Version/Flags | 0 |  |
|  | Graphics mode | 0x0040 |  |
|  | Opcolor (red) | 0x8000 |  |
|  | Opcolor (green) | 0x8000 |  |
|  | Opcolor (blue) | 0x8000 |  |
|  | Balance | 0 |  |
|  | Reserved | 0 |  |
|  | Atom size | 48 |  |
|  | Atom type | `'tmcd'` |  |
|  |  | Atom size | 40 |
|  |  | Atom type | `'tcmi'` |
|  |  | Version/Flags | 0 |
|  |  | Text font | 0 (system font) |
|  |  | Text face | 0 (plain) |
|  |  | Text size | 12 |
|  |  | Padding | 0 |
|  |  | Text color (red) | 0 |
|  |  | Text color (green) | 0 |
|  |  | Text color (blue) | 0 |
|  |  | Background color (red) | 0 |
|  |  | Background color (green) | 0 |
|  |  | Background color (blue) | 0 |
|  |  | Font name | `'\pChicago'` (Pascal string) |

The sample table atom contains all the standard sample atoms and has the following data values:

|  |  |  |  |
| --- | --- | --- | --- |
| Atom size | 174 |  |  |
| Atom type | `'stbl'` (sample table) |  |  |
|  | Atom size | 74 |  |
|  | Atom type | `'stsd'` (sample description) |  |
|  | Version/Flags | 0 |  |
|  | Number of entries | 1 |  |
|  | Sample description size [1] | 58 |  |
|  | Data format [1] | `'tmcd'` |  |
|  | Reserved [1] | 0 |  |
|  | Data reference index [1] | 1 |  |
|  | Flags[1] | 0 |  |
|  | Flags (timecode) [1] | 7 (drop frame + 24 hour + negative times OK) |  |
|  | Time scale[1] | 2997 |  |
|  | Frame duration[1] | 100 |  |
|  | Number of frames [1] | 20 |  |
|  |  | Atom size | 24 |
|  |  | Atom type | `'name'` |
|  |  | String length | 12 |
|  |  | Language code | 0 (English) |
|  |  | Name | “my tape name” |
|  | Atom size | 24 |  |
|  | Atom type | `'stts'` (time to sample) |  |
|  | Version/Flags | 0 |  |
|  | Number of entries | 1 |  |
|  | Sample count[1] | 1 |  |
|  | Sample duration[1] | 1 |  |
|  | Atom size | 28 |  |
|  | Atom type | `'stsc'` (sample to chunk) |  |
|  | Version/Flags | 0 |  |
|  | Number of entries | 1 |  |
|  | First chunk[1] | 1 |  |
|  | Samples per chunk[1] | 1 |  |
|  | Sample description ID[1] | 1 |  |
|  | Atom size | 20 |  |
|  | Atom type | `'stsz'` (sample size) |  |
|  | Version/Flags | 0 |  |
|  | Sample size | 4 |  |
|  | Number of entries | 1 |  |
|  | Atom size | 20 |  |
|  | Atom type | `'stco'` (chunk offset) |  |
|  | Version/Flags | 0 |  |
|  | Number of entries | 1 |  |
|  | Offset [1] | (offset into file of chunk 1) |  |

In the example, let’s assume that the segment’s beginning timecode is 1:15:32.4 (1 hour, 15 minutes, 32 seconds, and 4 frames). The time would be expressed in the data file as 0x010F2004 (0x01 = 1 hour; 0x0F = 15 minutes; 0x20 = 32 seconds; 0x04 = 4 frames).

The video and sound tracks must contain a track reference atom to indicate that they reference this timecode track. The track reference is the same for both and is contained in the track atom (at the same level as the track header and media atoms).

This track reference would contain the data values listed in [Table 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzrgi).

__Table 6-4__  Example track reference data values

| Field | Value |
| Atom size | 12 |
| Atom type | `'tref'` |
| Reference type | `'tmcd'` |
| Track ID of referenced track (timecode track) | 3 |

In this example, the video and sound tracks are tracks 1 and 2. The timecode track is track 3.

## Playing with Edit Lists

A segment of a movie can be repeated without duplicating media data by using edit lists. Suppose you have a single-track movie whose media time scale is 100 and track duration is 1000 (10 seconds). For this example the movie’s time scale is 600. If there are no edits in the movie, the edit atom would contain the data values listed in [Table 6-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzrgm).

__Table 6-5__  Example edit atom data values

| Atom size | 36 |  |
| Atom type | `'edts'` |  |
|  | Atom size | 28 |
|  | Atom type | `'elst'` |
|  | Version/Flags | 0 |
|  | Number of entries | 2 |
|  | Track duration | 6000 (10 seconds) |
|  | Media time | 0 |
|  | Media rate | 1.0 |

Because this is a single-track move, the track’s duration in the track header atom is 6000 and the movie’s duration in the movie header atom is 6000.

If you change the track to play the media from time 0 to time 2 seconds, and then play the media from time 0 to time 10 seconds, the edit atom would now contain these data values:

|  |  |  |
| --- | --- | --- |
| Atom size | 48 |  |
| Atom type | `'edts'` |  |
|  | Atom size | 40 |
|  | Atom type | `'elst'` |
|  | Version/Flags | 0 |
|  | Number of entries | 2 |
|  | Track duration[1] | 1200 (2 seconds) |
|  | Media time[1] | 0 |
|  | Media rate[1] | 1.0 |
|  | Track duration[2] | 6000 (10 seconds) |
|  | Media time[2] | 0 |
|  | Media rate[2] | 1.0 |

Because the track is now 2 seconds longer, the track’s duration in the track header atom must now be 7200, and the movie’s duration in the movie header atom must also be 7200.

Currently, the media plays from time 0 to time 2, then plays from time 0 to time 10. If you take that repeated segment at the beginning (time 0 to time 2) and play it at double speed to maintain the original duration, the edit atom would now contain the following values:

|  |  |  |
| --- | --- | --- |
| Atom size | 60 |  |
| Atom type | `'edts'` |  |
|  | Atom size | 52 |
|  | Atom type | `'elst'` |
|  | Version/Flags | 0 |
|  | Number of entries | 3 |
|  | Track duration[1] | 600 (1 second) |
|  | Media time[1] | 0 |
|  | Media rate[1] | 2.0 |
|  | Track duration[2] | 600 (1 second) |
|  | Media time[2] | 0 |
|  | Media rate[2] | 2.0 |
|  | Track duration[3] | 4800 (8 seconds) |
|  | Media time[3] | 200 |
|  | Media rate[3] | 1.0 |

Because the track is now back to its original duration of 10 seconds, its duration in the track header atom is 6000, and the movie’s duration in the movie header atom is 6000.

## Interleaving Movie Data

In order to get optimal movie playback, you must create the movie with interleaved data. Because the data for the movie is placed on disk in time order, the data for a particular time in the movie is close together in the file. This means that you must intersperse the data from different tracks. To illustrate this, consider a movie with a single video and a single sound track.

[Figure 6-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsgmyq) shows how the movie data was collected, and how the data would need to be played back for proper synchronization. In this example, the video data is recorded at 10 frames per second and the audio data is grouped into half-second chunks.

__Figure 6-7__  Non-interleaved movie data

（原归档配图获取待重试：`qt_l_211.gif`）

After the data has been interleaved on the disk, the movie data atom would contain movie data in the order shown in [Figure 6-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsgm2q).

__Figure 6-8__  Interleaved movie data

（原归档配图未能恢复：`qt_l_212.gif`）

In this example, the file begins with the movie atom (`'moov'`), followed by the movie data atom (`'mdat'`). In order to overcome any latencies in sound playback, at least one second of sound data is placed at the beginning of the interleaved data. This means that the sound and video data are offset from each other in the file by one second.

## Referencing Two Data Files With a Single Track

The data reference index to be used for a given media sample is stored within that sample’s sample description. Therefore, a track must contain multiple sample descriptions in order for that track to reference multiple data files. A different sample description must be used whenever the data file changes or whenever the format of the data changes. The sample-to-chunk atom determines which sample description to use for a sample.

The sample description atom would contain the following data values:

|  |  |  |
| --- | --- | --- |
| Atom size | … |  |
| Atom type | `'stsd'` |  |
| Version/Flags | 0 |  |
| Number of entries | 2 |  |
|  | Sample description size[1] | … |
|  | Data format | `'tmcd'` |
|  | Reserved | 0 |
|  | Data reference index | 1 |
|  | (sample data) | … |
|  | Sample description size[1] | … |
|  | Data format | `'tmcd'` |
|  | Reserved | 0 |
|  | Data reference index | 2 |
|  | (sample data) | … |

If there is only 1 sample per chunk and the first 10 samples are extracted from sample description 2 and the next 30 samples are extracted from sample description 1, the sample-to-chunk atom would contain the following data values:

|  |  |
| --- | --- |
| Atom size | 40 |
| Atom type | `'stsc'` |
| Version/Flags | 0 |
| Number of entries | 2 |
| First chunk[1] | 1 |
| Samples per chunk[1] | 1 |
| Sample description ID[1] | 2 |
| First chunk[2] | 11 |
| Samples per chunk[2] | 1 |
| Sample description ID[2] | 1 |

The data reference atom would contain the following data values:

|  |  |  |
| --- | --- | --- |
| Atom size | … |  |
| Atom type | `'dinf'` |  |
|  | Atom size | … |
|  | Atom type | `'dref'` |
|  | Version/Flags | 0 |
|  | Number of entries | 2 |
|  | Size[1] | … |
|  | Type[1] | `'alis'` |
|  | Version[1] | 0 |
|  | Flags[1] | 0 (not self referenced) |
|  | Data reference[1] | [alias pointing to file #1] |
|  | Size[2] | … |
|  | Type[2] | `'rsrc'` |
|  | Version[2] | 0 |
|  | Flags[2] | 0 (not self referenced) |
|  | Data reference[2] | [alias pointing to file #2] |

## Getting the Name of a QuickTime VR Node

You can use standard QuickTime atom container functions to retrieve the information in a QuickTime VR node header atom. For example, the `MyGetNodeName` function defined in [Listing 6-14](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenrxg42a) returns the name of a node, given its node ID.

__Listing 6-14__  Getting a node’s name

```
OSErr MyGetNodeName (QTVRInstance theInstance, UInt32 theNodeID,
                                                                 StringPtr  theStringPtr)
{
    OSErr                   theErr = noErr;
    QTAtomContainer         theNodeInfo;
    QTVRNodeHeaderAtomPtr   theNodeHeader;
    QTAtom                  theNodeHeaderAtom = 0;

    //Get the node information atom container.
    theErr = QTVRGetNodeInfo(theInstance, theNodeID, &theNodeInfo);

    //Get the node header atom.
    if (!theErr)
        theNodeHeaderAtom = QTFindChildByID(theNodeInfo, kParentAtomIsContainer,
                                                    kQTVRNodeHeaderAtomType,  1,  nil);
    if (theNodeHeaderAtom != 0) {
        QTLockContainer(theNodeInfo);

        //Get a pointer to the node header atom data.
        theErr = QTGetAtomDataPtr(theNodeInfo, theNodeHeaderAtom,  nil,
                                                            (Ptr  *)&theNodeHeader);
        //See if there is a name atom.
        if (!theErr && theNodeHeader->nameAtomID != 0)  {
            QTAtom theNameAtom;
            theNameAtom = QTFindChildByID(theNodeInfo, kParentAtomIsContainer,
                                kQTVRStringAtomType, theNodeHeader->nameAtomID,  nil);
            if (theNameAtom != 0) {
                VRStringAtomPtr theStringAtomPtr;

                //Get a pointer to the name atom data; copy it into  the string.
                theErr = QTGetAtomDataPtr(theNodeInfo, theNameAtom,  nil,
                                                            (Ptr  *)&theStringAtomPtr);
                if (!theErr) {
                    short theLen = theStringAtomPtr->stringLength;
                    if (theLen > 255)
                        theLen = 255;
                    BlockMove(theStringAtomPtr->string, &theStringPtr[1],  theLen);
                    theStringPtr[0] = theLen;
                }
            }
        }
        QTUnlockContainer(theNodeInfo);
    }

    QTDisposeAtomContainer(theNodeInfo);
    return(theErr);
}
```

The `MyGetNodeName` function defined in [Listing 6-14](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenrxg42a) retrieves the node information atom container (by calling `QTVRGetNodeInfo`) and then looks inside that container for the node header atom with atom ID 1. If it finds one, it locks the container and then gets a pointer to the node header atom data. The desired information, the node name, is contained in the string atom whose atom ID is specified by the `nameAtomID` field of the node header structure. Accordingly, the `MyGetNodeName` function then calls `QTFindChildByID` once again to find that string atom. If the string atom is found, `MyGetNodeName` calls `QTGetAtomDataPtr` to get a pointer to the string atom data. Finally, `MyGetNodeName` copies the string data into the appropriate location and cleans up after itself before returning.

## Adding Custom Atoms in a QuickTime VR Movie

If you author a QuickTime VR movie, you may choose to add custom atoms to either the VR world or node information atom containers. Those atoms can be extracted within an application to provide additional information that the application may use.

Information that pertains to the entire scene might be stored in a custom atom within the VR world atom container. Node-specific information could be stored in the individual node information atom containers or as sibling atoms to the node location atoms within the VR world.

Custom hot spot atoms should be stored as siblings to the hot spot information atoms in the node information atom container. Generally, its atom type is the same as the custom hot spot type. You can set up an intercept procedure in your application in order to process clicks on the custom hot spots.

If you use custom atoms, you should install your hot spot intercept procedure when you open the movie. [Listing 6-15](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenrxha3q) is an example of such an intercept procedure.

__Listing 6-15__  Typical hot spot intercept procedure

```
QTVRInterceptProc MyProc = NewQTVRInterceptProc (MyHotSpot);
QTVRInstallInterceptProc (qtvr, kQTVRTriggerHotSpotSelector, myProc,  0, 0);

pascal void MyHotSpot (QTVRInstance qtvr, QTVRInterceptPtr qtvrMsg,
                        SInt32 refCon, Boolean *cancel)
{
    UInt32 hotSpotID = (UInt32) qtvrMsg->parameter[0];
    QTAtomContainer nodeInfo =
            (QTAtomContainer) qtvrMsg->parameter[1];
    QTAtom hotSpotAtom = (QTAtom) qtvrMsg->parameter[2];
    OSType hotSpotType;
    CustomData myCustomData;
    QTAtom myAtom;

    QTVRGetHotSpotType (qtvr, hotSpotID, &hotSpotType);
    if (hotSpotType != kMyAtomType) return;

    // It's our type of hot spot - don't let anyone else handle  it
    *cancel = true;

    // Find our custom atom
    myAtom = QTFindChildByID (nodeInfo, hotSpotAtom, kMyAtomType,  1, nil);
    if (myAtom != 0) {
        OSErr err;
        // Copy the custom data into our structure
        err = QTCopyAtomDataToPtr (nodeInfo, myAtom, false,
                        sizeof(CustomData), &myCustomData, nil);
        if (err == noErr)
            // Do something with it
            DoMyHotSpotStuff (hotSpotID, &myCustomData);
    }
}
```

Your intercept procedure is called for clicks on any hot spot. You should check to see if it is your type of hot spot and, if so, extract the custom hot spot atom and do whatever is appropriate for your hot spot type (`DoMyHotSpotStuff`).

When you no longer need the intercept procedure you should call `QTVRInstallInterceptProc` again with the same selector and a `nil` procedure pointer and then call `DisposeRoutineDescriptor` on `myProc`.

Apple reserves all hot spot and atom types with lowercase letters. Your custom hot spot type should contain all uppercase letters.

## Adding Atom Containers in a QuickTime VR Movie

Assuming you have already created the QuickTime VR world and node information atom containers, you would use the code (minus error checking) [Listing 6-16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenrxhe4a) to add them to the QTVR track.

__Listing 6-16__  Adding atom containers to a track

```
long descSize;
QTVRSampleDescriptionHandle qtvrSampleDesc;

// Create a  QTVR sample description handle

descSize = sizeof(QTVRSampleDescription) + GetHandleSize((Handle)  vrWorld) -
                                        sizeof(UInt32);
qtvrSampleDesc = (QTVRSampleDescriptionHandle) NewHandleClear (descSize);
(*qtvrSampleDesc)->size = descSize;
(*qtvrSampleDesc)->type = kQTVRQTVRType;

// Copy the VR world atom container data into the QTVR sample description
BlockMove (*((Handle) vrWorld), &((*qtvrSampleDesc)->data),
                            GetHandleSize((Handle) vrWorld));
// Now add it to the QTVR track's media
err = BeginMediaEdits (qtvrMedia);
err = AddMediaSample (qtvrMedia, (Handle) nodeInfo, 0,
    GetHandleSize((Handle) nodeInfo), duration,
    (SampleDescriptionHandle) qtvrSampleDesc, 1, 0, &sampleTime);
err = EndMediaEdits (qtvrMedia);
InsertMediaIntoTrack (qtvrTrack, trackTime, sampleTime, duration,  1L<<16);
```

The `duration` value is computed based on the duration of the corresponding image track samples for the node. The value of `trackTime` is the time for the beginning of the current node (zero for a single node movie). The values of `duration` and `sampleTime` are in the time base of the media; the value of `trackTime` is in the movie’s time base.

## Optimizing QuickTime VR Movies for Web Playback

Originally, both QuickTime movies and QuickTime VR movies had to be completely downloaded to the user’s local hard disk before they could be viewed. Starting with QuickTime 2.5, if the movie data is properly laid out in the file, standard linear QuickTime movies can be viewed almost immediately. The frames that have been downloaded so far are shown while subsequent frames continue to be downloaded.

The important change that took place to allow this to happen was for QuickTime to place global movie information at the beginning of the file. Originally, this information was at the end of the file. After that, the frame data simply needs to be in order in the file. Similarly, QuickTime VR files also need to be laid out in a certain manner in order to get some sort of quick feedback when viewing on the web. Roughly speaking this involves writing out all of the media samples in the file in a particular order. Apple now provides a movie export component that does this for you: the QTVR Flattener.

### The QTVR Flattener

The QTVR Flattener is a movie export component that converts an existing QuickTime VR single node movie into a new movie that is optimized for the Web. Not only does the flattener reorder the media samples, but for panoramas it also creates a small preview of the panorama. When viewed on the Web, this preview appears after 5% to 10% of the movie data has been downloaded, allowing users to see a lower-resolution version of the panorama.

Using the QTVR flattener from your application is quite easy. After you have created the QuickTime VR movie, you simply open the QTVR Flattener component and call the `MovieExportToFile` routine as shown in [Listing 6-17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenrygu3a).

__Listing 6-17__  Using the flattener

```
ComponentDescription desc;
Component flattener;
ComponentInstance qtvrExport = nil;
desc.componentType = MovieExportType;
desc.componentSubType = MovieFileType;
desc.componentManufacturer = QTVRFlattenerType;
flattener = FindNextComponent(nil, &desc);
if (flattener) qtvrExport = OpenComponent (flattener);
if (qtvrExport)
    MovieExportToFile (qtvrExport, &myFileSpec, myQTVRMovie,  nil, 0, 0);
```

The code fragment shown in [Listing 6-17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenrygu3a) creates a flattened movie file specified by the `myFileSpec` parameter. If your QuickTime VR movie is a panorama, the flattened movie file includes a quarter size, blurred JPEG, compressed preview of the panorama image.

__Note:__ The constants `MovieExportType` and `MovieFileType` used in [Listing 6-17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenrygu3a) are defined in header files `QuickTimeComponents.h` and `Movies.h` respectively and are defined as `'spit'` and `'MooV'`.

You can present users with the QTVR Flattener’s own dialog box to allow them to choose options such as how to compress the preview image or to select a separate preview image file. Use the following code to show the dialog box:

```
        err = MovieExportDoUserDialog (qtvrExport, myQTVRMovie,  nil, 0, 0,  &cancel);
```

If the user cancels the dialog box, then the Boolean cancel is set to `true`.

If you do not want to present the user with the flattener’s dialog box, you can communicate directly with the component by using the `MovieExportSetSettingsFromAtomContainer` routine as described in the following paragraphs.

If you want to specify a preview image other than the default, you need to create a special atom container and then call `MovieExportSetSettingsFromAtomContainer` before calling `MovieExportToFile`. You can specify how to compress the image, what resolution to use, and you can even specify your own preview image file to be used. The atom container you pass in can have various atoms that specify certain export options. These atoms must all be children of a flattener settings parent atom.

The preview resolution atom is a 16-bit value that allows you to specify the resolution of the preview image. This value, which defaults to `kQTVRQuarterRes`, indicates how much to reduce the preview image.

The blur preview atom is a Boolean value that indicates whether to blur the image before compressing. Blurring usually results in a much more highly compressed image. The default value is `true`.

The create preview atom is a Boolean value that indicates whether a preview image should be created. The default value is `true`.

The import preview atom is a Boolean value that is used to indicate that the preview image should be imported from an external file rather than generated from the image in the panorama file itself. This allows you to have any image you want as the preview for the panorama. You can specify which file to use by also including the import specification atom, which is an `FSSpec` data structure that identifies the image file. If you do not include this atom, then the flattener presents the user with a dialog box asking the user to select a file. The default for import preview is `false.` If an import file is used, the image is used at its natural size and the resolution setting is ignored.

### Sample Atom Container for the QTVR Flattener

The sample code in [Listing 6-18](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtenryg44q) creates an atom container and adds atoms to indicate an import preview file for the flattener to use.

__Listing 6-18__  Specifying a preview file for the flattener to use

```
Boolean yes = true;
QTAtomContainer exportData;
QTAtom parent;
err = QTNewAtomContainer(&exportData);
// create a parent for the other settings atoms
err = QTInsertChild (exportData, kParentAtomIsContainer,
            QTVRFlattenerParentAtomType, 1, 0, 0, nil, &parent);
// Add child atom to indicate we want to import the preview from  a file
err = QTInsertChild (exportData, parent, QTVRImportPreviewAtomType,  1, 0,
            sizeof (yes), &yes, nil);
// Add child atom to tell which file to import
err = QTInsertChild (exportData, parent, QTVRImportSpecAtomType,  1, 0,
            sizeof (previewSpec), &previewSpec, nil);
// Tell the export component
MovieExportSetSettingsFromAtomContainer (qtvrExport, exportData);
```

Overriding the compression settings is a bit more complicated. You need to open a standard image compression dialog component and make calls to obtain an atom container that you can then pass to the QTVR Flattener component.

__Listing 6-19__  Overriding the compression settings

```
ComponentInstance sc;
QTAtomContainer compressorData;
SCSpatialSettings ss;
sc = OpenDefaultComponent(StandardCompressionType,StandardCompressionSubType);
ss.codecType = kCinepakCodecType;
ss.codec = nil;
ss.depth = 0;
ss.spatialQuality = codecHighQuality
err = SCSetInfo(sc, scSpatialSettingsType, &ss);
err = SCGetSettingsAsAtomContainer(sc, &compressorData);
MovieExportSetSettingsFromAtomContainer (qtvrExport, compressorData);
```

[Next](QuickTime%20Image%20File%20Format.md)[Previous](Basic%20Data%20Types.md)
