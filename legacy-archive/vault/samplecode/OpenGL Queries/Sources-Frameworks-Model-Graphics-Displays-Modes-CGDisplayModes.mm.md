---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Graphics_Displays_Modes_CGDisplayModes_mm.html
archived_at: '2026-07-18T03:18:13.720562Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Graphics-Displays-Modes-CGDisplayModes.h.md)[Previous](Sources-Frameworks-Model-Query-QueryDataSource.h.md)

# Sources/Frameworks/Model/Graphics/Displays/Modes/CGDisplayModes.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class to acquire all cg display modes usable for desktop gui.
 */

#pragma mark -
#pragma mark Private - Headers

#import "CGDisplayModes.h"

#pragma mark -
#pragma mark Private - Constructor

CG::Display::Modes::Modes(const CGDirectDisplayID& nDisplay)
{
    if(nDisplay)
    {
        CFArrayRef pModes = CGDisplayCopyAllDisplayModes(nDisplay, nullptr);

        if(pModes != nullptr)
        {
            CFIndex i;
            CFIndex iMax = CFArrayGetCount(pModes);

            CGDisplayModeRef pDisplayMode = nullptr;

            for(i = 0; i < iMax; ++i)
            {
                pDisplayMode = CGDisplayModeRef(CFArrayGetValueAtIndex(pModes, i));

                if(pDisplayMode != nullptr)
                {
                    CG::Display::Mode mode(pDisplayMode);

                    if(mode.isUsable())
                    {
                        m_Modes.push_back(mode.handle());
                        m_Table.emplace(mode.handle(), mode);
                    } // if
                } // if
            } // for

            mnCount = m_Modes.size();

            CFRelease(pModes);

            mnDDID = nDisplay;
        } // if
    } // if
} // Constructor

#pragma mark -
#pragma mark Private - Copy Constructor

CG::Display::Modes::Modes(const CG::Display::Modes& rModes)
{
   m_Modes = rModes.m_Modes;
   m_Table = rModes.m_Table;
   mnDDID  = rModes.mnDDID;
} // Copy Constructor

#pragma mark -
#pragma mark Private - Destructor

CG::Display::Modes::~Modes()
{
    if(!m_Table.empty())
    {
        m_Table.clear();
    } // if

    if(!m_Modes.empty())
    {
        m_Modes.clear();
    } // if
} // Destructor

#pragma mark -
#pragma mark Private - Assignment Operator

CG::Display::Modes& CG::Display::Modes::operator=(const CG::Display::Modes& rModes)
{
    if(this != &rModes)
    {
        m_Modes = rModes.m_Modes;
        m_Table = rModes.m_Table;
        mnDDID  = rModes.mnDDID;
    } // if

    return *this;
} // Operator =

#pragma mark -
#pragma mark Private - Accessors

const uint32_t& CG::Display::Modes::display() const
{
    return mnDDID;
} // display

const CG::Display::ModeTable& CG::Display::Modes::table() const
{
    return m_Table;
} // table

const CG::Display::ModeIDs& CG::Display::Modes::modes() const
{
    return m_Modes;
} // modes

const size_t& CG::Display::Modes::count() const
{
    return mnCount;
} // count

const CG::Display::Mode CG::Display::Modes::mode(const uint32_t& nID) const
{
    CG::Display::Mode value;

    CG::Display::ModeTable::const_iterator pIter = m_Table.find(nID);

    if(pIter != m_Table.end())
    {
        value = pIter->second;
    } // if

    return value;
} // mode
```

[Next](Sources-Frameworks-Model-Graphics-Displays-Modes-CGDisplayModes.h.md)[Previous](Sources-Frameworks-Model-Query-QueryDataSource.h.md)

