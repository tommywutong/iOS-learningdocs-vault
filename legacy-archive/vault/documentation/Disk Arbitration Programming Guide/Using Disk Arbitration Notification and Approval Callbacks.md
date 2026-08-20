---
title: Disk Arbitration Programming Guide
apple_id: TP40009310
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: DiskArbitration
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/DriversKernelHardware/Conceptual/DiskArbitrationProgGuide/ArbitrationBasics/ArbitrationBasics.html
archived_at: '2026-07-15T07:31:54.579095Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Disk Arbitration Programming Guide](About%20Disk%20Arbitration.md)


[Next](Manipulating%20Disks%20and%20Volumes.md)[Previous](About%20Disk%20Arbitration.md)

# Using Disk Arbitration Notification and Approval Callbacks

The most common way to use Disk Arbitration is to register for notifications and then take some action when those notifications occur. For example, when a new disk appears, you might ask if the user wants to use it as a backup destination. You can also register approval callbacks if your app needs to participate in the arbitration process—for example, helping decide whether a disk should be mounted or ejected.

This chapter tells how to use the notification and approval mechanisms provided by the Disk Arbitration framework, along with related concepts in the order in which you need to understand them when writing a disk arbitration client from scratch. If you do not want to use the notification or approval aspects of disk arbitration, skip to the next chapter, [Manipulating Disks and Volumes](Manipulating%20Disks%20and%20Volumes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgmjqfvbuqmznknltc).

If your app needs to register for notification or participate in the arbitration process, it must do the following:

1. Create a session object by calling `DASessionCreate`.
2. Register _notification callbacks_ if you want to know when a disk-related event happens, or register _approval callbacks_ if you want to actively participate in the arbitration process.
3. Schedule the session object on a run loop or dispatch queue (and start the run loop or dispatch queue, if necessary).
4. Handle any callbacks that your app receives.
5. When the app no longer needs to receive callbacks, unschedule the session object and release it.

