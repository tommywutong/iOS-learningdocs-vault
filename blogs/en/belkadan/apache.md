---
title: Apache
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/apache'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:186d7c03b2688ddd'
translated: false
---

> 原文：[Apache](https://belkadan.com/blog/tags/apache)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/?tag=apache)

03 April 2020

When I was getting the code in the [previous post](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/) ready to share, I ran into a problem: my checkouts of LLVM and Swift were _shallow clones,_ i.e. git repositories that _don’t_ store the full history of each branch. Working with those locally is surprisingly easy; trying to set them up on a server using `git push` is a bit trickier. While trying to figure out what was going on, I was dismayed by the lack of up-to-date documentation about shallow repositories, even on my usual go-to site, [git-scm.com](https://www.git-scm.com/doc). So here’s a collection of information I’ve gathered about shallow repositories.

[(Continue reading…)](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/?tag=apache)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Git](https://belkadan.com/blog/tags/git), [Apache](https://belkadan.com/blog/tags/apache), [Running a website](https://belkadan.com/blog/tags/running-a-website)

## [HTTPS and Name-based Virtual Hosting](https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/?tag=apache)

28 August 2008

If you’ve been running your own server for a while, eventually you’ll start getting privacy jitters and want to use HTTPS, at which point you’ll either happily set it up with minimal difficulty (if you’re running a single site) or realize frustratedly that you can’t use HTTPS with name-based virtual hosts. To quote the Apache site:

> The reason is very technical, and a somewhat “chicken and egg” problem. The SSL protocol layer stays below the HTTP protocol layer and encapsulates HTTP. When an SSL connection (HTTPS) is established Apache/mod_ssl has to negotiate the SSL protocol parameters with the client. For…

[(Continue reading…)](https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/?tag=apache)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Apache](https://belkadan.com/blog/tags/apache), [Unix](https://belkadan.com/blog/tags/unix)

### Possibly Related Tags

- Git
- Running a website
- Unix
