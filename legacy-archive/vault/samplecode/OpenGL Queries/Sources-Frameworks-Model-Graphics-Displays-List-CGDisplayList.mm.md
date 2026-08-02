---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Graphics_Displays_List_CGDisplayList_mm.html
archived_at: '2026-07-18T03:18:13.505595Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Graphics-Displays-List-CGDisplayList.h.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Data-CGDisplaysDataSource.h.md)

# Sources/Frameworks/Model/Graphics/Displays/List/CGDisplayList.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Mediator class to acquire properties usable for desktop gui for all active displays.
 */

#pragma mark -
#pragma mark Private - Headers

#import <iostream>

#import "CGDisplayList.h"

#pragma mark -
#pragma mark Private - Constructor

CG::Display::List::List(const uint32_t& nDisplayCount)
try :mpDisplays(new uint32_t[nDisplayCount])
{
    // Set the number displays for the impending query
    mnCount = nDisplayCount;

    // Populate an array with active display Ids
    CGError nError = CGGetActiveDisplayList(mnCount, mpDisplays, &mnCount);

    if(nError == kCGErrorSuccess)
    {
        GLuint i;

        for(i = 0; i < mnCount; ++i)
        {
            CG::Display::Modes modes(mpDisplays[i]);

            m_Table.emplace(mpDisplays[i], modes);
        } // for
    } // if
} // Constructore
catch(std::bad_alloc& ba)
{
    std::cerr << ">> ERROR: Failed acquring a backing-store for display identifiers!";
} // catch

#pragma mark -
#pragma mark Private - Destructor

CG::Display::List::~List()
{
    if(mpDisplays != nullptr)
    {
        delete [] mpDisplays;

        mpDisplays = nullptr;
    } // if

    if(!m_Table.empty())
    {
        m_Table.clear();
    } // if
} // Destructor

#pragma mark -
#pragma mark Private - Factory

CG::Display::List *CG::Display::List::create()
{
    GLuint nDisplayCount = 0;

    CG::Display::List *pList = nullptr;

    // Get all the number of active displays (multi-display support)
    CGError  nError = CGGetActiveDisplayList(0, nullptr, &nDisplayCount);

    if(nError == kCGErrorSuccess)
    {
        pList = new (std::nothrow) CG::Display::List(nDisplayCount);

        if(pList == nullptr)
        {
            NSLog(@">> ERROR: Failed creating a CG Display List object!");
        } // if
    } // if

    return pList;
} // create

#pragma mark -
#pragma mark Private - Accessors

const uint32_t& CG::Display::List::count() const
{
    return mnCount;
} // count

const uint32_t* CG::Display::List::displays() const
{
    return mpDisplays;
} // displays

const CG::Display::DisplayTable& CG::Display::List::table() const
{
    return m_Table;
} // table

const CG::Display::Modes CG::Display::List::modes(const uint32_t& nDisplayID) const
{
    CG::Display::Modes value;

    CG::Display::DisplayTable::const_iterator pIter = m_Table.find(nDisplayID);

    if(pIter != m_Table.end())
    {
        value = pIter->second;
    } // if

    return value;
} // modes
```

[Next](Sources-Frameworks-Model-Graphics-Displays-List-CGDisplayList.h.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Data-CGDisplaysDataSource.h.md)

