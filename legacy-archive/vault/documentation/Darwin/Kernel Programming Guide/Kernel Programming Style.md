---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/style/style.html
archived_at: '2026-07-15T07:23:14.187474Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Mach%20Overview.md)[Previous](Performance%20Considerations.md)

# Kernel Programming Style

As described in [Keep Out](Keep%20Out.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqguwuerkijjcemq2b), programming in the kernel is fraught with hazards that can cause instability, crashes, or security holes. In addition to these issues, programming in the kernel has the potential for compatibility problems. If you program only to the interfaces discussed in this document or other Apple documents, you will avoid the majority of these.

However, even limiting yourself to documented interfaces does not protect you from a handful of pitfalls. The biggest potential problem that you face is namespace collision, which occurs when your function, variable, or class name is the same as someone else’s. Since this makes one kernel extension or the other fail to load correctly (in a non-deterministic fashion), Apple has established function naming conventions for C and C++ code within the kernel. These are described in [Standard C Naming Conventions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqhawugskbirfegrsi) and [C++ Naming Conventions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqhawugskbirdeussj), respectively.

In addition to compatibility problems, kernel extensions that misbehave can also dramatically decrease the system’s overall performance or cause crashes. Some of these issues are described in [Performance and Stability Tips](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqhawugskbizbukqsc). For more thorough coverage of performance and stability, you should also read the chapters [Security Considerations](Security%20Considerations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqgywuerkijjcemq2b) and [Performance Considerations](Performance%20Considerations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqg4wuerkijjcemq2b).

