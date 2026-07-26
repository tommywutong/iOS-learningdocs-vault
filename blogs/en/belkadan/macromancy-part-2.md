---
title: Macromancy, Part 2
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2016/08/Macromancy-2/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:eb41b0300c5bb545'
translated: false
---

> 原文：[Macromancy, Part 2](https://belkadan.com/blog/2016/08/Macromancy-2/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Macromancy](https://belkadan.com/blog/2016/08/Macromancy/)

[Over-abstraction](https://belkadan.com/blog/2017/09/Over-abstraction/) »

« [Macromancy](https://belkadan.com/blog/2016/08/Macromancy/?tag=cxx)

[My Little Optimization: The Compiler Is Magic](https://belkadan.com/blog/2018/03/My-Little-Optimization/?tag=cxx) »

## [Macromancy, Part 2](#)

### The Challenge

> Given a macro that expands to an arbitrary list of headers, include every header in the list, in order.

```
#define HEADERS "stdio.h", "stdlib.h", "assert.h"
#include "include_dynamic.h"
// stdio.h, stdlib.h, and assert.h are now included and available.
```

### Progress So Far

The C preprocessor is a powerful tool, but not a particularly versatile one. Rather, it does a few specific things, and people have taken advantage of its workings to compose those capabilities to accomplish their tasks. And sometimes, to do something ridiculous and overengineered…like this.

I ended [part 1](https://belkadan.com/blog/2016/08/Macromancy/) here:

```
#if !defined(HEADERS_IMPL)
# define HEADERS_IMPL HEADERS, ()
#endif
#if !FIRST_IS_EMPTY_PARENS(HEADERS_IMPL)
# include APPLY(FIRST, HEADERS_IMPL)
/* Update HEADERS_IMPL to APPLY(REST, HEADERS_IMPL) */
# include __FILE__
#endif
```

(You can find the implementations of `FIRST`, `REST`, `APPLY`, and `FIRST_IS_EMPTY_PARENS` in [part 1](https://belkadan.com/blog/2016/08/Macromancy/).)

At this point there’s only one problem left: how to update the `HEADERS_IMPL` list once we’ve included a header, or alternately how to keep track of where we are in the list. This turns out to be _really hard._ Why? Because the C preprocessor doesn’t have any way to _update_ macros based on a previous value.

At least, not an obvious one.

### Rules of the Game

In order to have any chance of solving this problem, I’d like to lay out some hard rules of the C preprocessor. As far as I know these rules are completely inflexible and cannot be overridden in any way, at least not in [Clang](https://en.wikipedia.org/wiki/Clang).

1. The expansion of a macro cannot result in a new preprocessor directive. That is, you can’t define a macro that, when used, defines more macros or includes other files. (C11 6.10.3.4p3)
2. The name of a macro being `#define`d (or `#undef`ined) is always taken directly from the source; that is, it cannot be expanded from another macro. (C11 6.10.3p9-10)
3. If a macro name appears in its own expansion, it is not expanded again. (C11 6.10.3.4p2)
4. A macro is not expanded until it is used, e.g. in `#include` or `#if` (and definitely not within `#define`).

This last rule blocks the most obvious approach. In normal C programming, you could say `headers = rest(headers)` and be done, but the equivalent macro doesn’t do what you want at all.^[1](#fn:illegal)

```
#define FIRST(A, ...) A
#define REST(A, ...) __VA_ARGS__

#define APPLY(FN, ARGS) FN(ARGS)

#define HEADERS "stdio.h", "stdlib.h", "assert.h"

HEADERS
"stdio.h", "stdlib.h", "assert.h"

#define HEADERS APPLY(REST, HEADERS)

HEADERS
/* no output; applies REST to the one-element list HEADERS */
```

Clearly we’re going to need something else to maintain state.

### `__COUNTER__`?

While it’s not part of the C standard, several compilers implement a special macro called `__COUNTER__`. Unlike a normal macro, `__COUNTER__` has a different value every time you expand it, always one greater than the previous value. If we could guarantee that no one else in the program is using `__COUNTER__`, we could just use that to keep track of where we are in the list.

```
#if !defined(HEADERS_IMPL)
# define HEADERS_IMPL HEADERS, ()
#endif
#if !FIRST_IS_EMPTY_PARENS(HEADERS_IMPL)
# include NTH(__COUNTER__, HEADERS_IMPL)
# include __FILE__
#endif
```

But I didn’t want to make that assumption, or the related assumption that our special `include_dynamic.h` header wasn’t going to be included more than once. So that approach was out.

Okay, rather than relying on the _values_ of `__COUNTER__`, how about using it to generate unique identifiers? That’s the most common use for it, really: the standards-compliant macro `__LINE__` won’t be unique if it gets expanded more than once on the same line. Unfortunately, this fails on _two_ counts: rule (2) says we can’t use it to choose the name of a macro to define, and rule (4) says we can’t put it into another macro and have it expanded later—it’ll get a _new_ counter value at that point.

### `NTH`

Rule (3) says we’re going to have a hard time updating any existing macro in terms of itself. Instead, let’s try keeping a counter (a manual one, not using `__COUNTER__`), and then indexing into our list. How might we do that?

```
# include NTH(INDEX, HEADERS_IMPL)
/* increment 'INDEX' somehow */
# include __FILE__
```

One way to do this would be to make a long list of explicit indexes into macros, and then use [token-pasting](https://belkadan.com/blog/2016/08/Macromancy/#token-pasting-tricks) to pick the right one:

```
#define NTH_0(A, ...) A
#define NTH_1(A, B, ...) B
#define NTH_2(A, B, C, ...) C
/* … */

#define NTH(N, ...) NTH_##N(__VA_ARGS__, unused)

NTH(0, a, b)
a
NTH(1, a, b)
b
```

I found this fairly annoying because you have to define separate `NTH_*` macros up to the maximum number of items in the list, and they’re all slightly different. We can make this a little tidier at the cost of extra compiler work by using something like recursion:

```
#define FIRST(A, ...) A
#define REST(A, ...) __VA_ARGS__

#define NTH_0(...) FIRST(__VA_ARGS__)
#define NTH_1(...) NTH_0(REST(__VA_ARGS__))
#define NTH_2(...) NTH_1(REST(__VA_ARGS__))
/* … */

#define NTH(N, ...) NTH_##N(__VA_ARGS__, unused)

NTH(0, a, b, c)
a
NTH(2, a, b, c)
c
```

…but we’re still in the realm of “one more header = one more NTH macro”. Still, this works for now.

### Increment

`NTH` is useful, but it hasn’t actually solved our problem: how do we keep track of where we are in the list? We’ve moved that problem from “update `HEADERS_IMPL`” to “increment a counter”, but we haven’t actually solved it yet. Rather than flail around with various attempts, let’s take a closer look at the rules.

1. The expansion of a macro cannot result in a new preprocessor directive. That is, you can’t define a macro that, when used, defines more macros or includes other files.
2. The name of a macro being `#define`d (or `#undef`ined) is always taken directly from the source; that is, it cannot be expanded from another macro.
3. If a macro name appears in its own expansion, it is not expanded again.
4. A macro is not expanded until it is used, e.g. in `#include` or `#if` (and definitely not within `#define`).

Incrementing a counter requires us either to update the macro to have an additional `+1` at the end (e.g. `1` becoming `1+1`), which would violate rule (3), or it would have to get a new value based on its previous value (e.g. `1` becoming `2`), which would violate either rule (1) or rule (4) (depending on how you approach it). To put it another way, incrementing a counter macro is going to _require_ expanding that macro. We don’t want to include arbitrary headers, so we’re going to _have_ to use `#if` in some way.^[2](#fn:line)

This is this post’s preprocessor challenge, although there actually is a fairly straightforward solution. Given these hints, can you figure out how to increment a given macro? (Even within a finite range of values.) If you’re not interested in a puzzle, just scroll down.

Here’s the most straightforward way to do this:

```
#if INDEX == 0
# undef INDEX
# define INDEX 1
#elif INDEX == 1
# undef INDEX
# define INDEX 2
#elif INDEX == 2
/* … */
#else
# error "too many headers provided to include_dynamic.h"
#endif
```

And this is actually sufficient to solve the entire puzzle. We have a way to get the `NTH` element of a list, and we have a way to increment an index. That’s all we need!

```
#if !defined(HEADERS_IMPL)
# define HEADERS_IMPL HEADERS, ()
#endif
#if !FIRST_IS_EMPTY_PARENS(NTH(INDEX, HEADERS_IMPL))
# include NTH(INDEX, HEADERS_IMPL)
/* increment INDEX with a pile of #ifs */
# include __FILE__
#endif
```

### Powers of Two

But of course this made me even less happy than for `NTH`. This is repetitive to a silly degree—three lines to handle one higher value than before. So now I made the challenge arbitrarily harder: the lines-of-code / headers-supported ratio should have sub-linear growth (“better than O(N)”).

Fortunately, I now have the full power of `#if` at my disposal, which includes any arithmetic and comparison operators. So why not decompose `INDEX` into its component bits?

```
#if INDEX & (1 << 0)
# define PREV_INDEX_BIT_0 (1 << 0)
#else
# define PREV_INDEX_BIT_0 0
#endif

#if INDEX & (1 << 1)
# define PREV_INDEX_BIT_1 (1 << 1)
#else
# define PREV_INDEX_BIT_1 0
#endif

/* … */

#undef INDEX
#define INDEX \
  (1 + PREV_INDEX_BIT_0 + PREV_INDEX_BIT_1 + /*…*/ + PREV_INDEX_BIT_N)
```

Adding one more `PREV_INDEX_BIT_N` macro means being able to support values twice as big. I did have to trade something for it, though: the values here aren’t simple numbers but instead full-on expressions that add up to the next number. That means the token-pasting implementation of `NTH` (`NTH_0`, `NTH_1`, etc.) won’t work anymore.

### Powers of Two, constructively

Fortunately, we can use the same basic strategy to replace our implementation of `NTH`. Let’s start by building up powers-of-two repeated `REST`s.

```
#define FIRST(A, ...) A
#define REST(A, ...) __VA_ARGS__

#define REST_2_TO_THE_0(...) REST(__VA_ARGS__)
#define REST_2_TO_THE_1(...) REST_2_TO_THE_0(REST_2_TO_THE_0(__VA_ARGS__))
#define REST_2_TO_THE_2(...) REST_2_TO_THE_1(REST_2_TO_THE_1(__VA_ARGS__))
#define REST_2_TO_THE_3(...) REST_2_TO_THE_2(REST_2_TO_THE_2(__VA_ARGS__))

REST_2_TO_THE_3(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
80, 90, 100
```

What do we do if we want, say, `REST_5`, which drops the first five elements? Like before, we can decompose this into its composite bits: it’s equivalent to applying `REST_2_TO_THE_2` to the result of `REST_2_TO_THE_0`. Applying the same pattern as before, we can build up a composite operation based on the current value of `counter`:

```
#if INDEX & (1 << 0)
# define NTH_BIT_0(...) REST_2_TO_THE_0(__VA_ARGS__)
#else
# define NTH_BIT_0(...) __VA_ARGS__
#endif

#if INDEX & (1 << 1)
# define NTH_BIT_1(...) REST_2_TO_THE_1(__VA_ARGS__)
#else
# define NTH_BIT_1(...) __VA_ARGS__
#endif

/* … */

#undef NTH_N
#define NTH_N(...) \
  FIRST(NTH_BIT_0(NTH_BIT_1(/*…(*/ NTH_BIT_N(__VA_ARGS__) /*)…*/)))
```

Note the extra `FIRST` on the outside of `NTH_N`; the `REST…` macros all take a list and produce another list, but `NTH` is supposed to give us a single element.

With `NTH_N` and the incrementing definition of `counter` in the previous section, we’ve achieved the new goal: we can support twice as many headers by adding a fixed number of lines to the file (ten lines of `#if` and one more `REST…` macro, plus modification of `INDEX` and `NTH_N`).

But having the series of `#if` appear twice _still_ feels messy. We’re testing the same thing in both cases, so we could fold them together, but really it feels like there’s a higher abstraction here that’s missing.

### Higher-Order Macros

Let’s take a look at the `REST…` macros again:

```
#define REST_2_TO_THE_0(...) REST(__VA_ARGS__)
#define REST_2_TO_THE_1(...) REST_2_TO_THE_0(REST_2_TO_THE_0(__VA_ARGS__))
#define REST_2_TO_THE_2(...) REST_2_TO_THE_1(REST_2_TO_THE_1(__VA_ARGS__))
#define REST_2_TO_THE_3(...) REST_2_TO_THE_2(REST_2_TO_THE_2(__VA_ARGS__))
```

One thing to notice here is that these macros (a) never look at their arguments, and (b) never do anything with their results besides forward them on wholesale. And since they all eventually chain down to `REST`, they’re going to expand into one long chain of `REST`s at the end. (Which is what we expected; `REST_2_TO_THE_3` should be `REST` repeated two-to-the-third times—eight times—to drop the first eight elements of the list.)

There’s nothing special about `REST`, though. We could use something else instead.

```
#define BRACKET(...) [__VA_ARGS__]

#define BRACKET_2_TO_THE_0(...) BRACKET(__VA_ARGS__)
#define BRACKET_2_TO_THE_1(...) BRACKET_2_TO_THE_0(BRACKET_2_TO_THE_0(__VA_ARGS__))
#define BRACKET_2_TO_THE_2(...) BRACKET_2_TO_THE_1(BRACKET_2_TO_THE_1(__VA_ARGS__))

BRACKET_2_TO_THE_2(a, b, c)
[[[[a, b, c]]]]
```

So if the operation doesn’t matter…we should be able to pass it in separately.

```
#define REPEAT_2_TO_THE_0(OP, ...) OP(__VA_ARGS__)
#define REPEAT_2_TO_THE_1(OP, ...) \
  REPEAT_2_TO_THE_0(OP, REPEAT_2_TO_THE_0(OP, __VA_ARGS__))
#define REPEAT_2_TO_THE_2(OP, ...) \
  REPEAT_2_TO_THE_1(OP, REPEAT_2_TO_THE_1(OP, __VA_ARGS__))

#define REST(A, ...) __VA_ARGS__
#define BRACKET(...) [__VA_ARGS__]

REPEAT_2_TO_THE_2(REST, a, b, c, d, e, f, g)
e, f, g
REPEAT_2_TO_THE_2(BRACKET, a, b, c, d, e, f, g)
[[[[a, b, c, d, e, f, g]]]]
```

Nifty!

We can tie this together with a `REPEAT_N` that replaces `NTH_N`; `NTH_N(input)` is then just `FIRST(REPEAT_N(REST, input))`.

```
#if INDEX & (1 << 0)
# define REPEAT_BIT_0(OP, ...) REPEAT_2_TO_THE_0(OP, __VA_ARGS__)
#else
# define REPEAT_BIT_0(OP, ...) __VA_ARGS__
#endif

#if INDEX & (1 << 1)
# define REPEAT_BIT_1(OP, ...) REPEAT_2_TO_THE_1(OP, __VA_ARGS__)
#else
# define REPEAT_BIT_1(OP, ...) __VA_ARGS__
#endif

/* … */

#undef REPEAT_N
#define REPEAT_N(OP, ...) \
  REPEAT_BIT_0(OP, REPEAT_BIT_1(OP, /*…(*/ REPEAT_BIT_N(OP, __VA_ARGS__) /*)…*/))
```

### The Update Trap

At this point we’re _nearly_ done. Incrementing `INDEX` using `REPEAT` seems a little tricky at first, but it actually isn’t that hard.

```
#define INCREMENT(x) (1+x)
/* define REPEAT_N here based on INDEX */
#define INDEX_PLUS_ONE REPEAT_N(INCREMENT, 1)
```

This is going to expand to a _monster_ list of `(1+(1+(1+…)))`, but it should get the job done.^[3](#fn:limits) But we don’t want a different macro that has the value “`INDEX` plus 1”. We want it to be the _same_ macro.

```
#undef INDEX
#define INDEX REPEAT_N(INCREMENT, 1)
```

At first glance there’s nothing wrong with this, but you know it’s not correct because I started the sentence with “at first glance there’s nothing wrong with this”. The problem is that old rule (4):

> A macro is not expanded until it is used, e.g. in `#include` or `#if` (and definitely not within `#define`).

We’ve avoided the original problem of defining `INDEX` in terms of itself. Unfortunately, we’re now defining `REPEAT_N` in terms of itself—as we go through each of the `#if` blocks, we change out pieces that we’re in the middle of using.

```
#if INDEX & (1 << 1)
# define REPEAT_BIT_1(OP, ...) REPEAT_2_TO_THE_1(OP, __VA_ARGS__)
#else
# define REPEAT_BIT_1(OP, ...) __VA_ARGS__
#endif
```

I couldn’t come up with a better answer for this than to have two copies of the `REPEAT_BIT_N` logic, because of rule (2). That’s not exactly satisfying, but it doesn’t violate any of our goals.

### …But It All Works

Here’s the final solution, separated into five “paragraphs”. I’ve left out the helpers `FIRST`, `REST`, `INCREMENT`, `APPLY`, and `FIRST_IS_EMPTY_PARENS`, and also factored the powers-of-two `REPEAT_N` logic into a separate file. The result is actually fairly straightforward, at least if you take the existence and correctness of the other macros on faith.

```
// Start INDEX at 0.
#if !defined(INDEX)
# define INDEX 0
#endif

// Set up REPEAT_N based on INDEX.
// The extra macro REPEAT_COUNT just keeps the logic
// in "repeat.h" separate from this file.
#define REPEAT_COUNT (INDEX)
#include "repeat.h"

// Use REPEAT_N to drop the first N elements from HEADERS.
// The trailing () makes sure this is never empty.
#define HEADERS_REMAINING REPEAT_N(REST, HEADERS, ())

// Update INDEX for next time, using repeated INCREMENT.
#undef INDEX
#define INDEX REPEAT_N(INCREMENT, 1)

// Are we done? If not, get the next header and continue.
#if !FIRST_IS_EMPTY_PARENS(HEADERS_REMAINING)
# include APPLY(FIRST, HEADERS_REMAINING)
# undef HEADERS_REMAINING
# include __FILE__
#endif
```

You can [check out the whole thing](https://belkadan.com/blog/2016/08/Macromancy-2/include_dynamic.tbz), including some test files.

### Unbounded Lists?

While I did reach a solution that scales pretty well, it still only handles a finite number of headers (limited by `repeat.h`). Is there a way to truly handle an unbounded list?

Even ignoring sensible limits where the preprocessor might just give up (for example, more headers than fits in a platform-word-sized integer), my intuition says **no**, this is not possible. I feel like this conclusion should be derivable from rules (1)-(4), or possibly from something else in the standard, but I haven’t been able to prove it.

Part of this intuition comes from the way real preprocessor libraries handle incrementing logic: [Boost](http://www.boost.org/doc/libs/release/libs/preprocessor/doc/index.html) really does just [hardcode up to a certain limit](http://www.boost.org/doc/libs/1_61_0/boost/preprocessor/arithmetic/inc.hpp). I even found a [powers-of-ten table](http://www.boost.org/doc/libs/1_61_0/boost/preprocessor/slot/detail/counter.hpp) like my powers-of-two one; in retrospect a powers-of-ten table seems more useful because you can use token-pasting to get a single decimal integer token back out. But if there was a way to do this that wasn’t bounded, I’d expect a Boost contributor to have found it.

### P.S. Don’t Use This In Production

Okay, so this was all very cute, but I do want to point out some specific reasons why you shouldn’t adopt this:

- It’s not reentrant, meaning that if one of the headers you include is itself trying to use this trick, everything falls down. (It’s easy to check for this, at least, and I put that in the download, but still.)
- It’s brittle: a typo or bad input leads to a bunch of bizarre error messages.
- It messes up your diagnostics (because of the include stack).
- I’m not 100% sure it’s standards-compliant, which means it’s not portable. It passes Clang `-Weverything` without any issues, but that’s not a guarantee. I also didn’t try it in C++ mode.
- Preprocessing may be pretty fast but it still takes time. Why would you slow down your build?
- It’s “clever”. Clever code is unmaintainable code. I worked on a C++ compiler for two years and I find this confusing.
- Remember “global variables are bad”? Macros are global variables in a shared namespace.

But all in all I got [nerd-sniped](http://xkcd.com/356/) and it was fun. Thanks for reading!

1. …and isn’t even legal, first because redefining a macro without using `#undef` is forbidden (C11 6.10.3p2), and second because applying `REST` to a one-element list results in no variadic arguments being passed, which is also not allowed (C11 6.10.3p4). Most compilers allow both of these anyway. [↩︎](#fnref:illegal)
2. There actually _is_ another preprocessor directive that expands macros in a way the preprocessor can understand: `#line`. This controls the value of `__LINE__`, which could theoretically be used subsequently.

  ```
  #define FIRST(A, ...) A
  #define REST(A, ...) __VA_ARGS__

  #define NTH_0(...) FIRST(__VA_ARGS__)
  #define NTH_1(...) NTH_0(REST(__VA_ARGS__))
  #define NTH_2(...) NTH_1(REST(__VA_ARGS__))
  #define NTH_3(...) NTH_2(REST(__VA_ARGS__))
  /* ... */

  #define CONCAT(A, B) A ## B
  #define NTH(N, ...) CONCAT(NTH_, N)(__VA_ARGS__, unused)

  #define INDEX 1
  #line INDEX
  NTH(__LINE__, unused, a, b, c)
  a
  NTH(__LINE__, unused, a, b, c)
  c
  ```

  Unfortunately, while we can _update_ `__LINE__` this way, we can’t get the value back _out_ of `__LINE__`, because of rule (4). If you put `__LINE__` in a macro, it’ll give you the line where it finally gets expanded. (Also, this really messes with diagnostics coming from the current file.) [↩︎](#fnref:line)
3. Although the C standard only requires support for “4095 characters in a logical source line” (C11 5.2.4.1p1), so we’re only going to be able to count up to 1023 this way before we’re relying on our specific compiler. Then again, there’s also a paltry minimum of 127 arguments in one macro invocation, and only 15 nesting levels for `#include`d files! So one way or another a very long list of headers would be a problem for us. [↩︎](#fnref:limits)

This entry was posted on [August](https://belkadan.com/blog/2016/08) 21, [2016](https://belkadan.com/blog/2016) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [C++](https://belkadan.com/blog/tags/cxx)
