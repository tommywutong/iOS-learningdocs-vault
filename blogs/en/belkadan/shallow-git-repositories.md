---
title: Shallow Git Repositories
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/'
original_language: en
published: 2020-04-03
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a1d8bdc8c80eebfb'
translated: false
---

> 原文：[Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/)

[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) »

« [Flexible Identities in git](https://belkadan.com/blog/2020/02/Flexible-Identities-in-git/?tag=git)

[GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=git) »

« [Setting up gitweb on Shared Hosting](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/?tag=apache)

« [Setting up gitweb on Shared Hosting](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/?tag=running-a-website)

[Re: Twitter](https://belkadan.com/blog/2022/12/Re-Twitter/?tag=running-a-website) »

## [Shallow Git Repositories](#)

When I was getting the code in the [previous post](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/) ready to share, I ran into a problem: my checkouts of LLVM and Swift were _shallow clones,_ i.e. git repositories that _don’t_ store the full history of each branch. Working with those locally is surprisingly easy; trying to set them up on a server using `git push` is a bit trickier. While trying to figure out what was going on, I was dismayed by the lack of up-to-date documentation about shallow repositories, even on my usual go-to site, [git-scm.com](https://www.git-scm.com/doc). So here’s a collection of information I’ve gathered about shallow repositories.

### What is a shallow repository?

I’ll start with the definition from [`man gitglossary`](https://www.git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefshallowrepositoryashallowrepository) (emphasis mine):

> **A shallow repository has an incomplete history** some of whose commits have parents cauterized away (in other words, Git is told to pretend that these commits do not have the parents, even though they are recorded in the commit object). This is sometimes useful when you are interested only in the recent history of a project even though the real history recorded in the upstream is much larger. A shallow repository is created by giving the `--depth` option to `git-clone`(1), and its history can be later deepened with `git-fetch`(1).

This explains what a shallow repository is and why you might want one. The implied part of “even though the real history…is much larger” is that you want to avoid the bandwidth and/or storage costs of fetching / keeping around a whole upstream repository.

The last sentence is technically still correct, but there are several ways to get a shallow repository these days:

- `--depth <N>` is the oldest way, checking out the last `N` commits from a branch
- `--shallow-since <DATE>` includes commits from `DATE` and since but not older; the [git internal documentation](https://github.com/git/git/blob/9fadedd637b312089337d73c3ed8447e9f0aa775/Documentation/technical/protocol-capabilities.txt#L200-L207) says the search is equivalent to `git rev-list --max-age=<DATE>`
- `--shallow-exclude <REVISION>` excludes `REVISION` and its ancestors. You can use a remote tag or branch name here too.
- `--deepen <N>` adds an additional `N` commits to the branch in an existing shallow repository. `N` must be positive, though I wouldn’t be totally surprised if support for negative values was added in the future.

These are documented under [`git-clone`](https://git-scm.com/docs/git-clone) and [`git-fetch`](https://git-scm.com/docs/git-fetch).

An interesting note is that you can use these options on an _existing repository_ to adjust where your shallow history ends. Being git, you won’t see space savings from _shortening_ your history this way without running `git gc --prune=now` to make sure the now-unreferenced commits get deleted.

When you run `git log` on a shallow repository, you’ll see the “end” commits marked as “grafted”. This refers to the implementation of shallow repositories, which used to just use the _grafts_ feature of [`git-replace`](https://git-scm.com/docs/git-replace) and now have some additional bookkeeping in the `.git/shallow` file. (I didn’t look into this too much.)

If you want to get the full history of a branch, you can do that with `git fetch --unshallow`. This has been around nearly as long as the `--depth` option (the first bit of shallow repositories that got implemented), and will fix pretty much any problems you have with a shallow repository…at the cost of it no longer being shallow.

### Pushing a shallow repository

It’s one thing to push from a shallow repository to its original upstream, which has all the commits. It’s another to push to a _new_ repository when _you_ don’t have all the commits! That throws a wrench into the usual way to establish a new server-side repository:

If you try to do this, you’ll get this sort of response:

```
 ! [remote rejected]   dev -> dev (shallow update not allowed)
```

_However,_ if you do have control over the server, you can enable shallow pushes with the [`receive.shallowUpdate` config option](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receiveshallowUpdate).

Now you’ve got a shallow upstream repository, and one with no connection to the original repository you cloned from. This has some of the benefits of a local shallow repo, but since it’s going to be a source that _others_ clone from, it’s going to have some additional sharp edges.

### Sharp edges of a shallow upstream

- The so-called [“Dumb HTTP” server](https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols#_the_http_protocols) setup, which is what I was previously using on [https://belkadan.com/source/](https://belkadan.com/source/), doesn’t support shallow fetches or clones, but it _also_ doesn’t support shallow upstream repositories, and doesn’t produce a good error message if you try to fetch from a shallow repository. I set up the “smart” HTTP server to take care of this; see [below](#appendix) for more information.
- If you try to do a shallow fetch from a shallow repository, but accidentally specify an older start point than the shallow repository’s “ends”, you’ll get a bad error message about “failing to traverse parents”.
- If you want to “unshallow” a clone of the shallow upstream, you’ll have to do it by adding the original upstream as a second remote, and then using `git fetch --unshallow original-upstream`. Running `git fetch --unshallow shallow-upstream` still does something reasonable, though: it fetches everything the shallow upstream has.
- Of course, if the original upstream goes away, that history is (potentially) gone forever.

I think no one’s really focused on the user experience of shallow upstream repositories (yet?), but as far as I can tell they work fine as long as you do things that will succeed (as opposed to producing error messages).

### Appendix: Adding Smart HTTP support to a Gitweb setup

In a [previous article](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting) I talked about setting up git hosting under Apache using [gitweb](https://git-scm.com/docs/gitweb); one of my criteria for success was using the same URL for web browsing as for cloning. Git’s “smart” HTTP backend is supposed to dramatically cut down on HTTP requests when fetching, and can save overall bandwidth too, but I wasn’t sure of the CPU cost of running that on my shared hosting. And it _is_ one more moving piece. But hosting shallow repositories meant I needed a smart server, and so I set to work modifying my existing configuration.

#### Part 1: Running `git-http-backend` without being able to edit Apache’s root configuration

As I mentioned in the original article, I can’t edit my web server’s main configuration files; all I can do is add per-directory configuration. For gitweb, that meant putting the script directly in with the rest of my website files.^[1](#fn:cgi-bin) But gitweb’s just a little(ish) Perl script, while [`git-http-backend`](https://git-scm.com/docs/git-http-backend) is a whole compiled program. Do I really have to copy that into my website?

Fortunately, someone else has gone through this before. Tiago Alves Macambira documented their own approach to [hosting Git repositories on a shared hosting plan](https://github.com/tmacam/private-git-on-dreamhost) (Dreamhost), and while their goals were different from mine they’ve already solved this particular problem. Their answer? Write a wrapper shell script. Here’s mine, which I just named `git-http-backend.cgi`:

That `PATH` line is because the install of `git` in `/usr/bin` is much older than the one my hosting provides to users, and I want to use the new one.

This works, and I could test it with [`git ls-remote`](https://git-scm.com/docs/git-ls-remote.html):

```
git ls-remote https://belkadan.com/source/git-http-backend.cgi/swift
```

(Note: at the time I wrote this article I left this endpoint up, but I might close it down in the future so that git-http-backend is only run through the pretty URLs.)

#### Part 2: Supporting pretty URLs

The final goal here was for `git clone https://belkadan.com/source/swift` to work, just like it did for my existing repositories. This turned out to be pretty straightforward; taking a hint from the “[Accelerated static Apache 2.x](https://git-scm.com/docs/git-http-backend#Documentation/git-http-backend.txt-AcceleratedstaticApache2x)” configuration in the `git-http-backend` docs, I added this line to my `.htaccess` file, ahead of my previous rules for gitweb:

```
RewriteRule \
  ^[^/]+/(HEAD|info/refs|objects/info/.+|git-upload-pack)$ \
  git-http-backend.cgi/$0 [L]
```

This basically says “send requests in an immediate subdirectory for `HEAD`, `info/refs`, `git-upload-pack`, and anything in `objects/info/` to `git-http-backend.cgi`”.^[2](#fn:git-receive-pack) Requests for existing objects or packfiles will still be served through Apache, and any other requests will go to gitweb through the rest of my configuration. (That `[L]` at the end stands for “last”, which keeps the requests intended for `git-http-backend` from subsequently being routed to gitweb.)

Once again I tested it with `git ls-remote`:

```
git ls-remote https://belkadan.com/source/swift
```

and everything seems to be in order.

1. I suppose I could have used a separate [cgi-bin](https://httpd.apache.org/docs/2.4/howto/cgi.html#nonscriptalias) directory, but that always struck me as weird and also _more_ likely to be accidentally insecure if you’re already guarding against arbitrary uploads. [↩︎](#fnref:cgi-bin)
2. The `git-http-backend` docs also include `git-receive-pack` as a possible path, but that’s only used for _pushing_ through HTTPS, and I’m not using that. [↩︎](#fnref:git-receive-pack)

This entry was posted on [April](https://belkadan.com/blog/2020/04) 03, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Git](https://belkadan.com/blog/tags/git), [Apache](https://belkadan.com/blog/tags/apache), [Running a website](https://belkadan.com/blog/tags/running-a-website)
