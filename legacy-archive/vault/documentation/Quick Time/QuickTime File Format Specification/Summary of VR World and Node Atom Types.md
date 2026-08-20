---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFAppenE/QTFFAppenE.html
archived_at: '2026-07-27T06:57:06.769808Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](Profile%20Atom%20Guidelines.md)[Previous](Metadata%20Handling.md)

# Summary of VR World and Node Atom Types

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR media and should not be used for new development.

This appendix includes information that pertains to Chapter 3, [VR World Atom Container](Media%20Data%20Atom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzzhaya) and [Node Information Atom Container](Media%20Data%20Atom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtkobqgq4q).

## C Summary

### Constants

#### VR World Atom Types

```
enum {
    kQTVRWorldHeaderAtomType    = FOUR_CHAR_CODE('vrsc'),
    kQTVRImagingParentAtomType  = FOUR_CHAR_CODE('imgp'),
    kQTVRPanoImagingAtomType    = FOUR_CHAR_CODE('impn'),
    kQTVRObjectImagingAtomType  = FOUR_CHAR_CODE('imob'),
    kQTVRNodeParentAtomType     = FOUR_CHAR_CODE('vrnp'),
    kQTVRNodeIDAtomType         = FOUR_CHAR_CODE('vrni'),
    kQTVRNodeLocationAtomType   = FOUR_CHAR_CODE('nloc')
};
```

#### Node Information Atom Types

```
enum {
    kQTVRNodeHeaderAtomType     = FOUR_CHAR_CODE('ndhd'),
    kQTVRHotSpotParentAtomType  = FOUR_CHAR_CODE('hspa'),
    kQTVRHotSpotAtomType        = FOUR_CHAR_CODE('hots'),
    kQTVRHotSpotInfoAtomType    = FOUR_CHAR_CODE('hsin'),
    kQTVRLinkInfoAtomType       = FOUR_CHAR_CODE('link')
};
```

#### Miscellaneous Atom Types

```
enum {
    kQTVRStringAtomType             = FOUR_CHAR_CODE('vrsg'),
    kQTVRPanoSampleDataAtomType     = FOUR_CHAR_CODE('pdat'),
    kQTVRObjectInfoAtomType         = FOUR_CHAR_CODE('obji'),
    kQTVRAltImageTrackRefAtomType   = FOUR_CHAR_CODE('imtr'),
    kQTVRAltHotSpotTrackRefAtomType = FOUR_CHAR_CODE('hstr'),
    kQTVRAngleRangeAtomType         = FOUR_CHAR_CODE('arng'),
    kQTVRTrackRefArrayAtomType      = FOUR_CHAR_CODE('tref'),
    kQTVRPanConstraintAtomType      = FOUR_CHAR_CODE('pcon'),
    kQTVRTiltConstraintAtomType     = FOUR_CHAR_CODE('tcon'),
    kQTVRFOVConstraintAtomType      = FOUR_CHAR_CODE('fcon'),
    kQTVRCubicViewAtomType          = FOUR_CHAR_CODE('cuvw'),
    kQTVRCubicFaceDataAtomType      = FOUR_CHAR_CODE('cufa')
};
```

#### Track Reference Types

```
enum {
    kQTVRImageTrackRefType      = FOUR_CHAR_CODE('imgt'),
    kQTVRHotSpotTrackRefType    = FOUR_CHAR_CODE('hott')
};
```

#### Imaging Property Valid Flags

```
enum {
    kQTVRValidCorrection                        = 1 << 0,
    kQTVRValidQuality                           = 1 << 1,
    kQTVRValidDirectDraw                        = 1 << 2,
    kQTVRValidFirstExtraProperty                = 1 << 3
};
```

#### Link Hot Spot Valid Bits

```
enum {
    kQTVRValidPan                               = 1 << 0,
    kQTVRValidTilt                              = 1 << 1,
    kQTVRValidFOV                               = 1 << 2,
    kQTVRValidViewCenter                        = 1 << 3
};
```

#### Animation Settings

