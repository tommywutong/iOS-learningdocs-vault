---
title: Run Loops
apple_id: 10000135i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFRunLoops/Tasks/Running.html
archived_at: '2026-07-15T07:22:50.533669Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Run Loops](Introduction%20to%20Run%20Loops.md)


[Next](Using%20Run%20Loops%20With%20Cocoa%20and%20Carbon.md)[Previous](Input%20Modes.md)

# Running the Run Loop

There is exactly one run loop per thread. You neither create nor destroy a thread’s run loop. Core Foundation automatically creates it for you as needed. You obtain the current thread’s run loop with the `CFRunLoopGetCurrent` function. Call `CFRunLoopRun` to run the current thread’s run loop in the default mode until the run loop is stopped with `CFRunLoopStop`. You can also call `CFRunLoopRunInMode` to run the current thread’s run loop in a specified mode for a set period of time, until the run loop is stopped, or until after the next run loop source is processed.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrguytsljwha2tcmbnijbusskhjbauc) contains a function, `RunMyTimer`, that uses the run loop with a timer to call a particular function every 5 seconds for 20 seconds. The function creates the run loop timer, `myTimer`, with the `CFRunLoopTimerCreate` function, initializing the timer’s callback function to `MyTimerFunction`, its initial firing time to 1 second in the future, and its periodicity to 5 seconds. Before the timer can fire, the function has to place the timer into a run loop mode, in this case a new mode named `“MyCustomMode,”` and then run the run loop in that mode by calling `CFRunLoopRunInMode`. The run loop will run for 20 seconds before control returns to the caller. During this time, the timer will fire and `MyTimerFunction` will be called 4 times. After the run loop exits, the function invalidates the timer to render it inoperable and to remove it from all run loop modes. Finally, because the function still holds a reference to the timer from the create function, the function releases the timer object.

__Listing 1__  Running a run loop with a timer

```
void MyTimerFunction( CFRunLoopTimerRef timer, void *info );

void RunMyTimer ()
{
    CFStringRef myCustomMode = CFSTR(“MyCustomMode”);
    CFRunLoopTimerRef myTimer;

    myTimer = CFRunLoopTimerCreate( NULL, CFAbsoluteTimeGetCurrent()+1.0,
                    5.0, 0, 0, MyTimerFunction, NULL );
    CFRunLoopAddTimer( CFRunLoopGetCurrent(), myTimer, myCustomMode );
    CFRunLoopRunInMode( myCustomMode, 20.0, false );
    CFRunLoopTimerInvalidate( myTimer );
    CFRelease( myTimer );
}
```

A run loop can only run if the requested mode has at least one source or timer to monitor. If a run loop mode is empty, the `CFRunLoopRun` and `CFRunLoopRunInMode` functions return immediately without doing anything.

Run loops can be run recursively. You can call `CFRunLoopRun` or `CFRunLoopRunInMode` from within any run loop callout and create nested run loop activations on the current thread’s call stack. You are not restricted in which modes you can run from within a callout. You can create another run loop activation running in any available run loop mode, including any modes already running higher in the call stack.

[Next](Using%20Run%20Loops%20With%20Cocoa%20and%20Carbon.md)[Previous](Input%20Modes.md)

