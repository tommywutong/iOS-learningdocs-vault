---
title: File System Events Programming Guide
apple_id: TP40005289
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/FSEvents_ProgGuide/UsingtheFSEventsFramework/UsingtheFSEventsFramework.html
archived_at: '2026-07-15T07:23:04.164822Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Events Programming Guide](Introduction.md)


[Next](File%20System%20Event%20Security.md)[Previous](Technology%20Overview.md)

# Using the File System Events API

The File System Events API consists of several distinct groups of functions. You can obtain general information about volumes and events by using functions that begin with `FSEvents`. You can create a new event stream, perform operations on the stream, and so on using functions that begin with `FSEventStream`.

The life cycle of a file system events stream is as follows:

1. The application creates a stream by calling [FSEventStreamCreate](https://developer.apple.com/documentation/coreservices/1443980-fseventstreamcreate) or [FSEventStreamCreateRelativeToDevice](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev).
2. The application schedules the stream on the run loop by calling [FSEventStreamScheduleWithRunLoop](https://developer.apple.com/documentation/coreservices/1447824-fseventstreamschedulewithrunloop).
3. The application tells the file system events daemon to start sending events by calling [FSEventStreamStart](https://developer.apple.com/documentation/coreservices/1448000-fseventstreamstart).
4. The application services events as they arrive. The API posts events by calling the callback function specified in step 1.
5. The application tells the daemon to stop sending events by calling [FSEventStreamStop](https://developer.apple.com/documentation/coreservices/1447673-fseventstreamstop).
6. If the application needs to restart the stream, go to step 3.
7. The application unschedules the event from its run loop by calling [FSEventStreamUnscheduleFromRunLoop](https://developer.apple.com/documentation/coreservices/1441982-fseventstreamunschedulefromrunlo).
8. The application invalidates the stream by calling [FSEventStreamInvalidate](https://developer.apple.com/documentation/coreservices/1446990-fseventstreaminvalidate).
9. The application releases its reference to the stream by calling [FSEventStreamRelease](https://developer.apple.com/documentation/coreservices/1445989-fseventstreamrelease).

These steps are explained in more detail in the sections that follow.

Before you use the file system event stream API, you must include the Core Services framework as follows:

```c
#include <CoreServices/CoreServices.h>
```

When you compile, you must include the Core Services Framework by adding it to your target in Xcode or by adding the flag `-framework CoreServices` to your linker flags on the command line or in a Makefile.

The file system events API supports two types of event streams: per-disk event streams and a per-host event streams. Before you can create a stream, you must decide which type of stream to create: a per-host event stream or a per-disk event stream. You can create these streams by calling the functions [FSEventStreamCreate](https://developer.apple.com/documentation/coreservices/1443980-fseventstreamcreate) and [FSEventStreamCreateRelativeToDevice](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev), respectively.

A per-host event stream consists of events whose IDs are increasing with respect to other events on that host. These IDs are guaranteed to be unique with one exception: if additional disks are added from another computer that was also running OS X v10.5 or later, historical IDs may conflict between these volumes. Any new events will automatically start after the highest-numbered historical ID for any attached drive.

A per-disk event stream, by contrast, consists of events whose IDs are increasing with respect to previous events on that disk. It does not have any relationship with other events on other disks, and thus you must create a separate event stream for each physical device that you wish to monitor.

In general, if you are writing software that requires persistence, you should use per-disk streams to avoid any confusion due to ID conflicts. By contrast, per-host streams are most convenient if you are monitoring for changes in a directory or tree of directories during normal execution, such as watching a queue directory.

If you are monitoring files on the root file system, either stream mechanism will behave similarly.

For example, the following snippet shows how to create an event stream:

```
    /* Define variables and create a CFArray object containing
       CFString objects containing paths to watch.
     */
    CFStringRef mypath = CFSTR("/path/to/scan");
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&mypath, 1, NULL);
    void *callbackInfo = NULL; // could put stream-specific data here.
    FSEventStreamRef stream;
    CFAbsoluteTime latency = 3.0; /* Latency in seconds */

    /* Create the stream, passing in a callback */
    stream = FSEventStreamCreate(NULL,
        &myCallbackFunction,
        callbackInfo,
        pathsToWatch,
        kFSEventStreamEventIdSinceNow, /* Or a previous event ID */
        latency,
        kFSEventStreamCreateFlagNone /* Flags explained in reference */
    );
```

Once you have created an event stream, you must schedule it on your application’s run loop. To do this, call `FSEventStreamScheduleWithRunLoop`, passing in the newly-created stream, a reference to your run loop, and a run loop mode. For more information about run loops, read _[Run Loops](../../Core%20Foundation/Run%20Loops/Introduction%20to%20Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeztk2i)_.

If you don’t already have a run loop, you will need to devote a thread to this task. After creating a thread using your API of choice, call [CFRunLoopGetCurrent](https://developer.apple.com/documentation/corefoundation/1542428-cfrunloopgetcurrent) to allocate an initial run loop for that thread. Any future calls to [CFRunLoopGetCurrent](https://developer.apple.com/documentation/corefoundation/1542428-cfrunloopgetcurrent) will return the same run loop.

For example, the following snippet shows how to schedule a stream, called `stream`, on the current thread’s run loop (not yet running):

```
    FSEventStreamRef stream;
    /* Create the stream before calling this. */
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(),         kCFRunLoopDefaultMode);
```

The final step in setting up an event stream is to call `FSEventStreamStart`. This function tells the event stream to begin sending events. Its sole parameter is the event stream to start.

Once the event stream has been created and scheduled, if your run loop is not already running, you should start it by calling [CFRunLoopRun](https://developer.apple.com/documentation/corefoundation/1542011-cfrunlooprun).

Your event handler callback must conform to the prototype for [FSEventStreamCallback](https://developer.apple.com/documentation/coreservices/fseventstreamcallback). The parameters are described in the reference documentation for the `FSEventStreamCallback` data type.

Your event handler receives three lists: a list of paths, a list of identifiers, and a list of flags. In effect, these represent a list of events. The first event consists of the first entry taken from each of the arrays, and so on. Your handler must iterate through these lists, processing the events as needed.

For each event, you should scan the directory at the specified path, processing its contents as desired. Normally, you need to scan only the exact directory specified by the path. However, there are three situations in which this is not the case:

- If an event in a directory occurs at about the same time as one or more events in a subdirectory of that directory, the events may be coalesced into a single event. In this case, you will receive an event with the [kFSEventStreamEventFlagMustScanSubDirs](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagmustscansubdirs) flag set. When you receive such an event, you must recursively rescan the path listed in the event. The additional changes are not necessarily in an immediate child of the listed path.
- If a communication error occurs between the kernel and the user-space daemon, you may receive an event with either the [kFSEventStreamEventFlagKernelDropped](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagkerneldropped) or [kFSEventStreamEventFlagUserDropped](https://developer.apple.com/documentation/coreservices/kfseventstreameventflaguserdropped) flag set. In either case, you must do a full scan of any directories that you are monitoring because there is no way to determine what may have changed.
- If the root directory that you are watching is deleted, moved, or renamed (or if any of its parent directories are moved or renamed), the directory may cease to exist. If you care about this, you should pass the flag [kFSEventStreamCreateFlagWatchRoot](https://developer.apple.com/documentation/coreservices/kfseventstreamcreateflagwatchroot) when creating the stream. In this case, you will receive an event with the flag [kFSEventStreamEventFlagRootChanged](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagrootchanged) and an event ID of zero (`0`). In this case, you must rescan the entire directory because it may not exist.

  If you need to figure out where the directory moved, you should open the root directory with `open`, then pass `F_GETPATH` to [fcntl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fcntl.2.html#//apple_ref/doc/man/2/fcntl) to find its current path. See the manual page for [fcntl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fcntl.2.html#//apple_ref/doc/man/2/fcntl) for more information.
- If the number of events approaches 2^64, the event identifier will wrap around. When this happens, you will receive an event with the flag [kFSEventStreamEventFlagEventIdsWrapped](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflageventidswrapped). Fortunately, at least in the near term, this is unlikely to occur in practice, as 64 bits allows enough room for about one event per eraser-sized region on the Earth’s surface (including water) and would require about 2000 exabytes (2 million million gigabytes) of storage to hold them all. However, you should still check for this flag and take appropriate action if you receive it.

As part of your handler, you may sometimes need to obtain a list of paths being watched by the current event stream. You can obtain that list by calling [FSEventStreamCopyPathsBeingWatched](https://developer.apple.com/documentation/coreservices/1447917-fseventstreamcopypathsbeingwatch).

Sometimes, you may wish to monitor where you are in the stream. You might, for example, choose to do less processing if your code is slipping significantly behind. You can find out the latest event included in the current batch of events by calling [FSEventStreamGetLatestEventId](https://developer.apple.com/documentation/coreservices/1446030-fseventstreamgetlatesteventid) (or by examining the last event in the list). You can then compare this with the value returned by [FSEventsGetCurrentEventId](https://developer.apple.com/documentation/coreservices/1442917-fseventsgetcurrenteventid), which returns the highest numbered event in the system.

For example, the following code snippet shows a very simple handler.

```

void mycallback(
    ConstFSEventStreamRef streamRef,
    void *clientCallBackInfo,
    size_t numEvents,
    void *eventPaths,
    const FSEventStreamEventFlags eventFlags[],
    const FSEventStreamEventId eventIds[])
{
    int i;
    char **paths = eventPaths;

    // printf("Callback called\n");
    for (i=0; i<numEvents; i++) {
        int count;
        /* flags are unsigned long, IDs are uint64_t */
        printf("Change %llu in %s, flags %lu\n", eventIds[i], paths[i], eventFlags[i]);
   }
}
```


One of the most powerful features of file system events is their persistence across reboots. This means that your application can easily find out what happened since a particular time or a particular event in the distant past. By doing so, you can find out what files have been modified even when your application is not running. This can greatly simplify tasks such as backing up modified files, checking for changed dependencies in multi-file projects, and so on.

To work with persistent events, your application should regularly store the last event ID that it processes. Then, when it needs to go back and see what files have changed, it only needs to look at events that occurred after the last known event. To obtain all events since a particular event in the past, you pass the event ID in the `sinceWhen` argument to [FSEventStreamCreate](https://developer.apple.com/documentation/coreservices/1443980-fseventstreamcreate) or [FSEventStreamCreateRelativeToDevice](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev).]
[On a per-device basis, you can also easily use a timestamp to determine which events to include. To do this, you must first call [FSEventsGetLastEventIdForDeviceBeforeTime](https://developer.apple.com/documentation/coreservices/1449772-fseventsgetlasteventidfordeviceb) to obtain the last event ID `sinceWhen` argument to [FSEventStreamCreateRelativeToDevice](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev).

On a per-device basis, you can also easily use a time stamp to determine which events to include. To do this, you must first call [FSEventsGetLastEventIdForDeviceBeforeTime](https://developer.apple.com/documentation/coreservices/1449772-fseventsgetlasteventidfordeviceb) to obtain the last event ID for that device prior to the specified time stamp. You then pass the resulting value to [FSEventStreamCreateRelativeToDevice](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev). This is described further in [Special Considerations for Per-Device Streams](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobzfvbuqnbnknltg).

When working with persistent events, a commonly-used technique is to combine file system event notifications with a cached “snapshot” of the metadata of files within the tree. This process is described further in [Building a Directory Hierarchy Snapshot](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobzfvbuqnbnknlte).

File system events tell you that something in a given directory changed. In some cases, this is sufficient—for example, if your application is a print or mail spooler, all it needs to know is that a file has been added to the directory.

In some cases, however, this is not enough, and you need to know precisely what changed within the directory. The simplest way to solve this problem is to take a snapshot directory hierarchy, storing your own copy of the state of the system at a given point in time. You might, for example, store a list of filenames and last modified dates, thus allowing you to determine which files have been modified since the last time you performed a backup.

You do this by iterating through the hierarchy and building up a data structure of your choice. As you cache this metadata, if you see changes during the caching process, you can reread the directory or directories that changed to obtain an updated snapshot. Once you have a cached tree of metadata that accurately reflects the current state of the hierarchy you are concerned with, you can then determine what file or files changed within a directory or hierarchy (after a file system event notification) by comparing the current directory state with your snapshot.

OS X provides a number of APIs that can make this easier. The [scandir](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/scandir.3.html#//apple_ref/doc/man/3/scandir) function returns an array of directory entries that you can quickly iterate through. This is somewhat easier than reading a directory manually with [opendir](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/opendir.3.html#//apple_ref/doc/man/3/opendir), [readdir](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/readdir.3.html#//apple_ref/doc/man/3/readdir), and so on, and is slightly more efficient since you will always iterate through the entire directory while caching anyway.

The binary tree functions [tsearch](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tsearch.3.html#//apple_ref/doc/man/3/tsearch), [tfind](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tfind.3.html#//apple_ref/doc/man/3/tfind), [twalk](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/twalk.3.html#//apple_ref/doc/man/3/twalk), and [tdelete](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tdelete.3.html#//apple_ref/doc/man/3/tdelete) can simplify working with large search trees. In particular, binary trees are an easy way of quickly finding the cached file information from a particular directory. The following code snippet demonstrates the proper way to call these functions:

__Listing 2-1__  Using the tsearch, tfind, twalk, and tdelete API.

```c
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <search.h>

int array[] = { 1, 17, 2432, 645, 2456, 1234, 6543, 214, 3, 45, 34 };
void *dirtree;

static int cmp(const void *a, const void *b) {
    if (*(int *)a < *(int *)b) return -1;
    if (*(int *)a > *(int *)b) return 1;
    return 0;
}

void printtree(void);

/* Pass in a directory as an argument. */
int main(int argc, char *argv[])
{
    int i;
    for (i=0; i< sizeof(array) / sizeof(array[0]); i++) {
        void *x = tsearch(&array[i], &dirtree, &cmp);
        printf("Inserted %p\n", x);
    }

    printtree();

    void *deleted_node = tdelete(&array[2], &dirtree, &cmp);
    printf("Deleted node %p with value %d (parent node contains %d)\n",
        deleted_node, array[2], **(int**)deleted_node);

    for (i=0; i< sizeof(array) / sizeof(array[0]); i++) {
        void *node = tfind(&array[i], &dirtree, &cmp);
        if (node) {
            int **x = node;
            printf("Found %d (%d) at %p\n", array[i], **x, node);
        } else {
            printf("Not found: %d\n", array[i]);
        }
    }
    exit(0);
}

static void printme(const void *node, VISIT v, int k)
{
    const void *myvoid = *(void **)node;
    const int *myint = (const int *)myvoid;
    // printf("x\n");
    if (v != postorder && v != leaf) return;
    printf("%d\n", *myint);
}

void printtree(void)
{
    twalk(dirtree, &printme);
}
```

Two unusual design decisions in this API can make it tricky to use correctly if you haven’t used it before on other UNIX-based or UNIX-like operating systems:

- The [tsearch](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tsearch.3.html#//apple_ref/doc/man/3/tsearch) and [tdelete](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tdelete.3.html#//apple_ref/doc/man/3/tdelete) functions take the address of the tree variable, not the tree variable itself. This is because they must modify the value stored in the tree variable when they create or delete the initial root node, respectively.

  Even though [tfind](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tfind.3.html#//apple_ref/doc/man/3/tfind) does not modify the value of the root, it still takes the address of the root as its parameter, not the root pointer itself. A common mistake is to pass in the `dirtree` pointer. In fact, you must pass in `&dirtree` (the address of the `dirtree` pointer).
- The values passed to the callback by [twalk](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/twalk.3.html#//apple_ref/doc/man/3/twalk) and the values returned by [tfind](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tfind.3.html#//apple_ref/doc/man/3/tfind) and [tsearch](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tsearch.3.html#//apple_ref/doc/man/3/tsearch) are the address where the pointer to the data is stored, not the data value itself. Because this code passed in the address of an integer, it is necessary to dereference that value twice—once for the original `address-of` operator and once to dereference the pointer to that pointer that these functions return.

  Unlike the other functions, however, the function [tdelete](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tdelete.3.html#//apple_ref/doc/man/3/tdelete) does not return an address within the tree where the data is stored. This is because the data is no longer stored in the tree. Instead, it returns the _parent_ node of the node that it deleted.

The POSIX functions [stat](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/stat.2.html#//apple_ref/doc/man/2/stat) and [lstat](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/lstat.2.html#//apple_ref/doc/man/2/lstat) provide easy access to file metadata. These two functions differ in their treatment of symbolic links. The `lstat` function provides information about the link itself, while the `stat` function provides information about the file that the link points to. Generally speaking, when working with file system event notifications, you will probably want to use `lstat`, because changes to the underlying file will not result in a change notification for the directory containing the symbolic link to that file. However, if you are working with a controlled file structure in which symbolic links always point within your watched tree, you might have reason to use `stat`.

For an example of a tool that builds a directory snapshot, see the _[Watcher](../../../samplecode/Watcher/Watcher.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimbvgq)_ sample code.

When you no longer need a file system event stream, you should always clean up the stream to avoid leaking memory and descriptors. Before cleaning up, however, you must first stop the run loop by calling [FSEventStreamStop](https://developer.apple.com/documentation/coreservices/1447673-fseventstreamstop).

Next, you should call [FSEventStreamInvalidate](https://developer.apple.com/documentation/coreservices/1446990-fseventstreaminvalidate). This function unschedules the stream from all run loops with a single call. If you need to unschedule it from only a single run loop, or if you need to move the event stream between two run loops, you should instead call [FSEventStreamUnscheduleFromRunLoop](https://developer.apple.com/documentation/coreservices/1441982-fseventstreamunschedulefromrunlo). You can then reschedule the event stream, if desired, by calling [FSEventStreamScheduleWithRunLoop](https://developer.apple.com/documentation/coreservices/1447824-fseventstreamschedulewithrunloop).

Once you have invalidated the event stream, you can release it by calling [FSEventStreamRelease](https://developer.apple.com/documentation/coreservices/1445989-fseventstreamrelease). When the stream release and stream retain counts balance and there are no longer any occurances of the stream being retained, the stream will be freed.

There are three other cleanup-related functions that you should be aware of under certain circumstances. If your application needs to make certain that the file system has reached a steady state prior to cleaning up the stream, you may find it useful to flush the stream. You can do this with one of two functions: [FSEventStreamFlushAsync](https://developer.apple.com/documentation/coreservices/1441727-fseventstreamflushasync) and [FSEventStreamFlushSync](https://developer.apple.com/documentation/coreservices/1445629-fseventstreamflushsync).

When flushing events, the synchronous call will not return until all pending events are flushed. The asynchronous call will return immediately, and will return the event ID (of type [FSEventStreamEventId](https://developer.apple.com/documentation/coreservices/fseventstreameventid)) of the last event pending. You can then use this value in your callback function to determine when the last event has been processed, if desired.

The final function related to cleaning up is [FSEventsPurgeEventsForDeviceUpToEventId](https://developer.apple.com/documentation/coreservices/1447985-fseventspurgeeventsfordeviceupto). This function can only be called by the root user because it destroys the historical record of events on a volume prior to a given event ID. As a general rule, you should never call this function because you cannot safely assume that your application is the only consumer of event data.

If you are writing a specialized application (an enterprise backup solution, for example), it may be appropriate to call this function to trim the event record to some reasonable size to prevent it from growing arbitrarily large. You should do this _only_ if the administrator explicitly requests this behavior, however, and you should _always_ ask for confirmation (either before performing the operation or before enabling any rule that would cause it to be performed at a later time).

In addition to the considerations described in [Handling Events](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobzfvbuqnbnknltc), streams created with [FSEventStreamCreateRelativeToDevice](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev), per-device streams have some special characteristics that you should be aware of:

- All paths are relative to the root of the volume that you are monitoring, _not_ relative to the system root. This applies to both the path used when creating the stream and to any path that your callback receives as part of an event.
- Device IDs may not remain the same across reboots (particularly with removable devices). It is your responsibility to ensure that the volume you are looking at is the right one by comparing the UUID.

In addition to the functions provided for systemwide streams, you can obtain the UUID for the device associated with a stream by calling [FSEventStreamGetDeviceBeingWatched](https://developer.apple.com/documentation/coreservices/1449675-fseventstreamgetdevicebeingwatch).

You can obtain the unique ID for a device by calling [FSEventsCopyUUIDForDevice](https://developer.apple.com/documentation/coreservices/1444453-fseventscopyuuidfordevice). If this unique ID is different than the one obtained from a previous run, this can mean many things. It could mean that the user has two volumes with the same name, that the user has reformatted the volume with the same name, or that the event IDs have been purged for the volume. In any of these cases, any previous events for the volume do not apply to this particular volume, but they may still be valid for another volume.

If you find that the UUID for a volume matches what was stored on a previous run, but the event ID is lower than the last version you stored, this may mean that the user restored a volume from a backup, or it may mean that the IDs have wrapped around or have been purged. In either case, any stored events you may have for the device are invalid.

Finally, if you are using persistent events, you can also use the function [FSEventsGetLastEventIdForDeviceBeforeTime](https://developer.apple.com/documentation/coreservices/1449772-fseventsgetlasteventidfordeviceb) to find the last event prior to a time stamp. This event ID is persistent, and can be particularly useful for performing incremental backups.

The time format used is a [CFAbsoluteTime](https://developer.apple.com/documentation/corefoundation/cfabsolutetime) value, which is measured in seconds since January 1, 2001. For other timestamp formats, you must convert them to this format as follows:

- If you are writing a Cocoa application, you should use an [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate) object to perform any conversions, then use [CFDateGetAbsoluteTime](https://developer.apple.com/documentation/corefoundation/1542812-cfdategetabsolutetime) to obtain the corresponding `CFAbsoluteTime` value. (You can transparently pass an [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate) object as a [CFDateRef](https://developer.apple.com/documentation/corefoundation/cfdateref).)
- If you are starting with a POSIX timestamp in a non-Cocoa application, you should subtract [kCFAbsoluteTimeIntervalSince1970](https://developer.apple.com/documentation/corefoundation/kcfabsolutetimeintervalsince1970) from the value to convert to a `CFAbsoluteTime` value. Be sure to always use timestamps based on GMT.
- If you are working with a legacy Carbon timestamp in a non-Cocoa application, you would subtract [kCFAbsoluteTimeIntervalSince1904](https://developer.apple.com/documentation/corefoundation/kcfabsolutetimeintervalsince1904). Be sure to always use timestamps based on GMT.

For more information about date and time types, you should read _[Date and Time Programming Guide for Core Foundation](../../Core%20Foundation/Date%20and%20Time%20Programming%20Guide%20for%20Core%20Foundation/Introduction%20to%20Dates%20and%20Times%20Programming%20Guide%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdk2i)_.

[Next](File%20System%20Event%20Security.md)[Previous](Technology%20Overview.md)

