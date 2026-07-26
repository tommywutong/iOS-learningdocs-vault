---
title: Soft Orders of Magnitude
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/10/Soft-Orders-of-Magnitude/'
original_language: en
published: 2023-10-09
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c4280e09ad2a0c9b'
translated: false
---

> 原文：[Soft Orders of Magnitude](https://belkadan.com/blog/2023/10/Soft-Orders-of-Magnitude/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [There's No Such Thing As "Implicitly Atomic"](https://belkadan.com/blog/2023/10/Implicity-Atomic/)

[Type Erasure in Rust](https://belkadan.com/blog/2023/10/Type-Erasure-in-Rust/) »

« [Misleading Metrics and UX Tradeoffs](https://belkadan.com/blog/2018/04/Misleading-Metrics/?tag=user-experience)

[Online Communication](https://belkadan.com/blog/2024/01/Online-Communication/?tag=user-experience) »

## [Soft Orders of Magnitude](#)

If there’s one safe thing to complain about for any software development process, it’s that build times are too long. It doesn’t matter if it’s a minute, five minutes, or a hour—it could always be shorter. No one’s going to argue with that, right?more

Obviously that’s _too_ glib—someone might wait an hour for a build, or at least for CI, but only if they feel it’s doing commensurate work. This was on our minds a lot on my first full-time team at Apple, the [Clang Static Analyzer](https://clang-analyzer.llvm.org) team. The analyzer is in some ways an _inherently_ slow tool: it does a path-sensitive walk through each function in your program, which has a naive order of growth of O(2number of conditions). Yet with some clever tricks—and the limitations of C—it was fast enough and caught useful enough bugs that not only did people run it, some of them ran it on _every build._

We talked a fair bit about how we could make the analyzer faster…and on the flip side, how to make sure new features wouldn’t slow it down too much. What we came to realize was that absolute or percentage speedups, while obviously important, weren’t going to change how someone used the tool unless it crossed a “soft order of magnitude”:

- The task completes instantly.
- There is a short pause, maybe 1-2 seconds, but then it’s done.
- There is a long pause, maybe 3-20 seconds, that you have to wait.
- Time to check your email / messages / notifications while you wait.
- Time to refill your water.
- Time to work on something else for a bit.
- Long enough to go to lunch.
- Long enough to go home for the day.
- Long enough to go home for the weekend. (I’ve never worked on anything with a task this long, thankfully.)

The uneven nature of these categories means that improvements are not distributed the same way for all users. Oh, you got CI to take 8 minutes instead of 16? That’s not a _bad_ thing, but I’m still going to switch tasks rather than just wait for it. But taking 30 seconds instead of 1 minute means I might stay at my desk instead of getting up for a break.[1](#fn:break)

You can use the list in reverse, too. It’s okay to make things a little slower, until they cross a threshold. As a specific example, this is why the [`tsc`](https://www.typescriptlang.org) step in a particular work project is more frustrating than the [`cargo`](https://doc.rust-lang.org/cargo/) step, even though the `cargo` step takes longer. The `tsc` step _was_ a short pause, but now it has crossed over into a long pause instead. Whereas the `cargo` step has always been a long pause.

One way to make the tool _feel_ faster is to make it responsive, with progress updates as it works. Not only does this make it feel like many small tasks instead of one big task, it helps add to the user’s idea of whether the work is commensurate—whether it makes sense that it takes this much time. (Though be careful of [bad progress bars](https://mastodon.social/@JenMsft/110913130590010492).) By default `cargo` does this and `tsc` doesn’t, and I think it would help; time to look up those progress flags!

Of course, if we assume _projects_ have a continuous size distribution, we’d always be crossing a threshold for _somebody._ So this list may not be that helpful for working on a tool, in practice. But it _can_ be helpful for one-off things like build scripts, or CI, that are only ever used on one project, by one organization. Here, you can stay within one soft order of magnitude and do whatever you want, but crossing a threshold—in either direction—will likely have a noticeable effect on productivity.

---

P.S. Obligatory “if you care so much about build times, why is Swift so much slower to compile than Objective-C?” I can think of three main reasons:

- No header files means the compiler has to be conservative about possible cross-file dependencies. (This was especially bad for incremental builds while I was still at Apple but it got massively improved by [David Ungar](https://forums.swift.org/u/david_ungar2/), [Robert Widmann](https://mastodon.social/@cfi), and others around when I left.)
- Making modules the base compilation unit makes it harder to show progress. If you open an Xcode build log these days, you’ll see that even in a debug build, the compiler splits up the work based on the number of cores you have, with each process compiling several files. This shortens the overall build time, but means there’s no progress for a while, and then suddenly a bunch of things finish at once.
- [It’s possible we bit off more than we could chew with the type system.](https://belkadan.com/blog/2021/08/Swift-Regret-Type-based-Overloading/) (…But as I say in that post, I’m not an expert; I don’t know if this is really the problem for most people or just a convenient scapegoat.)

1. Don’t forget to take breaks though, especially if you work from home! [↩︎](#fnref:break)

This entry was posted on [October](https://belkadan.com/blog/2023/10) 09, [2023](https://belkadan.com/blog/2023) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [User experience](https://belkadan.com/blog/tags/user-experience)
