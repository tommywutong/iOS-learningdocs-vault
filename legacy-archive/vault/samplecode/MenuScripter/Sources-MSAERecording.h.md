---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAERecording_h.html
archived_at: '2026-07-18T03:14:38.586378Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAERevert.c.md)[Previous](Sources-MSAERecording.c.md)

# Sources/MSAERecording.h

```c
// MSAERecording.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAERECORDING__
#define __MSAERECORDING__

#include "MSGlobals.h"

#include "MSToken.h"

OSErr           InstallRecordingHandlers(void);

pascal OSErr    HandleStartRecording(const AppleEvent   *theAppleEvent,
                                            AppleEvent  *reply,
                                            long        handlerRefCon); 

pascal OSErr    HandleStopRecording(const AppleEvent    *theAppleEvent,
                                            AppleEvent  *reply,
                                            long        handlerRefCon); 

OSErr       MakeWindowObj(WindowPtr theWindow, AEDesc *result);
OSErr       MakeDocumentObj(WindowPtr theWindow, AEDesc *result);

OSErr       MakeTextObjFromToken(TextToken* theToken, AEDesc* result);
OSErr       MakeSelectedTextObj(WindowPtr   theWindow,
                                TEHandle    theTextEditHandle,
                                AEDesc      *result);
OSErr       MakeTextObj(WindowPtr theWindow, short selStart, short selEnd, AEDesc *result);


enum editCommandType
{
    editCutCommand   = 1,
    editCopyCommand  = 2,
    editPasteCommand = 3,
    editClearCommand = 4
};

typedef enum editCommandType editCommandType;

OSErr   SendSelectionEvent(DPtr docPtr);
void    DoEditCommand(DPtr theDocument, editCommandType whatCommand);
OSErr   SendAESetObjProp(AEDesc *theObj, DescType theProp, AEDesc *theData, AEAddressDesc *toWhom);

    // Text Commands

void    IssueCutCommand(DPtr theDocument);
void    IssueCopyCommand(DPtr theDocument);
void    IssuePasteCommand(DPtr theDocument);
void    IssueClearCommand(DPtr theDocument);
void    IssueFontCommand(DPtr theDocument, short theItem);
void    IssueSizeCommand(DPtr theDocument, short theItem);
void    IssueStyleCommand(DPtr theDocument, short theItem);

    // Window Commands

void    IssueZoomCommand(WindowPtr whichWindow, short whichPart);
void    IssueCloseCommand(WindowPtr whichWindow);
void    IssueSizeWindow(WindowPtr whichWindow, short newHSize,short newVSize);
void    IssueMoveWindow(WindowPtr whichWindow, Rect* sizeRect);
void    IssuePageSetupWindow(WindowPtr whichWindow, TPrint thePageSetup);
void    IssueGXPageSetupWindow(WindowPtr whichWindow, gxJob thGXJob);

#define kUsePrintDialog true
#define kNoPrintDialog false
void    IssuePrintWindow( WindowPtr whichWindow, Boolean useDialog);

    // Document Commands

OSErr   IssueAEOpenDoc(FSSpec myFSSpec);
void    IssueAENewWindow(void);
OSErr   IssueSaveCommand(WindowPtr theWindow, FSSpecPtr where);

OSErr   IssueRevertCommand(WindowPtr theWindow);
OSErr   IssueQuitCommand(void);

    // Recording of Keystrokes

void    AddKeyToTypingBuffer(DPtr theDocument, char theKey);
void    FlushAndRecordTypingBuffer(void);


void    StyleTokConst(short theStyleItem, DescType *thekConst);
OSErr   BuildTypeTextStylesDesc(Style onStyles, Style offStyles, AEDesc *resultDesc);
OSErr   BuildTextStylesDesc(Style theStyle, AEDesc *resultDesc);
OSErr   BuildStyledTextDesc(TEHandle theHTE, short start, short howLong, AEDesc *resultDesc);


Boolean PoseSizeDialog(long *whatSize);
OSErr   IssueSetDataObjToBufferContents(const AEDesc* theObj);

#endif
```

[Next](Sources-MSAERevert.c.md)[Previous](Sources-MSAERecording.c.md)

