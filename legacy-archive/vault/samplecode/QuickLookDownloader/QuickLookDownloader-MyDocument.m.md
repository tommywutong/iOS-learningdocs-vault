---
title: QuickLookDownloader
apple_id: DTS40009082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: QuickLook
published: '2017-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/QuickLookDownloader/Listings/QuickLookDownloader_MyDocument_m.html
archived_at: '2026-07-18T03:21:43.824961Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickLookDownloader](QuickLookDownloader.md)


[Next](QuickLookDownloader-DownloadItem.m.md)[Previous](QuickLookDownloader-DownloadsTableView.h.md)

# QuickLookDownloader/MyDocument.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 MyDocument manages a list of downloaded items.
 */

#import "MyDocument.h"
#import "DownloadItem.h"
#import "DownloadCell.h"

@import Quartz;   // Quartz framework provides the QLPreviewPanel public API

// DownloadItem will be used directlty as the items in preview panel
// The class just need to implement the QLPreviewItem protocol
//
@interface DownloadItem (QLPreviewItem) <QLPreviewItem>

@end


#pragma mark -

@implementation DownloadItem (QLPreviewItem)

- (NSURL *)previewItemURL
{
    return self.resolvedFileURL;
}

- (NSString *)previewItemTitle
{
    return [self.originalURL absoluteString];
}

@end


#pragma mark -

@interface MyDocument () <QLPreviewPanelDataSource, QLPreviewPanelDelegate, NSURLDownloadDelegate, NSTextFieldDelegate>
{
    BOOL downloading;
}

@property (strong) NSMutableArray *downloads;
@property (strong) NSURLDownload *download;
@property (assign) long long downloadedSoFar;
@property (assign) long long expectedContentLength;

@property (strong) NSURL *originalURL;
@property (strong) NSURL *targetFileURL;

@property (getter = isDownloading, setter = setDownloading:) BOOL downloading;
@property CGFloat downloadProgress;
@property BOOL downloadIsIndeterminate;
@property (nonatomic, copy) NSArray *selectedDownloads;
@property (nonatomic, copy) NSIndexSet *selectedIndexes;

@property IBOutlet NSTextField *downloadURLField;
@property IBOutlet NSView *downloadsView;
@property IBOutlet NSTableView *downloadsTableView;
@property IBOutlet NSButton *downloadButton;
@property IBOutlet NSView *downloadProgressView;

@property (strong) QLPreviewPanel *previewPanel;

@end


#pragma mark -

@implementation MyDocument

- (id)init
{
    self = [super init];
    if (self != nil)
    {
        _downloads = [[NSMutableArray alloc] init];
        _selectedIndexes = [[NSIndexSet alloc] init];
    }
    return self;
}

- (void)dealloc
{
    [self.download cancel];
}

- (NSString *)windowNibName
{
    return @"MyDocument";
}

// write method of NSDocument
//
- (NSData *)dataOfType:(NSString *)typeName error:(NSError **)outError
{
    NSMutableArray *propertyList = [[NSMutableArray alloc] initWithCapacity:self.downloads.count];

    for (DownloadItem *item in self.downloads)
    {
        id plistForItem = [item propertyListForSaving];
        if (plistForItem)
        {
            [propertyList addObject:plistForItem];
        }
    }

    NSData *result = [NSPropertyListSerialization dataWithPropertyList:propertyList
                                                                format:NSPropertyListBinaryFormat_v1_0
                                                               options:0
                                                                 error:NULL];
    assert(result);

    return result;
}

// read method of NSDocument
//
- (BOOL)readFromData:(NSData *)data ofType:(NSString *)typeName error:(NSError **)outError
{
    NSArray *propertyList = [NSPropertyListSerialization propertyListWithData:data
                                                                      options:NSPropertyListImmutable
                                                                       format:NULL
                                                                        error:outError];
    if (!propertyList)
    {
        return NO;
    }

    if (![propertyList isKindOfClass:[NSArray class]])
    {
        if (outError != NULL)
        {
            *outError = [NSError errorWithDomain:NSCocoaErrorDomain
                                            code:NSFileReadCorruptFileError
                                        userInfo:NULL];
        }
        return NO;
    }

    NSMutableArray *observableDownloads = [self mutableArrayValueForKey:@"downloads"];
    [observableDownloads removeAllObjects];

    for (id plistItem in propertyList)
    {
        DownloadItem *item = [[DownloadItem alloc] initWithSavedPropertyList:plistItem];
        if (item)
        {
            [observableDownloads addObject:item];
        }
    }

    return YES;
}


#pragma mark - Downloading

// the URL field text has changed, update the enable state of our Download button
- (void)controlTextDidChange:(NSNotification *)obj
{
    NSTextField *textField = [obj object];
    [self.downloadButton setEnabled:(textField.stringValue.length > 0)];
}

