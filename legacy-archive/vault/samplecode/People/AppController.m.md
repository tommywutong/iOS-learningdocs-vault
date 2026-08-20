---
title: People
apple_id: DTS40009050
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-07-21'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_People/Listings/AppController_m.html
archived_at: '2026-07-18T03:25:53.105981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [People](People.md)


[Next](AppControllerExtensions.h.md)[Previous](AppController.h.md)

# AppController.m

```objc
/*

File: AppController.m

Abstract: Part of the People project demonstrating use of the
              SyncServices framework

Version: 0.1

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Computer, Inc. ("Apple") in consideration of your agreement to the
following terms, and your use, installation, modification or
redistribution of this Apple software constitutes acceptance of these
terms.  If you do not agree with these terms, please do not use,
install, modify or redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software. 
Neither the name, trademarks, service marks or logos of Apple Computer,
Inc. may be used to endorse or promote products derived from the Apple
Software without specific prior written permission from Apple.  Except
as expressly stated in this notice, no other rights or licenses, express
or implied, are granted by Apple herein, including but not limited to
any patent rights that may be infringed by your derivative works or by
other works in which the Apple Software may be incorporated.

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

Copyright © 2005-2009 Apple Computer, Inc., All Rights Reserved.

*/ 

#import <SyncServices/SyncServices.h>

#import "AppController.h"
#import "AppControllerSyncing.h"
#import "AppControllerExtensions.h"
#import "Change.h"
#import "Constants.h"
#import "PeopleImageView.h"

static AppController *g_sharedAppController = nil;

@implementation AppController

//
// ===========================================
// General
//

- (void)awakeFromNib
{
    g_sharedAppController = self;

    m_entityNames = [[NSArray alloc] initWithObjects:EntityContact, nil];

    m_records = [[NSMutableArray alloc] init];
    m_changes = [[NSMutableArray alloc] init];

    m_syncMode = FastSync;

    [self readDataFile];
    [self update];

    if ([m_records count] > 0) {
        [m_table selectRowIndexes:[NSIndexSet indexSetWithIndex:0] byExtendingSelection:NO];
        [m_table scrollRowToVisible:0];
    }

    ISyncClient *client = [self registerClient];
    [client setSyncAlertHandler:self selector:@selector(client:willSyncEntityNames:)];

    [m_officialImageView setViewType:OfficialViewType];
    [m_candidImageView setViewType:CandidViewType];
    [m_extremeImageView setViewType:ExtremeViewType];

    [m_officialImageView registerForDraggedTypes:
        [NSArray arrayWithObject: NSFilenamesPboardType]];

    [m_candidImageView registerForDraggedTypes:
        [NSArray arrayWithObject: NSFilenamesPboardType]];

    [m_extremeImageView registerForDraggedTypes:
        [NSArray arrayWithObject: NSFilenamesPboardType]];

    [[NSNotificationCenter defaultCenter] addObserver:self
        selector:@selector(photoAdded:)
        name:@"PhotoAdded" object:nil];
}

+ (AppController *)sharedAppController
{
    return g_sharedAppController;
}

- (NSArray *)entityNames
{
    return m_entityNames;
}

//
// ===========================================
// Do and Undo
//

- (void)applyChange:(Change *)change
{
    if (!change)
        return;

    NSInteger rowToSelect = -1;
    NSInteger row = [change row];

    switch ([change type]) {
        case AddRecord:
            if (row >= [m_records count])
                [m_records addObject:[change record]];
            else
                [m_records insertObject:[change record] atIndex:row];
            rowToSelect = row;
            break;
        case DeleteRecord:
            [m_records removeObjectAtIndex:row];
            if ([m_records count] > 0)
                rowToSelect = row - 1 >= 0 ? row - 1 : 0;
            break;
        case ModifyRecord:
            [m_records replaceObjectAtIndex:row withObject:[change record]];
            rowToSelect = row;
            break;
    }

    [m_table reloadData];
    [self update];

    if (rowToSelect == -1) {
        [m_table deselectAll:self];
    }
    else {
        [m_table selectRowIndexes:[NSIndexSet indexSetWithIndex:rowToSelect] byExtendingSelection:NO];
        [m_table scrollRowToVisible:rowToSelect];
    }

    [m_changes addObject:change];

    [[m_window undoManager] registerUndoWithTarget:self selector:@selector(unapplyChange:) object:change];
    [self writeDataFile];
}

- (void)unapplyChange:(Change *)change
{
    if (!change)
        return;

    NSInteger rowToSelect = -1;
    NSInteger row = [change row];

    switch ([change type]) {
        case AddRecord:
            [m_records removeObjectAtIndex:row];
            if ([m_records count] > 0)
                rowToSelect = row - 1 >= 0 ? row - 1 : 0;
            break;
        case DeleteRecord:
            if (row >= [m_records count]) {
                [m_records addObject:[change oldRecord]];
                row++;
            } else
                [m_records insertObject:[change oldRecord] atIndex:row];
            rowToSelect = row;
            break;
        case ModifyRecord:
            [m_records replaceObjectAtIndex:row withObject:[change oldRecord]];
            rowToSelect = row;
            break;
    }
    [m_table reloadData];
    [self update];

    if (rowToSelect == -1) {
        [m_table deselectAll:self];
    }
    else {
        [m_table selectRowIndexes:[NSIndexSet indexSetWithIndex:rowToSelect] byExtendingSelection:NO];
        [m_table scrollRowToVisible:rowToSelect];
    }

    [m_changes removeLastObject];
    [[m_window undoManager] registerUndoWithTarget:self selector:@selector(applyChange:) object:change];
    [self writeDataFile];
}

//
// ===========================================
// Model and View
//

- (id)tableView:(NSTableView *)tableView 
    objectValueForTableColumn:(NSTableColumn *)tableColumn 
    row:(NSInteger)row
{
    id result = nil;
    if (row >= 0 && row < [m_records count]) {
        NSDictionary *record = [m_records objectAtIndex:row];
        result = [record objectForKey:[tableColumn identifier]];
    }
    return result;
}

- (void)tableView:(NSTableView *)tableView
    setObjectValue:(id)object
    forTableColumn:(NSTableColumn *)tableColumn
    row:(NSInteger)row
{
    if (row >= 0 && row < [m_records count]) {
        NSDictionary *oldRecord = [m_records objectAtIndex:row];
        NSDictionary *record = nil;
        if ([[tableColumn identifier] isEqual:FirstNameKey]) {
            record = [NSDictionary dictionaryWithObjectsAndKeys:
                object, FirstNameKey,
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:LastNameKey], LastNameKey, 
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,
                [oldRecord objectForKey:ImageKey], ImageKey,
                [oldRecord objectForKey:CandidPhotoKey], CandidPhotoKey,
                [oldRecord objectForKey:ExtremePhotoKey], ExtremePhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
        }
        else if ([[tableColumn identifier] isEqual:MiddleNameKey]) {
            record = [NSDictionary dictionaryWithObjectsAndKeys:
                object, MiddleNameKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:LastNameKey], LastNameKey, 
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,                
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,                
                [oldRecord objectForKey:ImageKey], ImageKey,
                [oldRecord objectForKey:CandidPhotoKey], CandidPhotoKey,
                [oldRecord objectForKey:ExtremePhotoKey], ExtremePhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
        }
        else if ([[tableColumn identifier] isEqual:LastNameKey]) {
            record = [NSDictionary dictionaryWithObjectsAndKeys:
                object, LastNameKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,                
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,                
                [oldRecord objectForKey:ImageKey], ImageKey,
                [oldRecord objectForKey:CandidPhotoKey], CandidPhotoKey,
                [oldRecord objectForKey:ExtremePhotoKey], ExtremePhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
        }
        else if ([[tableColumn identifier] isEqual:CompanyNameKey]) {
            record = [NSDictionary dictionaryWithObjectsAndKeys:
                object, CompanyNameKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:LastNameKey], LastNameKey,
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,
                [oldRecord objectForKey:ImageKey], ImageKey,
                [oldRecord objectForKey:CandidPhotoKey], CandidPhotoKey,
                [oldRecord objectForKey:ExtremePhotoKey], ExtremePhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
        }
        else if ([[tableColumn identifier] isEqual:LocationNameKey]) {
            record = [NSDictionary dictionaryWithObjectsAndKeys:
                object, LocationNameKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,                
                [oldRecord objectForKey:LastNameKey], LastNameKey,
                [oldRecord objectForKey:ImageKey], ImageKey,
                [oldRecord objectForKey:CandidPhotoKey], CandidPhotoKey,
                [oldRecord objectForKey:ExtremePhotoKey], ExtremePhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
        }
        else if ([[tableColumn identifier] isEqual:ImageKey]) {
            record = [NSDictionary dictionaryWithObjectsAndKeys:
                object, ImageKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,                
                [oldRecord objectForKey:LastNameKey], LastNameKey,
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,                
                [oldRecord objectForKey:CandidPhotoKey], CandidPhotoKey,
                [oldRecord objectForKey:ExtremePhotoKey], ExtremePhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
        }
        else if ([[tableColumn identifier] isEqual:CandidPhotoKey]) {
            record = [NSDictionary dictionaryWithObjectsAndKeys:
                object, CandidPhotoKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,                
                [oldRecord objectForKey:LastNameKey], LastNameKey,
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,                
                [oldRecord objectForKey:ImageKey], ImageKey,
                [oldRecord objectForKey:ExtremePhotoKey], ExtremePhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
        }
        else if ([[tableColumn identifier] isEqual:ExtremePhotoKey]) {
            record = [NSDictionary dictionaryWithObjectsAndKeys:
                object, ExtremePhotoKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,                
                [oldRecord objectForKey:LastNameKey], LastNameKey,
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,                
                [oldRecord objectForKey:ImageKey], ImageKey,
                [oldRecord objectForKey:CandidPhotoKey], CandidPhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
        }
        [self applyChange:[Change modifyRecordChange:record oldRecord:oldRecord row:row]];
    }
}

- (NSInteger)numberOfRowsInTableView:(NSTableView *)tableView
{
    return [m_records count];
}

- (void) tableViewSelectionDidChange: (NSNotification *) notification
{
    NSInteger selectedRow = [m_table selectedRow];
    BOOL hasSelectedRow =  (selectedRow != -1);

    //update the image view
    if ( hasSelectedRow ) {

        NSDictionary *record = [m_records objectAtIndex:selectedRow];
        NSImage *official = [[NSImage alloc] initWithData:[record objectForKey:ImageKey]];
        [m_officialImageView setImage: official];
        [official release];
        [m_officialImageView setNeedsDisplay: YES];

        NSImage *candid = [[NSImage alloc] initWithData:[record objectForKey:CandidPhotoKey]];
        [m_candidImageView setImage: candid];
        [candid release];
        [m_candidImageView setNeedsDisplay: YES];

        NSImage *extreme = [[NSImage alloc] initWithData:[record objectForKey:ExtremePhotoKey]];
        [m_extremeImageView setImage: extreme];
        [extreme release];
        [m_extremeImageView setNeedsDisplay: YES];
    }
}

- (void)update
{
    // m_countLabel
    NSString *countString = nil;
    if ([m_records count] == 1) {
        countString = @"1 Person";
    }
    else {
        countString = [NSString stringWithFormat:@"%d People", [m_records count]];
    }
    [m_countLabel setStringValue:countString];

    // m_table
    NSInteger row = [m_table selectedRow];
    if (row >= 0) {
        [m_table scrollRowToVisible:row];
    }
}

- (void)photoAdded:(NSNotification *)notification
{
    NSImage *image = [[notification object] image];

    if (image) {
        // fit the image in the view's bounds
        ///            [image drawInRect:[[notification object] bounds]
        ///                     fromRect: NSMakeRect(0, 0, [image size].width, [image size].height)
        ///                    operation: NSCompositeSourceOver
        ///                     fraction: 1.0];            

        NSInteger row = [m_table selectedRow];
        if (row >= 0 && row < [m_records count]) {
            NSDictionary *oldRecord = [m_records objectAtIndex:row];
            NSDictionary *record = nil;

            switch([[notification object] viewType])
            {
            case OfficialViewType:
                record = [NSDictionary dictionaryWithObjectsAndKeys:
                [image TIFFRepresentation], ImageKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,                
                [oldRecord objectForKey:LastNameKey], LastNameKey,
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,                
                [oldRecord objectForKey:CandidPhotoKey], CandidPhotoKey,
                [oldRecord objectForKey:ExtremePhotoKey], ExtremePhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
                [self applyChange:[Change modifyRecordChange:record oldRecord:oldRecord row:row]];
                break;

            case CandidViewType:
                record = [NSDictionary dictionaryWithObjectsAndKeys:
                [image TIFFRepresentation], CandidPhotoKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,                
                [oldRecord objectForKey:LastNameKey], LastNameKey,
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,                
                [oldRecord objectForKey:ImageKey], ImageKey,
                [oldRecord objectForKey:ExtremePhotoKey], ExtremePhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
                [self applyChange:[Change modifyRecordChange:record oldRecord:oldRecord row:row]];
                break;

            case ExtremeViewType:
                record = [NSDictionary dictionaryWithObjectsAndKeys:
                [image TIFFRepresentation], ExtremePhotoKey, 
                [oldRecord objectForKey:FirstNameKey], FirstNameKey, 
                [oldRecord objectForKey:MiddleNameKey], MiddleNameKey,
                [oldRecord objectForKey:CompanyNameKey], CompanyNameKey,                
                [oldRecord objectForKey:LastNameKey], LastNameKey,
                [oldRecord objectForKey:LocationNameKey], LocationNameKey,                
                [oldRecord objectForKey:ImageKey], ImageKey,
                [oldRecord objectForKey:CandidPhotoKey], CandidPhotoKey,
                [oldRecord objectForKey:IdentifierKey], IdentifierKey, 
                nil];
                [self applyChange:[Change modifyRecordChange:record oldRecord:oldRecord row:row]];
                break;
            }

        }
    }

}
//
// ===========================================
// IBActions
//
- (IBAction)delete:(id)sender
{
    NSInteger row = [m_table selectedRow];
    if (row < 0)
        return;

    NSDictionary *record = [m_records objectAtIndex:row];
    [self applyChange:[Change deleteRecordChange:record row:row]];

    //refresh photo tab view contents for deleted row
    [[NSNotificationCenter defaultCenter]
        postNotificationName:NSTableViewSelectionDidChangeNotification object:m_table];
}

- (IBAction)newPerson:(id)sender
{
    CFUUIDRef uuid = CFUUIDCreate(NULL);
    NSString *identifier = (NSString *)CFUUIDCreateString(NULL, uuid);
    CFRelease(uuid);

    NSDictionary *record = [NSDictionary dictionaryWithObjectsAndKeys:
        @"FirstName", FirstNameKey, 
        @"LastName", LastNameKey,
        @"", MiddleNameKey,
        @"", CompanyNameKey,
        @"", LocationNameKey,
        [[NSImage imageNamed: DefaultPhoto] TIFFRepresentation], ImageKey,
        [[NSImage imageNamed: DefaultPhoto] TIFFRepresentation], CandidPhotoKey,
        [[NSImage imageNamed: DefaultPhoto] TIFFRepresentation], ExtremePhotoKey,
        identifier, IdentifierKey, 
        nil];

    [self applyChange:[Change addRecordChange:record row:0]];

    //refresh photo tab view contents for inserted row
    [[NSNotificationCenter defaultCenter]
        postNotificationName:NSTableViewSelectionDidChangeNotification object:m_table];
}

- (BOOL)validateUserInterfaceItem:(id <NSValidatedUserInterfaceItem>)item
{
    NSInteger value = [item tag];
    switch (value) {
        case UsesRecordFiltering:
            [(NSMenuItem *)item setState:m_syncsUsingRecordFiltering ? NSOnState : NSOffState];
            break;
        case UsesRecordFormatting:
            [(NSMenuItem *)item setState:m_syncsUsingRecordFormatting ? NSOnState : NSOffState];
            break;
        case UsesSyncAlertHandler:
            [(NSMenuItem *)item setState:m_syncsUsingSyncAlertHandler ? NSOnState : NSOffState];
            break;
        case SyncsOnAppDeactivate:
            [(NSMenuItem *)item setState:m_syncsOnAppDeactivate ? NSOnState : NSOffState];
            break;
    }
    return YES;
}

//
// ===========================================
// Persistence
//

- (void)readDataFile
{
    NSData *data = [NSData dataWithContentsOfFile:DataFilePath];
    if (!data) {
        m_syncMode = RefreshSync;
        return;
    }

    NSPropertyListFormat format;
    NSArray *array = [NSPropertyListSerialization propertyListFromData:data 
        mutabilityOption:NSPropertyListImmutable 
        format:&format
        errorDescription:nil];

    if (array) {
        [m_records removeAllObjects];
        [m_records addObjectsFromArray:array];
        [self sortNamesAndDisplay];
    }
    else {
        NSLog(@"error reading data file");
    }
}

- (void)writeDataFile
{
    NSData *data = [NSPropertyListSerialization dataFromPropertyList:m_records 
        format:NSPropertyListXMLFormat_v1_0 
        errorDescription:nil];
    if (!data) {
        NSLog(@"error converting data");
        return;    
    }

    BOOL result = [data writeToFile:DataFilePath atomically:YES];
    if (!result) {
        NSLog(@"error writing data file");
    }
}

@end
```

[Next](AppControllerExtensions.h.md)[Previous](AppController.h.md)

