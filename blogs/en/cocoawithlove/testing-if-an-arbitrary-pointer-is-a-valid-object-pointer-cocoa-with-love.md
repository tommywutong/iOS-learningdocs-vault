---
title: 'Testing if an arbitrary pointer is a valid object pointer | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/10/testing-if-arbitrary-pointer-is-valid.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:5e022040f1c118bd'
translated: false
---

> 原文：[Testing if an arbitrary pointer is a valid object pointer | Cocoa with Love](https://www.cocoawithlove.com/2010/10/testing-if-arbitrary-pointer-is-valid.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I look at an approach for testing if an arbitrary pointer is a pointer to a valid Objective-C object. The result from the test is not absolutely accurate and can interfere with gdb debugging if the pointer isn't a valid memory location, so this is not something you'd want to do often (and certainly not in production code). But it can be a handy debugging tool for when you're staring blindly at memory you didn't allocate.

## Introduction

I originally wrote this code when I was looking through all the notifications from the local `CFNotificationCenter`, trying to work out where I was making mistakes in some AVFoundation video code (AVFoundation produces a lot of notifications when media playback is happening).

The callback function for these notifications has the following prototype:

```objc
void MyNotificationCallBack (
   CFNotificationCenterRef center,
   void *observer,
   CFStringRef name,
   const void *object,
   CFDictionaryRef userInfo
);
```

The `object` associated with the notification is passed as a `void *`. Most of the time, the value in `object` will be an Objective-C object but for the few times when it isn't, simply passing the result into `NSLog` can cause your program to crash.

## What do you need to test?

Again, this comes back to the question: what is a valid Objective-C object?

For the purpose of sending a message to an object, all you need is for the value pointed to by the object pointer (i.e. the `isa` pointer) to be a registered `Class` value. This is the most important point to test — the chance of an arbitrary memory value being a valid `Class` by chance is fairly low (although certainly not zero).

But there is another requirement to be a usable object: the memory space following the `isa` pointer must be valid. This is not an easy thing to test, but it is possible to test if the object itself was allocated at least as large as the class' instance size.

However, this allocation test does not need to return positive for any object that wasn't heap allocated. The most common example of non-heap allocated objects in Objective-C are compiler created strings. So while appropriate heap allocation for a block of memory that starts with an isa pointer is a near guarantee that the object is a valid Objective-C object, failure of this test does not eliminate the possibility that it's a valid object.

Finally, while all of this is happening, there remains the possibility that the pointer you're testing doesn't point to a valid memory location at all. If you're interested in handling this situation, you need to set up a signal handler (or Mach exception handler) to catch `SIGBUS` and `SIGSEGV` signals (or `EXC_BAD_ACCESS` if you go the Mach exceptions route).

## The code

```objc
#import &lt;malloc/malloc.h&gt;
#import &lt;objc/runtime.h&gt;

static sigjmp_buf sigjmp_env;

void
PointerReadFailedHandler(int signum)
{
    siglongjmp (sigjmp_env, 1);
}

BOOL IsPointerAnObject(const void *testPointer, BOOL *allocatedLargeEnough)
{
    *allocatedLargeEnough = NO;
    
    // Set up SIGSEGV and SIGBUS handlers
    struct sigaction new_segv_action, old_segv_action;
    struct sigaction new_bus_action, old_bus_action;
    new_segv_action.sa_handler = PointerReadFailedHandler;
    new_bus_action.sa_handler = PointerReadFailedHandler;
    sigemptyset(&new_segv_action.sa_mask);
    sigemptyset(&new_bus_action.sa_mask);
    new_segv_action.sa_flags = 0;
    new_bus_action.sa_flags = 0;
    sigaction (SIGSEGV, &new_segv_action, &old_segv_action);
    sigaction (SIGBUS, &new_bus_action, &old_bus_action);

    // The signal handler will return us to here if a signal is raised
    if (sigsetjmp(sigjmp_env, 1))
    {
        sigaction (SIGSEGV, &old_segv_action, NULL);
        sigaction (SIGBUS, &old_bus_action, NULL);
        return NO;
    }
    
    Class testPointerClass = *((Class *)testPointer);

    // Get the list of classes and look for testPointerClass
    BOOL isClass = NO;
    NSInteger numClasses = objc_getClassList(NULL, 0);
    Class *classesList = malloc(sizeof(Class) * numClasses);
    numClasses = objc_getClassList(classesList, numClasses);
    for (int i = 0; i < numClasses; i++)
    {
        if (classesList[i] == testPointerClass)
        {
            isClass = YES;
            break;
        }
    }
    free(classesList);

    // We're done with the signal handlers (install the previous ones)
    sigaction (SIGSEGV, &old_segv_action, NULL);
    sigaction (SIGBUS, &old_bus_action, NULL);
    
    // Pointer does not point to a valid isa pointer
    if (!isClass)
    {
        return NO;
    }
    
    // Check the allocation size
    size_t allocated_size = malloc_size(testPointer);
    size_t instance_size = class_getInstanceSize(testPointerClass);
    if (allocated_size > instance_size)
    {
        *allocatedLargeEnough = YES;
    }
    
    return YES;
}
```

## Results from the function

Running this test program:

```objc
void LogPointerInformation(const void *somePointer)
{
    BOOL allocatedLargeEnough;
    BOOL isMessageableObject = IsPointerAnObject(somePointer, &allocatedLargeEnough);
    NSLog(@"The pointer %p is %@ and is %@.",
        somePointer,
        isMessageableObject ?
            @"a valid object" :
            @"not a valid object",
        allocatedLargeEnough ?
            @"allocated at least as large as the required instance size" :
            @"not a known allocation");
}

int main (int argc, const char * argv[]) {
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

    LogPointerInformation(@"");
    LogPointerInformation([[[NSObject alloc] init] autorelease]);
    LogPointerInformation(LogPointerInformation);
    LogPointerInformation(0x12345678);

    [pool drain];
    return 0;
}
```

Gives the following results (I've chopped off the `NSLog` times for brevity):

```objc
The pointer 0x100001130 is a valid object and is not a known allocation.
The pointer 0x10011e940 is a valid object and is allocated at least as large as the required instance size.
The pointer 0x100000c0d is not a valid object and is not a known allocation.
The pointer 0x12345678 is not a valid object and is not a known allocation.
```

## Limitations of this approach

The most serious limitation of this approach is that it can never guarantee anything. For this reason, it is important that you never use this in production code.

The most obvious situation where the function will fail completely is when testing a `malloc`'d C array of Objective-C class pointers. This memory block definitely starts with a valid `Class` value and may even have a `malloc_size` greater than that class' instance size — but the block was never truly allocated as an object and if any instance values are important to the class, they are all likely to be invalid.

Objects that are not heap allocated are difficult to guarantee that their instance memory will be within addressable memory. This means that you could raise SIGSEGV or SIGBUS signals.

Still on the topic of signals, while I've included signal handling in this code, it's unlikely you'll ever want it to be invoked as it stops gdb dead.

While ordinarily, you can give gdb a `handle signal nostop noprint pass` to continue after the signal, that won't work here. There are issues getting the Mac version of gdb to proceed after an EXC_BAD_ACCESS. It is actually easier to let gdb catch the signal, then drag the program execution point in Xcode to the top of the `sigsetjmp` block manually.

As a final caveat: the signal handling code that I've written is strictly not thread-safe and non-reentrant.

## Conclusion

The result is more of a heuristic than an absolute verdict.

However, the approach is a useful tool to give an "acceptable" verification that a value is a valid object for debugging purposes. It is certainly good enough to test before sending values to `NSLog`.

The issues with gdb when an invalid memory access signal is raised are annoying. I'd be interested to see if there's a way to avoid this. It certainly provides an added disincentive to using this code on truly arbitrary values.
