---
title: Interacting with the Operating System
apple_id: 10000058i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/Tasks/endingtask.html
archived_at: '2026-07-15T07:17:37.560897Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interacting with the Operating System](Introduction%20to%20Interacting%20with%20the%20Operating%20System.md)


[Next](Piping%20Data%20Between%20Tasks.md)[Previous](Creating%20and%20Launching%20an%20NSTask.md)

# Ending an NSTask

Normally, you want the task that you’ve launched to run to completion. When the task exits, the corresponding `NSTask` object posts an `NSTaskDidTerminateNotification` to the default notification center. You can add one of the custom objects in your program as an observer of the notification and check the task’s exit status (using `terminationStatus`) in the observer method. For example:

```objc
-(id)init {
    self = [super init];
    [[NSNotificationCenter defaultCenter] addObserver:self
            selector:@selector(checkATaskStatus:)
            name:NSTaskDidTerminateNotification
            object:nil];
    return self;
}

- (void)checkATaskStatus:(NSNotification *)aNotification {
    int status = [[aNotification object] terminationStatus];
    if (status == ATASK_SUCCESS_VALUE)
        NSLog(@"Task succeeded.");
    else
        NSLog(@"Task failed.");
}
```

If you need to force a task to end execution, send a `terminate` message to the `NSTask` object. If the `NSTask` object gets released, however, `NSTaskDidTerminateNotification` does not get sent, as the port the message would have been sent on was released as part of the task release.

[Next](Piping%20Data%20Between%20Tasks.md)[Previous](Creating%20and%20Launching%20an%20NSTask.md)

