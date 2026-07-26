---
title: guest post about mach exception handlers
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-01-11-mach-exception-handlers.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2fa202501b04a03c'
translated: false
---

> 原文：[guest post about mach exception handlers](https://www.mikeash.com/pyblog/friday-qa-2013-01-11-mach-exception-handlers.html)　·　mikeash.com Friday Q&A

Posted at 2013-01-11 14:44 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-01-25: Let's Build NSObject](https://www.mikeash.com/pyblog/friday-qa-2013-01-25-lets-build-nsobject.html)  
Previous article: [Friday Q&A 2012-12-28: What Happens When You Load a Byte of Memory](https://www.mikeash.com/pyblog/friday-qa-2012-12-28-what-happens-when-you-load-a-byte-of-memory.html)  
Tags: [debugging](https://www.mikeash.com/pyblog/?tag=debugging) [evil](https://www.mikeash.com/pyblog/?tag=evil) [exception](https://www.mikeash.com/pyblog/?tag=exception) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [mach](https://www.mikeash.com/pyblog/?tag=mach) [mig](https://www.mikeash.com/pyblog/?tag=mig) [signal](https://www.mikeash.com/pyblog/?tag=signal)

Friday Q&A 2013-01-11: Mach Exception Handlers

by [Landon Fuller](http://landonf.bikemonkey.org)

**Signals vs. Exceptions**  
On most UNIX systems, the only mechanism available for handling crashes (such as dereferencing `NULL`, or writing to an unwritable page) are the standard UNIX [signal handlers](http://www.mikeash.com/pyblog/friday-qa-2011-04-01-signal-handling.html). When a fatal machine exception is generated, it is caught by the kernel, which then executes a user-space [trampoline](http://en.wikipedia.org/wiki/Trampoline_(computing%29) within the failing process, executing any function previously registered by that process via `sigaction(3)` or `signal(3)`.

On OS X, however, a much more versatile API exists: Mach exceptions. Dating back to Avie Tevanian's work on the [Mach](http://en.wikipedia.org/wiki/Mach_(kernel%29) OS (yes, _that_ [Avie Tevanian](http://en.wikipedia.org/wiki/Avie_Tevanian)), Mach exceptions build on [Mach IPC/RPC](https://developer.apple.com/library/mac/documentation/Darwin/Conceptual/KernelProgramming/boundaries/boundaries.html#//apple_ref/doc/uid/TP30000905-CH217-BABDECEG) to provide an alternative to the UNIX signal handler API. The original design of the Mach exception handling facility was first described, as far as I'm aware, in a [1988 paper](ftp://ftp.cs.cmu.edu/project/mach/doc/unpublished/exception.ps) authored by Avie Tevanian, among others. It remains fairly accurate to this day, and I'd recommend reading it for more details (after finishing this post, of course).

Mach exceptions differ from UNIX signals in three significant ways:

- Exception information is delivered as a Mach message via a Mach IPC port, rather than by the kernel calling into a userspace trampoline.
- Exception handlers may be registered by any process that has the appropriate mach port rights for the target process.
- Exception handlers may be registered for a specific thread, a specific task (process), or for the entire host. The kernel will search for handlers in that order.

These differences introduce a number of properties that can be useful when implementing debuggers and crash reporters, and are what make the Mach API interesting as an alternative to BSD signals.

**Exceptions are Messages**  
The Mach exception API is based on Mach RPC (which is, in itself, based on Mach IPC). There's a lot of confusion around Mach IPC, but at a high-level, it's not too dissimilar to UNIX sockets or other well-known IPC mechanisms that allow one to read/write messages between processes. Mach IPC communication occurs over mach ports, rather than via socket or other traditional UNIX mechanism; mach ports have unique names, and can be shared with other processes. They can be used to send and receive messages containing arbitrary data. There's a bit more complexity involved in their actual use, but conceptually, that's about all you need to know.

To write a Mach exception handler using raw Mach IPC, you would need to wait for a new exception message by calling `mach_msg()` on a Mach port previously registered as an exception handler (how to do this is covered below). The call to `mach_msg()` will block until an exception message is received, or the thread is interrupted. Once a message is received, you are free to introspect it for the state of the thread that generated the exception. You can even correct the cause of the crash and restart the failing thread, if you feel like hacking register state at runtime.

Since exceptions are provided as _messages_, rather than by calling a local function, exception messages can be forwarded to the previously registered Mach exception handler, even if that existing handler is completely out-of-process. This means that you can insert an exception handler without disturbing an existing one, whether it's the debugger or Apple's crash reporter. To forward the message to an existing handler, you also use `mach_msg()` to send the original message to a previously registered handler's mach port, using the `MACH_SEND_MSG` flag.

However, if you wish to respond the Mach RPC request yourself, rather than forwarding it, you would need to _reply_ to the message, informing the sender whether or not you _handled_ the exception. Mach considers an exception _handled_ if the crashing thread's state has been corrected such that its execution can be resumed. In this case, the kernel does not attempt to find any other exception handler, and considers the matter settled. However, if you reply to the RPC request informing the sender (usually the kernel) that the exception has not been handled, the sender will then try to find the next applicable Mach exception handler. Remember that the kernel attempts to send exceptions to thread-specific, task-specific, and host-global exception handlers, in that order.

The fact that a reply is expected from the exception request can be used for interesting purposes. For example, if a debugger has its exception handler called when a breakpoint is hit, it can simply wait to reply to the Mach exception message until (and only if) you request that the debugger continue execution.

**Mach RPC, not IPC**  
While above I described how one might implement mach exception handling with raw Mach IPC, the fact is that this is not how the interfaces are defined in Mach. Instead, Mach RPC uses an interface description language (called _matchmaker_ in the [original 1989 paper](http://www.cs.cmu.edu/afs/cs/project/mach/public/doc/unpublished/mig.ps)), to describe the format of Mach RPC requests (and their replies), and automatically generate code to handle received messages and generate a reply.

On OS X, the Mach RPC interface descriptions for exception handling - `mach_exc.defs` and `exc.defs` - are available via `/usr/include/mach`. If you include these files in your Xcode project, it will automatically run the `mig(1)` tool (Mach Interface Generator), generating headers and C source files necessary to receive and handle Mach exception messages. The `exc.defs` file provides an API for working with 32-bit exceptions, whereas the `mach_exc.defs` file provides an API for working with 64-bit exceptions. Unfortunately, the Mach RPC defs are not provided on iOS, and only a subset of the necessary generated headers are provided. As a result, it's not possible to implement a fully correct Mach exception handler on iOS without relying on undocumented functionality.

The code generated by MIG handles two things:

- Interpreting incoming RPC messages and calling out to an existing handler function with the decoded data.
- Initialize a response to the RPC messages using the return values from the handler function.

The generated code does not handle registering a Mach exception handler, receiving the Mach message, or actually sending the reply. That is the implementor's responsibility. In addition, there are multiple supported exception "behaviors" that provide different sets of information about an exception; it is the implementor's responsibility to provide callback functions for all of them.

This is best illustrated in the following 64-bit safe code, intended to work with RPC code generated by `mach_exc.defs` (I've left out error handling for simplicity):

```
    // Handle EXCEPTION_DEFAULT behavior
    kern_return_t catch_mach_exception_raise (mach_port_t exception_port,
                                               mach_port_t thread,
                                               mach_port_t task, 
                                               exception_type_t exception,
                                               mach_exception_data_t code,
                                               mach_msg_type_number_t codeCnt)
    {
        // Do smart stuff here.
        fprintf(stderr, "My exception handler was called by exception_raise()\n");

        // Inform the kernel that we haven't handled the exception, and the
        // next handler should be called.
        return KERN_FAILURE;
    }

    extern boolean_t mach_exc_server (mach_msg_header_t *msg, mach_msg_header_t *reply);
    static void exception_server (mach_port_t exceptionPort) {
        mach_msg_return_t rt;
        mach_msg_header_t *msg;
        mach_msg_header_t *reply;

        msg = malloc(sizeof(union __RequestUnion__mach_exc_subsystem));
        reply = malloc(sizeof(union __ReplyUnion__mach_exc_subsystem));

        while (1) {
             rt = mach_msg(msg, MACH_RCV_MSG, 0, sizeof(union __RequestUnion__mach_exc_subsystem), exceptionPort, 0, MACH_PORT_NULL);
             assert(rt == MACH_MSG_SUCCESS);

             // Call out to the mach_exc_server generated by mig and mach_exc.defs.
             // This will in turn invoke one of:
             // mach_catch_exception_raise()
             // mach_catch_exception_raise_state()
             // mach_catch_exception_raise_state_identity()
             // .. depending on the behavior specified when registering the Mach exception port.
             mach_exc_server(msg, reply);

             // Send the now-initialized reply
             rt = mach_msg(reply, MACH_SEND_MSG, reply->msgh_size, 0, MACH_PORT_NULL, 0, MACH_PORT_NULL);
             assert(rt == MACH_MSG_SUCCESS);
        }
    }
```

You'll note from the example code that our exception handler is called a _server_. In Mach RPC parlance, the kernel would be the _client_: it issues RPC requests to our exception server, and waits for our reply.

**Exception Behaviors**  
As described above, exception messages come in multiple formats, containing varying types of data. It's the implementor's responsibility to register for the correct behavior; the `mig`-generated RPC code will interpret the messages and hand it off to a user-defined function for the specific type. There are three basic behaviors defined by the Mach Exception API:

- `EXCEPTION_DEFAULT`: Exception messages will contain a reference thread that triggered it. Handled by `catch_exception_raise()`.
- `EXCEPTION_STATE`: Exception messages will contain the register state of the triggering thread, but not a reference to the thread itself. Handled by `catch_exception_raise_state()`.
- `EXCEPTION_STATE_IDENTITY`: Exception messages will contain the register state of the triggering thread, as well as a reference to the triggering thread. Handled by `catch_exception_raise_state_identity()`.

In addition to the above behaviors, an additional variant was added in later OS X releases to support 64-bit safety. The `MACH_EXCEPTION_CODES` flag may be set by OR'ing it with any of the listed behaviors, in which case 64-bit safe exception messages will be provided. This flag is used by LLDB/GDB even when targeting 32-bit processes. When using the `MACH_EXCEPTION_CODES` flag, one must also use the RPC functions generated by `mach_exc.defs`; these use the `mach_` prefix for all functions and types.

Generally speaking, `EXCEPTION_DEFAULT` or `EXCEPTION_STATE_IDENTITY` are sufficient for most purposes. Since `EXCEPTION_DEFAULT` behavior provides a reference to the triggering thread, you can also fetch the thread state that would normally be provided via `EXCEPTION_STATE_IDENTITY` via the Mach `thread_state()` API.

When registering your exception handler, you are responsible for requesting the `MACH_EXCEPTION_CODES` behavior that matches the RPC implementation (`exc.defs` or `mach_exc.defs`) that you intend to use.

**Putting it Together**  
It's time to get down to brass tacks: actually registering an mach port to receive exception messages. As noted above, handlers can be registered for threads, tasks, and the host, and there are different sets of identical APIs for each:

- `(thread|task|host)_get_exception_ports`: Returns the currently registered set of exception ports.
- `(thread|task|host)_set_exception_ports`: Sets the exception port that will be used for all future exceptions.
- `(thread|task|host)_swap_exception_ports`: Atomically set a new exception port, and return the current ports. This can be used to avoid race conditions that could otherwise occur if multiple handlers are registered concurrently.

To register your handler, you'll need to first allocate a mach port to receive the messages, insert a "send right" to permit sending responses, and then call one of the exception port `set()` or `swap()` functions to register it as a receiver of exception messages.

For example (error handling again elided for conciseness):

```
    mach_port_t server_port;
    kern_return_t kr = mach_port_allocate(mach_task_self(), MACH_PORT_RIGHT_RECEIVE, &server_port);
    assert(kr == KERN_SUCCESS);

    kr = mach_port_insert_right(mach_task_self(), &server_port, &server_port, MACH_MSG_TYPE_MAKE_SEND);
    assert(kr == KERN_SUCCESS);

    kr = task_set_exception_ports(task, EXC_MASK_BAD_ACCESS, server_port, EXCEPTION_DEFAULT|MACH_EXCEPTION_CODES, THREAD_STATE_NONE);
```

If you wish to preserve the previous exception handlers, `task_swap_exception_ports()` should be used in place of `task_set_exception_ports()`.

**Conclusion**  
Mach exception handlers are a very useful tool, and using them requires a fair bit of moving pieces, but hopefully they don't seem dauntingly complex. At the end of the day, mach exceptions are just a simple exception message, coupled with a reply, sent over Mach ports.

There are some signficiant advantages of the Mach API over signal handlers, including the ability to forward exceptions out-of-process, and handle all exceptions on a completely different stack - something that can be useful when handling an exception triggered by a stack overflow on the target thread.

If you plan on implementing your own mach exception handler, there are certainly more details worth further investigation:

- When forwarding mach exceptions, you need to send an exception message that matches the previous registered handler's exception flavor. This may mean populating a new Mach exception message with additional thread state.
- It's not strictly necessary to use the MIG-generated `exc_server()` or `mach_exc_server()` functions for interpreting Mach messages (though it is probably a good idea). Since `mig(1)` generates structures that may be used to directly interpret the Mach exception messages, you can do so directly.
- If you forward exception messages for exceptions that occur in your own process, you need to be sure that the target for the reply is not also your own process. Single-stepping debuggers will only resume the thread they wish to step; that means that they won't resume your exception handler's thread, you'll never receive the reply, and the interrupted thread will never resume.

Lastly, I should highlight that the headers and mach interfaces required to implement a correct mach exception handler on iOS are not available (though they are available and public on Mac OS X). I filed a radar requesting their addition (`rdar://12939497`), as well as an Apple DTS support incident to clarify the situation. The radar is still open, but DTS provided the following guidance:

> Our engineers have reviewed your request and have determined that this would be best handled as a bug report, which you have already filed. There is no documented way of accomplishing this, nor is there a workaround possible.

In the meantime, as far as I can determine through my own work, and as per DTS's feedback, it's not possible to implement Mach exception handling on iOS using only public API. Hopefully this will be resolved in a future release of iOS, such that we can safely adopt Mach exceptions.

Thus concludes my first contribution to Friday Q&A. If you have any questions, [feel free to drop me an e-mail](mailto:landonf@bikemonkey.org). If I got anything terrible wrong, feel free to roast me in the comments.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-01-11-mach-exception-handlers.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
