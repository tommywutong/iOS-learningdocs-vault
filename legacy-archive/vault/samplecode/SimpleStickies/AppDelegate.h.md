---
title: SimpleStickies
apple_id: DTS40009051
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_SimpleStickies/Listings/AppDelegate_h.html
archived_at: '2026-07-18T03:25:54.160213Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleStickies](SimpleStickies.md)


[Next](AppDelegate.m.md)[Previous](main.m.md)

# AppDelegate.h

```objc
/*

 File: AppDelegate.h

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

#import <Cocoa/Cocoa.h>
#import <SyncServices/SyncServices.h>

@interface AppDelegate : NSObject <ISyncSessionDriverDataSource>
{
    __weak IBOutlet NSProgressIndicator* _progressIndicator;
    __strong ISyncSessionDriver *syncDriver;
    __strong id _recordTransformer; 
    __strong id _myDataSource;
    __strong id _entityModel;
    __strong id notesController;
    __strong id _entityAnchors;

    ISyncSessionDriverMode _preferredSyncMode;
}

- (id)dataSource;
- (id)entityModel;
- (IBAction)saveAction:sender;
- (IBAction)syncAction:sender;
- (NSString *)fileName;
- (NSString *)folderName;
- (NSProgressIndicator*) progressIndicator;

/*** ISyncSessionDriverDataSource Methods ***/

// Getting Client Information
- (NSString *)clientIdentifier;
- (NSURL *)clientDescriptionURL;
- (NSArray *)schemaBundleURLs;
- (NSArray *)entityNamesToSync;

// Negotiating Phase
- (ISyncSessionDriverMode)preferredSyncModeForEntityName:(NSString *)entity;

// Pushing Phase
- (NSDictionary *)recordsForEntityName:(NSString *)entityName moreComing:(BOOL *)moreComing error:(NSError **)outError;
- (NSDictionary *)changedRecordsForEntityName:(NSString *)entityName moreComing:(BOOL *)moreComing error:(NSError **)outError;
- (NSArray *)identifiersForRecordsToDeleteForEntityName:(NSString *)entityName moreComing:(BOOL *)moreComing error:(NSError **)outError;

// Pulling Phase
- (ISyncSessionDriverChangeResult)applyChange:(ISyncChange *)change 
                                forEntityName:(NSString *)entityName 
                     remappedRecordIdentifier:(NSString **)outRecordIdentifier 
                              formattedRecord:(NSDictionary **)outRecord 
                                        error:(NSError **)outError;
- (BOOL)deleteObjectForRecordIdentifier:(NSString *)recordIdentifier forEntityName:(NSString *)entityName;
- (BOOL)deleteAllRecordsForEntityName:(NSString *)entityName error:(NSError **)outError;

/*** ISyncSessionDriver Delegate Methods ***/

- (BOOL)sessionDriver:(ISyncSessionDriver *)sender didRegisterClientAndReturnError:(NSError **)outError;
- (void)sessionDriverDidFinishSession:(ISyncSessionDriver *)sender;
- (void)sessionDriverDidCancelSession:(ISyncSessionDriver *)sender;

@end
```

[Next](AppDelegate.m.md)[Previous](main.m.md)

