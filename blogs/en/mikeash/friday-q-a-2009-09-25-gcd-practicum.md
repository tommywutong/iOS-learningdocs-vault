---
title: 'Friday Q&A 2009-09-25: GCD Practicum'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-09-25-gcd-practicum.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1caafbd18fd5ad2d'
translated: false
---

> 原文：[Friday Q&A 2009-09-25: GCD Practicum](https://www.mikeash.com/pyblog/friday-qa-2009-09-25-gcd-practicum.html)　·　mikeash.com Friday Q&A

Posted at 2009-09-25 11:52 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-10-02: Care and Feeding of Singletons](https://www.mikeash.com/pyblog/friday-qa-2009-10-02-care-and-feeding-of-singletons.html)  
Previous article: [Friday Q&A 2009-09-18: Intro to Grand Central Dispatch, Part IV: Odds and Ends](https://www.mikeash.com/pyblog/friday-qa-2009-09-18-intro-to-grand-central-dispatch-part-iv-odds-and-ends.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [performance](https://www.mikeash.com/pyblog/?tag=performance) [sourcecode](https://www.mikeash.com/pyblog/?tag=sourcecode)

Friday Q&A 2009-09-25: GCD Practicum

by [Mike Ash](https://www.mikeash.com/)

**Overview**  
 I'm going to walk through the parallelization of this program in four steps. The first step will be the basic serialized program, and the following steps work through building it into a fully parallel program using GCD. If you'd like to follow along, you can [get the full source code for all four steps](https://www.mikeash.com/pyblog/imagegcd.zip). Don't run `imagegcd2.m` though. You'll see why in a bit.

**The Original Program**  
 The program that we're going to work with is a simple thing that goes through the contents of `~/Pictures` and generates thumbnails for everything inside. It's a pure command-line program, albeit using Cocoa to do most of the work. This is what its main function looks like:

```
    int main(int argc, char **argv)
    {
        NSAutoreleasePool *outerPool = [NSAutoreleasePool new];
        
        NSApplicationLoad();
        
        NSString *destination = @"/tmp/imagegcd";
        [[NSFileManager defaultManager] removeItemAtPath: destination error: NULL];
        [[NSFileManager defaultManager] createDirectoryAtPath: destination
                                        withIntermediateDirectories: YES
                                        attributes: nil
                                        error: NULL];
        
        
        Start();
        
        NSString *dir = [@"~/Pictures" stringByExpandingTildeInPath];
        NSDirectoryEnumerator *enumerator = [[NSFileManager defaultManager] enumeratorAtPath: dir];
        int count = 0;
        for(NSString *path in enumerator)
        {
            NSAutoreleasePool *innerPool = [NSAutoreleasePool new];
            
            if([[[path pathExtension] lowercaseString] isEqual: @"jpg"])
            {
                path = [dir stringByAppendingPathComponent: path];
                
                NSData *data = [NSData dataWithContentsOfFile: path];
                if(data)
                {
                    NSData *thumbnailData = ThumbnailDataForData(data);
                    if(thumbnailData)
                    {
                        NSString *thumbnailName = [NSString stringWithFormat: @"%d.jpg", count++];
                        NSString *thumbnailPath = [destination stringByAppendingPathComponent: thumbnailName];
                        [thumbnailData writeToFile: thumbnailPath atomically: NO];
                    }
                }
            }
            
            [innerPool release];
        }
        
        End();
        
        [outerPool release];
    }
```

For the full listing including all of the auxiliary functions, please [refer to the companion source code download](https://www.mikeash.com/pyblog/imagegcd.zip). This program is `imagegcd1.m`. The important parts are all here, though. `Start` and `End` are just simple timing functions using `gettimeofday`. `ThumbnailDataForData` uses Cocoa to load the data into an image, shrink it proportionally to be no larger than 320x320, and then encodes the result as JPEG.

**Naïve Parallelization**  
 At first glance this looks pretty easy to parallelize. Each iteration through the loop can be pushed onto a GCD global queue. We can wait for them all to finish at the end by using a dispatch group. One last trick: to ensure that each iteration still gets a unique number for its filename, we'll use `OSAtomicIncrement32` to atomically increment `count`. This is what the new code looks like:

```
    dispatch_queue_t globalQueue = dispatch_get_global_queue(0, 0);
    dispatch_group_t group = dispatch_group_create();
    __block uint32_t count = -1;
    for(NSString *path in enumerator)
    {
        dispatch_group_async(group, globalQueue, BlockWithAutoreleasePool(^{
            if([[[path pathExtension] lowercaseString] isEqual: @"jpg"])
            {
                NSString *fullPath = [dir stringByAppendingPathComponent: path];
                
                NSData *data = [NSData dataWithContentsOfFile: fullPath];
                if(data)
                {
                    NSData *thumbnailData = ThumbnailDataForData(data);
                    if(thumbnailData)
                    {
                        NSString *thumbnailName = [NSString stringWithFormat: @"%d.jpg",
                                                   OSAtomicIncrement32(&count;)];
                        NSString *thumbnailPath = [destination stringByAppendingPathComponent: thumbnailName];
                        [thumbnailData writeToFile: thumbnailPath atomically: NO];
                    }
                }
            }
        });
    }
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
```

This one is `imagegcd2.m`. But _don't run it!_

If you ignored my warning and ran it anyway, you're probably just reloading this page after rebooting your computer. If you haven't run it, what happens (if you have a lot of pictures, at least) is that your computer locks up and you probably can't fix it unless you wait much longer than you'd really like to.

**The Problem**  
 What's causing all this trouble? The problem lies in GCD's smarts. GCD runs tasks on a global thread pool whose size is scaled in response to system load. For example, my computer has four cores, and so if I load up GCD with work, GCD will run four worker threads to load every core. If something else on my computer starts doing work, GCD will scale back a bit to give the other task some room.

However, GCD can also _increase_ the number of active threads. It will do this if one of the worker threads blocks. Imagine these four worker threads running and then suddenly one of them does something like, oh, let's say, read a file. It goes off to wait for the disk, and your cores are being under-utilized. GCD will see this situation and spawn another worker thread to fill the gap.

Now, think about what happens here. The main loop is pushing jobs onto the global queue extremely quickly. GCD will start off with a few worker threads and start popping jobs off the queue. These jobs perform a trifling amount of work up front and then immediately they go off and read a file from the disk. The slow, spinning disk.

And let's not forget another important property of the disk: unless you have an SSD or a fancy RAID, _they get substantially slower under contention_.

These first four jobs all hit the disk at the same time, which goes crazy trying to fill all four requests at once. GCD, which only looks at CPU usage, sees that the CPU cores are sitting mostly idle and starts spawning more worker threads. These threads also slam into the disk wall, causing GCD to spawn yet more threads, etc.

Eventually the file reads begin to complete. Now, instead of four threads for the four cores, there are hundreds. GCD will scale back if there are too many worker threads using CPU time, but it's limited in when it can scale back. It can't kill worker threads in the middle of a job, and can't even pause them. It has to wait until an entire job has completed before it can kill the thread that job is on. All of these pending in-flight jobs prevent GCD from reducing the worker thread count.

All these hundreds of threads start to finish reading their image data and begin process. They get in each other's way on the CPU as well, although the CPU handles contention much better than the disk. The trouble is, the first thing thing these threads do once they have the file data is decode it. If you have a lot of JPEGs, this image data is going to expand by a factor of 10 or more. With hundreds of these things in flight, you'll start to blow out your memory. What happens when you run out of physical RAM? More disk usage!

Now you have a vicious feedback cycle. Disk contention causes more worker threads, which causes more memory usage, which causes more disk contention. The process runs away until GCD hits its limit of 512 worker threads. With typical picture sizes, 512 in-flight jobs is more than enough to send your system into swap hell from which it will take a long time to recover. Quite likely you won't even be able to kill the job for quite some time.

This is something you really have to watch out for when using GCD. GCD is great for limiting the number of concurrent jobs for CPU usage, but it will do nothing about contention over other resources. If your jobs do IO or anything else that could block for a while, you need to beware of this problem.

**The Fix**  
 The root of this whole problem was IO contention leading to runaway feedback. Remove the contention, remove the problem.

GCD makes this easy with custom queues. Custom queues are inherently serialized. If we create a custom queue just for IO and put all file reading/writing onto that queue, then the disk will only be hit up for one file at a time and the contention disappears.

Here's the main loop of our program redone to use an IO queue:

```
    dispatch_queue_t globalQueue = dispatch_get_global_queue(0, 0);
    dispatch_queue_t ioQueue = dispatch_queue_create("com.mikeash.imagegcd.io", NULL);
    dispatch_group_t group = dispatch_group_create();
    __block uint32_t count = -1;
    for(NSString *path in enumerator)
    {
        if([[[path pathExtension] lowercaseString] isEqual: @"jpg"])
        {
            NSString *fullPath = [dir stringByAppendingPathComponent: path];
            
            dispatch_group_async(group, ioQueue, BlockWithAutoreleasePool(^{
                NSData *data = [NSData dataWithContentsOfFile: fullPath];
                if(data)
                    dispatch_group_async(group, globalQueue, BlockWithAutoreleasePool(^{
                        NSData *thumbnailData = ThumbnailDataForData(data);
                        if(thumbnailData)
                        {
                            NSString *thumbnailName = [NSString stringWithFormat: @"%d.jpg",
                                                       OSAtomicIncrement32(&count;)];
                            NSString *thumbnailPath = [destination stringByAppendingPathComponent: thumbnailName];
                            dispatch_group_async(group, ioQueue, BlockWithAutoreleasePool(^{
                                [thumbnailData writeToFile: thumbnailPath atomically: NO];
                            }));
                        }
                    }));
            }));
        }
    }
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
```

And this one is `imagegcd3.m`. It's great how easy GCD makes it to push different parts of a task onto different queues with some simple nesting. This one will behave fairly well... most of the time.

The problem is that it's inherently unstable because the different parts are not synchronized. The flow of data in this code looks like this:

```
    Main Thread          IO Queue            Concurrent Queue
    
    find paths  ------>  read  ----------->  process
                                             ...
                         write <-----------  process
```

The arrows in that diagram are _non-blocking_ and will simply buffer the objects being moved around.

Now imagine a machine where the disk is fast enough to read files faster than the CPU can process them. This isn't all that hard to imagine: although the CPU is much faster, it's also doing _much_ more work. The data read from the disk begins to pile up in the queue. This data takes up memory, possibly substantial amounts of memory if you have a lot of big pictures.

Then you run out of physical RAM and begin to swap.

This can lead to another runaway feedback loop like the first one. If anything causes the worker thread to block, GCD will spin off a new one, which will immediately start trying to allocate a bunch of memory and block because of the ongoing memory pressure. GCD will spin off more jobs, causing more memory pressure, and you're back in swap hell again.

What's interesting about this feedback is that, unlike the first GCD attempt, it's self-regulating to some extent. As IO contention goes through the roof, the IO queue will come to a halt, and won't make any significant progress until the situation has regained sanity. Once it does, you're back to low memory usage and good throughput until the buffered data builds up too far again.

End result: the program alternates between smooth processing and being bogged down.

Note that if the disk is slower the same problem can still occur because the thumbnails will be buffered at the end of the run, but it's likely to be much less severe because the quantity of data is so much smaller.

**Really Fixing the Problem**  
 Since the problem with the last attempt was a lack of synchronization between the different phases of the operation, let's synchronize them. The simple way to do this is to use a semaphore to limit the number of jobs in flight at any given time.

One question remains: how many jobs should we allow?

Obviously it should scale with the number of CPU cores in the system, because we want to take advantage of whatever is available. Simply limiting to the number of CPU cores is a bad idea, though, because much of each job is IO. And it can't be too high, because then we'll run out of memory.

I decided on having twice the number of jobs as CPU cores. My reasoning is that this will scale up to the point where IO takes as long as processing. If IO takes longer than processing, then IO will be the bottleneck anyway, and so there's no sense in having more concurrent jobs than this. If IO takes significantly less time than processing, then GCD will automatically keep the number of worker threads low enough to ensure minimal contention on the CPU.

This is what the main loop now looks ilke:

```
    dispatch_queue_t ioQueue = dispatch_queue_create("com.mikeash.imagegcd.io", NULL);
    
    int cpuCount = [[NSProcessInfo processInfo] processorCount];
    dispatch_semaphore_t jobSemaphore = dispatch_semaphore_create(cpuCount * 2);
    
    dispatch_group_t group = dispatch_group_create();
    __block uint32_t count = -1;
    for(NSString *path in enumerator)
    {
        WithAutoreleasePool(^{
            if([[[path pathExtension] lowercaseString] isEqual: @"jpg"])
            {
                NSString *fullPath = [dir stringByAppendingPathComponent: path];
                
                dispatch_semaphore_wait(jobSemaphore, DISPATCH_TIME_FOREVER);
            
                dispatch_group_async(group, ioQueue, BlockWithAutoreleasePool(^{
                    NSData *data = [NSData dataWithContentsOfFile: fullPath];
                    dispatch_group_async(group, globalQueue, BlockWithAutoreleasePool(^{
                        NSData *thumbnailData = ThumbnailDataForData(data);
                        if(thumbnailData)
                        {
                            NSString *thumbnailName = [NSString stringWithFormat: @"%d.jpg",
                                                       OSAtomicIncrement32(&count;)];
                            NSString *thumbnailPath = [destination stringByAppendingPathComponent: thumbnailName];
                            dispatch_group_async(group, ioQueue, BlockWithAutoreleasePool(^{
                                [thumbnailData writeToFile: thumbnailPath atomically: NO];
                                dispatch_semaphore_signal(jobSemaphore);
                            }));
                        }
                        else
                            dispatch_semaphore_signal(jobSemaphore);
                    }));
                }));
            }
        });
    }
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
```

And now we finally have a program which runs smoothly and processes quickly.

**Benchmarking**  
 I obtained the following runtimes, on a library of 7913 pictures:

| **Program** | **Time (seconds)** |
|---|---|
| `imagegcd1.m` | 984 |
| `imagegcd2.m` | did not run |
| `imagegcd3.m` | 300 |
| `imagegcd4.m` | 279 |

Note that, because I am lazy, I did not shut off all other programs before I ran this, so the program was not able to completely monopolize the CPUs. Given this, the total speedup of 3.5 is quite good for my 4 CPU cores.

It's interesting that version 3 performed as well as it did. I did observe it exhibiting the cycling behavior I discussed, but not too often. Most likely this is because my machine has 15GB of RAM. On a less well endowed system it's likely to perform substantially worse. I observed it using up to 10GB of RAM at one point. If I compile it as 32-bit then it rapidly runs out of virtual memory and crashes. Version 4 never uses any significant amout of RAM.

**Conclusion**  
 GCD is a fantastic piece of technology and does a lot of useful things, but it can't do everything for you. In particular, concurrent jobs which perform IO and have the potential to use a lot of memory must be managed carefully. Even so, the facilities that GCD provides make it easy to construct a system which will not overwhelm the computer's resources.

That wraps up this week's Friday Q&A. Come back next week for another exciting edition. In the mean time, [send me your topics to discuss](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-09-25-gcd-practicum.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
