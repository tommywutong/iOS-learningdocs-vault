---
title: Run Loops
apple_id: 10000062i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputControl/Tasks/runningloops.html
archived_at: '2026-07-15T07:16:06.021062Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Run Loops](Introduction%20to%20Run%20Loops.md)


[Next](Document%20Revision%20History.md)[Previous](Adding%20Input%20Sources.md)

# Running the Run Loop

You have numerous ways in which to run the run loop. Using `run`, control is passed to the run loop until all input sources in the `NSDefaultRunLoopMode` mode have been removed; if there are no input sources, the run loop returns immediately:

```
[[NSRunLoop currentRunLoop] run];
```

To specify a time at which the run loop should stop processing events and return control, use `runUntilDate:`:

```
[[NSRunLoop currentRunLoop] runUntilDate:aDate];
```

To specify a mode other than `NSDefaultRunLoopMode`, use `runMode:beforeDate:`. This method runs the run loop only once; it returns either after it processes a single input source or the _beforeDate_ date is reached. To run any mode continuously, invoke `runMode:beforeDate:` in a loop with a date far in the future:

```
while ( [[NSRunLoop currentRunLoop] runMode:NSModalPanelRunLoopMode
                beforeDate:[NSDate distantFuture]] );
```

The return value of `runMode:beforeDate:` indicates whether the run loop is still running; if the run loop is empty (in other words, it has no input sources) `runMode:beforeDate:` returns `NO` and the `while` loop exits.

Finally, to conditionalize the run loop so that you can define an exit condition, include a test in the loop surrounding the `runMode:beforeDate:` invocation:

```
double resolution = 1.0;
BOOL endRunLoop = NO;
BOOL isRunning;
do {
    NSDate* next = [NSDate dateWithTimeIntervalSinceNow:resolution];
    isRunning = [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode
                beforeDate:next];
} while (isRunning && !endRunLoop);
```

In this snippet, the `endRunLoop` variable is the test condition indicating when to break out of the run loop. It may be either a global variable or an instance variable that is set to `YES` from a run loop callout when it is time to exit the run loop.

[Next](Document%20Revision%20History.md)[Previous](Adding%20Input%20Sources.md)