```swift
enum QTVRAnimationSettings {
    kQTVRObjectAnimateViewFramesOn              = (1 << 0),
    kQTVRObjectPalindromeViewFramesOn           = (1 << 1),
    kQTVRObjectStartFirstViewFrameOn            = (1 << 2),
    kQTVRObjectAnimateViewsOn                   = (1 << 3),
    kQTVRObjectPalindromeViewsOn                = (1 << 4),
    kQTVRObjectSyncViewToFrameRate              = (1 << 5),
    kQTVRObjectDontLoopViewFramesOn             = (1 << 6),
    kQTVRObjectPlayEveryViewFrameOn             = (1 << 7)
};
```

#### Control Settings

```swift
enum QTVRControlSettings {
    kQTVRObjectWrapPanOn                        = (1 << 0),
    kQTVRObjectWrapTiltOn                       = (1 << 1),
    kQTVRObjectCanZoomOn                        = (1 << 2),
    kQTVRObjectReverseHControlOn                = (1 << 3),
    kQTVRObjectReverseVControlOn                = (1 << 4),
    kQTVRObjectSwapHVControlOn                  = (1 << 5),
    kQTVRObjectTranslationOn                    = (1 << 6)
};
```

#### Controller Subtype and ID

```
enum {
    kQTControllerType                           = FOUR_CHAR_CODE('ctyp').
    kQTControllerID                             = 1
};
```

#### Object Controller Types

```swift
enum ObjectUITypes {
    kGrabberScrollerUI                          = 1,
    kOldJoyStickUI                              = 2,
    kJoystickUI                                 = 3,
    kGrabberUI                                  = 4,
    kAbsoluteUI                                 = 5
};
```

#### Node Location Flag

```
enum {
    kQTVRSameFile                               = 0
};
```

#### Panorama Sample Flag

```
enum {
    kQTVRPanoFlagHorizontal                     = 1 << 0,
    kQTVRPanoFlagAlwaysWrap                     = 1 << 2
};
```

### Data Types

```c
typedef float                                       Float32;
```

#### Sample Description Header Structure

```c
typedef struct QTVRSampleDescription {
    UInt32                              size;
    UInt32                              type;
    UInt32                              reserved1;
    UInt16                              reserved2;
    UInt16                              dataRefIndex;
    UInt32                              data;
} QTVRSampleDescription, *QTVRSampleDescriptionPtr, **QTVRSampleDescriptionHandle;
```

#### String Atom Structure

```c
typedef struct QTVRStringAtom {
    UInt16                              stringUsage;
    UInt16                              stringLength;
    unsigned char                       string[4];
} QTVRStringAtom, *QTVRStringAtomPtr;
```

#### VR World Header Atom Structure

```c
typedef struct QTVRWorldHeaderAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    QTAtomID                            nameAtomID;
    UInt32                              defaultNodeID;
    UInt32                              vrWorldFlags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRWorldHeaderAtom, *QTVRWorldHeaderAtomPtr;
```

#### Panorama-Imaging Atom Structure

```c
typedef struct QTVRPanoImagingAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              imagingMode;
    UInt32                              imagingValidFlags;
    UInt32                              correction;
    UInt32                              quality;
    UInt32                              directDraw;
    UInt32                              imagingProperties[6];
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRPanoImagingAtom, *QTVRPanoImagingAtomPtr;
```

#### Node Location Atom Structure

```c
typedef struct QTVRNodeLocationAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              nodeType;
    UInt32                              locationFlags;
    UInt32                              locationData;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRNodeLocationAtom, *QTVRNodeLocationAtomPtr;
```

#### Node Header Atom Structure

```c
typedef struct QTVRNodeHeaderAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              nodeType;
    QTAtomID                            nodeID;
    QTAtomID                            nameAtomID;
    QTAtomID                            commentAtomID;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRNodeHeaderAtom, *QTVRNodeHeaderAtomPtr;
```

#### Hot Spot Information Atom Structure

