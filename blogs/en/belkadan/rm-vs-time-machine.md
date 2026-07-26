---
title: rm vs. Time Machine
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:d02791dfb73b6e08'
translated: false
---

> 原文：[rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Priorities](https://belkadan.com/blog/2011/07/Priorities/)

[Using Clang from SVN in Xcode](https://belkadan.com/blog/2011/07/Using-Clang-from-SVN-in-Xcode/) »

« [Priorities](https://belkadan.com/blog/2011/07/Priorities/?tag=mac-os-x)

[Keyboard Adventures](https://belkadan.com/blog/2012/04/Keyboard-Adventures/?tag=mac-os-x) »

« [Priorities](https://belkadan.com/blog/2011/07/Priorities/?tag=unix)

[Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/?tag=filesystems) »

## [rm vs. Time Machine](#)

Public Service Announcement: if a Time Machine backup fails, it will leave behind a file with an extension of `inprogress`. (It’s actually a folder.) If you have a hard time deleting it, **do not** use `rm`! It will erase files from **all** backups, instead of just the one in progress. Instead, trash the `inprogress` file from the Finder and Empty Trash as usual. It might take a while, but it will Do The Right Thing.

You could also leave the file alone and just try to backup again; Time Machine will clear out the failed `inprogress` file when the next backup succeeds.more

Yes, this happened to me today. Fortunately, I have about 8GB of game data in my Applications folder (alphabetically first), so I had misgivings and stopped before losing anything really important in my backups.

---

Why does this happen? First recall the concept of _hard links_. Hard links are to files as references are to objects in C++, Java, or most other OO languages. And just as more than one reference can point to the same object, most modern filesystems allow more than one filename (“link”) to point to the same file. If you remove one link, the file still exists; it’s only when you remove _all_ the links that the file is actually deleted. Of course, most files only have one link, so this distinction rarely matters.[1](#fn:softlinks)

This alone wouldn’t be a problem; in fact, it would mean that even if Time Machine shares data for files that haven’t changed between backups (which it does), it should be safe to use the Unix tool `rm` to delete one backup. Anything that shows up in another backup will still have at least one link left from that backup, and so won’t be deleted, right?

Unfortunately, there’s more going on here. Time Machine sharing data for files that haven’t changed does keep disk space down, but without anything else you’d need to recreate the entire directory tree for every backup. And with hourly/daily/weekly backups, eventually you’ll hit the limit for the _number of folders_ on your hard drive. (Plus, folders do not take 0 space to store…they still cost _something_.)

As a first optimization, you might say if an entire directory tree hasn’t changed, we can just use an alias or symlink that points to the previous backup’s version. The trouble here comes when you start trimming old backups: you now have to figure out _which_ directory trees are in use by later backups, and move them into those later backups. Doable, but annoying. Plus, most filesystems place a limit on how long you can chain your symlinks, so if you have something from 64 weeks ago (a chain of 64 or more symlinks), the filesystem may give up.[2](#fn:why)

Apple chose to do something more radical: they allowed Time Machine to create hard links to directories. Normally this is forbidden because it can create directory loops, which would completely confuse any tool that tries to find all files and folders on a disk (like, say, Spotlight). Actually, there are a lot of potential problems there. So on Macs, _only_ the root user can make symlinks to directory, and then Time Machine runs with root privileges.

And from that the picture is clear. The trusty `rm` tool only knows one way to remove directories: remove all links in the directory, then remove the directory itself.[3](#fn:order) It never stops to consider that the _directory_ might be shared, via hard links, with another location on the filesystem. The correct algorithm should say “does this directory have more than one hard link? if so, just remove this one”. Unfortunately, because hard links to directories are usually forbidden, it might be hard to ask how many links it currently has!

Empty Trash does the right thing. Make sure you do too.

1. Why is it called a _hard_ link? It turns out there’s another kind of link called a _soft_ link, also known as a _symbolic_ link or “symlink”. A symbolic link is nothing more than a path to the real file, like a forwarding address. (“Oh, the file you want is _really_ at…”) Symlinks have a couple of advantages:

    - You can move a new file in place of an old one, and the link will then refer to the new file.
    - They can refer to things on other filesystems (such as a network file-share).
    - They can point to directories, which can be dangerous for hard links.

  But they don’t prevent their target from being deleted, and if the target is moved they won’t be updated—the downside of the features mentioned above. So the two types of links aren’t interchangeable—you have to pick the right one for the job.

  Note that symlinks are not the same as _aliases_ (on Mac OS X) or _shortcuts_ (Windows). These are somewhere in between symlinks and hard links, in that they _are_ attached to a certain file and will follow it if you move that file around. But they still don’t keep the file from being deleted, and they can refer to directories and things on other filesystems. [↩︎](#fnref:softlinks)
2. Why is there a limit? To prevent endless recursion if a symlink/alias points to _itself_. Keep reading. [↩︎](#fnref:why)
3. This is important: if you remove a non-empty directory, you now have no way to access the files in it, which means you have no way to _delete_ the files in it. So the filesystem doesn’t let you delete non-empty directories directly, although Empty Trash is smart enough to delete their contents first. [↩︎](#fnref:order)

This entry was posted on [July](https://belkadan.com/blog/2011/07) 22, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS X](https://belkadan.com/blog/tags/mac-os-x), [Unix](https://belkadan.com/blog/tags/unix), [Time Machine](https://belkadan.com/blog/tags/time-machine), [Filesystems](https://belkadan.com/blog/tags/filesystems)
