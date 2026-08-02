---
title: PhotoSearch
apple_id: DTS10003994
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoSearch/Listings/MainWindowController_m.html
archived_at: '2026-07-18T03:18:54.772080Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoSearch](PhotoSearch.md)


[Next](CaseInsensitivePredicateTemplate.m.md)[Previous](MainWindowController.h.md)

# MainWindowController.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  This class provides the delegate/datasource for the NSOutlineView and NSPredicateEditor. 
   In addition, it maintains all the controller logic for the user interface. 
 */

#import "MainWindowController.h"
#import "SearchQuery.h"
#import "SearchItem.h"

@interface MainWindowController() <NSOutlineViewDelegate, NSOutlineViewDataSource, NSWindowDelegate, NSPathControlDelegate>

@property (strong) NSMutableArray *iSearchQueries;
@property (assign) CGFloat iThumbnailSize;
@property (strong) NSURL *searchLocation;

@property (weak) IBOutlet NSOutlineView *resultsOutlineView;
@property (weak) IBOutlet NSPathControl *pathControl;            // path control showing the search result item's location
@property (weak) IBOutlet NSPredicateEditor *predicateEditor;
@property (weak) IBOutlet NSWindow *window;
@property (weak) IBOutlet NSPathControl *searchLocationPathControl;  // path control determining the search location

// outlet to the height constraint of the enclosing NSScrollView to the predicate editor,
// each time a row is added or removed, we need to change this constraint value
@property (weak) IBOutlet NSLayoutConstraint *heightConstraint;

@property (strong) NSDateFormatter *dateFormatter;

@end


#pragma mark -

@implementation MainWindowController

@synthesize searchLocation = _searchLocation;

#define COL_IMAGE_ID            @"ImageID"          // NSTableColumn identifier for column 1 (image + title + subtitle + info button)
#define COL_CAMERA_MODEL_ID     @"CameraModelID"    // NSTableColumn identifier for column 2 (camera model)
#define COL_LAST_MODIFIED_ID    @"LastModifiedID"   // NSTableColumn identifier for column 2 (date modified)
#define VIEW_SEARCH_GROUP       @"SearchGroup"      // NSTableCellView identifier (group row view)

#define Search_Location_Key     @"searchLocationKey"// NSUserDefaults key for obtaining the security scoped bookmark search location

#define Info_Button_Key         @"InfoButtonKey"    // key used to identify the info button in each view-row during mouse tracking

#define SubTitle_Tag            1                   // view tag for the sub title string
#define InfoButton_Tag          2                   // view tag for the info button


#pragma mark -

