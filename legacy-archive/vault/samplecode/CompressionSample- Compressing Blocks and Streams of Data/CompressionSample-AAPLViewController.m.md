---
title: 'CompressionSample: Compressing Blocks and Streams of Data'
apple_id: TP40016182
resource_type: Sample Code
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CompressionSample/Listings/CompressionSample_AAPLViewController_m.html
archived_at: '2026-07-18T03:04:11.954242Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CompressionSample: Compressing Blocks and Streams of Data](CompressionSample-%20Compressing%20Blocks%20and%20Streams%20of%20Data.md)


[Next](README.md.md)[Previous](CompressionSample-StreamCompression.h.md)

# CompressionSample/AAPLViewController.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides a user interface for exercising the compression code.
*/

#import "AAPLViewController.h"
#import "BlockCompression.h"
#import "StreamCompression.h"

typedef enum {
    blockCompression = 0,
    streamCompression = 1,
} technique;

@interface AAPLViewController ()
{
    compression_algorithm algorithm;
    NSString* inFileName;
    NSString* outFileName;
    FILE* dataIn;
    FILE* dataOut;
}

@property(weak) IBOutlet  NSTextField*  messageLabel;
@property(weak) IBOutlet  NSMatrix*     techniqueButtons;
@property(weak) IBOutlet  NSMatrix*     algorithmButtons;
@property(weak) IBOutlet  NSButtonCell* LZ4button;
@property(weak) IBOutlet  NSButtonCell* LZMAbutton;
@property(weak) IBOutlet  NSButtonCell* ZLIBbutton;
@property(weak) IBOutlet  NSButtonCell* LZFSEbutton;
@property(weak) IBOutlet  NSButton*     compressButton;

@end

@implementation AAPLViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    algorithm = COMPRESSION_LZ4;
}

- (void)viewWillAppear
{
    [super viewWillAppear];
    [self resetUI];
}

- (void)resetUI
{
    [self queueUIBusiness:^{
        self.techniqueButtons.enabled = YES;
        self.algorithmButtons.enabled = YES;
        self.compressButton.enabled = YES;
    }];
}

- (void)openSourceFile:(NSURL*)url
{
    inFileName = [url lastPathComponent];

    // Open the file.
    char* path = (char*)malloc(512);
    if ([url.path getCString:path maxLength:512 encoding:NSUTF8StringEncoding]) {
        dataIn = fopen(path, "rb");
    }

    if (dataIn == NULL) {
        NSAlert* openFailedAlert = [[NSAlert alloc] init];
        openFailedAlert.messageText = [NSString stringWithFormat:@"Could not open file %@", inFileName];
        [openFailedAlert addButtonWithTitle:@"OK"];
        [openFailedAlert beginSheetModalForWindow:self.view.window completionHandler:^(NSModalResponse returnCode) {
            [self queueUIBusiness:^{
                [self resetUI];
            }];
        }];
    }
}

- (void)openDestinationFile:(NSURL*)url
{
    if (dataIn == NULL) { return; }

    outFileName = [url lastPathComponent];
    self.messageLabel.stringValue = [NSString stringWithFormat:@"Compressing file %@ with algorithm %@.\nWriting to file %@.", inFileName, self.algorithmName, outFileName];

    // Open the file.
    char* path = (char*)malloc(512);
    if ([url.path getCString:path maxLength:512 encoding:NSUTF8StringEncoding]) {
        dataOut = fopen(path, "wb");
        if (dataOut != NULL) {
            float compression_ratio;

            switch (self.techniqueButtons.selectedRow) {
                case blockCompression:
                    compression_ratio = doBlockCompression(dataIn, dataOut, algorithm);
                    break;

                case streamCompression:
                    compression_ratio = doStreamCompression(dataIn, dataOut, algorithm, COMPRESSION_STREAM_ENCODE);
                    break;

                default:
                    compression_ratio = 0;
                    break;
            }

            if (compression_ratio > 1.0) {
                switch (self.techniqueButtons.selectedRow) {
                    case blockCompression:
                        self.messageLabel.stringValue = [NSString stringWithFormat:@"Compressed and encrypted file %@ with algorithm %@.\nWrote to file %@.\nCompression Ratio = %.2f.", inFileName, self.algorithmName, outFileName, compression_ratio];
                        break;

                    case streamCompression:
                        self.messageLabel.stringValue = [NSString stringWithFormat:@"Compressed file %@ with algorithm %@.\nWrote to file %@.\nCompression Ratio = %.2f.", inFileName, self.algorithmName, outFileName, compression_ratio];
                        break;
                }
            }
            else {
                self.messageLabel.stringValue = @"Compression failed.";
            }
        }
    }

    if (dataOut == NULL) {
        NSAlert* openFailedAlert = [[NSAlert alloc] init];
        openFailedAlert.messageText = [NSString stringWithFormat:@"Could not open file %@", inFileName];
        [openFailedAlert addButtonWithTitle:@"OK"];
        [openFailedAlert beginSheetModalForWindow:self.view.window completionHandler:^(NSModalResponse returnCode) {
            [self queueUIBusiness:^{
                [self resetUI];
            }];
        }];
    }

    [self queueUIBusiness:^{
        [self resetUI];
    }];
}

