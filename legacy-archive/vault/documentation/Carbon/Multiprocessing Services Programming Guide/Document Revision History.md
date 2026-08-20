---
title: Multiprocessing Services Programming Guide
apple_id: TP40000853
resource_type: Guide
platform: macOS
topic: null
technology: CoreServices
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Multitasking_MultiproServ/appendixd/appendixd.html
archived_at: '2026-07-15T05:23:37.875192Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Multiprocessing Services Programming Guide](Introduction%20to%20Multiprocessing%20Services%20Programming%20Guide.md)


[Next](Index.md)[Previous](Changes%20From%20Previous%20Versions%20of%20Multiprocessing%20Services.md)

# Document Revision History

This table describes the changes to _Multiprocessing Services Programming Guide_.

| __Date__ | __Notes__ |
| 2012-07-23 | Identified Multiprocessing Services as obsolete technology and moved the document to Retired Documents. |
| 2005-07-07 | Changed title from "Adding Multitasking Capability to Applications Using Multiprocessing Services." Indicated that MPAllocateAligned is not needed in Mac OS X. Emphasized avoiding calling MPTerminateTask if possible. Added link to "Multithreading" programming topic. |
|  | Fixed bugs that caused broken links in HTML. |
| 1999-10-15 | Revised for Multiprocessing Services 2.1. The following changes were made from the 2.0 version: |
|  | Added “Gestalt Constants”, which you can use to determine the availability of preemptively safe Mac OS system software functions, and added a list of these functions in [Preemptive Task–Safe Mac OS System Software Functions](Preemptive%20Task%E2%80%93Safe%20Mac%20OS%20System%20Software%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrwfvjvomi). Changed text in [Criteria for Creating Tasks](Using%20Multiprocessing%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvomjt) and [Making Remote Procedure Calls](Using%20Multiprocessing%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvomq) to reflect these additions. |
|  | Added new functions: `MPGetNextCpuID` and `MPGetNextTaskID`. |
|  | Added new kernel notification functions: `MPCreateNotification`, `MPCreateNotification`, `MPModifyNotification`, and `MPCauseNotification`. Added [Kernel Notifications](About%20Multitasking%20on%20the%20Mac%20OS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenryfvjvooa) section. |
|  | Added new options for `MPCreateTask`. See “Task Creation Options” for details. |
|  | Added new task information structure, `MPTaskInfo`, for use with `MPExtractTaskState`. |
|  | Added new task run state constants to be used with the new `MPTaskInfo` structure. See “Task Run State Constants” for details. |
|  | Added glossary entries for coherence groups and kernel notifications. |
| 1999-04-30 | Initial public release. The following changes were made from the previous (seed draft) version: Added [Introduction to Multiprocessing Services Programming Guide](Introduction%20to%20Multiprocessing%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenjrfvbecssgjfdeori)[About Multitasking on the Mac OS](About%20Multitasking%20on%20the%20Mac%20OS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenryfvjvomi) and [Using Multiprocessing Services](Using%20Multiprocessing%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvomi) which include introductory information, conceptual information, programming discussions, and sample code. |
|  | Added versioning information to functions, data types, and constants in “Multiprocessing Services Reference.” |
|  | Added discussion and parameter information to `MPTaskIsPreemptive` indicating how and why you can specify `kInvalidID` to determine the preemptiveness of the current task. Also added Version Notes section. |
|  | Correction in `MPWaitOnQueue`, `MPWaitOnSemaphore`, `MPWaitForEvent`, and `MPEnterCriticalRegion`: When calling from a cooperative task, you should specify only `kDurationImmediate` waits; others are allowable, but they will cause the task to block. |
|  | Added information stating that setting event bits in `MPSetEvent` and obtaining and clearing and event group in `MPWaitForEvent` are atomic operations. For example, bits cannot be set between when a task obtains an event group and when the event group is cleared, so no data can be lost. |
|  | Changed wording in `MPDelayUntil` to clarify that you must indicate a specific time to unblock the task, not a duration. |
|  | Changed wording for `MPAllocateTaskStorageIndex` and `MPDeallocateTaskStorageIndex` to indicate that these functions do not actually allocate or deallocate memory. |
|  | Added disclaimer to `MPThrowException` indicating that you should throw an exception to a task to stop it only if you are debugging and plan to examine the state of the task. Otherwise, you should block the task using a traditional notification method (such as a message queue). |
|  | Modified discussion of `MPSetExceptionHandler` to indicate the format of the message sent to the exception handler. Discussion of informative messages in `MPRegisterDebugger` removed to reflect status as of version 2.0. |
|  | Added information to `MPExtractTaskState` and `MPSetTaskState` indicating that attempting to set or read state information for a non-suspended task returns the error `kMPInsufficientResourcesErr`. Added information to `MPSetTaskState` and ”Task State Constants”: the exception state information and some machine registers (MRS, ExceptKind, DSISR, and DAR) are read-only. Attempting to set the exception state information will return an error. Attempts to change the MRS, ExceptKind, DSISR, and DAR registers will simply have no effect. |
|  | Discussion in `MPRemoteCall` modified to reflect this clarification: If you specify that the function should execute in the same context that owns the task, the function has access to data available to the main application (just as if the application had called the function). However, the function cannot execute until the owning context becomes active (and then not until the application calls `WaitNextEvent`). Atomic memory operations mentioned in `MPRemoteCall` and [Making Remote Procedure Calls](Using%20Multiprocessing%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvomq) are now located in `InterfaceLib`, not the Driver Services Library. |
|  | Data types `MPAddressSpaceID` and `MPCpuID` removed to reflect status as of version 2.0. |
|  | Clarified that you can use the constants in “Timer Duration Constants to specify any number of waiting times by adding multipliers. |
|  | Correction in “Memory Allocation Alignment Constants“: CPU interlock instruction `swarx` should be `stwcx`. |
|  | Specified the `MachineExceptions.h` structures that correspond to the state information constants in ”Task State Constants”. Removed non-bitmask values (`kMPTaskPropagate`, `kMPTaskResumeStep`, and `kMPTaskResumeBranch`) and descriptions from “Task Exception Disposal Constants“. |
| 1999-02-26 | First seed draft release |

[Next](Index.md)[Previous](Changes%20From%20Previous%20Versions%20of%20Multiprocessing%20Services.md)

