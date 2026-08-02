---
title: Multiprocessing Services Programming Guide
apple_id: TP40000853
resource_type: Guide
platform: macOS
topic: null
technology: CoreServices
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Multitasking_MultiproServ/03tasks/tasks.html
archived_at: '2026-07-15T05:23:37.790397Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Multiprocessing Services Programming Guide](Introduction%20to%20Multiprocessing%20Services%20Programming%20Guide.md)


[Next](Preemptive%20Task%E2%80%93Safe%20Mac%20OS%20System%20Software%20Functions.md)[Previous](About%20Multitasking%20on%20the%20Mac%20OS.md)

# Using Multiprocessing Services

This chapter describes how to incorporate Multiprocessing Services into your Mac OS application. You should read this chapter if you are interested in adding preemptive tasks to your application.

Multiprocessing Services 2.1 runs on system software Mac OS 9 and later. All PowerPC Macintosh computers are supported..

Multiprocessing Services 2.1 is packaged as part of the Mac OS System file, so you cannot install version 2.1 on older versions of system software.

Multiprocessing Services allows your application to create preemptive tasks within your application’s process (or execution context). However, the individual applications are still cooperatively scheduled by the Process Manager. In Mac OS X, both applications and tasks created by applications will be preemptively scheduled. Multiprocessing Services is Carbon-compliant, so applications built following the Carbon specification can run transparently on both Mac OS 8&9 and Mac OS X systems.

Multiprocessing Services 2.0 was introduced with Mac OS 8.6. Unlike earlier versions of Multiprocessing Services, you can create and execute preemptive tasks with virtual memory turned on. Multiprocessing Services 2.0 runs on all Power Macintosh computers except for 6100/7100/8100 and 5200/6200 series computers.

Multiprocessing Services 1.0 functions can run on System 7.5.2 and later if the Multiprocessing Services 1.x shared library is available. Pre-2.0 versions of the library were installed as part of system software for Mac OS 8 through Mac OS 8.5 but must be explicitly installed for earlier releases. The 1.x versions of the Multiprocessing Services library can run on all PowerPC Macintosh computers.

For a listing of functions introduced with versions 1.0, 2.0, and 2.1 of Multiprocessing Services, see [Preemptive Task–Safe Mac OS System Software Functions](Preemptive%20Task%E2%80%93Safe%20Mac%20OS%20System%20Software%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrwfvjvomi).

Although you can in theory designate almost any type of code as a task, in practice you should use the following guidelines to make best use of the available processors and to avoid unnecessary bottlenecks.

- Tasks should generally perform faceless processing, such as calculation-intensive work or I/O operations.
- The work performed by a task should be substantially more than the time required to process the request and result notifications. If it takes much longer to notify a task and retrieve results than to execute the task itself, an application’s performance will be dramatically worse with multiprocessing. Assuming a typical intertask signaling time is 20-50 microseconds, your tasks should take at least 200-500 microseconds to execute. If you want to explicitly calculate the intertask signaling time, you can use the sample code provided in [Preemptive Task–Safe Mac OS System Software Functions](Preemptive%20Task%E2%80%93Safe%20Mac%20OS%20System%20Software%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrwfvjvomi).
- If your task needs to allocate memory in Mac OS 9 and earlier, you must allocate the memory prior to signaling the task, or use the function `MPAllocateAligned`.
- Tasks should not call 68K code. The 68K emulator runs only cooperatively within the Mac OS task, and not within any preemptive task. If you must call 68K code, you can do so using a remote procedure call. See [Making Remote Procedure Calls](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvomq) for more information.
- You can call only preemptive task–safe Mac OS system software functions directly from a task. See Multiprocessing Gestalt Constants and [Preemptive Task–Safe Mac OS System Software Functions](Preemptive%20Task%E2%80%93Safe%20Mac%20OS%20System%20Software%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrwfvjvomi) to determine which functions are preemptive task–safe. Other (unsafe) system software functions must be called indirectly through remote procedure calls. See [Making Remote Procedure Calls](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvomq) for more information.
- Tasks should not access low-memory global data. A task may be executing at any time, including when applications that did not create them are running.
- Tasks should not call into unknown code. If you allow third parties to specify a callback function, you should never call that function from a task, since you cannot control what the callback will do. Calling back into non-reentrant code could easily corrupt data or cause a system crash.
- Avoid global variables. The main cause of non-reentrancy is the manipulation of global data. Tasks that manipulate global variables, global states, or buffers pointed to by global variables must use synchronization techniques to prevent other tasks from attempting to do so at the same time. Read-only global data are allowed.
- Do not call any Multiprocessing Services functions at interrupt time unless you are signaling a notification mechanism. See [Notifying Tasks at Interrupt Time](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvomy) for more information.

