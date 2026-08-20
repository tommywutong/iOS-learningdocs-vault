---
title: txRatio PICT
apple_id: DTS10000177
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/txRatio_PICT/Listings/txRatioPict_c.html
archived_at: '2026-07-26T19:52:27.973833Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [txRatio PICT](txRatio%20PICT.md)


[Next](Document%20Revision%20History.md)[Previous](txRatio%20PICT.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# txRatioPict.c

```c
/*
    File:       txRatioPict.c

    Contains:   Creates a PICT file with a PICT containing the txRatio opcode.
                Someone wanted such a picture, so this is how to create one.

    Written by:

    Copyright:  Copyright © 1984-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/14/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1

*/
#include <Files.h>
#include <StandardFile.h>
#include <Fonts.h>

PicHandle InitPicture(void);
void PutPictToFile(PicHandle thePicture);

/*------ main ----------------------------------------------------------------------------*/

PicHandle ourPict;

void main()

{

GrafPort myPort;

    InitGraf((Ptr) &qd.thePort);
    OpenPort(&myPort);
    InitFonts();
    InitWindows();
    InitMenus();
    TEInit();
    InitDialogs(nil);
    InitCursor();

    ourPict = InitPicture();                    // get our picture
    PutPictToFile(ourPict);                     // put it to a file
    KillPicture(ourPict);                       // and then kill it

} /* main */

/*------ PutPictToFile ----------------------------------------------------------------------------*/

void PutPictToFile(PicHandle thePicture)

{

    SFReply tr;
    short   fRefNum, count;
    long inOutCount;
    Point   where;
    unsigned char header[512];
    OSErr myError;

    for (count = 0; count < 512; count++)
        header[count] = 0x00;

    where.h=100; where.v=50;     /* where the  Standard File dialog window goes */

    SFPutFile( where, "\pSave PICT as:", "\pMy PICT File", NULL, &tr );

    if ( tr.good ) {
        myError = Create(tr.fName, tr.vRefNum, '????', 'PICT');
        if (myError == dupFNErr) {
            myError = FSDelete(tr.fName,tr.vRefNum);
            myError = Create(tr.fName, tr.vRefNum, '????', 'PICT');
        }       /* this is quick 'n' dirty or there'd be more robust handling here */

        myError = FSOpen( tr.fName, tr.vRefNum, &fRefNum );
        if ( myError == noErr ) {
            inOutCount = 512;
            myError = FSWrite(fRefNum, &inOutCount, header);        /* write the header */
            HLock((Handle)thePicture);
            if (myError == noErr) {                 /* don't write if error the first time */
                inOutCount = GetHandleSize((Handle)thePicture);
                myError = FSWrite(fRefNum,&inOutCount,*thePicture);
            }
            FSClose( fRefNum );         /* close it */
            HUnlock((Handle)thePicture);
        }
    }
}

/*------ InitPicture ----------------------------------------------------------------------*/

PicHandle InitPicture (void)

{
    Rect myRect;
    PicHandle thePicHandle;
    CGrafPort myPort;
    PixPatHandle thePixPat;
    short theFont, textSize = 14;
    Str31 myString = "A wonderful test";
    Point myNumer, myDenom;

    OpenCPort(&myPort);
    SetRect(&myRect,0,0,200,200);
    thePicHandle = OpenPicture(&myRect);
    ClipRect(&myRect);

    thePixPat = GetPixPat(16);

    FillCOval(&myRect,thePixPat);

    MoveTo(22,22);
    LineTo(55,55);
    LineTo(58,22);
    LineTo(22,58);

    GetFNum ("\pTimes", &theFont);
    TextFont (theFont);
    TextSize (textSize);

    myNumer.v = 3;
    myNumer.h = myDenom.h = myDenom.v = 1;

    StdText(16, &myString, myNumer, myDenom);  /* string length hard-coded to avoid linking in
                                                  an ANSI library */

//  DrawString("\pA wonderful test");

    ClosePicture();
    CloseCPort(&myPort);

    return(thePicHandle);

}  /* InitPicture */
```

[Next](Document%20Revision%20History.md)[Previous](txRatio%20PICT.md)

