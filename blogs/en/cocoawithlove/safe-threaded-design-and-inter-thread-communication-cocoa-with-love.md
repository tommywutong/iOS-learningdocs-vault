---
title: 'Safe, threaded design and inter-thread communication | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/08/safe-threaded-design-and-inter-thread.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:ec186dd0e5e7553a'
translated: false
---

> 原文：[Safe, threaded design and inter-thread communication | Cocoa with Love](https://www.cocoawithlove.com/2009/08/safe-threaded-design-and-inter-thread.html)　·　Cocoa with Love (Matt Gallagher)

The Foundation framework provides all the tools you need for inter-thread communication — without needing to handling locks and synchronization yourself. I'll show you Cocoa's tools for inter-thread communication, notifications and easy synchronization — including far simpler code for posting NSNotifications on the main thread than the Cocoa documentation suggests.

## Introduction

Multi-threaded code has a reputation for being difficult to write and prone to deadlocks, race conditions and unpredictable behaviors.

While this remains true if you are forced to handle locking yourself, Foundation provides all the tools you require to manage typical multi-threaded situations so that you can avoid the risks of locks entirely.

This post comes from my shock at Apple's suggestion (in their [Delivering Notifications To Particular Threads](http://developer.apple.com/documentation/Cocoa/Conceptual/Notifications/Articles/Threading.html)) that something as simple as sending an `NSNotification` from one thread to another should take dozens of lines of code and a dedicated class for the purpose.

It isn't that difficult. Sending data between threads (including notifications) is a one line job.

## Rules for safe simple threading

Simple thread safety in Cocoa requires just two rules:

1. list of explicity thread-safe classes

  ).
2. and both the receiver and the "object" should belong (or be handed over) to the target thread.

The only limitation with this approach is that any thread that _receives_ communication must be running an `NSRunLoop`. Since communication after construction is normally one-way (from worker thread back to the main thread) this is rarely a significant limitation. Other threads can invoke the `[NSRunLoop currentRunLoop]`'s `runMode:beforeDate` to process the run loop and receive messages.

