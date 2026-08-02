---
title: 64-Bit Transition Guide
apple_id: TP40001064
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/Cross-ArchitecturePluginSupport/Cross-ArchitecturePluginSupport.html
archived_at: '2026-07-15T07:23:04.030571Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide](Introduction%20to%2064-Bit%20Transition%20Guide.md)


[Next](Performance%20Optimization.md)[Previous](High-Level%2064-Bit%20API%20Support.md)

# Cross-Architecture Plug-in Support

In some cases, you may find it useful to support plug-ins written for an architecture other than the one your application is running on at the time. You may need this simply for debugging purposes, but this approach may also be useful if you want your application to support existing plug-ins on newer architectures. For example, audio software manufacturers may find it easier to drive adoption of 64-bit versions of their application if they also support existing 32-bit audio unit plug-ins.

Designing a host application to load a given plug-in is a highly specialized task. This chapter provides an overview of common approaches to doing this. This chapter assumes that you have already written a dummy plug-in loader that loads the plug-in into memory (even if it doesn’t actually do anything with the plug-in yet).

In addition, this chapter describes several common interprocess communication APIs, explains how to pass large amounts of data between the host application and the plug-in helper host, and tells how to launch that host for a particular architecture.

Before you can build a helper host, you must first choose an architecture model that accomplishes your needs. There are many possible design models for helper hosts, each with varying levels of functionality and difficulty. This section describes three such models and explains the problems you may encounter with each model.

Of these models, remote hosting is generally recommended because it is the easiest and most reliable. Limited function-call marshaling works when the scope of the API is limited. Full programmatic function-call marshaling, although described here, should usually be avoided because the exceptions and edge cases can make it impractical.

The first thing most developers consider doing when they design a helper host is trying to make every function call from the plug-in result in the same function being called in the host. With programmatic function-call marshaling, your application extracts the symbols from the plug-in, then generates custom library code to marshall arguments across address space boundaries (or even from one machine to another).

In general, the sheer number of exceptions and edge cases involved makes programmatic function-call marshaling highly impractical, and thus it should generally be avoided. However, this design may be reasonable if the plug-ins call only C APIs.

Such a design, although powerful, is tricky to get right, particularly when used across byte-order boundaries, because this design requires intimate understanding of every data structure involved to know whether or not a field should be byte swapped. For example, swapping various BSD-level networking data structures would be disastrous.

Fortunately, these data types are by far the exception rather than the rule, and can generally be ignored. However, the prevalent use of structure hiding (for example, using `void *` pointers and opaque types) essentially makes programmatic function-call marshaling nearly impossible, because there is no way to programmatically determine the underlying structure of a piece of data passed in this manner (and in many cases, the value may be meaningless in the context of a different process).

Opaque data structures are particularly an issue if a plug-in executes some code in the local process and passes the resulting data to closely related functions in the remote process. For example, file system references (FSRef) would not make sense when passed via IPC to a process running on a different architecture because of byte order differences in the underlying (opaque) structure. Similarly, file descriptors (POSIX) function differently depending on the application, and thus cannot be usefully passed via IPC.

If the plug-in must call arbitrary C++ or Objective-C class or instance methods on classes outside the plug-in itself, it becomes even more difficult to remotely execute function calls because of the need to maintain synchronization of class instances between the helper host and the main host. Since you cannot recompile the plug-in, replacing variables with accessor methods is impossible. This means that each function that potentially manipulates state must copy all of the state from the main host’s notion of the class instance. Further, there is still some possibility that the host could update public class members without your knowledge, leading to potentially significant changes in your host application.

Finally, this method will not work transparently if the plug-in calls any functions that involve Mach ports, because port rights are not shared between the two processes unless they are explicitly passed from one process to the other or are inherited from the parent. Similarly, you should not try to marshal system calls in this way, because byte swapping at the lower levels of the operating system can be particularly complex.

