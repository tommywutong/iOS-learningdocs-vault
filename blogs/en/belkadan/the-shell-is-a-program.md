---
title: The Shell is a Program
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2024/12/The-Shell-is-a-Program/'
original_language: en
published: 2024-12-26
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dad6492306fffa63'
translated: false
---

> 原文：[The Shell is a Program](https://belkadan.com/blog/2024/12/The-Shell-is-a-Program/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [AnyObject](https://belkadan.com/blog/2024/07/AnyObject/)

[ROSE-8 in customasm](https://belkadan.com/blog/2025/01/ROSE-8-in-customasm/) »

« [rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/?tag=unix)

« [Online Communication](https://belkadan.com/blog/2024/01/Online-Communication/?tag=user-experience)

## [The Shell is a Program](#)

I have a friend who switched to Linux because they didn’t want to pay for a new license for Windows and thereby end up running modern Windows. They’re not very computer-minded, so troubleshooting doesn’t come naturally, and anything that requires dropping down to the command line is something that has to be done by rote. And on one occasion, when I asked them to run something, they asked where to type it in.

…

If you are a technical person familiar with Linux, you know there’s only one place to type things in: “the shell”. Or “the command line”, or “the terminal”. Technically these are all [slightly different things](https://askubuntu.com/questions/506510/what-is-the-difference-between-terminal-console-shell-and-command-line/506628#506628), but those distinctions don’t usually matter. The important thing is that the shell is the default place to run _any_ textual command. So it threw me when my friend asked “where do I put this in”.

I started thinking about how to explain this. _The terminal is basically talking directly to the operating system. That’s why text commands go there._

And, well, that’s not totally true, is it? If this were Windows, you _could_ do system manipulation stuff through cmd.exe, but you might also do it in [regedit](https://www.lifewire.com/windows-registry-2625992), or somewhere deep in the system settings, or through some dedicated program. On a [Classic](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/) Mac, there was no command line; the closest equivalent would be “running an AppleScript” and that’s not an interactive environment. (Also, you wouldn’t tell someone to type in an AppleScript, you’d just let them download a file.) On an embedded system, you might have standard input and output channels over a wired connection, but they may or may not look like shell commands. To some extent Linux is the odd one out here.

And it doesn’t even stop there. Most commands are going to be generic enough that they’ll work in any shell, but maybe a few are going to rely on `bash` syntax. What if someone has switched to `zsh`, `fish`, or nushell? Or prefers the venerable `ksh` or `tcsh`. This usually isn’t a problem because `zsh` and `bash` and `ksh` support a lot of the same extended syntax, and most systems have _one_ of those as a default these days, and if you’ve switched to something else, you at least know you’ve done it. Probably. It does underscore the point, though: your shell is a program, interpreting the commands you give it.

So, then, let’s turn it around. Why _is_ the shell a default line to the operating system? Well, because the main thing it does is _run other programs._ (I’ve said on occasion that shell syntax is a DSL for [`posix_spawn`](https://pubs.opengroup.org/onlinepubs/009696899/functions/posix_spawn.html).) And on top of that, Unix programs are often designed to be non-interactive, doing everything you need via arguments provided when the program is launched. You could use any program to do this—a Python script, a compiled executable, even a [custom GUI for running commands](https://belkadan.com/hermitcrab/)^[1](#fn:crab)—but for 50 years of Unix it’s been _assumed_ that there’s a shell available and that this is a good default way to write programs. And so we share commands as text instead of executable scripts or files.

But that idea that the shell _is_ the default, on any OS, is not some innate truth about computers, especially now that a [teletype](https://sfba.social/@williampietri/113387049693365012) isn’t the most common way to interact with them. It’s just a program that comes installed with your system. And people have to learn that, just like everything else about how to use a computer.

1. Okay, [Hermit Crab](https://belkadan.com/hermitcrab/) uses a shell too; it doesn’t try to parse commands on its own. It certainly could, but then you’d lose out on all the niceties a shell provides even in non-interactive mode, like tilde-aliases for home directories and substitution of environment variables. [↩︎](#fnref:crab)

This entry was posted on [December](https://belkadan.com/blog/2024/12) 26, [2024](https://belkadan.com/blog/2024) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Unix](https://belkadan.com/blog/tags/unix), [User experience](https://belkadan.com/blog/tags/user-experience)
