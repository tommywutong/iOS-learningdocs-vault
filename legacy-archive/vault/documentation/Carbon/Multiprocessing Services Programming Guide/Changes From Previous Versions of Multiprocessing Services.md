---
title: Multiprocessing Services Programming Guide
apple_id: TP40000853
resource_type: Guide
platform: macOS
topic: null
technology: CoreServices
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Multitasking_MultiproServ/appendixc/appendixc.html
archived_at: '2026-07-15T05:23:37.864186Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Multiprocessing Services Programming Guide](Introduction%20to%20Multiprocessing%20Services%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Calculating%20the%20Intertask%20Signaling%20Time.md)

# Changes From Previous Versions of Multiprocessing Services

Multiprocessing Services 2.1 supports all the functions available with version 2.0. For compatibility between version 2.0 and older versions, see Table C-3, Table C-4, and Table C-5.

Table C-1 lists Multiprocessing Services functions introduced with version 2.1:

__Table C-1__  New functions introduced with version 2.1

| Name | Comments |
| `MPGetNextCpuID` |  |
| `MPGetNextTaskID` |  |
| `MPCreateNotification` | For manipulating kernel notifications. See [Kernel Notifications](About%20Multitasking%20on%20the%20Mac%20OS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenryfvjvooa) for more information about this notification mechanism. |
| `MPDeleteNotification` | For manipulating kernel notifications. See [Kernel Notifications](About%20Multitasking%20on%20the%20Mac%20OS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenryfvjvooa) for more information about this notification mechanism. |
| `MPModifyNotification` | For manipulating kernel notifications. See [Kernel Notifications](About%20Multitasking%20on%20the%20Mac%20OS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenryfvjvooa) for more information about this notification mechanism. |
| `MPCauseNotification` | For manipulating kernel notifications. See [Kernel Notifications](About%20Multitasking%20on%20the%20Mac%20OS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenryfvjvooa) for more information about this notification mechanism. |

Table C-2 lists Multiprocessing Services functions that were introduced in version 2.0.

__Table C-2__  Functions introduced with version 2.0

| Name | Comments |
| `MPProcessorsScheduled` |  |
| `MPsetTaskWeight` |  |
| `MPTaskIsPreemptive` |  |
| `MPAllocateTaskStorageIndex` |  |
| `MPDeallocateTaskStorageIndex` |  |
| `MPSetTaskStorageValue` |  |
| `MPGetTaskStorageValue` |  |
| `MPSetQueueReserve` |  |
| `MPCreateEvent` |  |
| `MPDeleteEvent` |  |
| `MPSetEvent` |  |
| `MPWaitForEvent` |  |
| `UpTime` |  |
| `DurationToAbsolute` |  |
| `AbsoluteToDuration` |  |
| `MPDelayUntil` |  |
| `MPCreateTimer` |  |
| `MPDeleteTimer` |  |
| `MPSetTimerNotify` |  |
| `MPArmTimer` |  |
| `MPCancelTimer` |  |
| `MPSetExceptionHandler` |  |
| `MPThrowException` |  |
| `MPDisposeTaskException` |  |
| `MPExtractTaskState` |  |
| `MPSetTaskState` |  |
| `MPRegisterDebugger` |  |
| `MPRegisterDebugger` |  |
| `MPAllocateAligned` | Preferred over MPAllocate. |
| MPGetAllocatedBlockSize |  |
| `MPBlockClear` |  |
| `MPDataToCode` |  |
| `MPRemoteCall` | Preferred over `_MPRPC` |

Table C-3 lists the functions that were introduced in version 1.0 that are still supported in version 2.0.

__Table C-3__  Older functions supported in version 2.0

| Name | Comments |
| `MPProcessors` |  |
| `MPCreateTask` |  |
| `MPTerminateTask` |  |
| `MPCurrentTaskID` |  |
| `MPYield` |  |
| `MPExit` |  |
| `MPCreateQueue` |  |
| `MPDeleteQueue` |  |
| `MPNotifyQueue` |  |
| `MPWaitOnQueue` |  |
| `MPCreateSemaphore` |  |
| `MPCreateBinarySemaphore` | In C, a macro that calls `MPCreateSemaphore`. |
| `MPDeleteSemaphore` |  |
| `MPSignalSemaphore` |  |
| `MPWaitOnSemaphore` |  |
| `MPCreateCriticalRegion` |  |
| `MPDeleteCriticalRegion` |  |
| `MPEnterCriticalRegion` |  |
| `MPExitCriticalRegion` |  |
| `MPAllocate` | Deprecated. Use `MPAllocateAligned` instead. |
| `MPFree` |  |
| `MPBlockCopy` |  |
| `MPLibraryIsLoaded` | In C, a macro that checks to see if the `MPProcessors` symbol is resolved. |

Table C-4 shows unofficial functions included in earlier header files that remain supported in version 2.0. Note, however, that future versions may not support these functions.

__Table C-4__  Unofficial functions still supported in version 2.0

| Name | Comments |
| `_MPRPC` | Deprecated. Use `MPRemoteCall` instead. |
| `_MPAllocateSys` | Deprecated. Use `MPAllocateAligned` instead. |
| `_MPTaskIsToolboxSafe` |  |
| `_MPLibraryVersion` |  |
| `_MPLibraryIsCompatible` |  |

Table C-5 shows functions used for debugging that are no longer supported in version 2.0. You can access these functions for older builds if you `#define MPIncludeDefunctServices` to be nonzero.

__Table C-5__  Debugging functions unsupported in version 2.0

| Name | Comments |
| `_MPInitializePrintf` |  |
| `_MPPrintf` |  |
| `_MPDebugStr` |  |
| `_MPStatusPString` |  |
| `_MPStatusCString` |  |

[Next](Document%20Revision%20History.md)[Previous](Calculating%20the%20Intertask%20Signaling%20Time.md)

