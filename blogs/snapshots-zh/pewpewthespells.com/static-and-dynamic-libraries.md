---
title: 静态库与动态库
source_url: 'https://pewpewthespells.com/blog/static_and_dynamic_libraries.html'
source_domain: pewpewthespells.com
source_group: single-site
original_language: en
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:03866a4de26d6a00'
plan_ref: 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 3｜静态/动态不是文件后缀问答（对应 W1-09）
plan_week: 第七周：编译、链接、Mach-O、dyld 与 App 启动
plan_day: Day 3｜静态/动态不是文件后缀问答（对应 W1-09）
container: //body
container_source: map
translated: true
---

> 原文：[Static and Dynamic Libraries](https://pewpewthespells.com/blog/static_and_dynamic_libraries.html)

# 静态库与动态库

### 链接库

库的链接是一种代码依赖管理的形式。当任何 App 运行时，其可执行代码会被加载到内存中。此外，它所依赖的任何代码库也会被加载到内存中。链接有两种类型：静态链接和动态链接。两者为开发者提供不同的优势，应依据这些优势来选择使用。这篇博文会介绍各自提供的优势，然后解释在 OS X 和 iOS 上创建和链接你自己的库的基础知识。

---

### 动态链接

动态链接在 OS X 和 iOS 上最为常用。链接动态库时，库的代码不会被直接包含到链接目标中。相反，这些库会在运行时、符号被解析之前被加载到内存中。由于代码没有被静态链接到可执行二进制文件中，因此在运行时加载带来了一些好处。主要是，库可以在不重新编译和重新链接可执行文件的情况下，通过新功能或 bug 修复进行更新。此外，在运行时加载意味着各个代码库可以在被从内存中卸载前，拥有自己的初始化方法，并在其自己的任务完成后进行清理。关于概述和设计的更多信息，请参阅 Apple 的[动态库编程主题](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/OverviewOfDynamicLibraries.html)。

#### • 库

动态库是一种 Mach-O 二进制[^1](#fn1)类型，它在 App 启动或运行时被加载。由于动态库中的可执行代码没有被静态链接到目标可执行文件中，因此在需要重用相同代码时带来了一些好处。例如，如果你有一个 App 以及一个 daemon 或扩展需要用到相同的代码，那么该代码只需存在于一个位置——即动态库中，而不是同时存在于可执行文件的二进制文件和 daemon 的二进制文件中。由于动态库在运行时被加载，库负责告诉链接器还需要哪些额外代码，从而免去了你手动追踪这些依赖的负担。

#### • 框架

动态框架与动态库类似。两者都是可动态链接的库，区别在于动态框架是嵌入在 bundle 中的动态库。这允许动态库进行版本管理，并整理库代码所使用的附加资源。

#### • 构建

以下是构建 `libfoo_dynamic.dylib` 所需的步骤演练。

bar.h

```
#ifndef __foo__bar__
#define __foo__bar__

#include <stdio.h>

int fizz();

#endif /* defined(__foo__bar__) */
```

bar.c

```
#include "bar.h"
#include <CoreFoundation/CoreFoundation.h>

int fizz() {
    CFShow(CFSTR("buzz"));

    return 0;
}
```

从文件 `bar.h` 和 `bar.c` 开始。头文件定义了函数 `fizz()`，它返回一个整数值。实现文件导入了 CoreFoundation 框架，并实现了函数 `fizz`，用于在返回 `0` 之前打印字符串 "buzz"。

**编译：**

```
$ clang -c bar.c -o bar.o
```

这会创建目标文件（object file）[^2](#fn2)，即类型为 `MH_OBJECT` 的 Mach-O 二进制文件，名为 "bar"。库中编译的每个文件都会生成一个这样的文件。

**创建库：**

```
$ libtool -dynamic bar.o -o libfoo_dynamic.dylib -framework CoreFoundation -lSystem
```

这会创建 dylib（动态库），并链接到 `libSystem` 和 `CoreFoundation.framework`。dylib 是一个类型为 `MH_DYLIB` 的 Mach-O 二进制文件。它会在启动时被 dyld 作为另一个二进制的依赖项动态加载。

#### • 链接

main.c

```
#include "bar.h"

int main() {
    return fizz();
}
```

在这个例子中，导入了动态库的 "bar.h" 头文件，并直接调用 `fizz()`。

**编译：**

```
$ clang -c main.c -o main.o
```

这将会生成 main 的目标文件。

**链接：**

```
$ ld main.o -lSystem -L. -lfoo_dynamic -o test_dynamic
```

这会从 main 的目标文件生成一个二进制可执行文件，同时传递：

- `-lSystem` 用于 `dyld_stub_binder`
- `-lfoo_dynamic` 用于链接到 `libfoo_dynamic.dylib`

最后，输出一个名为 `test_dynamic` 的二进制文件。

**运行：**

```
$ ./test_dynamic
buzz
```

**符号：**

```
$ nm test_dynamic
0000000000001000 A __mh_execute_header
                 U _fizz
0000000000001fa0 T _main
                 U dyld_stub_binder
```

这会列出主二进制文件中的所有符号。这里列出了 `main` 和 `fizz` 两个符号。符号 `fizz` 没有地址，因为它不存在于主二进制文件中，而是存在于所创建的动态库中。这个符号会在启动时，在所有被引用的依赖项被加载到内存后被解析。

**引用：**

```
$ otool -L test_dynamic
test_dynamic:
    /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1197.1.1)
    libfoo_dynamic.dylib (compatibility version 0.0.0, current version 0.0.0)
```

生成的二进制文件只链接了 libSystem 和所创建的 dylib。`foo_dynamic` 库负责链接它所需的任何额外库。这会在启动时动态解析。在这种情况下，`libfoo_dynamic.dylib` 的搜索路径将与主可执行文件的搜索位置相同。

动态库和框架由动态链接器在启动时加载。它们有相关的搜索路径，以帮助链接器找到它们在文件系统中的位置并加载。

---

### 静态链接

与动态链接不同，链接静态库会将库中的目标文件代码包含到目标的二进制文件中。这会导致磁盘占用更大以及启动时间更慢。由于库的代码被直接添加到链接目标的二进制文件中，这意味着要更新库中的任何代码，链接目标也必须重新构建。

在 iOS 8 之前，静态链接库是在 App 中分发和包含任何第三方代码的事实标准。

注意：不要将其与[静态链接二进制文件](https://developer.apple.com/library/mac/qa/qa1118/_index.html)混淆。

#### • 库

静态库是目标文件的容器。静态库使用文件扩展名 ".a"，这来源于（ar）chive 文件[^3](#fn3)类型。归档文件被设计用于包含一组文件。这对于传输和使用组成单个代码库的多个目标文件来说是理想的。然而，链接器只能使用单一架构的目标文件，因此有两种不同的容器格式用于静态库，取决于它们是否支持单一架构还是多架构。

所有相同架构的目标文件都存储在一个单独的归档文件中。这是链接器期望的每种架构的容器文件类型。目标文件由 [ar](x-man-page://1/ar) 工具打包，该工具存储每个目标文件的内容。OS X 使用类似于 BSD 变体的 `ar` 实现；将符号查找和表创建的任务组织给一个名为 `ranlib` 的工具。在 OS X 上，这是 [libtool](x-man-page://1/libtool) 的别名。这个工具负责映射存储在目标文件中的符号，如果使用了不匹配的架构，它会发出警告。这会生成一个归档文件，可以使用 `ar` 工具进行检查和操作。

由于单个归档文件只能支持一种架构，因此使用另一种文件格式作为包含多个库的单个容器。为此选择的文件格式是 fat Mach-O 二进制文件。由于文件类型的变化，`ar` 不能再对静态库进行操作。fat Mach-O 二进制文件是一种非常简单的容器格式，可以容纳多个不同架构的文件。

```
// 这位于文件的最开头
struct fat_header {
    uint32_t magic;     // This indicates the endianness of the binary file
    uint32_t nfat_arch; // This indicates how many architecture headers are defined for the file
};

// 这是架构头的定义，这些定义紧跟在 'fat_header' 之后
struct fat_arch {
    cpu_type_t cputype;         // This defines the CPU family type: "Intel", "ARM", "PPC"
    cpu_subtype_t cpusubtype;   // This defines the CPU variant for the family type: "i386", "x86_64", "armv7", "armv7s", "ppc64"
    uint32_t offset;            // Offset in the file where the architecture specific data starts
    uint32_t size;              // Length of the architecture specific data in the file
    uint32_t align;             // Power of 2 alignment data for the architecture type
};
```

虽然这是一种 Mach-O 二进制文件类型，但它严格充当多架构的安全容器。这种格式用于为每个所需的架构类型存储一份库的副本。要修改使用 fat Mach-O 二进制文件类型的静态库，必须使用命令 [lipo](x-man-page://1/lipo)。它还可以根据特定架构提取静态库的副本。

#### • 框架

静态框架是包含一个静态库文件的 bundle。这些框架只是发布使用外部资源（如图片、字体或语言文件）的静态库的一种便捷方式。此外，静态框架的行为与静态库完全相同。它们是静态链接到可执行二进制文件中的，而不是在运行时加载。

#### • 构建

以下是构建 `libfoo_static.a` 的演练。这使用了与动态库示例中相同的文件。

bar.h

```
#ifndef __foo__bar__
#define __foo__bar__

#include <stdio.h>

int fizz();

#endif /* defined(__foo__bar__) */
```

bar.c

```
#include "bar.h"
#include <CoreFoundation/CoreFoundation.h>

int fizz() {
    CFShow(CFSTR("buzz"));

    return 0;
}
```

**编译：**

```
$ clang -c bar.c -o bar.o
```

这会创建名为 "bar" 的目标文件。同样，库中编译的每个文件都会生成一个这样的文件。

**创建库：**

```
$ ar -rcs libfoo_static.a bar.o
or
$ libtool -static bar.o -o libfoo_static.a
```

与动态库不同，创建静态库时，没有其他库会链接到它。这是因为（ar）chive 文件只是需要构建的目标文件的容器。通过对编译器生成的一组目标文件运行 `ar` 或 `libtool`，它们会被打包成一个可以包含多组架构和符号定义的归档。

直接运行 `ar` 将生成一个仅包含被传递的目标文件的归档文件。然后它会调用 `ranlib` 对这个创建的归档文件进行排序，并解析包含在归档中的任何重复符号名。改用 `libtool` 会产生相同的行为和输出，其代码路径略有不同，它会调用 `libstuff` 而不是 `ar` 工具。

由于这不是一个可执行二进制文件，静态库不会保留它们可能需要的任何链接关系。这将对依赖项进行追踪的负担推给了链接目标可执行文件，而不是静态库本身。幸运的是，Apple 实现了一个用于处理此问题的加载命令，`LC_LINKER_OPTION`。这在 Xcode 中的目标构建设置中以 "Link Frameworks Automatically" 名称出现。启用此选项会将新的加载命令附加到每个目标文件中，这些加载命令指定了应与每个目标文件一起使用的链接器标志。可以使用以下命令显示这些标志：

`$ otool -l <static library>  | grep LC_LINKER_OPTION -A 4`

#### • 链接

main.c

```
#include "bar.h"

int main() {
    return fizz();
}
```

在这个例子中，导入了静态库的 "bar.h" 头文件，并直接调用 `fizz()`。

**编译：**

```
$ clang -c main.c -o main.o
```

这将会生成 main 的目标文件。

**链接：**

```
$ ld main.o -framework CoreFoundation -lSystem -L. -lfoo_static -o test_static
```

这会从 main 的目标文件生成一个二进制可执行文件，同时传递：

- `-lSystem` 用于 `dyld_stub_binder`
- `-framework CoreFoundation` 用于链接 `CoreFoundation.framework`
- `-lfoo_static` 用于链接 `libfoo_static.a`

最后，输出一个名为 `test_static` 的二进制文件。

**运行：**

```
$ ./test_static
buzz
```

**符号：**

```
$ nm test_static
                 U _CFShow
                 U ___CFConstantStringClassReference
0000000000001000 A __mh_execute_header
0000000000001f90 T _fizz
0000000000001f70 T _main
                 U dyld_stub_binder
```

这里我们看到，符号 `fizz`（它曾是静态库的一部分）现在有一个关联的地址。这是因为与调用函数 `fizz()` 相关的可执行代码现在存储在主二进制可执行文件内部。此外，还有对 `CFShow` 和 `CFConstantStringClassReference` 的引用，它们作为 CoreFoundation 框架的一部分存在。

**引用：**

```
$ otool -L test_static
test_static:
    /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 855.17.0)
    /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1197.1.1)
```

通过 otool 检查链接库列表时，主二进制文件只链接了 libSystem。这是因为 `libfoo_static` 中的符号已经被添加到主二进制文件中。由于 `libfoo_static` 的代码依赖于链接 CoreFoundation，因此主二进制文件中会有一个对该依赖的引用。

---

### 进一步阅读

- [Overview of Dynamic Libraries](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/OverviewOfDynamicLibraries.html)
- [Dynamic Library Programming Topics](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html)
- [Mach-O Programming Topics](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/MachOTopics/0-Introduction/introduction.html)
- [Mach-O File Format ABI](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/MachORuntime/index.html)
- [Object File](http://en.wikipedia.org/wiki/Object_file)
- [UNIX (ar)chive](http://en.wikipedia.org/wiki/Ar_(Unix))
- [OS X ABI Dynamic Loader Reference](https://developer.apple.com/library/mac/documentation/DeveloperTools/Reference/MachOReference/index.html)
- [cctools source code](http://opensource.apple.com/source/cctools/)

---

如果这篇博文对你有所帮助，请考虑捐赠以维持此博客的运行，谢谢！

[![捐赠以支持此博客](https://pewpewthespells.com/media/donate_button.gif)](https://cash.me/$samanthademi)

---

1. 参见“进一步阅读”中的“Mach-O Programming Topics” [↩](#fnref1)
2. 参见“进一步阅读”中的“Object File” [↩](#fnref2)
3. 参见“进一步阅读”中的“UNIX (ar)chive” [↩](#fnref3)