- (void)awakeFromNib {

    // note: since we are using view-based NSOutlineView, awakeFromNib is called each time we call makeViewWithIdentifier
    // and since this window controller is created as a top-level nib object, this is called at initialization time too,
    // so avoid this initialization later when table row views are created.
    //
    if (self.iSearchQueries == nil) {
        _iSearchQueries = [[NSMutableArray alloc] init];
        _iThumbnailSize = 32.0;

        _dateFormatter = [[NSDateFormatter alloc] init];
        self.dateFormatter.timeStyle = NSDateFormatterShortStyle;
        self.dateFormatter.dateStyle = NSDateFormatterMediumStyle;

        [[NSNotificationCenter defaultCenter] addObserver:self
                                                 selector:@selector(queryChildrenChanged:)
                                                     name:SearchQueryChildrenDidChangeNotification
                                                   object:nil];
        [[NSNotificationCenter defaultCenter] addObserver:self
                                                 selector:@selector(searchItemChanged:)
                                                     name:SearchItemDidChangeNotification
                                                   object:nil];
        [[NSNotificationCenter defaultCenter] addObserver:self
                                                 selector:@selector(rowsDidChange:)
                                                     name:NSRuleEditorRowsDidChangeNotification
                                                   object:nil];

        (self.resultsOutlineView).target = self;
        (self.resultsOutlineView).doubleAction = @selector(resultsOutlineDoubleClickAction:);

        NSString *placeHolderStr = NSLocalizedString(@"Select an item to show its location.", @"Placeholder string for location items");
        [[self.pathControl cell] setPlaceholderString:placeHolderStr];
        ((NSPathCell *)(self.pathControl)).placeholderString = placeHolderStr;

        (self.pathControl).target = self;
        (self.pathControl).doubleAction = @selector(pathControlDoubleClick:);

        (self.predicateEditor).rowHeight = 25;

        // add some rows
        [(self.predicateEditor).enclosingScrollView setHasVerticalScroller:NO];
        [self.predicateEditor addRow:self];

        // put the focus in the text field
        id displayValue = [self.predicateEditor displayValuesForRow:1].lastObject;
        if ([displayValue isKindOfClass:[NSControl class]]) {
            [self.window makeFirstResponder:displayValue];
        }

        [self updatePathControl];

        // first look for the saved search location in NSUserDefaults
        NSError *error = nil;
        NSData *bookMarkDataToResolve = [[NSUserDefaults standardUserDefaults] objectForKey:Search_Location_Key];
        if (bookMarkDataToResolve != nil) {
            // we have a saved bookmark from last time, so resolve the bookmark data into our NSURL
            self.searchLocation = [NSURL URLByResolvingBookmarkData:bookMarkDataToResolve
                                                            options:NSURLBookmarkResolutionWithSecurityScope
                                                      relativeToURL:nil
                                                bookmarkDataIsStale:nil
                                                              error:&error];
        }

        if (error != nil || self.searchLocation == nil) {
            // we could not find the default search location (error code could be NSFileNoSuchFileError)
            // meaning the search location last time no longer exists...

            // we don't have a default search location setup yet, so default our searchLocation
            // pointing to "Pictures" folder:
            //
            NSURL *picturesDirectoryURL = [[NSFileManager defaultManager] URLsForDirectory:NSPicturesDirectory
                                                                                  inDomains:NSUserDomainMask].lastObject;
            // write out the NSURL as a security-scoped bookmark to NSUserDefaults
            // (so that we can resolve it again at re-launch), but first resolve the symbolic link to it
            //
            NSError *resolveError = nil;
            NSString *resolvedPath =
            [[NSFileManager defaultManager] destinationOfSymbolicLinkAtPath:picturesDirectoryURL.path
                                                                      error:&resolveError];
            if (resolvedPath != nil && resolveError == nil)
            {
                NSURL *bookMarkURL = [NSURL fileURLWithPath:resolvedPath isDirectory:YES];
                NSData *bookmarkData = [bookMarkURL bookmarkDataWithOptions:NSURLBookmarkCreationWithSecurityScope
                                             includingResourceValuesForKeys:nil
                                                              relativeToURL:nil
                                                                      error:&error];
                NSAssert(bookmarkData != nil, @"could not create security scoped bookmark");

                [[NSUserDefaults standardUserDefaults] setObject:bookmarkData forKey:Search_Location_Key];
                [[NSUserDefaults standardUserDefaults] synchronize];

                self.searchLocation = bookMarkURL;  // remember this for later
            }
        }

        NSAssert(self.searchLocation != nil, @"Could not obtain a default search location");

        // lastly, point our searchLocation NSPathControl to the search location
        (self.searchLocationPathControl).URL = self.searchLocation;

        (self.window).delegate = self;  // we want to be notified when this window is closed
    }
}

- (BOOL)windowShouldClose:(id)sender {

    for (SearchQuery *query in self.iSearchQueries) {
        // we are no longer interested in accessing SearchQuery's bookmarked search location,
        // so it's important we balance the start/stop access to security scoped bookmarks here
        //
        [query.searchURL stopAccessingSecurityScopedResource];
    }
    return YES;
}

- (void)dealloc {

    [[NSNotificationCenter defaultCenter] removeObserver:self name:SearchQueryChildrenDidChangeNotification object:nil];
    [[NSNotificationCenter defaultCenter] removeObserver:self name:SearchItemDidChangeNotification object:nil];
    [[NSNotificationCenter defaultCenter] removeObserver:self name:NSRuleEditorRowsDidChangeNotification object:nil];
}


#pragma mark - NSPredicateEditor support

