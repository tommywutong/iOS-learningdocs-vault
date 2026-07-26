---
title: 'Nibblesort: Adventures in Optimization'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2015/05/Nibblesort/'
original_language: en
published: 2015-05-09
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:896114ab07150d79'
translated: false
---

> 原文：[Nibblesort: Adventures in Optimization](https://belkadan.com/blog/2015/05/Nibblesort/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [AlterConf SF/Oakland](https://belkadan.com/blog/2015/02/AlterConf/)

[Recommendations](https://belkadan.com/blog/2015/11/Recommendations/) »

« [“Skip the FFI”](https://belkadan.com/blog/2015/01/Skip-the-FFI/?tag=compilers)

[Recommendations](https://belkadan.com/blog/2015/11/Recommendations/?tag=compilers) »

« [Quick Look in TextMate](https://belkadan.com/blog/2011/06/Quick-Look-in-TextMate/?tag=source-code)

[\> go east](https://belkadan.com/blog/2019/08/go-east/?tag=source-code) »

## [Nibblesort: Adventures in Optimization](#)

A few months ago compiler researcher [John Regehr](https://twitter.com/johnregehr) held a [low-level optimization contest](http://blog.regehr.org/archives/1213) for a silly problem: sort the [nibbles](http://en.wikipedia.org/wiki/Nibble) in an arbitrary 64-bit number:

> The problem is to sort the 4-bit pieces of a 64-bit word with (unsigned) smaller values towards the small end of the word. The nibble sort of 0xbadbeef is 0xfeedbba000000000. The function you implement will perform this sorting operation on a buffer of 1024 64-bit integers.

I decided to enter the contest because I don’t usually work on low-level optimization, either writing hand-tuned code or working on compiler transformations to make “normal” code execute in a more efficient way. I eventually submitted an entry that did pretty well (top half of the non-[SIMD](https://www.kernel.org/pub/linux/kernel/people/geoff/cell/ps3-linux-docs/CellProgrammingTutorial/BasicsOfSIMDProgramming.html) entries), and learned several “morals” about optimization along the way.

This post will walk through the progress of my entry from “all right, I guess” to “actually that’s pretty fast”, detailing both what the various implementations are doing and the thought processes behind them. I’ve attempted to make it fairly accessible—aiming for it to be understandable to anyone who’s comfortable reading C code—but several years as a compiler developer may have led to certain things being taken for granted. (If you spot any of these, please [let me know](https://twitter.com/UINT_MIN/) and I’ll update the post.) It’s also rather long, so feel free to read part of it and come back to it later.

1. The Reference Implementation
2. Bucket Sort
3. Building the Result Value
4. Avoiding Branches
5. Unroll Loops Manually
6. Avoid Memory Access?
7. Do Less Work
8. Under the Hood
9. Registers
10. Preserving Information
11. The Magic of XOR
12. The Winning Solution
13. Epilogue

### The Reference Implementation

John provided a simple, slow implementation of a [selection sort](http://en.wikipedia.org/wiki/Selection_sort) for us to use as a reference.

```
static inline int read_nibble(uint64_t w, int i) {
  assert(i >= 0 && i < 16);
  uint64_t res = w >> (i * 4);
  return res & 0xf;
}

static inline void write_nibble(uint64_t *w, int i, int v) {
  assert(i >= 0 && i < 16);
  uint64_t mask = 0xf;
  mask <<= (i * 4);
  *w &= ~mask;
  uint64_t prom = v;
  prom <<= (i * 4);
  *w |= prom;
}

uint64_t nibble_sort_word(uint64_t arg) {
  for (int i = 0; i < 16; ++i) {
    int min = i;
    for (int j = i+1; j < 16; ++j) {
      if (read_nibble(arg, j) < read_nibble(arg, min))
        min = j;
    }
    if (min != i) {
      int tmp = read_nibble(arg, i);
      write_nibble(&arg, i, read_nibble(arg, min));
      write_nibble(&arg, min, tmp);
    }
  }
  return arg;
}
```

It’s not exactly doing any _unnecessary_ work, but even with the optimizer on it’s doing a lot of moderately interesting bitwise manipulation that’s just going to take time. Hey, at least it’s not [bubble sort](http://en.wikipedia.org/wiki/Bubble_sort).

This reference implementation took about 400-500µs on my machine to sort 1024 64-bit words. That’s already not too slow; simply writing 1024 newlines using [`puts`](http://en.cppreference.com/w/cpp/io/c/puts) took over twice as long.[1](#fn:buffer) But we can do much, much better.

### Bucket Sort

Sorting normally requires [Ω(N log N)](http://en.wikipedia.org/wiki/Big_O_notation) operations to complete. (The proof of this is actually [rather clever](http://planetmath.org/lowerboundforsorting).) However, you might be able to do better if you know more about your data.

In this case N is rather low, but I wasn’t thinking about that. Instead, I focused on the fact that a nibble can only have 16 values. When you know what values can appear in your data (and there aren’t too many of them), you don’t actually have to compare them. Instead, you just go through each value and toss it into the correct “bucket”, keeping a count of how many you’ve seen. At the end, you can just go through the _buckets_ in order and write out the answer. This is called a [bucket sort](http://en.wikipedia.org/wiki/Bucket_sort), and since in our case we have only one value per bucket, it’s really just a [counting sort](http://en.wikipedia.org/wiki/Counting_sort).

Here’s my initial implementation:[2](#fn:actually)

```
void nibble_sort_bucket(uint64_t buf[static 1024]) {
  for (unsigned _=0; _<1024; _++) {
    uint64_t word = buf[_];
    unsigned counts[16] = {};

    for (int i = 0; i < 16; ++i)
      ++counts[read_nibble(word, i)];

    uint64_t result = 0;
    for (int i = 0xF; i >= 0; --i) {
      while (counts[i] > 0) {
        result <<= 4;
        result |= i;
        --counts[i];
      }
    }

    buf[_] = result;
  }
}
```

This was already more than twice as fast! That told me bucket sort was a viable strategy, and it was now time to take a look at the specific implementation.

**Moral: If you’re trying to optimize something, don’t take the current algorithm for granted.** Is there another way to get to the same answer?

### Building the Result Value

The code above was the simplest version of the bucket sort algorithm I could implement—which is a good thing: get the logic correct before trying to micro-optimize. But it’s doing more work than it needs to even before we get to the real “micro” stuff. In particular, take a look at this inner loop in constructing the result:

```
while (counts[i] > 0) {
  result <<= 4;
  result |= i;
  --counts[i];
}
```

What this is doing is taking our current working result value, say `0x0000_0000_0000_wxyz`, and shifting in a single nibble with the label for the current bucket `i`, creating `0x0000_0000_000w_xyzi`. Once we’ve gone over all the buckets, all sixteen nibbles will be in the right place.

The problem is that if `counts[0xC]` is, say, 10, it will take ten loops to fill in all the `C` nibbles, even though they’re all just `C`. It’s easy to shift the current result value over to fit all of the values:

```
result <<= 4 * counts[i];
```

But how can we fill in the correct value in the now-empty space? Well, let’s start with something simpler.

```
uint64_t allBitsSet = ~0ull; // 0xFFFF_FFFF_FFFF_FFFF
uint64_t repeatedOnes = allBitsSet / 0xF; // 0x1111_1111_1111_1111
uint64_t repeatedNibbles = repeatedOnes * i; // 0xiiii_iiii_iiii_iiii
```

This generates a value of the form `0xCCCC_CCCC_CCCC_CCCC`, or whatever the current value of `i` is. We don’t actually want 16 Cs, but it’s a start.

When all you have is a hammer, sometimes you have to treat things like nails. C’s bit-shift operators `<<` and `>>` fill in any extra bits with zeros, at least if you’re working with unsigned integers. That means shifting `repeatedNibbles` by N is the same thing as replacing N of the nibbles with 0, either on the right or left of the number. So if we want to _keep_ N values in a 64-bit (16-nibble) value, we can shift by `16 - N`.

So the final code looks like this:

```
result <<= 4 * counts[i];
uint64_t repeatedOnes = (~0ull) / 0xF;
uint64_t repeatedNibbles = repeatedOnes * i;
repeatedNibbles >>= 4 * (16 - counts[i]);
result |= repeatedNibbles;
```

Except now we have a problem. If `counts[i]` is 0, we end up shifting all 16 nibbles off the end of the value. According to the C standard, that’s [undefined behavior](http://blog.regehr.org/archives/213), and the resulting program is allowed to do whatever it likes, from not shifting at all, to performing an arbitrary system call (“erasing your hard drive”), to producing 0 like I’d like it to.

Fortunately, the fix here is easy: skip the whole thing if `counts[i]` is 0.

```
void nibble_sort_building_result_better(uint64_t buf[static 1024]) {
  for (unsigned _=0; _<1024; _++) {
    uint64_t word = buf[_];
    unsigned counts[16] = {};

    for (int i = 0; i < 16; ++i)
      ++counts[read_nibble(word, i)];

    uint64_t result = 0;
    for (int i = 0xF; i >= 0; --i) {
      if (counts[i] == 0)
        continue;
      result <<= 4 * counts[i];
      uint64_t repeatedOnes = (~0ull) / 0xF;
      uint64_t repeatedNibbles = repeatedOnes * i;
      repeatedNibbles >>= 4 * (16 - counts[i]);
      result |= repeatedNibbles;
    }

    buf[_] = result;
  }
}
```

This brings us down to less than a third of the original run time.

**Moral: Do things in bulk when possible.**

### Avoiding Branches

I just casually stuck that `if (counts[i] == 0)` test into the loop, but when we’re trying to optimize at this level that could actually be really problematic. We’re not accessing any memory within the outer loop besides the array of counts, so the most expensive thing we can do is a branch, particularly one where both the “true” and “false” cases will come up in practice. That means the CPU can’t “predict” which path to take and speculatively start executing instructions along that path. It would help a lot if we could get rid of that branch…but to do that, we have to get rid of the undefined behavior.

Fortunately, there are some “clever” ways to do that.

```
void nibble_sort_no_branch(uint64_t buf[static 1024]) {
  for (unsigned _=0; _<1024; _++) {
    uint64_t word = buf[_];
    unsigned counts[16] = {};
    
    for (int i = 0; i < 16; ++i)
      ++counts[read_nibble(word, i)];
    
    uint64_t result = 0;
    for (int i = 0xF; i >= 0; --i) {
      result <<= 4 * counts[i];
      uint64_t repeatedOnes = (~0ull) / 0xF;
      uint64_t repeatedNibbles = (repeatedOnes * i) * !!counts[i]; // NEW
      repeatedNibbles >>= (4 * (16 - counts[i])) * !!counts[i]; // NEW
      result |= repeatedNibbles;
    }
    
    buf[_] = result;
  }
}
```

I put “clever” in quotes because this is where things cross the line from “fairly clear code” into “fairly obscure code”, i.e. we’re sacrificing readability and maintainability for performance. Most of the time this isn’t worth it, especially because in most cases the CPU isn’t going to be the limiting factor for your program. If you’ve determined, however, that it really is important to squeeze performance out of this particular function, here’s a way to eliminate branches. (It’s also something that gets asked on interview questions sometimes.)

How does this work? In C, the `!` operator produces `0` (for “false”) if its input is non-zero, and `1` (for true) if its input is zero. This is normally used for negating boolean values, but it can also give us either 0 or 1 from an integer value. In this case I put the operator twice, meaning `0` for an input of 0 and `1` for anything else. So now when the input is non-zero, I have two useless multiplications by 1; when the input is zero, `repeatedNibbles` is first multiplied by 0 (i.e. set to 0) and then shifted by 0 before being combined with the result value we’re building.

_Aside: At the time I wasn’t yet looking at the generated [LLVM IR](http://llvm.org/docs/LangRef.html#abstract) or assembly for my programs, but it turns out that [Clang](http://clang.llvm.org) is smart enough to optimize this multiplication-by-zero-or-one into an LLVM `select` instruction, which turns into a “conditional move” CMOV[N]EQ on my [x86](https://en.wikipedia.org/wiki/X86) CPU. So it’s still doing a test, but it’s not branching as a result of that test._

In this case, this almost doubled the speed of the computation once again, bringing us well under a sixth of the original time.

**Moral: Branches are more expensive than simple computation,** at least if they can’t be predicted.

### Unroll Loops Manually

Okay, so branches are expensive, right? What about those loops? They’re both just going to run 16 times and then stop. Does it make more sense to just “[unroll](http://en.wikipedia.org/wiki/Loop_unrolling#A_simple_manual_example_in_C)” the loop into sixteen iterations?

```
static inline uint64_t shift_in(uint64_t result,
                                unsigned counts[static 16],
                                int which) {
  unsigned count = counts[which];
  result <<= 4 * count;
  uint64_t repeatedOnes = (~0ull) / 0xF;
  uint64_t repeatedNibbles = repeatedOnes * which * !!count;
  repeatedNibbles >>= 4 * (16 - count) * !!count;
  result |= repeatedNibbles;
  return result;
}

void nibble_sort_no_loops(uint64_t buf[static 1024]) {
  for (unsigned _=0; _<1024; _++) {
    uint64_t word = buf[_];
    unsigned counts[16] = {};

    ++counts[read_nibble(word, 0x0)];
    ++counts[read_nibble(word, 0x1)];
    ++counts[read_nibble(word, 0x2)];
    ++counts[read_nibble(word, 0x3)];
    ++counts[read_nibble(word, 0x4)];
    ++counts[read_nibble(word, 0x5)];
    ++counts[read_nibble(word, 0x6)];
    ++counts[read_nibble(word, 0x7)];
    ++counts[read_nibble(word, 0x8)];
    ++counts[read_nibble(word, 0x9)];
    ++counts[read_nibble(word, 0xA)];
    ++counts[read_nibble(word, 0xB)];
    ++counts[read_nibble(word, 0xC)];
    ++counts[read_nibble(word, 0xD)];
    ++counts[read_nibble(word, 0xE)];
    ++counts[read_nibble(word, 0xF)];

    uint64_t result = 0;
    result = shift_in(result, counts, 0xF);
    result = shift_in(result, counts, 0xE);
    result = shift_in(result, counts, 0xD);
    result = shift_in(result, counts, 0xC);
    result = shift_in(result, counts, 0xB);
    result = shift_in(result, counts, 0xA);
    result = shift_in(result, counts, 0x9);
    result = shift_in(result, counts, 0x8);
    result = shift_in(result, counts, 0x7);
    result = shift_in(result, counts, 0x6);
    result = shift_in(result, counts, 0x5);
    result = shift_in(result, counts, 0x4);
    result = shift_in(result, counts, 0x3);
    result = shift_in(result, counts, 0x2);
    result = shift_in(result, counts, 0x1);
    result = shift_in(result, counts, 0x0);

    buf[_] = result;
  }
}
```

Turns out it does! This shaves off another third or so of the time from the previous version. We’re down to about one-ninth of the original time!

I put “manually” in the title of this section because modern compilers will often decide to unroll loops themselves if they think it’s going to help. However, they might not unroll them _all the way_ like this, which is normally a good thing. (Imagine if it unrolled the _outer_ loop over all 1024 input values! That would not only result in a much larger executable file, but could actually result in execution being slower because the processor can’t keep the entire function in its cache.)

Note that this only works because my compiler inlines the helper functions `shift_in` and `read_nibble`—the overhead from a function call is normally bigger than any branch.[3](#fn:macros)

**Moral: Loops are also branches.** And branches are expensive.

Going forwards, I’m only going to show the function I’m changing, now that the logic has been split up into two separate functions.

### Avoid Memory Access?

At this point things are starting to get interesting. I’ve been focusing on the result generation, but that’s not everything that’s going on here, is it? There’s the whole part about counting the nibbles in the original word, which is going to result in touching 16 different counters.

Wait. 16? That’s _also_ the number of nibbles in a 64-bit word. (That’s why there are sixteen iterations in the first “loop”.) What if I packed the _counts_ into a single 64-bit value?

Well, first of all the actual counting would change:

```
uint64_t counts = 0;
counts += 1ull << (4 * read_nibble(word, 0x0));
// ...
```

And then extracting a particular count just becomes:

```
unsigned count = read_nibble(counts, which);
```

Finally, what happens if every nibble is the same? That will result in a count of 16 for one of the values, but that’s bigger than a single nibble can _store._ So instead, we’ll have to check up front if we’re dealing with that case. The expression I used for this is

```
word == ((word << 60) | (word >> 4))
```

which means “if I ‘rotate’ the nibbles in `word`, so that the rightmost one comes to the beginning and the others all slide down, do I get the original value back?”. Although “rotate” isn’t a single operation in C, most compilers will recognize it and compile it down to a single CPU instruction, so this should be fairly efficient. Apart from the branch, of course.

Doing this results in a run that’s about 15% _slower_ than the previous version.

Wait, what? Isn’t memory access supposed to be slow? What gives?

There are a few possible factors that might contribute to this result:

- The operations to access a particular count are now more complicated than they were before. Before we just pulled out a single 32-bit value and used it directly.
- We do have that extra branch, too, to check that the nibbles aren’t all the same.
- aren’t the cheapest instructions

  in most modern Intel-like CPUs.
- We might not have any registers to spare. (By the end of this exercise this turns out to not be the case, but even so.)

But the main thing is probably that I’m not accessing that much memory, and it’s all next to each other, and it’s not being accessed by multiple threads. (There are no other threads.) That means it’ll be pulled into the CPU’s cache and _stay there,_ which makes working with memory a much less expensive proposition.

**Moral: Memory access isn’t necessarily as expensive as you’re worried it is.** Caches work.

Aside: In my quest for more and more incremental improvements to my actual submission to the contest, I neglected to actually go back and test my false assumption. That means my final contest entry could have been faster if I hadn’t been hung up on being clever.

**Moral: Always test your assumptions.** Do a direct A/B comparison if at all possible.

### Do Less Work

This section is sort of a grab bag, but relies on noticing two places where we’re doing extra work after the fact rather than just doing the right thing up front.

The first involves the `shift_in` helper function:

```
// same as above
static inline uint64_t shift_in(uint64_t result,
                                unsigned counts[static 16],
                                int which) {
  unsigned count = counts[which];
  result <<= 4 * count;
  uint64_t repeatedOnes = (~0ull) / 0xF;
  uint64_t repeatedNibbles = repeatedOnes * which * !!count;
  repeatedNibbles >>= 4 * (16 - count) * !!count;
  result |= repeatedNibbles;
  return result;
}
```

Notice how every time we mention `count`, we’re either doing our “test for zero” trick or multiplying it by four. The compiler is smart enough to reuse the result from the first multiplication, but can we avoid the multiplication altogether? What if instead of storing counts, we store counts premultiplied by four?

```
counts[read_nibble(word, 0x0)] += 4;
counts[read_nibble(word, 0x1)] += 4;
// ...
counts[read_nibble(word, 0xF)] += 4;
```

```
// same as above
static inline uint64_t shift_in_scaled_counts(uint64_t result,
                                              unsigned counts[static 16],
                                              int which) {
  unsigned countTimesFour = counts[which];
  result <<= countTimesFour;
  uint64_t repeatedOnes = (~0ull) / 0xF;
  uint64_t repeatedNibbles = repeatedOnes * which * !!countTimesFour;
  repeatedNibbles >>= (64 - countTimesFour) * !!countTimesFour;
  result |= repeatedNibbles;
  return result;
}
```

Turns out that’s good for a solid 10% speedup right there.

The second place we’re doing extra work is when we build the result:

```
uint64_t result = 0;
result = shift_in(result, counts, 0xF);
result = shift_in(result, counts, 0xE);
// ...
```

The result value starts as 0, and we then shift in the correct number of `F` nibbles. Then we go on to `E`, `D`, etc. However, we know that unless the original value was zero, the leftmost nibble isn’t going to be `0`. That is, _all_ of the original nibbles from that initial assignment are going to disappear by the end of the result-building. We have two cases to consider:

- Then the lines from

  down to

  will build up the result, and the leftmost value will be one of them. We can’t really tell which one.
- Then we know what the leftmost nibble in the result will end up being:

  .

We can actually take this further. The point of that first `shift_in` line there is to guarantee that the rightmost N nibbles are all `F`, where “N” is `counts[0xF]`. We don’t actually care what the other nibbles are, because they’ll all be shifted out by the end of the result-building.

So let’s make _all_ the nibbles start out as `F`.

```
uint64_t result = ~0ull;
//result = shift_in(result, counts, 0xF);
result = shift_in(result, counts, 0xE);
// ...
```

The exact benefit of this change depends on which 64-bit values actually end up getting sorted, but it’s about another 1-2%—tiny, but we’ll take it.

**Moral: Don’t spend effort fixing up something to be in the right form if you can just start with it that way.**

Note: You might make a similar argument about the `0` case: mixing in `0` nibbles is unnecessary, because just doing a plain shift will put zeros there anyway! However, the compiler is smart enough to notice this as well, and eliminates all the work involving `repeatedNibbles` in the `0` case! Still, you could write it explicitly if you want:

```
//result = shift_in(result, counts, 0x0);
result <<= counts[0x0];
```

and it’ll come back later on.

It’d be nice if we could avoid spending the effort to _count_ the `0` and `F` nibbles, but since we don’t know ahead of time _which_ are the `0` and `F` nibbles, that’d be more trouble than it’s worth.

#### Under the Hood

At this point we’re _just_ above 10% of the reference implementation. I _really_ wanted to break 10%, so I decided to crack open the hood and see what’s really going on.

```
xcrun clang nibble_jrose.c -o nibble -O3 -DNDEBUG -S -o -
```

That `-S` at the end there tells my compiler ([Clang](http://clang.llvm.org)) to emit assembly, the textual form of actual machine code. If you want a fairly-long-but-practical guide on how to read assembly, check out [Gwynne Raskind’s guest post](https://mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html) on Mike Ash’s blog. I’ll try to keep things fairly simple here, but if you want you can just [skip all the assembly analysis](#underthehood-skip).

I looked at the various parts of the assembly to try to see what sort of work was being done. The counting part looks pretty good; just these four instructions repeated for most of it:

```
# Read third nibble.
movq    %rax, %rcx  # %rax is 'word'
shrq    $6, %rcx
andq    $60, %rcx
addl    $4, -112(%rbp,%rcx)
```

That’s essentially equivalent to this C code:

```
// Read third nibble.
uint64_t rcx = word;
rcx >>= 6;
rcx &= 0b00111100; // 0xF << 2
(rbp-112)[rcx] += 4;
```

There are two funny things here. The first is that we only shift by 6 instead of 8 to read the third nibble. Why’s that? Well, remember we’re storing the counts as `unsigned`, a type which is four bytes long. So the offset into the `counts` array needs to be multiplied by 4 to get a byte offset. The compiler is smart enough to fold this into the previous shifting-and-masking instructions.

The second funny thing is that `(rbp-112)`. That’s how a compiler refers to memory allocated on the stack. `rbp` is the “base pointer” for the function, i.e. where the stack was when we started. And on most modern machines, the stack grows down, so `rbp-112` refers to something allocated within this stack frame. In this case, it’s where the compiler put the start of the `counts` array: 112 bytes after the start of the frame.

Anyway, that code looks pretty good. What about the result-building? Well, that’s more interesting: it’s something like this:

```
# Write the 0xD nibbles.
movl    -60(%rbp), %ecx
shlq    %cl, %rsi  # %rsi is 'result'.

movl    $64, %eax
subl    %ecx, %eax

testl   %ecx, %ecx
movl    $0, %edx
movabsq $-2459565876494606883, %rcx ## imm = 0xDDDDDDDDDDDDDDDD
cmovneq %rcx, %rdx
cmoveq  %r13, %rax  # %r13 was initialized to 0 up above.

movb    %al, %cl
shrq    %cl, %rdx
orq     %rsi, %rdx  # Now %rdx is 'result'.
```

which looks like this in pseudo-C:

```
// Write the 0xD nibbles.
// %rcx/%ecx/%cl are all related, don't worry about it.
uint64_t rcx_countTimesFour = counts[0xD];
rsi_result >>= rcx_countTimesFour; // rsi is 'result' for now.

uint64_t rax_shift = 64; // %rax/%eax are related too.
rax_shift -= rcx_countTimesFour;

bool isZero = (rcx_countTimesFour == 0);
uint64_t rdx_repeated = 0; // %rdx/%edx are related too.
uint64_t rcx_repeated = 0xDDDDDDDDDDDDDDDD;
if (!isZero) rdx_repeated = rcx_repeated;
if (isZero) rax_shift = 0;

rcx_shift = rax_shift; // You can only shift by %cl/%ecx/%rcx.
rdx_repeated >>= rcx_shift;
rdx_repeated |= rsi_result; // Now rdx is 'result'.
```

(I’ve used new variables to indicate when a value of a register doesn’t actually depend on the previous value.)

That, um, looks like a lot of work! And there are also weird contortions to deal with the restriction on what registers can be used for what. We’ll come back to that. Meanwhile, is there any way we can compute the same value in fewer steps?

```
// same as above
static inline uint64_t shift_in_scaled_counts(uint64_t result,
                                              unsigned counts[static 16],
                                              int which) {
  unsigned countTimesFour = counts[which];
  result <<= countTimesFour;
  uint64_t repeatedOnes = (~0ull) / 0xF;
  uint64_t repeatedNibbles = repeatedOnes * which * !!countTimesFour;
  repeatedNibbles >>= (64 - countTimesFour) * !!countTimesFour;
  result |= repeatedNibbles;
  return result;
}
```

Let’s assume the handling of the original result—shift it over, then combine the new nibbles—is already as good as can be. In that case we’re just looking at how to bring in the new nibbles. That means looking at how we compute `repeatedNibbles`. In its final form, it’s something like `0x0000_0000_0000_DDDD`. What do we do to get that result?

1. Compute the shift amount: `64 - countTimesFour`
2. (The assembly part told us that there’s an efficient way to do this, but it’s still not free.)
3. to be 0: the other …

  .
4. by the shift amount.

It’d be really nice if we could stop worrying about shifting by 64 (remember, that’s [undefined behavior](http://blog.regehr.org/archives/213)!). But the only way to do that would be to stop shifting everything else _out._ Is there another way to go from `0xDDDD_DDDD_DDDD_DDDD` to `0x0000_0000_0000_DDDD`?

Okay, rather than shifting, how about masking? `0xDDDD_DDDD_DDDD_DDDD & 0x0000_0000_0000_FFFF` is also `0x0000_0000_0000_DDDD`. So if we can get `0x0000_0000_0000_FFFF` in less than three steps, we’ll be doing better than before. Turns out we can!

1. by

  . This produces a mask, e.g.

  .
2. .
3. with the inverted mask.

Or, in C code:

```
static inline uint64_t shift_in_separate_mask(uint64_t result,
                                              unsigned counts[static 16],
                                              int which) {
  unsigned countTimesFour = counts[which];
  result <<= countTimesFour;
  uint64_t mask = ~0ull; // NEW
  mask <<= countTimesFour; // NEW
  uint64_t repeatedOnes = (~0ull) / 0xF;
  uint64_t repeatedNibbles = repeatedOnes * which;
  repeatedNibbles &= ~mask; // NEW
  result |= repeatedNibbles;
  return result;
}
```

Rather than shifting `repeatedNibbles` to leave only the correct number of, say, `D`s, we instead use a separate mask. The mask starts as all-ones, and then we shift in the appropriate number of zeros for the new nibbles. The trick is then _inverting_ the mask, and applying that to our `repeatedNibbles` to get what we want.

Note: Because we’re no longer potentially shifting by 64, we don’t need the `!!count` trick to avoid undefined behavior anymore. That alone should save us some time.

This drops us to **9%** of the original run time! And the assembly went from 12 instructions to 8.

```
movb    -88(%rbp), %cl
shlq    %cl, %rsi

movq    $-1, %rdx
shlq    %cl, %rdx
notq    %rdx

movabsq $7378697629483820646, %rcx ## imm = 0x6666666666666666
andq    %rcx, %rdx
orq     %rsi, %rdx  # now %rdx is the result
```

You can see that indeed the `test` and `cmov` instructions are gone, as is the work to compute `64 - count`. In fact, it’s nearly line-for-line identical to the C version.

**Moral:** Actually just a smaller version of what we saw before: **try changing your algorithm** and **do less work.** Maybe someone else would have come up with this implementation as their first try, but in my case it made things a _lot_ faster. And we broke the 10% barrier!

I was pretty happy with this result, but couldn’t get away from a nagging notion that things could still be better. Where did that feeling come from?

### Registers

A CPU generally only operates on values immediately accessible to it, stored in a fixed set of “variables” called _registers._[4](#fn:memory) You might have noticed in the assembly snippet above that there are only three registers being used: `%cl`/`%rcx`, `%rsi`, and `%rdx`. But my CPU has a lot more named registers than that, more than ten. One of them has to be the loop counter, but what are the other registers being used for?

Well, looking up at the top of the assembly output shows this:

```
movabsq $8608480567731124087, %r13  ## imm = 0x7777777777777777
movabsq $-8608480567731124088, %r15 ## imm = 0x8888888888888888
movabsq $-7378697629483820647, %r12 ## imm = 0x9999999999999999
movabsq $-6148914691236517206, %rax ## imm = 0xAAAAAAAAAAAAAAAA
movabsq $-4919131752989213765, %rbx ## imm = 0xBBBBBBBBBBBBBBBB
movabsq $-3689348814741910324, %r8  ## imm = 0xCCCCCCCCCCCCCCCC
movabsq $-2459565876494606883, %r9  ## imm = 0xDDDDDDDDDDDDDDDD
movabsq $-1229782938247303442, %r10 ## imm = 0xEEEEEEEEEEEEEEEE
```

Wait, aren’t those the constants from the result-building? What are they doing up here, away from everything else? It turns out that the cost of _loading these constants_ is still noticeable: we can save a `mov` instruction in each step if the constant is already in a register. (We then use that register instead of %rcx when doing the `and`.) On the other hand, we can’t put _all_ the constants in registers, because then we run out of registers to do computation with.

(Aside: My particular compiler actually uses one more register in the loop than it really needs to, meaning it could have stuck one more constant at the top. But that’s not quite enough to help…)

Okay, so the people who work on [LLVM](http://llvm.org) are pretty smart, and even if they missed one register they still probably know what they’re doing. But there’s no way I’m going to be able to cram all 16 constants into registers in advance (well, 14, since we handled the `F` and `0` cases specially). However, we can be a bit smarter. The binary representation of `0xAA` is `0b10101010`. If we invert that, we get `0b01010101`, or `0x55`. So that means we can get all 14 constants by just storing the odd ones, and then do some bit-math to get the even ones back out.

Unfortunately, the compiler stymies us here: the same logic that turns `repeatedOnes * which` into a constant will recognize most attempts to derive `0x55` from `0xAA`. It’s also at the point where different compilers might do things very differently, and John’s contest rules actually specified a different compiler (GCC) on a different OS (Linux) with a different CPU (still 64-bit Intel, though). Short of writing assembly by hand, we’re probably stuck…

**Moral: Compilers may defeat your attempts to manually arrange code. These days, they’re right most of the time.**

…unless we change our algorithm.

### Preserving Information

At this point I was racking my brain trying to think of a way to shorten the result-building cycle. It all came down to taking `0x0000_0000_0000_wxyz` and turning it into `0x0000_0000_000w_xyzA`, or `0x0000_0000_wxyz_AAAA`, or whatever. I started thinking about this in terms of “information”: I needed to _preserve_ the information in the nibbles that are already set, and _add_ information for the new nibbles.

What do I mean by “preserving information”? Think about a cryptographic code, like a simple [Caesar cipher](http://en.wikipedia.org/wiki/Caesar_cipher). Let’s say we’re encoding a message in which every letter has been replaced by the letter thirteen places later in the English alphabet, say “cerfreivat vasbezngvba”. It’s trivial to undo this encryption and recover the original message precisely. This particular encoding is known as [rot13](http://rot13.com).

On the other hand, if we try encoding a message by replacing every vowel with an underscore (“pr_s_rv_ng _nf_rm_t__n”), then we have _not_ preserved information. You might be able to figure out the original word (indeed, that’s the premise behind the game show _[Wheel of Fortune](http://en.wikipedia.org/wiki/Wheel_of_Fortune_(U.S._game_show))),_ and so might a computer (with the help of an English dictionary), but you can’t always be sure. Is “m__nt__n” supposed to be “mountain” or “maintain”?

What does this have to do with our optimization problem? As long as we can get to the correct final form, the intermediate result doesn’t have to be in the same form. As a simple example, if it was more efficient to compute `~result`, we could do that, and then invert it as our last step. We saw before that putting information in its final form is a good thing, but if we save enough work or can get it to its final form as a side effect of work we’re doing anyway, it might be worth it.

So…_is_ there something more efficient?

(The next bit was a bit of an intuitive leap for me, which I then had to work out to make sure it actually made sense. I get the feeling that some people might have found it obvious and some may not have stumbled on it at all. So don’t stress if you’re in the latter group.)

…What if we build the result using inverted constants, and flip it back _as we go?_ Since two bitwise inversions gets you back to your original value, we’d use the original forms of the even constants and the inverted forms of the odd constants, and then they should both undergo the right number of flips by the time we finish building the result. This comes out to two new lines in `shift_in`:

```
static inline uint64_t shift_in_inverting(uint64_t result,
                                          unsigned counts[static 16],
                                          int which) {
  unsigned countTimesFour = counts[which];
  result <<= countTimesFour;
  uint64_t mask = ~0ull;
  mask <<= countTimesFour;
  uint64_t repeatedOnes = (~0ull) / 0xF;
  uint64_t repeatedNibbles = repeatedOnes * which;
  repeatedNibbles = repeatedNibbles ^ -(which & 1ull); // NEW
  repeatedNibbles &= ~mask;
  result |= repeatedNibbles;
  result = ~result; // NEW
  return result;
}
```

What’s that `repeatedNibbles ^ -(which & 1ull)`? Let’s break it down. `which & 1ull` is 1 if `which` is odd and 0 if it’s even. The minus sign turns that into -1 or 0, which is equivalent to ~0 or 0. Then we XOR that value with `repeatedNibbles`. So the code is equivalent to

```
if (which & 1ull) repeatedNibbles = ~repeatedNibbles;
```

but does that, again, without using a control-flow statement.

We also have to actually get rid of the call for the 0 case now, because otherwise we’d be doing an odd number of inversions.

```
//result = shift_in_inverting(result, counts, 0x0);
result <<= counts[0];
```

And looking at the generated assembly, we can see success! The constants at the top of the function are now just the even numbers:

```
movabsq $2459565876494606882, %r9   ## imm = 0x2222222222222222
movabsq $4919131752989213764, %r10  ## imm = 0x4444444444444444
movabsq $7378697629483820646, %r11  ## imm = 0x6666666666666666
movabsq $-8608480567731124088, %r14 ## imm = 0x8888888888888888
movabsq $-6148914691236517206, %r15 ## imm = 0xAAAAAAAAAAAAAAAA
movabsq $-3689348814741910324, %r12 ## imm = 0xCCCCCCCCCCCCCCCC
movabsq $-1229782938247303442, %r13 ## imm = 0xEEEEEEEEEEEEEEEE
```

It’s fun to see the result get built up, too. This example shows the intermediate values for an input of `0x0badbeef`.

```
ffffffffffffffff  // F:  f
0000000000000011  // E: ~fee
fffffffffffffeed  // D:  feed
0000000000000112  // C: ~feed
fffffffffffeedbb  // B:  feedbb
0000000000112445  // A: ~feedbba
ffffffffffeedbba  // 9:  feedbba
0000000000112445  // 8: ~feedbba
ffffffffffeedbba  // 7:  feedbba
0000000000112445  // 6: ~feedbba
ffffffffffeedbba  // 5:  feedbba
0000000000112445  // 4: ~feedbba
ffffffffffeedbba  // 3:  feedbba
0000000000112445  // 2: ~feedbba
ffffffffffeedbba  // 1:  feedbba
feedbba000000000  // 0: (shift)
```

**Moral: Generating the result in the right form to start is great, but if there’s another form that’s better for computation, use that while you’re still computing things.**

And the code in the cycle is…still 8 instructions. Hm.

```
movb    -88(%rbp), %cl
shlq    %cl, %rsi

movq    $-1, %rdx
shlq    %cl, %rdx
notq    %rdx

andq    %r11, %rdx
orq     %rsi, %rdx
notq    %rdx
```

We traded a `mov` for the extra `not`, and it turns out that’s more expensive. We actually _lost_ about 3% with this change. If we want this to be a win, we’re going to have to actually get rid of instructions.

### The Magic of XOR

Fortunately, we can actually do that. If we collapse the whole `shift_in` helper into a single line, we’d get something like this:

```
result = ~(result | (repeatedNibbles & ~mask))
```

This is really two separate parts: the “top” part of `result`, which has the value we’ve computed so far, and the “bottom” part, which is where we’re trying to put the new nibbles. If we look at these parts separately, we get this:

```
result_top    = ~(result_top | 0)
result_bottom = ~(0          | repeatedNibbles_bottom)
```

It actually helps a lot that we know that parts of each value are 0! You can really see how we’re preserving information in both values.

There are two other ways to preserve bitwise information like this. The first is to use AND:

```
result_top    = ~(result_top & ~0)
result_bottom = ~(~0         & repeatedNibbles_bottom)
```

But it turns out this isn’t any less work than using OR, even if we distribute some of the negations using [De Morgan’s laws](http://en.wikipedia.org/wiki/De_Morgan%27s_laws).

The other way is to use XOR:

```
result_top    = ~(result_top ^ 0)
result_bottom = ~(0          ^ repeatedNibbles_bottom)
```

And this is more promising, because now we can distribute the `~`:

```
result_top    = result_top ^ ~0
result_bottom = 0          ^ ~repeatedNibbles_bottom
```

What does this mean? It says that we can get the same result value by computing

```
result = result ^ ~(repeatedNibbles & ~mask)
```

And a simple application of De Morgan reduces that to

```
result = result ^ (~repeatedNibbles | mask)
```

Let’s try it.

```
static inline uint64_t shift_in_with_xor(uint64_t result,
                                         unsigned counts[static 16],
                                         int which) {
  unsigned countTimesFour = counts[which];
  result <<= countTimesFour;
  uint64_t mask = ~0ull;
  mask <<= countTimesFour;
  uint64_t repeatedOnes = (~0ull) / 0xF;
  uint64_t repeatedNibbles = repeatedOnes * which;
  repeatedNibbles = (~repeatedNibbles) ^ -(which & 1ull); // NEW
  repeatedNibbles |= mask;
  result ^= repeatedNibbles; // NEW
  return result;
}
```

The interesting change here is to our even-odd trick, which has an extra inversion in it. Since the whole expression collapses down to a constant anyway, that shouldn’t cost us anything.

This gets us down to a fifth of our first bucket sort, and below 8% of the original reference implementation. On my machine, that was going from 440s down to 33s. The assembly for the result-building cycle is also beautifully short:

```
movb    -88(%rbp), %cl
shlq    %cl, %rsi

movq    $-1, %rdx
shlq    %cl, %rdx

orq     %r11, %rdx
xorq    %rsi, %rdx
```

Not much left to squeeze out of that.

**Moral: An approach that may seem slower might have more opportunities for optimization.**

**Moral: XOR has NOT-like properties.**

**Moral: [You can go far, kid.](https://www.youtube.com/watch?v=5_LxyhCJpsM)**

…and that’s as good as I could do on my own.

### The Winning Solution

But I didn’t win the contest, even the non-SIMD division. I didn’t even get close: my solution (though using [packed counts](#avoid-memory-access) with the XOR solution) came in about 13th[5](#fn:about), and the winning solution was twice as fast—three times as fast on John’s machine. What did they do differently?

Interestingly, bucket sort seemed to be the right approach when forgoing SIMD: every solution that was faster than mine used some variation of the same basic strategy, except the one by my coworker, [Nadav](https://github.com/regehr/nibble-sort/blob/master/nadav.c).[6](#fn:Nadav)

So what did they do differently? Let’s look at the winning entry by “[Jerome](https://github.com/regehr/nibble-sort/blob/master/jerome.c)”:

```
static uint64_t table[256];
static uint64_t offsets[256];
static uint64_t table3[256 * 17];

__attribute__((constructor)) static void init_table() {
  for (int i = 0; i < 16; i++)
    for (int j = 0; j < 16; j++) {
      table[i * 16 + j] = (UINT64_C(1) << 4 * i) + (UINT64_C(1) << 4 * j);
      offsets[i * 16 + j] = (i + j) << 8;
      for (int k = 0; k < 17; k++)
        table3[i * 16 + j + k * 256] =
            ((i + j + k >= 16) ? 0 : (0x1111111111111111 << 4 * (i + j + k))) +
            ((j + k >= 16) ? 0 : (0x1111111111111111 << 4 * (j + k)));
    }
}

static uint64_t sort_word(uint64_t word) {
  if ((word << 4 | word >> 60) == word)
    return word;
  uint64_t counts = 0;
  for (int i = 0; i < 8; i++)
    counts += table[(word >> 8 * i) & 0xff];
  uint64_t output = 0;
  uint64_t offset = 0;
  for (int i = 0; i < 8; i++) {
    output += table3[((counts >> 8 * i) & 0xff) + offset];
    offset += offsets[(counts >> 8 * i) & 0xff];
  }
  return output;
}

void nibble_sort_jerome(uint64_t *buf) {
  for (int i = 0; i < 1024; i += 4) {
    buf[i] = sort_word(buf[i]);
    buf[i + 1] = sort_word(buf[i + 1]);
    buf[i + 2] = sort_word(buf[i + 2]);
    buf[i + 3] = sort_word(buf[i + 3]);
  }
}
```

!! What’s going on here? A few things look familiar, including a counting section using [packed counts](#avoid-memory-access):

```
if ((word << 4 | word >> 60) == word)
  return word;
uint64_t counts = 0;
for (int i = 0; i < 8; i++)
  counts += table[(word >> 8 * i) & 0xff];
```

and a result-building section of some kind:

```
uint64_t output = 0;
uint64_t offset = 0;
for (int i = 0; i < 8; i++) {
  output += table3[((counts >> 8 * i) & 0xff) + offset];
  offset += offsets[(counts >> 8 * i) & 0xff];
}
return output;
```

But what’s with those tables? And why are things being done in chunks of 8 instead of 4?

Let’s take the easy section first. Jerome is using packed counts in the same way I tried, where nibble 0 in `counts` represents the number of `0`s in `word`, all the way up to nibble 15 counting `F`s. Each time through the loop, they take _two_ nibbles from `word` and look them up in the table. Logically, when we look up, say, `0x9B` in the table, we want to find an entry that means “one `9` and one `B`”. Similarly, when we look up `0xAA`, we should find an entry that means “two `A`s”.

But since we’re using packed counts, we can encode each of those as a single number. “One `9` and one `B`” is represented as `(1 << (4 * 0x9)) + (1 << (4 * 0xB))`, and “two `B`s” is `2 << (4 * 0xB)`. And indeed this is what’s being calculated for `table`:

```
table[i * 16 + j] = (UINT64_C(1) << 4 * i) + (UINT64_C(1) << 4 * j);
```

Now we can see the benefit of going two nibbles at a time: we get through the value twice as fast while still computing the same counts! Being able to go two nibbles at a time makes the packed counts idea worth it, especially when we get to the result-building step.

_Aside: What’s that `__attribute__((constructor))`? It’s just a way to get certain compilers (including GCC or Clang) to run some code even before running `main`, the usual start of a C program. This functionality is a normal part of C++, but needs a [specific compiler extension](https://gcc.gnu.org/onlinedocs/gcc/Common-Function-Attributes.html#index-g_t_0040code_007bconstructor_007d-function-attribute-3065) to be used in C._

So they have the same kind of packed counts I tried. How does their result-building work? Like the counting they’re going two nibbles at a time, so they should be filling in all the `0`s and `1`s, then all the `2`s and `3`s, and so on. Let’s look first at the `offset` counter. What’s in the `offsets` table?

```
offsets[i * 16 + j] = (i + j) << 8;
```

This says that `0xC3` corresponds to `(0xC + 0x3) << 8`. In other words, it’s the sum of the two nibbles, times 28. Why “times 28”? We’ll come back to that. For now, just note that all `offsets` is doing is adding up values, which means the variable `offset` is a running total of all the nibbles we’ve seen so far.

Now we can look at `table3`. The expression for each element of `table3` is a bit monstrous, so I’m not going to try to take it apart. Instead, let’s figure out what we _want_ to see. Let’s say we’re on the second iteration of the loop, reading the counts for the `2`s and `3`s. After the loop, we want `output` to contain the correct number of `2`s and `3`s based on those counts. Since we’re not doing any shifting, they have to be in the correct position, too. Let’s say we have two `2`s and three `3`s, and we’ve already added three other nibbles (as tracked by `offset`). That means our current result is something like

```
0x0000_0000_0000_0xyz
```

And after the loop, we want it to look like this:

```
0x0000_0000_3332_2xyz
```

So we know that the value we get out of `table3` _must_ be

```
0x0000_0000_3332_2000
```

That is, it’s the correct number of `3`s, followed by the correct number of `2`s, at the correct offset. And there are 17 possible offsets, depending on how many nibbles we’ve already filled in (0 up to 16). Having that “completely full” 17th case makes it so that Jerome doesn’t have to test if we’re done already in the middle of the loop.

You’ll have to believe that those are in fact the values in `table3`, because I’m not going to break it down for you. (I didn’t do it myself either.) But why the “times 28”? Well, `table3` is declared like this:

```
static uint64_t table3[256 * 17];
```

…because there are 17 possible entries for each of the 256 two-nibble combinations (16 * 16).[7](#fn:impossible) They could have written it like this:

```
static uint64_t table3[256][17];
```

…but at least on my machine, that makes the resulting code run a little slower. So the “times 28” (or “times 256”) is just storing the offset in the form it’ll be used to look things up later on, just like my solution stored counts “times four”.

Why didn’t I come up with this solution? Essentially, Jerome took many of the morals I’ve already mentioned and applied them in even better ways. The one I’d underscore most?

**Moral: Always test your assumptions.**

I didn’t think a memory-based cache could beat pure register work no matter what the specifics of the algorithm I was using, and so _I didn’t even try it._ I was wrong.

One last note: what about those loops? Aren’t they still branches? Turns out that they’re simple enough that my compiler completely [unrolls](http://en.wikipedia.org/wiki/Loop_unrolling#A_simple_manual_example_in_C) them, just like we would have done manually. So, no harm done.

Nice work, Jerome!

### Epilogue

This was a fun little diversion from my usual work, even if it ended up becoming a [nerd snipe](https://xkcd.com/356/). The activity also reminded me of many things about optimization, some of which apply even beyond microbenchmarks such as these. Here are all my “morals” once again:

- If you’re trying to optimize something, don’t take the current algorithm for granted.
- Do things in bulk when possible.
- In general, do less work.
- Branches are more expensive than simple computation.
- Loops are also branches.
- Memory access isn’t necessarily as expensive as you’re worried it is.
- XOR has NOT-like properties.
- Don’t spend effort fixing up something to be in the right form if you can just start with it that way…
- …but if there’s another form that’s better for computation, use that while you’re still computing things.
- Compilers are right most of the time.
- An approach that may seem slower might have more opportunities for optimization.
- **Always test your assumptions.**

_You can download [all of the versions](https://belkadan.com/blog/2015/05/Nibblesort/nibble_sort.c) of `nibble_sort` discussed in this post; that file also contains a `main` that will run each of them. You can also check out [all of the submissions](https://github.com/regehr/nibble-sort) to the actual contest._

1. Note that if you don’t write newlines, however, the output gets buffered and takes _much_ less time. Another point of comparison is doing 1024 `malloc` allocations and immediately freeing them, and that only took 80-90µs on my machine. So 400µs isn’t _fast_ either. [↩︎](#fnref:buffer)
2. Actually, I didn’t keep my progress while working on this, and I didn’t use source control. I regretted it partway through, especially after getting the idea for this blog post, but then I kept thinking I was already done. These entries were constructed for the purpose of this blog post. **Moral: Put everything under source control from the start, even if it’s just a single file.** [↩︎](#fnref:actually)
3. When I started I was using macros to make sure the code actually was all in one function. Macros get the job done, but they’re pretty messy, so I was glad to switch to helper functions without any performance hit. I _did_ check that they were in fact being inlined by looking at the generated assembly, but since there’s no control flow at all it was probably a given. **Moral: Use helper functions instead of macros unless a macro is really needed.** [↩︎](#fnref:macros)
4. Some CPUs, including Intel-like CPUs, have instructions that can operate on memory as well. We actually saw this above with the code for `counts[i] += 4`. But this is still generally slower than simply operating on registers. [↩︎](#fnref:memory)
5. The results are pretty platform-dependent. On my machine and with my compiler, my code runs faster than some of my near competitors’. Also, one of the entries ahead of mine got a few cases wrong. [↩︎](#fnref:about)
6. Nadav’s solution did a sort of parallel bubble sort that compared each nibble to its neighbors and swapped them towards the right places. On my machine it beats my submitted solution but loses to the one with unpacked counts. Many of the SIMD solutions use similar strategies. **Moral: limitations based on theory are derived from assumptions that may not apply to your particular use case,** in this case that comparison-based sorts take O(N log N) time. [↩︎](#fnref:Nadav)
7. Admittedly some combinations can’t occur because they would imply more than 16 nibbles originally, e.g. `0xAA`. But it’d be more trouble to leave them out. [↩︎](#fnref:impossible)

This entry was posted on [May](https://belkadan.com/blog/2015/05) 09, [2015](https://belkadan.com/blog/2015) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Compilers](https://belkadan.com/blog/tags/compilers), [Source code](https://belkadan.com/blog/tags/source-code)
