---
title: 'Friday Q&A 2013-10-11: Why Registers Are Fast and RAM Is Slow'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-10-11-why-registers-are-fast-and-ram-is-slow.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e68f1f7d4b66b6ad'
translated: false
---

> 原文：[Friday Q&A 2013-10-11: Why Registers Are Fast and RAM Is Slow](https://www.mikeash.com/pyblog/friday-qa-2013-10-11-why-registers-are-fast-and-ram-is-slow.html)　·　mikeash.com Friday Q&A

Posted at 2013-10-11 14:14 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-10-25: NSObject: the Class and the Protocol](https://www.mikeash.com/pyblog/friday-qa-2013-10-25-nsobject-the-class-and-the-protocol.html)  
Previous article: [Friday Q&A 2013-09-27: ARM64 and You](https://www.mikeash.com/pyblog/friday-qa-2013-09-27-arm64-and-you.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hardware](https://www.mikeash.com/pyblog/?tag=hardware) [memory](https://www.mikeash.com/pyblog/?tag=memory)

Friday Q&A 2013-10-11: Why Registers Are Fast and RAM Is Slow

by [Mike Ash](https://www.mikeash.com/)

**Distance**  
Let's start with distance. It's not necessarily a big factor, but it's the most fun to analyze. RAM is farther away from the CPU than registers are, which can make it take longer to fetch data from it.

Take a 3GHz processor as an extreme example. The speed of light is roughly [one foot per nanosecond](https://www.google.com/search?q=speed+of+light+in+nanoseconds+per+foot), or about 30cm per nanosecond for you metric folk. Light can only travel about four inches in time of a single clock cycle of this processor. That means a roundtrip signal can only get to a component that's two inches away or less, and that assumes that the hardware is perfect and able to transmit information at the speed of light in vacuum. For a desktop PC, that's pretty significant. However, it's much less important for an iPhone, where the clock speed is much lower (the 5S runs at 1.3GHz) and the RAM is right next to the CPU.

**Cost**  
Much as we might wish it wasn't, cost is always a factor. In software, when trying to make a program run fast, we don't go through the entire program and give it equal attention. Instead, we identify the hotspots that are most critical to performance, and give them the most attention. This makes the best use of our limited resources. Hardware is similar. Faster hardware is more expensive, and that expense is best spent where it'll make the most difference.

Registers get used extremely frequently, and there aren't a lot of them. There are only about 6,000 bits of register data in an A7 (32 64-bit general-purpose registers plus 32 128-bit floating-point registers, and some miscellaneous ones). There are about 8 billion bits (1GB) of RAM in an iPhone 5S. It's worthwhile to spend a bunch of money making each register bit faster. There are literally a million times more RAM bits, and those eight billion bits pretty much have to be as cheap as possible if you want a $650 phone instead of a $6,500 phone.

Registers use an [expensive](http://en.wikipedia.org/wiki/Register_file#Array) design that can be read quickly. Reading a register bit is a matter of activating the right transistor and then waiting a short time for the register hardware to push the read line to the appropriate state.

Reading a RAM bit, on the other hand, is more involved. A bit in the DRAM found in any smartphone or PC consists of a single capacitor and a single transistor. The capacitors are extremely small, as you'd expect given that you can fit eight billion of them in your pocket. This means they carry a very small amount of charge, which makes it hard to measure. We like to think of digital circuits as dealing in ones and zeroes, but the analog world comes into play here. The read line is pre-charged to a level that's halfway between a one and a zero. Then the capacitor is connected to it, which either adds or drains a tiny amount of charge. An amplifier is used to push the charge towards zero or one. Once the charge in the line is sufficiently amplified, the result can be returned.

The fact that a RAM bit is only one transistor and one tiny capacitor makes it extremely cheap to manufacture. Register bits contain more parts and thereby cost much more.

There's also a lot more complexity involved just in figuring out what hardware to talk to with RAM because there's so much more of it. Reading from a register looks like:

1. Extract the relevant bits from the instruction.
2. Put those bits onto the register file's read lines.
3. Read the result.

Reading from RAM looks like:

1. Get the pointer to the data being loaded. (Said pointer is probably in a register. This already encompasses all of the work done above!)
2. Send that pointer off to the MMU.
3. The MMU translates the virtual address in the pointer to a physical address.
4. Send the physical address to the memory controller.
5. Memory controller figures out what bank of RAM the data is in and asks the RAM.
6. The RAM figures out particular chunk the data is in, and asks that chunk.
7. Step 6 may repeat a couple of more times before narrowing it down to a single array of cells.
8. Load the data from the array.
9. Send it back to the memory controller.
10. Send it back to the CPU.
11. Use it!

Whew.

**Dealing With Slow RAM**  
That sums up why RAM is so much slower. But how does the CPU deal with such slowness? A RAM load is a single CPU instruction, but it can take potentially hundreds of CPU cycles to complete. How does the CPU deal with this?

First, just how long does a CPU take to execute a single instruction? It can be tempting to just assume that a single instruction executes in a single cycle, but reality is, of course, much more complicated.

Back in the good old days, when men wore their sheep proudly and the nation was undefeated in war, this was not a difficult question to answer. It wasn't one-instruction-one-cycle, but there was at least some clear correspondence. The Intel 4004, for example, took either 8 or 16 clock cycles to execute one instruction, depending on what that instruction was. Nice and understandable. Things gradually got more complex, with a wide variety of timings for different instructions. Older CPU manuals will give a list of how long each instruction takes to execute.

Now? Not so simple.

Along with increasing clock rates, there's also been a long drive to increase the number of instructions that can be executed per clock cycle. Back in the day, that number was something like 0.1 of an instruction per clock cycle. These days, it's up around 3-4 on a good day. How does it perform this wizardry? When you have a billion or more transistors per chip, you can add in a lot of smarts. Although the CPU might be executing 3-4 instructions per clock cycle, that doesn't mean each instruction takes 1/4th of a clock cycle to execute. They still take at least one cycle, often more. What happens is that the CPU is able to maintain multiple instructions in flight at any given time. Each instruction can be broken up into pieces: load the instruction, decode it to see what it means, gather the input data, perform the computation, store the output data. Those can all happen on separate cycles.

On any given CPU cycle, the CPU is doing a bunch of stuff simultaneously:

1. Fetching potentially several instructions at once.
2. Decoding potentially a completely different set of instructions.
3. Fetching the data for potentially yet another different set of instructions.
4. Performing computations for yet more instructions.
5. Storing data for yet more instructions.

But, you say, how could this possibly work? For example:

```
    add x1, x1, x2
    add x1, x1, x3
```

These can't possibly execute in parallel like that! You need to be finished with the first instruction before you start the second!

It's true, that can't possibly work. That's where the smarts come in. The CPU is able to analyze the instruction stream and figure out which instructions depend on other instructions and shuffle things around. For example, if an instruction after those two adds doesn't depend on them, the CPU could end up executing that instruction _before_ the second add, even though it comes later in the instruction stream. The ideal of 3-4 instructions per clock cycle can only be achieved in code that has a lot of independent instructions.

What happens when you hit a memory load instruction? First of all, it is definitely going to take _forever_, relatively speaking. If you're really lucky and the value is in L1 cache, it'll only take a few cycles. If you're unlucky and it has to go all the way out to main RAM to find the data, it could take literally hundreds of cycles. There may be a lot of thumb-twiddling to be done.

The CPU will try not to twiddle its thumbs, because that's inefficient. First, it will try to anticipate. It may be able to spot that load instruction in advance, figure out what it's going to load, and initiate the load before it really starts executing the instruction. Second, it will keep executing other instructions while it waits, as long as it can. If there are instructions after the load instruction that don't depend on the data being loaded, they can still be executed. Finally, once it's executed everything it can and it absolutely cannot proceed any further without that data it's waiting on, it has little choice but to stall and wait for the data to come back from RAM..

**Conclusion**

1. RAM is slow because there's a ton of it.
2. That means you have to use designs that are cheaper, and cheaper means slower.
3. Modern CPUs do crazy things internally and will happily execute your instruction stream in an order that's wildly different from how it appears in the code.
4. That means that the first thing a CPU does while waiting for a RAM load is run other code.
5. If all else fails, it'll just stop and wait, and wait, and wait, and wait.

That wraps things up for today. As always, Friday Q&A is driven by reader suggestions, so if you have a topic you'd like to see covered or a question you'd like to see answered, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-10-11-why-registers-are-fast-and-ram-is-slow.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
