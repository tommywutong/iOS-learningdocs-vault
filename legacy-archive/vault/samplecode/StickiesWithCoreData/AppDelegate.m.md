---
title: StickiesWithCoreData
apple_id: DTS40009052
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_StickiesWithCoreData/Listings/AppDelegate_m.html
archived_at: '2026-07-18T03:25:55.422652Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [StickiesWithCoreData](StickiesWithCoreData.md)


[Next](Sticky.h.md)[Previous](AppDelegate.h.md)

# AppDelegate.m

```objc
/*

File: AppDelegate.m

Abstract: The Stickies application delegate

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

#import "AppDelegate.h"
#import "Sticky.h"
#import "StickyWindowController.h"



@implementation AppDelegate


#pragma mark
#pragma mark Persistence

- (NSString *)folderName
{
    return @"SyncExamples";
}

- (NSString *)fileName
{
    return @"com.mycompany.StickiesUsingCoreData.xml";
}

- (NSString *)applicationSupportFolder
{
    NSString *applicationSupportFolder = nil;
    FSRef foundRef;
    OSErr err = FSFindFolder(kUserDomain, kApplicationSupportFolderType, kDontCreateFolder, &foundRef);
    if (err != noErr) {
        NSRunAlertPanel(@"Alert", @"Can't find application support folder", @"Quit", nil, nil);
        [[NSApplication sharedApplication] terminate:self];
    } else {
        unsigned char path[1024];
        FSRefMakePath(&foundRef, path, sizeof(path));
        applicationSupportFolder = [NSString stringWithUTF8String:(char *)path];
        applicationSupportFolder = [applicationSupportFolder stringByAppendingPathComponent:[self folderName]];
    }
    return applicationSupportFolder;
}

- (NSManagedObjectContext *)managedObjectContext
{
    NSError *error;
    NSString *applicationSupportFolder = nil;
    NSURL *url;
    NSFileManager *fileManager;
    NSPersistentStoreCoordinator *coordinator;
    NSPersistentStore *store;
    NSURL *fastSyncDetailURL;

    if (managedObjectContext) {
        return managedObjectContext;
    }

    fileManager = [NSFileManager defaultManager];
    applicationSupportFolder = [self applicationSupportFolder];
    if ( ![fileManager fileExistsAtPath:applicationSupportFolder isDirectory:NULL] ) {
        [fileManager createDirectoryAtPath:applicationSupportFolder withIntermediateDirectories:YES attributes:nil error:nil];
    }
    // Request a refresh sync if the file doesn't exist
    if (![fileManager fileExistsAtPath:[applicationSupportFolder stringByAppendingPathComponent:[self fileName]]]){
        NSLog(@"Refresh sync because backup file doesn't exist.");
        shouldRefreshSync = YES;
    }

    url = [NSURL fileURLWithPath: [applicationSupportFolder stringByAppendingPathComponent:[self fileName]]];   
    coordinator = [[NSPersistentStoreCoordinator alloc] initWithManagedObjectModel:[NSManagedObjectModel mergedModelFromBundles:nil]];
    store = [coordinator addPersistentStoreWithType:NSXMLStoreType configuration:nil URL:url options:nil error:&error];

    if (store != nil) {
        fastSyncDetailURL = [NSURL fileURLWithPath:[applicationSupportFolder stringByAppendingPathComponent:@"com.mycompany.StickiesUsingCoreData.fastsyncstore"]];
        [coordinator setStoresFastSyncDetailsAtURL:fastSyncDetailURL forPersistentStore:store];
        managedObjectContext = [[NSManagedObjectContext alloc] init];
        [managedObjectContext setPersistentStoreCoordinator: coordinator];
    } else {
        // Not an error if the files is not there.
        [[NSApplication sharedApplication] presentError:error];
    }    
    [coordinator release];

    return managedObjectContext;
}


#pragma mark
#pragma mark Sync

- (ISyncClient *)syncClient
{
    NSString *clientIdentifier = [[NSBundle mainBundle] bundleIdentifier];
    NSString *reason = @"unknown error";
    ISyncClient *client;

    @try {
        client = [[ISyncManager sharedManager] clientWithIdentifier:clientIdentifier];
        if (nil == client) {
            if (![[ISyncManager sharedManager] registerSchemaWithBundlePath:
                  [[self applicationSupportFolder] stringByAppendingPathComponent:[@"Stickies" stringByAppendingPathExtension:@"syncschema"]]]) {
                reason = @"error registering the Stickies sync schema";
            } else {
                client = [[ISyncManager sharedManager] registerClientWithIdentifier:clientIdentifier descriptionFilePath:[[NSBundle mainBundle] pathForResource:@"ClientDescription" ofType:@"plist"]];
                [client setShouldSynchronize:YES withClientsOfType:ISyncClientTypeApplication];
                [client setShouldSynchronize:YES withClientsOfType:ISyncClientTypeDevice];
                [client setShouldSynchronize:YES withClientsOfType:ISyncClientTypeServer];
                [client setShouldSynchronize:YES withClientsOfType:ISyncClientTypePeer];
            }
        }
    }
    @catch (id exception) {
        client = nil;
        reason = [exception reason];
    }

    if (nil == client) {
        NSRunAlertPanel(@"You can not sync your Stickies.", [NSString stringWithFormat:@"Failed to register the sync client: %@", reason], @"OK", nil, nil);
    }

    return client;
}

- (void)client:(ISyncClient *)client mightWantToSyncEntityNames:(NSArray *)entityNames
{
    NSLog(@"Saving for alert to sync...");
    [self saveAction:self];
}

- (NSArray *)managedObjectContextsToMonitorWhenSyncingPersistentStoreCoordinator:(NSPersistentStoreCoordinator *)coordinator
{
    return [NSArray arrayWithObject:[self managedObjectContext]];
}

- (NSArray *)managedObjectContextsToReloadAfterSyncingPersistentStoreCoordinator:(NSPersistentStoreCoordinator *)coordinator
{
    return [NSArray arrayWithObject:[self managedObjectContext]];
}

- (NSDictionary *)persistentStoreCoordinator:(NSPersistentStoreCoordinator *)coordinator willPushRecord:(NSDictionary *)record forManagedObject:(NSManagedObject *)managedObject inSyncSession:(ISyncSession *)session
{
    NSLog(@"push %@ = %@", [managedObject objectID], [record description]);
    return record;
}

- (ISyncChange *)persistentStoreCoordinator:(NSPersistentStoreCoordinator *)coordinator willApplyChange:(ISyncChange *)change toManagedObject:(NSManagedObject *)managedObject inSyncSession:(ISyncSession *)session
{
    NSLog(@"pull %@", [change description]);
    return change;
}

#pragma mark
#pragma mark Application

- (void)syncAction:(id)sender
{
    NSError *error = nil;
    ISyncClient *client = [self syncClient];
    if (nil != client) {
        [[[self managedObjectContext] persistentStoreCoordinator] syncWithClient:client inBackground:YES handler:self error:&error];
    }
    if (nil != error) {
        [[NSApplication sharedApplication] presentError:error];
    }
}

- (void)saveAction:(id)sender
{
    NSError *error = nil;
    [[self managedObjectContext] save:&error];
    if (nil != error) {
        [[NSApplication sharedApplication] presentError:error];
    } else {
        [self syncAction:sender];
    }
}

- (void)saveInMainThread:(id)sender
{
    NSLog(@"Saving after delay...");
    [self performSelector:@selector(saveAction:) withObject:sender afterDelay:0.0];
}

- (void)applicationDidFinishLaunching:(NSNotification *)notification 
{
    // Next time through the event loop, load all the stickies.
    // This delay is required because the NSArrayController's fetch request is delayed until the next event loop
    NSLog(@"will load all stickies");
    [self performSelector:@selector(loadAllStickies) withObject:nil afterDelay:0.0];
    [[self syncClient] setSyncAlertHandler:self selector:@selector(client:mightWantToSyncEntityNames:)];
    [self syncAction:nil];

    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(managedObjectContextDidChange:) name:NSManagedObjectContextObjectsDidChangeNotification object:nil];
}

- (void)applicationWillTerminate:(NSNotification *)notification
{
    [self saveAction:nil];
}

- (void)createWindowControllersForStickies:(NSArray *)stickies
{
    if (nil == windowControllers) windowControllers = [[NSMutableArray alloc] init];

    for(Sticky *sticky in stickies)
    {
        if([self managedObjectContext] == [sticky managedObjectContext])
        {
            StickyWindowController *controller = [[StickyWindowController alloc] initWithSticky:sticky];
            [controller showWindow:self];
            [windowControllers addObject:controller];
        }
    }
}

- (void)deleteWindowControllersForStickies:(NSArray *)stickies
{
    for(Sticky *sticky in stickies)
    {
        for(StickyWindowController *controller in windowControllers)
        {
            if([[sticky objectID] isEqual:[[controller sticky] objectID]])
            {
                [controller close];
                [windowControllers removeObject:controller];
                break;
            }
        }
    }
}

- (void)loadAllStickies 
{
    // Fault each sticky in the array controller and call it's setup function
    [self createWindowControllersForStickies:[stickiesController arrangedObjects]];
}

- (void)removeSticky:(Sticky *)aSticky 
{
    if (nil != aSticky) [[self managedObjectContext] deleteObject:aSticky];
}

- (void)managedObjectContextDidChange:(NSNotification *)notification
{
    NSLog(@"Managed Object Context changed");
    [self createWindowControllersForStickies:[[[notification userInfo] objectForKey:NSInsertedObjectsKey] allObjects]];
    [self deleteWindowControllersForStickies:[[[notification userInfo] objectForKey:NSDeletedObjectsKey] allObjects]];
}

@end
```

[Next](Sticky.h.md)[Previous](AppDelegate.h.md)