Limited function-call marshaling is a far more realistic approach than fully programmatic marshaling. First, identify a set of (generally C) routines that call back into the host application. Then, replace those in the helper host with libraries that call across address space boundaries.

Because the scope of the supported API is limited, it is much more practical for you to support them through function-call marshaling, because you can hand-code routines for each function or class that you intend to call across an address-space boundary instead of relying on programmatically generated functions and classes.

As with programmatic function-call marshaling, you must be particularly careful when working with pointers. If pointer arguments are of a known type and size, it is relatively easy to work with them. However, you may encounter problems if you do not know the size of the referenced object and if you need to byte swap or otherwise manipulate the pointer contents during the boundary crossing.

C++ and Objective-C classes are a bit harder. You can’t simply pass pointers to classes, because they won’t be valid on the other side of the communications channel. However, if the number of classes is limited, you can emulate class pointers by using stub classes in the helper host that contain an extra member variable that stores the address of the real class instance on the host side.

Similarly, you must emulate any callback pointers passed as arguments, because the callback pointer is meaningless in the context of the main host application. You can emulate these pointers either through message passing in the reverse direction or through RPC from the primary host into the helper host.

When you use limited function-call marshaling, your helper host can be very compact and completely transparent. However, your stub libraries must contain every function that you intend to override. For large plug-in APIs, this approach can be daunting, particularly if you are not in control of the API itself.

Remote hosting is strongly recommended for most helper host implementations because it is relatively easy to implement reliably. With remote hosting, instead of relying on knowledge of the plug-in architecture, you rely on your knowledge of the plug-in host itself. Because you are in control of the code in question, you will be aware of any changes to the API. Also, because the interface between a host and its built-in engine rarely involves callback pointers, you can use a simpler communication mechanism.

With remote hosting, you create a stripped-down version of your application that displays no user interface itself (except possibly a mirror of the menu bars with appropriate message passing to the main application). This miniature application should include a full set of data processing functionality. In this model, the host application passes a chunk of data to the helper host, then relies on the helper host to process the data just as the host application’s built-in plug-in engine would.

You may choose to add a command-line flag (using `argc` and `argv`) to your application and, upon seeing that flag, call a separate initialization routine in which only the back-end functionality is configured. If you do, your helper host can simply be another running instance of your main application binary.

The biggest change you must make to support remote hosting is to maintain the state of your plug-in support engine through function calls instead of variable assignment (if you don’t already do so). After you make that change throughout your host, the problem becomes a relatively simple set of changes to these functions:

- State changes to the plug-in layer of the host application must be reflected in the helper host.
- In the helper host, whenever a plug-in calls a callback that changes the state information stored in the helper host, your application must notify the main host so that the two remain in sync.
- Additional code must be added to handle passing of any data on which the plug-in will operate.

This state synchronization can be achieved through a relatively straightforward use of interprocess communication (discussed in [Using Interprocess Communication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzr)). For transport of large data, you should generally transfer the data using memory mapping. This technique is described in [Memory Mapping for Bulk Data Transport](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzu).

For interprocess communication, you can design a helper host using three broad models:

- __Remote procedure call (RPC) model__—You can use remote procedure calls to handle synchronization of your main host and helper host for you. There are many different RPC APIs available, each with different features and limitations, but at a high level they all behave similarly.

  A helper host designed using the RPC model contains a stub library. The functions in this library are created by RPC support tools based on an interface description. When your helper host (or a plug-in) calls these functions, the stub library sends a message to the main application, which causes the corresponding function in the main application to be called. When that function has completed, the result (if any) is returned in the same manner.

  An RPC-based helper host can be easier to write than one based on a pure client/server model, but it may suffer from limitations in the RPC API itself. For example, Mach RPC has no notion of complex data structures. As a result, you still need to write a fair amount of code to marshal arguments across address space boundaries. Mach RPC is discouraged, and is not officially supported.

  You will learn about several RPC APIs in [Remote Procedure Call APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzrge).
