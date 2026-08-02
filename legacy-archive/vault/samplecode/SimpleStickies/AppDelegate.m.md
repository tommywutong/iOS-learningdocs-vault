---
title: SimpleStickies
apple_id: DTS40009051
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_SimpleStickies/Listings/AppDelegate_m.html
archived_at: '2026-07-18T03:25:54.224686Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleStickies](SimpleStickies.md)


[Next](DataSource.h.md)[Previous](AppDelegate.h.md)

# AppDelegate.m

```objc
/*

 File: AppDelegate.m

 Abstract: Application delegate that implements the saving, loading and
 syncing of user records.

 Version: 1.0

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
#import "EntityModel.h"
#import "DataSource.h"
#import "RecordTransformer.h"

#define kDefaultsTrickleSync @"TrickleSync"

@interface AppDelegate (AppDelegatePrivate)
// Private Syncing Methods
- (void)setPreferredSyncMode:(ISyncSessionDriverMode)mode;
- (ISyncSessionDriverMode)preferredSyncMode;

// Private Saving and Loading Methods
- (BOOL)_save;
- (NSString *)_applicationSupportFolder;
- (BOOL)_readFromURL:(NSURL *)url;
- (BOOL)_writeToURL:(NSURL *)url;
- (NSData *)_dataRepresentation;
- (BOOL)_loadDataRepresentation:(NSData *)data;
- (id)_loadEntityModelFromFile:(NSString *)fileName;

// Deleting Records
- (id)_objectForRecordIdentifier:(NSString *)recordIdentifier;
- (BOOL)_deleteRecordForRecordIdentifier:(NSString *)recordIdentifier;

@end


@implementation AppDelegate

// Initialization and Deallocation

- (id)init {
    self = [super init];
    if (self != nil) {
        // These are set when they are first accessed.
        _myDataSource = nil;
        _entityModel = nil;
        _entityAnchors = nil;

        // Create an ISyncSessionDriver object and configure it to handle sync alerts
        syncDriver = [ISyncSessionDriver sessionDriverWithDataSource:self];
        [syncDriver setHandlesSyncAlerts: YES];

        // Set the preferred sync mode to fast
        [self setPreferredSyncMode:ISyncSessionDriverModeFast];

        // Setup the record transformer.
        _recordTransformer = [[RecordTransformer alloc] init];
        [_recordTransformer setDataSource:[self dataSource]];

        // Syncs after launching to pull any changes since last running this app.
        (void)[syncDriver sync];

        // Register for data source change notifications.
        [(NSNotificationCenter *)[NSNotificationCenter defaultCenter] addObserver:self 
                                                                         selector:@selector(_handleSaveRequestNotification:) 
                                                                             name:DataSourceChangedNotification 
                                                                           object:[self dataSource]];
    }
    return self;
}


//********* ISyncSessionDriverDataSource Methods *************


// Providing Client Information

- (NSString *)clientIdentifier
{
    return @"com.mycompany.SimpleStickies";
}

- (NSURL *)clientDescriptionURL
{
    NSLog(@"AppDelegate: Requesting client description plist...");
    return [NSURL fileURLWithPath:[[NSBundle mainBundle] pathForResource:@"ClientDescription" ofType:@"plist"]];
}

- (NSArray *)schemaBundleURLs {
    NSLog(@"AppDelegate: Requesting schema bundle paths...");
    return [NSArray arrayWithObject:[NSURL fileURLWithPath:
                                     [[self _applicationSupportFolder] stringByAppendingPathComponent:[@"Stickies" stringByAppendingPathExtension:@"syncschema"]]]];
}

- (NSArray *)entityNamesToSync
{
    NSLog(@"AppDelegate: Requesting entity names...");
    return [[self entityModel] entityNames];
}

// Negotiating Phase

- (ISyncSessionDriverMode)preferredSyncModeForEntityName:(NSString *)entity
{
    NSLog(@"AppDelegate: Preferred sync mode=%d", [self preferredSyncMode]);
    return [self preferredSyncMode];
}


// Pushing Phase

// Transforms the sync source objects for the given entityName into sync records. 
// Invoked when the sync engine requests all records for an entity.
- (NSDictionary *)recordsForEntityName:(NSString *)entityName moreComing:(BOOL *)moreComing error:(NSError **)outError
{
    NSArray *objects = [[self dataSource] objectsForEntityName:entityName];

    // Transform the objects to records and puts them in a dictionary where the keys are record identifiers.
    NSEnumerator *objectEnumerator = [objects objectEnumerator];
    id anObject;
    NSMutableDictionary *records = [NSMutableDictionary dictionary];

    [_recordTransformer setEntityName:entityName];
    while (anObject = [objectEnumerator nextObject]){
        [records setObject:[_recordTransformer transformedValue:anObject] forKey:[anObject valueForKey:@"primaryKey"]];
    }
    return records;
}

// Returns a dictionary of changed records where the keys are the record identifiers. Uses RecordTransformer to
// to transform sync source objects to Sync Service records.
- (NSDictionary *)changedRecordsForEntityName:(NSString *)entityName moreComing:(BOOL *)moreComing error:(NSError **)outError
{
    NSArray *changedObjects = [[self dataSource] changedObjectsForEntityName:entityName];

    // Transform the objects to records and put them in a dictionary where the keys are the record identifiers
    NSEnumerator *objectEnumerator = [changedObjects objectEnumerator];
    id anObject;
    NSMutableDictionary *changes = [NSMutableDictionary dictionary];

    [_recordTransformer setEntityName:entityName];
    while (anObject = [objectEnumerator nextObject]){
        [changes setObject:[_recordTransformer transformedValue:anObject] forKey:[anObject valueForKey:@"primaryKey"]];
    }
    NSLog(@"AppDelegate: changedRecordsForEntityName... where changes=%@", [changes description]);

    return changes;
}

// Returns an array of record identifiers of the deleted objects. Invoked when pushing deletions to the sync engine.
- (NSArray *)identifiersForRecordsToDeleteForEntityName:(NSString *)entityName moreComing:(BOOL *)moreComing error:(NSError **)outError
{
    NSArray *deletedRecords = [[self dataSource] deletedObjectsForEntityName:entityName];
    return [deletedRecords valueForKey:@"primaryKey"];
}

// Pulling Phase

// Applies a pulled change (inserts, changes, or deletes a source object) for the specified record, record identifier and entity name. 
// The property values in record are applied to the existing source object. Returns an error if the source object 
// could not be created or found.
- (ISyncSessionDriverChangeResult)applyChange:(ISyncChange *)change 
                                forEntityName:(NSString *)entityName 
                     remappedRecordIdentifier:(NSString **)outRecordIdentifier 
                              formattedRecord:(NSDictionary **)outRecord 
                                        error:(NSError **)outError
{
    NSLog(@"AppDelegate: applyChange... where change=%@", [change description]);

    // Apply a delete change
    if ([change type] == ISyncChangeTypeDelete){ 
        if ([self deleteObjectForRecordIdentifier:[change recordIdentifier] forEntityName:entityName] == YES)
            return ISyncSessionDriverChangeAccepted;
        else {
            // ERROR: this is probably a can't find record identifier error. Modify deleteObjectForRecordIdentifier:... to return an NSError instead.
            *outError = [NSError errorWithDomain:@"SimpleStickies" code:0 
                                        userInfo:[NSDictionary dictionaryWithObject:@"Can't delete record." forKey:NSLocalizedDescriptionKey]];
            return ISyncSessionDriverChangeError;
        }
    }

    // Use the transformer to apply the change to the existing source object, or create a new source
    // object if this is an add.
    [_recordTransformer setEntityName:entityName];
    id sourceObject = [_recordTransformer reverseTransformedValueWithChange:change];

    if (sourceObject == nil)
        return ISyncSessionDriverChangeRefused;
    else
        return ISyncSessionDriverChangeAccepted;
}

- (BOOL)deleteObjectForRecordIdentifier:(NSString *)recordIdentifier forEntityName:(NSString *)entityName
{
    NSLog(@"AppDelegate: deleteObject... where recordIdentifier=%@", recordIdentifier);

    id anObject = [self _objectForRecordIdentifier:recordIdentifier];
    if (anObject == nil){
        NSLog(@"FAILED to delete record with recordIdentifier=%@", recordIdentifier);
        return NO;
    }
    NSLog(@"Deleting object: %@", anObject);    
    [self _deleteRecordForRecordIdentifier:recordIdentifier];
    return YES;     
}

- (BOOL)deleteAllRecordsForEntityName:(NSString *)entityName error:(NSError **)outError
{
    [[[self dataSource] mutableArrayValueForKey:[[self dataSource] keyForEntityName:entityName]] removeAllObjects];
    return YES; 
}

//Anchor Methods

- (NSString *)lastAnchorForEntityName:(NSString *)entity
{
    if(_entityAnchors == nil)
    {
        _entityAnchors = [[NSMutableDictionary alloc] init];
    }   
    NSLog(@"Retrieving last sync anchor: %@", [_entityAnchors objectForKey:entity]);
    return [_entityAnchors objectForKey:entity];
}

- (NSString *)nextAnchorForEntityName:(NSString *)entity
{
    if(_entityAnchors == nil)
    {
        _entityAnchors = [[NSMutableDictionary alloc] init];
    }
    NSString *nextAnchor = [NSString stringWithFormat:@"SimpleStickies - %@ - %@", entity, [NSDate date]];
    NSLog(@"Giving next sync anchor: %@", nextAnchor);
    [_entityAnchors setObject:nextAnchor forKey:entity];
    return nextAnchor;
}


//********* ISyncSessionDriver Delegate Methods *************

// This method starts the progress indicator and saves the local records before a sync begins.
- (BOOL)sessionDriver:(ISyncSessionDriver *)sender didRegisterClientAndReturnError:(NSError **)outError {
    // Start the progress indicator.
    NSProgressIndicator* progressIndicator = [self progressIndicator];
    [progressIndicator setUsesThreadedAnimation:YES];
    [progressIndicator setHidden:NO];
    [progressIndicator startAnimation:self];
    [progressIndicator display];

    BOOL saveSuccess = [self _save];
    if (saveSuccess == NO){
        if (outError) {
            *outError = [NSError errorWithDomain:@"SimpleStickies" code:0 
                                        userInfo:[NSDictionary dictionaryWithObject:@"Failed to save before syncing." forKey:NSLocalizedDescriptionKey]];
        }
        return NO;
    }
    return YES;
}

// This method clears the local changes from the data source and stops the progress indicator. This method is invoked
// when a sync session is successful so it sets the preferred sync mode to fast.
- (void)sessionDriverDidFinishSession:(ISyncSessionDriver *)sender {
    // Clear the changes so they are not synced the next time.
    [[self dataSource] clearAllChanges];
    [self setPreferredSyncMode:ISyncSessionDriverModeFast];

    // Stop the progress indicator
    [[self progressIndicator] stopAnimation:self];
    [[self progressIndicator] setHidden:YES];
}

// Stops the progress indicator and sets the preferred sync mode to slow since the sync session was cancelled.
- (void)sessionDriverDidCancelSession:(ISyncSessionDriver *)sender {
    [self setPreferredSyncMode:ISyncSessionDriverModeSlow];
    NSError *syncError = [syncDriver lastError];
    NSAlert *theAlert = [NSAlert alertWithError:syncError];
    [theAlert runModal];

    // Stop the progress indicator
    [[self progressIndicator] stopAnimation:self];
    [[self progressIndicator] setHidden:YES];
}


// Saving and Loading Methods

// Saves the sync source to disk. Returns YES if successful, NO otherwise.
- (BOOL)saveSource
{
    NSString *applicationSupportFolder = [self _applicationSupportFolder];
    NSURL *url = [NSURL fileURLWithPath:[applicationSupportFolder stringByAppendingPathComponent:[self fileName]]];
    if ([self _writeToURL:url] == NO) {
        NSLog(@"Failed to save source.");
        return NO;
    }
    NSLog(@"Successfully saved file.");
    return YES;
}

// Writes the sync source to the specified fie URL. Returns YES if successful, NO otherwise.
- (BOOL)_writeToURL:(NSURL *)url
{
    NSData *myData = [self _dataRepresentation];
    if (![myData writeToURL:url atomically:YES])
        return NO;
    return YES;
}

// Reads the sync source in from the specified file URL. Returns YES if successful, NO otherwise.
- (BOOL)_readFromURL:(NSURL *)url
{
    NSData *myData = [[NSData alloc] initWithContentsOfURL:url];
    if (myData == nil)
        return NO;

    [self _loadDataRepresentation:myData];
    return YES;
}

// Returns an NSData representation of the receiver for saving to disk. Encodes the data source and the 
// preferred sync mode.
- (NSData *)_dataRepresentation
{
    // Convert the DataSource object dictionary to an NSData for archiving because it can contain
    // unsupported property list types, like instances of NSCalendarDate and custom entities.
    NSDictionary *dict = [NSDictionary dictionaryWithObjectsAndKeys:
        [NSArchiver archivedDataWithRootObject:[_myDataSource representation]], @"data source",
        [NSNumber numberWithInteger:[self preferredSyncMode]], @"sync mode",
        _entityAnchors, @"entity anchors", 
        nil];
    NSData * data = (NSData *)CFPropertyListCreateXMLData(kCFAllocatorDefault, (CFPropertyListRef)dict);
    return data;
}

// Decodes the receiver from the given data that contains the data source and preferred sync mode.
// Returns YES if successful, NO otherwise.
- (BOOL)_loadDataRepresentation:(NSData *)data {
    NSString *error;
    NSDictionary *dict = (NSDictionary *)CFPropertyListCreateFromXMLData(kCFAllocatorDefault, (CFDataRef)data, 
                                                                         kCFPropertyListMutableContainersAndLeaves, 
                                                                         (CFStringRef *)&error);
    // Converts the NSData back into a DataSource representation that may contain non-property list types.
    [_myDataSource setRepresentation:[NSUnarchiver unarchiveObjectWithData:[dict objectForKey:@"data source"]]];
    NSInteger syncMode = [[dict objectForKey:@"sync mode"] integerValue];
    _entityAnchors = [dict objectForKey:@"entity anchors"];
    [self setPreferredSyncMode:syncMode];
    return YES;
}


// Reverts the data source to the last saved state. Returns YES if successful, NO otherwise.
- (BOOL)revertSource
{
    NSString *applicationSupportFolder = [self _applicationSupportFolder];
    NSURL *url = [NSURL fileURLWithPath:[applicationSupportFolder stringByAppendingPathComponent:[self fileName]]];
    if ([self _readFromURL:url] == NO) {
        NSLog(@"Failed to revert source.");
        return NO;
    }
    NSLog(@"Reverted to the saved file.");

    return YES;
}

// Returns YES if the dataSource changed, NO otherwise.
- (BOOL)hasChanges
{
    return [[self dataSource] isChanged];
}


//
// Syncing Methods
//

// Saves the receiver's records to disk by invoking saveSource.
- (BOOL)_save {
    return [self saveSource];
}


- (NSProgressIndicator*) progressIndicator {
    return _progressIndicator;
}

// Saves the receiver's records to disk whenever the user changes data.
- (void) _handleSaveRequestNotification:(NSNotification*)notification {
    [[NSRunLoop currentRunLoop] performSelector:@selector(saveAction:) 
                                         target:self argument:self order:1000 modes:[NSArray arrayWithObject:NSDefaultRunLoopMode]];
}

//
// Persistent Data Methods
// 

//Returns the receiver's entity model.
- (id)entityModel
{
    if (_entityModel != nil) 
        return _entityModel;
    NSLog(@"Loading the entity model...");
    _entityModel = [self _loadEntityModelFromFile:[DataSource defaultEntityModelFileName]];

    return _entityModel;
}

// Loads the entity model for the first time. Used by the init method.
- (id)_loadEntityModelFromFile:(NSString *)fileName
{
    id resourcePath = [[NSBundle mainBundle] resourcePath];
    return [[EntityModel alloc] initWithContentsOfFile:[resourcePath stringByAppendingPathComponent:fileName]];
}

// Returns the receiver's data source. Attempts to load it from disk if it doesn't exist.
- (id)dataSource 
{
    if (_myDataSource != nil)
        return _myDataSource;

    NSLog(@"Creating data source...");
    _myDataSource = [[DataSource alloc] initWithModel:[self entityModel]];

    // Load the data source content (tables and records) from the backup file, if it exists
    NSString *applicationSupportFolder = [self _applicationSupportFolder];
    NSLog(@"Initializing with data from file %@", [applicationSupportFolder stringByAppendingPathComponent:[self fileName]]);
    NSURL *url = [NSURL fileURLWithPath:[applicationSupportFolder stringByAppendingPathComponent:[self fileName]]];
    if ([self _readFromURL:url] == NO) {
        NSLog(@"No backup file, requesting a refresh sync.");
        [self setPreferredSyncMode:ISyncSessionDriverModeRefresh];      
    }
    else {
        NSLog(@"Read in some data on init from backup file");
    }

    return _myDataSource;
}

// Returns the receiver's application support folder that contains the saved records.
- (NSString *)_applicationSupportFolder {
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

        if (![[NSFileManager defaultManager] fileExistsAtPath:applicationSupportFolder]) {
            [[NSFileManager defaultManager] createDirectoryAtPath:applicationSupportFolder withIntermediateDirectories:YES attributes:nil error:nil];
        }
    }
    return applicationSupportFolder;
}

// Returns the name of the folder contained in the User's Application Support folder.
- (NSString *)folderName
{
    return @"SyncExamples";
}

// Returns the file name that contains the receiver's records.
- (NSString *)fileName
{
    return @"com.mycompany.SimpleStickies.xml";
}

// Action method that saves the receiver's records to disk.
- (IBAction) saveAction:(id)sender {
    //NSLog(@"invoking saveAction:...");
    (void) [self _save];
}

// Action method that syncs the receiver's records.
- (IBAction) syncAction:(id)sender {
    (void) [syncDriver sync];
}



// NSApplication delegate method that saves the records before terminating the application.
- (NSApplicationTerminateReply)applicationShouldTerminate:(NSApplication *)sender {
    NSInteger reply = NSTerminateNow;

    if (_myDataSource != nil) {
        [self _save];
    }
    return reply;
}


// Deletion Support

// Returns the receiver's object that matches the specified record identifier. Typically, used to
// get a record that will be deleted.
- (id)_objectForRecordIdentifier:(NSString *)recordIdentifier
{
    NSEnumerator *entityEnumerator = [[[self dataSource] entityNames] objectEnumerator];
    NSString *entityName;
    id anObject = nil;

    entityName = [entityEnumerator nextObject];
    while ((anObject == nil) && (entityName != nil)){
        anObject = [[self dataSource] recordWithPrimaryKey:recordIdentifier forEntityName:entityName];
        entityName = [entityEnumerator nextObject];
    }
    return anObject;
}

// Deletes the record corresponding to the specified record identifier. Typically, invoked when pulling
// deletions from the sync engine.
- (BOOL)_deleteRecordForRecordIdentifier:(NSString *)recordIdentifier
{
    NSEnumerator *entityEnumerator = [[[self dataSource] entityNames] objectEnumerator];
    NSString *entityName;
    BOOL success = NO;

    entityName = [entityEnumerator nextObject];
    while ((success == NO) && (entityName != nil)){
        success = [[self dataSource] deleteRecordWithPrimaryKey:recordIdentifier forEntityName:entityName];
        entityName = [entityEnumerator nextObject];
    }
    return success;
}

// Private Syncing Methods

- (ISyncSessionDriverMode)preferredSyncMode
{
    return _preferredSyncMode;
}

- (void)setPreferredSyncMode:(ISyncSessionDriverMode)mode
{
    _preferredSyncMode = mode;
    return;
}

@end
```

[Next](DataSource.h.md)[Previous](AppDelegate.h.md)