```c
typedef struct QTVRHotSpotInfoAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              hotSpotType;
    QTAtomID                            nameAtomID;
    QTAtomID                            commentAtomID;
    SInt32                              cursorID[3];
    Float32                             bestPan;
    Float32                             bestTilt;
    Float32                             bestFOV;
    FloatPoint                          bestViewCenter;
    Rect                                hotSpotRect;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRHotSpotInfoAtom, *QTVRHotSpotInfoAtomPtr;
```

#### Link Hot Spot Atom Structure

```c
typedef struct QTVRLinkHotSpotAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              toNodeID;
    UInt32                              fromValidFlags;
    Float32                             fromPan;
    Float32                             fromTilt;
    Float32                             fromFOV;
    FloatPoint                          fromViewCenter;
    UInt32                              toValidFlags;
    Float32                             toPan;
    Float32                             toTilt;
    Float32                             toFOV;
    FloatPoint                          toViewCenter;
    Float32                             distance;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRLinkHotSpotAtom, *QTVRLinkHotSpotAtomPtr;
```

#### Angle Range Atom Structure

```c
typedef struct QTVRAngleRangeAtom {
    Float32                             minimumAngle;
    Float32                             maximumAngle;
} QTVRAngleRangeAtom, *QTVRAngleRangeAtomPtr;
```

#### Panorama Sample Atom Structure

```c
typedef struct QTVRPanoSampleAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              imageRefTrackIndex;
    UInt32                              hotSpotRefTrackIndex;
    Float32                             minPan;
    Float32                             maxPan;
    Float32                             minTilt;
    Float32                             maxTilt;
    Float32                             minFieldOfView;
    Float32                             maxFieldOfView;
    Float32                             defaultPan;
    Float32                             defaultTilt;
    Float32                             defaultFieldOfView;
    UInt32                              imageSizeX;
    UInt32                              imageSizeY;
    UInt16                              imageNumFramesX;
    UInt16                              imageNumFramesY;
    UInt32                              hotSpotSizeX;
    UInt32                              hotSpotSizeY;
    UInt16                              hotSpotNumFramesX;
    UInt16                              hotSpotNumFramesY;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRPanoSampleAtom, *QTVRPanoSampleAtomPtr;
```

#### Cubic View Atom Structure

```swift
struct QTVRCubicViewAtom {
    Float32         minPan;
    Float32         maxPan;
    Float32         minTilt;
    Float32         maxTilt;
    Float32         minFieldOfView;
    Float32         maxFieldOfView;

    Float32         defaultPan;
    Float32         defaultTilt;
    Float32         defaultFieldOfView;
};
typedef struct QTVRCubicViewAtom    QTVRCubicViewAtom;
```

#### Cubic Face Data Atom Structure

```swift
struct QTVRCubicFaceData {
    float   orientation[4];
    float   center[2];
    float   aspect;
    float   skew;
};
typedef struct QTVRCubicFaceData    QTVRCubicFaceData;
```

#### Object Sample Atom Structure

```c
typedef struct QTVRObjectSampleAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt16                              movieType;
    UInt16                              viewStateCount;
    UInt16                              defaultViewState;
    UInt16                              mouseDownViewState;
    UInt32                              viewDuration;
    UInt32                              columns;
    UInt32                              rows;
    Float32                             mouseMotionScale;
    Float32                             minPan;
    Float32                             maxPan;
    Float32                             defaultPan;
    Float32                             minTilt;
    Float32                             maxTilt;
    Float32                             defaultTilt;
    Float32                             minFieldOfView;
    Float32                             fieldOfView;
    Float32                             defaultFieldOfView;
    Float32                             defaultViewCenterH;
    Float32                             defaultViewCenterV;
    Float32                             viewRate;
    Float32                             frameRate;
    UInt32                              animationSettings;
    UInt32                              controlSettings;
} QTVRObjectSampleAtom, *QTVRObjectSampleAtomPtr;
```

#### Track Reference Entry Structure

```swift
struct QTVRTrackRefEntry {
    UInt32                      trackRefType;
    UInt16                      trackResolution;
    UInt32                      trackRefIndex;
};
typedef struct QTVRTrackRefEntry QTVRTrackRefEntry;
```

[Next](Profile%20Atom%20Guidelines.md)[Previous](Metadata%20Handling.md)