- __Client/server message passing model__—Open a socket-based or pipe-based connection to the main host application and use it to pass messages back and forth.

  A client/server helper host design consists of three main parts:

  - Create stub versions of the functions you want your helper host to call in the main host. When a plug-in or some other part of the helper host calls one of these stub functions, the function adds a message to a queue and waits on a condition variable. The plug-in thread then sleeps until a response is received and is posted to the buffer by the communication thread.
  - Create a communication thread in the helper host to transmit message entries from the buffer and store the responses in some other part of the same message entry.
  - Create a listener thread in the primary host to manage this communication on the other end.

  You will learn about several client/server messaging APIs in [Client/Server Messaging APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzt).
- __Memory mapping__—Create a region of memory that is simultaneously accessible to two (or more) processes and use it to share data between them.

  If you want to use memory mapping for passing messages back and forth, you would have to write a lot of additional code. For this reason, for most messaging needs, you should use a different IPC mechanism. However, when you need to move large quantities of information in bulk, client/server and RPC communication can get bogged down.

  For this reason, memory mapping is a common technique for passing large amounts of information in an out-of-band fashion (that is, in lieu of sending it through the primary IPC channel). For example, it would make sense for an audio plug-in helper host to communicate changes to parameters using a traditional IPC API and use memory mapping for a locking-free buffer between the main host and the helper host.

  You can find out more about memory mapping in [Memory Mapping for Bulk Data Transport](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzu).

There are three remote procedure calls that are commonly used in OS X: distributed objects, Mach RPC, and Sun RPC. Of these, only distributed objects is a public API recommended for general use.

In OS X v10.7 and later, XPC services are the recommended way to support interprocess communication. The XPC services API lets you make cross-process method calls into objects that live in a different address space, transparently marshalling the data to the child process and back.

To learn how to create an XPC service, read _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

If XPC is not available on your target OS, and if your software does not need to run in a sandbox, Distributed Objects can provide similar functionality.

If you are calling C or C++ APIs, you must wrap them in Objective-C classes before you can use this API. Before you consider doing so, you should read [Limited Function-Call Marshaling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzrga).

For more information on distributed objects, see _[Distributed Objects Programming Topics](../../Cocoa/Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i)_.

Mach RPC is not considered a public interface, and its direct use is not generally recommended. However, if you decide to use it, you can find information about it at the following URLs:

