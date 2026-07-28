---
title: 解析 Mach-O 文件 - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/parsing-mach-o-files/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4d46a62158b33d08'
translated: true
---

> 原文：[Parsing Mach-O files - Low Level Bits 🇺🇦](https://lowlevelbits.org/parsing-mach-o-files/)　·　Low Level Bits (Alex Denisov)

# 解析 Mach-O 文件

_发表于 2015 年 8 月 20 日_

本文介绍如何解析 Mach-O 文件，并对其格式进行一些简单说明。它并非权威指南，但如果你不知从何入手，或许会有所帮助。更多信息请参考官方文档以及操作系统提供的头文件。

## 什么是 Mach-O 文件

摘自 [维基百科](https://en.wikipedia.org/wiki/Mach-O) 的简要描述：

> Mach-O，即 Mach 对象文件格式（Mach object file format）的缩写，是一种用于可执行文件、目标代码、共享库、动态加载代码和核心转储（core dump）的文件格式。作为 a.out 格式的替代，Mach-O 提供了更强的可扩展性，并能更快地访问符号表中的信息。
>
> 大多数基于 Mach 内核的系统都使用 Mach-O 格式。NeXTSTEP、OS X 和 iOS 就是在其原生可执行文件、库和目标代码中使用该格式的典型例子。

## Mach-O 格式

Mach-O 并没有 XML/YAML/JSON 等特殊格式，它只是一个由字节组成的二进制流，这些字节按有意义的块（chunk）进行分组。这些块包含元信息，例如：字节顺序、CPU 类型、块的大小等。

典型的 Mach-O 文件（[官方文档的副本（现已移除）](https://github.com/aidansteele/osx-abi-macho-file-format-reference)）由三个区域组成：

1.  头部（Header）——包含二进制文件的一般信息：字节顺序（魔数（magic number））、CPU 类型、加载命令（load command）数量等。
2.  加载命令（Load Commands）——类似于目录（table of contents），描述了段（segment）、符号表、动态符号表等的位置。每个加载命令都包含元信息，例如命令类型、名称、在二进制文件中的位置等。
3.  数据（Data）——通常是目标文件中最大的部分。它包含代码和数据，例如符号表、动态符号表等。

以下是简化的图形表示：

![](https://lowlevelbits.org/img/parse-mach-o-files/macho_header.png)

OS X 上有两种类型的目标文件：Mach-O 文件和通用二进制文件（Universal Binary），也称为胖文件（Fat file）。它们的区别在于：Mach-O 文件包含单一架构（i386、x86_64、arm64 等）的目标代码，而胖二进制文件可能包含多个目标文件，因此包含了不同架构（i386 和 x86_64、arm 和 arm64 等）的目标代码。

胖文件的结构非常简单：胖头部后紧跟 Mach-O 文件：

![](https://lowlevelbits.org/img/parse-mach-o-files/fat_header.png)

## 解析 Mach-O 文件

OS X 并没有提供类似 `libmacho` 的库，我们唯一拥有的是在 `/usr/include/mach-o/*` 下定义的一组 C 结构体，因此需要自己实现解析。这可能有些棘手，但并非特别困难。

### 内存表示

在开始解析之前，我们先看一下 Mach-O 文件的详细表示。为简化起见，以下目标文件是一个仅包含两个数据条目（均为段）的 Mach-O 文件（非胖文件），架构为 i386。

![](https://lowlevelbits.org/img/parse-mach-o-files/sample_macho.png)

表示该文件所需的唯二结构体：

```c
struct mach_header {
  uint32_t      magic;
  cpu_type_t    cputype;
  cpu_subtype_t cpusubtype;
  uint32_t      filetype;
  uint32_t      ncmds;
  uint32_t      sizeofcmds;
  uint32_t      flags;
};

struct segment_command {
  uint32_t  cmd;
  uint32_t  cmdsize;
  char      segname[16];
  uint32_t  vmaddr;
  uint32_t  vmsize;
  uint32_t  fileoff;
  uint32_t  filesize;
  vm_prot_t maxprot;
  vm_prot_t initprot;
  uint32_t  nsects;
  uint32_t  flags;
};
```

内存映射如下图所示：

![](https://lowlevelbits.org/img/parse-mach-o-files/macho_memory_layout.png)

如果你想要从文件中读取特定信息，只需要正确的数据结构和一个偏移量（offset）即可。

### 解析

我们来编写一个程序，它能读取 Mach-O 或胖文件，并打印每个段的名称以及它所构建的架构。

最终的效果大致如下：

```bash
$ ./segname_dumper some_binary
i386
segname __PAGEZERO
segname __TEXT
segname __LINKEDIT
```

#### 驱动（Driver）

我们从一个简单的“驱动”开始。

解析此类文件至少有两种可能的方式：将内容加载到内存中并直接处理缓冲区，或者打开文件并在其中前后跳转。两种方法各有优缺点，但我将采用第二种方法。此外，我假设没有人会以错误的方式使用该程序，因此不做任何错误处理。

```c
#include <stdio.h>
#include <stdlib.h>
#include <mach-o/loader.h>
#include <mach-o/swap.h>

void dump_segments(FILE *obj_file);

int main(int argc, char *argv[]) {
  const char *filename = argv[1];
  FILE *obj_file = fopen(filename, "rb");
  dump_segments(obj_file);
  fclose(obj_file);

  return 0;
}

void dump_segments(FILE *obj_file) {
  // 驱动
}
```

#### 魔数、CPU 与字节序

为了至少读取目标文件的头部，我们需要获取所有必要信息：CPU 架构（32 位或 64 位）和字节序。但首先需要获取魔数：

```c
uint32_t read_magic(FILE *obj_file, int offset) {
  uint32_t magic;
  fseek(obj_file, offset, SEEK_SET);
  fread(&magic, sizeof(uint32_t), 1, obj_file);
  return magic;
}

void dump_segments(FILE *obj_file) {
  uint32_t magic = read_magic(obj_file, 0);
}
```

函数 `read_magic` 相当直接，但有一处可能看起来有点奇怪：`fseek`。问题是，每当有人从文件读取数据时，文件的内部 `_offset` 就会改变。最好显式指定偏移量，以确保我们读到了实际想要读取的内容。另外，这个小技巧在后续也会派上用场。

表示 32 位和 64 位目标文件的结构体是不同的（例如：`mach_header` 和 `mach_header_64`），因此我们需要检查文件的架构来决定使用哪一个：

```c
int is_magic_64(uint32_t magic) {
  return magic == MH_MAGIC_64 || magic == MH_CIGAM_64;
}

void dump_segments(FILE *obj_file) {
  uint32_t magic = read_magic(obj_file, 0);
  int is_64 = is_magic_64(magic);
}
```

`MH_MAGIC_64` 和 `MH_CIGAM_64` 是系统提供的“魔数”。第二个看起来比第一个更神秘。解释如下。

由于历史原因，不同的计算机可能使用不同的[字节序](https://en.wikipedia.org/wiki/Endianness)：大端序（Big Endian，从左到右）和小端序（Little Endian，从右到左）。魔数也存储了此信息：`MH_CIGAM` 和 `MH_CIGAM_64` 表示字节序与主机操作系统不同，因此所有字节都需要交换：

```c
int should_swap_bytes(uint32_t magic) {
  return magic == MH_CIGAM || magic == MH_CIGAM_64;
}

void dump_segments(FILE *obj_file) {
  uint32_t magic = read_magic(obj_file, 0);
  int is_64 = is_magic_64(magic);
  int is_swap = should_swap_bytes(magic);
}
```

#### Mach-O 头部

终于可以读取 `mach_header` 了。首先引入一个通用的文件数据读取函数。

```c
void *load_bytes(FILE *obj_file, int offset, int size) {
  void *buf = calloc(1, size);
  fseek(obj_file, offset, SEEK_SET);
  fread(buf, size, 1, obj_file);
  return buf;
}
```

**注意：使用后需要释放（free）数据！**

```c
void dump_mach_header(FILE *obj_file, int offset, int is_64, int is_swap) {
  if (is_64) {
    int header_size = sizeof(struct mach_header_64);
    struct mach_header_64 *header = load_bytes(obj_file, offset, header_size);
    if (is_swap) {
      swap_mach_header_64(header, 0);
    }

    free(header);
  } else {
    int header_size = sizeof(struct mach_header);
    struct mach_header *header = load_bytes(obj_file, offset, header_size);
    if (is_swap) {
      swap_mach_header(header, 0);
    }

    free(header);
  }
  free(buffer);
}

void dump_segments(FILE *obj_file) {
  uint32_t magic = read_magic(obj_file, 0);
  int is_64 = is_magic_64(magic);
  int is_swap = should_swap_bytes(magic);
  dump_mach_header(obj_file, 0, is_64, is_swap);
}
```

这里我们引入了另一个函数 `dump_mach_header`，以免搞乱“驱动”函数。下一步是读取所有段命令并打印它们的名称。问题在于 Mach-O 文件通常还包含其他命令。如果你还记得，`segment_command` 结构体的第一个字段是 `uint32_t cmd;`，它表示命令的类型。下面是系统提供的另一个我们将用到的结构体：

```c
struct load_command {
  uint32_t cmd;
  uint32_t cmdsize;
};
```

除了所有信息之外，`mach_header` 还包含了加载命令的数量，因此我们可以进行迭代并跳过不感兴趣的命令。此外，我们需要计算头部结束的偏移量。以下是 `dump_mach_header` 的最终版本：

```c
void dump_mach_header(FILE *obj_file, int offset, int is_64, int is_swap) {
  uint32_t ncmds;
  int load_commands_offset = offset;

  if (is_64) {
    int header_size = sizeof(struct mach_header_64);
    struct mach_header_64 *header = load_bytes(obj_file, offset, header_size);
    if (is_swap) {
      swap_mach_header_64(header, 0);
    }
    ncmds = header->ncmds;
    load_commands_offset += header_size;

    free(header);
  } else {
    int header_size = sizeof(struct mach_header);
    struct mach_header *header = load_bytes(obj_file, offset, header_size);
    if (is_swap) {
      swap_mach_header(header, 0);
    }

    ncmds = header->ncmds;
    load_commands_offset += header_size;

    free(header);
  }

  dump_segment_commands(obj_file, load_commands_offset, is_swap, ncmds);
}
```

#### 段命令（Segment Command）

是时候转存所有段名称了：

```c
void dump_segment_commands(FILE *obj_file, int offset, int is_swap, uint32_t ncmds) {
  int actual_offset = offset;
  for (int  i = 0; i < ncmds; i++) {
    struct load_command *cmd = load_bytes(obj_file, actual_offset, sizeof(struct load_command));
    if (is_swap) {
      swap_load_command(cmd, 0);
    }

    if (cmd->cmd == LC_SEGMENT_64) {
      struct segment_command_64 *segment = load_bytes(obj_file, actual_offset, sizeof(struct segment_command_64));
      if (is_swap) {
        swap_segment_command_64(segment, 0);
      }

      printf("segname: %s\n", segment->segname);

      free(segment);
    } else if (cmd->cmd == LC_SEGMENT) {
      struct segment_command *segment = load_bytes(obj_file, actual_offset, sizeof(struct segment_command));
      if (is_swap) {
        swap_segment_command(segment, 0);
      }

      printf("segname: %s\n", segment->segname);

      free(segment);
    }

    actual_offset += cmd->cmdsize;

    free(cmd);
  }
}
```

此函数不需要 `is_64` 参数，因为我们可以从 `cmd` 类型本身（`LC_SEGMENT`/`LC_SEGMENT_64`）推断出来。如果它不是段，则跳过该命令并前进到下一个。

#### CPU 名称

最后我想展示的是如何根据 `mach_header` 中的 `cputype` 检索处理器名称。我认为这不是最好的方法，但对于这个人为示例来说是可以接受的：

```c
struct _cpu_type_names {
  cpu_type_t cputype;
  const char *cpu_name;
};

static struct _cpu_type_names cpu_type_names[] = {
  { CPU_TYPE_I386, "i386" },
  { CPU_TYPE_X86_64, "x86_64" },
  { CPU_TYPE_ARM, "arm" },
  { CPU_TYPE_ARM64, "arm64" }
};

static const char *cpu_type_name(cpu_type_t cpu_type) {
  static int cpu_type_names_size = sizeof(cpu_type_names) / sizeof(struct _cpu_type_names);
  for (int i = 0; i < cpu_type_names_size; i++ ) {
    if (cpu_type == cpu_type_names[i].cputype) {
      return cpu_type_names[i].cpu_name;
    }
  }

  return "unknown";
}
```

OS X 为许多 CPU 提供了 `CPU_TYPE_*`，因此我们可以“轻松”地将特定魔数与字符串字面量关联起来。为了打印 CPU 名称，我们需要稍微修改 `dump_mach_header`：

```c
int header_size = sizeof(struct mach_header_64);
struct mach_header_64 *header = load_bytes(obj_file, offset, header_size);
if (is_swap) {
  swap_mach_header_64(header, 0);
}
ncmds = header->ncmds;
load_commands_offset += header_size;

printf("%s\n", cpu_type_name(header->cputype)); // <-

free(header);
```

#### 胖对象（Fat objects）

这篇文章已经相当长了，所以我不打算描述如何处理胖对象，但你可以在以下位置找到实现：[segment_dumper](https://github.com/AlexDenisov/segment_dumper)

## 下一步

基本就这些了。

如果你想深入研究并了解更多关于 Mach-O 的知识，以下是一些可能有用的链接：

- [OS X ABI Mach-O File Format Reference](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/MachORuntime/index.html) - Apple 的官方文档
- [MachOView](http://sourceforge.net/projects/machoview/) - 一个可视化 Mach-O 文件浏览器。它提供了探索和原地编辑 Intel 及 ARM 二进制文件的完整解决方案。
- [Mach-O Executables](http://www.objc.io/issues/6-build-tools/mach-o-executables/) - 来自 [objc.io](http://www.objc.io) 的优秀文章。
- [bitcode_retriever](https://github.com/AlexDenisov/bitcode_retriever) - 一个从 Mach-O 二进制文件中检索 [Bitcode](http://llvm.org/docs/BitCodeFormat.html) 的简单 C 程序。
- [segment_dumper](https://github.com/AlexDenisov/segment_dumper) - 本文的源代码。

**祝编码愉快！**

**P.S.** 这是下一篇文章的补充资料，将介绍 Apple 的“新” [Bitcode 功能](https://developer.apple.com/library/prerelease/ios/documentation/IDEs/Conceptual/AppDistributionGuide/AppThinning/AppThinning.html#//apple_ref/doc/uid/TP40012582-CH35-SW2)。
