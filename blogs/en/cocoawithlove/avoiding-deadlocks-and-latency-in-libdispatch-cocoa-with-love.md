---
title: 'Avoiding deadlocks and latency in libdispatch | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/06/avoiding-deadlocks-and-latency-in.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:732229487d0cde8c'
translated: false
---

> 原文：[Avoiding deadlocks and latency in libdispatch | Cocoa with Love](https://www.cocoawithlove.com/2010/06/avoiding-deadlocks-and-latency-in.html)　·　Cocoa with Love (Matt Gallagher)

The system-wide thread pool of libdispatch's global queue is an easy way to efficiently manage concurrent operations but it is not the solution to all threading problems and it is not without its own class of problems. In this post I look at deadlocks and latency problems that are inherent in thread-pool based solutions like libdispatch's global concurrent queue so that you will know when you should use this option and when you need something else.

## Introduction: libdispatch's global queue is a constrained resource

In Mac OS X 10.6 (Snow Leopard), Apple introduced Grand Central Dispatch (GCD) for managing a system-wide thread pool. The normal API for GCD is libdispatch (despite the name, this API is part of libSystem).

The simplest way to interact with libdispatch is to execute blocks on the global queue:

```objc
dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
dispatch_async(queue, ^{ /* perform some work */ });
```

For discrete packets of work that are not order dependent, this is a great solution. In this post, however, I'm going to look at situations where this is a poor choice.

The key limitation of this approach is that the global concurrent thread pool is a constrained resource — there are only as many active threads in this pool as you have CPUs on your computer.

Using this constrained resource indiscriminately can lead to the following problems once the limits of the resource are reached:

- higher latency than other solutions
- deadlocks for interdependent jobs in the queue

## Latency problems

The following code simulates a tiny web sever or similar program that needs to serve a number of clients. In this case, it has 20 simultaneous requests from different clients.

In reality, this program just writes a small string to /dev/null 100,000 times for every client but that's sufficient to simulate any similar network or other non-CPU based operation.

```objc
int main(int argc, const char * argv[])
{
    dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_group_t group = dispatch_group_create();
    
    FILE *devNull = fopen("/dev/null", "a");

    const int NumConcurrentBlocks = 20;
    const int NumLoopsPerBlock = 100000;

    for (int i = 0; i < NumConcurrentBlocks; i++)
    {
        dispatch_group_async(group, queue, ^{
            NSLog(@"Started block %d", i);
            for (int j = 0; j < NumLoopsPerBlock; j++)
            {
                fprintf(devNull, "Write to /dev/null\n");
            }
            NSLog(@"Finished block %d", i);
        });
    }

    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
    dispatch_release(group);
    fclose(devNull);
    
    return 0;
}
```

This scenario illustrates the latency problems inherent in using the libdispatch global queue: on my computer, the first 4 blocks start immediately and the first of these finish 1.5 seconds later when the next blocks are started. The final block does not begin until 7.5 seconds after it is queued, finishing at the 9 second mark.

While the global queue in libdispatch is called "concurrent", it is only concurrent up to a threshold. Once the concurrent slots are full, the global queue becomes serial — in this case, the limit is reached and the serial nature increases the latency.

If this were a heavily loaded web server, instead of simply slowing down evenly for all users, the first few users would get a response and the last few would simply time out.

The solution to this type of problem is to create a specific queue for every block. Instead of pushing everything into the global queue (which is capped at 4 blocks on my test computer) we will have a separate queue for each block that will run simultaneously.

```objc
int main(int argc, const char * argv[])
{
    dispatch_group_t group = dispatch_group_create();
    FILE *devNull = fopen("/dev/null", "a");

    const int NumConcurrentBlocks = 20;
    dispatch_queue_t *queues = malloc(sizeof(dispatch_queue_t) * NumConcurrentBlocks);
    for (int q = 0; q < NumConcurrentBlocks; q++)
    {
        char label[20];
        sprintf(label, "Queue%d", q);
        queues[q] = dispatch_queue_create(label, NULL);
    }

    const int NumLoopsPerBlock = 100000;
    for (int i = 0; i < NumConcurrentBlocks; i++)
    {
        dispatch_group_async(group, queues[i], ^{
            NSLog(@"Started block %d", i);
            for (int j = 0; j < NumLoopsPerBlock; j++)
            {
                fprintf(devNull, "abcdefghijklmnopqrstuvwxyz\n");
            }
            NSLog(@"Finished block %d", i);
        });
    }

    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
    dispatch_release(group);
    fclose(devNull);
    
    return 0;
}
```

The result is that all 20 blocks are started simultaneously. All run at approximately the same speed and all finish at approximately the same time.

> : as suggested by Keith in the comments, since these operations are I/O bound, not CPU bound, a better solution would be to use a
> 
> file write source
> 
> in the queue instead of standard operation queue blocks. File write sources are removed from the queue when they are blocked on I/O and this would allow all 20 sources to operate equitably in the global concurrent queue (or any other single queue).

## Deadlocking

Deadlocking occurs when a first block stops and waits for a second to complete but the second can't proceed because it needs a resource that the first is holding.

In the following program, 20 parent blocks are queued (which will more than fill the constrained resource of the global concurrent queue). Each of these blocks spawns a child block which is queued in the same global concurrent queue. The parent runs a busy wait loop until the child adds its own integer to the `completedSubblocks` set.

```objc
NSMutableSet *completedSubblocks;
NSLock *subblocksLock;

int main (int argc, const char * argv[])
{
    completedSubblocks = [[NSMutableSet alloc] init];
    subblocksLock = [[NSLock alloc] init];

    dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_group_t group = dispatch_group_create();
        
    const int NumConcurrentBlocks = 20;
    for (int i = 0; i < NumConcurrentBlocks; i++)
    {
        dispatch_group_async(group, queue, ^{
            NSLog(@"Starting parent block %d", i);
            
            NSDate *endDate = [NSDate dateWithTimeIntervalSinceNow:1.0];
            while ([(NSDate *)[NSDate date] compare:endDate] == NSOrderedAscending)
            {
                // Busy wait for 1 second to let the queue fill
            }
            
            dispatch_async(queue, ^{
                NSLog(@"Starting child block %d", i);

                [subblocksLock lock];
                [completedSubblocks addObject:[NSNumber numberWithInt:i]];
                [subblocksLock unlock];
                
                NSLog(@"Finished child block %d", i);
            });

            BOOL complete = NO;
            while (!complete)
            {
                [subblocksLock lock];
                if ([completedSubblocks containsObject:[NSNumber numberWithInt:i]])
                {
                    complete = YES;
                }
                [subblocksLock unlock];
            }

            NSLog(@"Finished parent block %d", i);
        });
    }
    
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
    dispatch_release(group);
    
    [completedSubblocks release];
    [subblocksLock release];

    return 0;
}
```

On my computer the first 8 blocks are started (filling the global queue's concurrent blocks) and these blocks block the global queue so that the child blocks can never run. Since the parent is waiting for the child and the child can never run, the result is a deadlock: the program never completes.

You'll notice that I've used a busy wait loop for both the 1 second delay and to detect when the child has completed. Normally, you would dispatch the child using `dispatch_sync` (which is a different way to wait for the child to complete) but the reality is that libdispatch is smart enough to remove a block from its queue while it is using one of the libdispatch wait mechanisms (or one of the many Cocoa or OS functions that similarly yields CPU time like `sleep`).

While using the correct functions to wait will fix this trivial example, it will not fix the situation where the processes might be genuinely busy.

The best solution is to avoid dependencies between blocks in the same queue.

In a situation like this where one of the blocks (the child block) consumes a trivial amount of time and the other is time consuming (the parent always takes at least 1 second), you can simply enqueue the trivial time block in a separate serial queue. That will prevent deadlocking in all cases.

In a situation where both parent and child are time consuming, you could try:

- create a separate queue for every invocation of either the parent or child and queue the other in the global queue
- roll the functionality of the child into the parent so that they are always done as a single block
- carefully write your code to ensure that a libdispatch wait mechanism is always ahead of any dependency

## Conclusion

While libdispatch does an excellent job at making concurrent, multithreaded programming easier, it does not magically eliminate some of the pitfalls.

The problems I've looked at in this post are mostly a result of the fact that queues are shared resources and there are situations where you must be careful about how resources are shared.

In that sense, these problems are not directly related to libdispatch (although I've used libdispatch to implement the scenarios) they are problems that can be caused by misusing any system where a fixed number of servers is pulling data out of a queue.

Grand Central Dispatch's global queue is intended for CPU intensive operations. That it limits concurrency to the number of CPUs in your computer is good for CPU intensive operations; it prevents wasting CPU time due to task swapping. The examples here demonstrate the downside: it may increase latency for queue blocks and you need to be careful about dependencies between blocks on the same queue.
