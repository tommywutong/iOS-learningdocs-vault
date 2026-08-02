---
title: Scripting Bridge Release Note
apple_id: TP40004741
resource_type: Release Note
platform: macOS
topic: Interapplication Communication
technology: ScriptingBridge
published: '2009-05-27'
source_url: https://developer.apple.com/library/archive/releasenotes/ScriptingAutomation/RN-ScriptingBridge/index.html
archived_at: '2026-07-18T02:59:02.367010Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Scripting Bridge Release Notes

This document covers new and updated information for Scripting Bridge. Conceptual and reference information formerly in this document has been moved to _[Scripting Bridge Programming Guide](../../documentation/Cocoa/Scripting%20Bridge%20Programming%20Guide/Introduction%20to%20Scripting%20Bridge%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbu)_.

#### Contents:

- [10.6 Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [10.5.6 Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [Thread Safety](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)

### 10.6 Changes

### Error Handling

Instance methods in Scripting Bridge send Apple events to the target application, which may fail for a variety of different reasons, many of them not detectable beforehand. In previous versions, Scripting Bridge handled failed events by calling the delegate method [eventDidFail:withError:](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate/1424011-eventdidfail), the default implementation of which threw an exception. This reflected AppleScript’s usage, but in Cocoa, exceptions are reserved for programming errors, not run-time errors. Therefore, OS X v10.6 changes the error handling protocol. When an event fails, an [NSError](https://developer.apple.com/documentation/foundation/nserror) object will be attached to the SBObject instance that sent the event, which you can get using the new `-lastError` method:

```objc
@interface SBObject (ErrorHandling10_6)
- (NSError *) lastError;
@end
```

If the program set a delegate object, it will be called after setting `lastError`, and the originating method will return `nil` or `0` depending on its return type.

Because the error is only attached to the instance that sent the event, chained expressions will need to be rewritten if you want to report errors. Consider attempting to get the name of the current track in iTunes, which will fail if there is no current track. You could write this naively, ignoring the error:

```
iTunes = [SBApplication applicationWithBundleIdentifier:@"com.apple.iTunes"];
name = [[iTunes currentTrack] name];
if (name) NSLog(@"current track is %@", name);
```

This works, because `name` will return `nil` on failure, but the error has been effectively lost, because it was attached to the temporary object returned by `[iTunes currentTrack]`. To get at the error, you would have to rewrite the code slightly to hold a reference to the intermediate SBObject, shown here using `track`:

```
iTunes = [SBApplication applicationWithBundleIdentifier:@"com.apple.iTunes"];
track = [iTunes currentTrack];
name = [track name];
if (name)
    NSLog(@"current track is %@", name);
else {
    NSError *error = [track lastError];
    NSLog(@"couldn't get current track because %@", [error localizedDescription]);
}
```


### Predicate Handling

`-[SBElementArray filteredArrayUsingPredicate:]` does not directly support everything `NSPredicate` can do, because it must turn the predicate into an Apple event, which has fewer features. In previous versions, if it received a predicate that could not be represented as an Apple event, it would fall back to `-[NSArray filteredArrayUsingPredicate:]`. However, this gave inconsistent results: depending on the predicate, it might return either an `NSArray` or an `SBElementArray`, and the performance could be wildly different.

In v10.6, `-[SBElementArray filteredArrayUsingPredicate:]` will fail with an exception if given a predicate it cannot handle. If you cannot rewrite the predicate without the unsupported bits, you can emulate the old behavior by using `-get` to get an NSArray, and then use `-filteredArrayUsingPredicate:` on that:

```
filtered = [[SomeApp someObjects] get] filteredArrayUsingPredicate:complexPredicate];
```

For best performance, separate out the parts that `SBElementArray` can handle into another predicate and filter that first, so the second predicate will have to examine fewer objects:

```
firstPass = [[[SomeApp someObjects] filteredArrayUsingPredicate:simpleBits] get];
filtered = [firstPass filteredArrayUsingPredicate:complexBits];
```

For compatibility, applications linked on OS X v10.5 will still get the old behavior. For scripts using Scripting Bridge via an Objective-C bridge such as PyObjC or RubyCocoa, the relevant “application” is the interpreter. If the interpreter was built on OS X v10.6, as `python`(1) and `ruby`(1) are, then the script gets the new behavior.

### Bug Fixes and Enhancements

`NSDictionary`-`AERecord` translation now handles user-defined keys (as opposed to keys defined by the application scripting interface). [5525649]

`-[SBElementArray addObject:]` now works better with non-Cocoa applications. [5585347]

A number of memory leaks have been fixed. [5856221]

Scripting Bridge no longer prints warnings about malformed scripting interfaces when creating an `SBApplication` object. [5964420]

`sdp`(1) has improved error messages, and flags warning messages as warnings. [5649633]

### 10.5.6 Changes

Application-specific methods that return `BOOL` now work correctly on PowerPC systems. [5525649]

### Thread Safety

Using multiple threads with Scripting Bridge may give perceived or actual performance advantages. In particular, a remote application may take a while to respond to a message, and your application should stay responsive to user input while it waits. Scripting Bridge may be used with multiple threads, given a few guidelines.

- _An SBObject may do work on any thread._

  An SBObject may be invoked on any thread, main or background. Apple events sent from an SBObject are set up with a per-thread port, so Apple events on different threads will not block each other.
- _An SBObject must do work on only one thread at a time._

  Any single SBObject instance, including an SBApplication instance, must be used from at most one thread at a time. If you wish to share a single instance between threads, you must set up exclusive access using locks. Two object instances that refer to the same remote application object, such as a particular document in TextEdit, are still considered distinct for purposes of threading, but see below.
- _The target application may not be multi-threaded._

  Just because your application is multi-threaded does not mean that the target application is. In general, assume that a target application can handle only one message at a time. Also, trying to manipulate the same remote object, such as a particular document, from more than one thread at once is subject to the typical contention and race condition issues. Your application is responsible for doing any applicable locking.

This information applies to all versions of Scripting Bridge.