- (void)getSourceFileSelection
{
    NSOpenPanel* openPanel = [NSOpenPanel openPanel];
    openPanel.message = @"Please select a file to compress.";
    openPanel.prompt = @"Select";
    openPanel.canChooseFiles = YES;
    openPanel.canChooseDirectories = NO;
    openPanel.canCreateDirectories = NO;
    openPanel.resolvesAliases = YES;
    openPanel.allowsMultipleSelection = NO;

    [self queueUIBusiness:^{
        [openPanel beginSheetModalForWindow:self.view.window completionHandler:^(NSInteger result) {
            switch(result) {
                case NSFileHandlingPanelOKButton:
                    [self openSourceFile:openPanel.URLs[0]];
                    [self getDestinationFileSelection];
                    break;
                case NSFileHandlingPanelCancelButton:
                    [self resetUI];
                    break;
                default:
                    break;
            }
        }];
    }];
}

- (void)getDestinationFileSelection
{
    NSSavePanel* savePanel = [NSSavePanel savePanel];
    savePanel.message = @"Please specify a file to hold the compressed data.";
    savePanel.prompt = @"Write";
    savePanel.canCreateDirectories = YES;
    savePanel.nameFieldLabel = @"Filename:";
    savePanel.showsTagField = NO;

    // Suggest a filename.
    NSString *pathExtension = [[self algorithmName] lowercaseString];
    NSString *filename = [inFileName lastPathComponent];
    filename = [filename stringByDeletingPathExtension];
    filename = [filename stringByAppendingPathExtension:pathExtension];
    savePanel.nameFieldStringValue = filename;

    [self queueUIBusiness:^{
        [savePanel beginSheetModalForWindow:self.view.window completionHandler:^(NSInteger result) {
            switch (result) {
                case NSFileHandlingPanelOKButton:
                    self.techniqueButtons.enabled = NO;
                    self.algorithmButtons.enabled = NO;
                    self.compressButton.enabled = NO;
                    [self openDestinationFile:savePanel.URL];
                    break;
                case NSFileHandlingPanelCancelButton:
                    [self resetUI];
                    break;
                default:
                    break;
            }
        }];
    }];
}

- (void)queueUIBusiness:(void (^)())block
{
    dispatch_async(dispatch_get_main_queue(), block);
}

- (NSString*)algorithmName
{
    switch (algorithm) {
        case COMPRESSION_LZ4:
            return @"LZ4";
            break;
        case COMPRESSION_LZMA:
            return @"LZMA";
            break;
        case COMPRESSION_ZLIB:
            return @"ZLIB";
            break;
        case COMPRESSION_LZFSE:
            return @"LZFSE";
            break;

        default:
            return @"";
            break;
    }
}

- (IBAction)setLZ4:(id)sender
{
    algorithm = COMPRESSION_LZ4;
}

- (IBAction)setLZMA:(id)sender
{
    algorithm = COMPRESSION_LZMA;
}

- (IBAction)setZLIB:(id)sender
{
    algorithm = COMPRESSION_ZLIB;
}

- (IBAction)setLZFSE:(id)sender
{
    algorithm = COMPRESSION_LZFSE;
}

- (IBAction)compress:(id)sender
{
    [self getSourceFileSelection];
}

@end
```

[Next](README.md.md)[Previous](CompressionSample-StreamCompression.h.md)

