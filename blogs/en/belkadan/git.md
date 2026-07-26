---
title: Git
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/git'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c5471e3f9056403c'
translated: false
---

> 原文：[Git](https://belkadan.com/blog/tags/git)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=git)

26 November 2023

[A few days ago Julia Evans posted this:](https://social.jvns.ca/@b0rk/111462736760795943)

> has anyone made a read-only FUSE filesystem for a git repository where every commit is a folder and the folder contains all the files in that commit?
> 
> the idea is that you could just run `cd COMMIT_ID` and poke around instead of checking out the commit
> 
> and maybe the branches could be symbolic links to the commit folders?

And I _did_ in fact do something very like that, back when I was [playing with FUSE](https://belkadan.com/blog/2020/07/Suffusion/)! But I never put it up anywhere cause it had an annoying build process, and didn’t seem to add much, and—

[(Continue reading…)](https://belkadan.com/blog/2023/11/GitMounter/?tag=git)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Git](https://belkadan.com/blog/tags/git), [Source code](https://belkadan.com/blog/tags/source-code), [Filesystems](https://belkadan.com/blog/tags/filesystems)

## [Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/?tag=git)

03 April 2020

When I was getting the code in the [previous post](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/) ready to share, I ran into a problem: my checkouts of LLVM and Swift were _shallow clones,_ i.e. git repositories that _don’t_ store the full history of each branch. Working with those locally is surprisingly easy; trying to set them up on a server using `git push` is a bit trickier. While trying to figure out what was going on, I was dismayed by the lack of up-to-date documentation about shallow repositories, even on my usual go-to site, [git-scm.com](https://www.git-scm.com/doc). So here’s a collection of information I’ve gathered about shallow repositories.

[(Continue reading…)](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/?tag=git)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Git](https://belkadan.com/blog/tags/git), [Apache](https://belkadan.com/blog/tags/apache), [Running a website](https://belkadan.com/blog/tags/running-a-website)

## [Flexible Identities in git](https://belkadan.com/blog/2020/02/Flexible-Identities-in-git/?tag=git)

06 February 2020

> Noticed a colleague changed their name from traditionally-gender-A to tradtiionally-gender-B, and so went to clean up my comments of the form "thanks, [name]" to just "thank you".  
>   
> Doesn't really hide anything, but at the very least they won't be deadnamed if looking at old PRs?
> 
> — Jordan Rose (@UINT_MIN) [April 13, 2019](https://twitter.com/UINT_MIN/status/1116926726980820992?ref_src=twsrc%5Etfw)

> Git is terrible for this sort of identity-severing change thanks to burning the committer's name into the validity of the branch, and we-the-industry should probably do something.
> 
> — Jordan Rose (@UINT_MIN) [April 13, 2019](https://twitter.com/UINT_MIN/status/1116926727647707136?ref_src=twsrc%5Etfw)

[(Continue reading…)](https://belkadan.com/blog/2020/02/Flexible-Identities-in-git/?tag=git)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Git](https://belkadan.com/blog/tags/git), [Diversity in tech](https://belkadan.com/blog/tags/diversity-in-tech)

## Older Posts

1. 2020-01-22[Setting up gitweb on Shared Hosting](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/?tag=git)
2. 2012-10-02[Git Tricks](https://belkadan.com/blog/2012/10/Git-Tricks/?tag=git)
3. 2011-06-27[git add](https://belkadan.com/blog/2011/06/git-add/?tag=git)

### Possibly Related Tags

- [Apache](https://belkadan.com/blog/tags/apache)
- [Diversity in tech](https://belkadan.com/blog/tags/diversity-in-tech)
- [Filesystems](https://belkadan.com/blog/tags/filesystems)
- [Running a website](https://belkadan.com/blog/tags/running-a-website)
- [Source code](https://belkadan.com/blog/tags/source-code)
- [Swift](https://belkadan.com/blog/tags/swift)
