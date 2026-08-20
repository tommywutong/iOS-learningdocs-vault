---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Host-Common.html
archived_at: '2026-07-15T07:31:00.029845Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Filesystem](Filesystem.md#apple-izuwyzltpfzxizln),
Up: [Host Config](Host-Config.md#apple-jbxxg5bninxw4ztjm4)

---

### 14.1 Host Common

Some things are just not portable, even between similar operating systems,
and are too difficult for autoconf to detect. They get implemented using
hook functions in the file specified by the host_hook_obj
variable in `config.gcc`.

— Host Hook: void __HOST_HOOKS_EXTRA_SIGNALS__ (void)
> This host hook is used to set up handling for extra signals. The most
> common thing to do in this hook is to detect stack overflow.

— Host Hook: void __\*__ HOST_HOOKS_GT_PCH_GET_ADDRESS (size_t size, int fd)
> This host hook returns the address of some space that is likely to be
> free in some subsequent invocation of the compiler. We intend to load
> the PCH data at this address such that the data need not be relocated.
> The area should be able to hold size bytes. If the host uses
> `mmap`, fd is an open file descriptor that can be used for
> probing.

— Host Hook: int __HOST_HOOKS_GT_PCH_USE_ADDRESS__ (void \* address, size_t size, int fd, size_t offset)
> This host hook is called when a PCH file is about to be loaded.
> We want to load size bytes from fd at offset
> into memory at address. The given address will be the result of
> a previous invocation of `HOST_HOOKS_GT_PCH_GET_ADDRESS`.
> Return −1 if we couldn't allocate size bytes at address.
> Return 0 if the memory is allocated but the data is not loaded. Return 1
> if the hook has performed everything.
>
> If the implementation uses reserved address space, free any reserved
> space beyond size, regardless of the return value. If no PCH will
> be loaded, this hook may be called with size zero, in which case
> all reserved address space should be freed.
>
> Do not try to handle values of address that could not have been
> returned by this executable; just return −1. Such values usually
> indicate an out-of-date PCH file (built by some other GCC executable),
> and such a PCH file won't work.

— Host Hook: size_t __HOST_HOOKS_GT_PCH_ALLOC_GRANULARITY__ (void);
> This host hook returns the alignment required for allocating virtual
> memory. Usually this is the same as getpagesize, but on some hosts the
> alignment for reserving memory differs from the pagesize for committing
> memory.
