---
title: Out of This GWorld
apple_id: DTS10000094
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-12'
source_url: https://developer.apple.com/library/archive/samplecode/Out_of_This_GWorld/Listings/out_h.html
archived_at: '2026-07-18T03:18:16.467403Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Out of This GWorld](Out%20of%20This%20GWorld.md)


[Next](Document%20Revision%20History.md)[Previous](out.c.md)

# out.h

```c
/*
    File:       out.h

    Contains:   This application demonstrates one method to                 
                produce animation on the Macintosh using QuickDraw's        
                palette manager animation routines.  The app simply         
                creates an offscreen image, copies it to the                
                screen's window, then calls AnimatePalette()                
                every cycle through the eventloop.  To provide the          
                fastest possible animation, the image is only               
                created and copied once from the offscreen GWorld.          
                The actual animation is produced by shifting the            
                color entries within its colortable forward or              
                backward one index.  Also the cTable is divided             
                and shifted in two separate groups to simulate              
                objects moving at different speeds.         

    Written by: EL

    Copyright:  Copyright © 1991-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                08/2000     JM              Carbonized, non-Carbon code is commented out
                                            for demonstration purposes.
                7/16/1999   KG              Updated for Metrowerks Codewarror Pro 2.1


*/
#include "CarbonPrefix.h"
#include <AppleEvents.h>
#include <Types.h>
#include <Resources.h>
#include <QuickDraw.h>
#include <Fonts.h>
#include <Events.h>
#include <Windows.h>
#include <Menus.h>
#include <TextEdit.h>
#include <Dialogs.h>
//#include <Desk.h>
#include <Devices.h>
#include <ToolUtils.h>
#include <Memory.h>
#include <SegLoad.h>
#include <Files.h>
#include <OSUtils.h>
//#include <OSEvents.h>
#include <Events.h>
#include <DiskInit.h>
#include <Packages.h>
#include <Traps.h>
#include <QDOffscreen.h>
#include <Palettes.h>

/* Constant Declarations */

#define WWIDTH      360
#define WHEIGHT     360

//#define WLEFT     (((qd.screenBits.bounds.right - qd.screenBits.bounds.left) - WWIDTH) / 2)
//#define WTOP      (((qd.screenBits.bounds.bottom - qd.screenBits.bounds.top) - WHEIGHT) / 2)

#define TOTALCOLORS 255
#define SUN2MAC     (65535. / 255.)
#define SCALE       3

#define STOP        0
#define START       1
#define FORWARD     0
#define REVERSE     1
#define COLOR       0
#define GRAY        1

extern  WindowPtr       gWindow;
extern  CTabHandle      gCTable;
extern  GWorldPtr       gGWorld;
extern  PixMapHandle    gPixMap;
extern  PaletteHandle   gPalette;

extern  int             gCurrentPat;
extern  int             gCurrentMove;
extern  int             gCurrentDir;
extern  int             gCurrentColor;

void initMac();
void initVariables();
void createWindow();
void createGWorld();
void createPalette();
void updatePalette();
void defineColorPalette();
void defineGrayPalette();
void createImage();
void drawWindowBorder();
void drawImage();
void pollEvents();
void cleanUp();
void doAbout();
void setRGB();
void setColor();

void createColorScale();
void createColorWheels();
void createColorRings();
void createColorGears();
void createColorCurves();
void createColorBalls();
void createColorWave();
void createColorText();

void animateCTable();

void testTriangle();
void shadeWasher();
void translate();
void scale();
void drawCircle();
void drawWasher();
void drawLine();

void setUpMenus();
void adjustMenus();
void enable();
void handleMenu();
```

[Next](Document%20Revision%20History.md)[Previous](out.c.md)

