---
title: SimpleDownload
apple_id: DTS10000658
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleDownload/Listings/MyWindowController_m.html
archived_at: '2026-07-18T03:23:59.915314Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleDownload](SimpleDownload.md)


[Next](Document%20Revision%20History.md)[Previous](MyWindowController.h.md)

# MyWindowController.m

```objc
//////////
//
//  File:       MyWindowController.m
//
//  Contains:   Implementation file for the MyWindowController class.
//
//  Written by: Apple Image Capture Engineering
//
//  Copyright:  © 2001-2002 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//     
//     <1>      11/05/01    hwn     first file
//
//////////

/*
 IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc. ("Apple") in
 consideration of your agreement to the following terms, and your use, installation, 
 modification or redistribution of this Apple software constitutes acceptance of these 
 terms.  If you do not agree with these terms, please do not use, install, modify or 
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and subject to these 
 terms, Apple grants you a personal, non-exclusive license, under AppleÕs copyrights in 
 this original Apple software (the "Apple Software"), to use, reproduce, modify and 
 redistribute the Apple Software, with or without modifications, in source and/or binary 
 forms; provided that if you redistribute the Apple Software in its entirety and without 
 modifications, you must retain this notice and the following text and disclaimers in all 
 such redistributions of the Apple Software.  Neither the name, trademarks, service marks 
 or logos of Apple Computer, Inc. may be used to endorse or promote products derived from 
 the Apple Software without specific prior written permission from Apple. Except as expressly
 stated in this notice, no other rights or licenses, express or implied, are granted by Apple
 herein, including but not limited to any patent rights that may be infringed by your 
 derivative works or by other works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO WARRANTIES, 
 EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, 
 MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS 
 USE AND OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR CONSEQUENTIAL 
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS 
 OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, 
 REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND 
 WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY OR 
 OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#import <Carbon/Carbon.h>
#import "MyWindowController.h"

// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
// MyCompletion
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
void MyCompletion(ICAHeader * pbHeader)
{
    if (pbHeader->refcon)
        [(MyWindowController*)pbHeader->refcon handleNotification:(ICARegisterEventNotificationPB*)pbHeader];

}

@implementation MyWindowController

// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
//  - applicationShouldTerminateAfterLastWindowClosed
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender
{
    return YES;
}

// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
//  - numberOfRowsInTableView:
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (int)numberOfRowsInTableView:(NSTableView *)tableView
{
    int count = 0;
    if (dataArray)
        count = [dataArray count];
    return count;
}


// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
//  - tableView:objectValueForTableColumn:row:
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (id)tableView:(NSTableView *)tableView objectValueForTableColumn:(NSTableColumn *)tableColumn row:(int)row
{
    NSString * identifier = [tableColumn identifier];

    if ([identifier isEqualToString:@"index"])
        return [NSNumber numberWithInt:row];
    else if (dataArray)
    {
        if ([identifier isEqualToString:@"name"])
        {
            return [[dataArray objectAtIndex:row] objectForKey:@"ifil"];
        } else if ([identifier isEqualToString:@"size"])
        {
            return [[dataArray objectAtIndex:row] objectForKey:@"isiz"];
        }
    }
    return @"???";
}

// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
//  - updateFiles
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (void)updateFiles
{
    OSErr               err;
    ICAGetDeviceListPB  devListPB;

    [dataArray release];

    // get the devicelist
    memset(&devListPB, 0, sizeof(ICAGetDeviceListPB));
    err = ICAGetDeviceList(&devListPB, NULL);
    if (err == noErr)
    {
        ICAGetNthChildPB nthChildPB;

        // get the first device
        memset(&nthChildPB, 0, sizeof(ICAGetNthChildPB));
        nthChildPB.parentObject = devListPB.object;
        nthChildPB.index        = 0;
        err = ICAGetNthChild(&nthChildPB, NULL);
        if (err == 0)
        {
            ICACopyObjectPropertyDictionaryPB propPB;
            NSDictionary*                     dict;

            NSLog(@"got 1st device: %08X", nthChildPB.childObject);
            // 
            memset(&propPB, 0, sizeof(ICACopyObjectPropertyDictionaryPB));
            propPB.object  = nthChildPB.childObject;
            propPB.theDict = (CFDictionaryRef *)&dict;

            err = ICACopyObjectPropertyDictionary(&propPB, NULL);
            if (err == noErr)
            {
                [[self window] setTitle:[dict objectForKey:@"ifil"]];
                dataArray = [dict objectForKey:@"data"];
           }
        }
    }
}
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
// - installNotification:
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (void)installNotification
{
    ICARegisterEventNotificationPB pb;
    OSErr   err;

    memset(&pb, 0, sizeof(ICARegisterEventNotificationPB));
    pb.header.refcon = (UInt32)self;
    pb.object        = 0;   // all objects
    pb.notifyType    = 0;   // all types
    pb.notifyProc    = MyCompletion;
    err = ICARegisterEventNotification(&pb, NULL);
    if (noErr == err) 
    {
        NSLog(@"notification callback registered");
    }
}

// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
//  - awakeFromNib
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (void)awakeFromNib
{
    [self updateFiles];
    [self installNotification];
}

// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
//  - clearInfo:
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (void)clearInfo:(id)sender
{
    [sender setStringValue:@""];
}

// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
//  - download:
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (IBAction)download:(id)sender
{
    if (dataArray)
    {
        int         selectedRow;
        ICAObject   downloadObject;

        selectedRow = [table selectedRow];
        downloadObject = (ICAObject)[[[dataArray objectAtIndex:selectedRow] objectForKey:@"icao"] longValue];
        if (downloadObject)
        {
            OSErr err;
            FSRef pictFolderFSRef;
            FSRef fileFSRef;

            err = FSFindFolder(kOnAppropriateDisk, kPictureDocumentsFolderType, false, &pictFolderFSRef);
            if (noErr == err)
            {
                ICADownloadFilePB pb;

                memset(&pb, 0, sizeof(ICADownloadFilePB));
                pb.object   = downloadObject;
                pb.dirFSRef = &pictFolderFSRef;
                pb.flags    = kCreateCustomIcon;
                pb.fileFSRef= &fileFSRef;
                err = ICADownloadFile(&pb, NULL);
                if (noErr == err)
                {
                    char      fileName[255];
                    NSString* nsFileName;
                    NSString* infoStr = @"File downloaded to: ";

                    FSRefMakePath(&fileFSRef, fileName, 255);
                    nsFileName = [[NSString stringWithCString:fileName] stringByAbbreviatingWithTildeInPath];
                    infoStr = [infoStr stringByAppendingString:nsFileName];
                    [info setStringValue:infoStr];
                } else if (dupFNErr == err)
                {
                    [info setStringValue:[NSString stringWithFormat:@"File was not downloaded again, because it already exists on disk..."]];
                } else
                {
                    [info setStringValue:[NSString stringWithFormat:@"ERROR: ICADownloadFile returned %d", err]];
                }
                [self performSelector:@selector(clearInfo:) withObject:info afterDelay:4.0];
            }
        }
    }
}

// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
//  - tableViewSelectionDidChange:
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (void)tableViewSelectionDidChange:(NSNotification *)notification
{
    int  selectedRow;
    BOOL enabled;

    selectedRow = [table selectedRow];
    enabled = (selectedRow != -1);
    [downloadButton setEnabled:enabled];
}

// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
// - handleNotification:
// ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
- (void)handleNotification:(ICARegisterEventNotificationPB *)pb
{
    [self updateFiles];
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](MyWindowController.h.md)