// called when the user clicks the Download button
- (IBAction)startDownload:(id)sender
{
    assert(!self.download);

    [self.downloadButton setEnabled:NO]; // don't allow download button to work while downloading

    NSString *urlString = [self.downloadURLField stringValue];
    assert(urlString);

    urlString = [urlString stringByTrimmingCharactersInSet:[NSCharacterSet whitespaceAndNewlineCharacterSet]];

    NSURL *url = [NSURL URLWithString:urlString];
    _originalURL = [url copy];

    NSURLRequest *request = [NSURLRequest requestWithURL:url];

    self.downloadIsIndeterminate = YES;
    self.downloadProgress = 0.0f;
    self.downloading = YES;

    _download = [[NSURLDownload alloc] initWithRequest:request delegate:self];

    [[self.downloadsTableView window] makeFirstResponder:self.downloadsTableView];
}

- (void)setSelectedIndexes:(NSIndexSet *)indexSet
{
    if (indexSet != _selectedIndexes)
    {
        indexSet = [indexSet copy];
        _selectedIndexes = indexSet;
        self.selectedDownloads = [self.downloads objectsAtIndexes:indexSet];
    }
}

- (void)setSelectedDownloads:(NSArray *)array
{
    if (array != _selectedDownloads)
    {
        array = [array copy];
        _selectedDownloads = array;
        [self.previewPanel reloadData];
    }
}


#pragma mark - Download support

- (void)displayDownloadProgressView
{
    if (self.downloading && self.downloadProgressView.superview == nil)
    {
        // position and size downloadsProgressFrame appropriately
        NSRect downloadProgressFrame = self.downloadProgressView.frame;
        NSRect downloadsFrame = self.downloadsView.frame;
        downloadProgressFrame.size.width = CGRectGetWidth(downloadsFrame);
        downloadProgressFrame.origin.y = NSMaxY(downloadsFrame);
        [self.downloadProgressView setFrame:downloadProgressFrame];

        [[[self.downloadsView superview] animator] addSubview:self.downloadProgressView
                                                   positioned:NSWindowBelow
                                                   relativeTo:self.downloadsView];
    }
}

- (void)startDisplayingProgressView
{
    if (!self.downloading || [self.downloadProgressView superview])
    {
        return;
    }

    // we are starting a download, display the download progress view
    NSRect downloadProgressFrame = self.downloadProgressView.frame;
    NSRect downloadsFrame = self.downloadsView.frame;

    // reduce the size of the downloads view
    downloadsFrame.size.height -= CGRectGetHeight(downloadProgressFrame);

    [NSAnimationContext beginGrouping];

        [[NSAnimationContext currentContext] setDuration:0.2];
        [[self.downloadsView animator] setFrame:downloadsFrame];

    [NSAnimationContext endGrouping];

    [self performSelector:@selector(displayDownloadProgressView) withObject:nil afterDelay:0.2];
}

- (void)hideDownloadProgressView
{
    if (!self.downloading)
    {
        [NSObject cancelPreviousPerformRequestsWithTarget:self
                                                 selector:@selector(displayDownloadProgressView)
                                                   object:nil];

        // we are ending a download, remove the download progress view
        [self.downloadProgressView removeFromSuperview];

        [NSAnimationContext beginGrouping];

            [[NSAnimationContext currentContext] setDuration:0.5];
            [[self.downloadsView animator] setFrame:[[self.downloadsView superview] bounds]];

        [NSAnimationContext endGrouping];
    }
}

- (BOOL)isDownloading
{
    return downloading;
}

- (void)setDownloading:(BOOL)flag
{
    if (!flag != !downloading)
    {
        downloading = flag;

        if (downloading)
        {
            [self performSelector:@selector(startDisplayingProgressView) withObject:nil afterDelay:0.0];
        }
        else
        {
            [self performSelector:@selector(hideDownloadProgressView) withObject:nil afterDelay:0.1];
            _originalURL = nil;
            _targetFileURL = nil;
            _download = nil;
        }
    }
}

- (void)download:(NSURLDownload *)download didReceiveResponse:(NSURLResponse *)response
{
    _expectedContentLength = [response expectedContentLength];
    if (self.expectedContentLength > 0.0)
    {
        self.downloadIsIndeterminate = NO;
        _downloadedSoFar = 0;
    }
}

- (void)download:(NSURLDownload *)download didReceiveDataOfLength:(NSUInteger)length
{
    _downloadedSoFar += length;
    if (self.downloadedSoFar >= self.expectedContentLength)
    {
        // the expected content length was wrong as we downloaded more than expected
        // make the progress indeterminate
        //
        self.downloadIsIndeterminate = YES;
    }
    else
    {
        self.downloadProgress = (float)self.downloadedSoFar / (float)self.expectedContentLength;
    }
}

