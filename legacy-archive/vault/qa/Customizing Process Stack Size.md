---
title: Customizing Process Stack Size
apple_id: DTS10003531
resource_type: QA
platform: macOS
topic: Performance
technology: CoreServices
published: '2011-01-26'
source_url: https://developer.apple.com/library/archive/qa/qa1419/_index.html
archived_at: '2026-07-18T02:30:35.528183Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1419

# Customizing Process Stack Size

## Q:  My application maintains a large number of concurrent threads and needs to use a large amount of stack allocated data. How can I protect against overflowing my allocated stack space?

A: My application maintains a large number of concurrent threads and needs to use a large amount of stack allocated data. How can I protect against overflowing my allocated stack space?

Each Mac OS X process is launched with a default stack size of 8 Megabytes. This allocation is used exclusively for the main thread's stack needs. Each subsequent thread created is allocated its own default stack, the size of which differs depending on the threading API used. For example, the Mac OS X implementation of Pthreads defines a default stack size of 512 Kilobytes, while Carbon MPTasks are created with a 4 Kilobyte stack.

A process can outgrow its allocated stack space by any of the following means:

- Deep recursion
- Deeply nested procedure calls
- Large allocations of stack data
- Many concurrent threads

Since certain system defaults and limits can change between releases of Mac OS X, it is useful to be able to determine the default process stack size for the system you are developing on. From the command line, limit (csh, tcsh) or ulimit -a (sh, bash) will output a variety of system defaults including the default process stack size.

Alternately, the system-defined default and maximum process stack sizes can be obtained using the `getrlimit` function call. See the Darwin man page for getrlimit for more information.

If you find your application is crashing because it is outgrowing the default 8 Megabyte stack allocation, you can raise its default by passing the `-stack_size` flag on the link line and specifying a new stack size up to 64 Megabytes.

Using Xcode:

Add `-Wl,-stack_size,1000000` to the __Other Linker Flags__ field of the Build Styles pane.

Using ld from a Makefile or command line:

`ld -stack_size 1000000 foo.o bar.o`

Using gcc, pass link flags through to ld with `-Wl`:

`gcc -Wl,-stack_size -Wl,1000000 foo.c`

Using the BSD system call `setrlimit`, you can increase the stack size of a process up to the size allowed by the system. See the Darwin man page for setrlimit for more information.

You can also increase the stack size allocated to threads as you create them. In Pthreads this is done by setting up a custom attribute and passing it to `pthread_create`.

__Listing 1__  Setting a Pthread's Stack Size

```c
#include <limits.h> #include <pthread.h>  #define REQUIRED_STACK_SIZE 1024*1024  int CreateThreadWithLargeStack (pthread_t *outThread, void *threadFunc, void *arg) {     int 			err = 0;     pthread_attr_t 	stackSizeAttribute;     size_t			stackSize = 0;      /*  Initialize the attribute */     err = pthread_attr_init (&stackSizeAttribute);     if (err) return (err);      /* Get the default value */     err = pthread_attr_getstacksize(&stackSizeAttribute, &stackSize);      if (err) return (err);      /* If the default size does not fit our needs, set the attribute with our required value */     if (stackSize < REQUIRED_STACK_SIZE)     {         err = pthread_attr_setstacksize (&stackSizeAttribute, REQUIRED_STACK_SIZE);         if (err) return (err);     }      /*  Create the thread with our attribute */     err = pthread_create (outThread, &stackSizeAttribute, threadFunc, arg);     return (err); }
```


If you are using Carbon Multiprocessing Services, you can set the stack size of an MPTask when it is created by passing a value other than 0 in the `stackSize` parameter of `MPCreateTask`.

As of Mac OS X 10.5, the NSThread class includes the `setStackSize:` method which can be used to set a stack size of up 1GB. Previous releases hard coded the stack size of an NSThread to 512KB.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-01-26 | Updated "Other Linker Flags" sntax for Xcode 3.1.2. |
| 2008-02-20 | Updated NSThread section for Leopard. |
| 2005-04-22 | New document that describes methods for setting the stack size of a process and/or thread. |