// user started a search from the predicate editor
//
- (void)createNewSearchForPredicate:(NSPredicate *)predicate withTitle:(NSString *)title withScopeURL:(NSURL *)url {

    if (predicate != nil) {
        // Always search for images
        NSPredicate *imagesPredicate = [NSPredicate predicateWithFormat:@"(kMDItemContentTypeTree = 'public.image')"];
        predicate = [NSCompoundPredicate andPredicateWithSubpredicates:@[imagesPredicate, predicate]];

        // we are interested in accessing this bookmark for our SearchQuery class
        [url startAccessingSecurityScopedResource];

        // Create an instance of our datamodel and keep track of things.
        SearchQuery *searchQuery = [[SearchQuery alloc] initWithSearchPredicate:predicate title:title scopeURL:url];
        [self.iSearchQueries addObject:searchQuery];

        // Reload the children of the root item, "nil"
        [self.resultsOutlineView reloadItem:nil reloadChildren:YES];
        [self.resultsOutlineView expandItem:searchQuery];
        NSInteger row = [self.resultsOutlineView rowForItem:searchQuery];
        [self.resultsOutlineView scrollRowToVisible:row];
        [self.resultsOutlineView selectRowIndexes:[NSIndexSet indexSetWithIndex:row] byExtendingSelection:NO];
    }
}

// Foundation's Spotlight support in NSMetdataQuery places the following requirements on an NSPredicate:
//    - Value-type (always YES or NO) predicates are not allowed
//    - Any compound predicate (other than NOT) must have at least two subpredicates
//  The following method will "clean up" an NSPredicate to make it ready for Spotlight,
//    or return nil if the predicate can't be cleaned.
//
- (NSPredicate *)spotlightFriendlyPredicate:(id)predicate {

    if ([predicate isEqual:[NSPredicate predicateWithValue:YES]] || [predicate isEqual:[NSPredicate predicateWithValue:NO]])
        return nil;
    else if ([predicate isKindOfClass:[NSCompoundPredicate class]]) {
        NSCompoundPredicateType type = [predicate compoundPredicateType];
        NSMutableArray *cleanSubpredicates = [NSMutableArray array];
        for (NSPredicate *dirtySubpredicate in [predicate subpredicates]) {
            NSPredicate *cleanSubpredicate = [self spotlightFriendlyPredicate:dirtySubpredicate];
            if (cleanSubpredicate) [cleanSubpredicates addObject:cleanSubpredicate];
        }

        if (cleanSubpredicates.count == 0) {
            return nil;
        }
        else if (cleanSubpredicates.count == 1 && type != NSNotPredicateType) {
            return cleanSubpredicates[0];
        }
        else {
            return [[NSCompoundPredicate alloc] initWithType:type subpredicates:cleanSubpredicates];
        }
    }
    else return predicate;
}

// this method gets called whenever the predicate editor changes,
// but we only want to create a new predicate when the user hits return.
// So check NSApp currentEvent.
//
- (IBAction)predicateEditorChanged:(id)sender {

    NSEvent *event = NSApp.currentEvent;
    if (event.type == NSKeyDown) {
        NSString *characters = event.characters;
        if (characters.length > 0 && [characters characterAtIndex:0] == 0x0D) {
            /* Get the predicate, which is the object value of our view. */
            NSPredicate *predicate = self.predicateEditor.objectValue;
            /* Make it Spotlight friendly. */
            predicate = [self spotlightFriendlyPredicate:predicate];
            if (predicate) {
                static NSInteger searchIndex = 0;
                    NSString *title = NSLocalizedString(@"Search %ld", @"Search group title");
                [self createNewSearchForPredicate:predicate withTitle:[NSString stringWithFormat:title, (long)++searchIndex] withScopeURL:self.searchLocation];
            }
        }
    }
}

- (void)queryChildrenChanged:(NSNotification *)note {

    [self.resultsOutlineView reloadItem:note.object reloadChildren:YES];
}

// called as a result of "SearchItemDidChangeNotification"
// the item has an updated image preview to display
//
- (void)searchItemChanged:(NSNotification *)note {

    // When an item changes, it only will affect the display state.
    // So, we only need to redisplay its contents, and not reload it
    NSInteger row = [self.resultsOutlineView rowForItem:note.object];
    if (row != -1) {

        // force update the row that needs a re-draw
        [self.resultsOutlineView reloadDataForRowIndexes:[NSIndexSet indexSetWithIndex:row]
                             columnIndexes:[NSIndexSet indexSetWithIndex:0]];

        if ([self.resultsOutlineView isRowSelected:row]) {
            [self updatePathControl];
        }
    }
}