Basic I/O Kit C++ naming conventions are defined in the document _[IOKit Device Driver Design Guidelines](../../Device%20Drivers/IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_. This section refines those conventions in ways that should make them more useful to you as a programmer.

The primary conventions are as follows:

- Use the Java-style reverse DNS naming convention, substituting underscores for periods. For example, `com_apple_foo`.
- Avoid the following reserved prefixes:

  - OS
  - os
  - IO
  - io
  - Apple
  - apple
  - AAPL
  - aapl

This ensures that you will not collide with classes created by other companies or with future classes added to the operating system by Apple. It does not protect you from other projects created within your company, however, and for this reason, some additional guidelines are suggested.

These additional guidelines are intended to minimize the chance of accidentally breaking your own software and to improve readability of code by developers.

- To avoid namespace collisions, you should prefix the names of classes and families with project names or other reasonably unique prefix codes.

  For example, if you are working on a video capture driver, and one of its classes is called `capture`, you will probably encounter a name collision eventually. Instead, you should name the class something like `com_mycompany_driver_myproduct_capture`. Similarly, names like

  To maximize readability, you should use macros to rename classes and families at compile time. For example:

```
#define captureClass com_mycompany_driver_myproduct_capture
#define captureFamily com_mycompany_iokit_myproduct_capture
```
- Use prefixes in function and method names to make it easier to see relationships between them. For example, Apple uses NS, CF, IO, and other prefixes to indicate that functions belong to specific frameworks. This might be as simple as prefixing a function with the name of the enclosing or related class, or it might be some other scheme that makes sense for your project.

These are only suggested guidelines. Your company or organization should adopt its own set of guidelines within the constraints of the basic conventions described in the previous section. These guidelines should provide a good starting point.

The naming conventions for C++ have been defined for some time in the document _[IOKit Device Driver Design Guidelines](../../Device%20Drivers/IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_. However, no conventions have been given for standard C code. Because standard C has an even greater chance of namespace collision than C++, it is essential that you follow these guidelines when writing C code for use in the kernel.

Because C does not have the benefit of classes, it is much easier to run into a naming conflict between two functions. For this reason, the following conventions are suggested:

- Declare all functions and (global) variables static where possible to prevent them from being seen in the global namespace. If you need to share these across files within your KEXT, you can achieve a similar effect by declaring them `__private_extern__`.
- Each function name should use Java-style reverse DNS naming. For example, if your company is apple.com, you should begin each function with `com_apple_`.
- Follow the reverse DNS name with the name of your project. For example, if you work at Apple and were working on project Schlassen, you would start each function name (in drivers) with `com_apple_driver_schlassen_`.
- Use hierarchical names if you anticipate multiple projects with similar names coming from different parts of your company or organization.
- Use macro expansion to save typing, for example `PROJECT_eat` could expand to `com_apple_driver_schlassen_pickle_eat`.
- If you anticipate that the last part of a function name may be the same as the last part of another function name (for example, `PROJECT1_eat` and `PROJECT2_eat`), you should change the names to avoid confusion (for example, `PROJECT1_eatpickle` and `PROJECT2_eatburger`).
- Avoid the following reserved prefixes:

  - OS
  - os
  - IO
  - io
  - Apple
  - apple
  - AAPL
  - aapl
- Avoid conflicting with any names already in the kernel, and do not use prefixes similar to those of existing kernel functions that you may be working with.
- Never begin a function name with an underscore (_).
- Under no circumstances should you use common names for your functions without prefixing them with the name of your project in some form. These are some examples of unacceptable names:

  - getuseridentity
  - get_user_info
  - print
  - find
  - search
  - sort
  - quicksort
  - merge
  - console_log

In short, picking any name that you would normally pick for a function is generally a bad idea, because every other developer writing code is likely to pick the same name for his or her function.

Occasional conflicts are a fact of life. However, by following these few simple rules, you should be able to avoid the majority of common namespace pitfalls.

One of the most common problems faced when programming in the kernel is use of “standard” functions—things like [printf](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/printf.3.html#//apple_ref/doc/man/3/printf) or [bcopy](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/bcopy.3.html#//apple_ref/doc/man/3/bcopy). Many commonly used standard C library functions are implemented in the kernel. In order to use them, however, you need to include the appropriate prototypes, which may be different from the user space prototypes for those functions, and which generally have different names when included from kernel code.

In general, any non–I/O Kit header that you can safely include in the kernel is located in `xnu/bsd/sys` or `xnu/osfmk/mach`, although there are a few specialized headers in other places like `libkern` and `libsa`. Normal headers (those in `/usr/include`) cannot be used in the kernel.

[Table 7-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqhawugsceiveumrke) lists some commonly used C functions, variables, and types, and gives the location of their prototypes.

__Table 7-1__  Commonly used C functions

| Function name | Header path |
| [printf](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/printf.3.html#//apple_ref/doc/man/3/printf) | `<sys/systm.h>` |
| Buffer cache functions (`bread`, `bwrite`, and `brelse`) | `<sys/buf.h>` |
| Directory entries | `<sys/dirent.h>` |
| Error numbers | `<sys/errno.h>` |
| Kernel special variables | `<sys/kernel.h>` |
| Spinlocks | `<sys/lock.h>` |
| [malloc](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/malloc.3.html#//apple_ref/doc/man/3/malloc) | `<sys/malloc.h>` |
| Queues | `<sys/queue.h>` |
| Random number generator | `<sys/rand.h>` |
| [bzero](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/bzero.3.html#//apple_ref/doc/man/3/bzero), [bcopy](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/bcopy.3.html#//apple_ref/doc/man/3/bcopy), [copyin](https://developer.apple.com/documentation/kernel/1441036-copyin), and [copyout](https://developer.apple.com/documentation/kernel/1441088-copyout) | `<sys/systm.h>` |
| `timeout` and `untimeout` | `<sys/system.h>` |
| Various time functions | `<sys/time.h>` |
| Standard type declarations | `<sys/types.h>`  `<mach/mach_types.h>` |
| User credentials | `<sys/ucred.h>` |
| OS and system information | `<sys/utsname.h>` |

If the standard C function you are trying to use is not in one of these files, chances are the function is not supported for use within the kernel, and you need to implement your code in another way.

The symbols in these header files are divided among multiple symbol sets, depending on the technology area where they were designed to be used. To use these, you may have to declare dependencies on any of the following:

- `com.apple.kernel`—You should generally avoid this.
- `com.apple.kernel.bsd`—BSD portions of the kernel.
- co`m.apple.kernel.iokit`—The I/O Kit.
- `com.apple.kernel.libkern`—General-purpose functions.
- `com.apple.kernel.mach`—Mach-specific APIs.
- `com.apple.kpi.bsd`—BSD portions of the kernel (v10.4 and later).
- co`m.apple.kernel.iokit`—The I/O Kit (v10.4 and later).
- `com.apple.kernel.libkern`—General-purpose functions (v10.4 and later).
- `com.apple.kernel.mach`—Mach-specific APIs (v10.4 and later).
- `com.apple.kpi.unsupported`—Unsupported legacy functionality (v10.4 and later).

Where possible, you should specify a dependency on the KPI version of these symbols. However, these symbols are only available in v10.4 and later. For the I/O Kit and libkern, this should make little difference. For other areas, such as network kernel extensions or file system KEXTs, you must use the KPI versions if you want your extension to load in OS X v10.4 and later.

For a complete list of symbols in any of these dependencies, run `nm` on the binaries in `/System/Library/Extensions/System.kext/PlugIns`.

This section includes some basic tips on performance and stability. You should read the sections on security and performance for additional information. These tips cover only style issues, not general performance or stability issues.

Programming in the kernel is subject to a number of restrictions that do not exist in application programming. The first and most important is the stack size. The kernel has a limited amount of space allocated for thread stacks, which can cause problems if you aren’t aware of the limitation. This means the following:

- Recursion _must_ be bounded (to no more than a few levels).
- Recursion should be rewritten as iterative routines where possible.
- Large stack variables (function local) are dangerous. Do not use them. This also applies to large local arrays.
- Dynamically allocated variables are preferred (using [malloc](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/malloc.3.html#//apple_ref/doc/man/3/malloc) or equivalent) over local variables for objects more than a few bytes in size.
- Functions should have as few arguments as possible.

  - Pass pointers to structures, not the broken out elements.
  - Don’t use arguments to avoid using global or class variables.
  - Do name global variables in a way that protects you from collision.
- C++ functions should be declared static.
- Functions not obeying these rules can cause a kernel panic, or in extreme cases, do not even compile.

In addition to issues of stack size, you should also avoid doing anything that would generate unnecessary load such as polling a device or address. A good example is the use of mutexes rather than spinlocks. You should also structure your locks in such a way to minimize contention and to minimize hold times on the most highly contended locks.

Also, since unused memory (and particularly wired memory) can cause performance degradation, you should be careful to deallocate memory when it is no longer in use, and you should never allocate large regions of wired memory. This may be unavoidable in some applications, but should be avoided whenever possible and disposed of at the earliest possible opportunity. Allocating large contiguous blocks of memory at boot time is almost never acceptable, because it cannot be released.

There are a number of issues that you should consider when deciding whether to use floating point math or AltiVec vector math in the kernel.

First, the kernel takes a speed penalty whenever floating-point math or AltiVec instructions are used in a system call context (or other similar mechanisms where a user thread executes in a kernel context), as floating-point and AltiVec registers are only maintained when they are in use.

In general, you should avoid doing using floating-point math or AltiVec instructions in the kernel unless doing so will result in a significant speedup. It is not forbidden, but is strongly discouraged.

Second, AltiVec was not supported in the kernel prior to OS X v10.3. It was not possible to detect this support from within the kernel until a later 10.3 software update. If you must deploy your KEXT on earlier versions of OS X, you must either provide a non-AltiVec version of your code or perform the AltiVec instructions in user space.

Finally, AltiVec data stream instructions (`dst`, `dstt`, `dstst`, `dss`, and `dssall`) are not supported in the kernel, even for processors that support them in user space. Do not attempt to use them.

If you decide to use AltiVec in the kernel, your code can determine whether the CPU supports AltiVec using the [sysctlbyname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctlbyname.3.html#//apple_ref/doc/man/3/sysctlbyname) call to get the `hw.optional.altivec` property. For more information, see [The sysctlbyname System Call](Boundary%20Crossings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wviucykjcummjrhe).

- Don’t sleep while holding resources (locks, for example). While this is not forbidden, it is strongly discouraged to avoid deadlock.
- Be careful to allocate and free memory with matching calls. For example, do not use allocation routines from the I/O Kit and deallocation routines from BSD. Likewise, do not use [IOMallocContiguous](https://developer.apple.com/documentation/kernel/1575289-iomalloccontiguous) with `IOFreePageable`.
- Use reference counts to avoid freeing memory that is still in use elsewhere. Be sure to deallocate memory when its reference count reaches zero, but not before.
- Lock objects before operating on them, even to change reference counts.
- Never dereference pointers without verifying that they are not `NULL`. In particular, never do this:

```
int foo = *argptr;
```

  unless you have already verified that `argptr` cannot possibly be `NULL`.
- Test code in sections and try to think up likely edge cases for calculations.
- Never assume that your code will be run only on big endian processors.
- Never assume that the size of an instance of a type will never change. Always use `sizeof` if you need this information.
- Never assume that a pointer will always be the same size as an `int` or `long`.

Kernel programming style is very much a matter of personal preference, and it is not practical to programmatically enforce the guidelines in this chapter. However, we strongly encourage you to follow these guidelines to the maximum extent possible. These guidelines were created based on frequent problems reported by developers writing code in the kernel. No one can force you to use good style in your programming, but if you do not, you do so at your own peril.

[Next](Mach%20Overview.md)[Previous](Performance%20Considerations.md)

