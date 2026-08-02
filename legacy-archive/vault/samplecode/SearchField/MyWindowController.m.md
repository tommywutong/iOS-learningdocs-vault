---
title: SearchField
apple_id: DTS10004112
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-06-25'
source_url: https://developer.apple.com/library/archive/samplecode/SearchField/Listings/MyWindowController_m.html
archived_at: '2026-07-18T03:23:37.044906Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SearchField](SearchField.md)


[Next](Document%20Revision%20History.md)[Previous](LICENSE.txt.md)

# MyWindowController.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Sample's main NSWindowController
 */

#import "MyWindowController.h"

@interface MyWindowController ()

@property IBOutlet NSWindow *simpleSheet;
@property (weak) IBOutlet NSSearchField *searchField;

@property (nonatomic) NSMutableArray *allKeywords;
@property NSMutableArray *builtInKeywords;

@property BOOL completePosting;
@property BOOL commandHandling;

@end


#pragma mark -

@implementation MyWindowController

// -------------------------------------------------------------------------------
//  awakeFromNib
// -------------------------------------------------------------------------------
- (void)awakeFromNib
{
    // add the searchMenu to this control, allowing recent searches to be added.
    //
    // note that we could build this menu inside our nib, but for clarity we're
    // building the menu in code to illustrate the use of tags:
    //      NSSearchFieldRecentsTitleMenuItemTag, NSSearchFieldNoRecentsMenuItemTag, etc.
    //
    if ([self.searchField respondsToSelector:@selector(setRecentSearches:)])
    {
        NSMenu *searchMenu = [[NSMenu alloc] initWithTitle:@"Search Menu"];
        [searchMenu setAutoenablesItems:YES];

        // first add our custom menu item (Important note: "action" MUST be valid or the menu item is disabled)
        NSMenuItem *item = [[NSMenuItem alloc] initWithTitle:@"Custom" action:@selector(actionMenuItem:) keyEquivalent:@""];
        [item setTarget: self];
        [searchMenu insertItem:item atIndex:0];

        // add our own separator to keep our custom menu separate
        NSMenuItem *separator =  [NSMenuItem separatorItem];
        [searchMenu insertItem:separator atIndex:1];

        NSMenuItem *recentsTitleItem = [[NSMenuItem alloc] initWithTitle:@"Recent Searches" action:nil keyEquivalent:@""];
        // tag this menu item so NSSearchField can use it and respond to it appropriately
        [recentsTitleItem setTag:NSSearchFieldRecentsTitleMenuItemTag];
        [searchMenu insertItem:recentsTitleItem atIndex:2];

        NSMenuItem *norecentsTitleItem = [[NSMenuItem alloc] initWithTitle:@"No recent searches" action:nil keyEquivalent:@""];
        // tag this menu item so NSSearchField can use it and respond to it appropriately
        [norecentsTitleItem setTag:NSSearchFieldNoRecentsMenuItemTag];
        [searchMenu insertItem:norecentsTitleItem atIndex:3];

        NSMenuItem *recentsItem = [[NSMenuItem alloc] initWithTitle:@"Recents" action:nil keyEquivalent:@""];
        // tag this menu item so NSSearchField can use it and respond to it appropriately
        [recentsItem setTag:NSSearchFieldRecentsMenuItemTag];   
        [searchMenu insertItem:recentsItem atIndex:4];

        NSMenuItem *separatorItem = (NSMenuItem*)[NSMenuItem separatorItem];
        // tag this menu item so NSSearchField can use it, by hiding/show it appropriately:
        [separatorItem setTag:NSSearchFieldRecentsTitleMenuItemTag];
        [searchMenu insertItem:separatorItem atIndex:5];

        NSMenuItem *clearItem = [[NSMenuItem alloc] initWithTitle:@"Clear" action:nil keyEquivalent:@""];
        [clearItem setTag:NSSearchFieldClearRecentsMenuItemTag];    // tag this menu item so NSSearchField can use it
        [searchMenu insertItem:clearItem atIndex:6];

        id searchCell = [self.searchField cell];
        [searchCell setMaximumRecents:20];
        [searchCell setSearchMenuTemplate:searchMenu];
    }

    // build the list of keyword strings for our type completion dropdown list in NSSearchField
    _builtInKeywords = [[NSMutableArray alloc] initWithObjects:
                    @"Favorite", @"Favorite1", @"Favorite11", @"Favorite3", @"Vacations1", @"Vacations2",
                    @"Hawaii", @"Family", @"Important", @"Important2", @"Personal", nil];
}

// -------------------------------------------------------------------------------
//  applicationShouldTerminateAfterLastWindowClosed:
//
//  NSApplication delegate method placed here so the sample conveniently quits
//  after we close the window.
// -------------------------------------------------------------------------------
- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender
{
    return YES;
}


