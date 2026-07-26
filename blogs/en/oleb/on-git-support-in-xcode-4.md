---
title: On Git Support in Xcode 4
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/on-git-support-in-xcode-4/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:13dc47607a30cd79'
translated: false
---

> 原文：[On Git Support in Xcode 4](https://oleb.net/blog/2011/05/on-git-support-in-xcode-4/)　·　Ole Begemann

# On Git Support in Xcode 4

When Apple revealed at last year’s WWDC that Xcode 4 would have native [Git](http://git-scm.com/) support, it was one of the features I looked forward to the most. I had already adopted Git for all my projects at the time and the prospect of having version control integrated into the IDE was exciting. Now, having worked with Xcode 4 for a few months, I am quite disappointed with its Git integration.

# Good for diffs and simple merges

Let’s start with the good parts. One of the new UI features in Xcode 4 is the [version editor](http://developer.apple.com/technologies/tools/whats-new.html#version-editor), and it is indeed pretty cool. With its Time Machine-like timeline, it lets you compare any two versions in your repository in a very nice and clean diff view. It’s definitely one of the best diff implementations I have used.

The same interface is used when doing a merge. Best of all, you can edit the resulting file directly in the merge view if none of the four standard merge options do the right thing. This works mostly well as long as there is no merge conflict in your .pbxproj project file.

[![The Xcode 4 Version Editor](https://oleb.net/media/xcode4-version-editor-600px.jpg)](https://oleb.net/media/xcode4-version-editor-600px.jpg)

<sub>The Xcode 4 Version Editor is pretty cool.</sub>

# Bad for committing and “complex” merges

The problems start with this quote from the [Xcode 4 User Guide](http://developer.apple.com/library/ios/documentation/ToolsLanguages/Conceptual/Xcode4UserGuide/SCM/SCM.html#//apple_ref/doc/uid/TP40010215-CH7-SW12):

> In so far as is possible, Xcode provides a consistent user interface and workflow for users of either Subversion or Git.

Sounds well-intentioned but the underlying models of Subversion and Git are so radically different that I suppose it’s nearly impossible to provide a consistent UI and workflow for both that works well at the same time. For example, committing is a one-step process in SVN while Git users first stage the changes they want to commit to [the index](http://book.git-scm.com/1_the_git_index.html) and then commit from there. Xcode 4 has no concept of staging. When you add a new file to the project, it will automatically be staged for the next commit. And while you can uncheck entire files in the commit dialog, it is impossible to stage only some of a file’s changes, something I do frequently in [GitX](https://github.com/brotherbard/gitx/downloads). Similarly, Xcode does not support advanced Git features like [stashing](http://book.git-scm.com/4_stashing.html).

Merging branches becomes a problem as soon as Git encounters a merge conflict in your project file. The most common source of such conflicts is that you added one or more files to the project in both branches. Unfortunately, creating files is a very common activity when developing a new feature (which is the reason you have created the branch in the first place). In such cases, Xcode just indicates the fact that there is a conflict and denies the merge. It’s back to the command line to merge the XML project file manually. I really don’t get this: the one area where Xcode could actually do a _better_ job than a general-purpose Git app (because it knows the file format of the project file), it refuses to help you.

All this makes it much harder and sometimes impossible to use Git as intended by branching and merging often, and preferring multiple finegrained commits over fewer larger ones. Xcode wants you to remain stuck in your Subversion habits.

Here are two more annoyances where Xcode could use its knowledge about a project but doesn’t:

- When creating a new project, you can let Xcode create a Git repository for you automatically, but it doesn’t create a fitting `.gitignore` file for you. It’s not as bad as it could be because the default build location is no longer inside the project folder in Xcode 4 but I’d still like to exclude my user-specific settings from the repository.
- When switching branches, Xcode should know that the folder structure has just changed and silently close files that are not present in the newly checked out branch. Instead, we get the same “The file has disappeared” message we would get if we used an external tool to switch branches.

# Looks like a Subversion wrapper

I love this quote by Martin Pilkington in the conclusion of his [extensive Xcode 4 review](http://pilky.me/view/15):

> Xcode 4 is an interesting contraption. It has 4.0 as its version number, yet it is almost a 1.0. Xcode 1 to 3.2 were almost transitional, helping the migration from Project Builder to what we have now. In a sense Xcode 4 shouldn’t be judged on what it is, but what it shows it will be. The one thought that keeps popping into my head while using it is that there is a lot of cool new stuff, but it is lacking. The foundations are pretty much all there to build an Xcode that can compete with the likes of Visual Studio and Eclipse on all fronts. They just need fleshing out more.

This is exactly how I feel about Xcode’s Git support: in its current state, it does not seem to be much more than a wrapper around the existing Subversion interface. It’s close to unusable in its current incarnation, but the fact that it is there at all hopefully means it will get better over time. Until that time, I recommend you use Xcode’s version editor for diffs and the command line or a third-party Git GUI app for everything else
