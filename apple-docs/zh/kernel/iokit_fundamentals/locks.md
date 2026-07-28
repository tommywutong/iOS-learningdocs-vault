---
title: 锁
framework: Kernel
symbol_kind: symbol
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/iokit_fundamentals/locks
source_url: 'https://developer.apple.com/documentation/kernel/iokit_fundamentals/locks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/iokit_fundamentals/locks.json'
content_hash: 'sha256:e0c492476442a099'
translated: true
---

> 导航：[技术](../../technologies.md) · [Kernel](../../kernel.md) · [IOKit 基础](../iokit_fundamentals.md)

# 锁

<sub>API 集合</sub>

## 主题

### 简单锁

- [IOSimpleLockAlloc](../1553017-iosimplelockalloc.md) — 分配并初始化一个自旋锁。
- [IOSimpleLockInit](../1552990-iosimplelockinit.md) — 初始化一个自旋锁。
- [IOSimpleLockDestroy](../3380136-iosimplelockdestroy.md)
- [IOSimpleLockFree](../1553035-iosimplelockfree.md) — 释放一个自旋锁。
- [IOSimpleLockGetMachLock](../1553019-iosimplelockgetmachlock.md) — 获取一个 Mach 自旋锁的访问器。
- [IOSimpleLockLock](../1552997-iosimplelocklock.md) — 锁定一个自旋锁。
- [IOSimpleLockLockDisableInterrupt](../1553005-iosimplelocklockdisableinterrupt.md) — 锁定一个自旋锁。
- [IOSimpleLockTryLock](../1553029-iosimplelocktrylock.md) — 尝试锁定一个自旋锁。
- [IOSimpleLockUnlock](../1553015-iosimplelockunlock.md) — 解锁一个自旋锁。
- [IOSimpleLockUnlockEnableInterrupt](../1552998-iosimplelockunlockenableinterrup.md) — 解锁一个自旋锁，并恢复中断状态。

### 互斥锁

- [IOLockAlloc](../1553021-iolockalloc.md) — 分配并初始化一个互斥锁。
- [IOLockInitWithState](../1553028-iolockinitwithstate.md)
- [IOLockFree](../1553034-iolockfree.md) — 释放一个互斥锁。
- [IOTryLock](../1553012-iotrylock.md)
- [IOTakeLock](../1553007-iotakelock.md)
- [IOLockLock](../1553000-iolocklock.md) — 锁定一个互斥锁。
- [IOUnlock](../1552994-iounlock.md)
- [IOLockTryLock](../1553018-iolocktrylock.md) — 尝试锁定一个互斥锁。
- [IOLockUnlock](../1553006-iolockunlock.md) — 解锁一个互斥锁。
- [IOLockWakeup](../1553016-iolockwakeup.md)
- [IOLockSleep](../1553026-iolocksleep.md) — 睡眠，同时解锁并重新锁定互斥锁
- [IOLockSleepDeadline](../1553030-iolocksleepdeadline.md)
- [IOLockGetMachLock](../1553008-iolockgetmachlock.md) — 获取一个 Mach 互斥锁的访问器。

### 读写锁

- [IORWLockAlloc](../1553010-iorwlockalloc.md) — 分配并初始化一个读写锁。
- [IORWLockFree](../1553003-iorwlockfree.md) — 释放一个读写锁。
- [IORWLockGetMachLock](../1553033-iorwlockgetmachlock.md) — 获取一个 Mach 读写锁的访问器。
- [IORWLockRead](../1553004-iorwlockread.md) — 锁定一个读写锁用于读取。
- [IORWLockUnlock](../1553011-iorwlockunlock.md) — 解锁一个读写锁。
- [IORWLockWrite](../1552996-iorwlockwrite.md) — 锁定一个读写锁用于写入。
- [IORWUnlock](../1553027-iorwunlock.md)
- [IOWriteLock](../1552985-iowritelock.md)
- [IOReadLock](../1553022-ioreadlock.md)

### 递归锁

- [IORecursiveLockAlloc](../1553013-iorecursivelockalloc.md) — 分配并初始化一个递归锁。
- [IORecursiveLockFree](../1553031-iorecursivelockfree.md) — 释放一个递归锁。
- [IORecursiveLockGetMachLock](../1552988-iorecursivelockgetmachlock.md) — 获取一个 Mach 互斥锁的访问器。
- [IORecursiveLockHaveLock](../1552995-iorecursivelockhavelock.md) — 检查调用线程是否持有递归锁。
- [IORecursiveLockLock](../1553020-iorecursivelocklock.md) — 锁定一个递归锁。
- [IORecursiveLockSleep](../1553001-iorecursivelocksleep.md)
- [IORecursiveLockSleepDeadline](../1552986-iorecursivelocksleepdeadline.md)
- [IORecursiveLockTryLock](../1552993-iorecursivelocktrylock.md) — 尝试锁定一个递归锁。
- [IORecursiveLockUnlock](../1553032-iorecursivelockunlock.md) — 解锁一个递归锁。
- [IORecursiveLockWakeup](../1553014-iorecursivelockwakeup.md)

### 条件锁

- [IOConditionLock](../ioconditionlock.md)

## 另请参阅

### 相关资源

- [内存](memory.md) — 在内核中分配、映射、释放和管理内存。
- [工作流与控制](workflow_and_control.md)
- [数据类型](../libkern/data_types.md) — 创建字符串、数字、集合、数据对象以及驱动程序和内核扩展（kernel extension）所使用的其他标准类型。