- (void)download:(NSURLDownload *)aDownload decideDestinationWithSuggestedFilename:(NSString *)filename
{
    // find the user's Downloads folder
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDownloadsDirectory, NSUserDomainMask, YES);
    NSString *documentsDirectory = paths[0];
    NSString *downloadPath = [documentsDirectory stringByAppendingPathComponent:filename];

    [aDownload setDestination:downloadPath allowOverwrite:NO];
}

- (void)download:(NSURLDownload *)download didCreateDestination:(NSString *)path
{
    _targetFileURL = [[NSURL alloc] initFileURLWithPath:path];
}

- (void)downloadDidFinish:(NSURLDownload *)download
{
    if (self.originalURL && self.targetFileURL)
    {
        DownloadItem *item = [[DownloadItem alloc] initWithOriginalURL:self.originalURL fileURL:self.targetFileURL];
        if (item != nil)
        {
            [[self mutableArrayValueForKey:@"downloads"] addObject:item];
            [self updateChangeCount:NSChangeDone];
        }
        else
        {
            NSLog(@"Can't create download item at %@", self.targetFileURL);
        }
    }

    self.downloading = NO;

    [self.downloadButton setEnabled:YES];    // allow for downloads again
}

- (void)download:(NSURLDownload *)aDownload didFailWithError:(NSError *)error
{
    [self presentError:error modalForWindow:[self windowForSheet] delegate:nil didPresentSelector:NULL contextInfo:NULL];
    self.downloading = NO;
}


#pragma mark - NSTableViewDelegate

- (void)tableView:(NSTableView *)tableView willDisplayCell:(id)cell forTableColumn:(NSTableColumn *)tableColumn row:(NSInteger)row
{
    if ([[tableColumn identifier] isEqual:@"Filename"])
    {
        ((DownloadCell *)cell).originalURL = ((DownloadItem *)self.downloads[row]).originalURL;
        [cell setFont:[NSFont systemFontOfSize:TEXT_SIZE]];
    }
}


#pragma mark - Quick Look panel support

- (BOOL)acceptsPreviewPanelControl:(QLPreviewPanel *)panel
{
    return YES;
}

- (void)beginPreviewPanelControl:(QLPreviewPanel *)panel
{
    // This document is now responsible of the preview panel
    // It is allowed to set the delegate, data source and refresh panel.
    //
    _previewPanel = panel;
    panel.delegate = self;
    panel.dataSource = self;
}

- (void)endPreviewPanelControl:(QLPreviewPanel *)panel
{
    // This document loses its responsisibility on the preview panel
    // Until the next call to -beginPreviewPanelControl: it must not
    // change the panel's delegate, data source or refresh it.
    //
    _previewPanel = nil;
}


#pragma mark - QLPreviewPanelDataSource

- (NSInteger)numberOfPreviewItemsInPreviewPanel:(QLPreviewPanel *)panel
{
    return self.selectedDownloads.count;
}

- (id <QLPreviewItem>)previewPanel:(QLPreviewPanel *)panel previewItemAtIndex:(NSInteger)index
{
    return (self.selectedDownloads)[index];
}


#pragma mark - QLPreviewPanelDelegate

- (BOOL)previewPanel:(QLPreviewPanel *)panel handleEvent:(NSEvent *)event
{
    // redirect all key down events to the table view
    if ([event type] == NSKeyDown)
    {
        [self.downloadsTableView keyDown:event];
        return YES;
    }
    return NO;
}

// This delegate method provides the rect on screen from which the panel will zoom.
- (NSRect)previewPanel:(QLPreviewPanel *)panel sourceFrameOnScreenForPreviewItem:(id <QLPreviewItem>)item
{
    NSRect returnIconRect = NSZeroRect;
    NSInteger index = [self.downloads indexOfObject:item];
    if (index != NSNotFound)
    {
        NSRect iconRect = [self.downloadsTableView frameOfCellAtColumn:0 row:index];

        // Check that the icon rect is visible on screen.
        NSRect visibleRect = [self.downloadsTableView visibleRect];

        if (NSIntersectsRect(visibleRect, iconRect))
        {
            // Convert icon rect to screen coordinates.
            NSRect convertedRect = [self.downloadsTableView convertRect:iconRect toView:nil];
            convertedRect.origin = [self.downloadsTableView.window convertRectToScreen:convertedRect].origin;
            returnIconRect = convertedRect;
        }
    }
    return returnIconRect;
}

// this delegate method provides a transition image between the table view and the preview panel
//
- (id)previewPanel:(QLPreviewPanel *)panel transitionImageForPreviewItem:(id <QLPreviewItem>)item contentRect:(NSRect *)contentRect
{
    DownloadItem *downloadItem = (DownloadItem *)item;

    return downloadItem.iconImage;
}

@end
```

[Next](QuickLookDownloader-DownloadItem.m.md)[Previous](QuickLookDownloader-DownloadsTableView.h.md)

