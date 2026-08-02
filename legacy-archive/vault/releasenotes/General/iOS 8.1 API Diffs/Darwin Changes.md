---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/Darwin.html
archived_at: '2026-07-18T02:56:11.241790Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# Darwin Changes

## Darwin

Removed malloc_size(UnsafePointer<Void>) -> UIntRemoved putchar() -> Int32Removed strcmp(UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32Removed strcpy(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>Removed strlen() -> UIntModified OSAtomicAdd32(Int32, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicAdd32Barrier(Int32, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicAdd64(Int64, UnsafeMutablePointer<Int64>) -> Int64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicAdd64Barrier(Int64, UnsafeMutablePointer<Int64>) -> Int64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified OSAtomicAnd32(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicAnd32Barrier(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicAnd32Orig(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified OSAtomicAnd32OrigBarrier(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified OSAtomicCompareAndSwap32(Int32, Int32, UnsafeMutablePointer<Int32>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicCompareAndSwap32Barrier(Int32, Int32, UnsafeMutablePointer<Int32>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicCompareAndSwap64(Int64, Int64, UnsafeMutablePointer<Int64>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicCompareAndSwap64Barrier(Int64, Int64, UnsafeMutablePointer<Int64>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified OSAtomicCompareAndSwapInt(Int32, Int32, UnsafeMutablePointer<Int32>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicCompareAndSwapIntBarrier(Int32, Int32, UnsafeMutablePointer<Int32>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicCompareAndSwapLong(Int, Int, UnsafeMutablePointer<Int>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicCompareAndSwapLongBarrier(Int, Int, UnsafeMutablePointer<Int>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicCompareAndSwapPtr(UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicCompareAndSwapPtrBarrier(UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicDecrement32(UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified OSAtomicDecrement32Barrier(UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified OSAtomicDecrement64(UnsafeMutablePointer<Int64>) -> Int64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified OSAtomicDecrement64Barrier(UnsafeMutablePointer<Int64>) -> Int64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified OSAtomicDequeue(COpaquePointer, UInt) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified OSAtomicEnqueue(COpaquePointer, UnsafeMutablePointer<Void>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified OSAtomicIncrement32(UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified OSAtomicIncrement32Barrier(UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified OSAtomicIncrement64(UnsafeMutablePointer<Int64>) -> Int64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified OSAtomicIncrement64Barrier(UnsafeMutablePointer<Int64>) -> Int64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified OSAtomicOr32(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicOr32Barrier(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicOr32Orig(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified OSAtomicOr32OrigBarrier(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified OSAtomicTestAndClear(UInt32, UnsafeMutablePointer<Void>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicTestAndClearBarrier(UInt32, UnsafeMutablePointer<Void>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicTestAndSet(UInt32, UnsafeMutablePointer<Void>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicTestAndSetBarrier(UInt32, UnsafeMutablePointer<Void>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicXor32(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicXor32Barrier(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSAtomicXor32Orig(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified OSAtomicXor32OrigBarrier(UInt32, UnsafeMutablePointer<UInt32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified OSMemoryBarrier()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSSpinLockLock(UnsafeMutablePointer<OSSpinLock>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSSpinLockTry(UnsafeMutablePointer<OSSpinLock>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified OSSpinLockUnlock(UnsafeMutablePointer<OSSpinLock>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified acl_get_permset_mask_np(acl_entry_t, UnsafeMutablePointer<acl_permset_mask_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified acl_maximal_permset_mask_np(UnsafeMutablePointer<acl_permset_mask_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified acl_set_permset_mask_np(acl_entry_t, acl_permset_mask_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified arc4random_buf(UnsafeMutablePointer<Void>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified arc4random_uniform() -> UInt32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified atexit_b() -> Void)!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified bsearch_b(UnsafePointer<Void>, UnsafePointer<Void>, UInt, UInt,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified dirfd(UnsafeMutablePointer<DIR>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified dlopen_preflight(UnsafePointer<Int8>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified endutxent_wtmp()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified ffsctl(Int32, UInt, UnsafeMutablePointer<Void>, UInt32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified ffsl() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified ffsll() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified fgetattrlist(Int32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UInt, UInt) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified fgetwln(UnsafeMutablePointer<FILE>, UnsafeMutablePointer<UInt>) -> UnsafeMutablePointer<wchar_t>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified filesec_unset_property(filesec_t, filesec_property_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified fls() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified flsl() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified flsll() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified fsetattrlist(Int32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UInt, UInt) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified fsync_volume_np(Int32, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified getdelim(UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<UInt>, Int32, UnsafeMutablePointer<FILE>) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified getiopolicy_np(Int32, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified getipv4sourcefilter(Int32, in_addr, in_addr, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<in_addr>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified getlastlogx(uid_t, UnsafeMutablePointer<lastlogx>) -> UnsafeMutablePointer<lastlogx>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified getlastlogxbyname(UnsafePointer<Int8>, UnsafeMutablePointer<lastlogx>) -> UnsafeMutablePointer<lastlogx>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified getline(UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<FILE>) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified getsourcefilter(Int32, UInt32, UnsafeMutablePointer<sockaddr>, socklen_t, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<sockaddr_storage>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified getutxent_wtmp() -> UnsafeMutablePointer<utmpx>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified glob_b(UnsafePointer<Int8>, Int32,((UnsafePointer<Int8>, Int32) -> Int32)!, UnsafeMutablePointer<glob_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified heapsort_b(UnsafeMutablePointer<Void>, UInt, UInt,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified imaxabs(intmax_t) -> intmax_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified imaxdiv(intmax_t, intmax_t) -> imaxdiv_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified j0() -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified j1() -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified jn(Int32, Double) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified lchflags(UnsafePointer<Int8>, __uint32_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified lchmod(UnsafePointer<Int8>, mode_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified lutimes(UnsafePointer<Int8>, UnsafePointer<timeval>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified malloc_default_purgeable_zone() -> UnsafeMutablePointer<malloc_zone_t>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified malloc_make_nonpurgeable(UnsafeMutablePointer<Void>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified malloc_make_purgeable(UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified malloc_zone_disable_discharge_checking(UnsafeMutablePointer<malloc_zone_t>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified malloc_zone_discharge(UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified malloc_zone_enable_discharge_checking(UnsafeMutablePointer<malloc_zone_t>) -> boolean_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified malloc_zone_enumerate_discharged_pointers(UnsafeMutablePointer<malloc_zone_t>,((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified malloc_zone_memalign(UnsafeMutablePointer<malloc_zone_t>, UInt, UInt) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified malloc_zone_pressure_relief(UnsafeMutablePointer<malloc_zone_t>, UInt) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified memmem(UnsafePointer<Void>, UInt, UnsafePointer<Void>, UInt) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified memset_pattern16(UnsafeMutablePointer<Void>, UnsafePointer<Void>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified memset_pattern4(UnsafeMutablePointer<Void>, UnsafePointer<Void>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified memset_pattern8(UnsafeMutablePointer<Void>, UnsafePointer<Void>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified memset_s(UnsafeMutablePointer<Void>, rsize_t, Int32, rsize_t) -> errno_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified mergesort_b(UnsafeMutablePointer<Void>, UInt, UInt,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified mkpath_np(UnsafePointer<Int8>, mode_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified posix_memalign(UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UInt, UInt) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified posix_spawn(UnsafeMutablePointer<pid_t>, UnsafePointer<Int8>, UnsafePointer<posix_spawn_file_actions_t>, UnsafePointer<posix_spawnattr_t>, UnsafePointer<UnsafeMutablePointer<Int8>>, UnsafePointer<UnsafeMutablePointer<Int8>>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawn_file_actions_addclose(UnsafeMutablePointer<posix_spawn_file_actions_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawn_file_actions_adddup2(UnsafeMutablePointer<posix_spawn_file_actions_t>, Int32, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawn_file_actions_addinherit_np(UnsafeMutablePointer<posix_spawn_file_actions_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified posix_spawn_file_actions_addopen(UnsafeMutablePointer<posix_spawn_file_actions_t>, Int32, UnsafePointer<Int8>, Int32, mode_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawn_file_actions_destroy() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawn_file_actions_init() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_destroy() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_getbinpref_np(UnsafePointer<posix_spawnattr_t>, UInt, UnsafeMutablePointer<cpu_type_t>, UnsafeMutablePointer<UInt>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_getflags(UnsafePointer<posix_spawnattr_t>, UnsafeMutablePointer<Int16>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_getpgroup(UnsafePointer<posix_spawnattr_t>, UnsafeMutablePointer<pid_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_getsigdefault(UnsafePointer<posix_spawnattr_t>, UnsafeMutablePointer<sigset_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_getsigmask(UnsafePointer<posix_spawnattr_t>, UnsafeMutablePointer<sigset_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_init() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_setauditsessionport_np(UnsafeMutablePointer<posix_spawnattr_t>, mach_port_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified posix_spawnattr_setbinpref_np(UnsafeMutablePointer<posix_spawnattr_t>, UInt, UnsafeMutablePointer<cpu_type_t>, UnsafeMutablePointer<UInt>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_setexceptionports_np(UnsafeMutablePointer<posix_spawnattr_t>, exception_mask_t, mach_port_t, exception_behavior_t, thread_state_flavor_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_setflags(UnsafeMutablePointer<posix_spawnattr_t>, Int16) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_setpgroup(UnsafeMutablePointer<posix_spawnattr_t>, pid_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_setsigdefault(UnsafeMutablePointer<posix_spawnattr_t>, UnsafePointer<sigset_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_setsigmask(UnsafeMutablePointer<posix_spawnattr_t>, UnsafePointer<sigset_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnattr_setspecialport_np(UnsafeMutablePointer<posix_spawnattr_t>, mach_port_t, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified posix_spawnp(UnsafeMutablePointer<pid_t>, UnsafePointer<Int8>, UnsafePointer<posix_spawn_file_actions_t>, UnsafePointer<posix_spawnattr_t>, UnsafePointer<UnsafeMutablePointer<Int8>>, UnsafePointer<UnsafeMutablePointer<Int8>>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified psort(UnsafeMutablePointer<Void>, UInt, UInt, CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified psort_b(UnsafeMutablePointer<Void>, UInt, UInt,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified psort_r(UnsafeMutablePointer<Void>, UInt, UInt, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified pthread_atfork(CFunctionPointer<(() -> Void)>, CFunctionPointer<(() -> Void)>, CFunctionPointer<(() -> Void)>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_destroy() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_getdetachstate(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_getguardsize(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<UInt>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_getinheritsched(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_getschedparam(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<sched_param>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_getschedpolicy(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_getscope(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_getstack(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UInt>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_getstackaddr(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_getstacksize(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<UInt>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_init() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_setdetachstate(UnsafeMutablePointer<pthread_attr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_setguardsize(UnsafeMutablePointer<pthread_attr_t>, UInt) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_setinheritsched(UnsafeMutablePointer<pthread_attr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_setschedparam(UnsafeMutablePointer<pthread_attr_t>, UnsafePointer<sched_param>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_setschedpolicy(UnsafeMutablePointer<pthread_attr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_setscope(UnsafeMutablePointer<pthread_attr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_setstack(UnsafeMutablePointer<pthread_attr_t>, UnsafeMutablePointer<Void>, UInt) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_setstackaddr(UnsafeMutablePointer<pthread_attr_t>, UnsafeMutablePointer<Void>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_attr_setstacksize(UnsafeMutablePointer<pthread_attr_t>, UInt) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_cancel() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_cond_broadcast() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_cond_destroy() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_cond_init(UnsafeMutablePointer<pthread_cond_t>, UnsafePointer<pthread_condattr_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_cond_signal() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_cond_signal_thread_np(UnsafeMutablePointer<pthread_cond_t>, pthread_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_cond_timedwait(UnsafeMutablePointer<pthread_cond_t>, UnsafeMutablePointer<pthread_mutex_t>, UnsafePointer<timespec>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_cond_timedwait_relative_np(UnsafeMutablePointer<pthread_cond_t>, UnsafeMutablePointer<pthread_mutex_t>, UnsafePointer<timespec>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_cond_wait(UnsafeMutablePointer<pthread_cond_t>, UnsafeMutablePointer<pthread_mutex_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_condattr_destroy() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_condattr_getpshared(UnsafePointer<pthread_condattr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_condattr_init() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_condattr_setpshared(UnsafeMutablePointer<pthread_condattr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_create(UnsafeMutablePointer<pthread_t>, UnsafePointer<pthread_attr_t>, CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, UnsafeMutablePointer<Void>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_create_suspended_np(UnsafeMutablePointer<pthread_t>, UnsafePointer<pthread_attr_t>, CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)>, UnsafeMutablePointer<Void>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_detach() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_equal(pthread_t, pthread_t) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_exit()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_from_mach_thread_np() -> pthread_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_get_stackaddr_np() -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_get_stacksize_np() -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_getconcurrency() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_getname_np(pthread_t, UnsafeMutablePointer<Int8>, UInt) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified pthread_getschedparam(pthread_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<sched_param>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_getspecific() -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_is_threaded_np() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_join(pthread_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_key_create(UnsafeMutablePointer<pthread_key_t>, CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_key_delete() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_kill(pthread_t, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mach_thread_np() -> mach_port_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_main_np() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutex_destroy() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutex_getprioceiling(UnsafePointer<pthread_mutex_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutex_init(UnsafeMutablePointer<pthread_mutex_t>, UnsafePointer<pthread_mutexattr_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutex_lock() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutex_setprioceiling(UnsafeMutablePointer<pthread_mutex_t>, Int32, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutex_trylock() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutex_unlock() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_destroy() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_getprioceiling(UnsafePointer<pthread_mutexattr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_getprotocol(UnsafePointer<pthread_mutexattr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_getpshared(UnsafePointer<pthread_mutexattr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_gettype(UnsafePointer<pthread_mutexattr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_init() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_setpolicy_np(UnsafeMutablePointer<pthread_mutexattr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified pthread_mutexattr_setprioceiling(UnsafeMutablePointer<pthread_mutexattr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_setprotocol(UnsafeMutablePointer<pthread_mutexattr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_setpshared(UnsafeMutablePointer<pthread_mutexattr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_mutexattr_settype(UnsafeMutablePointer<pthread_mutexattr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_once(UnsafeMutablePointer<pthread_once_t>, CFunctionPointer<(() -> Void)>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlock_destroy() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlock_init(UnsafeMutablePointer<pthread_rwlock_t>, UnsafePointer<pthread_rwlockattr_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlock_rdlock() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlock_tryrdlock() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlock_trywrlock() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlock_unlock() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlock_wrlock() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlockattr_destroy() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlockattr_getpshared(UnsafePointer<pthread_rwlockattr_t>, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlockattr_init() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_rwlockattr_setpshared(UnsafeMutablePointer<pthread_rwlockattr_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_self() -> pthread_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_setcancelstate(Int32, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_setcanceltype(Int32, UnsafeMutablePointer<Int32>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_setconcurrency() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_setname_np() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified pthread_setschedparam(pthread_t, Int32, UnsafePointer<sched_param>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_setspecific(pthread_key_t, UnsafePointer<Void>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_sigmask(Int32, UnsafePointer<sigset_t>, UnsafeMutablePointer<sigset_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_testcancel()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified pthread_threadid_np(pthread_t, UnsafeMutablePointer<__uint64_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified pthread_yield_np()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified qsort_b(UnsafeMutablePointer<Void>, UInt, UInt,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified rb_tree_count() -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified rb_tree_find_node(UnsafeMutablePointer<rb_tree_t>, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified rb_tree_find_node_geq(UnsafeMutablePointer<rb_tree_t>, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified rb_tree_find_node_leq(UnsafeMutablePointer<rb_tree_t>, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified rb_tree_init(UnsafeMutablePointer<rb_tree_t>, UnsafePointer<rb_tree_ops_t>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified rb_tree_insert_node(UnsafeMutablePointer<rb_tree_t>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified rb_tree_iterate(UnsafeMutablePointer<rb_tree_t>, UnsafeMutablePointer<Void>, UInt32) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified rb_tree_remove_node(UnsafeMutablePointer<rb_tree_t>, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified regncomp(UnsafeMutablePointer<regex_t>, UnsafePointer<Int8>, UInt, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified regnexec(UnsafePointer<regex_t>, UnsafePointer<Int8>, UInt, UInt, UnsafeMutablePointer<regmatch_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified regwcomp(UnsafeMutablePointer<regex_t>, UnsafePointer<wchar_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified regwexec(UnsafePointer<regex_t>, UnsafePointer<wchar_t>, UInt, UnsafeMutablePointer<regmatch_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified regwncomp(UnsafeMutablePointer<regex_t>, UnsafePointer<wchar_t>, UInt, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified regwnexec(UnsafePointer<regex_t>, UnsafePointer<wchar_t>, UInt, UInt, UnsafeMutablePointer<regmatch_t>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified scandir_b(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>>>,((UnsafePointer<dirent>) -> Int32)!,((UnsafeMutablePointer<UnsafePointer<dirent>>, UnsafeMutablePointer<UnsafePointer<dirent>>) -> Int32)!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified setiopolicy_np(Int32, Int32, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified setipv4sourcefilter(Int32, in_addr, in_addr, UInt32, UInt32, UnsafeMutablePointer<in_addr>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified setsourcefilter(Int32, UInt32, UnsafeMutablePointer<sockaddr>, socklen_t, UInt32, UInt32, UnsafeMutablePointer<sockaddr_storage>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified setutxent_wtmp()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified sockatmark() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified stpncpy(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, UInt) -> UnsafeMutablePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified strndup(UnsafePointer<Int8>, UInt) -> UnsafeMutablePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified strnlen(UnsafePointer<Int8>, UInt) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified strtoimax(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32) -> intmax_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified strtoumax(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32) -> uintmax_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified sync_volume_np(UnsafePointer<Int8>, Int32) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified system() -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified utmpxname() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified vdprintf(Int32, UnsafePointer<Int8>, CVaListPointer) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified vm_kernel_page_mask

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vm_kernel_page_shift

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified vm_kernel_page_size

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified wcpcpy(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>) -> UnsafeMutablePointer<wchar_t>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified wcpncpy(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, UInt) -> UnsafeMutablePointer<wchar_t>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified wcscasecmp(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified wcsdup() -> UnsafeMutablePointer<wchar_t>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified wcsncasecmp(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>, UInt) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified wcsnlen(UnsafePointer<wchar_t>, UInt) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified wcstoimax(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, Int32) -> intmax_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified wcstoumax(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, Int32) -> uintmax_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified wtmpxname() -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified y0() -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified y1() -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified yn(Int32, Double) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
