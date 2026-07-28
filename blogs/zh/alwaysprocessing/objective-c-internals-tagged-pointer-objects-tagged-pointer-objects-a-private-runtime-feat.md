---
title: 'Objective-C 内部机制：Tagged Pointer 对象'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr'
original_language: en
published: 2023-03-19
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0204f51cfe1e305c'
translated: true
---

> 原文：[Objective-C Internals: Tagged Pointer Objects Tagged pointer objects (a private runtime feature) optimize performance by storing an object’s data in its pointer value, eliminating the object’s heap al](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr)　·　Always Processing (Brian T. Kelley)

# Objective-C 内部机制：Tagged Pointer 对象

![两只黄色的狗在树木繁茂的草地上跳跃。它们向上翘起鼻子，每只都跳起来去标记另一只。](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/0349e4f7-98ee-4653-764c-48a72cea8000/public)

Tagged Pointer 对象（一项私有运行时特性）通过在指针值中存储对象数据来优化性能，省去了对象的堆内存分配。本文通过分析 `NSNumber` 的实现，重点展示这一优化技术的使用及其影响。

Tagged Pointer 对象是 Objective-C 运行时的一项私有特性，Apple 用它来优化部分核心 Foundation 类（双关语）。

## 什么是 Tagged Pointer？

大多数内存分配器会保证每次分配的最小对齐。例如，Apple 平台上的 `malloc()` 保证的对齐“可以用于任何数据类型，包括 AltiVec 和 SSE 相关类型”。

实际上，所有分配都是 16 字节对齐的，因此任何指针的低 4 位始终为零。有时可以利用这一事实，在这些位中存储附加信息（这需要更新所有使用指针值的地方，以正确处理额外的位）。当指针中未使用的位存储了附加信息时，这种指针通常称为 _tagged（标记）_。

