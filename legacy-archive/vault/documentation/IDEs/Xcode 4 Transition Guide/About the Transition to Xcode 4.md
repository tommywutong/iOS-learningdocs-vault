---
title: Xcode 4 Transition Guide
apple_id: TP40009984
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-08-10'
source_url: https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/Xcode4TransitionGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:41:49.304229Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Using%20an%20Existing%20Xcode%203%20Project.md)

# About the Transition to Xcode 4

Xcode 4 is the latest iteration of Apple’s integrated development environment (IDE). This document is intended for developers who are familiar with Xcode 3 and want to get started quickly using Xcode 4. If you want a short tutorial that introduces you to the major features of Xcode 4, see _Xcode Quick Start Guide_. If you want a more complete introduction to the features and workflows of Xcode 4, see _[Xcode Overview](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/index.html#//apple_ref/doc/uid/TP40010215)_.

Figure I-1 shows the main user interface elements described in this document.

__Figure I-1__  The Xcode 4 workspace window

!

Xcode 4 uses one type of main window, called the _workspace window_, to hold most of the data you need. You can have as many workspace windows open as you need. A second window, called the Organizer window, is used for organizing your projects and reading documentation. For iOS projects, the Organizer window is also used for managing devices.

There are many improvements and new features in Xcode 4. A very partial list includes:

- Xcode 4 has a new, single-window interface for all major workflows (you can have multiple workspace windows and multiple tabs per window).
- Interface Builder is fully integrated with the main Xcode application.
- Assistant provides a second editor pane that complements the file you’re working on—for example, if you’re working on an implementation file, it can automatically find and open the corresponding header file.
- Fix-it checks your symbol names and code syntax as you type, highlights any errors it detects, and in some cases can even fix them for you.
- The version editor works with Git or Subversion to show a file’s entire SCM history and compare any two versions of a file.
- The LLVM 2.0 compiler includes full support for C, Objective-C, and C++.
- The LLDB debugger is faster and uses less memory than the GDB debugging engine.
- Xcode 4 lets you work on several interdependent projects in the same window, automatically determining dependencies so that it builds the projects in the right order.

### Use Xcode 4 for Development on Recent OS Versions

Xcode 4 runs on the current release of OS X and comes with current releases of OS X and iOS software development kits (SDKs).

### Open Your Project in Xcode 4

You can start a new project or open your Xcode 3 project in Xcode 4. Following this introduction, the first couple of chapters help you get started.

Relevant Chapters: [Using an Existing Xcode 3 Project](Using%20an%20Existing%20Xcode%203%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqmrnknltemi), [Creating a New Xcode 4 Project](Creating%20a%20New%20Xcode%204%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqnbnknltc).

### Get Oriented to Xcode’s Organization and Features

Xcode 4 is fundamentally different than Xcode 3, so whether you’re new to Apple platforms or an experienced Apple developer, you should read the next chapter to learn about Xcode 4.

Relevant Chapter: [Orientation to Xcode 4](Orientation%20to%20Xcode%204.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqnjnknltc).

### Learn How to Use Xcode 4 to Design a User Interface

One of the most obvious differences between Xcode 3 and Xcode 4 is that Interface Builder is now fully integrated into the Xcode application. The chapter on the Interface Builder highlights the advantages that ensue from this change.

Relevant Chapter: [Designing User Interfaces in Xcode 4](Designing%20User%20Interfaces%20in%20Xcode%204.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqnrnknltc).

### Debug and Refine Your Code In Xcode 4

Xcode 4 provides a consistent interface for debugging regardless of which supported debugger you use.

Relevant Chapters: [Orientation to Xcode 4](Orientation%20to%20Xcode%204.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqnjnknltc), [Debugging and Analyzing Your Code](Debugging%20and%20Analyzing%20Your%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqmznknltc), [Replacing Text and Refactoring](Replacing%20Text%20and%20Refactoring.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqobnknltk).

### Back Up Your Code and Use Source Control

Xcode provides easy backups with snapshots and provides access to the most commonly used features of source control repositories.

Relevant Chapter: [Repositories, Snapshots, and Archives](Repositories%2C%20Snapshots%2C%20and%20Archives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqnznknltcma).

### Use Archives to Distribute Your Program

When you’re ready to share your program with others, create an archive to distribute or to submit to iTunes Connect.

Relevant Chapter: [Repositories, Snapshots, and Archives](Repositories%2C%20Snapshots%2C%20and%20Archives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqnznknltcma).

[Next](Using%20an%20Existing%20Xcode%203%20Project.md)