- [http://www.cs.cmu.edu/afs/cs/project/mach/public/www/doc/osf.html](http://www.cs.cmu.edu/afs/cs/project/mach/public/www/doc/osf.html)—OSF's Mach Documentation (from CMU)
- [http://www.cs.cmu.edu/afs/cs/project/mach/public/www/doc/tutorials.html](http://www.cs.cmu.edu/afs/cs/project/mach/public/www/doc/tutorials.html)—Mach Tutorials and Examples (from CMU)

Sun RPC is beyond the scope of this document. You can find more information in the following places:

- [rpc](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/rpc.3.html#//apple_ref/doc/man/3/rpc) man page
- `rpcgen` man page
- [xdr](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/xdr.3.html#//apple_ref/doc/man/3/xdr) man page
- `rpcinfo` man page
- `portmap` man page

Sun RPC is generally not recommended for new designs.

OS X supports several client/server messaging APIs, including Apple events, BSD sockets, and pipes (standard input and output, for example). These APIs are described in the sections that follow.

A common API for interprocess communication in OS X is Apple events. The Apple Events API is a fairly straightforward API for low-bandwidth IPC, and you are probably already using it in your application. If so, you can add additional message types for communication between your application and the plug-in host.

For more information, see _[Apple Events Programming Guide](../../Apple%20Script/Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.

The most common API for simple interprocess communication is an old standby, sockets. There are a number of different OS X technologies for working with sockets, including:

- `CFNetwork` API (described in _[CFNetwork Programming Guide](../../Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs)_)
- `NSSocketPort` API (described in _[NSSocketPort Class Reference](https://developer.apple.com/documentation/foundation/socketport)_)
- BSD socket API (described in [socket](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/socket.2.html#//apple_ref/doc/man/2/socket))

Each of these APIs implements the same underlying message, a bidirectional stream of bytes between both ends. Stream-based messaging presents a problem if your helper host needs to concurrently support multiple plug-ins, however, because you will need to multiplex data from multiple sources. You can solve this problem by using message queues, as described in [Message Queues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzv).

As an added bonus, communication via sockets is not limited to a single machine. If you are writing software that can benefit from distributed computing, such remote communication can be a significant benefit.

If you are writing an audio helper host, most of the work is done for you beginning in OS X v10.4. The AUNetSend and AUNetReceive audio units can make helper hosting relatively painless to implement, whether on a local machine or remotely. However, with these plug-ins, _all_ information passes through the TCP/IP stack even if the destination is on the local machine.

Keep in mind two caveats if you use TCP/IP for passing the actual data back and forth instead of just passing control information. First, the latency of remote communications is _not_ insignificant. If this matters in your application (for example, an audio application), you _must_ compensate for this latency or quality will suffer greatly. Second, the amount of information being sent is substantial, and thus, for performance reasons, socket programming may not be ideal for hosting a large number of individual plug-ins on a helper host. If you expect a large number of non-native plug-ins, you should generally use memory mapping to pass data from the main host to the helper host, as described in [Memory Mapping for Bulk Data Transport](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzu).

With those caveats in mind, sockets also open up the possibility of alternative software usage models. For example, you might design an audio application so that the front end can run on a small, low-power, fanless computer in a studio control room, with all of the heavy lifting performed by a separate computer in another room. You could implement the user interface by temporarily hosting a local copy of plug-ins when a user wants to show their user interface, then sending control change messages across the wire to the actual host (where the plug-ins are all running with no UI displayed). Then, use TCP/IP for sending _only_ the raw audio from the audio interface. For audio play-through while recording, you should mix the incoming audio into the output on the front-end computer as the very last step in processing.

The details of creating and using sockets are beyond the scope of this document. For additional information, consult the documents listed above. You may also find useful information in the UNIX Socket FAQ, which can be found at [http://www.developerweb.net/forum/](http://www.developerweb.net/forum/). This FAQ includes code examples that illustrate how to use TCP/IP and UNIX domain sockets at the BSD API level.

Another common API for interprocess communication is standard input and output. This API provides a pair of unidirectional streams. Much like socket programming, the stream-based nature of standard input and output requires you to keep additional state information if you need to associate responses to messages with the original message. A good way to solve that problem is through the use of message queues, as described in [Message Queues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzv).

One thing that makes standard input and output convenient is that they are largely set up for you. Every process in a UNIX-based system has standard input and output automatically. You can take advantage of these to communicate between a parent process (your main application) and its children (your helper host).

To communicate with child processes in Cocoa, you should use the `NSTask` API, described in [NSTask Class Reference](https://developer.apple.com/documentation/foundation/nstask). For more information on this method, read [Creating and Launching an NSTask](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/Tasks/createtask.html#//apple_ref/doc/uid/20000803) and [Ending an NSTask](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/Tasks/endingtask.html#//apple_ref/doc/uid/20000804).

Alternatively, in BSD tools, you can accomplish the same thing at a file descriptor level using a few low-level APIs as shown in this example:

```c
#include <stdlib.h>
comm_channel *startchild(char *path)
{
        comm_channel *channel = malloc(sizeof(*channel));
        pid_t childpid;
        int in_descriptors[2];
        int out_descriptors[2];

        /* Create a pair of file descriptors to use for communication. */
        if (pipe(in_descriptors) == -1) {
                fprintf(stderr, "pipe creation failed.\n");
                goto error_exit;
        }
        if (pipe(out_descriptors) == -1) {
                fprintf(stderr, "pipe creation failed.\n");
                goto error_exit;
        }
        /* Create a new child process. */
        if ((childpid = fork()) == -1) {
                fprintf(stderr, "fork failed.\n");
                goto error_exit;
        }
        if (childpid) {
                /* Parent process */
                channel->in_fd = in_descriptors[0];
                close(in_descriptors[1]);
                channel->out_fd = out_descriptors[1];
                close(out_descriptors[0]);
                return channel;
        } else {
                /* Child process */
                if (dup2(in_descriptors[1], STDOUT_FILENO) == -1) {
                        fprintf(stderr, "Call to dup2 failed.\n");
                        goto error_exit;
                }
                close(in_descriptors[0]);

                if (dup2(out_descriptors[0], STDIN_FILENO) == -1) {
                        fprintf(stderr, "Call to dup2 failed.\n");
                        goto error_exit;
                }
                close(out_descriptors[1]);

                execl(path, path, NULL);

                /* If we get here, something went wrong. */
                fprintf(stderr, "Exec failed.\n");
                goto error_exit;
        }
        return channel;
    error_exit:
        free(channel);
        perror("msg_send");
        return NULL;
}
```


Message queues provide a way for one process to communicate with another process in a flexible fashion over a stream-based transport without requiring that the two processes behave in a lockstep fashion at all times. You can build message queues on top of either bidirectional communication channels, such as sockets, or on top of pairs of unidirectional communication channels, such as pipes or standard input and output.

A message queue at its simplest consists of a linked list of message structures. Each message structure contains an outgoing message and a location in which the response will be stored. Depending on how you write your code, it may contain a callback, to be executed upon completion, or a single handler that calls the right function based on the original message type.

On each end, you should have a thread to handle messages from the socket. You can use your run loop thread as a handler thread if you are writing a traditional application, or you can use a separate message thread if you prefer to use lower-level socket APIs.

The code for managing a message queue is relatively straightforward, locking issues notwithstanding. A complete code example is provided in the companion files associated with this document. The companion files archive can be downloaded from the sidebar when viewing this document as HTML at the ADC Reference Library (`developer.apple.com`).

For moving large quantities of data between two applications, unless you are communicating over a network, you should generally avoid most traditional message-passing algorithms because of the inherent CPU overhead and latency involved. Instead, you should consider a shared memory design using [mmap](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mmap.2.html#//apple_ref/doc/man/2/mmap).

The following example shows how to create a shared memory region between a process and its child:

```c
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/dirent.h>
#include <fcntl.h>
#include <stdlib.h>

/* Create the map file and fill it with bytes. */
char *create_shm_file(char *progname, int length)
{
    int fd, i;
    char *filename=malloc(MAXNAMLEN+1);
    char *ret;
    char byte = 0;

    sprintf(filename, "/tmp/%s-XXXXXXXX", progname);
    ret = mktemp(filename);

    fd = open(filename, O_RDWR|O_CREAT, 0600);
    for (i=0; i<length; i++) {
        write(fd, &byte, 1);
    }
    return ret;
}

/* Map the file into memory in a read-write fashion */
void *map_shm_file(char *filename, int length)
{
    int fd = open(filename, O_RDWR, 0);
    void *map;
    if (fd == -1) return NULL; /* Could not open file */
    map = mmap(NULL, length, PROT_READ|PROT_WRITE,
        MAP_FILE|MAP_SHARED, fd, 0);
    return map;
}
```

Using this sample code, the two applications can rendezvous using a file as a shared memory buffer between them. As long as both applications use the same file, any changes made by one application will be seen by the other and vice versa. Your application can then assign pieces of this buffer to be used for various tasks just as though you were using anonymous memory returned by a call to [malloc](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/malloc.3.html#//apple_ref/doc/man/3/malloc).

If you intend to work with page-sized regions, you should also take note of the functions described in the [mpool](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/mpool.3.html#//apple_ref/doc/man/3/mpool) manual page. However, for most purposes, you should write your own pool allocator if you need to regularly allocate and deallocate shared memory.

For more information on the functions used in the example above, see the man pages for [mmap](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mmap.2.html#//apple_ref/doc/man/2/mmap), [open](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/open.2.html#//apple_ref/doc/man/2/open), and [mktemp](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/mktemp.3.html#//apple_ref/doc/man/3/mktemp).

A good way of working with shared memory is for you to use a lock-free ring buffer design. In such a design, each communication endpoint reads from two variables but writes only to one. In this way, both sides know where in the buffer the other endpoint is working.

For example:

```swift
typedef struct ringbuffer {
    void *buffer;
    int buflen;
    int readpos;
    int writepos;
} *ringbuffer;

#define BYTES_TO_READ(ringbuffer) (ringbuffer->writepos - \
    ringbuffer->readpos + \
    ((ringbuffer->readpos > ringbuffer->writepos) * \
        (ringbuffer->buflen)))

/*  Use >= here because if readpos and writepos are equal,
    the buffer must be assumed to be empty.  Otherwise,
    the buffer would start out full. For this reason,
    the writepos must not be allowed to overtake the read
    position, so subtract one from the final value.
*/
#define BYTES_TO_WRITE(ringbuffer) (ringbuffer->readpos - \
    ringbuffer->writepos + \
    ((ringbuffer->writepos >= ringbuffer->readpos) * \
        ringbuffer->buflen) - 1)
```

The code reading from this buffer knows that it can always read from `readpos` forwards up to `writepos` (or if `writepos` is less than `readpos`, it can read to the end of the buffer, then read from the start of the buffer up to `writepos`). After reading, the read code updates `readpos` to reflect the location of the last byte read.

In a similar fashion, the code writing to this buffer knows that it can safely write from the `writepos` position until it reaches `readpos`, wrapping around the end of the buffer if necessary. After writing, the write code updates `writepos` to reflect the location of the last byte written.

Because only one process will ever modify either `readpos` or `writepos`, no synchronization between the two processes is required. Note, however, that the reading code _must_ protect `readpos` against other threads within that process, and the writing code must do the same for `writepos`.

After you’ve build a helper host, the next step is to determine the architecture of the plug-in. For PEF/CFM plug-ins, it is safe for you to assume that the plug-in contains 32-bit PowerPC executable code. For Mach-O plug-ins, the method you should use varies according to the version of OS X being used.

For backward compatibility with versions of OS X prior to 10.5, your application should use the detection code presented in the _[CheckExecutableArchitecture](../../../samplecode/CheckExecutableArchitecture/CheckExecutableArchitecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvgy)_ sample code. This sample code is straightforward and presents a fairly easy way to determine which architecture to use for loading existing plug-ins.

In OS X v10.5 and later, you should use the `CFBundle` API. This API is safer as a long-term solution, because it will support any binary format that is supported by that particular version of OS X, thus freeing you from the need to alter the code as new binary formats are introduced. The relevant functions are:

```
CFArrayRef CFBundleCopyExecutableArchitecturesForURL(CFURLRef url);
CFArrayRef CFBundleCopyExecutableArchitectures(CFBundleRef bundle);
```

The next step is to execute the helper host, choosing the appropriate architecture in the process. In OS X v10.5 and later, the recommended way to launch an executable using a particular architecture is through an extension to `posix_spawn`. This API is described in the manual page for [posix_spawn](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawn.2.html#//apple_ref/doc/man/2/posix_spawn), [posix_spawnattr_init](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/posix_spawnattr_init.3.html#//apple_ref/doc/man/3/posix_spawnattr_init), and the related manual pages linked from those pages. The extension for choosing an architecture to launch is described in the manual page for [posix_spawnattr_setbinpref_np](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/posix_spawnattr_setbinpref_np.3.html#//apple_ref/doc/man/3/posix_spawnattr_setbinpref_np).

To support helper hosts on OS X v10.4, you can use separate copies of your helper host for each processor architecture instead of a universal binary, then launch whichever version is appropriate.

[Next](Performance%20Optimization.md)[Previous](High-Level%2064-Bit%20API%20Support.md)