- (void)rowsDidChange:(NSNotification *)notification {
    // adjust the height constraint to our predicate editor's scroll view to accomodate any added or removed rows
    // we use the predicate editor's intrinsic size to help us.
    //
    NSSize intrinsicSize = self.predicateEditor.intrinsicContentSize;
    [self.self.heightConstraint animator].constant = intrinsicSize.height;
}


#pragma mark - NSOutlineViewDataSource

- (NSInteger)outlineView:(NSOutlineView *)outlineView numberOfChildrenOfItem:(id)item {

    NSArray *children = item == nil ? self.iSearchQueries : [item children];
    return children.count;
}

- (id)outlineView:(NSOutlineView *)outlineView child:(NSInteger)index ofItem:(id)item {

    NSArray *children = item == nil ? self.iSearchQueries : [item children];
    return children[index];
}

- (BOOL)outlineView:(NSOutlineView *)outlineView isItemExpandable:(id)item {

    if ([item isKindOfClass:[SearchQuery class]]) {
        return YES;
    }
    return NO;
}

// construct the table cell view for each row in our outline view
//
- (NSView *)outlineView:(NSOutlineView *)outlineView viewForTableColumn:(NSTableColumn *)tableColumn item:(id)item {

    NSTableCellView *result = nil;

    if ([self outlineView:outlineView isGroupItem:item] && [item isKindOfClass:[SearchQuery class]]) {

        // it's a grouped-style row, find it's view and set the title as the query title
        result = [outlineView makeViewWithIdentifier:VIEW_SEARCH_GROUP owner:self];
        SearchQuery *query = item;
        result.textField.stringValue = query.title;

    } else if (tableColumn != nil && item != nil) {

        result = [outlineView makeViewWithIdentifier:tableColumn.identifier owner:self];
        if (result != nil) {
            if (tableColumn == nil || [item isKindOfClass:[SearchQuery class]]) {
                SearchQuery *query = item;
                if ([tableColumn.identifier isEqualToString:COL_IMAGE_ID]) {
                    result.textField.stringValue = query.title;
                }
            } else if ([item isKindOfClass:[SearchItem class]]) {
                SearchItem *searchItem = (SearchItem *)item;

                if ([tableColumn.identifier isEqualToString:COL_IMAGE_ID]) {
                    if (searchItem.title != nil) {
                        result.textField.stringValue = searchItem.title;
                        result.imageView.image = searchItem.thumbnailImage;

                        NSTextField *subTitle = [result viewWithTag:SubTitle_Tag];
                        NSSize imageSize = [item imageSize];
                        if (imageSize.width > 0) {
                            subTitle.stringValue = [NSString stringWithFormat:@"(%ldx%ld)", (long)imageSize.width, (long)imageSize.height];
                        } else {
                            subTitle.stringValue = @"--";
                        }
                    }
                    else {
                        result.textField.stringValue = NSLocalizedString(@"(Untitled)", @"Untitled title");
                    }

                    // add a tracking area to the info button so we can alter it's image
                    NSButton *infoButton = [result viewWithTag:InfoButton_Tag];

                    NSDictionary *userInfo = @{Info_Button_Key: infoButton};

                    NSTrackingArea *trackingArea = [[NSTrackingArea alloc] initWithRect:infoButton.frame
                                                                                options:(NSTrackingEnabledDuringMouseDrag | NSTrackingMouseEnteredAndExited | NSTrackingActiveAlways)
                                                                                  owner:self
                                                                               userInfo:userInfo];
                    [result addTrackingArea:trackingArea];

                    infoButton.target = self;
                    infoButton.action = @selector(infoButtonAction:);

                } else if ([tableColumn.identifier isEqualToString:COL_CAMERA_MODEL_ID]) {
                    if (searchItem.cameraModel != nil)
                    {
                        result.textField.stringValue = searchItem.cameraModel;
                    }
                    else {
                        result.textField.stringValue = NSLocalizedString(@"(Unknown)", @"Unknown camera model name");
                    }
                } else if ([tableColumn.identifier isEqualToString:COL_LAST_MODIFIED_ID]) {
                    result.textField.stringValue = [self.dateFormatter stringFromDate:searchItem.modifiedDate];
                }
            }
        }
    }

    return result;
}


#pragma mark - NSOutlineViewDelegate

