---
title: 'CloudSearch: Query for documents in iCloud using NSMetaDataQuery'
apple_id: DTS40013494
resource_type: Sample Code
platform: iOS|macOS
topic: Data Management
technology: ApplicationServices
published: '2016-03-24'
source_url: https://developer.apple.com/library/archive/samplecode/CloudSearch/Listings/iOS_CloudSearch_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:03:35.328237Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudSearch: Query for documents in iCloud using NSMetaDataQuery](CloudSearch-%20Query%20for%20documents%20in%20iCloud%20using%20NSMetaDataQuery.md)


[Next](iOS-CloudSearch-AAPLTableViewController.h.md)[Previous](iOS-CloudSearch-main.m.md)

# iOS/CloudSearch/AAPLAppDelegate.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate class used for copying cloud documents.
 */

#import "AAPLAppDelegate.h"
#import "AAPLTableViewController.h"

@interface AAPLAppDelegate ()

@property (nonatomic, strong) NSURL *ubiquityContainer;
@property (nonatomic, strong) NSArray *documents;

@property (nonatomic, strong) NSMetadataQuery *ubiquitousQuery;
@property id metadataQueryFinishGatherObserver;

@end


#pragma mark -

@implementation AAPLAppDelegate

// The app delegate must implement the window @property
// from UIApplicationDelegate @protocol to use a main storyboard file.
@synthesize window;

// -------------------------------------------------------------------------------
//  ubiquityDocumentsFolder
// -------------------------------------------------------------------------------
- (NSURL *)ubiquityDocumentsFolder
{
    return [self.ubiquityContainer URLByAppendingPathComponent:@"Documents" isDirectory:YES];
}

// -------------------------------------------------------------------------------
//  willFinishLaunchingWithOptions:launchOptions
// -------------------------------------------------------------------------------
- (BOOL)application:(UIApplication *)application willFinishLaunchingWithOptions:(nullable NSDictionary *)launchOptions
{
    // remember our ubiquity container NSURL for later use
    _ubiquityContainer = [[NSFileManager defaultManager] URLForUbiquityContainerIdentifier:nil];

    return YES;
}

// -------------------------------------------------------------------------------
//  applicationDidBecomeActive:application
// -------------------------------------------------------------------------------
- (void)applicationDidBecomeActive:(UIApplication *)application
{
    if (self.ubiquityContainer != nil)
    {
        [self copyDefaultDocumentsToCloud];
    }
}

// -------------------------------------------------------------------------------
//  didFinishLaunchingWithOptions:launchOptions
// -------------------------------------------------------------------------------
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    _documents = @[@"Text Document1.txt",
                   @"Text Document2.txt",
                   @"Text Document3.txt",
                   @"Text Document4.rtf",
                   @"Image Document.jpg",
                   @"PDF Document.pdf",
                   @"HTML Document.html",
                   @"Video.m4v"];

    if (self.ubiquityContainer == nil)
    {
        dispatch_async(dispatch_get_main_queue(), ^ {

            // not logged in, alert the user
            UIAlertController *alert = [UIAlertController alertControllerWithTitle:NSLocalizedString(@"Not_Logged_In", nil)
                                                                           message:NSLocalizedString(@"Not_Logged_In_Explain", nil)
                                                                    preferredStyle:UIAlertControllerStyleAlert];

            UIAlertAction *OKAction = [UIAlertAction actionWithTitle:NSLocalizedString(@"OK_Button_Title", nil)
                                                               style:UIAlertActionStyleDefault
                                                             handler:nil];
            [alert addAction:OKAction];
            [self.window.rootViewController presentViewController:alert animated:YES completion:nil];
        });
    }

    return YES;
}

// -------------------------------------------------------------------------------
//  copyDefaultDocumentsToCloud
// -------------------------------------------------------------------------------
- (void)copyDefaultDocumentsToCloud
{
    // the caller makes sure the ubiquityContainer is not nil
    assert(self.ubiquityContainer != nil);

    NSMetadataQuery *queryForPreloadData = [[NSMetadataQuery alloc] init];
    queryForPreloadData.predicate = [NSPredicate predicateWithFormat:@"%K like '*.*'", NSMetadataItemFSNameKey];
    queryForPreloadData.searchScopes = @[NSMetadataQueryUbiquitousDocumentsScope];

    __block __weak id observer; // Use __weak to ensure the observer is released after being removed from NC.
    observer = [[NSNotificationCenter defaultCenter] addObserverForName:NSMetadataQueryDidFinishGatheringNotification
                                                                 object:queryForPreloadData
                                                                  queue:nil // use the current queue
                                                             usingBlock:^(NSNotification *gatherNotification)
    {
        // Use queryForPreloadData so that it is held by the block
        // thus won't be released outside of the method.
        //
        [queryForPreloadData stopQuery];

        NSMutableArray *existingFileURLs = [queryForPreloadData.results valueForKey:NSMetadataItemURLKey];
        existingFileURLs = [existingFileURLs valueForKey:@"lastPathComponent"];

        if (existingFileURLs.count == 0)
        {
            // no default documents found, ask user to upload them
            UIAlertController *alert = [UIAlertController alertControllerWithTitle:NSLocalizedString(@"Ask_Upload", nil)
                                                                           message:NSLocalizedString(@"Ask_Upload_Explain", nil)
                                                                    preferredStyle:UIAlertControllerStyleAlert];

            UIAlertAction *OKAction = [UIAlertAction actionWithTitle:NSLocalizedString(@"OK_Button_Title", nil)
                                                               style:UIAlertActionStyleDefault
                                                             handler:^(UIAlertAction *action) {
                NSURL *documentsCloudDirectoryURL = [self ubiquityDocumentsFolder];
                for (NSString *documentName in self.documents)
                {
                    if (![existingFileURLs containsObject:documentName])
                    {
                        [[NSFileManager defaultManager] copyItemAtPath:[[NSBundle mainBundle].resourcePath stringByAppendingPathComponent:documentName]
                                                                toPath:[documentsCloudDirectoryURL.path stringByAppendingPathComponent:documentName]
                                                                 error:nil];
                    }
                }

                // since the copy operation occurred, we need to tell our table view to rescan for documents
                AAPLTableViewController *tableViewController = (AAPLTableViewController *)((UINavigationController *)self.window.rootViewController).visibleViewController;
                [tableViewController rescanForDocuments];
            }];
            [alert addAction:OKAction];

            UIAlertAction *cancelAction = [UIAlertAction actionWithTitle:NSLocalizedString(@"Cancel_Button_Title", nil)
                                                                   style:UIAlertActionStyleCancel
                                                                 handler:nil];
            [alert addAction:cancelAction];

            [self.window.rootViewController presentViewController:alert animated:YES completion:nil];
        }
        [[NSNotificationCenter defaultCenter] removeObserver:observer];
    }];

    [queryForPreloadData startQuery];
}

@end
```

[Next](iOS-CloudSearch-AAPLTableViewController.h.md)[Previous](iOS-CloudSearch-main.m.md)