You should always determine the availability of Multiprocessing Services before attempting to call any of its functions. If you are programming in C, you should do so by calling the Boolean macro `MPLibraryIsLoaded`. A return value of true indicates that the Multiprocessing Services library is present and available for use. [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvona) in [Creating Tasks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvooa) shows an example of using the `MPLibraryIsLoaded` macro.

You probably want your application to run even if Multiprocessing Services is not available, so you should specify a weak link to the Multiprocessing Services shared library. Doing so allows your application to run even if the shared library is not present.

You may want to determine the number of processors available on the host computer before creating any tasks. Typically, you would create one task per processor; even if only one processor is present, it is generally more efficient to assign faceless work to a task and have the cooperatively scheduled main application handle only user interaction.

Multiprocessing Services uses two functions to determine the number of processors. The function `MPProcessors` returns the number of physical processors available on the host computer. The function `MPProcessorsScheduled` returns the number of active processors available (that is, the number that are currently available to execute tasks). The number of active processors may vary over time (due to changing priorities, power consumption issues, and so on).

After determining how many processors are available, you can go ahead and create tasks for your application.

Each task must be a function that takes one pointer-sized parameter and returns a result of type `OSStatus` when it finishes. The input parameter can be any information that the task needs to perform its function. Some examples of input are:

- A message queue ID that indicates which queue the task should go to for information
- A pointer to a structure containing data to process
- A pointer to a C++ object
- A pointer to a task-specific block of memory through which the application can communicate information for the life of the task

You create a task by calling the function `MPCreateTask`. The code in Listing 2-1 shows how you can create a number of identical tasks. Identical tasks can be useful when you want to divide up a large calculation (such as a image filtering operation) among several processors to improve performance.

__Listing 2-1__  Creating tasks

```
#define kMPStackSize 0 // use default stack size
#define kMPTaskOptions 0 // use no options

typedef struct {
    long firstThing;
    long totalThings;
    } sWorkParams, *sWorkParamsPtr;

typedef struct {
    MPTaskID taskID;
    MPQueueID requestQueue;
    MPQueueID resultQueue;
    sWorkParams params;
    } sTaskData, *sTaskDataPtr;

sTaskDataPtr myTaskData;
UInt32 numProcessors;
MPQueueID notificationQueue;

void CreateMPTasks( void ) {

    OSErr theErr;
    UInt32 i;

    theErr = noErr;

    /* Assume single processor mode */
    numProcessors = 1;

    /* Initialize remaining globals */
    myTaskData = NULL;
    notificationQueue = NULL;

    /* If the library is present then create the tasks */
    if( MPLibraryIsLoaded() ) {
        numProcessors = MPProcessorsScheduled();
        myTaskData = (sTaskDataPtr)NewPtrClear
                ( numProcessors * sizeof( sTaskData ) );
        theErr = MemError();
        if( theErr == noErr  )
                theErr = MPCreateQueue( &notificationQueue );
        for( i = 0; i < numProcessors && theErr == noErr; i++ ) {
            if( theErr == noErr )
                    theErr = MPCreateQueue(&myTaskData[i].requestQueue );
            if( theErr == noErr )
                    theErr = MPCreateQueue(&myTaskData[i].resultQueue );
            if( theErr == noErr )
                    theErr = MPCreateTask( MyTask, &myTaskData[i],
                        kMPStackSize, notificationQueue,
                        NULL, NULL, kMPTaskOptions,
                        &myTaskData[i].taskID );
            }
        }

/* If something went wrong, just go back to single processor mode */
    if( theErr != noErr ) {
        StopMPTasks();
        numProcessors = 1;
        }
    }
```

