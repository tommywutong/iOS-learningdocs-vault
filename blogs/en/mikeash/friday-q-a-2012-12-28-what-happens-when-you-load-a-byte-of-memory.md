---
title: 'Friday Q&A 2012-12-28: What Happens When You Load a Byte of Memory'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-12-28-what-happens-when-you-load-a-byte-of-memory.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:622ecbb76fa64f68'
translated: false
---

> 原文：[Friday Q&A 2012-12-28: What Happens When You Load a Byte of Memory](https://www.mikeash.com/pyblog/friday-qa-2012-12-28-what-happens-when-you-load-a-byte-of-memory.html)　·　mikeash.com Friday Q&A

Posted at 2012-12-28 14:45 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-01-11: Mach Exception Handlers](https://www.mikeash.com/pyblog/friday-qa-2013-01-11-mach-exception-handlers.html)  
Previous article: [Friday Q&A 2012-12-14: Objective-C Pitfalls](https://www.mikeash.com/pyblog/friday-qa-2012-12-14-objective-c-pitfalls.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hardware](https://www.mikeash.com/pyblog/?tag=hardware) [memory](https://www.mikeash.com/pyblog/?tag=memory)

Friday Q&A 2012-12-28: What Happens When You Load a Byte of Memory

by [Mike Ash](https://www.mikeash.com/)

**Code**  
Let's start with the code that loads the byte of memory. In C, it would look something like this:

```
    char *addr = ...;
    char value = *addr;
```

On `x86-64`, this compiles to something like:

```
    movsbl (%rdi),%eax
```

This instructs the CPU to load the byte located at the address stored in `%rdi` into the `%eax` register. On ARM, the compiler produces:

```
    ldrsb.w r0, [r0]
```

Although the instruction name is different, the effect is basically the same. It loads the byte located at the address stored in `r0`, and puts the value into `r0`. (The compiler is reusing `r0` here, since the address isn't needed anymore.)

Now that the CPU has its instruction, the software is done. Well, maybe.

**Instruction Decoding and Execution**  
I don't want to go too in depth with how the CPU actually executes code in general. In short, the CPU loads the above instruction from memory and decodes it to figure out the opcode and operands. Once it sees that it's a load instruction, it issues the memory load at the appropriate address.

**Virtual Memory**  
On most hardware you're likely to program for today, and on any Apple platform from the past couple of decades, the system uses virtual memory. In short, virtual memory disconnects the memory addresses seen by your program from the physical memory addresses of the actual RAM in your computer. In other words, when your program accesses address `42`, that might actually access the physical RAM address `977305`.

This mapping is done by _page_. Each page is a 4kB chunk of memory. The overhead of tracking virtual address mappings for every byte in memory would be far too great, so pages are mapped instead. They're small enough to provide decent granularity, but large enough to not incur too much overhead in maintaining the mapping.

Modern virtual memory systems also have the ability to set permissions on a page. A page may be readable, writeable, or executable, or some combination thereof. If the program tries to do something with a page that it isn't allowed, or tries to access a page that has no mapping at all, the program is suspended and a fault is raised with the operating system. The OS can then take further action, such as killing the program and generating a crash report, which is what happens when you experience the common `EXC_BAD_ACCESS` error.

The hardware that handles this work is called the Memory Management Unit, or MMU. The MMU intercepts all memory accesses and remaps the address according to the current page mappings.

The first thing that happens when the CPU loads a byte of memory is to hand the address to the MMU for translation. (This is not always true. On some CPUs, there is a layer of cache that comes before the MMU. However, the overall principle remains.)

The first thing the MMU does with the address is slice off the bottom 12 bits, leaving a plain page address. 2^12 equals 4096, so the bottom 12 bits describe the address's location within its page. Once the rest of the address is remapped, the bottom 12 bits can be added on to generate the full physical address.

With the page address in hand, the MMU consults the Translation Lookaside Buffer, or TLB. The TLB is a cache for page mappings. If the page in question has been accessed recently, the TLB will remember the mapping, and quickly return the physical page address, at which point the MMU's work is done.

When the TLB does not contain an entry for the given page, this is called a TLB miss, and the entry must be found by searching the entire page table. The page table is a chunk of memory that describes every page mapping in the current process. Most commonly, the page table is laid out in memory by the OS in a special format that the MMU can understand directly. Following a TLB miss, the MMU searches the page table for the appropriate entry. If it finds one, it loads it into the TLB and performs the remapping.

On some architectures, the page table mapping is left entirely up to the OS. When a TLB miss occurs, the CPU passes control to the OS, which is then responsible for looking up the mapping and filling the TLB with it. This is more flexible but much slower, and isn't found much in modern hardware.

If no entry is found in the page table, that means the given address doesn't exist in RAM at all. The CPU informs the OS, which then decides how to handle the situation. If the OS doesn't think that address is valid, it terminates the program and you get an `EXC_BAD_ACCESS`. In some cases, the OS does think the address is valid, but just doesn't have the data in RAM. This can happen if the data has been swapped out to disk, is part of a memory mapped file, or is freshly allocated with backing memory being provided on demand. In these cases, the OS loads the appropriate data into RAM, adds an entry to the page table, and then lets the MMU translate the virtual address into a physical address now that the backing data is available.

**Cache**  
With the address in hand, the CPU consults its memory cache. In days of yore, the CPU would talk directly to RAM. However, CPU speeds have increased faster than memory speeds, and that's no longer practical. If a modern CPU had to talk directly to modern RAM for every memory access, our computers would slow to a relative crawl.

The cache is a hardware map from a set of memory addresses to memory contents. Caches are organized into cache lines, which are typically in the region of 32-128 bytes each. Each entry in the cache holds an address and a single cache line corresponding to that address. When loading data from the cache, it checks to see if the requested address exists in the cache, and if so, returns the appropriate data from that address's cache line.

There are typically several levels of cache. Due to hardware design constraints, larger caches are necessarily slower. By having multiple levels, a small, fast cache can be checked first, with slower, larger caches used later to avoid the cost of fetching from RAM. The CPU first checks with the L1 cache, which is the first level. This cache is small, typically around 16-64kB. If it contains the data in question, then the memory load is complete! Since that's boring, we'll assume the caches don't contain the data being loaded here.

Next up is the L2 cache. This is bigger, generally anywhere from 256kB to several megabytes. In some CPUs, the L2 cache is the last level, and these typically have larger L2 caches. Other CPUs have an L3 cache as well, in which case the L2 is usually smaller, and it's supplemented by a large L3 cache, usually several megabytes, with some high performance chips having up to 20MB of L3 cache.

Once all levels of cache have been tried, if none of them contain the necessary data, it's time to try main memory. Because caches work with entire cache lines, the entire cache line is loaded from main memory at once, even though we're only loading a single byte. This greatly increases efficiency in the common case of accessing other nearby memory, since subsequent nearby loads can come from cache, at the cost of wasting time when memory use is scattered.

**Memory**  
It's finally time to start querying RAM. The CPU has been waiting quite a while by this point, and will have to wait a long time more before it gets the data it wants.

The load is handed off to the memory controller, which is the bit of hardware that actually knows how to talk to RAM. On a lot of modern hardware, the memory controller is integrated directly into the CPU, while on some systems it's part of a separate chip called the "northbridge".

The memory controller then starts loading data from RAM. Modern SDRAM transfers 64 bits of data at a time, so several transfers have to be done to fill the entire cache line being requested.

The memory controller places the load address on the address pins of the RAM and waits for the data to be returned. Internally, the RAM uses the values on the address pins to activate a row of memory cells, whose contents are then exposed on the RAM's output pins.

RAM is not instantaneous, and there's an appreciable delay between when the memory controller requests an address and when the data is available, on the order of 10 nanoseconds in current hardware. It takes more time to perform the subsequent loads needed for the cache line, but the loads can be pipelined, so total transfer time is maybe 50% more.

As the memory controller obtains data from RAM, it hands that data back to the caches, which store it in case other data from the same cache line is needed soon. Finally, the requested byte is handed to the CPU, which places the data into the register requested by the instruction. At last, after all of this work, the CPU can get on with running the code that needed that byte of data.

**Consequences**  
There are a lot of practical consequences that result from how all of this stuff works. In particular, memory acccess is _slow_, relatively speaking. It's amazing that your computer can do all of the above work literally tens of millions of times per second, but it can do other things literally billions of times per second. Everything is relative.

The total time required for all of this, assuming a TLB hit (the fast case for the MMU) is a couple of dozen nanoseconds. On a 2GHz CPU, that could mean something like 50 clock cycles with the potential to execute perhaps 150 instructions in that time. That's a lot. A TLB miss may double or triple this latency number.

Modern CPUs are pipelined and parallelized. This means that they will likely see the need for the memory read ahead of time and initiate the load at that point, softening the blow. Parallel execution means that the CPU will probably be able to continue executing some code _after_ the load instruction while waiting for the load, especially code that doesn't depend on the loaded value. However, this stuff has limits, and finding 150 instructions that can be executed while waiting for RAM is a tall order. You're almost certain to hit a point where program execution has to stop and wait for the memory load to complete.

Incidentally, this is where hyperthreading gains its advantage. Instead of having an entire CPU core just idle while waiting for RAM, hyperthreading lets it switch over to a completely different thread of execution and run code from _that_ instead, so that it can still get useful work done while it waits.

Access patterns are _key_ to performance. Discussions about micro-optimization tend to center on using some instructions rather than others, avoiding divisions, etc. Relatively few talk about memory access patterns. However, it doesn't matter how optimized your individual instructions are if they're operating on memory that's loaded in a way that isn't kind to the memory system. Saving a few cycles here and there is meaningless if you're waiting dozens of cycles for every new piece of data to load. For example, this is why, although it's the more natural way to express it, you should never write loops to access image data like this:

```
    for(int x = 0; x < width; x++)
        for(int y = 0; y < height; y++)
            // use the pixel at x, y
```

Images are typically laid out in contiguous rows, and this loop does _not_ take advantage of that fact. It accesses columns, only coming back to the next pixel in the first row after loading the entire first column. This causes cache and TLB misses. This loop will be vastly slower than if you iterate over rows first, then columns:

```
    for(int y = 0; y < height; y++)
        for(int x = 0; x < width; x++)
            // use the pixel at x, y
```

In many cases, the top loop with fast code in the loop body will be massively outperformed by the bottom loop with slow code in the loop body, simply because memory access delays can be so punishing.

To make things even worse, profilers, such as Apple's Time Profiler in Instruments, aren't good at showing these delays. They'll tell you what instructions took time, but because of the pipelined, parallel nature of modern CPUs, the instruction that takes the hit of the memory load may not be the actual load instruction. The CPU will hit the load instruction, mark its destination register as not having its data yet, and move on. When the CPU hits an instruction that actually needs that register's value, _then_ it will stop and wait. The clue here is when the first instruction in a sequence of manipulations on the same value takes _far_ longer than the rest, and far longer than it should. For example, if you have code that does `load`, `add`, `mul`, `add`, and the profiler says that the first `add` takes the vast majority of the time, this is likely to be a memory delay, not actually a slow `add`.

**Conclusion**  
Modern computers operate on time scales that are difficult to envision. To a human, the time required for a single CPU cycle and the time required to perform a hard disk seek are both indistingusihably instantaneous, yet they vary by many orders of magnitude. The computer is an incredibly complicated system that requires a huge number of things to happen in order to load a single chunk of data from memory. Knowing what goes on in the hardware when this happens is fascinating and can even help write better code. It's even more incredible once you think that this complicated set of operations happens literally millions of times every second in the computer you're using to read this.

That's it for today. Check back next time for another exploration of the trans-mundane. If you somehow didn't already know, Friday Q&A is driven by reader submissions. By "reader" I mean _you_, so if you have a topic that you'd like to see covered, please [send it in](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-12-28-what-happens-when-you-load-a-byte-of-memory.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