#pragma mark - Custom sheet

// -------------------------------------------------------------------------------
//  sheetDidEnd:sheet:returnCode:returnCode:contextInfo:
// -------------------------------------------------------------------------------
- (void)sheetDidEnd:(NSWindow *)sheet returnCode:(int)returnCode contextInfo:(void *)contextInfo
{
    [sheet orderOut:self];
}

// -------------------------------------------------------------------------------
//  sheetDoneButtonAction:sender
// -------------------------------------------------------------------------------
- (IBAction)sheetDoneButtonAction:(id)sender
{
    [NSApp endSheet:self.simpleSheet];
}

// -------------------------------------------------------------------------------
//  actionMenuItem:sender
// -------------------------------------------------------------------------------
- (IBAction)actionMenuItem:(id)sender
{
    [NSApp beginSheet:self.simpleSheet modalForWindow:[self window] modalDelegate:self
                didEndSelector:@selector(sheetDidEnd:returnCode:contextInfo:) contextInfo:nil];
}


#pragma mark - Keyword search handling

// -------------------------------------------------------------------------------
//  allKeywords
// -------------------------------------------------------------------------------
- (NSArray *)allKeywords
{
    if (_allKeywords == nil)
    {
        _allKeywords = [self.builtInKeywords mutableCopy];

        [_allKeywords sortUsingComparator:^(NSString *a, NSString *b) {
            return [a localizedStandardCompare:b];
        }];
    }

    return _allKeywords;
}

// -------------------------------------------------------------------------------
//  control:textView:completions:forPartialWordRange:indexOfSelectedItem:
//
//  Use this method to override NSFieldEditor's default matches (which is a much bigger
//  list of keywords).  By not implementing this method, you will then get back
//  NSSearchField's default feature.
// -------------------------------------------------------------------------------
- (NSArray *)control:(NSControl *)control textView:(NSTextView *)textView completions:(NSArray *)words forPartialWordRange:(NSRange)charRange indexOfSelectedItem:(NSInteger *)index
{
    NSMutableArray *matches = [[NSMutableArray alloc] init];
    NSString *partialString  = [textView.string substringWithRange:charRange];

    NSUInteger rangeOptions = NSAnchoredSearch | NSCaseInsensitiveSearch;

    [self.allKeywords enumerateObjectsUsingBlock:^(NSString *keyword, NSUInteger idx, BOOL *stop) {

        NSRange searchRange = NSMakeRange(0, keyword.length);
        NSRange foundRange = [keyword rangeOfString:partialString options:rangeOptions range:searchRange];

        BOOL partialStringIsMatchForKeyword = YES;
        if (foundRange.location == NSNotFound)
        {
            partialStringIsMatchForKeyword = NO;
        }

        if (partialStringIsMatchForKeyword)
        {
            [matches addObject:keyword];
        }
    }];

    [matches sortUsingComparator:^(NSString *a, NSString *b) {
        return [a localizedStandardCompare:b];
    }];

    return matches;
}

// -------------------------------------------------------------------------------
//  controlTextDidChange:notification:
//
//  The text in NSSearchField has changed, try to attempt type completion.
// -------------------------------------------------------------------------------
- (void)controlTextDidChange:(NSNotification *)notification
{
    NSTextView *textView = notification.userInfo[@"NSFieldEditor"];

    // prevent calling "complete" too often
    if (!self.completePosting && !self.commandHandling)
    {
        _completePosting = YES;
        [textView complete:nil];
        _completePosting = NO;
    }
}

// -------------------------------------------------------------------------------
//  control:textView:commandSelector
//
//  Handle all commend selectors that we can handle here
// -------------------------------------------------------------------------------
- (BOOL)control:(NSControl *)control textView:(NSTextView *)textView doCommandBySelector:(SEL)commandSelector
{
    BOOL didPerformRequestedSelectorOnTextView = NO;

    if ([textView respondsToSelector:commandSelector])
    {
        _commandHandling = YES;

        NSMethodSignature *textViewSelectorMethodSignature = [textView methodSignatureForSelector:commandSelector];

        NSInvocation *textViewInvocationForSelector = [NSInvocation invocationWithMethodSignature:textViewSelectorMethodSignature];

        [textViewInvocationForSelector setTarget:textView];
        [textViewInvocationForSelector setSelector:commandSelector];
        [textViewInvocationForSelector invoke];
        _commandHandling = NO;

        didPerformRequestedSelectorOnTextView = YES;
    }

    return didPerformRequestedSelectorOnTextView;
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](LICENSE.txt.md)

