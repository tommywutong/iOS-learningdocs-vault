---
title: FinalCutPro_AppleEvents
apple_id: DTS10004110
resource_type: Sample Code
platform: macOS
topic: Apple Applications
technology: null
published: '2009-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/FinalCutPro_AppleEvents/Listings/AEController_m.html
archived_at: '2026-07-18T03:08:39.678092Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FinalCutPro_AppleEvents](FinalCutProAppleEvents.md)


[Next](appleevent.h.md)[Previous](AEController.h.md)

# AEController.m

```objc
/*

    File: AEController.m
Abstract: UI controller class for AEDialog.nib
 Version: 1.2

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Inc. ("Apple") in consideration of your agreement to the following
terms, and your use, installation, modification or redistribution of
this Apple software constitutes acceptance of these terms.  If you do
not agree with these terms, please do not use, install, modify or
redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software.
Neither the name, trademarks, service marks or logos of Apple Inc. may
be used to endorse or promote products derived from the Apple Software
without specific prior written permission from Apple.  Except as
expressly stated in this notice, no other rights or licenses, express or
implied, are granted by Apple herein, including but not limited to any
patent rights that may be infringed by your derivative works or by other
works in which the Apple Software may be incorporated.

The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Copyright (C) 2009 Apple Inc. All Rights Reserved.


*/ 

#import "AEController.h"
#import "FCP_AppleEvents.h"
#import "apple_event.h"


@implementation AEController

- (id)init
{
    self = [super initWithWindowNibName:@"AEDialog"];
    if (self) {
        msgToSend = 0;
        fileURL = nil;
        fileSendMode = sendAsFSRef;
        isProject = YES;
        projFileURL = nil;
        projString = nil;
        mediaFileURL = nil;
        mediaString = @"";
    }
    return self;
}


- (void)windowDidLoad
{
    [self addColumnItems:columnPopUp1];
    [self addColumnItems:columnPopUp2];
}


// I felt it was rather opaque to have these defined in the nib
// especially since there were two popups with the same list
- (void)addColumnItems:(NSPopUpButton *)button
{
    char *list[] = {
        "name",
        "duration",
        "in",  
        "out", 
        "start",
        "end", 
        "scene",
        "shottake",
        "lognote",
        "good",
        "label",
        "label2",
        "mastercomment1",
        "mastercomment2",
        "mastercomment3",
        "mastercomment4",
        "clipcommenta",
        "clipcommentb",
        0
    };
    char **p;

    for (p = list; *p != 0; p++) {
        [button addItemWithTitle:[NSString stringWithCString:*p encoding:NSASCIIStringEncoding]];
    }
}


- (IBAction)clearProjectData:(id)sender
{
    if (fileURL != nil) {
        [fileURL release];
    }   
    fileURL = nil;

    [fileToSend setStringValue: @""];

    // Pop the menu back to the correct chooseMode 
    // Not the best way to do this - since we are hard coding the menu order  
    if ([fileToSend isEditable] == NO) {
        [chooseButton selectItemAtIndex:0];
    } else {
        [chooseButton selectItemAtIndex:1];
    }
}


- (IBAction)switchToPath:(id)sender
{
    NSString *pathString = nil;

    if (fileURL != nil) {
        pathString = [fileURL path];
        [fileURL release];
    }
    fileURL = nil;

    if (pathString == nil) {
        [fileToSend setStringValue: @""];
    } else {
        [fileToSend setStringValue: pathString];
    }
    [fileToSend setEditable:YES];
}


- (IBAction)chooseFileToSend:(id)sender
{
    NSOpenPanel * op = [NSOpenPanel openPanel];
    NSArray *file_types;
    NSString *title;

    // pick a media file or a project, depending on the selected command
    if (msgToSend == kFCPUpdateMediaFile) {
        title = @"Select a media file";
        file_types = [NSArray arrayWithObjects:@"mov", @"MooV", nil];
    } else {
        title = @"Select an FCP project file";
        file_types = [NSArray arrayWithObjects:@"fcp",nil];
    }

    // create the file sheet
    [op setTitle: title];
    [op setCanChooseFiles: YES];
    [op setCanChooseDirectories: NO];
    [op setAllowsMultipleSelection:NO];
    [op beginSheetForDirectory:nil file:nil types: file_types
                modalForWindow:[self window] modalDelegate:self didEndSelector:@selector(sheetDidEnd:returnCode:contextInfo:) 
                   contextInfo:nil];
}


// rather than have two completion routines I use contextInfo to decide where I came from
- (void)sheetDidEnd:(NSWindow *)sheet returnCode:(int)returnCode contextInfo:(void *)contextInfo
{
    if (contextInfo != nil) {
        // sheet started by sendAndReport:
        [NSApp endSheet:sheet];
    } else {
        // sheet started by chooseFileToSend:
        if (returnCode == NSOKButton) {
            [self setSelectedFileURL:[[(NSOpenPanel*)sheet URLs] objectAtIndex:0]];

            NSString *pathString = [fileURL path];

            if (pathString != nil) {
                NSString *newShortName = [pathString lastPathComponent];

                [fileToSend setStringValue: newShortName];
            }
        }
        if ([fileToSend isEditable] == YES) {
            [[fileToSend window] makeFirstResponder:nil];
            [fileToSend setEditable:NO];
        }
    }
}


- (void)setSelectedFileURL:(NSArray *)newURL
{
    if (newURL != nil) {
        if (fileURL != nil) {
            [fileURL release];
        }
        fileURL = [newURL retain];
    }
}


- (IBAction)setSendMode:(id)sender
{
    fileSendMode = [sender tag];
}


// AppleEvent menu items in the AEDialog.nib point to this, with the appropriate tag value
// see also Controller.m
- (IBAction)setMsg:(id)sender
{
    int tag;
    int tab;
    OSType msg;

    if (sender == nil) {
        // this is Controller.m sending us a "choose default"
        tag = 0;
    } else {
        tag = [sender tag];
    }

    switch (tag) {
    case 0:     msg = kFCPOpenProjectFile;          tab = tabOpen;  break;
    case 1:     msg = kFCPSaveAndCloseProjectFile;  tab = tabClose; break;
    case 2:     msg = kFCPGetDocumentXML;           tab = tabGet;   break;
    case 3:     msg = kFCPImportXMLToDocument;      tab = tabSend;  break;
    case 4:     msg = kFCPSelectItemInBrowser;      tab = tabUUIDs; break;
    case 5:     msg = kFCPOpenItemInProject;        tab = tabUUID;  break;
    case 6:     msg = kFCPFindItemsInProject;       tab = tabFind;  break;
    case 7:     msg = kFCPGetItemXML;               tab = tabGet;   break;
    case 8:     msg = kFCPGetAllEffectsXML;         tab = tabGet;   break;
    case 9:     msg = kFCPGetAllOpenProjects;       tab = tabOpen;  break;
    case 10:    msg = kFCPUpdateMediaFile;          tab = tabOpen;  break;
    case 11:    msg = kFCPSaveProjectFileAs;        tab = tabSave;  break;
    case 12:    msg = kFCPGetProjectTOC;            tab = tabGet;   break;

    default:    return;
    }

    // show/hide the general controls to make the tab look right
    if (msg == kFCPGetAllEffectsXML || msg == kFCPGetAllOpenProjects) {
        [fileLabel setHidden:YES];
        [modeButton setHidden:YES];
        [chooseButton setHidden:YES];
        [fileToSend setHidden:YES];
    } else if (msg == kFCPUpdateMediaFile) {
        [fileLabel setHidden:YES];
        [modeButton setHidden:NO];
        [chooseButton setHidden:NO];
        [fileToSend setHidden:NO];
    } else {
        [fileLabel setHidden:NO];
        [modeButton setHidden:NO];
        [chooseButton setHidden:NO];
        [fileToSend setHidden:NO];
    }

    // alter controls in the 'get' tab
    if (msg == kFCPGetItemXML) {
        [uuidLabel setHidden:NO];
        [uuidToGet setHidden:NO];
    } else {
        [uuidLabel setHidden:YES];
        [uuidToGet setHidden:YES];
    }
    if (msg == kFCPGetProjectTOC) {
        [xmlVersion setEditable:NO];
        [xmlVersion setStringValue: @"n/a"];
    } else {
        [xmlVersion setEditable:YES];
        [xmlVersion setStringValue: @"5.0"];
    }

    // swap between project file / media file selection
    if (msg == kFCPUpdateMediaFile) {
        if (isProject == YES) {
            isProject = NO;
            projFileURL = [fileURL retain];
            projString = [[fileToSend stringValue] retain];
            fileURL = mediaFileURL;
            [fileToSend setStringValue:mediaString];
            [mediaFileURL release];
            [mediaString release];
        }
        [mixedStateLabel setHidden:NO];
        [ignoreDateButton setHidden:NO];
    } else {
        if (isProject == NO) {
            isProject = YES;
            mediaFileURL = [fileURL retain];
            mediaString = [[fileToSend stringValue] retain];
            fileURL = projFileURL;
            [fileToSend setStringValue:projString];
            [projFileURL release];
            [projString release];
        }
        [mixedStateLabel setHidden:YES];
        [ignoreDateButton setHidden:YES];
    }

    // switch to correct tab
    [event selectItemWithTag:tag];
    [tabView selectTabViewItemWithIdentifier:[[NSNumber numberWithInt:tab] stringValue]];
    msgToSend = msg;
}


- (void)sendAndReport: (apple_event *) evt
{
    OSStatus err_num;

    err_num = [evt send];
    if (err_num != noErr) {
        // NSBeginAlertSheet( NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton,
        //      NSWindow *docWindow, id modalDelegate, SEL didEndSelector,
        //      SEL didDismissSelector, void *contextInfo, NSString *msg, ... );            
        NSBeginAlertSheet(@"AppleEvent error", nil, nil, nil,
                [self window], self, @selector(sheetDidEnd:returnCode:contextInfo:),
                nil, self, @"%d", err_num);
        // NSRunAlertPanel(@"AppleEvent error", @"%d", nil, nil, nil, err_num);
        // NSLog(@"Error was: %D", err_num)
    }
}


// The apple_event class encapsulates all the grubby low-level AppleEvent stuff
// The structure for sending an event is:
//      alloc/init
//      fill in the top level info
//      set up all the parameters
//      send the event & report any error
//      deal with reply data
//
- (IBAction)sendAppleEvent:(id)sender
{
    apple_event *evt = [[apple_event alloc] init];
    [evt create:msgToSend class:kFCPEventClass dest:kFCPEventClass];

    if (msgToSend ==  kFCPGetAllEffectsXML) {
        [evt version:[xmlVersion stringValue]];
        [self sendAndReport: evt];
        [evt createDocFromXML:([reformatButton state] == NSOnState)];

    } else if (msgToSend == kFCPGetAllOpenProjects) {
        [self sendAndReport: evt];
        [evt createDocFromList];

    } else if (msgToSend == kFCPUpdateMediaFile) {
        [evt sendAFile:[fileToSend stringValue] 
                    url:fileURL 
                    key:kFCPMediaFileKey
                    as:fileSendMode];
        [evt modDate:[ignoreDateButton state]];
        [self sendAndReport: evt];

    } else {
        // All the rest of the events take a project file
        [evt sendAFile:[fileToSend stringValue] 
                    url:fileURL 
                    key:kFCPProjectFileKey
                    as:fileSendMode];

        if (msgToSend == kFCPOpenProjectFile) {
            [self sendAndReport: evt];

        } else if (msgToSend == kFCPSaveAndCloseProjectFile) {
            [evt save:[saveButton state]];
            [self sendAndReport: evt];

        } else if (msgToSend == kFCPGetDocumentXML) {
            [evt version:[xmlVersion stringValue]];
            [self sendAndReport: evt];
            [evt createDocFromXML:([reformatButton state] == NSOnState)];

        } else if (msgToSend == kFCPImportXMLToDocument) {
            [evt addDoc];
            [self sendAndReport: evt];

        } else if (msgToSend == kFCPFindItemsInProject) {
            [evt logicOr:[logicButton state]];
            [evt criteria:[stringToFind1 stringValue]
                    match:[[matchPopUp1 selectedItem] tag]
                   column:[columnPopUp1 titleOfSelectedItem]
                     omit:([omitButton1 state] == NSOnState)];
            if (! [[stringToFind2 stringValue] isEqualToString:@""]) {
                [evt criteria:[stringToFind2 stringValue]
                        match:[[matchPopUp2 selectedItem] tag]
                       column:[columnPopUp2 titleOfSelectedItem]
                         omit:([omitButton2 state] == NSOnState)];
            }
            [evt addList];
            [self sendAndReport: evt];

        } else if (msgToSend == kFCPOpenItemInProject) {
            [evt uuid:[uuidToActOn stringValue]];
            [uuidToGet setStringValue:[uuidToActOn stringValue]];
            [self sendAndReport: evt];

        } else if (msgToSend == kFCPSelectItemInBrowser) {
            [evt uuids:[uuidsToSelect string]];
            [self sendAndReport: evt];

        } else if (msgToSend == kFCPGetItemXML) {
            [evt version:[xmlVersion stringValue]];
            [evt uuid:[uuidToGet stringValue]];
            [uuidToActOn setStringValue:[uuidToGet stringValue]];
            [self sendAndReport: evt];
            [evt createDocFromXML:([reformatButton state] == NSOnState)];

        } else if (msgToSend == kFCPSaveProjectFileAs) {
            [evt save:[overwriteButton state] as:[savePath stringValue]];
            [self sendAndReport: evt];

        } else if (msgToSend == kFCPGetProjectTOC) {
            [self sendAndReport: evt];
            [evt createDocFromXML:([reformatButton state] == NSOnState)];

        } else {
            // do nothing - unrecognized message
        }
    }
}

@end
```

[Next](appleevent.h.md)[Previous](AEController.h.md)