The first thing you must do when writing a disk arbitration notification client is create a session ([DASessionRef](https://developer.apple.com/documentation/diskarbitration/dasessionref)). To create a disk arbitration session, call [DASessionCreate](https://developer.apple.com/documentation/diskarbitration/1501530-dasessioncreate), as shown below:

```
DASessionRef session;
session = DASessionCreate(kCFAllocatorDefault);
```


There are two types of callbacks supported by disk arbitration. _Notification callbacks_ tell you that something happened. _Approval callbacks_ allow you to prevent mount, unmount, or eject actions from happening.

There are four types of notification callbacks:

- [DADiskAppearedCallback](https://developer.apple.com/documentation/diskarbitration/dadiskappearedcallback)—called when a disk appears or a partition appears
- [DADiskDescriptionChangedCallback](https://developer.apple.com/documentation/diskarbitration/dadiskdescriptionchangedcallback)—called when a disk’s description has changed (and, in OS X v10.7 and later, when a volume is first mounted)
- [DADiskDisappearedCallback](https://developer.apple.com/documentation/diskarbitration/dadiskdisappearedcallback)—called when a removable disk is ejected
- [DADiskPeekCallback](https://developer.apple.com/documentation/diskarbitration/dadiskpeekcallback)—called when a disk is first probed, before automatic mounting begins, and before any other notifications are sent out)

Each has its own registration function ([DARegisterDiskAppearedCallback](https://developer.apple.com/documentation/diskarbitration/1492707-daregisterdiskappearedcallback), [DARegisterDiskDescriptionChangedCallback](https://developer.apple.com/documentation/diskarbitration/1492705-daregisterdiskdescriptionchanged), [DARegisterDiskDisappearedCallback](https://developer.apple.com/documentation/diskarbitration/1492696-daregisterdiskdisappearedcallbac), and [DARegisterDiskPeekCallback](https://developer.apple.com/documentation/diskarbitration/1492728-daregisterdiskpeekcallback)).

Most of these registration functions take a matching dictionary. You should usually pass `NULL` (to match all disks) or pass a standard matching dictionary such as [kDADiskDescriptionMatchMediaUnformatted](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchmediaunformatted). The detailed matching behavior of these matching dictionaries is shown in [Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgmjqfvbuqmrnknltcny).

__Table 1-1__  Explanation of standard matching dictionaries

| Standard dictionary | Contents | Description |
| [kDADiskDescriptionMatchMediaUnformatted](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchmediaunformatted) | `kDADiskDescriptionMediaSizeKey` with value of `0` | Matches unformatted media (such as a blank DVD). |
| [kDADiskDescriptionMatchMediaWhole](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchmediawhole) | `kDADiskDescriptionMediaWholeKey` with value `true` | Matches only whole-disk media (`/dev/disk0`, for example). |
| [kDADiskDescriptionMatchVolumeMountable](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchvolumemountable) | `kDADiskDescriptionVolumeMountableKey` with value `true` | Matches mountable volumes. |
| [kDADiskDescriptionMatchVolumeUnrecognized](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchvolumeunrecognized) | `kDADiskDescriptionVolumeMountableKey` with value `false` | Matches nonmountable disks. |

For example, to limit matching to USB-attached media, you might create a matching dictionary like this:

```
CFMutableDictionaryRef matchingDict =
    CFDictionaryCreateMutable(
        kCFAllocatorDefault,
        0,
        &kCFTypeDictionaryKeyCallBacks,
        &kCFTypeDictionaryValueCallBacks);

CFDictionaryAddValue(matchingDict,
    kDADiskDescriptionDeviceProtocolKey,
    CFSTR(kIOPropertyPhysicalInterconnectTypeUSB));
```

Additional interconnect types and other related constants are described in _[IOStorageProtocolCharacteristics.h User-Space Reference](https://developer.apple.com/documentation/iokit/iostorageprotocolcharacteristics.h_user_space)_.

Finally, you can pass arbitrary data to the callback whenever a disk event matches the specified matching dictionary (or dictionaries) and event type using the context pointer. By passing different context pointers, you can register the same callback multiple times with a different matching dictionary and provide information to the callback that indicates which registration matched. If you do not need to provide such contextual information, just pass `NULL` for this parameter.

The details of each callback are described in more detail in the sections that follow.

To watch for new disks or partitions, call [DARegisterDiskAppearedCallback](https://developer.apple.com/documentation/diskarbitration/1492707-daregisterdiskappearedcallback). For example:

```
void got_disk(DADiskRef disk, void *context);
...

void *context = NULL;

DARegisterDiskAppearedCallback(session,
    kDADiskDescriptionMatchVolumeMountable,
    got_disk, context);

void got_disk(DADiskRef disk, void *context)
{
    printf("Got new disk\n");
}
```

This example uses the [kDADiskDescriptionMatchVolumeMountable](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchvolumemountable) matching dictionary to limit callbacks to mountable disks. You can also limit callbacks to nonmountable disks or whole media partitions (`/dev/disk1`, for example). For a list of predefined dictionaries, see the documentation for `DiskArbitration.h`.

To be notified when a disk has been ejected (whether by the user ejecting it or unplugging the device), call [DARegisterDiskDisappearedCallback](https://developer.apple.com/documentation/diskarbitration/1492696-daregisterdiskdisappearedcallbac). For example:

```
void got_disk_removal(DADiskRef disk, void *context);

...

/* Match all volumes */
CFDictionaryRef matchingdictionary = NULL;
/* No context needed here. */
void *context = NULL;

DARegisterDiskDisappearedCallback(session,
    matchingdictionary,
    got_disk_removal,
    context);

...

void got_disk_removal(DADiskRef disk, void *context)
{
    printf("Disk removed: %s\n", DADiskGetBSDName(disk));
}
```


The disk description provides information about the disk, including whether it is formatted, the mount point, the volume name, and so on. You can watch for changes in this information by calling [DARegisterDiskDescriptionChangedCallback](https://developer.apple.com/documentation/diskarbitration/1492705-daregisterdiskdescriptionchanged).

When your callback gets called, it gets three values passed in: a reference to the disk (or partition), a [CFArrayRef](https://developer.apple.com/documentation/corefoundation/cfarray) object containing a list of keys that changed, and a context pointer that you passed in when you registered the callback.

For example, if you want to find out the new mount point (`/Volumes/My Disk/`, for example) after a volume gets renamed, you might watch for a change in the volume path by using the [kDADiskDescriptionWatchVolumePath](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionwatchvolumepath) matching dictionary.

```
void got_rename(DADiskRef disk, CFArrayRef keys, void *context);

...

CFMutableArrayRef keys = CFArrayCreateMutable(kCFAllocatorDefault, 0, NULL);
CFArrayAppendValue(keys, kDADiskDescriptionVolumeNameKey);

DARegisterDiskDescriptionChangedCallback(session,
    NULL, /* match all disks */
    keys, /* match the keys specified above */
    got_rename,

    NULL);

...


void got_rename(DADiskRef disk, CFArrayRef keys, void *context)
{
    CFDictionaryRef dict = DADiskCopyDescription(disk);
    CFURLRef fspath = CFDictionaryGetValue(dict, kDADiskDescriptionVolumePathKey);

    char buf[MAXPATHLEN];
    if (CFURLGetFileSystemRepresentation(fspath, false, (UInt8 *)buf, sizeof(buf))) {
        printf("Disk %s is now at %s\nChanged keys:\n", DADiskGetBSDName(disk), buf);
        CFShow(keys);
    } else {
        /* Something is *really* wrong. */
    }
}
```


To be notified when a new disk appears before automatic mounting occurs, use [DARegisterDiskPeekCallback](https://developer.apple.com/documentation/diskarbitration/1492728-daregisterdiskpeekcallback).

Unlike the previous notifications, when you register for a disk peek callback, you pass an extra parameter, `order`, which allows you to set the order in which your callbacks get called relative to other peek callbacks. Unless you have a reason to do otherwise, pass zero (`0`).

The following snippet shows how to use a disk peek callback to claim a volume. This technique is commonly used by software such as iTunes to claim blank media for its own use so that OS X does not ask the user what to do.

```
void got_disk(DADiskRef disk, void *context);
void myreleasecallback(DADiskRef disk, void *context);
void myclaimcallback(DADiskRef disk, DADissenterRef dissenter, void *context);

DARegisterDiskPeekCallback(session,
    kDADiskDescriptionMatchVolumeMountable,
    0,
    got_disk,
    NULL);

void got_disk(DADiskRef disk, void *context)
{
    printf("Got new disk\n");

    /* Claim the disk exclusively. */
    DADiskClaim(disk,
        kDADiskClaimOptionDefault,
        myreleasecallback,
        NULL,
        myclaimcallback,
        NULL /* Or optional context */
    );

    /* Do other stuff here... */
}
```


When you no longer need a notification callback, unregister it by calling [DAUnregisterCallback](https://developer.apple.com/documentation/diskarbitration/1492712-daunregistercallback). For example:

```
DAUnregisterCallback(session, mycallbackfuntion, NULL);
```

Be sure to pass in the original context pointer value that you used when you registered the function.

You can register approval callbacks in a disk arbitration in three ways, depending on when you want to be notified.

- If you want to be asked for permission before a disk is ejected, call [DARegisterDiskEjectApprovalCallback](https://developer.apple.com/documentation/diskarbitration/1492715-daregisterdiskejectapprovalcallb).
- If you want to be asked for permission before a volume is mounted, call [DARegisterDiskMountApprovalCallback](https://developer.apple.com/documentation/diskarbitration/1492762-daregisterdiskmountapprovalcallb).
- If you want to be asked for permission before a volume is unmounted, call [DARegisterDiskUnmountApprovalCallback](https://developer.apple.com/documentation/diskarbitration/1492698-daregisterdiskunmountapprovalcal).

Like the notification callbacks, these registration functions take four parameters: a session, a matching dictionary, a callback routine, and a context pointer.

For the matching dictionary, you generally pass `NULL` (to match all disks) or pass a standard matching dictionary such as [kDADiskDescriptionMatchMediaUnformatted](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchmediaunformatted). These standard dictionaries are documented in the Globals section of the documentation for `DiskArbitration.h`.

Finally, you can pass arbitrary data to the callback whenever a disk event matches the specified matching dictionary (or dictionaries) and event type using the context pointer. By passing different context pointers, you can register the same callback multiple times with a different matching dictionary and provide information to the callback that indicates which registration matched. If you do not need to provide such contextual information, just pass `NULL` for this parameter.

After you register a callback routine for a specific event type, whenever an event of that type occurs, Disk Arbitration calls your callback function, passing it the context pointer you specified earlier, along with a disk object (`DADiskRef`).

In your callback function, you should inspect the disk object as necessary to determine whether to allow the event (see [Manipulating Disks and Volumes](Manipulating%20Disks%20and%20Volumes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgmjqfvbuqmznknltc)). Then:

- Return `NULL` if you want to allow the operation to complete.
- Return a [DADissenterRef](https://developer.apple.com/documentation/diskarbitration/dadissenter) object to cancel the operation.

When you create the [DADissenterRef](https://developer.apple.com/documentation/diskarbitration/dadissenter) object, set the status to one of the status codes in `DAReturn`, and set the status string to a [CFStringRef](https://developer.apple.com/documentation/corefoundation/cfstringref) object containing an appropriate explanation.

For example:

```
DADissenterRef allow_mount(DADiskRef disk, void *context);

...

session = DASessionCreate(kCFAllocatorDefault);

DARegisterDiskMountApprovalCallback(session,
                NULL, /* Match all disks */
                allow_mount,
                NULL); /* No context */

...

DADissenterRef allow_mount(
        DADiskRef disk,
        void *context)
{
        int allow = 0;

        if (allow) {
                /* Return NULL to allow */
                fprintf(stderr, "allow_mount: allowing mount.\n");
                return NULL;
        } else {
                /* Return a dissenter to deny */
                fprintf(stderr, "allow_mount: refusing mount.\n");
                return DADissenterCreate(
                        kCFAllocatorDefault, kDAReturnExclusiveAccess,
                        CFSTR("It's mine!"));
        }
}
```


When you no longer need an approval callback, you should unregister it by calling [DAUnregisterApprovalCallback](https://developer.apple.com/documentation/diskarbitration/1492750-daunregisterapprovalcallback). For example:

```
DAUnregisterApprovalCallback(session, mycallbackfuntion, NULL);
```

Be sure to pass in the original context pointer value that you used when you registered the function.

The last thing you must do to make your callbacks actually get called is to schedule your disk arbitration session with the run loop or dispatch queue (and, if necessary, start the run loop). The way you schedule the session depends on whether you are using Grand Central Dispatch queues or a run loop (in Core Foundation or Foundation).

If you are using Grand Central Dispatch, you can schedule and unschedule your disk arbitration session by calling [DASessionSetDispatchQueue](https://developer.apple.com/documentation/diskarbitration/1501542-dasessionsetdispatchqueue), defined in `DASession.h`.

The following code snippet shows how to schedule sessions, unschedule sessions, and release the resources associated with the sessions:

```
/* Schedule the session on a dispatch queue. */
DASessionSetDispatchQueue(session, queue);

/* Unschedule the session on a dispatch queue. */
DASessionSetDispatchQueue(session, NULL);

/* Clean up the session resources. */
CFRelease(session);
```


If you are using a Core Foundation or Foundation run loop, you can schedule your disk arbitration session by calling [DASessionScheduleWithRunLoop](https://developer.apple.com/documentation/diskarbitration/1501544-dasessionschedulewithrunloop), defined in `DASession.h`.

The following code snippet shows how to schedule sessions with the run loop, start the run loop, unschedule the sessions, and release the resources associated with them:

```
/* Schedule a disk arbitration session. */
DASessionScheduleWithRunLoop(session,         CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

/* Start the run loop.  (Don't do this if you already have
   a running Core Foundation or Cocoa run loop.) */
CFRunLoopRun();

/* Clean up a session. */
DASessionUnscheduleFromRunLoop(session,
    CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);
CFRelease(session);
```

[Next](Manipulating%20Disks%20and%20Volumes.md)[Previous](About%20Disk%20Arbitration.md)

