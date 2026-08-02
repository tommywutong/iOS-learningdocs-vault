---
title: DTS.Utilities
apple_id: DTS10000277
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-17'
source_url: https://developer.apple.com/library/archive/samplecode/DTS.Utilities/Listings/UtilitiesCommon_h.html
archived_at: '2026-07-18T03:05:51.219752Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DTS.Utilities](DTS.Utilities.md)


[Next](Document%20Revision%20History.md)[Previous](Utilities.r.md)

# UtilitiesCommon.h

```
/*
    File:       UtilitiesCommon.h

    Contains:   Collection of Utilities for DTS Sample code

    Written by:     

    Copyright:  Copyright © 1988-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/18/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#define kUseCreatorString       (-1)        /* Pass this to StandardAbout if you would
                                               like the string stored in your creator
                                               resource to appear in the about box. */
#define kUseRealAppName         (-2)        /* Pass this to StandardAbout if you would
                                               like the name of your application to
                                               appear in the about box. */

#define rUtilErrorAlert         256         /* dlg ID used in ErrorAlert */
#define rUtilErrorMessageAlert  257         /* dlg ID used in ErrorAlertMessage */
#define rStdAboutAlert          258         /* dlg ID used for About box. */

#define rUtilStrings            256         /* STR# resource we use for errors. */
#define eStandardErr            1           /* Generic "An error occured" string. */
#define eNoMenuBar              2           /* "No 'MBAR' resource was found." */

#define kButtonFrameSize        3           /* button frameÕs pen size */
#define kButtonFrameInset       (-4)        /* inset rectangle adjustment around button */

#define kExtremeNeg             (-32768)    /* kExtremeNeg and kExtremePos are used to set
                                               up wide open rectangles and regions. */
#define kExtremePos             (32767 - 1) /* required to address an old region bug */

#define kDITop                  0x0050      /* kTopLeft - for positioning the Disk
                                               Initialization dialogs. */
#define kDILeft                 0x0070

#define kControlInvisible       0
#define kControlVisible         0xFF
#define kCntlActivate           0           /* enabled controlÕs hilite state */
#define kCntlDeactivate         0xFF        /* disabled controlÕs hilite state */
#define kCntlOn                 1           /* controlÕs value when truned on */
#define kCntlOff                0           /* controlÕs value when truned off */
#define kSelect                 1           /* select the control */
#define kDeselect               0           /* deselect the control */

#define kScrollbarWidth         16          /* kScrollBarWidth can be used in
                                               calculating values for control
                                               positioning and sizing.*/
#define kScrollbarAdjust        (kScrollbarWidth - 1)
```

[Next](Document%20Revision%20History.md)[Previous](Utilities.r.md)

