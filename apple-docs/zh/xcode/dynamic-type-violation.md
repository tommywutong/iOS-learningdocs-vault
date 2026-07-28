---
title: 动态类型违规
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/dynamic-type-violation
source_url: 'https://developer.apple.com/documentation/xcode/dynamic-type-violation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/dynamic-type-violation.json'
content_hash: 'sha256:118b930e261ecadd'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 动态类型违规

<sub>文章</sub>

检测对象具有错误动态类型的情况。

## 概述

使用此检查来检测对象具有错误动态类型的情况。动态类型违规可能导致意外的代码执行。此功能在 Xcode 9 及更高版本中可用。

### 在 C++ 中对类型不正确的实例进行成员调用

在以下代码中，`reinterpret_cast` 创建了一个动态类型错误的变量：

```occ
struct Animal {
    virtual const char *speak() = 0;
};
struct Cat : public Animal {
    const char *speak() override {
        return "meow";
    }
};
struct Dog : public Animal {
    const char *speak() override {
      return "woof";
    }
};
auto *dog = reinterpret_cast<Dog *>(new Cat); // 错误：dog 的动态类型不正确
dog->speak(); // 错误：此调用具有未定义行为
```

方法调用 `dog->speak()` 值得怀疑。如果 `Dog` 中的 `speak` 方法是 `final override`，优化器可以将该调用去虚拟化，因此 `dog->speak()` 可能返回 `"woof"`；否则，它可能返回 `"meow"`。

> [!note] 注意
> 此 UBSan 检查需要运行时类型信息，并且与 `-fno-rtti` 编译器标志不兼容。

#### 解决方案

谨慎使用 `reinterpret_cast`，并且仅在能够验证被转换对象是目标类型实例时使用。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐的指针](misaligned-pointer.md) — 检测代码访问未对齐指针或创建未对齐引用的情况。
- [无效布尔值](invalid-boolean.md) — 检测程序访问布尔变量，而其值既非 `true` 也非 `false` 的情况。
- [越界数组访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [无效枚举值](invalid-enumeration-value.md) — 检测枚举变量具有无效值的情况。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序到达不可达位置的情况。
- [无效浮点转换](invalid-float-cast.md) — 检测与浮点类型相互转换或在浮点类型之间转换时的超范围转换。
- [除以零](division-by-zero.md) — 检测除数为零的除法。
- [非空参数违规](nonnull-argument-violation.md) — 检测参数错误接收空值的情况。
- [非空返回值违规](nonnull-return-value-violation.md) — 检测函数错误返回空值的情况。
- [非空变量赋值违规](nonnull-variable-assignment-violation.md) — 检测错误地将空值赋给变量的情况。
- [创建空引用和解引用空指针](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建和空指针解引用。
- [无效对象大小](invalid-object-size.md) — 检测因类型大小差异导致的无效指针转换。
- [无效移位](invalid-shift.md) — 检测无效和溢出的移位。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效变长数组](invalid-variable-length-array.md) — 检测负数数组边界。
