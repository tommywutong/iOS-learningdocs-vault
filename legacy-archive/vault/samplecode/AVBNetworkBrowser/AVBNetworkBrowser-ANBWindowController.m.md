---
title: AVBNetworkBrowser
apple_id: DTS40014220
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioVideoBridging
published: '2014-03-20'
source_url: https://developer.apple.com/library/archive/samplecode/sc1827/Listings/AVBNetworkBrowser_ANBWindowController_m.html
archived_at: '2026-07-26T19:54:13.938967Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVBNetworkBrowser](AVBNetworkBrowser.md)


[Next](AVBNetworkBrowser-AVBTypes.h.md)[Previous](AVBNetworkBrowser-ANBWindowController.h.md)

# AVBNetworkBrowser/ANBWindowController.m

```objc
/*

     File: ANBWindowController.m
 Abstract: Implementation for NSWindowController subclass for maintaining the user interface. It uses a view based NSTableView to display the entities available on the network.
  Version: 1.0

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

 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 */

#import "ANBWindowController.h"

#import "ANBInterface.h"
#import "ANBAVDECCEntity.h"

@interface ANBWindowController ()

@end

@implementation ANBWindowController

- (id)initWithWindow:(NSWindow *)window
{
    self = [super initWithWindow:window];
    if (self)
    {
        _tableContents = [NSMutableArray array];
    }
    return self;
}

- (NSString *)windowNibName
{
    return [self className];
}

- (void)windowDidLoad
{
    [super windowDidLoad];

    // Implement this method to handle any initialization after your window controller's window has been loaded from its nib file.
}

#pragma mark Table View Handling

- (NSInteger)numberOfRowsInTableView:(NSTableView *)tableView
{
    return _tableContents.count;
}

//If the object is an ANBInterface then it is a group row otherwise it is an entry (and an ANBAVDECCEntity object)
- (BOOL)tableView:(NSTableView *)tableView isGroupRow:(NSInteger)row
{
    BOOL isGroup = NO;

    if ([[_tableContents objectAtIndex:row] isKindOfClass:[ANBInterface class]])
    {
        isGroup = YES;
    }

    return isGroup;
}

// We make the "group rows" have the standard height, while all other image rows have a larger height
- (CGFloat)tableView:(NSTableView *)tableView heightOfRow:(NSInteger)row
{
    CGFloat rowHeight;

    if ([[_tableContents objectAtIndex:row] isKindOfClass:[ANBInterface class]])
    {
        rowHeight = [tableView rowHeight];
    }
    else
    {
        rowHeight = 75.0;
    }

    return rowHeight;
}

//This is a view based table (rather than cell based) so return the right view for the row type. The views are defined in
//the xib file in the table.
- (NSView *)tableView:(NSTableView *)tableView viewForTableColumn:(NSTableColumn *)tableColumn row:(NSInteger)row
{
    if ([[_tableContents objectAtIndex:row] isKindOfClass:[ANBInterface class]])
    {
        ANBInterface *interface = [_tableContents objectAtIndex:row];
        NSTextField *textField = [tableView makeViewWithIdentifier:@"TextCell" owner:self];
        [textField setStringValue:interface.userInterfaceName];
        return textField;
    }
    else
    {
        NSTableCellView *cellView = [tableView makeViewWithIdentifier:@"MainCell" owner:self];
        cellView.objectValue = [_tableContents objectAtIndex:row];

        return cellView;
    }
}

//The user changed the selection so update the selected property (used by the Cocoa Bindings in the detail view)
//The table does not have multiple selection turned on so there will always be only one selected row.
- (void)tableViewSelectionDidChange:(NSNotification *)notification
{
    NSUInteger selected = [_tableView selectedRow];

    if(selected < _tableContents.count)
    {
        if([[_tableContents objectAtIndex:[_tableView selectedRow]] isKindOfClass:[ANBAVDECCEntity class]])
        {
            self.selected = [_tableContents objectAtIndex:[_tableView selectedRow]];
        }
        else
        {
            self.selected = nil;
        }
    }
    else
    {
        self.selected = nil;
    }
}

//App delegate calls this method whenever entites are added or removed on an interface or when interfaces are added and removed
- (void)didUpdateInterfaceEntities:(NSDictionary *)interfaces
{
    //Create a sorted list of keys (sort the BSD names of the interfaces) so that they are always displayed in the same order.
    NSArray *sorted = [[interfaces allKeys] sortedArrayUsingDescriptors:@[[NSSortDescriptor sortDescriptorWithKey:@"self" ascending:YES]]];

    [_tableContents removeAllObjects];

    //Walk through the dictionary of interfaces updating the table contents.
    for(NSString *ifName in sorted)
    {
        ANBInterface *interface = [interfaces objectForKey:ifName];

        [_tableContents addObject:interface];

        [_tableContents addObjectsFromArray:interface.avdeccEntities];
    }

    //If we removed the object that was selected update the selected object.
    if(![_tableContents containsObject:self.selected])
    {
        [self tableViewSelectionDidChange:nil];
    }

    [_tableView reloadData];
}

@end
```

[Next](AVBNetworkBrowser-AVBTypes.h.md)[Previous](AVBNetworkBrowser-ANBWindowController.h.md)

