---
title: Interacting with the Operating System
apple_id: 10000058i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/Tasks/createtask.html
archived_at: '2026-07-15T07:17:37.065054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interacting with the Operating System](Introduction%20to%20Interacting%20with%20the%20Operating%20System.md)


[Next](Ending%20an%20NSTask.md)[Previous](Signals.md)

# Creating and Launching an NSTask

There are two ways to create an `NSTask` object. If it is sufficient for the task to run in the environment that it inherits from the process that creates it, use the class method `launchedTaskWithLaunchPath:arguments:`. This method both creates and executes (launches) the task. If you need to change the task’s environment, create the task using `alloc` and `init`, use `set...` methods to change parts of the environment, then use the `launch` method to launch the task. For example, the following method runs tasks that take an input file and an output file as arguments. It reads these arguments, the task’s executable, and the current directory from text fields before it launches the task:

```objc
- (void)runTask:(id)sender
{
    NSTask *aTask = [[NSTask alloc] init];
    NSMutableArray *args = [NSMutableArray array];

    /* set arguments */
    [args addObject:[[inputFile stringValue] lastPathComponent]];
    [args addObject:[outputFile stringValue]];
    [aTask setCurrentDirectoryPath:[[inputFile stringValue]
            stringByDeletingLastPathComponent]];
    [aTask setLaunchPath:[taskField stringValue]];
    [aTask setArguments:args];
    [aTask launch];
}
```

If you create an `NSTask` object in this manner, you must be sure to set the executable name using `setLaunchPath:`. If you don’t, an `NSInvalidArgumentException` is raised.

[Next](Ending%20an%20NSTask.md)[Previous](Signals.md)

