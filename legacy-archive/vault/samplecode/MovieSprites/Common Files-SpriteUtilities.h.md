---
title: MovieSprites
apple_id: DTS10001040
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieSprites/Listings/Common_Files_SpriteUtilities_h.html
archived_at: '2026-07-18T03:16:11.725283Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MovieSprites](MovieSprites.md)


[Next](Common%20Files-WinPrefix.h.md)[Previous](Common%20Files-SpriteUtilities.c.md)

# Common Files/SpriteUtilities.h

```c
#ifndef _SPRITEUTILITIES_
#define _SPRITEUTILITIES_
#ifndef __MOVIES__
    #include <Movies.h>
#endif
#endif

// _____________________ Sprite Utilities _____________________ //

// set sprite properties for non-nil parameters, overriding or adding atoms as neccessary
OSErr SetSpriteData( QTAtomContainer sprite, Point *location, short *visible, short *layer, short *imageIndex, 
                        ModifierTrackGraphicsModeRecord *graphicsMode, StringPtr spriteName, 
                        QTAtomContainer actionAtoms );
// add a sprite to a sample
OSErr AddSpriteToSample( QTAtomContainer theSample, QTAtomContainer theSprite, QTAtomID spriteID );

// add a sprite key frame sample to sprite track's media
OSErr AddSpriteSampleToMedia( Media theMedia, QTAtomContainer sample, TimeValue duration, Boolean isKeyFrame,
                        TimeValue *sampleTime );

// add a sprite key frame sample--and compress it in the process--to sprite track's media
OSErr AddCompressedSpriteSampleToMedia( Media theMedia, QTAtomContainer sample, TimeValue duration, Boolean isKeyFrame,
                        OSType dataCompressorType,
                        TimeValue *sampleTime );

// compress a PICT with animation compressor and add image data to a sprite key sample's images container atom
OSErr AddPICTImageToKeyFrameSample( QTAtomContainer keySample, short pictID, RGBColor *keyColor, QTAtomID id, 
                        FixedPoint *registrationPoint, StringPtr imageName );

// add compressed image data to a sprite key sample's images container atom
OSErr AddCompressedImageToKeyFrameSample( QTAtomContainer keySample, ImageDescriptionHandle idh, long dataSize, Ptr compressedDataPtr,
                        QTAtomID imageID, FixedPoint *registrationPoint, StringPtr imageName );

// assign image group ID's to the images in a key frame sample
OSErr AssignImageGroupIDsToKeyFrame( QTAtomContainer keySample );
```

[Next](Common%20Files-WinPrefix.h.md)[Previous](Common%20Files-SpriteUtilities.c.md)

