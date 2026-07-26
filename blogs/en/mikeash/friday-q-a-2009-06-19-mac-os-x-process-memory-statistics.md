---
title: 'Friday Q&A 2009-06-19: Mac OS X Process Memory Statistics'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-06-19-mac-os-x-process-memory-statistics.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:86bbd14518b06bf4'
translated: false
---

> 原文：[Friday Q&A 2009-06-19: Mac OS X Process Memory Statistics](https://www.mikeash.com/pyblog/friday-qa-2009-06-19-mac-os-x-process-memory-statistics.html)　·　mikeash.com Friday Q&A

Posted at 2009-06-19 13:48 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-06-26: Type Qualifiers in C, Part 1](https://www.mikeash.com/pyblog/friday-qa-2009-06-26-type-qualifiers-in-c-part-1.html)  
Previous article: [Friday Q&A 2009-06-05: Introduction to Valgrind](https://www.mikeash.com/pyblog/friday-qa-2009-06-05-introduction-to-valgrind.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-06-19: Mac OS X Process Memory Statistics

by [Mike Ash](https://www.mikeash.com/)

**Memory Structure**  
 Before I can discuss what the stats mean, I first have to discuss just how memory actually works on a modern operating system. If you already know the difference between physical memory and virtual address space, understand how file mapping works, etc., then feel free to skip ahead.

**Hardware**  
 At the hardware level, memory is physical chips accessed over a bus. Each byte of memory in those chips has a discrete physical address (although technically modern systems aren't usually byte-addressible, requiring larger chunks to be accessed).

Mediating access to the physical chips is the CPU's MMU (Memory Management Unit). The MMU is what allows for virtual memory. It maps between logical addresses coming from the CPU and physical addresses sitting out in physical RAM.

This gives the CPU a large virtual address space that doesn't necessarily correspond to the physical memory. (This space is 4GB in 32-bit, and a really big number in 64-bit.) Any given section of that address space can either be mapped to an arbitrary section of physical memory, or it can be left unmapped.

**OS**  
 What happens when a program tries to access memory that's unmapped? A hardware exception results, and the OS gets to take over.

A cleverly programmed OS (like, say, any halfway recent UNIX, or even Windows) can use this fact to do some interesting things. It could, say, maintain its own, more complicated mapping behind the scenes which says that a section of memory that's unmapped in hardware is actually mapped to a file on disk. Then when a hardware exception is raised for trying to access that section, the OS can read a chunk of the file into that spot and then let program execution continue. Now you have file mapping and (if you automatically _unmap_ little-used sections of memory and write their contents out to disk) swap.

Another clever thing is to map sections of two different processes' address spaces to the same chunk of physical memory. Now you have shared memory!

These techniques can be combined. For example, shared frameworks are typically loaded by mapping them into memory (allowing the OS to load them off of disk lazily). And they're then mapped into multiple processes at once, allowing them to use the same physical RAM for all processes instead of having a bunch of copies.

**Definitions**  
 Now that we know roughly how the stuff works, let's define some memory-related terms:

- memory which is located in physical RAM.
- memory which is only mapped into one process.
- memory which is mapped into multiple processes.
- the quantity of address space occupied by a particular section of virtual memory.
- the amount of actual physical memory occupied.

And with that, we can now see what the various fields in

mean, from looking at the man page and using these definitions:

- The amount of address space, local to this process, which corresponds to items currently present in physical RAM.
- The amount of address space, shared between this process and at least one other, which corresponds to items currently present in physical RAM.
- The total amount of physical RAM used by this process. (This is

  equal to

  +

  because they measure address space, but this measures actual memory.)
- The amount of address space in the process mapped to items which are not shared with other processes.
- The total amount of address space in the process that's mapped to anything.

It should also be noted that these numbers are derived from an accounting system which does not always completely correspond to the true numbers, especially when distinguishing between shared and private memory. They're generally close enough to be useful, at least.

**Interpretation**  
 By this point you're probably scratching your head and wondering which number you should look at to see how much memory your program is using. Trouble is, there isn't one!

As you've seen, memory usage is highly complicated, and none of these numbers answers that question. In fact, with things like file mapping and shared memory, it's not even a question that really makes sense.

That's not to say that these numbers are useless, though. Even though nothing directly corresponds to what you'd really like to know, there are still some interesting facts you can obtain.

For 32-bit programs, **VSIZE** can be very important. This is because 32-bit programs have a hard 4GB limit on virtual address space, and in this modern world it's not all that hard to hit that limit. Once you do, memory allocations will begin to fail and your program will probably crash shortly afterwards. If your **VSIZE** is near the 4GB limit, you're chewing up too much address space on something.

(For 64-bit programs, the virtual address space is virtually unlimited, and so this column is of little use. For example, garbage collected apps in 64-bit immediately allocate a 64GB chunk of virtual address space just to make the accounting easier. This has no bearing on your actual memory usage and is completely harmless, although it tends to freak out users who go groveling around Activity Monitor.)

**RPRVT** can be useful as a rough indicator for watching if the total amount of memory your program has allocated is going up or down. This is dangerous to rely on, however. Because this only tracks resident memory, if your program has started to swap then your **RPRVT** will no longer increase, even though you're still allocating more and more memory. (To detect this, you can watch to see if **VPRVT** is going up, and the number of pageouts listed at the top of the screen is going up.) Conversely, the memory allocator doesn't always give memory back to the system right away, so this number may not go down if your program is freeing memory.

Overall, be careful not to rely too much on these statistics. For more precise information to track down leaks and excessive memory allocation, tools like the `leaks` command and the ObjectAlloc instrument are much better.

**Conclusion**  
 That brings us to the end of this edition of Friday Q&A. Now you should understand what all those weird numbers mean in `top` (except, potentially, for all of the ones that aren't related to memory) and how best to use and not use them.

Come back next week (I hope) for another exciting edition. Be sure to send along your ideas for topics to discuss. Without your contributions, Friday Q&A could not exist. Post them in the comments or [e-mail them directly to me](mailto:mike@mikeash.com).

Friday Q&A would like to acknowledge Ed Wynne's important role in providing technical advice for this week's post.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
