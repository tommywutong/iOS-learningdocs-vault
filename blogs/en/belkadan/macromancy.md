---
title: Macromancy
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2016/08/Macromancy/'
original_language: en
published: 2016-08-07
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:92ac44f9190349ac'
translated: false
---

> 原文：[Macromancy](https://belkadan.com/blog/2016/08/Macromancy/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Pronoun Buttons](https://belkadan.com/blog/2016/06/Pronoun-Buttons/)

[Macromancy, Part 2](https://belkadan.com/blog/2016/08/Macromancy-2/) »

« [C++ Templates are Turing-Complete](https://belkadan.com/blog/2009/05/C-plus-plus-Templates-are-Turing-Complete/?tag=cxx)

[Macromancy, Part 2](https://belkadan.com/blog/2016/08/Macromancy-2/?tag=cxx) »

## [Macromancy](#)

In section 6.10.2, paragraph 8 of the C11 standard, this example is specifically called out as legal (if implementation-defined):

```
#if VERSION == 1
  #define INCFILE "vers1.h"
#elif VERSION == 2
  #define INCFILE "vers2.h" // and so on
#else
  #define INCFILE "versN.h"
#endif
#include INCFILE
```

Yikes! Do people really want to do this? If I encountered this in a real program, I’d try to get rid of it—in most cases I figure you can just put the `#include`s inside the `#if` and be done with it. You can’t even do any clever tricks like building up a path, at least not portably.

So of course, after telling someone _else_ about this, my next reaction was how to take it further. (Please do not put this in a real program.)

This post expects that you are familiar with C or C++ and know what the C preprocessor is, at least abstractly. You do not need to be an expert, but you should recognize `#if`, `#include`, and `#define`. If you want to follow along, most of the code snippets here can be fed directly into `clang -E` (or `xcrun clang -E` on ~~OS X~~ macOS), which will display the output of preprocessing.^[1](#fn:cpp) (Bonus macOS tip: the invocation ``pbpaste | xcrun clang -E -`` will feed the contents of the clipboard directly into the preprocessor.)

### The Challenge

> Given a macro that expands to an arbitrary list of headers, include every header in the list, in order.

That is, I want to be able to do something like this:^[2](#fn:quotes)

```
#define HEADERS "stdio.h", "stdlib.h", "assert.h"
#include "include_dynamic.h"
// stdio.h, stdlib.h, and assert.h are now included and available.
```

I had a pretty strong feeling that it was possible, and (spoiler) it is, as long as you’re willing to accept a limit on the number of headers in the list. More on that later.

### The Easy Part

Step 1 was to make sure I could extract elements from this list, which turned out to be very easy:

```
#define FIRST(A, ...) A
#define REST(A, ...) __VA_ARGS__

FIRST(a, b, c)
a
REST(a, b, c)
b, c
```

Here I’m using the _variadic macros_ feature of C; the identifier `__VA_ARGS__` refers to the arguments passed in the `...` section of the macro.

Testing this was a little tricky, because of the order of macro expansion. If I just write `FIRST(HEADERS)`, the `FIRST` gets expanded before the `HEADERS`, i.e. it gets the first element of the “list of one item” `HEADERS`, then expands _that._

```
#define FIRST(A, ...) A
#define REST(A, ...) __VA_ARGS__

#define HEADERS "stdio.h", "stdlib.h", "assert.h"

FIRST(HEADERS)
"stdio.h", "stdlib.h", "assert.h"
```

Fortunately, this can be solved by a bit of indirection:

```
#define FIRST(A, ...) A
#define REST(A, ...) __VA_ARGS__

#define APPLY(FN, ARGS) FN(ARGS)

#define HEADERS "stdio.h", "stdlib.h", "assert.h"
	
APPLY(FIRST, HEADERS)
"stdio.h"
APPLY(REST, HEADERS)
"stdlib.h", "assert.h"
```

Now `APPLY` gets expanded and `FN` and `ARGS` get replaced at the same time, resulting in `FIRST("stdio.h", "stdlib.h", "assert.h")`. Which is exactly what we want.

With `FIRST`, `REST`, and `APPLY`, I could now lay out the high-level algorithm of `include_dynamic.h`:

```
#if /* HEADERS is not empty */
# include APPLY(FIRST, HEADERS)
/* Update HEADERS to APPLY(REST, HEADERS) */
# include __FILE__
#endif
```

No, I didn’t know how to implement the two commented bits yet, but this was an encouraging start!

By the way, manipulating structured data using the preprocessor like this may be a bit unusual, but it’s by no means a new thing. The [Boost](http://www.boost.org/doc/libs/1_61_0/libs/preprocessor/doc/index.html) C++ library includes a whole subsection on the preprocessor, and has a whole slew of ready-made macros for this sort of thing. In addition to (parenthesized) comma-separated lists, which they call [tuples](http://www.boost.org/doc/libs/1_61_0/libs/preprocessor/doc/index.html), they also have [several](http://www.boost.org/doc/libs/1_61_0/libs/preprocessor/doc/data/arrays.html) [other](http://www.boost.org/doc/libs/1_61_0/libs/preprocessor/doc/data/lists.html) [representations](http://www.boost.org/doc/libs/1_61_0/libs/preprocessor/doc/index.html) for structured data that can be manipulated by the preprocessor.

### The Base Case

Now that we can represent lists, the next step is to figure out when they’re empty. Unfortunately, this is trickier than it looks!

My first thought was to use a clever counting idiom I’ve seen before, which looks like this:

```
#define COUNT_IMPL(A, B, C, D, N, ...) N
#define COUNT(...) COUNT_IMPL(__VA_ARGS__, 4, 3, 2, 1)

COUNT(a, b)
2
COUNT(a, b, c, d)
4
```

This `COUNT` macro counts lists from 1 to 4 elements by _appending_ the numbers `4, 3, 2, 1` to the list. That means we have a new list with at least 5 elements in it, and the fifth element _is always the count of the original list.^[3](#fn:empty)_

(Play with a few examples to convince yourself that it works. It’s really quite clever!)

This trick is actually used to handle the one- and two-argument forms of [`CF_ENUM`](https://github.com/apple/swift-corelibs-foundation/blob/master/CoreFoundation/Base.subproj/CFAvailability.h#L113) (and `NS_ENUM`) in Apple’s frameworks. What it can’t do, however, is count _arbitrarily_ long lists—it relies on being able to pick the element “one after the longest list”.

I wasn’t willing to give up on arbitrarily long lists of headers just yet, so I set this solution aside and kept looking.

### Token-Pasting Tricks

My next thought was a trick that makes use of the _token-pasting_ operator, `##`. This operator takes two tokens and concatenates them—so, for example, `TOKEN ## PASTING` would result in `TOKENPASTING`, `2 ## 3` would give you `23`, and `NUMBER ## 1` would be `NUMBER1`. This can be used to tell if something is a _specific_ name by doing something like this:

```
#define IS_THE_WORD_FOO_CHECK_foo special

IS_THE_WORD_FOO_CHECK_ ## not_foo
IS_THE_WORD_FOO_CHECK_not_foo
IS_THE_WORD_FOO_CHECK_ ## foo
special
```

However, there’s a more interesting expansion here:

```
#define IS_THE_WORD_FOO_CHECK_foo unused, 1

IS_THE_WORD_FOO_CHECK_ ## not_foo
IS_THE_WORD_FOO_CHECK_not_foo
IS_THE_WORD_FOO_CHECK_ ## foo
unused, 1
```

The trick here is that for any identifier or number that _isn’t_ the interesting one, you get a single identifier out, but the interesting one becomes a _two-_element list. We can then use something like the `COUNT` idiom to get a true-or-false (`1`-or-`0`) value out.

```
#define APPLY_N(FN, ...) FN(__VA_ARGS__)

#define IS_THE_WORD_FOO_CHECK_foo unused, 1
#define IS_THE_WORD_FOO_IMPL(UNUSED, RESULT, ...) RESULT
#define IS_THE_WORD_FOO(X) \
  APPLY_N(IS_THE_WORD_FOO_IMPL, IS_THE_WORD_FOO_CHECK_ ## X, 0, unused)

IS_THE_WORD_FOO(not_foo)
0
IS_THE_WORD_FOO(foo)
1
```

If you work it out, the arguments to `IS_THE_WORD_FOO_IMPL` become `(IS_THE_WORD_FOO_CHECK_not_foo, 0, unused)` in the first case, and `(unused, 1, 0, unused)` in the second.^[4](#fn:cpp2) Perfect!

(`APPLY_N` is just like `APPLY` except that it accepts macros that take variadic arguments. Like before, we’re using it to make sure that the result of the token-pasting is expanded before the replacement of the `IS_THE_WORD_FOO_IMPL` macro.)

This seems like a great plan—I can just put some kind of placeholder at the end of the list of headers, and when we reach that placeholder we’re done. However, there’s a catch: “If the result is _not_ a valid preprocessing token, the behavior is undefined” (C11 6.10.3.3p3, emphasis mine). This technique relies on _non-_interesting concatenations resulting in a single valid identifier, which we then throw away, but the elements of the `HEADERS` list are string literals, not numbers or identifiers. String literals can’t be concatenated with anything (except an empty macro argument, I suppose), so this approach wasn’t going to work either.

### The Placeholder Is The Key

I was feeling pretty stuck at this point, and started searching around for more creative answers, at first focusing on the case where the result was _empty._ That led me to [this Stack Overflow answer](http://stackoverflow.com/a/11742317), which included a pattern like this:^[5](#fn:empty2)

```
#define CHECK_ZERO_ARGUMENTS_IMPL() something clever here
#define CHECK_ZERO_ARGUMENTS(...) CHECK_ZERO_ARGUMENTS_IMPL __VA_ARGS__ ()

CHECK_ZERO_ARGUMENTS(a, b)
CHECK_ZERO_ARGUMENTS_IMPL a, b ()
CHECK_ZERO_ARGUMENTS()
something clever here
```

_This_ trick relies on the fact that `HAS_ZERO_ARGUMENTS_IMPL` is declared as a so-called _function-like macro,_ and therefore won’t be expanded to `something clever here` unless it’s followed by parentheses—which in this case means “unless `__VA_ARGS__` is empty”. It does have some drawbacks, namely that `__VA_ARGS__` could itself contain parentheses and that the last thing in `__VA_ARGS__` could itself be a function-like macro, but our `HEADERS` list doesn’t have either of those issues.

This got me thinking in the right direction, and led me to realize that I could do something simpler. Since all of the elements in the `HEADERS` list are strings (and therefore none have parentheses), I could just use empty parentheses as a placeholder at the end of the list.

```
#define CHECK_EMPTY_PARENS_IMPL() something clever here
#define CHECK_EMPTY_PARENS(...) CHECK_EMPTY_PARENS_IMPL __VA_ARGS__

CHECK_EMPTY_PARENS(a, b)
CHECK_EMPTY_PARENS_IMPL a, b
CHECK_EMPTY_PARENS((), b)
something clever here, b
```

Now the last step is converting to a boolean value (`0` or `1`). This is the mini-puzzle for today’s post, so I’m going to put some newlines in so that you don’t immediately look at the answer. If you’re up for a preprocessor challenge, try to figure out how to get a `0` or `1` out of this…and remember not to hardcode it for just two-element lists! (Otherwise, just scroll down.)

So. The first thing I want to do here is make sure we can handle the arbitrary results we get back when there _aren’t_ empty parentheses. Rather than write something that takes arbitrary many arguments, I hit upon the idea of just wrapping up the existing arguments in parens themselves.

```
#define CHECK_EMPTY_PARENS_IMPL() something clever here
#define CHECK_EMPTY_PARENS(...) (CHECK_EMPTY_PARENS_IMPL __VA_ARGS__)

CHECK_EMPTY_PARENS(a, b)
(CHECK_EMPTY_PARENS_IMPL a, b)
CHECK_EMPTY_PARENS((), b)
(something clever here, b)
```

And here’s where the ~~evil~~ clever bit comes in. When you expand a function-like macro, it matches parentheses and treats everything in between the parens as an argument. But macros can also _expand_ to parentheses, and _those_ don’t have to match. That means I can do this:

```
#define CHECK_EMPTY_PARENS_IMPL() ), (unused
#define CHECK_EMPTY_PARENS(...) (CHECK_EMPTY_PARENS_IMPL __VA_ARGS__)

CHECK_EMPTY_PARENS(a, b)
(CHECK_EMPTY_PARENS_IMPL a, b)
CHECK_EMPTY_PARENS((), b)
(), (unused, b)
```

And _now_ we’re in a situation where we’re deciding between one or two elements, and _that_ we know how to handle.

```
#define APPLY_N(FN, ...) FN(__VA_ARGS__)

#define CHECK_EMPTY_PARENS_IMPL() ), (unused
#define CHECK_EMPTY_PARENS(...) (CHECK_EMPTY_PARENS_IMPL __VA_ARGS__)

#define FIRST_IS_EMPTY_PARENS_IMPL(A, B, RESULT, ...) RESULT
#define FIRST_IS_EMPTY_PARENS(...) \
  APPLY_N(FIRST_IS_EMPTY_PARENS_IMPL, CHECK_EMPTY_PARENS(__VA_ARGS__), 1, 0, unused)

FIRST_IS_EMPTY_PARENS(a, b)
0
FIRST_IS_EMPTY_PARENS((), b)
1
```

With this we can fill in one of the placeholders in the main implementation. All right!

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

P.S. Since `#if` can actually evaluate arbitrary expressions, we didn’t actually need to produce a literal 1 or 0; we could have reused `COUNT` instead.

```
#define COUNT_IMPL(A, B, C, D, N, ...) N
#define COUNT(...) COUNT_IMPL(__VA_ARGS__, 4, 3, 2, 1)

#define CHECK_EMPTY_PARENS_IMPL() ), (unused
#define CHECK_EMPTY_PARENS(...) (CHECK_EMPTY_PARENS_IMPL __VA_ARGS__)

#define FIRST_IS_EMPTY_PARENS(...) \
  (2 == COUNT(CHECK_EMPTY_PARENS(__VA_ARGS__)))

FIRST_IS_EMPTY_PARENS(a, b)
(2 == 1)
FIRST_IS_EMPTY_PARENS((), b)
(2 == 2)
```

But it’s really the same idea.

### The Final Boss

At this point there’s only one problem left: how to update the `HEADERS` list (now `HEADERS_IMPL`) once we’ve included a header, or alternately how to keep track of where we are in the list. That turns out to be enough of a challenge (and intricate solution) to deserve a whole post of its own, so stay tuned for “[Macromancy: Part 2](https://belkadan.com/blog/2016/08/Macromancy-2/)”!

1. Why `clang -E` and not `cpp`? `cpp` operates in so-called “traditional mode”, which handles whitespace differently from modern C preprocessing. Most of the examples should still work, but have slightly different output. [↩︎](#fnref:cpp)
2. One thing odd here is that standard library headers are usually referred to using angle brackets `<>` rather than quotes `""`. However, “[t]he method by which a sequence of preprocessing tokens between a `<` and a `>` preprocessing token pair or a pair of `"` characters is combined into a single header name preprocessing token is implementation-defined” (C11 6.10.2p4). Since string literals are considered single preprocessing tokens, they’re a lot more likely to behave as expected. In practice, quoted includes always fall back to angle-bracket includes if the header can’t be found (C11 6.10.2p3), so unless someone has their _own_ header named “stdio.h” (unlikely) we’re probably okay. [↩︎](#fnref:quotes)
3. What about zero elements? Technically this isn’t allowed—the C standard says that “there shall be more arguments in the invocation than there are parameters in the macro definition (excluding the `...`)” (C11 6.10.3p4). However, both GCC and Clang support this as an extension to the language, and you can make the `COUNT` macro work with it by adding a `0` to the end. [↩︎](#fnref:empty)
4. This is the only example that doesn’t work in “traditional mode” preprocessing. I didn’t look into why because—as will be described shortly—this approach was a dead end anyway. [↩︎](#fnref:cpp2)
5. In a previous footnote I noted that passing zero arguments to a variadic macro is technically not valid C, but if you’re willing to depend on compiler-provided language extensions, this might still be a useful thing to do. [↩︎](#fnref:empty2)

This entry was posted on [August](https://belkadan.com/blog/2016/08) 07, [2016](https://belkadan.com/blog/2016) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [C++](https://belkadan.com/blog/tags/cxx)
