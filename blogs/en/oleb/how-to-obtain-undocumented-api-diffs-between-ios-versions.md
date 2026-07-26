---
title: How to Obtain Undocumented API Diffs Between iOS Versions
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/02/how-to-undocumented-ios-api-diffs/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:d102827525011ec1'
translated: false
---

> 原文：[How to Obtain Undocumented API Diffs Between iOS Versions](https://oleb.net/blog/2013/02/how-to-undocumented-ios-api-diffs/)　·　Ole Begemann

# How to Obtain Undocumented API Diffs Between iOS Versions

Just in case you were wondering how exactly I compiled the [list of undocumented iOS API changes for my last article](https://oleb.net/blog/2013/02/new-undocumented-apis-ios-6-1/), let me walk you through it.

# Clone the iOS Runtime Headers Repository

Every time Apple releases a new iOS version, [Nicolas Seriot](http://seriot.ch/) does the excellent job of dumping all existing classes and APIs into his [iOS Runtime Headers](https://github.com/nst/iOS-Runtime-Headers) repository on GitHub. So let’s go ahead and clone the repo locally. Open a Terminal window and enter these commands:

```
> git clone https://github.com/nst/iOS-Runtime-Headers.git
> cd iOS-Runtime-Headers
```

# git difftool

We obtain the list of changes between two iOS version by diffing different commits in the repository. When I first tried this a few days ago, I got a lot of false positives – the diff tool reported thousands of files as changed that really didn’t. All that had changed in most files was the order of the method declarations.

When [I pointed this out to Nicolas](https://github.com/nst/iOS-Runtime-Headers/issues/1), he quickly came up with a script that sorted the declarations and rebuilt the repository with the sorted versions of the files. Thanks Nicolas!

This is the command to show all the differences between two iOS versions:

```
> git difftool 6.0 6.1
```

Nicolas has tagged each iOS version in the repository. Note that we can refer directly to the tags here; we don’t have to specify a commit by their SHA1 hash.

# Kaleidoscope

I am assuming here that you have configured a diff tool in your Git configuration. The best tool by far for this purpose [Black Pixel’s new Kaleidoscope 2](http://www.kaleidoscopeapp.com), especially because it can deal with multiple files and folders at once. If you have Kaleidoscope, you can tell it to configure itself as your default diff and merge tool right from the UI.

When you run the `git difftool` command, Kaleidoscope launches and will take a while to compile all the changes. In all, there are 500 modified classes between iOS 6.0 and 6.1:

![Screenshot of Kaleidoscope 2 showing API diffs between iOS 6.0 and 6.1](https://oleb.net/media/kaleidoscope2-screenshot-api-diffs-ios-6.0-6.1.png)

<sub>Kaleidoscope 2 showing API diffs between iOS 6.0 and 6.1.</sub>

If you don’t have Kaleidoscope 2, you can use Apple’s FileMerge tool, too:

```
> git difftool --tool=opendiff 6.0 6.1
```

The problem with FileMerge is that it can only handle one file at a time. FileMerge will launch with the first file. When you are done with it, you have to quit FileMerge for it to relaunch immediately with the next file. Doing this 500 times is not very comfortable.

Another option is to show the API diffs directly in the Terminal. Then, when a change catches your eye, open just this specific file in FileMerge. For example:

```
> git diff 6.0 6.1
> git difftool --tool=opendiff 6.0 6.1 -- Frameworks/AVFoundation.framework/AVAssetInspector.h
```
