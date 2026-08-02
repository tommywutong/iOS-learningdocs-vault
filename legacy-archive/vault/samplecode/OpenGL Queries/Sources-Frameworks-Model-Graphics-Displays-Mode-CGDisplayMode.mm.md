---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Graphics_Displays_Mode_CGDisplayMode_mm.html
archived_at: '2026-07-18T03:18:13.602772Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Graphics-Displays-Mode-CGDisplayMode.h.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Modes-CGDisplayModes.h.md)

# Sources/Frameworks/Model/Graphics/Displays/Mode/CGDisplayMode.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class to acquire cg display mode properties.
 */

#pragma mark -
#pragma mark Private - Headers

#import "CGDisplayMode.h"

#pragma mark -
#pragma mark Private - Utilities

// We'll use the handle later as a key  to create a table of all
// the modes that are useful and can be used for desktop gui.
static uint32_t CGDisplayModeGetHandleFromModeID(const CGDisplayModeRef pDisplayMode)
{
    // Returns a negative number for the mode id
    int32_t nModeID = CGDisplayModeGetIODisplayModeID(pDisplayMode);

    // The upper 16-bits are always 0xFFFF0000, so we'll mask here to select
    // only the lower 16-bits - which we can later use as key for hashing.
    return nModeID & 0x0000FFFF;
} // CGDisplayModeGetHandleFromModeID

// Display dimensions in points
static CG::Display::Size CGDisplayModeGetPointSize(const CGDisplayModeRef pDisplayMode)
{
    CG::Display::Size size;

    size.width  = CGDisplayModeGetWidth(pDisplayMode);
    size.height = CGDisplayModeGetHeight(pDisplayMode);

    return size;
} // CGDisplayModeGetPointSize

// Display dimensions in pixels
static CG::Display::Size CGDisplayModeGetPixelSize(const CGDisplayModeRef pDisplayMode)
{
    CG::Display::Size size;

    size.width  = CGDisplayModeGetPixelWidth(pDisplayMode);
    size.height = CGDisplayModeGetPixelHeight(pDisplayMode);

    return size;
} // CGDisplayModeGetPixelSize

#pragma mark -
#pragma mark Public - Constructor

CG::Display::Mode::Mode(const CGDisplayModeRef pDisplayMode)
{
    if(pDisplayMode != nullptr)
    {
        // Is this mode usable for desktop UI
        mbIsUsable = CGDisplayModeIsUsableForDesktopGUI(pDisplayMode);

        // Get flags associated withthis mode
        mnFlags = CGDisplayModeGetIOFlags(pDisplayMode);

        // Display dimensions in points
        m_Points = CGDisplayModeGetPointSize(pDisplayMode);

        // Display dimensions in pixels
        m_Pixels = CGDisplayModeGetPixelSize(pDisplayMode);

        // We'll the handle later as a key  to create a table of all
        // the modes that are useful and can be used for desktop gui.
        mnHandle = CGDisplayModeGetHandleFromModeID(pDisplayMode);
    } // if
} // Constructor

#pragma mark -
#pragma mark Public - Copy Constructor

CG::Display::Mode::Mode(const CG::Display::Mode& rMode)
{
    mbIsUsable = rMode.mbIsUsable;
    mnFlags    = rMode.mnFlags;
    mnHandle   = rMode.mnHandle;

    m_Points.width  = rMode.m_Points.width;
    m_Points.height = rMode.m_Points.height;

    m_Pixels.width  = rMode.m_Pixels.width;
    m_Pixels.height = rMode.m_Pixels.height;
} // Mode

#pragma mark -
#pragma mark Public - Destructor

CG::Display::Mode::~Mode()
{
    mbIsUsable = false;
    mnFlags    = 0;
    mnHandle   = 0;

    m_Points.width  = 0;
    m_Points.height = 0;
    m_Pixels.width  = 0;
    m_Pixels.height = 0;
} // Destructor

#pragma mark -
#pragma mark Private - Assignment Operator

CG::Display::Mode& CG::Display::Mode::operator=(const CG::Display::Mode& rMode)
{
    if(this != &rMode)
    {
        mbIsUsable = rMode.mbIsUsable;
        mnFlags    = rMode.mnFlags;
        mnHandle   = rMode.mnHandle;

        m_Points.width  = rMode.m_Points.width;
        m_Points.height = rMode.m_Points.height;

        m_Pixels.width  = rMode.m_Pixels.width;
        m_Pixels.height = rMode.m_Pixels.height;
    } // if

    return *this;
} // Operator =

#pragma mark -
#pragma mark Public - Query

const bool& CG::Display::Mode::isUsable() const
{
    return mbIsUsable;
} // isUsable

#pragma mark -
#pragma mark Public - Accessors

const CG::Display::Size& CG::Display::Mode::points() const
{
    return m_Points;
} // width

const CG::Display::Size& CG::Display::Mode::pixels() const
{
    return m_Pixels;
} // height

const uint32_t& CG::Display::Mode::flags() const
{
    return mnFlags;
} // flags

const uint32_t& CG::Display::Mode::handle() const
{
    return mnHandle;
} // handle
```

[Next](Sources-Frameworks-Model-Graphics-Displays-Mode-CGDisplayMode.h.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Modes-CGDisplayModes.h.md)

