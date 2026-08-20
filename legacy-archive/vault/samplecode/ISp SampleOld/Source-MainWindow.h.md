---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_MainWindow_h.html
archived_at: '2026-07-18T03:12:09.876976Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-MemoryHandler.c.md)[Previous](Source-MainWindow.cp.md)

# Source/MainWindow.h

```c
/*
    File:       MainWindow.h

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

       <SP1>      7/1/99    BWS     first checked in
*/

#ifndef __MAINWINDOW__
#define __MAINWINDOW__

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Includes

#include "ShellWindow.h"
#include "ISp_Sample.h"

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Types

class MainWindow : public ShellWindow
{
private:

    Input_GameState     mInputState;
    float               mAngleOfRoll;
    float               mAngleOfPitch;
    float               mAngleOfYaw;
    float               mVelocity;

    void AdjustControlPositions(void);

    void DrawStringCentered (StringPtr string, SInt16 height);
    void DrawStringLeftJustified (StringPtr string, SInt16 indent, SInt16 height, SInt16 eraseSize);
    void DrawStringRightJustified (StringPtr string, SInt16 indent, SInt16 height, SInt16 eraseSize);

    void FixedToString (Fixed inFixed, StringPtr ioString);
    void FloatToString (float inFloat, StringPtr ioString);

    float   AdjustAngleByAxisInput (float inCurrentAngle, SInt32 inAxisValue);
    float   AdjustAngleByFixedDelta (float inCurrentAngle, Fixed inDeltaValue);

public:

    MainWindow();
    ~MainWindow();

    virtual void    Update(void);
    virtual OSErr   Grow(const Point inWhere);
    virtual OSErr   Click(const Point inWhere, const short inModifiers);
    virtual OSErr   Close(void);
    virtual void    Idle(void);
    virtual Boolean Menu(const UInt32 inMenuCommand, const short inModifiers);
    virtual void    Suspend(void);
    virtual void    Resume(void);

    void DrawContents(void);
    void DrawValues(void);

    void StartGame(void);
    void EndGame(void);
    void TogglePauseGame(void);

    void GetWeaponString (SInt16 inWeapon, StringPtr ioString);
};

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Functions

#ifdef __cplusplus
extern "C" {
#endif

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-MemoryHandler.c.md)[Previous](Source-MainWindow.cp.md)

