---
title: 'Emerge Tools 博客 | 符号化 SwiftUI（及任意 Apple 框架），第一部分'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:e444d91658734f6b'
translated: true
---

> 原文：[Emerge Tools Blog | Symbolicating SwiftUI (and any Apple Framework), Part 1](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework)　·　Emerge Tools Blog

# 符号化 SwiftUI（及任意 Apple 框架），第一部分

2023 年 9 月 7 日，作者

[Itay Brenner](https://twitter.com/itaybre)

iOS 精选 开源

![符号化 SwiftUI（及任意 Apple 框架），第一部分](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner.00234c1e.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

📚️

本文是两篇系列文章的第一部分。如果你对如何使用 SwiftUI 符号感兴趣，请阅读[第二部分](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2)。

你是否注意到崩溃日志有时意义不大或缺少某些符号？与传统的 UIKit 应用不同，Apple 没有为 SwiftUI 提供调试符号（dSYM）。这意味着任何在堆栈跟踪中包含 SwiftUI 地址的崩溃将无法被符号化。

我们发现了一种**符号化任意 Apple 框架**的方法，并希望与大家分享。

## [问题所在](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework#the-problem)

当你使用 Sentry、Crashlytics 或 Bugsnag 等崩溃报告工具时，你通常会为每个发布版本上传项目的调试符号（dSYM）。这些 dSYM 使得这些工具能够将崩溃报告中的内存地址符号化为人类可读的格式。

Apple 为大多数系统框架（如 UIKit、AVFoundation 等）提供了符号，但其他框架如 SwiftUI、Combine 和 Metal Performance Shaders Graph 是例外——没有提供符号。依赖这些符号的工具在面临这种情况时，要么不显示任何内容，要么只显示内存地址这样的无用信息。这会使你在阅读崩溃报告或 Instruments 跟踪时更难以理解发生了什么。

![Bugsnag 示例崩溃](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog17%2F5.png&w=3840&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Bugsnag 示例崩溃

![Firebase 示例崩溃](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog17%2F6.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Firebase 示例崩溃

## [为什么 SwiftUI 不像其他框架](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework#why-swiftui-isnt-like-other-frameworks)

原因在于已发布的操作系统中的 SwiftUI 二进制文件没有符号名称。如果我们提取它（从 IPSW 或 iOS DeviceSupport 文件夹：`~/Library/Developer/Xcode/iOS DeviceSupport`），可以确认这种情况。

使用 `symbols` 命令，我们可以按格式打印二进制符号：`address (size) symbol-name [FLAGS]`。以下是 Foundation 框架的示例：

```basic
Foundation [arm64e, 0.016873 seconds]:
  6E76DC96-11AF-3B2E-B71E-215F9CC6E822 Foundation [DYLIB, DYLDSHAREDCACHE, FaultedFromDisk, MMap64]  
      0x00000001812e5000 (0x8de000) __TEXT SEGMENT
          0x00000001812e5000 (  0x27d0) MACH_HEADER
          0x00000001812e77d0 (0x5f1684) __TEXT __text
              0x00000001812e77d0 (    0xc8) -[NSComparisonPredicate predicateFormat] [FUNC, OBJC, NameNList, MangledNameNList, Merged, NList, FunctionStarts] 
              0x00000001812e7898 (    0x28) -[NSComparisonPredicate comparisonPredicateModifier] [FUNC, OBJC, NameNList, MangledNameNList, Merged, NList, FunctionStarts] 
              0x00000001812e78c0 (    0x8c) -[NSCompoundPredicate acceptVisitor:flags:] [FUNC, OBJC, NameNList, MangledNameNList, Merged, NList, FunctionStarts] 
              0x00000001812e794c (    0xfc) -[NSCompoundPredicate _acceptSubpredicates:flags:] [FUNC, OBJC, NameNList, MangledNameNList, Merged, NList, FunctionStarts] 
              0x00000001812e7a48 (    0xc0) -[NSComparisonPredicate acceptVisitor:flags:] [FUNC, OBJC, NameNList, MangledNameNList, Merged, NList, FunctionStarts] 
              0x00000001812e7b08 (    0x60) -[NSComparisonPredicate _acceptExpressions:flags:] [FUNC, OBJC, NameNList, MangledNameNList, Merged, NList, FunctionStarts] 
              0x00000001812e7b68 (   0x13c) -[NSFunctionExpression acceptVisitor:flags:] [FUNC, OBJC, NameNList, MangledNameNList, Merged, NList, FunctionStarts]
              ...
```

symbols Foundation -arch arm64e -filterSegment "__TEXT"

但对于 `SwiftUI`，大多数符号的 `symbol-name` 为 null：

```basic
SwiftUI [arm64e, 0.011490 seconds]:
  E76F182B-D965-3F8C-8D31-7C963B676EEB SwiftUI [DYLIB, DYLDSHAREDCACHE, FaultedFromDisk, MMap64]  
      0x000000018a8bf000 (0x1976000) __TEXT SEGMENT
          0x000000018a8bf000 (  0x2a68) MACH_HEADER
          0x000000018a8c1a68 (0x15f41d0) __TEXT __text
              0x000000018a8c1a68 (    0x4c) (null) [FUNC, FunctionStarts] 
              0x000000018a8c1ab4 (    0x4c) (null) [FUNC, FunctionStarts] 
              0x000000018a8c1b00 (    0x44) (null) [FUNC, FunctionStarts] 
              0x000000018a8c1b44 (    0xa8) (null) [FUNC, FunctionStarts] 
              0x000000018a8c1bec (    0x44) (null) [FUNC, FunctionStarts] 
              0x000000018a8c1c30 (    0x90) (null) [FUNC, FunctionStarts] 
              0x000000018a8c1cc0 (    0x84) (null) [FUNC, FunctionStarts] 
              0x000000018a8c1d44 (    0x68) (null) [FUNC, FunctionStarts]
              ...
```

symbols SwiftUI -arch arm64e -filterSegment "__TEXT”

## [一线希望](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework#a-ray-of-hope)

Apple 在 Xcode Organizer 中提供了一个免费崩溃报告服务，该服务为 App Store 和 TestFlight 构建收集并符号化崩溃报告。这些崩溃报告经过 Apple 的服务器，并在可能时进行符号化。对我们来说幸运的是，`SwiftUI` 在这些报告中已被符号化。

![Xcode Organizer 示例](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog17%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Xcode Organizer 示例

这意味着 Apple 确实拥有这些框架的 dSYM 文件，并且可以处理它们。问题是，我们如何提取它们？幸运的是，Xcode 会下载所有崩溃报告，我们可以通过右键点击它们来找到（保存路径为 `~/Library/Developer/Xcode/Products/YOUR_APP_BUNDLE_ID/Crashes/Points`）：

![从 Xcode Organizer 在访达中打开](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog17%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

从 Xcode Organizer 在访达中打开

当访达打开时，你会看到很多“文件”，其中你的文件已被选中。这些实际上是包含崩溃日志的文件夹。你可以通过右键点击并按下 `Show Package Contents` 来打开它们。

![崩溃位于 ~/Library/Developer/Xcode/Products/YOUR_APP_BUNDLE_ID/Crashes/Points](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog17%2F4.png&w=640&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

崩溃位于 ~/Library/Developer/Xcode/Products/YOUR_APP_BUNDLE_ID/Crashes/Points

![`xccrashpoint` 文件内的崩溃日志](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog17%2F3.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

`xccrashpoint` 文件内的崩溃日志

现在我们有了符号化的崩溃日志。这是很好的一步，但我们需要找到一种方法为一个特定的内存地址做到这一点。

```basic
Incident Identifier: CA429E35-72B9-4412-84D7-40EF2A7718F8
Hardware Model:      iPhone15,2
Process:             Emerge TestApp [22028]
...
Exception Type:  EXC_BREAKPOINT (SIGTRAP)
Exception Codes: 0x0000000000000001, 0x0000000100da8710
...

Thread 0 name:
Thread 0 Crashed:
0 Emerge TestApp 0x0000000100da8710 Swift runtime failure: Division by zero + 0 (<compiler-generated>:0)
1 Emerge TestApp 0x0000000100da8710 closure #3 in closure #1 in CrashView.body.getter + 432 (CrashView.swift:43)
2 Emerge TestApp 0x0000000100da8600 specialized _allocateUninitializedArray<A>(_:) + 24 (<compiler-generated>:0)
3 Emerge TestApp 0x0000000100da8600 closure #3 in closure #1 in CrashView.body.getter + 160 (CrashView.swift:43)
4 SwiftUI 0x00000001a9e9ad98 partial apply for implicit closure #2 in implicit closure #1 in WrappedButtonStyle.makeBody(configuration:) + 28
5 SwiftUI 0x00000001a9e9b320 ButtonBehavior.ended() + 240 (ButtonStyle.swift:349)
6 SwiftUI 0x00000001a9e9b224 implicit closure #2 in implicit closure #1 in ButtonBehavior.body.getter + 32 (ButtonStyle.swift:301)
...

...
Binary Images:
0x100da0000 - 0x100dabfff Emerge TestApp arm64 <5761b557a08d3b79ba5015baac99164b> /private/var/containers/Bundle/Application/5DBAE586-D41D-486F-9E31-03F97FFDA005/Emerge TestApp.app/Emerge TestAppTestApp.app/Emerge TestApp
...
0x1a956f000 - 0x1aaee7fff SwiftUI arm64e <14c7908e8c603bf7b6d8937d502b5918> /System/Library/Frameworks/SwiftUI.framework/SwiftUI
...
```

我们的符号化崩溃日志

本文主要关注符号化 SwiftUI，但所描述的技术同样适用于其他框架。

## [为地址查找符号](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework#finding-symbols-for-an-address)

上述方法可行，但让 App 为每个符号崩溃一次是不可行的（SwiftUI 中有超过 `198725` 个符号）。我们需要找到一种方法来操纵内存以批量添加地址。

第一步是获取当前堆栈跟踪。最初我们尝试了 Swift 的 [`Thread.callStackSymbols`](https://developer.apple.com/documentation/foundation/thread/1414836-callstacksymbols)，但它返回的是已经符号化的符号数组。这对调试很有用，但不是我们想要的。

然后我们查看了 [Libc 的 backtrace](https://opensource.apple.com/source/Libc/Libc-1439.141.1/gen/backtrace.c.auto.html)。这个替代方案返回地址，更重要的是，它是开源的，所以我们可以检查它是如何工作的。

查看 backtrace 的实现：

```cpp
int backtrace(void** buffer, int size) {
unsigned int num_frames;
_thread_stack_pcs((vm_address_t*)buffer, size, &num_frames, 1, NULL);
while (num_frames >= 1 && buffer[num_frames-1] == NULL) num_frames -= 1;
return num_frames;
}
```

相关代码在 _thread_stack_pcs 中，实现见[此处](https://opensource.apple.com/source/Libc/Libc-1081.1.3/gen/thread_stack_pcs.c.auto.html)：

```cpp
void _thread_stack_pcs(vm_address_t *buffer, unsigned max, unsigned *nb, unsigned skip) {
  void *frame, *next;
  pthread_t self = pthread_self();
  void *stacktop = pthread_get_stackaddr_np(self);
  void *stackbot = stacktop - pthread_get_stacksize_np(self);

  *nb = 0;
  stacktop -= (FP_LINK_OFFSET + 1) * sizeof(void *);

  frame = __builtin_frame_address(0);

  if (!INSTACK(frame) || !ISALIGNED(frame)) {
      return;
  }

  // Stripped skip code

  while (max--) {
      buffer[*nb] = *(vm_address_t *)(((void **)frame) + FP_LINK_OFFSET);
      (*nb)++;
      next = *(void **)frame;

      if (!INSTACK(next) || !ISALIGNED(next) || next <= frame) {
          return;
      }

      frame = next;
  }

};
```

让我们分解这段代码，首先它获取当前线程并得到堆栈的顶部和底部，同时将堆栈底部与内存对齐（`FP_LINK_OFFSET` 是内存指针的大小）：

```cpp
pthread_t self = pthread_self();
void *stacktop = pthread_get_stackaddr_np(self);
void *stackbot = stacktop - pthread_get_stacksize_np(self);

stacktop -= (FP*LINK_OFFSET + 1) * sizeof(void _);
```

这些信息对于解析堆栈跟踪至关重要。

然后它获取当前帧地址并检查它是否在堆栈中并且内存对齐，否则退出。

```cpp
frame = __builtin_frame_address(0);
if(!INSTACK(frame) || !ISALIGNED(frame))
return;
```

有了这些，它可以轻松地迭代堆栈中的地址：

```cpp
while (max--) {
buffer[*nb] = *(vm_address_t *)(((void **)frame) + FP_LINK_OFFSET);
(*nb)++;
next = *(void **)frame;
if(!INSTACK(next) || !ISALIGNED(next) || next <= frame)
  return;
frame = next;
}
```

这段底层代码工作得很好，但如果我们考虑用于堆栈的结构，可以使它更易读：

```cpp
typedef uintptr_t frame_data_addr_t;

struct frame_data {
  frame_data_addr_t frame_addr_next;
  frame_data_addr_t ret_addr;
};
```

基于这些信息，我们可以构建自己的 `print_my_backtrace` 实现：

```cpp
void print_my_backtrace() {
  int max = 100; // Print up to 100 frames
  void *frame, *next;
  pthread_t self = pthread_self();
  void *stacktop = pthread_get_stackaddr_np(self);
  void *stackbot = stacktop - pthread_get_stacksize_np(self);

  frame = __builtin_frame_address(0);

  if (!INSTACK(frame) || !ISALIGNED(frame)) {
      return;
  }

  int counter = 0;
  while (max--) {
      struct frame_data *currentFrame = (struct frame_data *)frame;
      printf("[%i] - %lu", counter, currentFrame->ret_addr);

      next = (void *)currentFrame->ret_addr;

      if (!INSTACK(next) || !ISALIGNED(next) || next <= frame) {
          return;
      }

      frame = next;
  }

};
```

这里堆栈跟踪打印的是 `print_my_backtrace` 的帧。我们需要在开始计数器之前将帧调整到下一个，以跳过它。`frame_data` 是可修改的，这意味着我们实际上可以将返回地址（`ret_addr`）替换为任何我们想要的地址。基于当前的实现，我们可以为每个线程执行此操作，并替换堆栈中的每个函数。

既然我们可以编辑堆栈，我们需要获取 SwiftUI 的符号输出中所有符号的地址。下一节将介绍如何分析内存中的 SwiftUI 二进制文件以找到所有函数。

## [获取 SwiftUI 的所有地址](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework#getting-all-addresses-for-swiftui)

虽然这一步听起来很难，但实际上是最简单的之一。我们可以使用开源代码来提取 `Function Starts`，它给出了 Mach-O 二进制文件中每个函数的起始地址。

首先，我们可以使用 `dyld` 来获取 `SwiftUI` 的[加载地址](https://developer.apple.com/documentation/xcode/examining-the-fields-in-a-crash-report#Binary-images)：

```cpp
const imagePath = "/System/Library/Frameworks/SwiftUI.framework/SwiftUI"
const uint32_t image_count = _dyld_image_count();
for (uint32_t image_index = 0; image_index < image_count; image_index++) {
  const char *imageName = _dyld_get_image_name(image_index);
  
  if (strcmp(imageName, imagePath) != 0) {
      continue;
  }
  
  const struct mach_header_64 *header = (const void *)_dyld_get_image_header(image_index);
  ...
}
```

找到镜像头后，我们只需要遍历加载命令直到找到所需的信息。`LC_SEGEMENT_64` 提供了查找和验证 `Function Starts` 数据的信息。`LC_FUNCTION_STARTS` 加载命令获取所有函数起始点。

```cpp
#import <mach-o/dyld.h>

intptr_t slide = _dyld_get_image_vmaddr_slide(image_index);

uint64_t linkedit_seg_start = 0;
uint64_t linkedit_seg_end = 0;
uint64_t linkedit_seg_fileoff = 0;

uint64_t text_seg_start = 0;
uint64_t text_sect_start = 0;
uint64_t text_sect_end = 0;

const struct load*command _load_cmd = (const void *)(header + 1);
for (uint32*t i = 0; i < header->ncmds; ++i) {
switch (load_cmd->cmd) {
case LC_SEGMENT_64: {
const struct segment_command_64 _seg_cmd = (const void *)load_cmd;

          // __LINKEDIT 的信息用于计算 Function Starts 数据的地址
          if (strncmp(seg_cmd->segname, SEG_LINKEDIT, sizeof(seg_cmd->segname)) == 0) {
              linkedit_seg_fileoff = seg_cmd->fileoff;
              linkedit_seg_start = seg_cmd->vmaddr + slide;
              linkedit_seg_end = linkedit_seg_start + seg_cmd->vmsize;
          }

          if (strncmp(seg_cmd->segname, SEG_TEXT, sizeof(seg_cmd->segname)) == 0) {
              text_seg_start = seg_cmd->vmaddr + slide;
              // 获取 __text section 信息，以便后续验证函数地址
              for (uint32_t sect_idx = 0; sect_idx < seg_cmd->nsects; sect_idx++) {
                  const struct section_64 *section = (const struct section_64 *)(seg_cmd + 1) + sect_idx;
                  if (strncmp(section->sectname, SECT_TEXT, sizeof(section->sectname)) == 0) {
                      text_sect_start = section->addr + slide;
                      text_sect_end = text_sect_start + section->size;
                      break;
                  }
              }
          }

          break;
      }
      case LC_FUNCTION_STARTS: {
        ...
      }
  }
  // 读取下一个加载命令
  load_cmd = (const void *)((const char *)load_cmd) + load_cmd->cmdsize;

}
```

要解析 `Function Starts`，我们可以使用 Apple 的实现[此处](https://opensource.apple.com/source/ld64/ld64-241.9/src/other/dyldinfo.cpp)，并根据我们的需求进行调整：

```cpp
uint64_t* functionStartsArray = malloc(sizeof(uint64_t) * INITIAL_CAPACITY);
int capacity = INITIAL_CAPACITY;
int counter = 0;

...
case LC*FUNCTION_STARTS: {
const struct linkedit_data_command _data_cmd = (const void *)load*cmd;
assert(data_cmd->dataoff > linkedit_seg_fileoff);
const uint32_t offset_from_linkedit = data_cmd->dataoff - (uint32_t) linkedit_seg_fileoff;
const uint8_t _start = (const uint8_t *)linkedit_seg_start + offset_from_linkedit;
const uint8_t *end = start + data_cmd->datasize;
assert((uintptr_t)end < linkedit_seg_end);

  uint64_t address = text_seg_start;

  // 函数起始点以 LEB128 编码的一系列偏移量存储。
  // 改编自 DyldInfoPrinter<A>::printFunctionStartsInfo() in ld64-127.2/src/other/dyldinfo.cpp
  for (const uint8_t *p = start; (*p != 0) && (p < end); ) {

      // 增加数组容量
      if (counter == capacity) {
          capacity *= 2;
          functionStartsArray = realloc(functionStartsArray, sizeof(uint64_t) * capacity);

          if (functionStartsArray == NULL) {
              fprintf(stderr, "Memory reallocation failed");
              exit(1);
          }
      }

      uint64_t delta = 0;
      uint32_t shift = 0;
      bool more = true;
      do {
          uint8_t byte = *p++;
          delta |= ((byte & 0x7F) << shift);
          shift += 7;
          if (byte < 0x80) {
              address += delta;
              assert(// Function address resides in the __text section
                     address >= text_sect_start && address < text_sect_end);

              functionStartsArray[counter++] = address;

              more = false;
          }
      } while (more);
  }
  break;

}
```

由于我们想要获取完整的函数起始点列表，我们将地址保存在一个数组中。为简化起见，我在 C 中使用了一个简单的指针数组，并在必要时将大小加倍。

## [改进符号提取](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework#improving-symbols-extraction)

现在我们有了重建符号所需的所有信息。通过将从 `LC_FUNCTION_STARTS` 提取的地址插入到我们修改过的堆栈跟踪中，我们可以伪造一个包含 SwiftUI 函数的崩溃来对它们进行符号化。

虽然我没有找到 iOS 最大堆栈大小或线程限制的文档，但我无法从 Apple 的崩溃中获得超过 550 帧。所以我们需要 `198725/550=361` 次崩溃才能完全符号化——这不可行。

幸运的是，Apple 对所有线程进行符号化，所以我们实际上可以在崩溃前创建多个线程。我创建了 `EMGThread` 来帮助：

```objectivec
#define    MAX_FRAMES 550

@interface EMGThread : NSThread
@property (copy) void (^completionBlock)(void);
@property (nonatomic, assign) NSInteger startingIndex;
@property (nonatomic, assign) uint64_t *addresses;
@end
```

```objectivec
#define    INSTACK(a)    ((a) >= stackbot && (a) <= stacktop)
#define    ISALIGNED(a)    ((((uintptr_t)(a)) & 0x1) == 0)

typedef uintptr_t frame_data_addr_t;

struct frame_data {
frame_data_addr_t frame_addr_next;
frame_data_addr_t ret_addr;
};

@interface EMGThread ()
@property (nonatomic, assign) NSInteger threadLoopCounter;
@end

@implementation EMGThread

-(void) main {
if (_threadLoopCounter < MAX_FRAMES) {
_threadLoopCounter++;
[self main];
}

  [self modifyFrameAndWait];

}

- (void) modifyFrameAndWait {
// 要打印的帧数
int max = MAX_FRAMES;

    void *frame, *next;
    pthread_t thisThread = pthread_self();
    void *stacktop = pthread_get_stackaddr_np(thisThread);
    void *stackbot = stacktop - pthread_get_stacksize_np(thisThread);

    // 依赖调用者拥有空堆栈帧（无局部变量）的事实
    // 来确定堆栈帧的最小大小（帧指针和返回地址）
    frame = __builtin_frame_address(0);
    next = (void *)((struct frame_data *) frame)->ret_addr;

    /* 确保返回地址不会越界 */
    stacktop -= (next - frame);

    int counter = 0;

    if(!INSTACK(frame) || !ISALIGNED(frame))
        return;

    // 跳过一个帧，以便在需要时返回调用函数
    frame = next;

    while (max--) {
        // 尝试覆盖
        struct frame_data *frameModifier = (struct frame_data *)frame;

        // 加 2 使地址位于函数起始点之后
        frameModifier->ret_addr = self.addresses[self.startingIndex + counter++] + 2;

        next = (void *)frameModifier->ret_addr;

        if(!INSTACK(next) || !ISALIGNED(next) || next <= frame)
            return;
        frame = next;
    }

    // 通知完成
    self.completionBlock();

    // 使线程休眠但保持其活跃，以便堆栈跟踪使用
    while(true) {
        [NSThread sleepForTimeInterval:0.01];
    }

}
```

我们还将使用一个辅助类 EMGCrasher 来同步多个线程，并在一切就绪时使 App 崩溃。

```objectivec
class EMGCrasher {
  var completedThreads = 0
  let lock = NSLock()
  
  func crash(_ threadCount: Int) -> Bool {
      let functions = get_function_starts()
      let threadCount = functions.functionsCount / Int(MAX_FRAMES)
      
      for index in 0..<threadCount {
          let thread = EMGThread()
          thread.startingIndex = index * Int(MAX_FRAMES)
          thread.addresses = functions.functionsPointers!
          thread.completionBlock = { [self] in
              self.lock.lock()
              self.completedThreads += 1
              self.lock.unlock()
          }
          thread.start()
      }
      
      while(completedThreads != threadCount) {
          usleep(100)
      }
      
      fatalError("Crash App (Excpected)")
  }
}
```

## [总结](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework#wrapping-up)

通过这些步骤，我们现在拥有了完整的 SwiftUI 框架符号化。我们将发布本博客的第二部分，在其中我们将解析崩溃并构建一个工具来帮助符号化它们。

你可以订阅下面的新闻通讯，以便在它发布时收到通知！在那之前，祝编码愉快，符号化顺利！
