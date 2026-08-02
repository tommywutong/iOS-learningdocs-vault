---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/vm/vm.html
archived_at: '2026-07-15T07:23:14.219055Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Mach%20Scheduling%20and%20Thread%20Interfaces.md)[Previous](Mach%20Overview.md)

# Memory and Virtual Memory

This chapter describes allocating memory and
the low-level routines for modifying memory maps in the kernel.
It also describes a number of commonly used interfaces to the virtual
memory system. It does not describe how to make changes in paging
policy or add additional pagers. OS X does not support external
pagers, although
much of the functionality can be achieved in other ways, some of
which are covered at a high level in this chapter. The implementation
details of these interfaces are subject to change, however, and
are thus left undocumented.

With the exception of the section [Allocating Memory in the Kernel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgawugscejbeusssg),
this chapter is of interest only if you are writing file systems
or are modifying the virtual memory system itself.

The VM system
used in OS X is a descendent of Mach VM, which was created at Carnegie
Mellon University in the 1980s. To a large extent, the fundamental
design is the same, although some of the details are different,
particularly when enhancing the VM system. It does, however, support
the ability to request certain paging behavior through the use of _universal
page lists (UPLs)_. See [Universal Page Lists (UPLs)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgawugscejfdesq2h) for
more information.

The design of Mach VM centers around the concept of physical
memory being a cache for virtual memory.

At its highest level, Mach VM consists of address spaces and
ways to manipulate the contents of those address spaces from outside
the space. These address spaces are sparse and have a notion of
protections to limit what tasks
can access their contents.

At a lower level, the object level, virtual memory is seen
as a collection of VM objects and memory objects, each with a particular owner and
protections. These objects can be modified with object calls that
are available both to the task and (via the back end of the VM)
to the pagers.

The VM object is internal to the virtual memory system, and
includes basic information about accessing the memory. The memory
object, by contrast, is provided by the pager. The contents of the
memory associated with that memory object can be retrieved from
disk or some other backing store by exchanging messages with the
memory object. Implicitly, each VM object is associated with a given
pager through its memory object.

VM objects are cached with system pages (RAM), which can be
any power of two multiple of the hardware page size. In the OS X kernel, system pages are the same size as hardware pages. Each
system page is represented in a given address space by a map entry. Each
map entry has its own protection and inheritance. A given map entry
can have an inheritance of `shared`, `copy`,
or `none`. If a page is
marked `shared` in a given
map, child tasks share this page for reading and writing. If a page
is marked `copy`, child
tasks get a copy of this page (using copy-on-write). If a page is
marked `none`, the child’s
page is left unallocated.

VM objects are managed by the machine-independent VM system,
with the underlying virtual to physical mappings handled by the
machine-dependent _pmap
system_. The `pmap` system
actually handles page tables, translation lookaside buffers, segments,
and so on, depending on the design of the underlying hardware.

When a VM object is duplicated (for example,
the data pages from a process that has just called `fork`),
a _shadow object_ is created. A shadow object is initially
empty, and contains a reference to another object. When the contents
of a page are modified, the page is copied from the parent object
into the shadow object and then modified. When reading data from a
page, if that page exists in the shadow object, the page listed
in the shadow object is used. If the shadow object has no copy of
that page, the original object is consulted. A series of shadow
objects pointing to shadow objects or original objects is known
as a _shadow chain_.

