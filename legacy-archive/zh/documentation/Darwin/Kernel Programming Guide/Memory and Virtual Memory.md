---
title: 内存与虚拟内存
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/vm/vm.html
archived_at: '2026-07-15T07:23:14.219055Z'
translated: true
---
> 导航：[总目录](../../../../en/README.md) · [documentation](../../../../en/_indexes/documentation.md) · [Kernel Programming Guide（英文）](../../../../en/documentation/Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md)


[下一页](../../../../en/documentation/Darwin/Kernel%20Programming%20Guide/Mach%20Scheduling%20and%20Thread%20Interfaces.md)[上一页](../../../../en/documentation/Darwin/Kernel%20Programming%20Guide/Mach%20Overview.md)

# 内存与虚拟内存

本章说明在内核中分配内存，以及修改内存映射所用的低层例程。
它还介绍虚拟内存系统中若干常用接口。本章不说明如何更改分页策略，
也不说明如何添加额外的分页器。OS X 不支持外部分页器；不过，
其中大部分功能可通过其他方式实现，本章会从高层角度介绍其中一些方式。
但是，这些接口的实现细节可能变化，因此未予以文档化。

除[在内核中分配内存](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgawugscejbeusssg)一节外，
本章只适合正在编写文件系统，或修改虚拟内存系统本身的读者。

OS X 使用的 VM 系统源自 20 世纪 80 年代卡内基梅隆大学创建的 Mach VM。
其基本设计大体相同，但有些细节不同，特别是在增强 VM 系统时。
不过，它确实支持通过 _universal page lists（通用页面列表，UPL）_ 请求特定分页行为。
详见[通用页面列表（UPL）](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgawugscejfdesq2h)。

Mach VM 的设计核心是：物理内存是虚拟内存的缓存。

在最高层次上，Mach VM 由地址空间，以及从空间外部操作这些地址空间内容的方法构成。
这些地址空间是稀疏的，并带有保护机制，以限制哪些任务能够访问其内容。

在较低的对象层次上，虚拟内存可看作 VM 对象和内存对象的集合；每个对象都有特定的所有者和保护属性。
任务和分页器（通过 VM 的后端）都可以使用对象调用来修改这些对象。

VM 对象是虚拟内存系统内部的对象，包含访问内存所需的基本信息。相对地，内存对象由分页器提供。
与该内存对象关联的内存内容，可通过与内存对象交换消息，从磁盘或其他后备存储中取得。
隐含地，每个 VM 对象都会通过其内存对象关联到特定分页器。

VM 对象以系统页面（RAM）为缓存；系统页面的大小可以是硬件页面大小的任意 2 的幂倍数。
在 OS X 内核中，系统页面和硬件页面大小相同。给定地址空间中的每个系统页面，都由一个映射条目表示。
每个映射条目有自己的保护和继承属性。给定映射条目的继承属性可以是 `shared`、`copy` 或 `none`。
若某页面在给定映射中标为 `shared`，子任务会共享该页面以进行读写。若标为 `copy`，子任务会得到该页面的副本（使用写时复制）。
若标为 `none`，子任务的该页面不会分配。

VM 对象由与机器无关的 VM 系统管理，底层的虚拟到物理映射则由与机器相关的 _pmap 系统_处理。
`pmap` 系统会根据底层硬件设计实际处理页表、转换后备缓冲器、段等内容。

VM 对象被复制时（例如，刚调用 `fork` 的进程的数据页面），会创建一个 _shadow object（影子对象）_。
影子对象起初为空，并持有对另一对象的引用。修改页面内容时，页面会先从父对象复制到影子对象，再被修改。
读取页面数据时，若该页面存在于影子对象中，就使用影子对象列出的页面；若影子对象没有该页面的副本，则查阅原始对象。
一系列指向影子对象或原始对象的影子对象称为 _shadow chain（影子链）_。

