---
title: Foundation Release Notes for OS X v10.9
apple_id: TP40016592
resource_type: Release Note
platform: iOS|macOS
topic: General
technology: Foundation
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/releasenotes/Foundation/RN-Foundation-older-but-post-10.8/index.html
archived_at: '2026-07-18T02:50:31.051408Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Foundation Release Notes for OS X v10.9

Document Generated: 2013-11-08 18:55:29 -0800

OS X Release Notes Copyright © 2013 Apple Inc. All Rights Reserved.

#### Contents:

- [OS X 10.9 Release Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dkojsfvkfeqkokngecvcfirpugscbkbkekus7he3dklkukjau4u2mifkekrc7ircvgvc7ga)
- [Cocoa Foundation Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dkojsfvkfeqkokngecvcfirpugscbkbkekus7he3dklkukjau4u2mifkekrc7ircvgvc7ge)

### OS X 10.9 Release Notes

### Cocoa Foundation Framework

The Foundation Framework is a library of Objective-C classes that provide the infrastructure for object-based applications without graphical user interfaces. It is available on OS X and iOS.

You can find release notes for the Application Kit as well as some notes on general backward compatibility issues, version handling, etc, in [AppKit Release Notes (10.10 and Earlier).](https://developer.apple.com/library/mac/releasenotes/AppKit/RN-AppKitOlderNotes/index.html#X10_9Notes)

### Some of the major topics covered in this document:

- [Progress reporting and cancellation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dkojsfvkfeqkokngecvcfirpugscbkbkekus7he3dkljrgbptsudsn5txezltom)
- [App Nap](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dkojsfvkfeqkokngecvcfirpugscbkbkekus7he3dkljrgbptsqlqobhgc4a)
- [NSCalendar](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dkojsfvkfeqkokngecvcfirpugscbkbkekus7he3dkljrgbptsq3bnrsw4zdboi)
- [NSData Base64 support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dkojsfvkfeqkokngecvcfirpugscbkbkekus7he3dkljrgbptsqtbonstmna)
- [instancetype adoption](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dkojsfvkfeqkokngecvcfirpugscbkbkekus7he3dkljrgbpts2loon2gc3tdmv2hs4df)

### NSXPCConnection

In OS X 10.8 Mountain Lion, if a programmer error caused an exception when a message is received on a connection, the message would be dropped and no further action would be taken. As of OS X 10.9, NSXPCConnection will also automatically invalidate the connection. This ensures that the error handler will be invoked on the calling side with a ‘connection interrupted’ or ‘connection invalidated’ error.

The CPU and memory performance of sending large amounts of data over an NSXPCConnection is significantly increased.

NSXPCConnection will now clear the invalidation handler, interruption handler, and exported object after the connection is invalidated. This helps prevent accidental retain cycles, for example when an invalidation handler block captures the NSXPCConnection instance. NSXPCConnection will also stop retaining any additional exported objects.

### NSKeyedArchiver

In previous releases, archiving a string with the exact contents "$null" would cause it to be unarchived as a nil object. Archives with this string created on OS X 10.9 will unarchive correctly on OS X 10.9 and previous releases.

NSKeyedArchiver supports the NSSecureCoding feature added in OS X 10.8 Mountain Lion. The support is available on OS X 10.8 Mountain Lion and later. To use secure coding, create the NSKeyedUnarchiver or NSKeyedArchiver instance and use the new method. This code sample assumes ARC is enabled.

```
NSString *myString = @"Hello world";
NSMutableData *data = [NSMutableData data];
NSKeyedArchiver *archiver = [[NSKeyedArchiver alloc] initForWritingWithMutableData:data];
[archiver setRequiresSecureCoding:YES];
[archiver encodeObject:myString forKey:@"MyKey"];
[archiver finishEncoding];
```

```
// ...
```

```
NSData *dataToUnarchive = ...;
NSKeyedUnarchiver *unarchiver = [[NSKeyedUnarchiver alloc] initForReadingWithData:dataToUnarchive];
[unarchiver setRequiresSecureCoding:YES];
NSString *decodedString = [unarchiver decodeObjectOfClass:[NSString class] forKey:@"MyKey”];
```

If the class of the decoded object is not an NSString or NSString subclass, then the decodeObjectOfClass:forKey: method will thrown an exception.

In OS X 10.9, Foundation exports a new key: NSKeyedArchiveRootObjectKey. This is the root key used for archives created with the existing NSKeyedArchiver method +archivedDataWithRootObject: on all previous releases.

### NSBundle

Although the documentation allows NSBundle and CFBundle to insert new keys in a bundle’s Info.plist, doing so resulted in a common crash when the Info.plist dictionary was read on one thread and modified on another. NSBundle and CFBundle will no longer set any additional keys in the Info.plist dictionary, and applications are highly discouraged from attempting to modify the Info.plist dictionary returned from the -infoDictionary method.

### NSOperation and NSOperationQueue

The performance of -addOperationWithBlock:, -addOperation:, starting execution of operations, and starting execution of completion blocks is significantly faster.

### NSUserNotification

Calling -removeDeliveredNotification: and -removeAllDeliveredNotifications: will now remove notifications that are displayed.

A new property on NSUserNotification, -identifier, can be used to uniquely identify an individual notification even across separate launches of an application. If a notification is delivered with the same identifier as an existing notification, it will replace the preexisting notification. This can be used to update existing notifications.

NSUserNotification has a new property to specify the image shown in the content of a notification.

NSUserNotification allows for a ‘quick reply.’ The property responsePlaceholder can be used to set a placeholder string and the response can be retrieved from the response property.

### App Nap

App Nap is a new feature in OS X 10.9 which focuses system resources like CPU, I/O, and battery energy on the most important work done for the user. The system uses heuristics to determine when an application is doing important work, and when the work it is doing is not critical. These heuristics include (but are not limited to): visibility on screen, drawing activity, event processing, audio playback, foreground vs background, and application type.

When an application enters app nap mode, the system applies up to three kinds of effects: CPU priority lowering, I/O priority lowering, and timer throttling. CPU priority lowering will make an application lower priority than other apps, but not as low as most system daemons. I/O priority lowering will allow I/O to proceed as fast as possible, but allows high priority I/O to go first. This is designed to improve responsiveness in foreground applications that the user is actively interacting with. Timer throttling will reduce the frequency of most kinds of timers in an application. These combined effects provide a significant increase in battery life when an application is performing frequent unnecessary work.

The greatest benefit to the user comes when every application on their system is doing as little work as possible. Therefore, App Nap is an opt-out feature. The user can opt an application out of App Nap manually with a checkbox in the Finder “Get Info...” pane. Developers can temporarily opt an application out by bracketing user-initiated activities with new NSProcessInfo API. Please consider the power usage of your application before opting out of App Nap.

### App Nap - User Activities

Applications can help improve the result of the App Nap heuristics by using new API on NSProcessInfo to distinguish user-initiated activities from background or other maintenance work. This API is called automatically by AppKit for user event handling. You should call it when your application begins long-running or asynchronous work.

The new API has two forms. The first form is a begin/end pairing. Call -[NSProcessInfo beginActivityWithOptions:reason:] when your application begins a user initiated activity. The returned object should then passed into -[NSProcessInfo endActivity:] when the activity is finished.

The second form is block-based: -[NSProcessInfo performActivityWithOptions:reason:block:]. With this API, you specify the kind of activity and do the work inside the block. The method will run the block synchronously and automatically begin and end the activity around the block.

The options parameter describes the kind of activity your application is performing. If the work is user initiated, use NSActivityUserInitiated. If the work is background or other maintenance work then use NSActivityBackground. The options can also be used to prevent the system from entering idle system sleep or idle display sleep, with the NSActivityIdleSystemSleepDisabled and NSActivityIdleDisplaySleepDisabled constants. If your app is performing user initiated work that should not prevent the system from idle sleeping, then use NSActivityUserInitiated. You should be careful to choose the right kind of activity any time you use the new API. Preventing the computer from idling and going to sleep may result in an empty battery.

User initiated activities should be limited to work explicitly started by the user. Examples include exporting files or recording audio. Application-initiated activities like performing maintenance should either not use this API or use the NSActivityBackground type. There is new API in XPC for performing regular maintenance activities at more appropriate times (like when connected to A/C power). See <xpc/activity.h>.

### App Nap - Eligibility

Applications may be opted out of App Nap automatically based on their application type. Currently, only applications which can become the frontmost app are eligible. This behavior may change in the future. If you have an application which is LSUIElement or LSBackgroundOnly, you can opt your application in to App Nap by setting the NSSupportsAppNap key in your Info.plist to be a Boolean type with a value of YES. A value of NO is ignored for all applications.

If your application shows a user interface, then the system will use the application visibility and other heuristics to move your application in and out of App Nap automatically. If your app does background work at various times but shows no UI, it can use the User Activities API to inform the system when it is appropriate for it to be eligible for App Nap.

### App Nap - Debugging

There are many new tools available on the system to investigate the root cause of unexpected battery drain. Xcode now includes a view of the energy usage when running your application. Activity Monitor includes a new column that shows if your app is in App Nap or not, plus a synthesized “power score” which indicates the overall power usage of your app. The battery menu extra will now report apps using an excessive amount of power. The new command line tool timerfires (“man timerfires” for more information) can be used to investigate what timers your application has scheduled.

You should strive to have a power score of 0.0 and 0 idle wake ups. Remember that even a small amount of CPU usage can have a significant effect on battery life.

### Timer Tolerance

It is now possible to inform the system of the potential “tolerance” for NSTimer or CFRunLoopTimerRef objects. The tolerance is an allowable delay after the scheduled fire date of a timer. For example, a timer is setup with a fire date of 5 seconds from now, repeating every 7 seconds, and with a tolerance of 3 seconds. The timer may then fire between times 5 to 8s, 12 to 15s, 19 to 22s, 26 to 29s, and so forth.

Adding a tolerance allows the system to schedule timers in a significantly more power-friendly fashion. Most timers should have a tolerance set. A value of at least 10% of the interval is recommended, but the exact value will be application-specific.

### Progress Reporting and Cancellation

Mac OS X 10.9 and iOS 7.0 include a new mechanism for progress reporting. It allows code that does work to report the progress of that work, and user interface code to observe that progress so the progress can be presented to the user. Specifically, it can be used to show the user a progress bar and explanatory text, both updated properly as progress is made. It also allows work to be cancelled or paused by the user. This mechanism takes the form of a new class in the Foundation framework named NSProgress. Some design goals of this class were:

• Loose coupling. Code that does work can report the progress of that work regardless of what is observing it, or even whether it is being observed at all. To a lesser degree, code that observes progress and presents it to the user does not have to account for how the code that does the work is structured. Most of this goal is achieved simply by there being a single NSProgress class that can be used by a wide variety of progress reporters and observers.

• Composability. Code that does work can report progress without taking into account whether that work is actually just part of a larger operation whose total progress is what's really interesting to the user. To this end every NSProgress can have a single parent and multiple children. An NSProgress representing the total progress of an operation that's interesting to the user typically has no parent. If there are suboperations then their progress is represented by child NSProgresses. Reports of progress being made propagate from children to parents. Requests for cancellation propagate from parents to children. The subdivision of progress into a tree of NSProgresses enables solutions to problems like how the progress of work performed by disparate pieces of code should be used to calculate one overall progress number worth presenting to the user. For example, see -[NSProgress fractionCompleted], which returns a value that takes into account both the receiver and its children.

• Reusability. NSProgress is meant to be used by virtually all code that can link to the Foundation framework and that makes user-presentable progress. On Mac OS X, NSProgress includes a mechanism for publishing progress in one process and observing the progress in others.

• Usability. In many cases a substantial obstacle to using NSProgress would be arranging for code that does work to find the exact instance of NSProgress it should use to report its progress. The size of this obstacle depends on many things, like how layered your code is (would you have to pass the NSProgress as an argument through many layers of functions and methods?), how it is already being used by multiple projects (can you even add NSProgress parameters without breaking things?), how it is divided between framework and application code (does all of this code ship at the same time?), and so on. To help surmount this obstacle there is a notion of current progress, which is the instance of NSProgress that should be the parent for any new progress objects that represent a subdivision of work. You can set a progress object as the current progress, then call into a framework or other section of code. If it supports progress reporting, it can find the current progress object using the currentProgress method, attach its own children if required, and do its work.

The NSProgress.h header has more detailed information about the methods available.

### Reporting Progress

Using NSProgress in simple situations is not too complicated, though getting progress reporting and error handling right at the same time requires some care. Here's an example of doing that in a method that is supposed to be reusable regardless of whether the code that's invoking it will actually present its progress to the user, and even regardless of whether the work it's doing is just part of a larger operation.

```objc
- (BOOL)readFromData:(NSData *)data error:(NSError **)outError {
    // If there is already current progress, make a child of it to report progress about the part of the work that's being done by this method. In this example we simply use "bytes of input" as the unit of progress.
    NSUInteger length = [data length];
    NSProgress *progress = [NSProgress progressWithTotalUnitCount:length];
```

```
    // A loop that does something with each byte of data.
    NSError *error = nil;
    for (NSUInteger index = 0; index < length; index++) {
```

```
        // For the most part cancellation is just another kind of error to Cocoa. In real code there might be some cleanup to do here, but it should be just more of the same thing that you would do after any kind of error.
        if ([progress isCancelled]) {
            error = [NSError errorWithDomain:NSCocoaErrorDomain code:NSUserCancelledError userInfo:nil];
            break;
        }
```

```
        // Do some work with each byte. This code also might set the error to something, clean up, and break out of the loop.
        // ...
```

```
        // Report progress. We add one to the index so that the completed unit count will equal the total unit count at the end.
        [progress setCompletedUnitCount:(index + 1)];
```

```
    }
```

```
    // Finish up the error handling.
    if (error && outError) {
        *outError = error;
    }
    return error ? NO : YES;
}
```

If your method does work asynchronously, then you can create a new child object synchronously, capture it in a block, and update it from another thread or queue. Creating the child object first allows it to be attached to the currentProgress, if set by the caller of the method.

```objc
- (void)readAsynchronouslyFromData:(NSData *)data withCompletionHandler:(void (^)(NSError *error))completionHandler {
    NSUInteger length = [data length];
```

```
    // By creating the child progress before we move the work to another queue, we can capture the currentProgress object if set by the caller of this method.
    NSProgress *progress = [NSProgress progressWithTotalUnitCount:length];
```

```
    // We use a pre-existing NSOperationQueue here, but this approach will also apply if you use dispatch_async or another technique to move the work onto another thread or queue.
    NSOperationQueue *queue = _queue;
```

```
    [queue addOperationWithBlock:^{
        NSError *error = nil;
        for (NSUInteger index = 0; index < length; index++) {
            if ([progress isCancelled]) {
                error = [NSError errorWithDomain:NSCocoaErrorDomain code:NSUserCancelledError userInfo:nil];
                break;
            }
```

```
            // Do some work with each bytes, as before
            // ...
```

```
            // Report progress. We add one to the index so that the completed unit count will equal the total unit count at the end.
            [progress setCompletedUnitCount:(index + 1)];
        }
```

```
        completionHandler(error);
    }];
}
```


### Creating a Tree of Progress Objects

NSProgress is designed to promote loose coupling of its objects, to free each section of code from having to concern itself with the implementation details of code that it calls or code that calls it. This is accomplished by using the notion of a current progress to implicitly create a tree of progress objects.

For example, imagine that application code intends to read many data objects using the above methods. Assume that this example method is called when there is no current progress object and an array with 3 objects.

```objc
- (void)readAllData:(NSArray *)arrayOfData {
    NSProgress *overallProgress = [NSProgress progressWithTotalUnitCount:[arrayOfData count]];
    for (NSUInteger index = 0; index < [arrayOfData count]; index++) {
        [overallProgress becomeCurrentWithPendingUnitCount:1];
        [self readAsynchronouslyFromData:arrayOfData[index] withCompletionHandler:^(NSError *error) {
            // Perform error handling here
        }];
        [overallProgress resignCurrent];
    }
}
```

Because the readAsynchronously... method supports NSProgress, this will create a tree of objects. The overallProgress object will be the parent, and it will have 3 children. As each child NSProgress is updated, it will report its progress to the overallProgress, which will reflect the updates via Key-Value Observing and its fractionCompleted property. When each child asynchronously finishes its work, the overallProgress object will update its own completedUnitCount to include the pendingUnitCount that was assigned to that child. The calling code should not attempt to set completedUnitCount on the overallProgress object manually. If multiple children are attached to a parent progress during one period of becoming current, then the pending unit count will be divided equally among them. This can potentially cause the progress to move backwards (because it can not be known in advance how many children there will be), so if you have the choice, prefer to become current several times as this example method does.

It is likely that some methods you invoke do not yet support NSProgress. The class is designed so that the calling code does not need to know if the called code will create a child or not. For example, let’s assume the writeData method in the following example has not yet been updated to use NSProgress:

```objc
- (void)writeAllData:(NSArray *)arrayOfData {
    NSProgress *overallProgress = [NSProgress progressWithTotalUnitCount:[arrayOfData count]];
    for (NSUInteger index = 0; index < [arrayOfData count]; index++) {
        [overallProgress becomeCurrentWithPendingUnitCount:1];
        [self writeData:arrayOfData[index]];
        [overallProgress resignCurrent];
    }
}
```

In this case, NSProgress will determine that no children have been attached between the time that overallProgress became current and the time it resigned current. In this case NSProgress will simply assume that the pendingUnitCount assigned to the work in between the two calls has been completed and update its own completedUnitCount and fractionCompleted. The caller does not have to manually increment the completed unit count of the overallProgress.

### Observing Progress

For the most part, observing progress means creating an NSProgress and adding key-value observers of properties like "indeterminate," "fractionCompleted," and "localizedDescription" to it. These KVO notifications are sent out on the thread that changes the value of the property on the NSProgress object. If your code requires that the notification be posted on the main thread (for example, it updates your user interface in AppKit or UIKit), then it can either change the properties on on the main thread or the controller object can be the observer and assume responsibility for moving the UI work onto the main thread when it receives the KVO notification. This approach allows for maximum flexibility when deciding how to structure your code.

Here is an example of how one might implement a controller method that is invoked when the user chooses to open a file in our application:

```objc
- (void)openFromFileAtURL:(NSURL *)url {
```

```
    // This is a method for some sort of controller object that reads model objects from a file, presenting a progress panel if that takes too long, and presenting an error panel if that fails.
```

```
    // Certain properties of the NSProgress object may be interesting to display to the user. This controller object may use Key Value Observing to watch the values of those properties and update an AppKit or UIKit view. It is important to note that the KVO notifications will be posted on the thread that changes the value. If the UI view must be updated on the main thread, it is your responsibility to move that work to the main thread from your observeValueForKeyPath:ofObject:change:context: implementation.
```

```
    // You may have to make a decision about how useful it is to show a progress panel. For example, if the length of the operation is short enough it may make sense not to put up a panel only to immediately dismiss it. That human interface decision is encapsulated in the following fictional method implemented on this controller object.
    [self setUpProgressPanel];
```

```
    // The total unit count we use for this operation is arbitrary. What matters is that the counts of units we attribute to suboperations add up to it.
    _progress = [NSProgress progressWithTotalUnitCount:10];
```

```
    // It is important to remember not to block the main thread with the work. Otherwise the progress would not even be visible to the user.
    [_concurrentQueue addOperationWithBlock:^(void) {
```

```
        // To take advantage of NSData's progress reporting, make our progress the current one before we ask NSData to read the file. NSData will add a child NSProgress and report its reading progress through that. After a little bit of theoretical experimentation, we theoretically determined that in this example it's reasonable to call the actual reading of the file 20% of the work, and the parsing of the file and the creation of objects from it the other 80%. Some files, like those on network drives, take longer to read than others though. This is not an exact science.
        NSError *error = nil;
        BOOL didRead = NO;
        [_progress becomeCurrentWithPendingUnitCount:2];
        NSData *data = [NSData dataWithContentsOfURL:url options:0 error:&error];
        [_progress resignCurrent];
```

```
        // -readFromData:error:, shown above in "Reporting Progress," does 80% of the work here but its progress reporting is reusable in situations where it's some other fraction of the work. This approach is most useful when the code involved is spread all over a large code base built for reusability.
        [_progress becomeCurrentWithPendingUnitCount:8];
        didRead = [self readFromData:data error:&error];
        [_progress resignCurrent];
```

```
        // Get back on the main thread to do whatever it is this app does with the objects it just created.
        [[NSOperationQueue mainQueue] addOperationWithBlock:^(void) {
```

```
            // Success or failure, if our progress panel was presented then tear it down, and clean up.
            [self tearDownProgressPanel];
```

```
            _progress = nil;
```

```
            // If there was a failure, you may want to present it to the user.
            if (!didRead) {
                // You never have to tell the user they hit the Cancel button! On Mac OS X, AppKit's error presentation methods in NSResponder and its subclasses take care of not doing that for you. On iOS you are responsible for checking the kind of error yourself, which we show here.
                BOOL errorIsCocoa = [[error domain] isEqualToString:NSCocoaErrorDomain];
                if (!(errorIsCocoa && [error code] == NSUserCancelledError)) {
                    [self presentError:error];
                }
            }
```

```
        }];
    }];
}
```


### Reporting Progress to Other Processes and Observing Progress in Other Processes

There are a variety of reasons why a process might require the progress of work it's doing to be presented by another process. For example, in Mac OS X 10.9, the progress of Safari downloading a file is presented by Finder, on the file's icon, and by the Dock, on the containing folder's Dock item. To make that sort of thing possible, instances of NSProgress can be published.

The published NSProgress must have a value for NSProgressFileURLKey in its userInfo dictionary. The other process can then subscribe to the progress by invoking +addSubscriberForFileURL:withPublishingHandler:. The first argument is the file URL that the subscribing process wishes to observe and the second argument is a block which is invoked when the publishing process calls -publish. The block has an NSProgress argument, which is a proxy that can be observed like any other NSProgress. The KVO notifications for updates on this NSProgress proxy are sent on the main thread. The block passed to +addSubscriberForFileURL:withPublishingHander: and the block it returns (for use when the progress is unpublished) are also invoked on the main thread.

Not every process in a running OS X system is necessarily running with the same localization, so care must be taken that text about progress is localized in the process that will present it to the user. To help with this, NSProgress encapsulates the creation of text describing the progress made, formatted and localized such that it is suitable for presenting to the user. See the localizedDescription, localizedAdditionalDescription, and kind properties.

### NSProgresses Have User Info Dictionaries

NSProgress follows the pattern established by NSError, in which all localized text generated by the Foundation framework is derived, at least in part, from values found in a user info dictionary attached to each instance. See user info keys like NSProgressFileOperationKindKey. Entries in the user info dictionary also affect how an NSProgress is published, so see NSProgressFileURLKey for example too.

You can put entries in an NSProgress' user info dictionary for your own purposes. If the values are property list objects then they will be preserved when an NSProgress published by one process is observed by another.

### NSMetadata

NSMetadata now supports additional attributes and scopes as well as API that was formerly available only through the lower level MDQuery API. Availability of these new symbols and methods is indicated in the corresponding header.

Attributes that are defined in the MDQuery API are now also available as equivalents in NSMetadata. For example, NSMetadataItemRecipientAddressesKey is equivalent to kMDItemRecipientAddressesKey. The full set of attributes can be seen in the new header NSMetadataAttributes.h, which is included by NSMetadata.h. The string value of these symbols is identical to the lower level MDQuery equivalents.

Two additional scopes are available to complement the existing ones by limiting the scope to volumes which are indexed. NSMetadataQueryIndexedLocalComputerScope represents all indexed locally mounted volumes plus the user's home even if remote. NSMetadataQueryIndexedNetworkScope represents all indexed user-mounted remote volumes.

Additionally, NSMetadataQuery now supports scoping a search to an existing array of items, which can be specified as an arbitrary mixture of NSURLs and NSMetadataItems. -setSearchItems: is the setter, and -searchItems is the getter. The getter returns the same mixture as was set.

NSMetadataQuery now supports setting an operation queue on which query result notifications will occur. This makes it easier to synchronize query result processing with other related operations, such as updating the data model, and decouples it from the thread used to execute the query. -setOperationQueue: is the setter, and -operationQueue is the getter.

NSMetadataItem can now be created from a NSURL using -initWithURL:. This makes it easier to get NSMetadata attributes on arbitrary URLs without resorting to the lower-level APIs.

NSMetadataQuery now provides a simpler way of enumerating results using a block that automatically disables the query at the start of the iteration and re-enables it upon completion. -enumerateResultsUsingBlock: provides basic iteration, and -enumerateResultsWithOptions:usingBlock: provides additional options for concurrent or reverse iteration.

NSMetadataQuery notifications now provide a notification info dictionary. The new keys NSMetadataQueryUpdateAddedItemsKey, NSMetadataQueryUpdateChangedItemsKey, and NSMetadataQueryUpdateRemovedItemsKey provide access to corresponding arrays of NSMetadataItems that indicate which items have been added, changed, or removed since the last update.

### Bug Fixes in NSFilePresenter Messaging

File coordination allows you to register an NSFilePresenter for any file or directory, even one inside a file package. For example, when you double-click on an embedded image in TextEdit to open it in Preview, Preview registers an NSFilePresenter for the image file that is inside the TextEdit .rtfd file package. In this example you might expect that when TextEdit does a coordinated write of the file package as a whole, which it does during document saving, that Preview's NSFilePresenter would be sent a -relinquishPresentedItemToWriter:. Since file coordination's introduction in Mac OS 10.7 this has not been the case. This bug has been fixed in Mac OS 10.9.

An NSFilePresenter may signal an error when invoking the completion handler passed to -savePresentedItemChangesWithCompletionHandler: or -accommodatePresentedItemDeletionWithCompletionHandler:. Since file coordination’s introduction in Mac OS 10.7, however, doing so would often cause file coordination to not invoke the reacquisition block provided by your NSFilePresenter in its response to a previous invocation of -relinquishPresentedItemToReader: or -relinquishPresentedItemToWriter: for the same coordinated reading or writing. This bug has been fixed in Mac OS 10.9. Now your NSFilePresenter’s reacquisition blocks are always invoked, even when your NSFilePresenter has signaled a failure to save changes or accommodate deletion.

### Bug Fix in Key Value Observing (KVO)

Mac OS 10.8 and earlier had a bug in which KVO could send an -observeValueForKeyPath:ofObject:change:context: to an observer after it was no longer an observer, and in some cases even after the observer was deallocated. This could happen, for example, if an object had multiple observers of key paths, and the implementation of -observeValueForKeyPath:ofObject:change:context: for one observer attempted to removed one of the other observers. The removal would not take effect immediately enough to prevent the messaging of the other observer's zombie. This was possible even when just one thread was involved. This bug has been fixed in Mac OS 10.9.

### NSURL

The "file" URL scheme is defined so that no authority, an empty host, and "localhost" all mean the end-user's machine. To reduce memory use, file URL objects created with file system paths or from file system representation no longer include the host string "localhost".

This change also means -host no longer returns the string "localhost" for file URLs and will instead return nil.

-initFileURLWithFileSystemRepresentation:isDirectory:relativeToURL:, +fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:, -getFileSystemRepresentation:maxLength:. and -fileSystemRepresentation were added to allow easy conversion from file system representation to URL and URL to file system representation.

-removeCachedResourceValueForKey:, and -removeAllCachedResourceValues were added to allow removal of cached resource values from a URL object. -setTemporaryResourceValue:forKey: provides a way to set temporary resource values on a URL object.

URL objects created from URL strings where the URL string length was exactly 1 can no longer be created with characters not allowed in URL strings. This change affects CFURL's CFURLCreateWithString(), and the NSURL methods -initWithString:, -initWithString:relativeToURL:, +URLWithString:, and +URLWithString:relativeToURL:.

Added -stringByAddingPercentEncodingWithAllowedCharacters: and -stringByRemovingPercentEncoding. -stringByAddingPercentEncodingWithAllowedCharacters: is intended to percent-encode an URL component or subcomponent string, NOT the entire URL string. The predefined NSCharacters sets returned by +URLUserAllowedCharacterSet, +URLPasswordAllowedCharacterSet, +URLHostAllowedCharacterSet, +URLPathAllowedCharacterSet, +URLQueryAllowedCharacterSet, and +URLFragmentAllowedCharacterSet are intended to be passed to -stringByAddingPercentEncodingWithAllowedCharacters:.

The descriptions of long URLs with the data scheme may be truncated if the data URL is very large.

### NSURLComponents

NSURLComponents is a new class which encapsulates the components of a URL in an object-oriented manner. When a NSURLComponents is created from a NSURL or URL string, it provides IETF STD 66 (rfc3986) parsing of the URL string. When it is used to create a NSURL by providing the components and subcomponents which make up a URL (scheme, host, port, path, query and so on), the URL is created using IETF STD 66 (rfc3986) rules. NSURLComponents makes it easy to correctly parse an existing NSURL or URL string, makes it easy to create a correctly formed NSURL from URL components and makes it easy to create a new NSURL from an existing URL with modifications.

### Custom NSData Deallocator for No-Copy Buffers

NSData has long provided the ability to create instances that use a buffer provided by you, instead of copying its contents to an internally created buffer. The APIs to do this are -[NSData initWithBytesNoCopy:length:] and -[NSData initWithBytesNoCopy:length:freeWhenDone:]. One limitation of these APIs is that if you wish to defer deallocation of the no-copy buffer to the NSData instance, then you must use malloc(3) (or one if its variants), because NSData will use free(3).

To eliminate this limitation, NSData has added an API In OS X 10.9 that allows you to specify a custom method of deallocation via a block parameter. That API is -[NSData initWithBytesNoCopy:length:deallocator:].

There are some important things to be aware of when using this API. NSData will, when necessary, copy the deallocator block onto the heap. As a byproduct, any Objective-C object pointers that are captured in that block will be retained. In order to avoid any inadvertent retain cycles, you should avoid capturing pointers to any objects that may in turn retain the NSData object, including explicit references to self and implicit ones via instance variable referencing. To assist in this, the deallocator block has two parameters, the buffer's pointer its length. You should always use these values instead of trying to use references from outside the block.

### NSData API for Base 64 Encoding and Decoding

NSData has added an API in OS X 10.9 for encoding and decoding Base 64. The encoding algorithm can be configured to automatically insert line breaks with customizable line ending characters. The decoding algorithm by default will reject the entire input if it encounters any non-Base 64 characters (including whitespace), but there is an option available to make it more lenient. Depending on your needs, you can use one of the two variants of the encoding and decoding methods. One pair uses Base 64 encoded NSStrings and the other uses Base 64 encoded NSDatas.

If your application needs to target an operating system prior to OS X 10.9, you can use NSData's -initWithBase64Encoding: and -base64Encoding instead. These methods have existed since OS X 10.6, but were not exposed until OS X 10.9. These methods behave like the new methods, except -initWithBase64Encoding: will ignore unknown characters. When your application no longer needs to target an operation system prior to OS X 10.9, you should transition to the new methods.

### NSPurgeableData Thread Safety

Prior to OS X 10.9, NSPurgeableData was not fully thread-safe. If multiple threads were to invoke certain NSPurgeableData methods simultaneously, an exception or a crash could result. This has been resolved on OS X 10.9.

### NSString -stringByAppendingPathExtension: Behavior Change

Prior to OS X 10.9, if the receiver of NSString's -stringByAppendingPathExtension: method started with a tilde (~) character, the method would silently fail to append the extension and return the string unmodified. This behavior has been changed for applications linked against the 10.9 SDK to allow this method to behave as expected for home-relative paths (e.g. "~/user/path/to/file") and terminal file names (e.g. "~tempfile").

### NSFileProtectionKey Bug Fixed

Prior to iOS 7.0, when the device was locked, -[NSFileManager attributesOfItemAtPath:error:] would return a dictionary without NSFileProtectionKey. This has been fixed on iOS 7.0 so that the returned dictionary will report the proper NSFileProtectionKey value.

### NSFileManager Delegate Method Bug Fixed

Prior to OS X 10.9, delegate implementations of the NSFileManagerDelegate method -fileManager:shouldProceedAfterError:removingItemAtURL: would never be invoked. This has been fixed on OS X 10.9. To work around the problem, you can use the -fileManager:shouldProceedAfterError:removingItemAtPath: method instead. If implemented, that method will be invoked regardless of whether you invoked -removeItemAtPath:error: or -removeItemAtURL:error:.

### NSData Copying Behavior Change

Prior to OS X 10.9 and iOS 7.0, the +[NSData initWithData:] method would always return a new NSData instance when the existing NSData object was immutable (and not a custom subclass). Additionally, -[NSData copyWithZone:] would always retain the receiver under the same circumstances. These behaviors have changed for applications linked against the OS X 10.9 or iOS 7.0 SDKs.

For applications linked against the OS X 10.9 or iOS 7.0 SDKs, +dataWithData: now calls -copyWithZone: for immutable objects, allowing it to avoid unnecessary memory allocations. In addition, -[NSData copyWithZone:], when sent to an immutable object, will create a new NSData instance if the receiver was created with a "NoCopy" initializer and does not own its bytes buffer (meaning freeWhenDone was NO, or the deallocator block was nil). This latter change helps to avoid problems where an NSData object created via -copyWithZone: could end up with an invalid bytes pointer.

If you need to create a new NSData object that contains a copy of the contents of another NSData object, the only supported and guaranteed way to do ensure this has been to create it explicitly with something like [NSData dataWithBytes:[otherData bytes] length:[otherData length]].

### NSUserDefaults support for Security Application Groups (Sandboxing)

For applications that are part of a Security Application Group, the NSUserDefaults "suite" APIs (-initWithSuiteName:, -addSuiteNamed: and -removeSuiteNamed:) will operate on a suite shared by applications in the group and stored in the group container, if the suite identifier is the identifier of the group.

### Changes to NSUserDefaults "compatibility" keys (Mac)

The deprecated constant user defaults keys at the bottom of NSUserDefaults.h are no longer functional in applications built with the 10.9 or later SDK.

### Improved safety of NSUserDefaults values

Validation that values set in NSUserDefaults are valid Property List types has been made more thorough, and easier to debug. Crash logs from failing to do this will now include additional information noting the problem.

Collections returned from NSUserDefaults have always been documented to be immutable, but for applications built with the 10.9 or later SDK, actually are now. Attempting to mutate these collections on earlier releases led to extremely hard to diagnose bugs.

Nonsensical parameters to "Suite" methods on NSUserDefaults will now be rejected with a logged message. Currently the cases rejected are NSGlobalDomain and the bundle identifier of the main bundle.

### -[NSUserDefaults synchronize] and non-current-application domains (Mac)

In earlier releases, -[NSUserDefaults synchronize] synchronized only the current application's search list. In 10.9 and later it also synchronizes any other domains with un-synchronized changes.

### -[NSUserDefaults synchronize] is not generally useful (Mac)

You should only need to call -synchronize if a separate application will be reading the default that you just set, or if a process that does not use AppKit is terminating. In most applications neither of these should ever occur, and -synchronize should not be called. Note that prior to Mac OS X 10.8.4 there was a bug that caused AppKit to automatically synchronize slightly prematurely during application termination, so preferences set in response to windows closing while the application is terminating might not be saved; this has been fixed.

### dispatch_data_t -> NSData bridging

In 64-bit apps using either manual retain/release or ARC, dispatch_data_t can now be freely cast to NSData \*, though not vice versa. Note that one implication of this is that NSData objects created by Cocoa may now contain several discontiguous pieces of data. You can efficiently work with discontiguous ranges of data by using the new

```objc
- (void) enumerateByteRangesUsingBlock:(void (^)(const void *bytes, NSRange byteRange, BOOL *stop))block
```

API on NSData. This will be roughly the same speed as -bytes on a contiguous NSData, but avoid allocation and copying for a discontiguous one. Once a discontiguous NSData is compacted to a contiguous one (generally by calling -bytes, other NSData API will do discontiguous accesses), future accesses to the contiguous region will not require additional copying.

Various system APIs (in particular NSFileHandle) have been updated to use discontiguous data for improved performance, so it's best to structure your code to handle it unless it absolutely needs contiguous bytes.

### Empty NSData objects

Immutable NSData objects with a length of zero are now all a single object. This shouldn't matter for most applications, but relying on the == operator or methods like -indexOfObjectIdenticalTo: to distinguish between empty data objects will no longer work.

### Immutable NSData objects may be vm-backed

Starting in 10.9, NSData may choose to allocate its backing store with vm_allocate, rather than malloc. This should not impact behavior at all, but may be useful to know when examining your program with memory analysis tools (vmmap, Instruments, etc…). This also means that transferring NSData objects over NSXPCConnection can remap the pages rather than copying them, which can improve performance.

### NSData -copy, -copyWithZone: and -initWithData:

Methods that create copies of NSData have been improved to simply retain if it's safe to do so in more cases. This shouldn't matter for most applications, but relying on the == operator or methods like -indexOfObjectIdenticalTo: to distinguish between copied data objects will be less likely to work than in the past.

### plutil(1) plist editing

plutil(1) has four additional verbs: insert, replace, extract, and remove, which can be used to manipulate plist files. Run 'plutil -help' for more information.

### defaults(1) additions for dealing with arbitrary plist files

defaults(1) has two additional verbs: import and export. These can be used to add the contents of a property list file to a defaults domain, or save the contents of a defaults domain as a property list file.

### NSCalendar performance and thread-safety

Prior to 10.9, NSCalendar was not thread-safe, which required the +currentCalendar and -copy/-copyWithZone: methods to make time consuming full copies. This has been improved so that expensive copy operations will be deferred until the object is mutated. If you can avoid calling setter methods on NSCalendar instances, you'll likely get better performance.

### NSTask performance and thread-safety

NSTask is now thread-safe, and significantly more efficient, especially when launching tasks from host processes with very large VSIZEs and/or unusual memory mappings.

### NSDateFormatter and NSNumberFormatter thread-safety

When set to the modern formatter behavior (NSNumberFormatterBehavior10_4), NSNumberFormatter instances are now thread-safe. When set to the modern formatter behavior and using the non-fragile ABI (64 bit applications, on OSX), NSDateFormatter instances are also thread-safe.

### NSNetServices

A new includesPeerToPeer property was added to NSNetService and NSNetServiceBrowser to enable Bonjour discovery and connectivity over peer-to-peer Wi-Fi and Bluetooth.

A new NSNetServiceListenForConnections option was added to -publishWithOptions: that allows a published NSNetService to listen for incoming TCP connections. New connections are delivered in the form of NSStreams via the new -netService:didAcceptConnectionWithInputStream:outputStream: delegate method.

### NSURLSession

NSURLSession is a replacement API for NSURLConnection. It supports out-of-process downloads and uploads that notify your app on completion.  In addition, it provides a new way to configure your networking requests (NSURLRequest) so that they don't conflict with other networking code in your application.

### NSURLCredential

Use the new NSURLCredentialPersistenceSynchronizable persistence policy flag to sync the credential across devices through iCloud.

The new -[NSURLCredentialStorage removeCredential:forProtectionSpace:options:] API can be used to remove a credential that has a persistence policy of NSURLCredentialPersistenceSynchronizable.  If the passed in NSURLCredential object has a persistence policy of NSURLCredentialPersistenceSynchronizable, and if the options dictionary is present and includes the NSURLCredentialStorageRemoveSynchronizableCredentials key set to YES, the remove will attempt to delete the credential from iCloud, which will result in the credential being removed from all synchronized devices.  If the passed in NSURLCredential object has a persistence policy of NSURLCredentialPersistenceSynchronizable and no options dictionary is provided, or NSURLCredentialStorageRemoveSynchronizableCredentials does exist but is set to NO, then the call will fail.  Passing in an NSURLCredential with a persistence policy other than NSURLCredentialPersistenceSynchronizable is the same as calling the existing -[NSURLCredentialStorage removeCredential:forProtectionSpace:] method.

### NSPredicate, NSExpression, and NSSortDescriptor

NSPredicate, NSExpression, and NSSortDescriptor now support NSSecureCoding.

While it is safe to unarchive these objects using NSSecureCoding, it is not safe to blindly evaluate anything you get out of the archive, and as such, evaluation of securely decoded objects will be disabled. Any process receiving predicates/expressions/sortDescriptors should preflight the content of the archive by validating keypaths, selectors, etc contained within it to ensure no erroneous or malicious code will be executed. Once preflighting has been done, evaluation can be enabled by invoking allowEvaluation on the decoded object to recursively enable evaluation on the object graph rooted at the receiver.

### NSCalendar

In OS X 10.9, Foundation provides many new APIs to simplify calendrical calculations. This also helps to avoid mistakes from complex calendrical calculations. The new APIs are:

```objc
+ (id)calendarWithIdentifier:(NSString *)calendarIdentifierConstant;
- (void)getEra:(out NSInteger *)eraValuePointer year:(out NSInteger *)yearValuePointer
           month:(out NSInteger *)monthValuePointer day:(out NSInteger *)dayValuePointer fromDate:(NSDate *)date;
- (void)getEra:(out NSInteger *)eraValuePointer yearForWeekOfYear:(out NSInteger *)yearValuePointer
           weekOfYear:(out NSInteger *)weekValuePointer weekday:(out NSInteger *)weekdayValuePointer fromDate:(NSDate *)date;
- (void)getHour:(out NSInteger *)hourValuePointer minute:(out NSInteger *)minuteValuePointer second:(out NSInteger *)secondValuePointer
           nanosecond:(out NSInteger *)nanosecondValuePointer fromDate:(NSDate *)date;
- (NSInteger)component:(NSCalendarUnit)unit fromDate:(NSDate *)date;
- (NSDate *)dateWithEra:(NSInteger)eraValue year:(NSInteger)yearValue month:(NSInteger)monthValue day:(NSInteger)dayValue
           hour:(NSInteger)hourValue minute:(NSInteger)minuteValue second:(NSInteger)secondValue nanosecond:(NSInteger)nanosecondValue;
- (NSDate *)dateWithEra:(NSInteger)eraValue yearForWeekOfYear:(NSInteger)yearValue weekOfYear:(NSInteger)weekValue
           weekday:(NSInteger)weekdayValue hour:(NSInteger)hourValue minute:(NSInteger)minuteValue second:(NSInteger)secondValue nanosecond:(NSInteger)nanosecondValue;
- (NSDate *)startOfDayForDate:(NSDate *)date;
- (NSDateComponents *)componentsInTimeZone:(NSTimeZone *)timezone fromDate:(NSDate *)date;
- (NSComparisonResult)compareDate:(NSDate *)date1 toDate:(NSDate *)date2 toUnitGranularity:(NSCalendarUnit)unit;
- (BOOL)isDate:(NSDate *)date1 equalToDate:(NSDate *)date2 toUnitGranularity:(NSCalendarUnit)unit;
- (BOOL)isDate:(NSDate *)date1 inSameDayAsDate:(NSDate *)date2;
- (BOOL)isDateInToday:(NSDate *)date;
- (BOOL)isDateInYesterday:(NSDate *)date;
- (BOOL)isDateInTomorrow:(NSDate *)date;
- (BOOL)isDateInWeekend:(NSDate *)date;
- (BOOL)rangeOfWeekendStartDate:(out NSDate **)datep interval:(out NSTimeInterval *)tip containingDate:(NSDate *)date;
- (BOOL)nextWeekendStartDate:(out NSDate **)datep interval:(out NSTimeInterval *)tip options:(NSCalendarOptions)options afterDate:(NSDate *)date;
- (NSDateComponents *)components:(NSCalendarUnit)unitFlags fromDateComponents:(NSDateComponents *)startingDateComp
           toDateComponents:(NSDateComponents *)resultDateComp options:(NSCalendarOptions)options;
- (NSDate *)dateByAddingUnit:(NSCalendarUnit)unit value:(NSInteger)value toDate:(NSDate *)date options:(NSCalendarOptions)options;
- (void)enumerateDatesStartingAfterDate:(NSDate *)start matchingComponents:(NSDateComponents *)comps options:(NSCalendarOptions)opts
           usingBlock:(void (^)(NSDate *date, BOOL exactMatch, BOOL *stop))block;
- (NSDate *)nextDateAfterDate:(NSDate *)date matchingComponents:(NSDateComponents *)comps options:(NSCalendarOptions)options;
- (NSDate *)nextDateAfterDate:(NSDate *)date matchingUnit:(NSCalendarUnit)unit value:(NSInteger)value options:(NSCalendarOptions)options;
- (NSDate *)nextDateAfterDate:(NSDate *)date matchingHour:(NSInteger)hourValue minute:(NSInteger)minuteValue second:(NSInteger)secondValue options:(NSCalendarOptions)options;
- (NSDate *)dateBySettingUnit:(NSCalendarUnit)unit value:(NSInteger)v toDate:(NSDate *)date options:(NSCalendarOptions)opts;
- (NSDate *)dateBySettingHour:(NSInteger)h minute:(NSInteger)m second:(NSInteger)s toDate:(NSDate *)date options:(NSCalendarOptions)opts;
```

More details about these new APIs can be found in NSCalendar.h. The Date and Time Programming Guide also has more detail discussion about how these APIs would be used.

In addition to the new APIs, Foundation also exports a new notification: NSCalendarDayChangedNotification. This new notification is posted through [NSNotificationCenter defaultCenter] when the system day changes. Note that the notification is not posted to observers on any particular or defined thread or queue, so if you need the handling of the notification to do things that must only be done by a specific thread or queue, you need to then schedule that work in response to the notification.

CoreFoundation and Foundation are going to deprecate several existing calendar-related APIs in the next release. If the preprocessor macro NS_ENABLE_CALENDAR_DEPRECATIONS is set to a non-zero value in a project, then usage of those APIs will be indicated by the compiler.

### NSDateComponents

NSDateComponents has four new APIs for convenience:

```objc
- (void)setValue:(NSInteger)value forComponent:(NSCalendarUnit)unit;
- (NSInteger)valueForComponent:(NSCalendarUnit)unit;
- (BOOL)isValidDate;
- (BOOL)isValidDateInCalendar:(NSCalendar *)calendar;
```

More details about these new APIs can be found in NSCalendar.h.

### instancetype

Many new core APIs of Foundation use the 'instancetype' return type. These are class methods which return an instance of the receiving class, even if the receiving class is a subclass of the class which declares the method. Typically these methods would have returned 'id' in the past.

This information can help the compiler identify basic kinds of errors, like the NSArray type in the following line:

    NSArray \*set = [NSSet setWithObject:@"A String"];

But conversely, note that just because a method is a class method and returns an instance of the class, it does not necessarily follow that it will return an instance of an arbitrary subclass if the method is sent to the subclass. Thus, not all class methods which return instances are necessarily true candidates for the 'instancetype' return value.

### NSArray -firstObject

The -firstObject method returns the first object in the array, or nil if the array is empty. This method is available back to OS X 10.6 and iOS 4.0.

### NSString Errors

NSString out-of-bounds index and ranges now generate better error messages.

Formatting localized numbers with NSStrings using the "+" flag will now will no longer display an extra "+" for negative numbers. However, the "+" is not localized.

### NSScanner

NSScanner now provides the following API to scan unsigned long long values:

- (BOOL)scanUnsignedLongLong:(unsigned long long \*)value;

This works exactly like other existing NSScanner methods, including the caveats:

- it doesn't scan localized numbers or numbers with thousands separators

- returns YES on overflow, with a clamped result

### NSAttributedString

For applications linked against the 10.9 SDK or later, copying a standard instance of NSAttributedString now retains it instead.

### Localized Property List File

Many languages including English have grammatical rules for selecting a word form depending on contextual conditions such as the gender or plurality.  For example, it is common to manually implement the logic for selecting singular or plural forms in formatting localized strings.

```
NSString *localizedString;
NSUInteger numberOfItems; // assume the number of selected item is stored
```

```
if (numberOfItems == 1) { // single item
    localizedString = NSLocalizedString(@"A file is selected", @"Message displayed when showing a single file selection.");
} else { // multiple item
    localizedString = [NSString localizedStringWithFormat:NSLocalizedString(@"%d files are selected", @"Message displayed when showing multiple file selection."), numberOfItems];
}
```

The rule gets more complex when dealing with languages requiring the gender-based form selection and/or plural form condition. For languages such as Russian and Arabic with multiple plural forms, properly formatting by conditional logic like above becomes extremely hard to maintain.

To show the complexity, the following code snippet illustrates what would happen to support the Arabic plural logic for the same message selection logic shown above.

```
NSString *localizedString;
NSUInteger numberOfItems; // assume the number of selected item is stored
NSUInteger modValue = numberOfItems % 100;
```

```
if (numberOfItems == 0) { // no item
    localizedString = NSLocalizedString(@"No file is selected", @"Message displayed when showing no selection.");
} else if (numberOfItems == 1) { // single item
    localizedString = NSLocalizedString(@"A file is selected", @"Message displayed when showing a single file selection.");
} else if (numberOfItems == 2) { // dual items
    localizedString = NSLocalizedString(@"Two files are selected", @"Message displayed when showing two files selected.");
} else if ((modValue >= 3) && (modValue <= 10)) { // paucal items
    localizedString = [NSString localizedStringWithFormat:NSLocalizedString(@"A few files (%d items) are selected", @"Message displayed when showing paucal files selected."), numberOfItems];
} else { // multiple items
    localizedString = [NSString localizedStringWithFormat:NSLocalizedString(@"%d files are selected", @"Message displayed when showing multiple file selection."), numberOfItems];
}
```

Further complicating the issue, the logic for choosing from multiple plural forms varies from locale to locale.

In order to solve this issue, the localizers need to be able to specify more sophisticated data structure than the simple key-value pair from the strings file format. There is a new file format with ".stringsdict" suffix introduced. -[NSBundle localizedStringForKey:value:table:] now accesses two files: .stringsdict and .strings.  It queries the .stringsdict file first, then, .strings file. Note that if a .stringsdict file is provided, a .strings file with the same name also needs to be there, even if empty.

The .stringsdict file contains the original key (i.e. @"%d files are selected") with the value as an arbitrary property list (mostly dictionary or string). When the value is a dictionary, it must contain a key for the localized format string value and its format specifier configuration dictionaries.

When -localizedStringForKey:value:table: returns an NSString instantiated from an entry in a .stringsdict file, the string object carries the additional information stored in the file.  The information can be retained and copied across -copy and -mutableCopy.  It gets discarded when a mutable copy gets mutated.

### NSString %@ format specifier enhancement

For representing a new dictionary based formatting rule, %@ format directive is enhanced with the alternate form flag '#'.

The extended %@ format syntax is:

```
%[n$]#[FLAGS][FIELD WIDTH][.PRECISION]@<CONFIGURATION KEY>@
```

A configuration key between two @s is used to query an item in the external format configuration dictionary.  Only characters in [a-zA-Z_0-9] are allowed.  The name space is independent for each format string.

For example, @"%d files are selected" can become @"%#@num_files_are@ selected" referencing an item for "num_files_are" in the external format configuration dictionary.

### The format specifier configuration dictionary

The format specifier configuration dictionary contains key-value pairs of configuration data.  Each value is represented by itself a dictionary.

There are a couple of dictionary keys predefined.

- NSStringFormatSpecTypeKey

This key defines the type of format specifier configuration.  This is a mandatory key.  Currently we're supporting NSStringPluralRuleType and NSStringGenderRuleType.  The rest of dictionary contents is determined by the type.

- NSStringFormatValueTypeKey

This is an optional key describing the original argument type on the stack.  The value is the original format specifier.  For mapping @"%d files are selected" to @"%#@num_files_are@ selected", the configuration dictionary for num_files_are should contain an entry "NSStringFormatValueTypeKey = d".  If absent, %@ is assumed.

The NSStringPluralRuleType configuration maps the argument number into a plural choice using the Unicode CLDR Plural mapping rule.  The configuration dictionary could contain keys for "zero", "one", "two", "few", "many", and "others".  They correspond to the Unicode CLDR Plural supplement data items.  The value for "others" is mandatory.  If "zero" is present, the value is used for mapping the argument value zero regardless of what CLDR rule specifies for the numeric value.  If a mapping key is absent, the value for "others" is used as the fallback.

The NSStringGenderRuleType configuration maps the argument number to a variant form.  As with most other gender variation handling systems including CLDR, we're assigning index numbers to genders.  For example, male is 0, female is 1, and neutral is 2.  Since the number of gender types varies greatly from languages to languages (i.e. Polish has 5).  The key for this configuration info type is represented by a positive integer number.  The key 0 is mandatory and used for absence of other gender keys.

The mapped value itself can be a format string.  The format string is evaluated with the value used to select it.

Sample configuration information for the selected file example.

```
@"%d files are selected" = @"%#@num_files_are@ selected" // localized string dynamically substitute "%d files are"
```

The configuration dict is:

```
{
    "NSStringFormatSpecTypeKey" = "NSStringPluralRuleType"; // plural type
    "NSStringFormatValueTypeKey" = "d"; // int argument
```

```
    "zero" = "No file is";
    "one" = "A file is";
    "other" = "%d files are";
}
```

Since there are cases where the condition of a plural/gender rule substitution is depending on another substitution (i.e. French articles like le, la, and les), the recursive formatting capability is essential for this feature.  For example, with @"%d in %d files are selected", giving localizers options to substitute the whole sentence depending on the number of total files is necessary.  We're allowing the recursive formatting by applying the entire argument list to each substituted format specifier.

```
@"%d in %d files are selected" = @"%2$#@d_in_d_files_are_selected@"
```

The configuration dictionary can contain

```
"d_in_d_files_are_selected" = {
    "NSStringFormatSpecTypeKey" = "NSStringPluralRuleType"; // plural type
    "NSStringFormatValueTypeKey" = "d"; // int argument
```

```
    "zero" = "There is no file";
    "one" = "There is a file, and %1$#@it_is_selected@";
    "other" = "%1$d in %2$d files are selected";
};
```

```
"it_is_selected" = {
    "NSStringFormatSpecTypeKey" = "NSStringPluralRuleType"; // plural type
    "NSStringFormatValueTypeKey" = "d"; // int argument
```

```
    "zero" = "it is not selected";
    "other" = "it is selected";
};
```

The results are "There is no file" for 0 files, "there is a file, and it is not selected" for 0 in 1, and "3 in 5 files are selected" for 3 in 5.

This is a sample stringsdict contents:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>%d files are selected</key>
    <dict>
        <key>NSStringLocalizedFormatKey</key>
        <string>%#@num_files_are@ selected</string>
        <key>num_files_are</key>
        <dict>
            <key>NSStringFormatSpecTypeKey</key>
            <string>NSStringPluralRuleType</string>
            <key>NSStringFormatValueTypeKey</key>
            <string>d</string>
            <key>zero</key>
            <string>No file is</string>
            <key>one</key>
            <string>A file is</string>
            <key>other</key>
            <string>%d files are</string>
        </dict>
    </dict>
</dict>
</plist>
```