Objective-C 对象中的 `isa` 指针也可能是 tagged 的，其细节已在同一系列之前的文章 [The Many Uses of isa](https://alwaysprocessing.blog/2023/01/19/objc-class-isa) 的 [Non-Pointer isa](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa) 一节中讨论过。

## Tagged Pointer 对象

Objective-C 中的 Tagged Pointer 对象是一种特殊类型的对象指针。如果对象指针是 tagged 的，那么该 tagged 指针所代表的类实例所持有的数据会被完全编码到指针值本身中。不会发生堆内存分配。

省去堆内存分配可以显著降低成本，例如一个包含 `NSNumber` 对象的 `NSArray`。在堆上分配的 `NSNumber` 至少使用 16 字节（因为分配是 16 字节对齐的），再加上其指针的 8 字节。然而，编码到 tagged 指针中的 `NSNumber` 只使用其指针的 8 字节，通过不调用分配器同时节省了内存和时间。

### 标记标识

用于标识指针为 tagged 的位因平台而异。[objc-internal.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-internal.h#L755-L759) 为运行时实现提供了一个便捷函数，用于标识指针是否为 tagged。Intel 处理器上的 macOS 和 Catalyst 应用使用位 0 来标识 tagged pointer 对象，而其他所有平台使用位 63。

```
#if __arm64__
  // ARM64 uses a new tagged pointer scheme...
# define _OBJC_TAG_MASK (1UL<<63)
#elif (TARGET_OS_OSX || TARGET_OS_MACCATALYST) && __x86_64__
  // 64-bit Mac - tag bit is LSB
# define _OBJC_TAG_MASK 1UL
#else
  // Everything else - tag bit is MSB
# define _OBJC_TAG_MASK (1UL<<63)
#endif

static inline bool
_objc_isTaggedPointer(const void *ptr) {
  return ((uintptr_t)ptr & _OBJC_TAG_MASK) == _OBJC_TAG_MASK;
}
```

省去存储对象值的堆内存分配，同时也省去了存储 `isa` 指针的空间。因此，tagged pointer 对象方案会预留一些位来标识对象的类。

在撰写本文时，Objective-C 运行时具有两种预留类标识位的方案：一种为具有 60 位有效载荷的对象预留 3 位，另一种为具有 52 位有效载荷的对象预留 11 位。

最多有 7 种类型可以使用 60 位有效载荷变体（第八种类型是特殊情况，用于标识 52 位有效载荷变体）。最多有 256 种类型可以使用 52 位有效载荷变体。[objc-internal.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-internal.h#L447-L509) 中有一个枚举，为各种类标识位值提供了一些符号标识。

当运行时需要某个对象的 `isa` 指针时，它会调用 `objc_object::getIsa()`^[[1](#_footnotedef_1)]（定义在 [objc-object.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L76-L92) 中），该函数为堆上分配的对象返回 `isa` 实例变量，而为 tagged pointer 对象返回存储在某个 tag 类数组中的 `isa` 指针。

```
inline Class
objc_object::getIsa() {
  if (fastpath(!isTaggedPointer())) return ISA(/*authenticated*/true);

  extern objc_class OBJC_CLASS_$___NSUnrecognizedTaggedPointer;
  uintptr_t slot, ptr = (uintptr_t)this;
  Class cls;

  slot = (ptr >> _OBJC_TAG_SLOT_SHIFT) & _OBJC_TAG_SLOT_MASK;
  cls = objc_tag_classes[slot];
  if (slowpath(cls == (Class)&OBJC_CLASS_$___NSUnrecognizedTaggedPointer)) {
      slot = (ptr >> _OBJC_TAG_EXT_SLOT_SHIFT) & _OBJC_TAG_EXT_SLOT_MASK;
      cls = objc_tag_ext_classes[slot];
  }
  return cls;
}
```

当系统框架在进程启动时初始化，它们会调用 `_objc_registerTaggedPointerClass()` 来为给定的 tag 值设置 `Class` 对象。我们可以通过为该函数添加符号断点并打印其被调用时的参数来观察到这一点：

```
(lldb) reg re x0 x1
      x0 = 0x0000000000000003
      x1 = 0x0000000203a994f0  (void *)0x0000000203a99518: __NSCFNumber
```

### 消息发送的剖析

任何对指针值进行操作的代码都必须专门处理 tagged 指针，因为无条件解引用该指针几乎肯定会导致运行时崩溃。

`objc_msgSend()` 的第一步是[检查是否为 tagged 指针](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/Messengers.subproj/objc-msg-arm64.s#L578-L596)，以确定如何加载对象的 `isa` 指针来查找其类的方法，这与上面的 `objc_object:getIsa()` 实现类似。在 `isa` 指针被加载之后，无论指针是否为 tagged，对消息发送逻辑的其余部分都无关紧要。

当支持 tagged pointer 对象的 Objective-C 类接收到消息时，它必须检查其 `self` 指针是否为 tagged，并适当处理这种情况。以下是对 `-[NSNumber integerValue]` 的反汇编，部分展示了 `NSNumber` tagged 指针的工作方式（根据我对 macOS 12.6.2 上 arm64 以下函数反汇编的理解）。

```
@implementation __NSCFNumber
- (NSInteger)integerValue {
  return [self longValue];
}

- (long)longValue {
  long longValue;
  CFNumberGetValue((__bridge CFNumberRef)self, kCFNumberSInt64Type, &longValue);
  return longValue;
}
@end

Boolean CFNumberGetValue(CFNumberRef number, CFNumberType theType, void *valuePtr) {
  if (_objc_isTaggedPointer(number)) {
    if (_objc_getTaggedPointerTag(number) == OBJC_TAG_NSNumber) {
      long localMemory;
      valuePtr = valuePtr ?: (void *)&localMemory;

      uintptr_t value = _objc_getTaggedPointerValue(number);
      uintptr_t shift = (value & 0x08) ? 0x4 : 0x6;

      CFNumberType type = __CFNumberTypeTable[theType].canonicalType;
      if (type <= kCFNumberFloat64Type) {
        value = value >> shift;

        switch (type) {
        case kCFNumberSInt8Type:
          *(uint8_t *)valuePtr = (uint8_t)value;
          break;
        case kCFNumberSInt16Type:
          *(uint16_t *)valuePtr = (uint16_t)value;
          break;
        case kCFNumberSInt32Type:
          *(uint32_t *)valuePtr = (uint32_t)value;
          break;
        case kCFNumberSInt64Type:
          *(uint64_t *)valuePtr = (uint64_t)value;
          break;
        case kCFNumberFloat32Type:
          *(float *)valuePtr = (float)value;
          break;
        case kCFNumberFloat64Type:
          *(double *)valuePtr = (double)value;
          break;
        }
        return true;
      } else {
        return __CFNumberGetValueCompat(number, theType, valuePtr);
      }
    } else {
      theType = __CFNumberTypeTable[theType].canonicalType;
      return [(__bridge id)number _getValue:valuePtr forType:theType];
    }
  } else {
    // ...
  }
}
```

我将对上面手动反编译的代码分享几点评论和观察：

1. 私有的 `__NSCFNumber` 子类（在此代码路径中）并不对 `self` 的值进行操作，因此不需要处理 tagged 指针的情况。`-integerValue` 方法作为 `longValue` 方法的别名，后者调用 CoreFoundation 来完成繁重的工作。鉴于 `CFNumberRef` 和 `NSNumber *` 是[toll-free bridged](https://alwaysprocessing.blog/2023/02/16/objc-unrealized-classes#toll-free-bridging)，看到一种类型是另一种类型的包装器是有道理的。
2. Apple 的 `CFNumber` 实现几乎肯定包含 [objc-internal.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-internal.h#L755-L825)，以访问简化 tagged pointer 对象处理的函数。
3. 有效载荷中的 4 或 6 位似乎作为其他 `CFNumber` 功能的位标志，但无论该功能可能是什么，此函数并未使用。
4. [`__CFNumberTypeTable`](https://github.com/apple-oss-distributions/CF/blob/CF-1153.18/CFNumber.c#L385-L424) 将面向公众的类型值映射到对应的固定大小类型，简化了值提取逻辑。
5. Apple 有一个私有类型 [`kCFNumberSInt128Type`](https://github.com/apple-oss-distributions/CF/blob/CF-1153.18/CFNumber.c#L423)，switch 语句未处理该类型，因此对该情况的调用 `__CFNumberGetValueCompat()` 是必要的。
6. 具有非零小数部分的浮点数不使用 tagged pointer 对象优化，因为 `switch` 语句中的逻辑不处理该场景。
7. 我对 `-_getValue:forType:` 的调用很感兴趣。它暗示了另一个私有子类使用了 tag pointer 对象优化，但我没有跟踪各个代码路径来尝试识别它。

---

[1](#_footnoteref_1). 在我看来，使用 C++ 实现 Objective-C 运行时相当巧妙。我将在未来的文章中讨论其工作机理。
