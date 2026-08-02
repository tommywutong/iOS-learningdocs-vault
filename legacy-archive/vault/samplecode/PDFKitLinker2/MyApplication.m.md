---
title: PDFKitLinker2
apple_id: DTS10003594
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-08-10'
source_url: https://developer.apple.com/library/archive/samplecode/PDFKitLinker2/Listings/MyApplication_m.html
archived_at: '2026-07-18T03:18:25.980389Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDFKitLinker2](PDFKitLinker2.md)


[Next](MyDocument.h.md)[Previous](MyApplication.h.md)

# MyApplication.m

```objc
// ======================================================================================================================
//  MyApplication.m
// ======================================================================================================================


#import "MyApplication.h"
#import "MyWindowController.h"


@implementation MyApplication
// ======================================================================================================== MyApplication
// ---------------------------------------------------------------------------------------------------------- findOptions

- (int) findOptions
{
    int     options = 0;

    if ([_ignoreCaseCheckbox intValue])
        options = options | NSCaseInsensitiveSearch;

    return options;
}

// ------------------------------------------------------------------------------------------------------------- findNext

- (void) findNext: (id) sender
{
    MyWindowController  *controller;
    PDFView             *theView;
    PDFSelection        *selection;

    controller = [[self mainWindow] windowController];
    if (controller == NULL)
        return;

    theView = [controller pdfView];
    selection = [[theView document] findString: [_findPanelSearchField stringValue] fromSelection: 
            [theView currentSelection] withOptions: [self findOptions]];
    if (selection)
    {
        [theView setCurrentSelection: selection];
        [theView scrollSelectionToVisible: self];
    }
    else
    {
        NSBeep();
    }
}

// ----------------------------------------------------------------------------------------- findNextAndOrderOutFindPanel

- (void) findNextAndOrderOutFindPanel: (id) sender
{
    [self findNext: sender];
    [_findPanel orderOut: self];
}

// --------------------------------------------------------------------------------------------------------- findPrevious

- (void) findPrevious: (id) sender
{
    MyWindowController  *controller;
    PDFView             *theView;
    PDFSelection        *selection;

    controller = [[self mainWindow] windowController];
    if (controller == NULL)
        return;

    theView = [controller pdfView];
    selection = [[theView document] findString: [_findPanelSearchField stringValue] fromSelection: 
            [theView currentSelection] withOptions: [self findOptions] | NSBackwardsSearch];
    if (selection)
    {
        [theView setCurrentSelection: selection];
        [theView scrollSelectionToVisible: self];
    }
    else
    {
        NSBeep();
    }
}

// ----------------------------------------------------------------------------------------------- performFindPanelAction

- (void) performFindPanelAction: (id) sender
{
    MyWindowController  *controller;
    PDFView             *theView;
    PDFSelection        *selection;
    NSPasteboard        *findPasteboard;

    switch ([sender tag])
    {
        case NSFindPanelActionShowFindPanel:
        [_findPanel makeKeyAndOrderFront: self];
        break;

        // Select next row.
        case NSFindPanelActionNext:
        [self findNext: sender];
        break;

        case NSFindPanelActionPrevious:
        [self findPrevious: sender];
        break;

        case NSFindPanelActionReplaceAll:
        case NSFindPanelActionReplace:
        case NSFindPanelActionReplaceAndFind:
        case NSFindPanelActionReplaceAllInSelection:
        NSBeep();
        break;

        // Get selected text.
        case NSFindPanelActionSetFindString:
        controller = [[self mainWindow] windowController];
        if (controller)
        {
            theView = [controller pdfView];
            selection = [theView currentSelection];
            if (selection == NULL)
                break;
        }

        // Load up on find pasteboard.
        findPasteboard = [NSPasteboard pasteboardWithName: NSFindPboard];
        [findPasteboard declareTypes: [NSArray arrayWithObject: NSStringPboardType] owner: NULL];
        [findPasteboard setString: [selection string] forType: NSStringPboardType];

        // Select it.
        [_findPanelSearchField setStringValue: [selection string]];
        break;

        case NSFindPanelActionSelectAll:
        case NSFindPanelActionSelectAllInSelection:
        NSBeep();
        break;
    }
}

// ----------------------------------------------------------------------------------------------------- validateMenuItem

- (BOOL) validateMenuItem: (NSMenuItem *) menuItem
{
    BOOL        enable = YES;

    if ([menuItem action] == @selector(performFindPanelAction:))
    {
        if ([menuItem tag] != NSFindPanelActionSetFindString)
        {
            NSWindowController  *controller;

            // Do we have a window controller (document open)?
            controller = [[self mainWindow] windowController];

            // No document: no find, otherwise see that there is text worth searching.
            if (controller == NULL)
            {
                enable = NO;
            }
            else
            {
                if ([menuItem tag] != NSFindPanelActionShowFindPanel)
                    enable = ([[_findPanelSearchField stringValue] length] > 0);
            }
        }
    }

    return enable;
}

@end
```

[Next](MyDocument.h.md)[Previous](MyApplication.h.md)