A lot of multi-threaded code does not follow these rules. A lot of multi-threaded code uses a careful system of locks, synchronized sections, volatile variables and atomic operations to allow single objects to be accessed simultaneously from multiple threads. This does work but generally speaking: you don't want to design code this way. It's tricky, confusing and prone to errors. To illustrate, you can have a look at how many changes I had to make to my AudioStreamer code between the [first](https://www.cocoawithlove.com/2008/09/streaming-and-playing-live-mp3-stream.html) and [second](https://www.cocoawithlove.com/2009/06/revisiting-old-post-streaming-and.html) versions — rock-solid, manually-locked code is annoying and difficult to write.

Instead, as much as possible, you should write your code to keep all objects compartmentalized to individual threads and to restrict communication between threads to method invocations using `performSelector:onThread:withObject:waitUntilDone:`. To explain how this works, I'll show a simple example of something running in a separate thread and show how it can perform all its inter-thread communication using existing Foundation methods to automatically handle all thread safety issues.

## Scenario: writing to a network NSFileHandle in a worker thread

One of the simplest situations where you may want multithreading is writing to a network socket's `NSFileHandle`. This is a synchronous operation (blocks until complete) so it is a good idea to perform this in a worker thread so that the main thread of your program can remain responsive.

The following class is an `NSOperation` subclass. If you don't know about `NSOperation`, it's an object that you can add to an `NSOperationQueue` to have the object's `main` method run in a separate thread (see [Apple's Threading Programming Guide](http://developer.apple.com/documentation/Cocoa/Conceptual/Multithreading/OperationObjects/OperationObjects.html)). While `NSThread`'s `detachNewThreadSelector:toTarget:withObject:` is the best way to launch a single worker thread, `NSOperation`s are the best way to run a series threaded tasks (or has been since [serious bugs in it were fixed in 10.5.7](http://www.mikeash.com/?page=pyblog/use-nsoperationqueue.html)).

This class' init method takes an `NSFileHandle` and an `NSData` object on construction and writes the data to the file handle in its `main` method.

```objc
@interface FileWriteOperation : NSOperation
{
    NSFileHandle *fileHandle;
    NSData *data;
}
@end

@implementation FileWriteOperation

- (id)initWithFileHandle:(NSFileHandle *)aFileHandle data:(NSData *)aData
{
    self = [super init];
    if (self != nil)
    {
        fileHandle = [aFileHandle retain];
        data = [aData retain];
    }
    return self;
}

- (void)main
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    @try
    {
        [fileHandle writeData:data];
        // At this point, the write has succeeded
    }
    @catch (NSException *e)
    {
        // At this point, the write has failed
    }
    @finally
    {
        [pool drain];
    }
}

- (void)dealloc
{
    [fileHandle closeFile];
    [fileHandle release];
    [data release];
    [super dealloc];
}

@end
```

The `NSOperation` is created and its thread is launched as follows:

```objc
// Assume the operationQueue, fileHandle and fileData already exist
[operationQueue
    addOperation:
        [[[FileWriteOperation alloc]
            initWithFileHandle:fileHandle
            data:fileData]
        autorelease]];
```

To follow the first rule of thread-safety, after the `FileWriteOperation` is constructed, the `fileHandle` value passed into its `initWithFileHandle:data:` method cannot be used again outside the `NSOperationQueue`'s worker thread.

## Communicating success or failure

The above class works but doesn't have any way of communicating the result. What would be good is if we could send a `writeFinishedWithSuccess:YES` at the "`write has succeeded`" line and a `writeFinishedWithSuccess:NO` at the "`write has failed`" line.

The unsafe way of doing this is to invoke a method on another object sending the result:

```objc
    [responseHandler writeFinishedWithSuccess:YES]; // BAD!!
```

If `responseHandle` belongs to another thread, then this method could cause any number of race conditions and other multi-threading issues.

The solution though is exceptionally simple:

```objc
    [responseHandler
        performSelectorOnMainThread:@selector(writeFinishedWithSuccess:)
        withObject:[NSNumber numberWithBool:YES]
        waitUntilDone:NO];
```

This assumes that `responseHandler` is a nominally "main thread" object. You can use the `performSelector:onThread:withObject:waitUntilDone:` method and specify a different thread if you need to send the response elsewhere.

You'll notice that the parameter has to be an object in this case (`[NSNumber numberWithBool:YES]` instead of simply `YES`) and any parameter that you pass to another thread should not be used again in the current thread.

## Delivering Notifications To Particular Threads

Of course, the `FileWriteOperation` class shown above doesn't have a `responseHandle` object that it can notify when it is done, so I'd rather use an `NSNotification` sent to the `NSNotificationCenter` and if any object wants to receive the notification, it can.

The `NSNotificationCenter` itself is thread-safe but it delivers the notifications on the thread in which you invoke `postNotification:` so if you expect the observers of that notification to belong to a different thread, you've just broken those objects' thread safety.

Normally it is a good idea to deliver all notifications on the main thread. We can do this as follows:

```objc
// Line of code in some method of some class...
[[self class]
    performSelectorOnMainThread:@selector(postNotification:)
    withObject:
        [NSNotification
            notificationWithName:@"FileWriteOperationSucceeded"
            object:self]];

+ (void)postNotification:(NSNotification *)aNotification
{
    [[NSNotificationCenter defaultCenter] postNofication:aNotification];
}
```

Notice that we don't call `+[NSNotificationCenter defaultCenter]` until we're on the main thread. If we call it on the other thread, it will return the notification center for that other thread.

Some classes follow a different behavior of delivering notifications to the thread on which they were constructed (not necessarily the main thread). To follow this behavior, simply save the `[NSThread currentThread]` on construction and perform the `postNotification:` selector on that thread.

You may have noticed that the notification is passing "`self`" from one thread to another — breaking the thread ownership of "`self`". This is only really safe in one of the following cases:

- — the parameter will never be used on this thread again.

  In this case, if "

  " is complete on the worker thread (for example at the bottom of the

  method shown above). In this case, the object is passing itself back to the other thread.
- — if the class or specific methods are guaranteed to be thread-safe.

  In this case, if the only methods invoked on

  are

  ,

  and the default pointer comparison

  method (these are the methods invoked when removing from an

  ). These are guaranteed thread-safe methods.

If neither of these are true then you can't pass `self` (or any other parameter) safely between threads.

## Conclusion

The purpose of this article is to communicate two ideas:

- Carefully locking and synchronizing makes programming hard but if you design your objects to be used on only one thread at a time, then they are thread-safe without the need for locks or synchronzation (if needed, split your objects into components for separate threads).
- Use inter-thread communication to keep objects in separate threads up-to-date with each other. In Cocoa, this is very simple but you do need to ensure that all parameters you pass are either thread-safe objects or handover objects.

Apple's [Delivering Notifications To Particular Threads](http://developer.apple.com/documentation/Cocoa/Conceptual/Notifications/Articles/Threading.html) code is woefully out of date. I would be happy to see it completely changed — you should never need to implement something so complex just to deliver notifications to another thread.

Of couse, there are always situations where you can't run an `NSRunLoop` to process `performSelector:onThread:withObject:waitUntilDone:` messages. There are also situations where you feel that one of your object s must be multi-threaded (rather than single thread exclusive). Either of these cases requires will require a synchronized or locked solution but my recommendation is to try to find an `NSRunLoop` and thread exclusive solution first as these are significantly easier to manage and prone to fewer potential problems.
