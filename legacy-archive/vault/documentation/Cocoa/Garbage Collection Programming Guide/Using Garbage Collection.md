---
title: Garbage Collection Programming Guide
apple_id: TP40002431
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/GarbageCollection/Articles/gcUsing.html
archived_at: '2026-07-15T07:16:01.008310Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Garbage Collection Programming Guide](Introduction%20to%20Garbage%20Collection.md)


[Next](Implementing%20a%20finalize%20Method.md)[Previous](Architecture.md)

# Using Garbage Collection

This article describes some of the design patterns and features you can take advantage of when you use garbage collection, and some of subtleties you need to be aware of.

A problem when using manually reference counting is that it is possible to create retain cycles. If two objects retain each other, and you do not have a reference to either, then they will remain valid for the lifetime of your application—constituting a memory leak (see, for example, Object Ownership and Disposal).

With garbage collection, retain cycles are not a problem. Since the collector traces strong reference from root objects, even if two objects have strong references to each other they can be collected if neither has a reference from a root object.

Sometimes you need a reference to an object but do not want to form a strong relationship to that object to prevent its being collected if it has no other references. For example, a notification center should not form strong relationships to registered observers, otherwise it artificially prolongs the lifetime of those objects indefinitely. You can specify a weak reference—one that the collector does not follow—using the keyword `__weak`.

