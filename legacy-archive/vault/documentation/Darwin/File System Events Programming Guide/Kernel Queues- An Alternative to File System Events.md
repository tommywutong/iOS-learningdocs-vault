---
title: File System Events Programming Guide
apple_id: TP40005289
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/FSEvents_ProgGuide/KernelQueues/KernelQueues.html
archived_at: '2026-07-15T07:23:04.141558Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Events Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](File%20System%20Event%20Security.md)

# Kernel Queues: An Alternative to File System Events

The kernel queues API provides a way for an application to receive notifications whenever a given file or directory is modified in any way, including changes to the file’s contents, attributes, name, or length. Your application can also receive notification if you are watching a block or character device and access is revoked through a call to [revoke](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/revoke.2.html#//apple_ref/doc/man/2/revoke).

The kernel queues API also provides a way to monitor child processes and find out when they call [exit](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/exit.3.html#//apple_ref/doc/man/3/exit), `fork`, [exec](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/exec.3.html#//apple_ref/doc/man/3/exec), and so on. This use of kernel queues is beyond the scope of this document. For more information about kernel queues and processes, you should read the FreeBSD documentation for kernel queues. You can find links to this documentation at [http://people.freebsd.org/~jmg/kq.html](http://people.freebsd.org/~jmg/kq.html).

File system events are intended to provide notification of changes with directory-level granularity. For most purposes, this is sufficient. In some cases, however, you may need to receive notifications with finer granularity. For example, you might need to monitor only changes made to a single file. For that purpose, the kernel queue (kqueue) notification system is more appropriate.

If you are monitoring a large hierarchy of content, you should use file system events instead, however, because kernel queues are somewhat more complex than kernel events, and can be more resource intensive because of the additional user-kernel communication involved.

The kernel queues (kqueue) and kernel events (kevent) mechanism is extremely powerful and flexible, allowing you to receive a stream of kernel-level events (including file modifications) and to define a set of filters that limit which events are delivered to your application.

To use kernel queues, you must do four things:

- Create a kernel event queue by calling `kqueue(2) OS X Developer Tools Manual Page`. This function returns a file descriptor for a newly allocated event queue.
- Open a file descriptor for each file that you wish to watch.
- Create a list of events to watch for. To do this, use the [EV_SET](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/EV_SET.2.html#//apple_ref/doc/man/2/EV_SET) to fill in the fields of a kernel event structure. The prototype is as follows:

```
      EV_SET(&kev, ident, filter, flags, fflags, data, udata);
```

  The first argument, `kev`, is the address of the structure itself. The second, `ident`, contains a file descriptor for the file you are watching.

  The third argument, `filter`, contains the name of the kernel filter whose results you want to see. For example, you can use `EVFILT_VNODE` to monitor vnode operations on the file.

  The remaining arguments are all specific to a particular filter and are described in the manual page for [kevent](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/kevent.2.html#//apple_ref/doc/man/2/kevent).
- Call `kevent` in a loop. This function monitors the kernel event queue for events and stores them in a buffer that you provide. The prototype is as follows:

```

     int kevent(int kq, const struct kevent *changelist,
          int nchanges, struct kevent *eventlist,
          int nevents, const struct timespec *timeout);
```

  Its arguments are (in order) the queue file descriptor, the list of events to watch for (from the previous step), the number of events in that list, temporary storage space for the resulting event data, the size of that storage, and a timeout.

  On success, the `kevent` function returns the number of events returned. If the timeout expires before any event occurs, it returns 0. Depending on the nature of the error, errors may be reported either as an event with the `EV_ERROR` flag set and the system error stored in the `data` field or by returning -1 with the error stored in `errno`.

Listing A-1 is a brief example that shows how to monitor a single file using kernel queues. For a more complex example that monitors directories, look at the _[FileNotification](../../../samplecode/FileNotification/FileNotification.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjugm)_ sample code.

__Listing A-1__  Watch a File Using Kernel Queues

```c
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/event.h>
#include <sys/time.h>
#include <errno.h>
#include <string.h>
#include <inttypes.h>

#define NUM_EVENT_SLOTS 1
#define NUM_EVENT_FDS 1

char *flagstring(int flags);

int main(int argc, char *argv[])
{
    char *path = argv[1];
    int kq;
    int event_fd;
    struct kevent events_to_monitor[NUM_EVENT_FDS];
    struct kevent event_data[NUM_EVENT_SLOTS];
    void *user_data;
    struct timespec timeout;
    unsigned int vnode_events;

    if (argc != 2) {
        fprintf(stderr, "Usage: monitor <file_path>\n");
        exit(-1);
    }

    /* Open a kernel queue. */
    if ((kq = kqueue()) < 0) {
        fprintf(stderr, "Could not open kernel queue.  Error was %s.\n", strerror(errno));
    }

    /*
       Open a file descriptor for the file/directory that you
       want to monitor.
     */
    event_fd = open(path, O_EVTONLY);
    if (event_fd <=0) {
        fprintf(stderr, "The file %s could not be opened for monitoring.  Error was %s.\n", path, strerror(errno));
        exit(-1);
    }

    /*
       The address in user_data will be copied into a field in the
       event.  If you are monitoring multiple files, you could,
       for example, pass in different data structure for each file.
       For this example, the path string is used.
     */
    user_data = path;

    /* Set the timeout to wake us every half second. */
    timeout.tv_sec = 0;        // 0 seconds
    timeout.tv_nsec = 500000000;    // 500 milliseconds

    /* Set up a list of events to monitor. */
    vnode_events = NOTE_DELETE |  NOTE_WRITE | NOTE_EXTEND |                            NOTE_ATTRIB | NOTE_LINK | NOTE_RENAME | NOTE_REVOKE;
    EV_SET( &events_to_monitor[0], event_fd, EVFILT_VNODE, EV_ADD | EV_CLEAR, vnode_events, 0, user_data);

    /* Handle events. */
    int num_files = 1;
    int continue_loop = 40; /* Monitor for twenty seconds. */
    while (--continue_loop) {
        int event_count = kevent(kq, events_to_monitor, NUM_EVENT_SLOTS, event_data, num_files, &timeout);
        if ((event_count < 0) || (event_data[0].flags == EV_ERROR)) {
            /* An error occurred. */
            fprintf(stderr, "An error occurred (event count %d).  The error was %s.\n", event_count, strerror(errno));
            break;
        }
        if (event_count) {
            printf("Event %" PRIdPTR " occurred.  Filter %d, flags %d, filter flags %s, filter data %" PRIdPTR ", path %s\n",
                event_data[0].ident,
                event_data[0].filter,
                event_data[0].flags,
                flagstring(event_data[0].fflags),
                event_data[0].data,
                (char *)event_data[0].udata);
        } else {
            printf("No event.\n");
        }

        /* Reset the timeout.  In case of a signal interrruption, the
           values may change. */
        timeout.tv_sec = 0;        // 0 seconds
        timeout.tv_nsec = 500000000;    // 500 milliseconds
    }
    close(event_fd);
    return 0;
}

/* A simple routine to return a string for a set of flags. */
char *flagstring(int flags)
{
    static char ret[512];
    char *or = "";

    ret[0]='\0'; // clear the string.
    if (flags & NOTE_DELETE) {strcat(ret,or);strcat(ret,"NOTE_DELETE");or="|";}
    if (flags & NOTE_WRITE) {strcat(ret,or);strcat(ret,"NOTE_WRITE");or="|";}
    if (flags & NOTE_EXTEND) {strcat(ret,or);strcat(ret,"NOTE_EXTEND");or="|";}
    if (flags & NOTE_ATTRIB) {strcat(ret,or);strcat(ret,"NOTE_ATTRIB");or="|";}
    if (flags & NOTE_LINK) {strcat(ret,or);strcat(ret,"NOTE_LINK");or="|";}
    if (flags & NOTE_RENAME) {strcat(ret,or);strcat(ret,"NOTE_RENAME");or="|";}
    if (flags & NOTE_REVOKE) {strcat(ret,or);strcat(ret,"NOTE_REVOKE");or="|";}

    return ret;
}
```


For more information about kernel queues, see the manual page for [kqueue](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/kqueue.2.html#//apple_ref/doc/man/2/kqueue)), the _[FileNotification](../../../samplecode/FileNotification/FileNotification.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjugm)_ sample code, and the FreeBSD documentation for kernel queues at [http://people.freebsd.org/~jmg/kq.html](http://people.freebsd.org/~jmg/kq.html)..

[Next](Document%20Revision%20History.md)[Previous](File%20System%20Event%20Security.md)

