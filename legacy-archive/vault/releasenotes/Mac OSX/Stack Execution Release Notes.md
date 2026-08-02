---
title: Stack Execution Release Notes
apple_id: TP40006105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2007-07-17'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/RN-StackExecution/index.html
archived_at: '2026-07-18T02:58:41.043489Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Stack Execution Release Notes for Mac OS X v10.5

> [!IMPORTANT]
> 

### Restrictions on Executing from Data Areas

Beginning in Leopard, there is a change that affects 64-bit programs that dynamically generate and execute code in their address space. In prior releases, programs could generally execute from any part of their address space that was readable. The only exception to this rule was in Tiger on Intel systems regarding the stack: execution from any portion of the stack was disallowed unless the -allow_stack_execute option was given to `ld(1)` or the protections were changed on the stack region to allow execution via the [mprotect(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mprotect.2.html#//apple_ref/doc/man/2/mprotect) system call.

In Leopard, the restrictions on executing from data areas in 64-bit programs are expanding to increase security. Not only will attempts to execute from the stack area be disallowed, but execution from all other areas of a process's address space will be disallowed unless they are explicitly marked as executable. 64-bit programs that attempt to execute from their data areas without first marking them as executable will receive a SIGBUS signal. This applies to both Intel and PowerPC based systems.
This change only affects programs that have been compiled for 64-bit. Existing 32-bit programs are unaffected and they will continue to run without changes. Similarly, any new programs compiled for 32-bit and any old 32-bit programs that are recompiled under Leopard will also be unaffected.

By default, the instruction segment in an a.out file is marked as executable by ld, so programs that don't dynamically generate code and don't otherwise need to execute from their data areas require no changes. Note that the permissions on the segments in the a.out can be controlled with the -segprot option to ld. Also, the -allow_stack_execution option continues to be supported.

64-bit programs that generate code in dynamically allocated memory (via malloc, for example) must use the mprotect system call to add execute permission (specified with `PROT_EXEC`) to those pages before the program attempts to execute from them. If this is not done, the program will receive a SIGBUS signal when execution is attempted. To maximize security, programs should only add execute permission to those pages from which the program actually needs to execute.