[NSMapTable](https://developer.apple.com/documentation/foundation/nsmaptable), [NSHashTable](https://developer.apple.com/documentation/foundation/nshashtable), and [NSPointerArray](https://developer.apple.com/documentation/foundation/nspointerarray) provide collection objects that have the option of maintaining zeroing weak references to their elements. If an element is collected, the reference from the collection object is simply removed.

There are several Cocoa methods and Core Foundation functions that have as one parameter an opaque pointer (`void *`). In a garbage collected environment, the general policy is that the lifetime of any object passed as a `void *` should be either managed by the callbacks or known to be safe.

For example, in Cocoa, there are a several “asynchronous” methods that take a delegate object, a selector, and a context and send the selector to the delegate object at some later point passing the context as an argument. These APIs typically declare the context as a `void *` and represent it as such in their internal state. A common example of this kind of code flow is seen with sheets, especially sheets that are created by a temporary controller object as illustrated in the following code fragment:

```objc
@implementation MySheetController
- (IBAction)showDoSomethingSheetAction:(id)action {

    id contextObject = /* ... */;
    // Code omitted.

    // Point A.
    [NSApp beginSheet:sheetWindow
           modalForWindow:window
           modalDelegate:delegate
           didEndSelector:@selector(sheetDidEnd:returnCode:contextInfo:);
           contextInfo:(void *)contextObject];
}
@end

@implementation MySheetControllerDelegate
- (void)sheetDidEnd:(NSWindow *)sheet returnCode:(int)returnCode contextInfo:(void *)contextInfo {

    // Point B.
    id contextObject = (id)contextInfo;

    [contextObject doSomething];
    // ...
}
@end
```

The problem is that in between points A and B, a garbage collection can occur and—if there are no strong references to it from a root object—the context object can be collected. (This example is somewhat simplified, but in a complex application it's a situation that can happen when the only strong reference to the object passed via the context parameter is on the stack—which for a sheet will be unwound all the way to the main run loop.)

The solution is to use a `CFRetain`/`CFRelease` pair as the value is put into/taken out of the `void *` parameter. This ensures that the object that will be used as context won't be collected until after it's no longer used (see [Memory Management Semantics](Using%20Core%20Foundation%20with%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmobxfvjvomy)).

```objc
@implementation MySheetController

- (IBAction)showDoSomethingSheetAction:(id)action {

    id contextObject = /* ... */;
    // Code omitted.

    // Point A.
    CFRetain(contextObject);

    [NSApp beginSheet:sheetWindow
           modalForWindow:window
           modalDelegate:delegate
           didEndSelector:@selector(sheetDidEnd:returnCode:contextInfo:);
           contextInfo:(void *)contextObject];
}
@end

@implementation MySheetControllerDelegate

- (void)sheetDidEnd:(NSWindow *)sheet returnCode:(int)returnCode contextInfo:(void *)contextInfo {

    // Point B.
    id contextObject = (id)contextInfo;
    // Code omitted.
    [contextObject doSomething];
    CFRelease(contextObject);
}
@end
```


Typically, the garbage collector treats global object pointers as root objects and so does not consider them candidates for collection (see [Root Set and Reference Types](Garbage%20Collection%20for%20Cocoa%20Essentials.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjsfvjvoni)). Globals of Objective-C objects or other `__strong` pointer variables, and function-level static variables, are written to with a write-barrier. Note that although this is true for Objective-C or Objective-C++, writing to globals from C or C++ is not supported. Weak globals have the same restriction; in addition, however, you cannot read from them in C or C++.

You can check whether a write-barrier is being used with the `-Wassign-intercept` compiler flag—see [Compiler Flag](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dambwfvjvooa).

The compiler can reuse stack slots it determines are no longer used (see [Root Set and Reference Types](Garbage%20Collection%20for%20Cocoa%20Essentials.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjsfvjvoni)). This can mean that objects are collected more quickly than you might expect—when a local variable is removed from the stack and hence the corresponding object not considered rooted. This has implications for situations in which you access data held by a local variable after the last direct reference to that variable. To illustrate, consider the following example:

```
NSData *myData = [someObject getMyData];
const uint8_t *bytes = [myData bytes];
NSUInteger offset = 0, length = [myData length];

while (offset < length) {
  // if you never reference myData again, bytes is a dangling pointer.
}
```

Suppose that after you send `myData` the `length` message, you do not reference it again directly. The compiler may reuse the stack slot for `myData`. `myData` may then become eligible for collection (see [Root Set and Reference Types](Garbage%20Collection%20for%20Cocoa%20Essentials.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjsfvjvoni)); if it is collected, then `bytes` becomes invalid.

You can ensure that the data object remains valid until you’ve finished using it by sending it a message, as shown in the following version:

```
NSData *myData = [someObject getMyData];
[myData retain];
const uint8_t *bytes = [myData bytes];
NSUInteger offset = 0, length = [myData length];

while (offset < length) {
  // bytes remains valid until next message sent to myData
}
[myData release];
```

Alternatively, in this particular case you can retrieve data from the object by sending it messages, as in this variant:

```
NSData *myData = [someObject getMyData];
const uint8_t *bytes = [myData bytes];
NSUInteger currentAddress = 0, finalAddress = [myData length];

while (currentAddress < finalAddress) {

    NSRange range = NSMakeRange (currentAddress, bytes[currentAddress]);
    if (range.length > finalAddress || currentAddress > finalAddress - range.length) {
        // This is an overflow
        break;
    }

    NSData *newData = [NSData dataWithBytesNoCopy:(void *)&bytes[currentAddress]
                                           length:length freeWhenDone:NO];
    currentAddress += length;
    // use the data from newData...
}
```

This ensures that `myData` remains on the stack until after you have finished processing the data it contains.

You can use the `-Wassign-intercept` compiler flag to find out when write-barriers are being used in your code. When you set the flag, the compiler logs a message when it offloads an assignment statement to a helper function.

Typically you use the flag to find situations where a write-barrier is _not_ actually used. A missing write-barrier can cause various problems—primarily when memory is being collected before you expect it to be. This is of particular interest when you’re using pointers to garbage-collected memory—especially pointers to pointers—such as where a left-hand-side cast discards the strong knowledge, as illustrated in the following example:

```
__strong CFDictionaryRef x;  // struct or ivar declaration
*(CFMutableDictionaryRef)&x = CFDictionaryCreateMutable(...);
```

[Next](Implementing%20a%20finalize%20Method.md)[Previous](Architecture.md)

