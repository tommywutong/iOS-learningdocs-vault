---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_MyDocument_m.html
archived_at: '2026-07-18T03:13:31.718321Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-ClickTracker.m.md)[Previous](LightTable-DragTracker.m.md)

# LightTable/MyDocument.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This is a basic Core Data based document subclass. This subclass overrides -makeWindowControllers to instantiate the window from the storyboard.
 */

#import "MyDocument.h"
#import "LTWindowController.h"


@implementation MyDocument

- (instancetype)init {
    self = [super init];
    if (self) {
        // Add your subclass-specific initialization here.
    }
    return self;
}

- (void)makeWindowControllers {
    // Create the window controller.
    LTWindowController *windowController = [[NSStoryboard storyboardWithName:@"Storyboard" bundle:nil] instantiateControllerWithIdentifier:@"documentWindowController"];
    // Make it part of the document.
    [self addWindowController:windowController];

    // Get a reference to the view controller.
    NSViewController *viewController = windowController.contentViewController;
    // And set its represented object to the MOC that is the data model.
    viewController.representedObject = self.managedObjectContext;

}

- (void)windowControllerDidLoadNib:(NSWindowController *) aController
{
    [super windowControllerDidLoadNib:aController];
    // Add any code here that needs to be executed once the windowController has loaded the document's window.
}

- (NSData *)dataOfType:(NSString *)typeName error:(NSError **)outError {
    // Insert code here to write your document to data of the specified type. If outError != NULL, ensure that you create and set an appropriate error when returning nil.
    // You can also choose to override -fileWrapperOfType:error:, -writeToURL:ofType:error:, or -writeToURL:ofType:forSaveOperation:originalContentsURL:error: instead.
    [NSException raise:@"UnimplementedMethod" format:@"%@ is unimplemented", NSStringFromSelector(_cmd)];
    return nil;
}


- (BOOL)readFromData:(NSData *)data ofType:(NSString *)typeName error:(NSError **)outError {
    // Insert code here to read your document from the given data of the specified type. If outError != NULL, ensure that you create and set an appropriate error when returning NO.
    // You can also choose to override -readFromFileWrapper:ofType:error: or -readFromURL:ofType:error: instead.
    // If you override either of these, you should also override -isEntireFileLoaded to return NO if the contents are lazily loaded.
    [NSException raise:@"UnimplementedMethod" format:@"%@ is unimplemented", NSStringFromSelector(_cmd)];
    return YES;
}

- (NSError *)willPresentError:(NSError *)error {

    // Only deal with Core Data Errors
    if (!([[error domain] isEqualToString:NSCocoaErrorDomain])) {
        return error;
    }
    NSInteger errorCode = [error code];
    if ((errorCode < NSValidationErrorMinimum) || (errorCode > NSValidationErrorMaximum)) {
        return error;
    }

    // If there is only 1 error, let the usual alert display it
    if (errorCode != NSValidationMultipleErrorsError) {
        return error;
    }

    // Get the errors. NSValidationMultipleErrorsError - the errors are in an array in the userInfo dictionary for key NSDetailedErrorsKey
    NSArray *detailedErrors = [[error userInfo] objectForKey:NSDetailedErrorsKey];
    NSUInteger errorCount = [detailedErrors count];
    NSMutableString *errorString = [NSMutableString stringWithFormat:@"There are %lu validation errors:-", errorCount];
    for (int i = 0; i < errorCount; i++) {
        [errorString appendFormat:@"%@\n",
         [[detailedErrors objectAtIndex:i] localizedDescription]];
    }

    // Create a new error with the new userInfo and return it
    NSMutableDictionary *newUserInfo = [NSMutableDictionary dictionaryWithDictionary:[error userInfo]];
    [newUserInfo setObject:errorString forKey:NSLocalizedDescriptionKey];
    NSError *newError = [NSError errorWithDomain:[error domain] code:[error code] userInfo:newUserInfo];
    return newError;
}

@end
```

[Next](LightTable-ClickTracker.m.md)[Previous](LightTable-DragTracker.m.md)

