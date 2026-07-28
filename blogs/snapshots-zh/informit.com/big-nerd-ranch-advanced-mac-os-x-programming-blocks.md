---
title: 'Big Nerd Ranch Advanced Mac OS X 编程：Block'
source_url: 'https://www.informit.com/articles/article.aspx?p=1749597&seqNum=12'
source_domain: informit.com
source_group: single-site
original_language: en
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:c6bf79d578c7fbd1'
plan_ref: 第二周：weak、属性关键字与 Block / Day 3｜先看 Block 是什么，再谈捕获（对应 W2-12、W2-13、W2-15）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 3｜先看 Block 是什么，再谈捕获（对应 W2-12、W2-13、W2-15）
container: '//div[contains(@class,''articleProduct'')]'
container_source: map
translated: true
---

> 原文：[Big Nerd Ranch Advanced Mac OS X Programming: Blocks](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=12)

[首页](https://www.informit.com/) \> [文章](https://www.informit.com/articles/index.aspx) \> [家庭与办公计算](https://www.informit.com/articles/index.aspx?st=60192) \> [Mac OS X](https://www.informit.com/articles/index.aspx?st=98692)

# [Big Nerd Ranch Advanced Mac OS X 编程：Block](https://www.informit.com/articles/article.aspx?p=1749597)

- 2011 年 11 月 14 日

[📄 目录](#)

[␡](#)

1. [Block 语法](https://www.informit.com/articles/article.aspx?p=1749597)
2. [返回值](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=2)
3. [访问封闭作用域](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=3)
4. [修改封闭作用域](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=4)
5. [Block 变量](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=5)
6. [变量捕获再探](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=6)
7. [作为对象的 Block](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=7)
8. [何时复制](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=8)
9. [集合中的 Block](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=9)
10. [Block 保留循环](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=10)
11. [使用 Block 的新 API](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=11)
12. 更进一步：Block 内部实现
13. [练习](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=13)

- [⎙ 打印](https://www.informit.com/articles/printerfriendly/1749597)

## 更进一步：Block 内部实现

Block 和 `__block` 变量是通过结构与函数的组合来实现的。这些结构与函数由编译器生成，并由运行时（runtime）环境维护。了解底层工作机制有助于理解内存管理和调试的细节。

### 实现

编译器会解释新的、Block 专有的语法，并生成数据来与运行时交互，以及生成依赖运行时提供的函数的代码。Block 运行时使得 Block 在应用实际运行时能够被使用。

具体的编译器与我们这里的讨论无关。**gcc** 和 **clang** 之间最明显的区别在于，编译器为了支持 Block 和 `__block` 变量而生成的私有结构与函数的名称不同。

这些私有结构与函数构成了 Block 实现的核心。

#### Block 字面量

每个 Block 字面量声明都会触发编译器生成两个结构体和至少一个函数。这两个结构体描述了 Block 及其运行时信息；该函数则包含了 Block 的可执行代码。

这两个结构体是 *Block 字面量*（也称为“Block 持有者”）和 *Block 描述符*。

一个 Block 描述符看起来像这样：

```
static const struct block_descriptor_NAME {
    unsigned long reserved;
    unsigned long literal_size;

    /* helper functions - present only if needed */
    void (*copy_helper)(void *dst, void *src);
    void (*dispose_helper)(void *src);
};
```

`reserved` 字段目前未被使用。`literal_size` 字段被设置为对应 Block 字面量的大小。两个辅助函数指针仅在需要时才存在。当 Block 引用了一个 Objective-C 或 C++ 对象，或者一个 `__block` 变量时，就需要它们。当需要辅助函数时，编译器除了生成实现 Block 字面量主体的函数外，还会生成这些辅助函数。

一个 Block 字面量看起来像这样：

```
struct block_literal_NAME {
    void *isa;
    int flags;
    int reserved;
    void (*invoke)(void *literal, ...);
    struct block_descriptor_NAME *descriptor;
    /* referenced captured variables follow */
};
```

`isa` 指针使得 Block 成为一个 Objective-C 对象。即使在不使用 Objective-C 的情况下，Block 运行时仍然使用 `isa` 指针来指示它正在处理的是哪种 Block。

`isa` 字段将指向：

**_NSConcreteStackBlock**

当 Block 在栈上时。

**_NSConcreteGlobalBlock**

当 Block 在全局存储区时。

**_NSConcreteMallocBlock**

当 Block 在堆上时。

**_NSConcreteAutoBlock**

当 Block 在可回收内存中时。在使用垃圾回收器（garbage collector）的情况下，当某个未引用 C++ 对象的栈 Block 被复制到堆上时，便会使用此类。

**_NSConcreteFinalizingBlock**

当 Block 在可回收内存中并且被回收时必须运行终结器（finalizer）时。在使用垃圾回收器的情况下，当某个引用了 C++ 对象的栈 Block 被复制到堆上时，便会使用此类——因为运行时必须确保在回收该 Block 时调用 C++ 对象的析构函数。

所有这些 Block 类都是 **_NSAbstractBlock** 的子类。这个抽象类为 Block 使用的内存相关方法提供了实现。各个具体子类存在的唯一目的，就是指示 Block 存储位置的信息。

`flags` 字段提供了关于 Block 的进一步信息：

```
enum {
    BLOCK_REFCOUNT_MASK    = (0xFFFF),
    BLOCK_NEEDS_FREE       = (1 << 24),
    BLOCK_HAS_COPY_DISPOSE = (1 << 25),
    BLOCK_HAS_CXX_OBJ      = (1 << 26),
    BLOCK_IS_GC            = (1 << 27),
    BLOCK_IS_GLOBAL        = (1 << 28),
    BLOCK_HAS_DESCRIPTOR   = (1 << 29),
};
```

`BLOCK_REFCOUNT_MASK`、`BLOCK_NEEDS_FREE` 和 `BLOCK_IS_GC` 会在 Block 被复制时，由运行时按需设置。

`BLOCK_IS_GLOBAL` 会在编译时，针对位于全局存储区中的 Block 设置。复制和释放这类 Block 不会有任何效果，因为该 Block 始终驻留在应用的内存中。如果某个栈局部的 Block 没有引用任何栈局部（包括 `__block`）变量，编译器可能会选择将其提升到静态内存并设置 `BLOCK_IS_GLOBAL` 标志。

`BLOCK_HAS_DESCRIPTOR` 始终会被设置。这个标志的加入，是为了将最终随 Snow Leopard 一起发布的 Block 实现版本与此前的实现区分开来。

每个 Block 调用函数都会接收一个指向调用它的 Block 字面量的指针，作为其第一个参数。这为该函数提供了访问 Block 捕获变量的途径。这在功能上等同于 C++ 成员函数第一个参数中的 `this` 指针——成员函数用它来访问成员变量；也等同于 Objective-C 实例方法获取的第一个参数 `self` 指针——方法用它来访问实例变量。与 C++ 一样，Block 调用函数的返回值及剩余参数也由程序员声明。（Objective-C 在 `self` 和程序员声明的参数之间还会增加一个隐式参数 `_cmd`，该参数会被设置为方法的选择器（selector）。）

除了那些明显被引用的捕获变量之外，Block 还被视作引用了嵌套在它内部的所有 Block 所引用的全部变量。来看下面这个简短的例子：

```
int x = 0;
int y = 1;
int (^b)(void) = ^{
    int (^c)(void) = ^{
        return y;
    };
    return x + c();
}
```

这里，赋值给 `b` 的那个 Block 被认为同时引用了 `x` 和 `y`。

要了解 Block 字面量、Block 描述符和 Block 调用函数是如何组合在一起的，请考虑以下代码：

```
void f(void) {
    int x = 0;
    int (^b)(void) = ^{ return x + 1; };
    int y = b();
}
```

编译器会把这段代码转换成类似下面的形式：

```
typedef void (*generic_invoke_funcptr)(void *, ...);
struct __block_literal {
    void *isa;
    int flags;
    int reserved;
    generic_invoke_funcptr invoke;
    struct __block_descriptor_tmp *descriptor;
    const int captured_x;
};

static const struct __block_descriptor_tmp {
    unsigned long reserved;
    unsigned long literal_size;
    /* no copy/dispose helpers needed */
} __block_descriptor_tmp = {
    0UL, sizeof(struct __block_literal)
};

// ^int (void) { return x + 1; }
int __f_block_invoke_(struct __block_literal *bp) {
    return bp->captured_x + 1;
}
typedef int (*iv_funcptr)(struct __block_literal *);

void f(void) {
    int x = 0;
    // int (^b)(void) = ^{ return x + 1 };
    struct __block_literal __b = {
        .isa = &_NSConcreteStackBlock,
        .flags = BLOCK_HAS_DESCRIPTOR,
        .reserved = 0,
        .invoke = (generic_invoke_funcptr)__f_block_invoke_,
        .descriptor = &__block_descriptor_tmp,
        .captured_x = x
    };
    struct __block_literal *b = &__b;
    int y = (*(iv_funcptr)(b->invoke))(b);
}
```

注意，Block 变量实际上是一个指向栈上创建的结构的指针。在思考 Block 字面量何时必须被复制时，牢牢记住这一点会很有帮助。

#### `__block` 变量

和 Block 字面量一样，`__block` 变量既可以从栈移动到堆，其变量数据也可能需要内存管理——例如当该变量是 Objective-C 对象时。因此，`__block` 变量同样被编译为一个结构体，并在必要时生成辅助函数。

为了确保对所有 `__block` 变量的操作处理的都是变量的当前位置，所有访问都通过一个转发指针（forwarding pointer）进行中转。当某个 `__block` 变量从栈复制到堆时，栈上和堆中两个结构体的转发指针都会被更新为指向堆中的结构体。

由于所有对 `__block` 变量的访问都按引用进行，因此与 `__block` 变量关联的结构和函数名称中会嵌入“byref”。

byref 结构体看起来像这样：

```
struct Block_byref {
    void *isa;
    struct Block_byref *forwarding;
    int flags;
    int size;

    /* helper functions - present only if needed */
    void (*byref_keep)(struct Block_byref *dst, struct Block_byref *src);
    void (*byref_destroy)(struct Block_byref *);

    /* actual variable data follows */
}
```

`isa` 字段初始时始终为 `NULL`。当带有 `__weak` 限定符的 `__block` 变量被复制时，这个字段会被设置为 `&NSConcreteWeakBlockVariable`。

转发指针始终指向权威的 byref 头部的起始位置。在一开始，这永远会是包含该转发指针的 byref 结构体自身的地址。

`flags` 字段用于指示复制和释放的辅助函数是否存在。如果不存在，它将被初始化为 `0`；否则将初始化为 `BLOCK_HAS_COPY_DISPOSE`。与 Block 字面量一样，当结构体在运行时被复制时，`flags` 字段还会用内存管理信息进行更新。如果它被复制到扫描内存中，则会设置 `BLOCK_IS_GC`；否则将设置 `BLOCK_NEEDS_FREE`，并用低两个字节存储引用计数。

`size` 会被设置为该 `Block_byref` 结构体的具体大小。

如果 byref 变量为 Block 引用、Objective-C 对象或 C++ 对象，编译器就会合成辅助函数。如果存在辅助函数，`flags` 字段将包含 `BLOCK_HAS_COPY_DISPOSE`。在复制和释放引用了 `__block` 变量的 Block 时，这些辅助函数会被调用。

当某个 Block 捕获一个 `__block` 变量时，它持有的是该 byref 结构体的转发指针，并通过这个指针与变量交互。这样，Block 就需要复制和释放辅助函数来处理所捕获的 `__block` 变量的复制和释放。

作为例子，我们再次回到函数 **f**。稍作修改，将被引用的变量 `x` 从 auto 存储挪到 `__block` 存储：

```
void f(void) {
    __block int x = 0;
    int (^b)(void) = ^{ return x + 1; };
    int y = b();
}
```

作为响应，编译器将生成类似下面的代码（因添加 `__block` 而导致的变化已用高亮标出）：

```
   // __block int x
   struct __byref_x {
   /* header */
   void *isa;
   struct __byref_x *forwarding;
   int flags;
   int size;
   /* no helpers needed */
   int x;
   };

typedef void (*generic_invoke_funcptr)(void *, ...);
struct __block_literal {
    void *isa;
    int flags;
    int reserved;
    generic_invoke_funcptr invoke;
    struct __block_descriptor_tmp *descriptor;

    struct __byref_x *captured_x;

};

void __copy_helper_block_(struct __block_literal *dst,
                             struct __block_literal *src);
void __destroy_helper_block_(struct __block_literal *bp);

typedef void (*generic_copy_funcptr)(void *, void *);
typedef void (*generic_dispose_funcptr)(void *);
static const struct __block_descriptor_tmp {
    unsigned long reserved;
    unsigned long literal_size;

    /* helpers to copy __block reference captured_x */
    generic_copy_funcptr copy;
    generic_dispose_funcptr dispose;

} __block_descriptor_tmp = {
    0UL, sizeof(struct __block_literal),

   (generic_copy_funcptr)__copy_helper_block_,
   (generic_dispose_funcptr)__destroy_helper_block_
};

// ^int (void) { return x + 1; }
int __f_block_invoke_(struct __block_literal *bp) {
    return bp->captured_x->forwarding->x + 1;
}
typedef int (*iv_funcptr)(struct __block_literal *);

void f(void) {

    // __block int x = 0;
    struct __byref_x x = {
        .isa = NULL,
        .forwarding = &x,
        .flags = 0,
        .size = sizeof(x),
        .x = 0
    };

    // int (^b)(void) = ^{ return x + 1 };
    struct __block_literal __b = {
        .isa = &_NSConcreteStackBlock,
        .flags = BLOCK_HAS_DESCRIPTOR,
        .reserved = 0,
        .invoke = (generic_invoke_funcptr)__f_block_invoke_,
        .descriptor = &__block_descriptor_tmp,

        .captured_x = x.forwarding

    };
    struct __block_literal *b = &__b;
    int y = (*(iv_funcptr)(b->invoke))(b);

    // Clean up before leaving scope of x.
    _Block_object_dispose(x.forwarding, BLOCK_FIELD_IS_BYREF);
}

void __copy_helper_block_(struct __block_literal *dst,
                          struct __block_literal *src) {
  _Block_object_assign(&dst->captured_x, src->captured_x,
                       BLOCK_FIELD_IS_BYREF);
}

void __destroy_helper_block_(struct __block_literal *bp) {
  _Block_object_dispose(bp->captured_x, BLOCK_FIELD_IS_BYREF);
}
```

这里尤其值得注意的是 `f()` 末尾对 `_Block_object_dispose()` 的调用。这是因为，当未使用垃圾回收时，一旦 `__block` 变量离开作用域，运行时就必须调整其引用计数。当所有引用都被清除后，运行时便会释放已分配的内存。

辅助函数所使用的 `_Block_object_assign()` 和 `_Block_object_dispose()` 由 Block 运行时提供，供编译器使用。它们的行为在很大程度上取决于最后一个参数 `const int flags`，该参数提供了被分配或释放的对象的类型信息。该字段的可能取值如下：

```
enum {
    BLOCK_FIELD_IS_OBJECT   =  3,
    BLOCK_FIELD_IS_BLOCK    =  7,
    BLOCK_FIELD_IS_BYREF    =  8,
    BLOCK_FIELD_IS_WEAK     = 16,
    BLOCK_BYREF_CALLER      = 128
};
```

`BLOCK_BYREF_CALLER` 标志被用来向这些函数发出信号，表明它们正被某个 byref 结构体的 `byref_keep` 或 `byref_destroy` 函数调用。只有这类函数才会设置这个标志。

其他标志则根据被分配或释放的对象的类型按需设置。注意，Block 字段同样也是一个对象，因为 `BLOCK_FIELD_IS_BLOCK & BLOCK_FIELD_IS_OBJECT` 的结果正是 `BLOCK_FIELD_IS_OBJECT`。在需要区分普通对象与 Block 对象的情况下，运行时函数会谨慎地先检查 Block 标志是否设置，再检查对象标志是否设置。

### 调试

调试 Block 可能会很棘手，因为调试环境恰好夹在抽象和实现之间。**gcc** 提供的调试信息远优于 **clang**，但这一情况将来可能会改变。

**gdb** 只带有一个 Block 专用命令：**invoke-block**，你可以明确地将其缩写为 **inv**。它的参数是一个 Block 引用或 Block 字面量结构的地址，后跟该 Block 函数所声明的参数。参数之间以空格分隔，因此含有空格的参数必须用双引号引起。被引号引住的参数内部的双引号则必须用反斜杠转义。你唯一可能遇到这种情况的场景，是在向 Block 传递字符串参数时；所产生的命令看起来会是这样：

```
inv string_block "\"string argument\""
```

**gcc** 和 **clang** 在它们为 Block 提供的调试信息方面存在显著差异。

#### gcc 的调试信息

**gcc** 嵌入的关于 Block 的调试信息相当丰富。**print** 命令（简写为 **p**）能识别出 Block 引用是指针，你还可以用 **ptype** 打印出编译器为 Block 生成的类型：

```
(gdb) p local_block
$1 = (struct __block_literal_2 *) 0xbffff854
(gdb) ptype local_block
type = struct __block_literal_2 {
    void *__isa;
    int __flags;
    int __reserved;
    void *__FuncPtr;
    struct __block_descriptor_withcopydispose *__descriptor;
    const char *enc_vbv;
    struct __Block_byref_1_i *i;
} *
(gdb) ptype local_block->__descriptor
type = struct __block_descriptor_withcopydispose {
    long unsigned int reserved;
    long unsigned int Size;
    void *CopyFuncPtr;
    void *DestroyFuncPtr;
} *
```

你也可以使用 Objective-C 命令 **print-object**（简写为 **po**）来以另一种视角查看 Block：

```
(gdb) po local_block
<__NSStackBlock__: 0xbffff854>
```

在 Block 内部获取局部变量信息会显示 **gcc** 添加了 `__func__` 变量，该变量会被设置为函数名。如果你获取函数实参的信息，则会看到那个隐式的 Block 字面量指针参数：

```
(gdb) i args
.block_descriptor = (struct __block_literal_2 *) 0xbffff854
```

**gcc** 生成的调试信息会“假装”`__block` 变量与其对应的 auto 变量完全相同，因此，如果你有一个 `__block int i` 变量，会发现打印 `i` 及其大小与打印 `int i` 变量的行为一样。

#### clang 的调试信息

可惜的是，**clang** 不为 Block 引用提供任何调试信息。调试器找不到 Block 引用的类型信息，也没有办法去查找某个 Block 的 Block 实现函数，因此 `invoke-block` 总是会失败。

你仍然可以通过在文件的某一行设置断点，或者在调用函数（如果你能确定它的名字）处设置断点，来在 Block 内设置断点。但你会发现 **clang** 会假装 Block 实现函数拥有与 Block 字面量相同的参数，因此你无法轻易访问到隐式的 Block 字面量指针参数。有趣的是，**clang** 不会报告任何 `__func__` 局部变量；如果你在 Block 字面量里使用它，它会生成一条警告，但你会发现无论调试信息怎么说，该变量实际上确实存在。

**clang** 也不会为 `__block` 变量产生任何调试信息。它们既不会出现在局部变量列表中，而且任何引用它们的尝试都会导致类似下面的消息：

```
No symbol "i" in current context.
```

虽然你可以借助对 Block 实现的了解，从使用 **clang** 编译的程序里变着法子挖出所需信息，但在这些问题得到修复之前，只要你打算在将来依赖调试信息，最好还是使用 **gcc** 来编译使用了 Block 的应用。

### 转储运行时信息

Apple 的 Block 运行时包含几个函数，用于转储 Block 引用和 `__block` 变量的信息。

这些函数如下：

```
const char *_Block_dump(const void *block);
const char *_Block_byref_dump(struct Block_byref *src);
```

你可以在 **gdb** 中调用它们，以转储某个 Block 或 `__block` 变量的信息。假设你有如下声明：

```
__block int i = 23;
void (^local_block)(void) = ^{ /*...*/ };
```

则可以像下面这样转储它们的信息：

```
(gdb) call (void)printf((const char *)_Block_dump(local_block))
^0xbffff854 (new layout) =
isa: stack Block
flags: HASDESCRIPTOR HASHELP
refcount: 0
invoke: 0x1e50
descriptor: 0x20bc
descriptor->reserved: 0
descriptor->size: 28
descriptor->copy helper: 0x1e28
descriptor->dispose helper: 0x1e0a

(gdb) set $addr = (char *)&i - 2*sizeof(int) - 2*sizeof(void *)
(gdb) call (void)printf((const char *)_Block_byref_dump($addr))
byref data block 0xbffff870 contents:
  forwarding: 0xbffff870
  flags: 0x0
  size: 20
```

注意，虽然 **gcc** 提供的调试信息会假装 `__block` 变量 `i` 仅仅是一个 `int` 变量，但该变量的地址实际上正是它在 byref 结构体中内部的地址。既然我们知道该结构体的布局，就可以计算出结构体起始地址，并将其传给 `_Block_byref_dump()`。

你可以把这些调用包装成用户自定义的命令。将以下定义添加到你的 `.gdbinit` 文件中，则每次运行 **gdb** 时都可以直接使用它们：

```
define dump-block-literal
    printf "%s", (const char *)_Block_dump($arg0)
end

document dump-block-literal
    Dumps runtime information about the supplied block reference.
    Argument is the name or address of a block reference.
end

define dump-block-byref
    set $_dbb_addr = (char *)&$arg0 - 2*sizeof(int) - 2*sizeof(void *)
    printf "%s", (const char *)_Block_byref_dump($_dbb_addr)
end

document dump-block-byref
    Dumps runtime information about the supplied __block variable.
    Argument is a pointer to the variable embedded in a block byref structure.
end
```

定义好这些命令后，转储这些信息就变得非常简单：

```
(gdb) dump-block-literal local_block
^0xbffff854 (new layout) =
isa: stack Block
flags: HASDESCRIPTOR HASHELP
refcount: 0
invoke: 0x1e50
descriptor: 0x20bc
descriptor->reserved: 0
descriptor->size: 28
descriptor->copy helper: 0x1e28
descriptor->dispose helper: 0x1e0a
(gdb) dump-block-byref i
byref data block 0xbffff870 contents:
  forwarding: 0xbffff870
  flags: 0x0
  size: 20
```

### 实现的发展

本章描述的是随 Mac OS X 10.6（Snow Leopard）发布的 Block 运行时。Block 运行时不太可能做出会破坏遵循该接口编译的代码的更改，但它不会停止演进。

当前运行时中内置了若干扩展点。各 flags 字段可以谨慎地扩展；保留字段可被赋予新用途；新字段也可以追加到各种结构体的末尾。

一个可能发布的较小扩展，是在 Block 描述符结构体末尾增加一个签名字段。该字段将包含一个指向 Block 调用函数的 Objective-C 类型编码的指针。

（对于那些感到好奇的读者：Block 自身的 `@encode` 编码为 `@?`；这与函数指针的编码 `^?` 类似，后者的字面含义是“指向未知类型的指针”。）

为了表示该字段的存在，将不再设置 `BLOCK_HAS_DESCRIPTOR` 标志，而会为所有面向新运行时编译的 Block 设置一个新的标志 `BLOCK_HAS_SIGNATURE = (1 \<\< 30)`。

一旦有了通过测试 `BLOCK_HAS_SIGNATURE` 来检查某个 Block 是否针对较新版本运行时编译的能力，就为其他变更打开了大门，包括将 `BLOCK_HAS_DESCRIPTOR` 改为用于指示 Block 返回的结构体大到在某些架构上需要特殊处理。这个标志可以重命名为 `BLOCK_USE_STRET`。这与 Objective-C 运行时在相同情况下使用 `objc_msgSend_stret()` 而非 `objc_msgSend()` 的做法很相似。

一个更为重大的变化，是增加 Block 所捕获变量的签名。这将使运行时能够淘汰辅助函数，转而利用现在与 Block 一同编码的类型信息，在 Block 被复制或释放时自行对所有捕获的变量执行正确的操作。

### 编译器生成的名称

**gcc** 与 **clang** 都会自动为构成 Block 与 `__block` 变量的结构体和函数生成名称。在调试过程中，有时如果能猜出实现某个 Block 或 `__block` 变量时所生成的名称，会非常有用。

遗憾的是，除了那些玩具般的例子之外，如果不参考代码的反汇编，这通常是不可能的。两个编译器都会在自己生成的同一字符串末尾追加数字来消歧结构体和辅助函数的名称。因此，你虽然能判断出自己看到的是哪种支持结构或辅助函数，却很难回溯到导致它生成的那个 Block 或 `__block` 变量。

幸运的是，在 Block 调用函数方面，前景并没有那么悲观。未在全局作用域定义的 Block 调用函数会嵌入它最外层的封闭函数名称。对于函数 `f()` 中的第一个 Block，如果由 **gcc** 生成，它将被命名为 `__f_block_invoke_1`；如果由 **clang** 生成，则名为 `__f_block_invoke_`。在生成该函数内后续遇到的每个 Block 调用函数名称时，数字后缀都会递增。（**clang** 会从追加数字 `1` 开始，之后与 **gcc** 一样递增。）Objective-C 方法名会像 C 函数名一样被嵌入，由此产生诸如 `__-[Foo init]_block_invoke_1` 这样的 Block 调用函数名称。C++ 成员函数在嵌入时既不会被限定，也不会经过名字修饰（mangling），因此在成员函数 `Foo::Bar()` 内定义的 Block 会让编译器生成名为 `__Bar_block_invoke_` 的 Block 调用函数（如果编译器是 **gcc**，则追加 `1`）。

在全局作用域定义的 Block，其调用函数更难追踪，因为它们没有可供锚定的封闭函数。**gcc** 以 `__block_global_1` 作为这类函数的开头命名。**clang** 则采用与在函数内部定义的 Block 相同的命名方案，只是用 `global` 替代函数名。因此，**clang** 遇到的一个在全局作用域定义的 Block 会被命名为 `__global_block_invoke_`，第二个则为 `__global_block_invoke_1`。

全局作用域的 Block 的命名惯例带来的一个令人惊讶的结果是：当多个源文件被编译进同一个可执行文件时，每个文件都可以拥有自己的 `__global_block_invoke_` 函数。生成的可执行文件中，将会有多个拥有完全相同名称的函数，它们仅仅靠位于不同的地址来区分。

在任何可能的时候，都请用文件和行号而不是名称来在 Block 函数内指定断点。名称生成方案将来可能会变化，而且它也并不保证在链接出的可执行文件中的唯一性，仅能保证在单个编译单元内的唯一性。

- [🔖 保存到你的账户](#addToWishList)