Shadow chains can become arbitrarily long if an object is
heavily reused in a copy-on-write fashion. However, since `fork` is
frequently followed by [exec](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/exec.3.html#//apple_ref/doc/man/3/exec),
which replaces all of the material being shadowed, long chains are
rare. Further, Mach automatically garbage collects shadow objects,
removing any intermediate shadow objects whose pages are no longer
referenced by any (nondefunct) shadow object. It is even possible
for the original object to be released if it no longer contains
pages that are relevant to the chain.

The VM calls available to an application include `vm_map` and `vm_allocate`,
which can be used to map file data or anonymous memory into the
address space. This is possible only because the address space is
initially sparse. In general, an application can either map a file into
its address space (through file mapping primitives, abstracted by
BSD) or it can map an object (after being passed a handle to that
object). In addition, a task can change the protections of the objects
in its address space and can share those objects with other tasks.

In addition to the mapping and allocation aspects of virtual
memory, the VM system contains a number of other subsystems. These
include the back end (pagers) and the shared memory subsystem. There
are also other subsystems closely tied to VM, including the VM shared
memory server. These are described in [Other VM and VM-Related Subsystems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgawugscejjbemqsd).

Each Mach task has its own memory map. In Mach, this memory
map takes the form of an ordered doubly linked list. As described
in [OS X VM Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgawugsceivceoq2b),
each of these objects contains a list of pages and shadow references
to other objects.

In general, you should never need to access a memory map directly
unless you are modifying something deep within the VM system. The `vm_map_entry` structure
contains task-specific information about an individual mapping along
with a reference to the backing object. In essence, it is the glue
between an VM object and a VM map.

While the details of this data structure are beyond the scope
of this document, a few fields are of particular importance.

The field `is_submap` is
a Boolean value that tells whether this map entry is a normal VM object
or a _submap_.
A submap is a collection of mappings that is part of a larger map. Submaps
are often used to group mappings together for the purpose of sharing
them among multiple Mach tasks, but they may be used for many purposes.
What makes a submap particularly powerful is that when several tasks
have mapped a submap into their address space, they can see each
other’s changes, not only to the contents of the objects in the
map, but to the objects themselves. This means that as additional
objects are added to or deleted from the submap, they appear in
or disappear from the address spaces of all tasks that share that
submap.

The field `behavior` controls
the paging reference behavior of a specified range in a given map.
This value changes how pageins are clustered. Possible values are `VM_BEHAVIOR_DEFAULT`, `VM_BEHAVIOR_RANDOM`, `VM_BEHAVIOR_SEQUENTIAL`,
and `VM_BEHAVIOR_RSEQNTL`,
for default, random, sequential, or reverse-sequential pagein ordering.

The `protection` and `max_protection` fields
control the permissions on the object. The `protection` field
indicates what rights the task currently has for the object, while
the `max_protection` field
contains the maximum access that the current task can obtain for
the object.

You might use the `protection` field
when debugging shared memory. By setting the protection to be read-only,
any inadvertent writes to the shared memory would cause an exception.
However, when the task actually needs to write to that shared region,
it could increase its permissions in the `protection` field
to allow writes.

It would be a security hole if a task could increase
its own permissions on a memory object arbitrarily, however. In
order to preserve a reasonable security model, the task that owns a
memory object must be able to limit the rights granted to a subordinate
task. For this reason, a task is not allowed to increase its protection
beyond the permissions granted in `max_protection`.

Possible values for `protection` and `max_protection` are
described in detail in `xnu/osfmk/mach/vm_prot.h`.

Finally, the `use_pmap` field
indicates whether a submap’s low-level mappings should be shared
among all tasks into which the submap is mapped. If the mappings
are not shared, then the structure of the map is shared among all
tasks, but the actual contents of the pages are not.

For example, shared libraries are handled with
two submaps. The read-only shared code section has `use_pmap` set
to true. The read-write (nonshared) section has `use_pmap` set
to false, forcing a clean copy of the library’s `DATA` segment
to be mapped in from disk for each new task.

The OS X VM system provides an abstraction known as a _named
entry_. A
named entry is nothing more than a handle to a shared object or
a submap.

Shared memory support in OS X is achieved by sharing objects
between the memory maps of various tasks. Shared memory objects
must be created from existing VM objects by calling `vm_allocate` to
allocate memory in your address space and then calling `mach_make_memory_entry_64` to
get a handle to the underlying VM object.

The handle returned by `mach_make_memory_entry_64` can
be passed to `vm_map` to
map that object into a given task’s address space. The handle
can also be passed via IPC or other means to other tasks so that
they can map it into their address spaces. This provides the ability
to share objects with tasks that are not in your direct lineage,
and also allows you to share additional memory with tasks in your
direct lineage after those tasks are created.

The other form of named entry, the submap, is used to group
a set of mappings. The most common use of a submap is to share mappings
among multiple Mach tasks. A submap can be created with `vm_region_object_create`.

What makes a submap particularly powerful is that when several
tasks have mapped a submap into their address space, they can see
each other’s changes to both the data and the structure of the
map. This means that one task can map or unmap a VM object in another task’s
address space simply by mapping or unmapping that object in the
submap.

A universal page list, or UPL, is a data structure used when
communicating with the virtual memory system. UPLs can be used to
change the behavior of pages with respect to caching, permissions,
mapping, and so on. UPLs can also be used to push data into and pull
data from VM objects. The term is also often used to refer to the
family of routines that operate on UPLs. The flags used when dealing
with UPLs are described in `osfmk/mach/memory_object_types.h`.

The life cycle of a UPL looks like this:

1. A UPL is
   created based on the contents of a VM object. This UPL includes
   information about the pages within that object.
2. That UPL is modified in some way.
3. The changes to the UPL are either committed (pushed back to
   the VM system) or aborted, with [ubc_upl_commit](https://developer.apple.com/documentation/kernel/1463702-ubc_upl_commit) or [ubc_upl_abort](https://developer.apple.com/documentation/kernel/1463754-ubc_upl_abort),
   respectively.

If you have a control handle for a given VM object (which
generally means that you are inside a pager), you can use `vm_object_upl_request` to
get a UPL for that object. Otherwise, you must use the `vm_map_get_upl` call.
In either case, you are left with a handle to the UPL.

When a pagein is requested, the pager receives a list of pages
that are locked against the object, with certain pages set to not
valid. The pager must either write data into those pages or must
abort the transaction to prevent invalid data in the kernel. Similarly
in pageout, the kernel must write the data to a backing store or
abort the transaction to prevent data loss. The pager may also elect
to bring additional pages into memory or throw additional pages
out of memory at its discretion.

Because pagers can be used both for virtual memory and for
memory mapping of file data, when a pageout is requested, the data
may need to be freed from memory, or it may be desirable to keep
it there and simply flush the changes to disk. For this reason,
the flag `UPL_CLEAN_IN_PLACE` exists
to allow a page to be flushed to disk but not removed from memory.

When a pager decides to page in or out additional pages, it
must determine which pages to move. A pager can request all of the
dirty pages by setting the `RETURN_ONLY_DIRTY` flag. It
can also request all pages that are not in memory using the `RETURN_ONLY_ABSENT` flag.

There is a slight problem, however. If a given page is marked
as `BUSY` in the UPL, a
request for information on that page would normally block. If the
pager is doing prefetching or preflushing, this is not desirable,
since it might be blocking on itself or on some other pager that
is blocked waiting for the current transaction to complete. To avoid
such deadlock, the UPL mechanism provides the `UPL_NOBLOCK` flag.
This is frequently used in the anonymous pager for requesting free
memory.

The flag `QUERY_OBJECT_TYPE` can
be used to determine if an object is physically contiguous and to
get other properties of the underlying object.

The flag `UPL_PRECIOUS` means
that there should be only one copy of the data. This prevents having
a copy both in memory and in the backing store. However, this breaks
the adjacency of adjacent pages in the backing store, and is thus
generally not used to avoid a performance hit.

The flag `SET_INTERNAL` is
used by the BSD subsystem to cause all information about a UPL to
be contained in a single memory object so that it can be passed
around more easily. It can only be used if your code is running
in the kernel’s address space.

Since this handle can be used for multiple small transactions
(for example, when mapping a file into memory block-by-block), the
UPL API includes functions for committing and aborting changes to
only a portion of the UPL. These functions are [upl_commit_range](https://developer.apple.com/documentation/kernel/1538509-upl_commit_range) and [upl_abort_range](https://developer.apple.com/documentation/kernel/1538505-upl_abort_range),
respectively.

To aid in the use of UPLs for handling multi-part transactions,
the [upl_commit_range](https://developer.apple.com/documentation/kernel/1538509-upl_commit_range) and [upl_abort_range](https://developer.apple.com/documentation/kernel/1538505-upl_abort_range) calls
have a flag that causes the UPL to be freed when there are no unmodified
pages in the UPL. If you use this flag, you must be very careful
not to use the UPL after all ranges have been committed or aborted.

Finally, the function `vm_map_get_upl` is
frequently used in file systems. It gets the underlying VM object
associated with a given range within an address space. Since this returns
only the first object in that range, it is your responsibility to
determine whether the entire range is covered by the resulting UPL
and, if not, to make additional calls to get UPLs for other objects.
Note that while the `vm_map_get_upl` call
is against an address space range, most UPL calls
are against a `vm_object`.

From the context of the kernel (_not_ from
a KEXT), there are two maps that you will probably need to deal
with. The first is the kernel map. Since your code is executing
in the kernel’s address space, no additional effort is needed
to use memory referenced in the kernel map. However, you may need
to add additional mappings into the kernel map and remove them when
they are no longer needed.

The second map of interest is the memory map for a given task.
This is of most interest for code that accepts input from user programs,
for example a `sysctl` or
a Mach RPC handler. In nearly all cases, convenient wrappers provide
the needed functionality, however.

Most of these functions are based around the `vm_offset_t` type, which is a pointer-sized integer. In effect, you can think of them as pointers, with the caveat that they are not necessarily pointers to data in the kernel’s address space, depending on usage.

The low-level VM map API includes the following functions:

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

The function `vm_map_copyin` copies
data from an arbitrary (potentially non–kernel) memory map into
a copy list and returns the copy list pointer in `copy_result`.
If something goes wrong and you need to throw away this intermediate
object, it should be freed with `vm_map_copy_discard`.

In order to actually get the data from the copy list, you
need to overwrite a memory object in the kernel’s address space
with `vm_map_copy_overwrite`. This overwrites
an object with the contents of a copy list. For most purposes, the
value passed for `interruptible` should be `FALSE`,
and `pmap` should be `NULL`.

Copying data from the kernel to user space is exactly the
same as copying data from user space, except that you pass `kernel_map` to `vm_map_copyin` and
pass the user map to `vm_map_copy_overwrite`.
In general, however, you should avoid doing this, since you could end
up with a task’s memory being fragmented into lots of tiny objects,
which is undesirable.

Do _not_ use `vm_map_copyout` when
copying data into an existing user task’s address map. The function `vm_map_copyout` is
used for filling an unused region in an address map. If the region
is allocated, then `vm_map_copyout` does
nothing. Because it requires knowledge of the current state of the
map, it is primarily used when creating a new address map (for example,
if you are manually creating a new process). For most purposes,
you do not need to use `vm_map_copyout`.

The functions `vm_map_wire` and `vm_map_unwire` can
be used to wire and unwire portions of an address map. If you set
the argument `user_wire` to `TRUE`,
then the page can be unwired from user space. This should be set
to `FALSE` if you are about
to use the memory for I/O or for some other operation that cannot
tolerate paging. In `vm_map_wire`,
the argument `access_type` indicates
the types of accesses that should not be allowed to generate a page fault.
In general, however, you should be using `vm_wire` to
wire memory.

As mentioned earlier, this information is presented strictly
for use in the heart of the kernel. You cannot use anything
in this section from a kernel extension.

There are two additional VM subsystems: pagers and the working
set detection subsystem. In addition, the VM shared memory server
subsystem is closely tied to (but is not part of) the VM subsystem.
This section describes these three VM and VM-related subsystems.

OS X has three basic pagers: the vnode pager, the default
pager (or anonymous pager), and the device pager. These are used
by the VM system to actually get data into the VM objects that underlie
named entries. Pagers are linked into the VM system through a combination
of a subset of the old Mach pager interface and UPLs.

The default pager is what most people
think of when they think of a VM system. It is responsible for moving
normal data into and out of the backing store. In addition, there
is a facility known as the dynamic pager that
sits on top of the default pager and handles the creation and deletion
of backing store files. These pager files are filled with data in
clusters (groups of pages).

When the total fullness of the paging file pool reaches a
high–water mark, the default pager asks the dynamic pager to allocate
a new store file. When the pool drops below its low water mark,
the VM system selects a pager file, moves its contents into other
pager files, and deletes it from disk.

The vnode pager has a 1:1 (onto) mapping between
objects in VM space and open files (vnodes). It is used for memory
mapped file I/O. The vnode pager is generally hidden behind calls
to BSD file APIs.

The device pager allows you to map non–general-purpose
memory with the cache characteristics required for that memory (_WIMG_). Non–general–purpose
memory includes physical addresses that are mapped onto hardware
other than main memory—for example, PCI memory, frame buffer memory,
and so on. The device pager is generally hidden behind calls to
various I/O Kit functions.

To improve performance, OS X has a subsystem known as
the working set detection subsystem. This subsystem is called on
a VM fault; it keeps a profile of the fault behavior of each task
from the time of its inception. In addition, just before a page
request, the fault code asks this subsystem which adjacent pages
should be brought in, and then makes a single large request to the
pager.

Since files on disk tend to have fairly good locality, and
since address space locality is largely preserved in the backing
store, this provides a substantial performance boost. Also, since
it is based upon the application’s previous behavior, it tends
to pull in pages that would probably have otherwise been needed
later. This occurs for all pagers.

The working set code works well once it is established. However,
without help, its performance would be the baseline performance
until a profile for a given application has been developed. To overcome
this, the first time that an application is launched in a given user
context, the initial working set required to start the application
is captured and stored in a file. From then on, when the application
is started, that file is used to seed the working set.

These working set files are established on a per-user basis.
They are stored in `/var/vm/app_profile` and
are only accessible by the super-user (and the kernel).

The VM shared memory server
subsystem is a BSD service that is closely tied to VM, but is not
part of VM. This server provides two submaps that are used for shared
library support in OS X. Because shared libraries contain
both read-only portions (text segment) and read-write portions (data
segment), the two portions are treated separately to maximize efficiency.
The read-only portions are completely shared between tasks, including
the underlying `pmap` entries.
The read-write portions share a common submap, but have different
underlying data objects (achieved through copy-on-write).

The three functions exported by the VM shared memory server
subsystem should only be called by `dyld`.
Do not use them in your programs.

The function `load_shared_file` is
used to load a new shared library into the system. Once such a file
is loaded, other tasks can then depend on it, so a shared library
cannot be unshared. However, a new set of shared regions can be
created with `new_system_shared_regions` so
that no new tasks will use old libraries.

The function `reset_shared_file` can
be used to reset any changes that your task may have made to its
private copy of the data section for a file.

Finally, the function `new_system_shared_regions` can
be used to create a new set of shared regions for future tasks.
New regions can be used when updating prebinding with new shared
libraries to cause new tasks to see the latest libraries at their
new locations in memory. (Users of old shared libraries will still
work, but they will fall off the pre-bound path and will perform
less efficiently.) It can also be used when dealing with private libraries
that you want to share only with your task’s descendents.

This section explains issues that some developers may see
when using their drivers in Panther or later. These changes were
necessitated by a combination of hardware and underlying OS changes;
however, you may see problems resulting from the changes even on
existing hardware.

There are three basic areas of change in OS X v10.3. These
are:

- `IOMemoryDescriptor` changes
- VM system (`pmap`)
  changes
- Kernel dependency changes

These are described in detail in the sections that follow.

To allow existing device drivers to work with upcoming 64-bit
system architectures, a number of changes were required. To explain
these, a brief introduction to PCI bus bridges is needed.

When a PCI device needs to perform a data transaction to or
from main memory, the device driver calls a series of functions
intended to prepare this memory for I/O. In an architecture where
both the device drivers and the memory subsystem use 32-bit addressing,
everything just works, so long as the memory doesn't get paged out
during the I/O operation. As kernel memory is generally not pageable,
the preparation is largely superfluous.

On a system whose memory subsystem uses 64-bit addressing,
however, this becomes a bit of a problem. Because the hardware devices
on the PCI bus can only handle 32-bit addresses, the device can
only “see” a 4 gigabyte aperture into the (potentially much larger)
main memory at any given time.

There are two possible solutions for this problem. The easy
(but slow) solution would be to use “bounce buffers”. In such
a design, device drivers would copy data into memory specifically
allocated within the bottom 4 gigs of memory. However, this incurs
a performance penalty and also puts additional constraints on the
lower 4 gigs of memory, causing numerous problems for the VM system.

The other solution, the one chosen in Apple's 64-bit implementation,
is to use address translation to “map” blocks of memory into
the 32-bit address space of the PCI devices. While the PCI device
can still only see a 4 gig aperture, that aperture can then be non-contiguous,
and thus bounce buffers and other restrictions are unnecessary.
This address translation is done using a part of the memory controller
known as DART, which stands for Device Address Resolution Table.

This introduces a number of potential problems, however. First,
physical addresses as seen by the processor no longer map 1:1 onto
the addresses as seen by PCI devices. Thus, a new term, I/O addresses,
is introduced to describe this new view. Because I/O addresses and physical
addresses are no longer the same, the DART must keep a table of
translations to use when mapping between them. Fortunately, if your
driver is written according to Apple guidelines (using only documented
APIs), this process is handled transparently.

When your driver calls `IOMemoryDescriptor``::``prepare`,
a mapping is automatically injected into the DART. When it calls `IOMemoryDescriptor``::``release` ,
the mapping is removed. If you fail to do this, your driver could
experience random data corruption or panics.

Because the DART requires different caching for reads and
writes, the DMA direction is important on hardware that includes
a DART. While you may receive random failures if the direction
is wrong in general (on any system), if you attempt to call WriteBytes
on a memory region whose DMA direction is set up for reading, you
will cause a kernel panic on 64-bit hardware.

If you attempt to perform a DMA transaction to unwired (user)
memory, on previous systems, you would only get random crashes,
panics, and data corruption. On machines with a DART, you will
likely get no data whatsoever.

As a side-effect of changes in the memory subsystem, OS X is much more likely to return physically contiguous page ranges
in memory regions. Historically, OS X returned multi-page
memory regions in reverse order, starting with the last page and moving
towards the first page. The result of this was that multi-page
memory regions essentially never had a contiguous range of physical
pages.

Because of the increased probability of seeing physically
contiguous blocks of memory in a memory region, this change may
expose latent bugs in some drivers that only show up when handling
contiguous ranges of physical pages, which could result in incorrect
behavior or panics.

Note that the problems mentioned above are caused by bugs
in the drivers, and could result in problems on older hardware prior
to Panther. These issues are more likely to occur in Panther and
later versions of OS X, however, because of the new hardware designs
and the OS changes that were made to support those designs.

In Panther, as a result of the changes described in detail
in the section on PCI address translation, physical addresses obtained
directly from the `pmap` layer
have no useful purpose outside the VM system itself. To prevent
their inadvertent use in device drivers, the `pmap` calls
are no longer available from kernel extensions.

A few drivers written prior to the addition of the `IOMemoryDescriptor` class
still use `pmap` calls
to get the physical pages associated with a virtual address. Also,
a few developers have looked at the `IOMemoryDescriptor` implementation
and chosen to obtain addresses directly from the `pmap`
layer to remove what was perceived as an unnecessary abstraction
layer.

Even without removing access to the `pmap` calls,
these drivers would not function on systems with a DART (see the
PCI section above for info on DARTs). To better emphasize this upcoming
failure, Panther will cause these drivers to fail to load with an
undefined symbol error (generally for `pmap_extract` )
even on systems without a DART.

Beginning in Panther, device drivers that declare a dependency
on version 7 (the Panther version) of the I/O Kit will no longer
automatically get symbols from Mach and BSD. This change was made
to discourage I/O Kit developers from relying on symbols that are
not explicitly approved for use in the I/O Kit.

Existing drivers are unaffected by this change. This change
only affects you if you explicitly modify your device driver to
declare a dependency on version 7 of the I/O Kit to take advantage
of new I/O Kit features.

As described above, some device drivers may require minor
modifications to support Panther and higher. Apple has made every
effort to ensure compatibility with existing device drivers to the
greatest extent possible, but a few drivers may break. If your driver breaks,
you should first check to see if your driver includes any of the
bugs described in the previous sections. If it does not, contact
Apple Developer Technical Support for additional debugging suggestions.

As with most things in the OS X kernel, there are a number of ways to allocate memory. The choice of routines depends both on the location of the calling routine and on the reason for allocating memory. In general, you should use Mach routines for allocating memory unless you are writing code for use in the I/O Kit, in which case you should use I/O Kit routines.

The `<libkern/OSMalloc.h>` header defines the following routines for kernel memory allocation:

- [OSMalloc](https://developer.apple.com/documentation/kernel/1398447-osmalloc)—allocates a block of memory.
- [OSMalloc_noblock](https://developer.apple.com/documentation/kernel/1398431-osmalloc_noblock)—allocates a block of memory, but immediately returns NULL if the request would block.
- [OSMalloc_nowait](https://developer.apple.com/documentation/kernel/1398445-osmalloc_nowait)—same as `OSMalloc_noblock`.
- [OSFree](https://developer.apple.com/documentation/kernel/1398441-osfree)—releases memory allocated with any of the `OSMalloc` variants.
- [OSMalloc_Tagalloc](https://developer.apple.com/documentation/kernel/1398437-osmalloc_tagalloc)—allows you to create a unique tag for your memory allocations. You `must` create at least one tag before you can use any of the `OSMalloc` functions.
- [OSMalloc_Tagfree](https://developer.apple.com/documentation/kernel/1398439-osmalloc_tagfree)—releases a tag allocated with OSMalloc_Tagalloc. (You _must_ release all allocations associated with that tag before you call this function.)

For example, to allocate and free a page of wired memory, you might write code like this:

```c
#include <libkern/OSMalloc.h>
#define MYTAGNAME "com.apple.mytag"

...

OSMallocTag mytag = OSMalloc_Tagalloc(MYTAGNAME, OSMT_DEFAULT);
void *datablock = OSMalloc(PAGE_SIZE_64, mytag);

...

OSFree(datablock, PAGE_SIZE_64, mytag);
```

To allocate a page of pageable memory, pass [OSMT_PAGEABLE](https://developer.apple.com/documentation/kernel/osmt_pageable) instead of [OSMT_DEFAULT](https://developer.apple.com/documentation/kernel/osmt_default) in your call to `OSMalloc_Tagalloc`.

Although the I/O Kit is generally beyond the scope of this document, the I/O Kit memory management routines are presented here for completeness. In general, I/O Kit routines should not be used outside the I/O Kit. Similarly, Mach allocation routines should not be directly used from the I/O Kit because the I/O Kit has abstractions for those routines that fit the I/O Kit development model more closely.

The I/O Kit includes the following routines for kernel memory allocation:

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

Most of these routines are relatively transparent wrappers around the Mach allocation functions. There are two major differences, however. First, the caller does not need to know which memory map is being modified. Second, they have a separate free call for each allocation call for internal bookkeeping reasons.

The functions [IOMallocContiguous](https://developer.apple.com/documentation/kernel/1575289-iomalloccontiguous) and [IOMallocAligned](https://developer.apple.com/documentation/kernel/1575291-iomallocaligned) differ somewhat from their Mach underpinnings. [IOMallocAligned](https://developer.apple.com/documentation/kernel/1575291-iomallocaligned) uses calls directly to Mach VM to add support for arbitrary (power of 2) data alignment, rather than aligning based on the size of the object. [IOMallocContiguous](https://developer.apple.com/documentation/kernel/1575289-iomalloccontiguous) adds an additional parameter, `PhysicalAddress`. If this pointer is not `NULL`, the physical address is returned through this pointer. Using Mach functions, obtaining the physical address requires a separate function call.

In addition to the routines available to kernel extensions, there are a number of other functions you can call to allocate memory when you are modifying the Mach kernel itself. Mach routines provide a relatively straightforward interface for allocating and releasing memory. They are the preferred mechanism for allocating memory outside of the I/O Kit. BSD also offers `_MALLOC` and `_FREE`, which may be used in BSD parts of the kernel.

These routines do not provide for forced mapping of a given physical address to a virtual address. However, if you need such a mapping, you are probably writing a device driver, in which case you should be using I/O Kit routines instead of Mach routines.

Most of these functions are based around the `vm_offset_t` type, which is a pointer-sized integer. In effect, you can think of them as pointers, with the caveat that they are not necessarily pointers to data in the kernel’s address space, depending on usage.

These are some of the commonly used Mach routines for allocating memory:

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

These functions all take a map as the first argument. Unless
you need to allocate memory in a different map, you should pass `kernel_map` for
this argument.

All of the `kmem_alloc` functions
except `kmem_alloc_pageable` allocate
wired memory. The function `kmem_alloc_pageable` creates
the appropriate VM structures but does not back the region with
physical memory. This function could be combined with `vm_map_copyout` when creating
a new address map, for example. In practice, it is rarely used.

The function `kmem_alloc_aligned` allocates
memory aligned according to the value of the `size` argument,
which must be a power of 2.

The function `kmem_alloc_wired` is
synonymous with `kmem_alloc` and
is appropriate for data structures that cannot be paged out. It
is not strictly necessary; however, if you explicitly need certain
pieces of data to be wired, using `kmem_alloc_wired` makes
it easier to find those portions of your code.

The function `kmem_alloc_contig` attempts
to allocate a block of physically contiguous memory. This is not
always possible, and requires a full sort of the system free list
even for short allocations. After startup, this sort can cause long
delays, particularly on systems with lots of RAM. You should generally
not use this function.

The function `kmem_free` is
used to free an object allocated with one of the `kmem_alloc` functions.
Unlike the standard C [free](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/free.3.html#//apple_ref/doc/man/3/free) function, `kmem_free` requires
the length of the object. If you are not allocating fixed-size objects
(for example, `sizeof struct foo`),
you may have to do some additional bookkeeping, since you must free
an entire object, not just a portion of one.

[Next](Mach%20Scheduling%20and%20Thread%20Interfaces.md)[Previous](Mach%20Overview.md)

