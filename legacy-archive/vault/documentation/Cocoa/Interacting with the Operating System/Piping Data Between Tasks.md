---
title: Interacting with the Operating System
apple_id: 10000058i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/Tasks/pipes.html
archived_at: '2026-07-15T07:17:38.067812Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interacting with the Operating System](Introduction%20to%20Interacting%20with%20the%20Operating%20System.md)


[Next](Document%20Revision%20History.md)[Previous](Ending%20an%20NSTask.md)

# Piping Data Between Tasks

Each end point of the pipe is a file descriptor, represented by an `NSFileHandle` object. You thus use `NSFileHandle` messages to read and write pipe data. A “parent” process creates the `NSPipe` object and holds one end of it. It creates an `NSTask` object for the other process and, before launching it, passes the other end of the pipe to that process; it does this by setting the standard input, standard output, or standard error device of the `NSTask` object to be the other `NSFileHandle` or the `NSPipe` itself (in the latter case, the type of `NSFileHandle`—reading or writing—is determined by the “set” method of `NSTask`).

The following example illustrates the above procedure:

```objc
- (void)readTaskData:(id)sender
{
    NSTask *pipeTask = [[NSTask alloc] init];
    NSPipe *newPipe = [NSPipe pipe];
    NSFileHandle *readHandle = [newPipe fileHandleForReading];
    NSData *inData = nil;

    // write handle is closed to this process
    [pipeTask setStandardOutput:newPipe];
    [pipeTask setLaunchPath:[NSHomeDirectory()
            stringByAppendingPathComponent:
                    @"PipeTask.app/Contents/MacOS/PipeTask"]];
    [pipeTask launch];

    while ((inData = [readHandle availableData]) && [inData length]) {
        [self processData:inData];
    }
    [pipeTask release];
}
```

The launched process in this example must get data and write that data (using the `writeData:` method of `NSFileHandle`), to its standard output device, which is obtained using the `fileHandleWithStandardOutput` method of `NSFileHandle`.

When the processes have no more data to communicate across the pipe, the writing process should simply send `closeFile` to its `NSFileHandle` end point. This causes the process with the “read” `NSFileHandle` to receive an empty `NSData` object, signalling the end of data. If the “parent” process created the `NSPipe` object with the `init` method, it should then release it.

[Next](Document%20Revision%20History.md)[Previous](Ending%20an%20NSTask.md)