The `sTaskData` structure defines a number of values to be used with the task, such as the task ID, the IDs of the message queues used with the task, and a pointer to parameters to pass to the task. A pointer to a structure of this type is passed in the function `MPCreateTask`.

The variable `notificationQueueID` holds the ID of the notification queue to associate with the tasks. When a task terminates, it sends a message to this queue. After sending a termination request, the application typically polls this queue to determine when the task has actually terminated.

The `CreateMPTasks` function creates as many identical tasks as there are available processors (as stored in `numProcessors`). If for some reason the tasks cannot be created (for example, if Multiprocessing Services is not available), the variable `numProcessors` is set to 1 and the application should do the work of the tasks itself without making any Multiprocessing Services calls.

Before creating the tasks, `CreateMPTasks` calls the function `MPCreateQueue` to create a notification queue to be used by all the tasks. It then calls the Memory Manager function `NewPtrClear` to allocate memory for all the `myTaskData` structures required (in the case of this example, one per task).

Next, `CreateMPTasks` iterates over the number of requested tasks. For each iteration, it does the following:

- Makes two calls to `MPCreateQueue` to create a request queue and a result queue for each task. The IDs for these queues are stored in the task’s `myTaskData` structure.
- Fills out the `myTaskData` structure for that task as necessary.
- Calls the function `MPCreateTask`. When calling this function, you must specify the following values:

  - the entry point of the task and its input parameters
  - the size of the stack to associate with the task
  - the notification queue to associate with the task (by passing the ID of the queue obtained in the function `MPCreateQueue`.)

Each task is assigned its own unique ID, which is passed back in the `taskID` field of the `myTaskData` task structure.

Although not a requirement, you can assign a relative weight to each task by calling the function `MPSetTaskWeigh`. The task weight is a value that indicates the amount of processor attention to give this task relative to all other eligible tasks. If, as in this example, you create a number of identical tasks, each would probably be given equal weight.

The sample task in Listing 2-2 calls one of two different functions depending on the request is placed on its queue.

__Listing 2-2__  A sample task

```swift
#define kMyRequestOne                   1
#define kMyRequestTwo                   2

#define kMyResultException      -1

OSStatus MyTask( void *parameter ) {

    OSErr theErr;
    sTaskDataPtr p;
    Boolean finished;
    UInt32 message;

    theErr = noErr;

    /* Get a pointer to this task's unique data */
    p = (sTaskDataPtr)parameter ;

    /* Process each request handed to the task and return a result */
    finished = false;
    while( !finished ) {
        theErr = MPWaitOnQueue( p->requestQueue, (void **)&message,
                NULL, NULL, kDurationForever );
        if( theErr == noErr ) {
/* Pick a function to call and pass in the parameters.  */
/* The parameters should be set up prior to sending the */
/* message just received. Note that we could also just  */
/* pass in a pointer to the desired function instead of */
/* using a selector.                                                    */
            switch( message ) {
                case kMyRequestOne:
                    theErr = fMyTaskFunctionOne( &p->params );
                    break;
                case kMyRequestTwo:
                    theErr = fMyTaskFunctionTwo( &p->params );
                    break;
                default:
                    finished = true;
                    theErr = kMyResultException;
                }
            MPNotifyQueue( p->resultQueue, (void *)theErr, NULL, NULL );
            }
        else
            finished = true;
        }

    /* Task is finished now */
    return( theErr );
    }
```

This task takes one parameter, a pointer to its task data structure. This structure contains all the information that is needed for the life of the task, such as the request and result queues created for it, and any input necessary when processing a task request. The input parameters are passed along to the requested function.

After some initialization, the task sets the `finished` flag to `false` and then spends the rest of its time in a `while` loop processing message requests. The task calls the function `MPWaitOnQueue`, which waits indefinitely until a message appears on its request queue. In this case, the message indicates which function the task is to call. When a message is received, `MyTask` checks the request message to determine which function is desired and calls through to that function. Upon return, it posts a message on the result queue by calling `MPNotifyQueue` and then calls `MPWaitOnQueue` again to wait for the next message.

