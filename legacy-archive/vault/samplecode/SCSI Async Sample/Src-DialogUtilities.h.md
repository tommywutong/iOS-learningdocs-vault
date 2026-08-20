---
title: SCSI Async Sample
apple_id: DTS10000022
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Async_Sample/Listings/Src_DialogUtilities_h.html
archived_at: '2026-07-18T03:22:30.331563Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Async Sample](SCSI%20Async%20Sample.md)


[Next](Src-DisplayTestParameters.c.md)[Previous](Src-DialogUtilities.c.md)

# Src/DialogUtilities.h

```c
/*                                  DialogManager.c                             */
/*
 * DialogManager.c
 * Copyright © 1993 Apple Computer Inc. All rights reserved.
 *
 * Simple subroutines to make Modal Dialogs a pleasant experience for the
 * entire family.
 */
#ifndef THINK_C             /* MPW includes         */
#include <Errors.h>
#include <Script.h>
#include <Types.h>
#include <Files.h>
#include <Resources.h>
#include <QuickDraw.h>
#include <Fonts.h>
#include <Events.h>
#include <Windows.h>
#include <ToolUtils.h>
#include <Memory.h>
#include <Menus.h>
#include <Lists.h>
#include <Printing.h>
#include <Dialogs.h>
#include <StandardFile.h>
#endif

#define kActiveButton       0
#define kCheckedButton      1
#define kDisabledButton     255

void
SelectCheckBox(
        DialogPtr           theDialog,
        short               itemNumber,
        Boolean             *value
    );
void
SetCheckBox(
        DialogPtr           theDialog,
        short               itemNumber,
        Boolean             value
    );
void
SelectRadioButton(
        DialogPtr           theDialog,
        short               first,
        short               last,
        short               item,
        short               *value      /* Has/gets zero to last-1  */
    );
void
SetRadioButtons(
        DialogPtr           theDialog,
        short               first,
        short               last,
        short               value
    );
void
SetDialogButton(
        DialogPtr           theDialog,
        short               item,
        short               value
    );
short
GetDialogButton(
        DialogPtr           theDialog,
        short               item
    );
void
EnableDialogItem(
        DialogPtr           theDialog,
        short               item,
        Boolean             enableItem
    );
signed long
GetDialogValue(
        DialogPtr           theDialog,
        short               item
    );
void
SetDialogValue(
        DialogPtr           theDialog,
        short               item,
        signed long         value
    );
void
SetDialogText(
        DialogPtr           theDialog,
        short               item,
        ConstStr255Param    text
    );
```

[Next](Src-DisplayTestParameters.c.md)[Previous](Src-DialogUtilities.c.md)

