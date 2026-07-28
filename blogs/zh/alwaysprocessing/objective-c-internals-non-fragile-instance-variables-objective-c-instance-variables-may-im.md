---
title: 'Objective-C 内部实现：非脆弱实例变量（Non-Fragile Instance Variables）'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/03/12/objc-ivar-abi'
original_language: en
published: 2023-03-12
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1d8f40491166d9c8'
translated: true
---

> 原文：[Objective-C Internals: Non-Fragile Instance Variables Objective-C instance variables may impact ABI stability. In Objective-C 2, Apple introduced a "non-fragile" layout to preserve ABI stability acros](https://alwaysprocessing.blog/2023/03/12/objc-ivar-abi)　·　Always Processing (Brian T. Kelley)

# Objective-C 内部实现：非脆弱实例变量（Non-Fragile Instance Variables）

![两只黄色拉布拉多犬坐在堆满箱子的房间里。它们能否在不打翻任何东西的情况下重新排列这些箱子？](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c2988a3b-e50e-4f00-1116-eb898b8df300/public)

Objective-C 实例变量（instance variable）可能会影响 ABI 稳定性。在 Objective-C 2 中，Apple 引入了一种“非脆弱”布局（"non-fragile" layout），以在对类的实例变量进行某些类型的更改时保持 ABI 稳定性。

Objective-C 运行时（runtime）的部分机制对 ABI 有影响，这在 Objective-C 类中实例变量的演变过程中得到了体现。

## 脆弱实例变量（Fragile Instance Variables）

在 32 位版本的 macOS 中，Objective-C 类的实例变量采用“脆弱”布局（"fragile" layout），这意味着该部署目标下的实例变量通过其在类起始位置的偏移量（offset）来访问，就好像整个类层级（class hierarchy）中的实例变量被拼接成一个 C 结构体（C struct）一样。并且，就像 C 结构体中的字段一样，每个实例变量的偏移量在机器码中会被硬编码到每次读取或写入操作中，且一旦部署便无法更改。

因此，每个实例变量的大小、对齐方式（alignment）和偏移量都是其类 ABI 的一部分。在公开的 Objective-C 类中添加或删除实例变量可能会在运行时导致其子类（subclass）崩溃，这就是“脆弱”一词的由来。（更改实例变量的类型可视为先删除再添加的操作。）

当链接到一个二进制库（binary library，例如一个 App 链接到 AppKit 框架（framework））时，链接到该二进制库的实体（entity）依赖于其 ABI 保持“稳定”。为了维持稳定的 ABI，对二进制库所做的所有更改都不能使编译器和链接器（linker）用于与该库互操作的契约失效。如果新版本的二进制库更改了该契约，之前链接到它的任何内容都很可能会崩溃。

为了探究 Apple 在 Objective-C 2 之前如何处理 ABI 稳定性的限制，让我们检查以下来自 macOS 10.13 SDK 的经剪辑和注释的类定义。

```
// #import <objc/NSObject.h>
@interface NSObject <NSObject> {
  Class             isa;                // 0x00
}
@end

// #import <AppKit/NSResponder.h>
@interface NSResponder: NSObject {
  id                _nextResponder;     // 0x04
}
@end

// #import <AppKit/NSView.h>
typedef struct __VFlags {
  unsigned int flags;
} _VFlags;

@class _NSViewAuxiliary;

@interface NSView: NSResponder {
  /* 所有实例变量均为私有 */
  NSRect            _frame;             // 0x08
  NSRect            _bounds;            // 0x18
  NSView           *_superview;         // 0x28
  NSArray          *_subviews;          // 0x2c
  NSWindow         *_window;            // 0x30
  id                _unused_was_gState; // 0x34
  id                _frameMatrix;       // 0x38
  CALayer          *_layer;             // 0x3c
  id                _dragTypes;         // 0x40
  _NSViewAuxiliary *_viewAuxiliary;     // 0x44
  _VFlags           _vFlags;            // 0x48
  struct __VFlags2 {
    unsigned int flags;
  }                 _vFlags2;           // 0x4c
}
@end
```

上述每个实例变量右侧的注释指示了编译器进行读取或写入操作时所发出的相对于 `self` 指针的硬编码偏移量。

以下展示了 `NSView` 的实例变量 ABI，反映了其在内存中的布局（layout），以及编译器如何将实例变量视为 C 结构体中的字段。

```
struct NSViewHeapLayout {
  Class             isa;                // 0x00
  id                _nextResponder;     // 0x04
  NSRect            _frame;             // 0x08
  NSRect            _bounds;            // 0x18
  NSView           *_superview;         // 0x28
  NSArray          *_subviews;          // 0x2c
  NSWindow         *_window;            // 0x30
  id                _unused_was_gState; // 0x34
  id                _frameMatrix;       // 0x38
  CALayer          *_layer;             // 0x3c
  id                _dragTypes;         // 0x40
  _NSViewAuxiliary *_viewAuxiliary;     // 0x44
  _VFlags           _vFlags;            // 0x48
  struct __VFlags2  _vFlags2;           // 0x4c
};
```

如果我们仔细梳理自 Mac OS X 10.0 发布以来的所有公开 SDK，可以发现 `NSObject` 和 `NSResponder` 的实例变量没有发生变化（从而保持了 ABI 稳定性）。然而，`NSView` 有两个奇怪的实例变量，它们是维护 ABI 稳定性的产物：

1. `_unused_was_gState`

    - 在 Mac OS X 的早期版本中，`NSView` 有一个 `_gState` 实例变量，用于支持其集成到图形栈中。该状态在后续版本中已废弃，因此 AppKit 维护人员重命名了这个实例变量，以表明它已被有意弃用。
    - AppKit 维护人员不能删除这个实例变量，因为删除它会改变其后所有实例变量（包括子类中的）的偏移量。
    - 我怀疑维护人员没有重新利用这个实例变量，因为某些 App 可能读取（甚至写入）了该变量。这些 App 通常无法正确处理指向完全不同的不透明类型（opaque type）的指针，因此重新利用它可能会破坏这些 App。然而，对于使用该变量默认/占位值的情况，受影响的 App 可能仍能正常运行。

          - `@private` 访问修饰符（access modifier）是随 Objective-C 2 的发布一同添加到 Objective-C 语言中的。在引入访问控制之前，约定（convention）是防止子类直接访问超类（superclass）状态的唯一工具（这就是 `NSView` 实例变量块开头注释的原因）。
2. `_viewAuxiliary`：当一个类需要 ABI 稳定性时，使用私有辅助类（private helper class）是一种典型模式，以便在每个版本中保留添加或删除实例变量的能力。因此，每个 `NSView` 实例会分配一个 `_NSViewAuxiliary` 实例，用于存储实例变量和状态，而不会影响 `NSView` 的 ABI。

当一个类需要 ABI 稳定性但没有使用私有辅助类的选项时（例如 `NSObject` 或 `NSResponder`），另一种添加或删除实例变量的典型模式是使用侧表（side table）。（Mac OS X 10.6 和 iPhoneOS 3.1 中的 Objective-C 运行时通过其[关联引用（associated references）](https://alwaysprocessing.blog/2023/06/05/objc-assoc-obj)功能，为侧表存储提供了通用支持。）

## 非脆弱实例变量（Non-Fragile Instance Variables）

在 Objective-C 2 中，Apple 更改了 Objective-C 运行时和 ABI，以支持“非脆弱”布局，该布局适用于所有版本的 iOS、tvOS、watchOS 以及 64 位版本的 macOS。此功能在向类添加实例变量以及删除非公开实例变量时，保持了 ABI 稳定性。因此，不再需要使用上述模式（废弃的实例变量、私有辅助类和侧表存储）来保持 ABI 稳定性。

非脆弱实例变量布局有两个主要要求来保持 ABI 稳定性：

- 向类添加实例变量需要更新用于访问其后所有实例变量（包括所有子类中的实例变量）的偏移量。
- 从类中删除实例变量要求这些实例变量不能在类的二进制映像（binary image）之外被访问。

在编译 Objective-C 2 代码时，编译器会为每个实例变量发出一个偏移量符号（offset symbol），其使用满足了 ABI 稳定性的要求：

- 当 Objective-C 运行时检测到一个类的超类变大了时，它会更新该类的实例变量偏移量符号，以适应更大的超类大小。
- 对于具有 `@package` 或 `@private` 访问权限的实例变量，发出的符号在目标文件（object file）中具有私有外部可见性（private extern visibility），因此不会从二进制映像中导出。删除这些非公开实例变量是一种 ABI 稳定的更改，因为之前试图访问它们的任何代码都会链接失败。

如果超类缩小，Objective-C 运行时（目前）不会减小一个类的实例变量的偏移量。这种方法倾向于最小化 Objective-C 运行时堆（heap）的使用和 App 启动时间，但代价是受影响类的实例会使用更多的堆。

作为一种优化，每个偏移量符号的初始值是该实例变量在构建时（build time）的偏移量，这使得 Objective-C 运行时能够在基类没有增长时，跳过在每次 App 启动时计算偏移量。

## 脆弱布局与非脆弱布局示例

为了说明编译器在 Objective-C 1 和 Objective-C 2 之间生成代码的差异，让我们看一些加载 `_superview` 实例变量的简单代码。

```
NSView *superview = aView->_superview;
```

无论我们是编译 `NSView` 本身，还是构建第三方 App（假设该实例变量仍然是隐式的 `@public`），编译器发出的代码将是相同的。

在采用脆弱布局的 Objective-C 1 中，编译器简单地将编译时观察到的实例变量偏移量加到对象实例指针上，以计算出要加载该实例变量的地址。

```
NSView *superview = *(NSView **)((intptr_t)aView + 0x28);
```

如果在此次编译之后 `NSView` 的布局发生了变化，则在硬编码偏移量处进行的加载的结果可能会变得未定义。

在采用非脆弱布局的 Objective-C 2 中，编译器将实例变量偏移量符号的值加到对象实例指针上，以计算出要加载该实例变量的地址。

```
extern uint32_t OBJC_IVAR_$_NSView._superview;
NSView *superview = *(NSView **)((intptr_t)aView + OBJC_IVAR_$_NSView._superview);
```

`NSView` 的布局对此编译而言是不透明的，因此只要该实例变量存在，加载的结果将保持明确定义。然而，如果该实例变量被删除，`dyld` 将无法加载该二进制映像，因为实例变量偏移量符号将无法解析。（我想这总比未定义的运行时行为要好！）

## Objective-C 运行时实现

更新类的实例变量偏移量是在类的首次初始化中，作为 [`realizeClassWithoutSwift()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2594-L2741) 的一部分进行的。

```
static Class realizeClassWithoutSwift(Class cls, Class previously) {
  // ...
  // 协调实例变量偏移量/布局。
  // 这可能会重新分配 class_ro_t，更新我们的 ro 变量。
  if (supercls && !isMeta) reconcileInstanceVariables(cls, supercls, ro);
  // ...
}
```

只有当超类“增长”到子类中时（相对于在编译子类期间计算出的布局），才需要进行更新。超类可能因为增加了实例变量、将实例变量更改为更大尺寸的类型、向作为实例变量存储的 struct 中添加字段，或者其自身的超类增长了，而增大了大小。（回想一下，如果超类缩小了，运行时不会执行任何操作。）

[`reconcileInstanceVariables()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2484-L2581) 函数首先确保，如果需要更新类的实例变量偏移量，该 `class_ro_t`^[[1](#_footnotedef_1)] 数据结构已复制到堆上，因为初始数据结构值是从可执行文件的只读段（read-only section）映射而来的。需要一个可写副本，以便运行时能够存储更新后的类布局元数据（metadata）。

```
static void reconcileInstanceVariables(Class cls, Class supercls, const class_ro_t*& ro) {
  // ...
  if (ro->instanceStart >= super_ro->instanceSize) {
    // 超类没有超过其空间。我们完成了。
    return;
  }

  if (ro->instanceStart < super_ro->instanceSize) {
    // 超类大小已改变。此类的 ivar 必须移动。
    // 同时滑动布局位。
    // 此代码无法压缩子类以
    //   补偿缩小的超类，所以不要这样做。
    class_ro_t *ro_w = make_ro_writeable(rw);
    ro = rw->ro();
    moveIvars(ro_w, super_ro->instanceSize);
  }
}
```

[`moveIvars()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2433-L2481) 函数对类的实例变量偏移量符号应用必要的偏移调整，以适应超类的增长。

````
static void moveIvars(class_ro_t *ro, uint32_t superSize) {
  uint32_t diff = superSize - ro->instanceStart;

  if (ro->ivars) {
    // 查找此类 ivar 中的最大对齐
    uint32_t maxAlignment = 1;
    for (const auto& ivar : *ro->ivars) {
      if (!ivar.offset) continue;  // 匿名位域

      uint32_t alignment = ivar.alignment();
      if (alignment > maxAlignment) maxAlignment = alignment;
    }

    // 计算一个保持该对齐的偏移量
    uint32_t alignMask = maxAlignment - 1;
    diff = (diff + alignMask) & ~alignMask;

    // 整体滑动此类所有的 ivar
    for (const auto& ivar : *ro->ivars) {
      if (!ivar.offset) continue;  // 匿名位域

      uint32_t oldOffset = (uint32_t)*ivar.offset;
      uint32_t newOffset = oldOffset + diff;
      *ivar.offset = newOffset;
    }
  }

  *(uint32_t *)&ro->instanceStart += diff;
  *(uint32_t *)&ro->instanceSize += diff;
}
```
````

上面的 `for` 循环“滑动”了实例变量相对于类起始位置的偏移量，以适应更大的基类，同时保持对齐。它写入的 `ivar` 变量就是上一节讨论的实例变量偏移量符号，例如 `OBJC_IVAR_$_NSView._superview`。

因此，通过为读取或写入实例变量值增加一层间接寻址，并付出较小的潜在启动代价，Objective-C 运行时能够优雅地消除一个重大的 ABI 兼容性问题，且开销和复杂度都很小。

---

[1](#_footnoteref_1). 未来的文章将介绍只读和读写类元数据结构的划分。