若频繁以写时复制方式重用对象，影子链可以任意长。不过，`fork` 后通常紧接着调用[exec](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/exec.3.html#//apple_ref/doc/man/3/exec)，
后者会替换全部被影子化的内容，因此长链很少见。此外，Mach 会自动垃圾回收影子对象，删除页面不再被任何未失效影子对象引用的中间影子对象。
若原始对象已不含与该链相关的页面，它也可能被释放。

应用程序可用的 VM 调用包括 `vm_map` 和 `vm_allocate`，可将文件数据或匿名内存映射到地址空间。
这之所以可行，是因为地址空间起初是稀疏的。一般而言，应用程序既可以通过 BSD 抽象的文件映射原语将文件映射到地址空间，
也可以在取得对象句柄后映射该对象。此外，任务可改变其地址空间中对象的保护属性，并可与其他任务共享这些对象。

除了映射与分配，VM 系统还包含许多其他子系统，包括后端（分页器）和共享内存子系统。
还有与 VM 紧密相关的其他子系统，包括 VM 共享内存服务器。这些内容见[其他 VM 及 VM 相关子系统](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgawugscejjbemqsd)。

每个 Mach 任务都有自己的内存映射。在 Mach 中，该内存映射是一个有序双向链表。
如[OS X VM 概览](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgawugsceivceoq2b)所述，
这些对象分别包含页面列表和对其他对象的影子引用。

通常，你绝不需要直接访问内存映射，除非你正在修改 VM 系统深层的内容。
`vm_map_entry` 结构包含单个映射的任务专属信息，以及对后备对象的引用。本质上，它是 VM 对象与 VM 映射之间的黏合层。

尽管该数据结构的细节超出本文范围，其中若干字段尤为重要。

`is_submap` 字段是一个布尔值，说明该映射条目是普通 VM 对象还是 _submap（子映射）_。
子映射是更大映射中的一组映射。子映射常用于将映射分组，以便在多个 Mach 任务间共享，但也可用于多种用途。
子映射特别强大之处在于：多个任务将其映射到地址空间后，彼此不仅能看到映射中对象内容的变化，也能看到对象本身的变化。
这意味着，向子映射添加或从中删除对象时，这些对象会在共享该子映射的所有任务地址空间中出现或消失。

`behavior` 字段控制给定映射中指定范围的分页引用行为。
该值会改变页面调入的聚簇方式。可能的值为 `VM_BEHAVIOR_DEFAULT`、`VM_BEHAVIOR_RANDOM`、`VM_BEHAVIOR_SEQUENTIAL` 和 `VM_BEHAVIOR_RSEQNTL`，
分别表示默认、随机、顺序或反向顺序的页面调入次序。

`protection` 和 `max_protection` 字段控制对象权限。`protection` 字段表示任务当前拥有的对象权限，
而 `max_protection` 字段包含当前任务能够获得的最大访问权限。

调试共享内存时，你可能会使用 `protection` 字段。将保护设为只读，可使对共享内存的意外写入触发异常。
但任务确实需要写入该共享区域时，可提高 `protection` 字段中的权限以允许写入。

不过，若任务能任意提高自己对内存对象的权限，就会形成安全漏洞。为了维持合理的安全模型，
拥有内存对象的任务必须能够限制授予下属任务的权限。因此，任务不得将其保护权限提高到 `max_protection` 授予的权限之上。

`protection` 和 `max_protection` 的可用值详见 `xnu/osfmk/mach/vm_prot.h`。

最后，`use_pmap` 字段表示：子映射映射进的所有任务是否应共享该子映射的低层映射。
如果映射不共享，则所有任务共享映射结构，但不共享页面的实际内容。

例如，共享库由两个子映射处理。只读的共享代码段将 `use_pmap` 设为 true。
读写的非共享段将 `use_pmap` 设为 false，因此每个新任务都会从磁盘映射出库的 `DATA` 段的干净副本。

OS X VM 系统提供一种称为 _named entry（命名条目）_的抽象。
命名条目只是共享对象或子映射的一个句柄。

OS X 的共享内存支持通过在多个任务的内存映射之间共享对象实现。
共享内存对象必须由现有 VM 对象创建：先调用 `vm_allocate` 在你的地址空间中分配内存，
再调用 `mach_make_memory_entry_64` 取得底层 VM 对象的句柄。

`mach_make_memory_entry_64` 返回的句柄可传给 `vm_map`，
以便将该对象映射到给定任务的地址空间。该句柄也可通过 IPC 或其他方式传给其他任务，
使它们将对象映射到自己的地址空间。这使你可以与不在直接谱系中的任务共享对象，
也可在直接谱系中的任务创建后，与它们共享额外内存。

命名条目的另一种形式是子映射，用于将一组映射分组。子映射最常见的用途是在多个 Mach 任务间共享映射。
可使用 `vm_region_object_create` 创建子映射。

子映射特别强大之处在于：多个任务将其映射到地址空间后，可以看到彼此对数据和映射结构的修改。
这意味着，一个任务只要在子映射中映射或取消映射 VM 对象，就能在另一任务的地址空间中映射或取消映射该对象。

通用页面列表（UPL）是与虚拟内存系统通信时使用的数据结构。UPL 可改变页面在缓存、权限、映射等方面的行为。
UPL 还可向 VM 对象推送数据，或从 VM 对象拉取数据。该术语也常指操作 UPL 的整组例程。
处理 UPL 时使用的标志定义在 `osfmk/mach/memory_object_types.h` 中。

UPL 的生命周期如下：

1. 根据 VM 对象的内容创建 UPL。该 UPL 包含该对象内页面的信息。
2. 以某种方式修改该 UPL。
3. 使用 [ubc_upl_commit](https://developer.apple.com/documentation/kernel/1463702-ubc_upl_commit) 或 [ubc_upl_abort](https://developer.apple.com/documentation/kernel/1463754-ubc_upl_abort)，
   分别提交更改（推回 VM 系统）或中止更改。

如果你拥有给定 VM 对象的控制句柄（这通常表示你身处分页器内部），可使用 `vm_object_upl_request` 获取该对象的 UPL。
否则，必须使用 `vm_map_get_upl` 调用。无论哪种方式，最终都会得到 UPL 的句柄。

请求页面调入时，分页器会收到一份相对于对象锁定的页面列表，其中某些页面被设为无效。
分页器必须向这些页面写入数据，或中止事务，以避免内核中存在无效数据。类似地，在页面调出时，
内核必须将数据写入后备存储，或中止事务以防止数据丢失。分页器也可自行决定额外调入页面或额外调出页面。

由于分页器既可用于虚拟内存，也可用于文件数据的内存映射，收到页面调出请求时，可能需要从内存释放数据，
也可能希望将其留在内存中，只把更改刷新到磁盘。因此有 `UPL_CLEAN_IN_PLACE` 标志，
它允许将页面刷新到磁盘而不将其从内存移除。

分页器决定额外调入或调出页面时，必须确定要移动哪些页面。设置 `RETURN_ONLY_DIRTY` 标志可请求所有脏页。
也可使用 `RETURN_ONLY_ABSENT` 标志请求所有不在内存中的页面。

不过存在一个小问题。若给定页面在 UPL 中标为 `BUSY`，对该页面的信息请求通常会阻塞。
分页器进行预读或预刷写时，这并不理想，因为它可能阻塞在自身，或阻塞在正等待当前事务完成的其他分页器上。
为避免这种死锁，UPL 机制提供 `UPL_NOBLOCK` 标志。匿名分页器请求空闲内存时经常使用它。

`QUERY_OBJECT_TYPE` 标志可用于判断对象是否物理连续，并取得底层对象的其他属性。

`UPL_PRECIOUS` 标志表示数据应只有一份副本。这样可以防止数据同时在内存和后备存储中各有一份副本。
但它会破坏后备存储中相邻页面的相邻性，因此通常不会使用，以避免性能损失。

`SET_INTERNAL` 标志由 BSD 子系统使用，使 UPL 的所有信息都包含在单个内存对象中，因而更易于传递。
仅当代码运行在内核地址空间中时才能使用该标志。

由于这个句柄可用于多笔小事务（例如，分块将文件映射到内存），UPL API 包含只提交或中止部分 UPL 更改的函数。
这些函数分别是 [upl_commit_range](https://developer.apple.com/documentation/kernel/1538509-upl_commit_range) 和 [upl_abort_range](https://developer.apple.com/documentation/kernel/1538505-upl_abort_range)。

为便于使用 UPL 处理多部分事务，[upl_commit_range](https://developer.apple.com/documentation/kernel/1538509-upl_commit_range) 和 [upl_abort_range](https://developer.apple.com/documentation/kernel/1538505-upl_abort_range) 调用
带有一个标志：UPL 中没有未修改页面时释放 UPL。若使用此标志，务必不要在所有范围均已提交或中止后继续使用 UPL。

最后，`vm_map_get_upl` 函数常用于文件系统。它取得地址空间内给定范围关联的底层 VM 对象。
由于它只返回该范围内的第一个对象，你有责任确定得到的 UPL 是否覆盖整个范围；若不覆盖，
则需额外调用以取得其他对象的 UPL。请注意，`vm_map_get_upl` 调用针对地址空间范围，
而大多数 UPL 调用针对的是 `vm_object`。

在内核上下文中（_不是_ KEXT 中），你很可能需要处理两种映射。第一种是内核映射。
由于代码正在内核地址空间执行，使用内核映射引用的内存不需要额外工作。
不过，你可能需要向内核映射添加额外映射，并在不再需要时将其移除。

第二种相关映射是给定任务的内存映射。它对接受用户程序输入的代码最有意义，
例如 `sysctl` 或 Mach RPC 处理程序。不过，绝大多数情况下都有方便的包装器提供所需功能。

这些函数大多围绕 `vm_offset_t` 类型设计，它是一个与指针等宽的整数。实际上可将它们视为指针，
但要注意：根据用法，它们未必指向内核地址空间中的数据。

低层 VM 映射 API 包括以下函数：

```
kern_return_t vm_map_copyin(vm_map_t src_map, vm_offset_t src_addr,
            vm_size_t len, boolean_t src_destroy,
            vm_map_copy_t *copy_result);

kern_return_t vm_map_copyout(vm_map_t map, vm_offset_t *addr, /*  Out */
            register vm_map_copy_t copy);

kern_return_t vm_map_copy_overwrite(vm_map_t dst_map,
            vm_offset_t dst_address,vm_map_copy_t copy,
            boolean_t interruptible, pmap_t pmap);

void vm_map_copy_discard(vm_map_copy_t copy);

void vm_map_wire(vm_map_t map, vm_offset_t start, vm_offset_t end,
            vm_prot_t access_type, boolean_t user_wire);

void vm_map_unwire(vm_map_t map, vm_offset_t start, vm_offset_t  end,
            boolean_t user_wire);
```

`vm_map_copyin` 函数将数据从任意（可能不是内核）内存映射复制到复制列表，
并在 `copy_result` 中返回复制列表指针。若发生问题而需丢弃这个中间对象，
应使用 `vm_map_copy_discard` 释放它。

要实际从复制列表取得数据，需要使用 `vm_map_copy_overwrite` 覆盖内核地址空间中的内存对象。
该函数会用复制列表的内容覆盖对象。多数情况下，`interruptible` 应传入 `FALSE`，
`pmap` 应传入 `NULL`。

从内核向用户空间复制数据，与从用户空间复制数据完全相同，只是将 `kernel_map` 传给 `vm_map_copyin`，
并将用户映射传给 `vm_map_copy_overwrite`。不过通常应避免这样做，因为任务内存可能会碎片化为许多微小对象，
这并不可取。

向现有用户任务的地址映射复制数据时，_不要_ 使用 `vm_map_copyout`。
`vm_map_copyout` 用于填充地址映射中未使用的区域；若区域已分配，`vm_map_copyout` 不执行任何操作。
它需要了解映射的当前状态，因此主要用于创建新地址映射时（例如手动创建新进程）。多数情况下不需要使用 `vm_map_copyout`。

`vm_map_wire` 和 `vm_map_unwire` 可将地址映射的一部分锁定到内存或解除锁定。
若将参数 `user_wire` 设为 `TRUE`，则可从用户空间解除页面锁定。
即将把内存用于 I/O 或其他不能容忍分页的操作时，应将其设为 `FALSE`。
在 `vm_map_wire` 中，参数 `access_type` 指出哪些访问类型不应产生缺页异常。
不过通常应使用 `vm_wire` 锁定内存。

如前所述，这些信息严格仅供内核核心部分使用。不能从内核扩展中使用本节任何内容。

另有两个 VM 子系统：分页器和工作集检测子系统。此外，VM 共享内存服务器子系统与 VM 子系统紧密相关，但不属于它。
本节介绍这三个 VM 及 VM 相关子系统。

OS X 有三个基本分页器：vnode 分页器、默认分页器（或匿名分页器）和设备分页器。
VM 系统通过它们将数据实际取入构成命名条目底层的 VM 对象。分页器通过部分旧 Mach 分页器接口和 UPL 的组合连接到 VM 系统。

默认分页器是大多数人想到 VM 系统时所指的组件。它负责将普通数据移入和移出后备存储。
此外，默认分页器之上还有名为动态分页器的设施，负责创建和删除后备存储文件。
这些分页器文件以聚簇（页面组）为单位填充数据。

分页文件池的总使用率达到高水位线时，默认分页器会要求动态分页器分配新的存储文件。
该池降至低水位线以下时，VM 系统会选择一个分页器文件，将其内容移到其他分页器文件中，并从磁盘删除该文件。

vnode 分页器在 VM 空间中的对象与打开的文件（vnode）之间有一对一（满射）映射。
它用于内存映射文件 I/O。vnode 分页器通常隐藏在对 BSD 文件 API 的调用之后。

设备分页器允许你以该内存所需的缓存特性（_WIMG_）映射非通用内存。
非通用内存包括映射到主内存以外硬件的物理地址，例如 PCI 内存、帧缓冲内存等。
设备分页器通常隐藏在对各种 I/O Kit 函数的调用之后。

为提高性能，OS X 有一个称为工作集检测子系统的子系统。VM 缺页时会调用它；
它从任务创建时起维护每个任务的缺页行为概况。此外，就在页面请求之前，缺页代码会询问该子系统应调入哪些相邻页面，
然后向分页器发出一次大型请求。

磁盘文件通常具有良好的局部性，且地址空间局部性在后备存储中大致会被保留，因此这可显著提高性能。
此外，它基于应用程序先前的行为，往往会调入本来可能稍后才需要的页面。所有分页器都会发生这种情况。

工作集代码建立起来后效果良好。不过，若没有帮助，在建立给定应用程序的概况前，其性能只能达到基准水平。
为克服此问题，给定用户上下文中首次启动应用程序时，会捕获启动该应用所需的初始工作集并存入文件。
之后启动该应用时，该文件会用于为工作集提供初始数据。

这些工作集文件按用户分别建立，保存在 `/var/vm/app_profile`，且仅超级用户（和内核）可以访问。

VM 共享内存服务器子系统是与 VM 紧密相关、但不属于 VM 的 BSD 服务。
该服务器提供两个子映射，用于支持 OS X 中的共享库。由于共享库同时包含只读部分（文本段）和读写部分（数据段），
两部分会被分别处理以尽可能提高效率。只读部分在任务之间完全共享，包括底层 `pmap` 条目。
读写部分共享一个公共子映射，但底层数据对象不同（通过写时复制实现）。

VM 共享内存服务器子系统导出的三个函数只能由 `dyld` 调用。
请不要在程序中使用它们。

`load_shared_file` 函数用于向系统加载新的共享库。文件一旦加载，其他任务即可依赖它，
因此共享库不能取消共享。不过，可通过 `new_system_shared_regions` 创建一组新的共享区域，
使后续新任务不再使用旧库。

`reset_shared_file` 函数可重置任务可能对某个文件数据段私有副本所做的任何修改。

最后，`new_system_shared_regions` 函数可为未来任务创建一组新的共享区域。
更新预绑定并加入新共享库时，可使用新区域，使新任务在内存中的新位置看到最新库。
（使用旧共享库的用户仍可工作，但会脱离预绑定路径，效率较低。）
当处理只希望与任务后代共享的私有库时，也可使用它。

本节说明开发者在 Panther 或更高版本中使用驱动程序时可能看到的问题。
这些更改由硬件与底层 OS 更改共同促成；不过，即使在既有硬件上，也可能因这些改变看到问题。

OS X v10.3 有三个基本变化领域：

- `IOMemoryDescriptor` 更改
- VM 系统（`pmap`）
  更改
- 内核依赖项更改

下节将详细说明这些变化。

为使现有设备驱动程序能在将来的 64 位系统架构上工作，需要进行若干更改。
要解释这些更改，先简要介绍 PCI 总线桥。

PCI 设备需要向主内存发起或从主内存接收数据事务时，设备驱动程序会调用一系列函数为 I/O 准备该内存。
在设备驱动程序和内存子系统都使用 32 位寻址的架构中，只要内存不会在 I/O 操作期间被分页换出，一切都会正常工作。
由于内核内存通常不可分页，这些准备大多是多余的。

但是，在内存子系统使用 64 位寻址的系统中，问题会更复杂。PCI 总线上的硬件设备只能处理 32 位地址，
因此设备在任意时刻只能“看见”主内存中一个 4 GB 的窗口，而主内存可能远大于此。

此问题有两种解决方案。简单但较慢的方案是使用“弹跳缓冲区”。在这种设计中，设备驱动程序会将数据复制到
专门分配在内存低 4 GB 内的内存中。但这会带来性能损失，也会给低 4 GB 内存增加额外约束，从而为 VM 系统造成许多问题。

Apple 的 64 位实现选择另一种方案：使用地址转换将内存块“映射”到 PCI 设备的 32 位地址空间。
PCI 设备仍然只能看到 4 GB 窗口，但该窗口可以是不连续的，因此不需要弹跳缓冲区及其他限制。
这种地址转换由内存控制器中称为 DART 的部分完成，DART 即 Device Address Resolution Table（设备地址解析表）。

不过，这会引入若干潜在问题。首先，处理器看到的物理地址不再与 PCI 设备看到的地址一一对应。
因此引入术语 I/O 地址来描述这种新视角。由于 I/O 地址与物理地址不再相同，DART 必须维护转换表以便在两者间映射。
幸而，若驱动程序按 Apple 指南编写（只使用已文档化的 API），该过程会透明地处理。

驱动程序调用 `IOMemoryDescriptor``::``prepare` 时，映射会自动注入 DART。
调用 `IOMemoryDescriptor``::``release` 时，映射会被移除。若未这样做，驱动程序可能出现随机数据损坏或内核恐慌。

由于 DART 对读取和写入需要不同的缓存，DMA 方向在包含 DART 的硬件上很重要。
通常方向错误时，在任何系统上都可能随机失败；而在 DMA 方向设为读取的内存区域上调用 WriteBytes 时，
会在 64 位硬件上导致内核恐慌。

若尝试对未锁定的用户内存执行 DMA 事务，在旧系统上只会遇到随机崩溃、内核恐慌和数据损坏。
在配有 DART 的机器上，很可能完全得不到数据。

作为内存子系统更改的副作用，OS X 更可能在内存区域中返回物理连续的页面范围。
过去 OS X 以倒序返回多页面内存区域，从最后一页开始向第一页移动。
结果是，多页面内存区域实际上从不具有连续的物理页面范围。

因为在内存区域中看到物理连续内存块的概率提高，此更改可能暴露某些驱动程序中的潜在错误。
这些错误只会在处理连续物理页面范围时出现，可能导致行为错误或内核恐慌。

请注意，上述问题由驱动程序中的错误造成，在 Panther 以前的旧硬件上也可能引发问题。
不过，由于新的硬件设计以及支持这些设计的 OS 更改，这些问题在 Panther 及更高版本 OS X 中更可能出现。

在 Panther 中，由于 PCI 地址转换一节详细说明的更改，直接从 `pmap` 层取得的物理地址在 VM 系统本身之外没有用途。
为防止设备驱动程序无意使用它们，内核扩展不再能使用 `pmap` 调用。

在 `IOMemoryDescriptor` 类加入之前编写的一些驱动程序，仍会使用 `pmap` 调用取得与虚拟地址关联的物理页面。
此外，一些开发者查看 `IOMemoryDescriptor` 的实现后，选择直接从 `pmap` 层取得地址，
以移除被认为不必要的抽象层。

即使不移除对 `pmap` 调用的访问，这些驱动程序在具有 DART 的系统上也无法工作（关于 DART 参见前文 PCI 部分）。
为了更明确地表明即将发生的失败，Panther 会使这些驱动程序加载失败并报未定义符号错误（通常是 `pmap_extract`），
即使系统没有 DART 也是如此。

从 Panther 开始，声明依赖 I/O Kit 版本 7（Panther 版本）的设备驱动程序不再自动获得 Mach 和 BSD 符号。
这一改变旨在阻止 I/O Kit 开发者依赖未被明确批准可在 I/O Kit 中使用的符号。

现有驱动程序不受该改变影响。只有在你显式修改设备驱动程序，声明依赖 I/O Kit 版本 7，
以利用新的 I/O Kit 功能时，才会受影响。

如上所述，一些设备驱动程序可能需要小幅修改以支持 Panther 及更高版本。
Apple 已尽力最大程度确保与现有设备驱动程序兼容，但少数驱动程序可能失效。
如果驱动程序失效，应先检查它是否包含前述各节描述的任何错误；若没有，请联系 Apple Developer Technical Support 获取额外调试建议。

与 OS X 内核中的大多数事物一样，分配内存有多种方式。例程的选择取决于调用例程的位置和分配内存的原因。
通常应使用 Mach 例程分配内存；若正在编写供 I/O Kit 使用的代码，则应使用 I/O Kit 例程。

`<libkern/OSMalloc.h>` 头文件定义以下内核内存分配例程：

- [OSMalloc](https://developer.apple.com/documentation/kernel/1398447-osmalloc)—分配一个内存块。
- [OSMalloc_noblock](https://developer.apple.com/documentation/kernel/1398431-osmalloc_noblock)—分配一个内存块；若请求会阻塞，则立即返回 NULL。
- [OSMalloc_nowait](https://developer.apple.com/documentation/kernel/1398445-osmalloc_nowait)—与 `OSMalloc_noblock` 相同。
- [OSFree](https://developer.apple.com/documentation/kernel/1398441-osfree)—释放通过任一 `OSMalloc` 变体分配的内存。
- [OSMalloc_Tagalloc](https://developer.apple.com/documentation/kernel/1398437-osmalloc_tagalloc)—允许你为内存分配创建唯一标记。使用任何 `OSMalloc` 函数前，你 `must` 至少创建一个标记。
- [OSMalloc_Tagfree](https://developer.apple.com/documentation/kernel/1398439-osmalloc_tagfree)—释放由 OSMalloc_Tagalloc 分配的标记。（调用此函数前，你 _必须_ 释放与该标记关联的全部分配。）

例如，要分配并释放一页已锁定内存，可以编写如下代码：

```c
#include <libkern/OSMalloc.h>
#define MYTAGNAME "com.apple.mytag"

...

OSMallocTag mytag = OSMalloc_Tagalloc(MYTAGNAME, OSMT_DEFAULT);
void *datablock = OSMalloc(PAGE_SIZE_64, mytag);

...

OSFree(datablock, PAGE_SIZE_64, mytag);
```

要分配一页可分页内存，请在调用 `OSMalloc_Tagalloc` 时传入 [OSMT_PAGEABLE](https://developer.apple.com/documentation/kernel/osmt_pageable)，而不是 [OSMT_DEFAULT](https://developer.apple.com/documentation/kernel/osmt_default)。

虽然 I/O Kit 通常超出本文范围，为求完整，这里仍给出 I/O Kit 内存管理例程。
通常不应在 I/O Kit 外部使用 I/O Kit 例程。同样，也不应直接从 I/O Kit 使用 Mach 分配例程，
因为 I/O Kit 对这些例程提供了更贴合 I/O Kit 开发模型的抽象。

I/O Kit 包含以下内核内存分配例程：

```
void *IOMalloc(vm_size_t size);
void *IOMallocAligned(vm_size_t size, vm_size_t alignment);
void *IOMallocContiguous(vm_size_t size, vm_size_t alignment,
            IOPhysicalAddress *physicalAddress);
void *IOMallocPageable(vm_size_t size, vm_size_t alignment);
void IOFree(void *address, vm_size_t size);
void IOFreeAligned(void *address, vm_size_t size);
void IOFreeContiguous(void *address, vm_size_t size);
void IOFreePageable(void *address, vm_size_t size);
```

这些例程大多是对 Mach 分配函数相对透明的包装，但有两个主要区别。
第一，调用者不必知道正在修改哪一个内存映射。第二，由于内部记账原因，每个分配调用都有独立的释放调用。

[IOMallocContiguous](https://developer.apple.com/documentation/kernel/1575289-iomalloccontiguous) 和 [IOMallocAligned](https://developer.apple.com/documentation/kernel/1575291-iomallocaligned) 函数与其 Mach 基础稍有不同。
[IOMallocAligned](https://developer.apple.com/documentation/kernel/1575291-iomallocaligned) 直接调用 Mach VM，以支持任意的（2 的幂）数据对齐，而不是根据对象大小对齐。
[IOMallocContiguous](https://developer.apple.com/documentation/kernel/1575289-iomalloccontiguous) 增加了额外参数 `PhysicalAddress`。若该指针不是 `NULL`，会通过该指针返回物理地址。
使用 Mach 函数取得物理地址则需要单独调用函数。

除内核扩展可用的例程外，修改 Mach 内核本身时还有其他可调用的内存分配函数。
Mach 例程为分配和释放内存提供相对直接的接口。它们是在 I/O Kit 外分配内存的首选机制。
BSD 还提供 `_MALLOC` 和 `_FREE`，可用于内核的 BSD 部分。

这些例程不能强制将给定物理地址映射到虚拟地址。但若确实需要这种映射，你很可能正在编写设备驱动程序，
此时应使用 I/O Kit 例程，而不是 Mach 例程。

这些函数大多围绕 `vm_offset_t` 类型设计，它是一个与指针等宽的整数。实际上可将它们视为指针，
但要注意：根据用法，它们未必指向内核地址空间中的数据。

以下是一些常用的 Mach 内存分配例程：

```
kern_return_t kmem_alloc(vm_map_t map, vm_offset_t *addrp, vm_size_t  size);
void kmem_free(vm_map_t map, vm_offset_t addr, vm_size_t size);
kern_return_t mem_alloc_aligned(vm_map_t map, vm_offset_t *addrp,
            vm_size_t size);
kern_return_t kmem_alloc_wired(vm_map_t map, vm_offset_t *addrp,
            vm_size_t size);
kern_return_t kmem_alloc_pageable(vm_map_t map, vm_offset_t *addrp,
            vm_size_t size);
kern_return_t kmem_alloc_contig(vm_map_t map, vm_offset_t *addrp,
            vm_size_t size, vm_offset_t mask, int flags);
```

这些函数都以映射为第一个参数。除非需要在不同映射中分配内存，否则应为该参数传入 `kernel_map`。

除 `kmem_alloc_pageable` 外，所有 `kmem_alloc` 函数都会分配已锁定内存。
`kmem_alloc_pageable` 会创建适当的 VM 结构，但不会用物理内存支持该区域。
例如，创建新地址映射时，可将此函数与 `vm_map_copyout` 结合使用。实际中它很少使用。

`kmem_alloc_aligned` 函数按 `size` 参数的值分配对齐内存，该值必须是 2 的幂。

`kmem_alloc_wired` 函数等同于 `kmem_alloc`，适合不能被分页换出的数据结构。
它并非严格必要；但若明确需要将某些数据锁定到内存，使用 `kmem_alloc_wired` 更易找到代码的这些部分。

`kmem_alloc_contig` 函数会尝试分配物理连续内存块。这并非总能成功，且即使分配很短，
也需要完整排序系统空闲链表。系统启动后，此排序可能造成长时间延迟，特别是在 RAM 很多的系统中。
通常不应使用该函数。

`kmem_free` 函数用于释放由任一 `kmem_alloc` 函数分配的对象。
与标准 C 的 [free](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/free.3.html#//apple_ref/doc/man/3/free) 函数不同，`kmem_free` 需要对象长度。
若分配的不是固定大小对象（例如 `sizeof struct foo`），你可能需要进行额外记账，因为必须释放整个对象，而不能只释放其中一部分。

[下一页](../../../../en/documentation/Darwin/Kernel%20Programming%20Guide/Mach%20Scheduling%20and%20Thread%20Interfaces.md)[上一页](../../../../en/documentation/Darwin/Kernel%20Programming%20Guide/Mach%20Overview.md)