- (CGFloat)outlineView:(NSOutlineView *)outlineView heightOfRowByItem:(id)item {

    CGFloat rowHeight = outlineView.rowHeight;

    if ([item isKindOfClass:[SearchItem class]]) {
        SearchItem *searchItem = item;
        if (searchItem.metadataItem != nil) {
            // We could dynamically change the thumbnail size, if desired
            rowHeight = self.iThumbnailSize + 9.0; // The extra space is padding around the cell
        }
    }
    return rowHeight;
}

- (BOOL)outlineView:(NSOutlineView *)outlineView isGroupItem:(id)item {

    return [item isKindOfClass:[SearchQuery class]];
}

// used upon selection so we can set the info button's icon as selected
- (void)outlineViewSelectionDidChange:(NSNotification *)notification {

    [self updatePathControl];   // change the path control to reflect the current selection in the outline view

    // change the all the info button images to reflect the current selection in the outline view
    NSIndexSet *selectedRows = self.resultsOutlineView.selectedRowIndexes;
    if (selectedRows.count > 0) {
        for (NSUInteger rowIndex = selectedRows.firstIndex; rowIndex <= selectedRows.lastIndex; rowIndex = [selectedRows indexGreaterThanIndex:rowIndex]) {

            NSTableRowView *rowView = [self.resultsOutlineView rowViewAtRow:rowIndex makeIfNecessary:NO];
            if (rowView != nil) {
                NSButton *infoButton = [rowView viewWithTag:InfoButton_Tag];
                if (infoButton != nil) {
                    infoButton.image = [NSImage imageNamed:@"info-selected"];
                }
            }
        }
    }
}

// used upon de-selection so we can restore the info button's icon
- (NSIndexSet *)outlineView:(NSOutlineView *)outlineView selectionIndexesForProposedSelection:(NSIndexSet *)proposedSelectionIndexes {

    NSIndexSet *selectedRows = self.resultsOutlineView.selectedRowIndexes;
    if (selectedRows.count > 0) {
        for (NSUInteger rowIndex = selectedRows.firstIndex; rowIndex <= selectedRows.lastIndex; rowIndex = [selectedRows indexGreaterThanIndex:rowIndex]) {
            NSTableRowView *rowView = [self.resultsOutlineView rowViewAtRow:rowIndex makeIfNecessary:NO];
            if (rowView != nil) {
                NSButton *infoButton = [rowView viewWithTag:InfoButton_Tag];
                if (infoButton != nil) {
                    infoButton.image = [NSImage imageNamed:@"info-normal"];
                }
            }
        }
    }
    return proposedSelectionIndexes;
}


#pragma mark - Action Methods

- (void)updatePathControl {

    // Clear out the prior cells
    [self.pathControl setPathComponentCells:@[]];

    // Watch for the selection to change in order to update the path control
    NSIndexSet *selection = self.resultsOutlineView.selectedRowIndexes;
    if (selection.count == 0) {
        NSString *str = NSLocalizedString(@"Select an item to show its location.", @"Text to display in path control to select a location");
        ((NSFormCell *)self.pathControl.cell).placeholderString = str;
    } else if (selection.count == 1) {
        id selectedItem = [self.resultsOutlineView itemAtRow:selection.firstIndex];
        if ([selectedItem isKindOfClass:[SearchItem class]]) {
            SearchItem *searchItem = selectedItem;
            self.pathControl.URL = searchItem.filePathURL;
        } else {
            NSDictionary *attrs = @{NSForegroundColorAttributeName: [[NSColor blueColor] colorWithAlphaComponent:0.5],
                                    NSFontAttributeName: [NSFont systemFontOfSize:[NSFont systemFontSize]]};
            NSAttributedString *str = [[NSAttributedString alloc] initWithString:[selectedItem title] attributes:attrs];
            ((NSFormCell *)self.pathControl.cell).placeholderAttributedString = str;
        }
    } else {
        NSString *str = NSLocalizedString(@"Multiple items selected.", @"Text to display in path control when multiple items are selected");
        ((NSFormCell *)self.pathControl.cell).placeholderString = str;
    }
}