Note that if you are creating tasks on-the-fly, you may want to have your task dispose of its task record (pointed to by `p`) upon completion of the task. For more information about allocating and disposing of memory in tasks, see [Allocating Memory in Tasks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvonq).

In general, you should avoid terminating a task directly. Instead, you should let the task exit normally, either because it has finished its assigned work, or because you posted a quit notification. Doing so allows the task to dispose of any resources or structures it may have allocated. In addition, in Mac OS X, MP tasks may use additional system resources that do not expect to have the task abruptly terminated.

If you must terminate a task, you should call the function `MPTerminateTask`, ideally when the task is blocked waiting on an MP synchronization construct (queue, event, semaphore, or critical region). Doing so deletes the task, but you are still responsible for disposing of any memory you may have allocated for the task. In addition, because the tasks run asynchronously, the task may not actually terminate until sometime after the `MPTerminateTask` function returns. Therefore, you should not assume that the task has terminated until you have received a termination message from the notification queue you specified in the function `MPCreateTask`. See the discussion of `MPTerminateTask` in _[Multiprocessing Services Reference](https://developer.apple.com/documentation/coreservices/carbon_core/multiprocessing_services)_ in Carbon Process Management documentation for additional considerations.

Listing 2-3 shows how you might terminate the tasks created in [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvona).

__Listing 2-3__  Terminating tasks

```
void StopMPTasks(void)
{
    UInt32 i;

    if (myTaskData != NULL)
    {
        for (i = 0; i < numProcessors; i++)
        {
            if (myTaskData[i].TaskID != NULL)
            {
                MPTerminateTask(myTaskData[i].TaskID, noErr);
                MPWaitOnQueue(notificationQueue, NULL, NULL, NULL,
                    kDurationForever);
            }

            if (myTaskData[i].fRequestQueue != NULL)
                MPDeleteQueue(myTaskData[i].RequestQueue);
            if (myTaskData[i].fResultQueue != NULL)
                MPDeleteQueue (myTaskData[i].ResultQueue);
        }

        if (notificationQueue != NULL)
        {
            MPDeleteQueue (notificationQueue);
            notificationQueue = NULL;
        }

        DisposePtr((Ptr)myTaskData);
        myTaskData = NULL;
    }
}
```

The `StopMPTasks` function iterates through all the task data structures that were created in `CreateMPTasks` and checks for those with valid task IDs. It then calls the function `MPTerminateTask` for each valid task ID.

After making the termination call, `StopMPTasks` then waits for a message to appear on the notification queue indicating that the task has in fact been terminated. It does so by waiting continuously on the notification queue until the termination message arrives. It then clears the task ID and disposes of the queues allocated for the task.

After terminating all the existing tasks, `StopMPTasks` then deletes the notification queue and disposes of the task data structures.

As described in [About Multitasking on the Mac OS](About%20Multitasking%20on%20the%20Mac%20OS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenryfvjvomi) tasks often need to coordinate with the main application or with other tasks to avoid data corruption or synchronization problems. To coordinate tasks, Multiprocessing Services provides three simple notification mechanisms (semaphores, event groups, and message queues), one complex one (kernel notifications), and critical regions.

Of the three simple notification mechanisms, message queues are the easiest to use, but they are the slowest. Typically a task has two message queues associated with it. It takes messages off an input queue, processes the information accordingly, and, when done, posts a message to an output queue.

Before notifying a task, your application should make sure that everything the task needs is in memory. That is, you should have created any necessary queues and allocated space for any data the task may require. For each task, your application establishes the parameters of the work that it wants the task to perform and then it must signal the task through either a queue or a semaphore to begin performing that work. The specific work that the task is to perform can be completely defined within a message, or possibly within a block of memory reserved for that task. You can also pass in a pointer to the function that the task should call to perform the work. Doing so allows one task to perform many different types of chores.

Listing 2-4 shows a function that divides up a large amount of data among multiple tasks, placing requests on each task’s request queue and waiting for the results.

__Listing 2-4__  Assigning work to tasks

```
OSErr NotifyTasks( UInt32 realFirstThing, UInt32 realTotalThings ) {

    UInt32 i;
    OSErr theErr;
    UInt32 thingsPerTask;
    UInt32 message;
    sWorkParams appData;

    theErr = noErr;

    thingsPerTask = realTotalThings / numProcessors;

    /* Start each task working on a unique piece of the total data */
    for( i = 0; i < numProcessors; i++ ) {
        myTaskData[i].params.firstThing =
                                    realFirstThing + thingsPerTask * i;
        myTaskData[i].params.totalThings = thingsPerTask;
        message = kMyRequestOne;
        MPNotifyQueue( myTaskData[i].requestQueue, (void *)message,
            NULL, NULL );
        }

    /* Now wait for the tasks to finish */
    for( i = 0; i < numProcessors; i++ )
        MPWaitOnQueue( myTaskData[i].resultQueue, (void **)&message,
            NULL, NULL, kDurationForever );

    return( theErr );
}
```

For each task, it calls `MPNotifyQueue` to place the pointer to the task’s portion of the data on the task’s request queue. It then calls `MPWaitOnQueue` to wait for confirmation that the task has completed.

If you want to use semaphores or event groups instead of message queues, you would call the following functions to set up, notify, and wait on them, in a manner similar to that shown in [Listing 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvooi):

- `MPCreateSemaphore`, `MPSignalSemaphore`, `MPWaitOnSemaphore`, and `MPDeleteSemaphore` for semaphores
- `MPCreateEvent`, `MPSetEvent`, `MPWaitForEvent`, and `MPDeleteEvent` for event groups

However, if you use the simpler notification mechanisms, you have to find another way to pass the function pointer to the task. One possibility is to assign the pointer to a field in the task’s task data structure.

To use kernel notifications, you should call the following functions:

- `MPCreateNotification`, `MPCauseNotification`, `MPModifyNotification`, and `MPDeleteNotification`

There is no function for waiting on a kernel notification, as the task would wait on the appropriate subcomponents of the kernel notification (for example, a semaphore and a message queue).

Note that the example in [Listing 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvooi) will wait forever (`kDurationForever`) for a message to appear on its result queue. While this method is fine if called from a preemptive task, it can cause problems if called from a cooperative task. If the task takes a significant amount of time to execute, the calling task “hangs” for that time, since it can’t call `WaitNextEvent` to give other applications processor time. If you want to wait on a task from a cooperative task, your application should post the message and then return to its event loop. From within the event loop it can then poll the result queue using `kDurationImmediate` waits until a message appears.

If you specify `kDurationImmediate` for the waiting time for either `MPWaitOnQueue`, `MPWaitOnSemaphore`, `MPWaitForEvent`, or `MPEnterCriticalRegion`, the function always returns immediately. If the return value is `kMPTimeoutErr`, then the task generated no new results since the last time the application checked. That is, no message was available, the semaphore was zero, or the critical region was being executed by another processor. If the value is `noErr`, a result was present and obtained by the call.

You can use notification mechanisms to do more than simply signal tasks. For example, Listing 2-5 shows a task that uses a semaphore to do periodic actions.

__Listing 2-5__  Using a semaphore to perform periodic actions

```
void MyTask(void) {

    MPSemaphoreID delay;

    MPCreateSemaphore(1, 0, &delay); // a binary semaphore
    while(true)
        {
            DoIt();    // do something interesting
            (void) MPWaitOnSemaphore(delay, 10 * kDurationMillisecond);
            }
    }
```

This example uses a semaphore solely to create a delay. After each call to the `DoIt` function, `MyTask` waits for a notification that never arrives and times out after 10ms.

You can combine the delaying and notification aspects of a semaphore to add more flexibility as shown in Listing 2-6.

__Listing 2-6__  Performing actions periodically and on demand

```
main(void) {

    MPSemaphoreID delay;
    …
    MPCreateSemaphore(2, 0, &delay);
    MPCreateTask(…);

    while(true) {
        // Event loop.

        if ( /* something important happened */ )
            {
                MPSignalSemaphore(delay);
                }

            }
}

void MyTask(void) {

    while(true) {
        DoIt();    // Do interesting things.
        (void) MPWaitOnSemaphore(work, 100 * kDurationMillisecond);
        }
    }
```

In this example, the `MyTask` task runs essentially as before, except that the main application creates the semaphore. If no signal is sent to the semaphore, the `DoIt` function in `MyTask` executes every 100ms. However, in this example the application can signal the semaphore, which unblocks the task and allows the `DoIt` function to execute. That is, the `DoIt` function executes whenever the application signals the semaphore, or every 100ms otherwise.

If you want to send a notification to a task from a 68K-style interrupt handler, you can do so using the functions `MPSignalSemaphore`, `MPSetEvent`, or `MPNotifyQueue`. The `MPSignalSemaphore` and `MPSetEvent` functions are always interrupt-safe, while the `MPNotifyQueue` function becomes interrupt-safe if you reserve notifications on the message queue. See the `MPSetQueueReserve` function description for more information about reserving notifications.

If your tasks need access to code that is non-reentrant, (that is, only one task can be executing the code at any particular time), you must designate that code as being a critical region. You do so by calling the function `MPCreateCriticalRegion`. Doing so returns a critical region ID that you use to identify the region when you want to enter or exit it later. To enter a critical region, the task must call `MPEnterCriticalRegion` and specify the ID of the region to enter. This function acts much like the functions that wait on message queues and semaphores; if the critical region is not currently available, the task can wait for a specified time for it to become available (after which it will time out).

After the task has completed using the critical region, you must call `MPExitCriticalRegion`. Doing so “frees” the critical region so that another task that is waiting on it can enter. Note that a task can call `MPEnterCriticalRegion` multiple times during execution (as in a recursive call) as long as it balances each such call with `MPExitCriticalRegion` when it leaves the critical region.

Note that the area of code designated as a critical region is not “tagged” as such in any way. You must make sure that your code is synchronized to properly isolate the critical region. For example, if you have a critical region that will be shared by two different tasks, you must create the critical region outside the tasks that will require it and pass the critical region ID to the tasks. This method ensures that, even if multiple instances of a task were created and running, only one could access a particular critical region at a time.

If a task contains more than one critical region, each critical region must have its own unique ID; otherwise, a task entering a critical region may block another task from entering a different critical region.

In Mac OS X, if you need to allocate memory for a task, you can use `malloc` or the usual Core Foundation allocator functions, and free it using `free` or `CFRelease` respectively.

However, in Mac OS 9 and earlier, you must call the function `MPAllocateAligned`. Doing so returns a pointer to allocated memory with the alignment you specify. Prior to Mac OS X, you should always use the Multiprocessing Services memory allocation functions if your task needs to allocate, deallocate, or otherwise manipulate memory. For example, if your task deallocates its task data structure after it has finished processing, it must call `MPFree`. Note however, that since the memory is being deallocated by a preemptive task, you must have initially allocated the task record by calling `MPAllocateAligned`, even if this allocation didn’t occur in a preemptive task.

Task-specific storage is useful for storing small pieces of data, such as pointers to task-specific information. For example, if you create several identical tasks, each of which requires some unique data, you can store that data as task-specific storage. Task-specific storage locations are cross-referenced by an index value and the task ID, so the same code can easily refer to “per-instance” variables. Each such storage location holds a pointer-sized value.

Task-specific storage is automatically allocated when a task is created; the amount is fixed and cannot change for the life of the task. To access the task-specific storage, you call the function `MPAllocateTaskStorageIndex`. Doing so returns an index number which references a storage location in each available task in the process. Subsequent calls to `MPAllocateTaskStorageIndex` return new task index values to access more of the task-specific storage. Note that, aside from the fact that each index value is unique, you should not assume anything about the actual values of the index. For example, you cannot assume that successive calls to `MPAllocateTaskStorageIndex` will monotonically increase the index value.

Since the amount of task-specific storage is fixed, you may use up the available storage (and corresponding index values) if you make many `MPAllocateTaskStorageIndex` calls. In such cases, further calls to `MPAllocateTaskStorageIndex` return an error indicating insufficient resources.

You call `MPSetTaskStorageValue` and `MPGetTaskStorageValue` to set and retrieve the storage data. After you are finished using the storage locations, you must call `MPDeallocateTaskStorageIndex` to free the index.

On occasion you may want to use timers in your preemptive tasks. For example, say you want a task to send a message to a given queue every 20 milliseconds. To do so, you can set a timer to block your task for 20ms after sending the notification by calling the function `MPDelayUntil`.

In addition, you can create timers that will signal a specified notification mechanism after the timer expires. For example, say you have a task that is prompting the user to enter a name and password. Once you bring up the input dialog box, you may have another task (or the application) create a timer object to expire after five minutes. If the user has not entered a password during those five minutes, the timer expires and sends a message to the task, signaling that it should terminate.

You create a timer using the function `MPCreateTimer` and arm it by calling the function `MPArmTimer`. To specify the notification mechanisms to signal when the timer expires, you call the function `MPSetTimerNotify`. Note that you can signal one notification mechanism of each type if desired. For example, the timer can send a message to a queue and also set a bit in an event group when it expires.

The timers in Multiprocessing Services use time units of type `AbsoluteTime`, which increases monotonically since the host computer was started up. You can obtain the time since startup by calling the function `UpTime`. Multiprocessing Services also provides the functions `DurationToAbsolute` and `AbsoluteToDuration`which let you convert time between units of `AbsoluteTime` and units of type `Duration`. Note that you should not make any assumptions about what the `AbsoluteTime` units are based upon.

At times a preemptive task may need to call a system software function, and doing so may cause problems. For example, many calls to Mac OS system software manipulate global variables, so data could easily be corrupted if more than one task attempts to make similar calls. To work around this problem, Multiprocessing Services allows you to make remote procedure calls if you need to call system software from a preemptive task. A remote procedure call also allows your task to call 68K code.

To make a remote procedure call, you must designate an application-defined function that will make the actual calls to system software. You then pass a pointer to this function as well as any required parameters in the `MPRemoteCall` function.

When you call the function `MPRemoteCall` from a task, that task is blocked, and the application-defined function you designated then executes as a cooperatively scheduled task, which can make system software calls with no danger.

Note that when you call `MPRemoteCall`, you can designate which context (or process) you want your application-defined function to execute in. If you specify that the function should execute in the same context that owns the task, the function has access to data available to the main application (just as if the application had called the function). However, the function cannot execute until the owning context becomes active (and then not until the application calls `WaitNextEvent`). Alternatively, you can designate that the function execute in any available context. Doing so minimizes possible lag time, but the function cannot access any resources specific to the task’s context.

After your application-defined function returns, the task is unblocked and execution proceeds normally.

Multiprocessing Services provides a number of functions you can use to handle exceptions and to aid in debugging.

By default, if you do not register an exception handler, and no debuggers are registered, a task terminates when it takes an exception. If debuggers or exception handlers exist, then the task is suspended when an exception occurs and a message is sent to the appropriate debugger or handler.

If desired, you can install an exception handler for a task by calling the function `MPSetExceptionHandler`. When an exception occurs, a message is sent to a designated queue, which your exception handler can wait upon.

In addition, you can register one or more debuggers with Multiprocessing Services by calling the function `MPRegisterDebugger`. When calling `MPRegisterDebugger`, you must specify the queue to which you want the exception message to be sent as well as a debugger level. The debugger level is simply an integer that indicates where to place this debugger in the hierarchy of registered debuggers. In addition, When an exception occurs, the order of notification for handlers is as follows:

- The debugger with the highest debugger level (for example, a debugger registered at level 3 will have precedence over one registered as level 2).
- The debugger with the next highest level (and so on, for all the registered debuggers).
- The task’s exception handler.
- The task’s termination function.

At each level, the handler can choose to do either of the following:

- Set or retrieve the task’s register or stack information using `MPSetTaskState` or `MPExtractTaskState`.
- Call `MPDisposeTaskException`, which allows you to do any of the following:

  - Resume the task.
  - Resume the task and enable single-stepping or branch-stepping.
  - Propagate the exception to the next lower level. For example, instead of handling the exception itself, a debugger can pass the exception message to the next debugger (or exception handler) in the hierarchy.

If you want to throw an exception to a task, you can use the `MPThrowException` function.

[Next](Preemptive%20Task%E2%80%93Safe%20Mac%20OS%20System%20Software%20Functions.md)[Previous](About%20Multitasking%20on%20the%20Mac%20OS.md)

