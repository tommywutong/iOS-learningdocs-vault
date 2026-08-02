---
title: People
apple_id: DTS40009050
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-07-21'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_People/Listings/AppControllerSyncing_annotated_m.html
archived_at: '2026-07-18T03:25:52.611097Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [People](People.md)


[Next](AppControllerSyncing.h.md)[Previous](AppControllerExtensions.m.md)

# AppControllerSyncing-annotated.m

```objc
/*

File: AppControllerSyncing.m

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

Copyright © 2005 Apple Computer, Inc., All Rights Reserved

*/ 

#import <SyncServices/SyncServices.h>

#import "AppControllerSyncing.h"
#import "Change.h"
#import "Constants.h"
#import "LastNameFilter.h"
#import "NSArrayExtras.h"

@implementation AppController (Syncing)

//
// ===========================================
// Syncing
//

//
// This function encapsulates the control flow for a sync
// session. It is the callback that has been registered
// in the ISyncSession call to 
// beginSessionInBackgroundWithClient:entityNames:target:selector:.
// As documented, it takes an ISyncClient and an ISyncSession
// as its two arguments. If the session is nil, then an
// ISyncSession could not be created, and the function should
// take no action. Also note that this function includes an
// exception handler. This serves as a "top-level" handler
// to catch any exceptions that are raised by the sync process.
//
- (void)performSync:(ISyncClient *)client :(ISyncSession *)session
{
    @try {
        if (session) {
            [self configureSession:session];
            [self pushDataForSession:session];
            [self pullDataForSession:session];
        }
    }
    @catch (NSException *exception) {
        NSLog(@"caught exception: %@: %@", [exception name], [exception reason]);
    }
    @finally {
        [self syncCleanup];
    }
}

//
// This method is the sync alert handler registered by the ISyncClient call to
// setSyncAlertHandler:self selector:. It calls sync:, and is therefore
// equivalent in its behavior to the user pressing the "Sync" button in the
// user interface.
//
- (void)client:(ISyncClient *)client willSyncEntityNames:(NSArray *)entityNames
{
    [self sync:self];
}

//
// This method registers our schema and client with the sync engine. 
// It is OK to register your schema and client repeatedly. Reregistrations
// do not cause any bad effects. In the case where the client is not
// already registered, a client description for the client is also supplied,
// which tells the sync engine about our client, the schema elements it
// syncs with, and (optionally) about any sync tool we supply.
//
- (ISyncClient *)registerClient 
{
    ISyncManager *manager = [ISyncManager sharedManager];
    ISyncClient *client;

    // Register the schema.
    [manager registerSchemaWithBundlePath:CanonicalContactsSchemaPath];

    // See if our client has already registered
    if (!(client = [manager clientWithIdentifier:ClientIdentifier])) {
        // and if it hasn't, register the client.
        client = [manager registerClientWithIdentifier:ClientIdentifier descriptionFilePath:
            [[NSBundle mainBundle] pathForResource:@"ClientDescription" ofType:@"plist"]];
    }

    return client;
}

//
// This method helps to negotiate a sync mode for the session. It takes it cues
// from the user interface in this example, but in the case of a "real" app,
// setting the sync mode would probably take some input from application state.
// For instance, if an application has lost part of its data set, it will likely
// wish to perform a refresh sync.
//
- (void)configureSession:(ISyncSession *)session 
{
    switch (m_syncMode) {
        case FastSync:
            // nothing to do here.
            break;
        case SlowSync:
            [session clientWantsToPushAllRecordsForEntityNames:m_entityNames];
            break;
        case RefreshSync:
            [session clientDidResetEntityNames:m_entityNames];
            break;
        case PullTheTruth:
            // not handled here. must be handled before session starts.
            break;
    }
}

//
// The push sync step. 
//
- (void)pushDataForSession:(ISyncSession *)session
{
    if ([session shouldPushAllRecordsForEntityName:EntityContact]) {
        // Slow sync. Push all records we have. Any record not pushed
        // in this step that the sync engine has in its store will
        // be construed as a delete. Ask for a refresh sync when 
        // negotiating a sync mode if you do not wish to have records
        // you do not push to be considered deletes. 
        NSEnumerator *enumerator = [m_syncRecords objectEnumerator];
        NSDictionary *appRecord;
        while ((appRecord = [enumerator nextObject])) {
            NSDictionary *syncRecord = [self syncRecordForAppRecord:appRecord];
            NSString *identifier = [appRecord objectForKey:IdentifierKey];
            [session pushChangesFromRecord:syncRecord withIdentifier:identifier];
        }
    }
    else if ([session shouldPushChangesForEntityName:EntityContact]) {
        // Fast sync. Fast syncing requires that you to present the only
        // changes since your last sync. Your code must be able to track
        // such changes over time if you wish to fast sync. Note how
        // this is accomplished in the AppController class using the 
        // Change object. Conveniently, such Changes objects are also used
        // by this application to implement undo/redo.
        NSEnumerator *enumerator = [m_syncChangesIn objectEnumerator];
        Change *change;
        while ((change = [enumerator nextObject])) {
            switch ([change type]) {
                case AddRecord:
                case ModifyRecord: {
                    // Adds and modifies are treated the same: Just push
                    // the whole record. This seems OK since our records
                    // are small. If our records were larger, it might make sense
                    // to push modifications using the pushChange: method on ISyncSession.
                    NSDictionary *appRecord = [change record];
                    NSString *identifier = [appRecord objectForKey:IdentifierKey];
                    NSDictionary *syncRecord = [self syncRecordForAppRecord:appRecord];
                    [session pushChangesFromRecord:syncRecord withIdentifier:identifier];
                    break;
                }
                case DeleteRecord:
                    // For a delete, all we have to do is push the identifier. Again, fast
                    // sync requires that we save the identifiers for deleted records so
                    // this information can be pushed here.
                    [session deleteRecordWithIdentifier:[[change oldRecord] objectForKey:IdentifierKey]];
                    break;
            }
        }
    }
}

//
// The pull sync step. 
//
- (void)pullDataForSession:(ISyncSession *)session
{
    // Figure out what to pull. If you are pulling more than one entity type,
    // ask for them individually. You cannot make any assumptions about one
    // entity type based on the result of shouldPullChangesForEntityName: for
    // another entity type.
    BOOL shouldPull = [session shouldPullChangesForEntityName:EntityContact];
    if (!shouldPull) {
        [self syncCleanup];
    }

    // Determine if we need to replace all data from server. This will return
    // YES if pulling the truth. However, it is important to note that you
    // should not throw away your data upon receiving a YES response from this
    // call. You should wait until a later time, at the very least, you should
    // wait until after you call and receive a YES response from
    // prepareToPullChangesForEntityNames:beforeDate:. The prepareXXX function
    // can return NO or may not return in the time you are willing to wait.
    // If you delete your data here and then do not pull, you will wind up
    // with no data in your code.
    // Again, if you are pulling more than one entity type, ask for them 
    // individually. you cannot make any assumptions about one entity
    // type based on the result of shouldReplaceAllRecordsOnClientForEntityName: 
    // for another entity type.
    if ([session shouldReplaceAllRecordsOnClientForEntityName:EntityContact]) {
        // As stated above: do not delete your data now.
        m_syncReplaceAllRecords = YES;
    }

    // Ask the sync engine if it is ready to pull changes. This code is willing
    // to wait an indefinite amount of time for this method to return. You may
    // wish to have a shorter time out and call this code in a loop. 
    // Particularly if you are calling this code from the main thread, you may
    // wish to provide feedback to the user while waiting for a YES response.
    if (![session prepareToPullChangesForEntityNames:m_entityNames beforeDate:[NSDate distantFuture]]) {
        [self syncFailed:session error:nil];
        return;
    }   

    // Now that prepareToPullChangesForEntityNames:beforeDate: has been called, it is
    // OK to delete data here when pulling the truth. Optionally, you could wait until
    // all the new records are pulled before deleting your local store, but you should
    // wait at least this long.
    if (m_syncReplaceAllRecords)
        [m_syncRecords removeAllObjects];

    // Now do the actual pulling.
    NSEnumerator *changeEnumerator = [session changeEnumeratorForEntityNames:m_entityNames];
    ISyncChange *change;
    while ((change = [changeEnumerator nextObject])) {
        NSString *identifier = [change recordIdentifier];
        [m_pulledIdentifiers addObject:identifier];
        switch ([change type]) {
            case ISyncChangeTypeDelete: {
                unsigned index = [m_syncRecords indexOfSyncRecordWithIdentifier:identifier];
                if ([m_syncRecords count] > index)
                    [m_syncRecords removeObjectAtIndex:index];
                break;
            }
            case ISyncChangeTypeAdd: {
                NSDictionary *syncRecord = [change record];
                NSDictionary *appRecord = [self appRecordForSyncRecord:syncRecord withIdentifier:identifier];
                [m_syncRecords addObject:appRecord];
                break;
            }
            case ISyncChangeTypeModify: {
                NSDictionary *syncRecord = [change record];
                NSDictionary *appRecord = [self appRecordForSyncRecord:syncRecord withIdentifier:identifier];
                int index = [m_syncRecords indexOfSyncRecordWithIdentifier:identifier];
                if ([m_syncRecords count] > index) {
                    [m_syncRecords replaceObjectAtIndex:index withObject:appRecord];
                }
                break;
            }
        }
    }

    // Note how records were not accepted at the time they were pulled. Separating the
    // pull operation from the accept operation gives you the opportunity to run
    // this code inside a critical section. Why might you want to do that?
    // If you are running the sync operation in a background thread, where the main
    // thread might still be accepting changes from the user, you can lock out the UI
    // here while you check the records you have pulled against the records that have
    // been modified since you started syncing. If you have such records, do not
    // accept them. By not accepting them, the sync engine will give them to you 
    // again the next time you sync, and the sync framework conflict resolver will
    // run to automatically handle conflicts.
    // This is also the place where we tell the sync engine about any record formatting
    // we have done.
    NSString *identifier;
    NSEnumerator *enumerator = [m_pulledIdentifiers objectEnumerator];
    while ((identifier = [enumerator nextObject])) {
        [session clientAcceptedChangesForRecordWithIdentifier:identifier 
            formattedRecord:[m_formattedRecords objectForKey:identifier]
            newRecordIdentifier:nil];
    }

    // Second phase of two-phase commit.
    [session clientCommittedAcceptedChanges];
    [session finishSyncing];

    // Update our local record store with the records modified by the sync operation.
    [m_records removeAllObjects];
    [m_records addObjectsFromArray:m_syncRecords];
}

//
// Catch all failure handler. This would likely communicate the failure to the
// user in some kind, gentle (and hopefully informative) way.
//
- (void)syncFailed:(ISyncSession *)session error:(NSError *)error
{
    [session cancelSyncing];
    NSLog(@"sync failed: %@", [error localizedFailureReason]);
    [self syncCleanup];
}

//
// All sync sessions, whether they succeed or fail, come through this code.
// This handles updating the UI, and releases some objects used in the sync
// session.
//
- (void)syncCleanup
{
    [m_syncProgress stopAnimation:self];
    [m_syncProgress setHidden:YES];
    [m_syncButton setEnabled:YES];
    [m_syncModeButton setEnabled:YES];

    [m_syncRecords release];
    [m_syncChangesIn release];
    [m_pulledIdentifiers release];
    [m_formattedRecords release];

    [m_table reloadData];
    [self update];
    [self writeDataFile];
}

//
// ===========================================
// Record conversion
//

//
// This method converts a sync record, like the ones pulled from
// the sync engine, into the form used by the application. The mapping
// is trivially simple in this example, but real code will likely need
// to do more serious work here.
//
- (NSDictionary *)syncRecordForAppRecord:(NSDictionary *)record
{
    NSString *firstName = [record objectForKey:FirstNameKey];
    NSString *lastName = [record objectForKey:LastNameKey];
    return [NSDictionary dictionaryWithObjectsAndKeys:
        EntityContact, ISyncRecordEntityNameKey,
        firstName ? firstName : @"", FirstNameKey,
        lastName ? lastName : @"", LastNameKey,
        nil];
}

//
// This method converts an application record, like the ones used to
// represent data internally in application-specific code, into the
// form the sync engine uses. The mapping is trivially simple in 
// this example, but real code will likely need to do more serious 
// work here.
//
- (NSDictionary *)appRecordForSyncRecord:(NSDictionary *)record withIdentifier:(NSString *)identifier
{
    NSString *firstName = [record objectForKey:FirstNameKey];
    NSString *lastName = [record objectForKey:LastNameKey];
    if (m_syncsUsingRecordFormatting) {
        firstName = [firstName length] > FormatLimit ? [firstName substringToIndex:FormatLimit] : firstName;
        lastName = [lastName length] > FormatLimit ? [lastName substringToIndex:FormatLimit] : lastName;
    }
    NSDictionary *result = [NSDictionary dictionaryWithObjectsAndKeys:
        identifier, IdentifierKey,
        firstName ? firstName : @"", FirstNameKey,
        lastName ? lastName : @"", LastNameKey,
        nil];
    if (m_syncsUsingRecordFormatting) {
        [m_formattedRecords setObject:[self syncRecordForAppRecord:result] forKey:identifier];
    }
    return result;
}

//
// ===========================================
// IBActions
//

//
// Handles the changes to sync options as shown in the "Options" menu in 
// the application.
//
- (IBAction)syncOptionsChanged:(id)sender
{
    int value = [sender tag];
    switch (value) {
        case UsesRecordFiltering:
            m_syncsUsingRecordFiltering = !m_syncsUsingRecordFiltering;
            break;
        case UsesRecordFormatting:
            m_syncsUsingRecordFormatting = !m_syncsUsingRecordFormatting;
            break;
        case UsesSyncAlertHandler:
            m_syncsUsingSyncAlertHandler = !m_syncsUsingSyncAlertHandler;
            BOOL flag = m_syncsUsingSyncAlertHandler;

            // These few lines of code register a sync alert handler method.
            // When our application is running, it will be asked through the
            // handler we supply if it wishes to join a sync session that is
            // beginning.
            ISyncClient *client = [self registerClient];
            [client setShouldSynchronize:flag withClientsOfType:ISyncClientTypeApplication];
            [client setShouldSynchronize:flag withClientsOfType:ISyncClientTypeDevice];
            [client setShouldSynchronize:flag withClientsOfType:ISyncClientTypeServer];
            [client setShouldSynchronize:flag withClientsOfType:ISyncClientTypePeer];
            [client setSyncAlertHandler:self selector:@selector(client:willSyncEntityNames:)];

            break;
        case SyncsOnAppDeactivate:
            m_syncsOnAppDeactivate = !m_syncsOnAppDeactivate;
            NSNotificationCenter *defaultCenter = [NSNotificationCenter defaultCenter];
            if (m_syncsOnAppDeactivate) {
                [defaultCenter addObserver:self 
                    selector:@selector(sync:) 
                    name:NSApplicationWillResignActiveNotification 
                    object:nil];
            }
            else {
                [defaultCenter removeObserver:self 
                    name:NSApplicationWillResignActiveNotification 
                    object:nil];
            }
            break;
    }
}

//
// This method starts a sync session. It updates the UI, creates some
// session-specific objects used to track the activity of the session,
// and starts the session running.
//
- (IBAction)sync:(id)sender
{
    @try {
        [m_syncButton setEnabled:NO];
        [m_syncModeButton setEnabled:NO];
        [m_syncProgress setHidden:NO];
        [m_syncProgress startAnimation:self];
        [[m_window undoManager] removeAllActions];

        m_syncRecords = [m_records mutableCopy];
        m_syncChangesIn = [m_changes copy];
        [m_changes removeAllObjects];
        m_pulledIdentifiers = [[NSMutableArray alloc] init];
        m_formattedRecords = [[NSMutableDictionary alloc] init];
        m_syncReplaceAllRecords = NO;
        m_syncMode = [m_syncModeButton indexOfSelectedItem];

        // Register ourselves as a client if this has not yet been done.
        // You may re-register yourself as many times as you like without
        // worry.
        ISyncClient *client = [self registerClient];
        if (!client) {
            NSLog(@"cannot create sync client.");
            return;
        }

        // If you are going to be doing record filtering, set the filters
        // on the client before starting the session.
        if (m_syncsUsingRecordFiltering) {
            id filter = [LastNameFilter filter];
            [client setFilters:[NSArray arrayWithObject:filter]]; 
        }
        else {
            [client setFilters:[NSArray array]]; 
        }

        // Also, if you are pulling the truth, tell the client this fact
        // before starting the session.
        if (m_syncMode == PullTheTruth) {
            [client setShouldReplaceClientRecords:YES forEntityNames:m_entityNames];
        }

        // Ask for a session to be started in the background. This is a good choice
        // if starting the session from the main thread, since other clients in 
        // other processes may be joining, and you will not want to block your UI
        // while that handshaking is taking place.
        [ISyncSession beginSessionInBackgroundWithClient:client entityNames:m_entityNames 
            target:self selector:@selector(performSync::)];
    }
    @catch (NSException *exception) {
        NSLog(@"caught exception: %@: %@", [exception name], [exception reason]);
        [self syncCleanup];
    }
}

@end
```

[Next](AppControllerSyncing.h.md)[Previous](AppControllerExtensions.m.md)