- (void)resultsOutlineDoubleClickAction:(NSOutlineView *)sender {

    // Open a page for all the selected items
    NSIndexSet *selectedRows = sender.selectedRowIndexes;

    if (selectedRows.count > 0) {
        for (NSUInteger i = selectedRows.firstIndex; i <= selectedRows.lastIndex; i = [selectedRows indexGreaterThanIndex:i]) {
            id item = [sender itemAtRow:i];
            if ([item isKindOfClass:[SearchItem class]]) {
                [[NSWorkspace sharedWorkspace] openURL:[item filePathURL]];
            }
        }
    }
}

- (void)infoButtonAction:(NSOutlineView *)sender {

    // Access the row that was clicked on and open that image
    NSInteger row = [self.resultsOutlineView rowForView:sender];
    if (row > 0) {
        id item = [self.resultsOutlineView itemAtRow:row];
        if ([item isKindOfClass:[SearchItem class]]) {
            if ([item filePathURL]) {
                NSPasteboard *pboard = [NSPasteboard pasteboardWithUniqueName];
                [pboard declareTypes:@[NSStringPboardType] owner:nil];
                [pboard setString:[item filePathURL].path forType:NSStringPboardType];
                NSPerformService(@"Finder/Show Info", pboard);
            }
        }
    }
}


#pragma mark - NSPathControl support

- (void)pathControlDoubleClick:(id)sender {

    if ([self.pathControl clickedPathComponentCell] != nil) {
        [[NSWorkspace sharedWorkspace] openURL:[self.pathControl clickedPathComponentCell].URL];
    }
}

- (IBAction)searchLocationChanged:(id)sender {

    self.searchLocation = [sender URL];

    // write out the NSURL as a security-scoped bookmark to NSUserDefaults
    // (so that we can resolve it again at re-launch)
    //
    NSData *bookmarkData = [self.searchLocation bookmarkDataWithOptions:NSURLBookmarkCreationWithSecurityScope
                                         includingResourceValuesForKeys:nil
                                                          relativeToURL:nil
                                                                  error:nil];
    [[NSUserDefaults standardUserDefaults] setObject:bookmarkData forKey:Search_Location_Key];
    [[NSUserDefaults standardUserDefaults] synchronize];
}

// delegate method to NSPathControl to determine how the NSOpenPanel will look/behavior
- (void)pathControl:(NSPathControl *)pathControl willDisplayOpenPanel:(NSOpenPanel *)openPanel {

    // customize the open panel to choose directories
    openPanel.allowsMultipleSelection = NO;
    openPanel.message = @"Choose a location to search for photos and images:";
    openPanel.canChooseDirectories = YES;
    openPanel.canChooseFiles = NO;
    openPanel.prompt = @"Choose";
    openPanel.title = @"Choose Location";

    // set the default location to the Documents folder
    NSArray *documentsFolderPath = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    openPanel.directoryURL = [NSURL fileURLWithPath:documentsFolderPath[0]];
}


#pragma mark - Mouse tracking support

- (void)mouseEntered:(NSEvent *)theEvent {

    // alter the button image to the hovered representation
    NSDictionary *userInfo = theEvent.userData;
    NSButton *button = [userInfo valueForKey:Info_Button_Key];

    // decide which image to use for entering the tracking area
    NSPoint viewLocation = [self.resultsOutlineView convertPoint:theEvent.locationInWindow fromView:nil];
    NSInteger rowAtPoint = [self.resultsOutlineView rowAtPoint:viewLocation];
    if ([self.resultsOutlineView isRowSelected:rowAtPoint]) {
        button.image = [NSImage imageNamed:@"info-selected-hovered"];
    } else {
        button.image = [NSImage imageNamed:@"info-normal-hovered"];
    }
}

- (void)mouseExited:(NSEvent *)theEvent {

    // reset the button image to normal representation
    NSDictionary *userInfo = theEvent.userData;
    NSButton *button = [userInfo valueForKey:Info_Button_Key];

    // decide which image to use for entering the tracking area
    NSPoint viewLocation = [self.resultsOutlineView convertPoint:theEvent.locationInWindow fromView:nil];
    NSInteger rowAtPoint = [self.resultsOutlineView rowAtPoint:viewLocation];
    if ([self.resultsOutlineView isRowSelected:rowAtPoint]) {
        button.image = [NSImage imageNamed:@"info-selected"];
    } else {
        button.image = [NSImage imageNamed:@"info-normal"];
    }
}

@end
```

[Next](CaseInsensitivePredicateTemplate.m.md)[Previous](MainWindowController.h.md)

