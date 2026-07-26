---
title: Swift Support in CodeRunner
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/06/swift-in-coderunner/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7e4de669bde21375'
translated: false
---

> 原文：[Swift Support in CodeRunner](https://oleb.net/blog/2014/06/swift-in-coderunner/)　·　Ole Begemann

# Swift Support in CodeRunner

I am [a big fan](https://oleb.net/blog/2011/10/coderunner/) of [CodeRunner](http://krillapps.com/coderunner/), Nikolai Krill’s Mac app that lets you quickly run few lines of code without the need to create a project or to even save the file first. I have used it primarily for testing Objective-C snippets until now, but naturally I would also like to use it with Swift. In this post, I want to show you how to add Swift support to CodeRunner.

# Playgrounds and the Swift REPL

Arguably, a tool like CodeRunner is not as valuable for Swift development considering that [Playgrounds](https://developer.apple.com/swift/) and Swift’s built-in [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) largely meet the same requirements. This is especially true because CodeRunner does not have support for code completion or Swift syntax highlighting at this time. Nevertheless, I have found it easier to test a small snippet in CodeRunner than to create a playground in Xcode.^[1](#fn:1)

# Set Up Swift Support in CodeRunner

## Set Active Developer Directory

You must have Xcode 6 installed for this to work. If you have more than one version of Xcode, you must also make sure that the active developer directory (the directory the `xcrun` command uses to run command-line utilities) is set to your Xcode 6 installation. To test this, run the following in Terminal:

```
> xcrun swift --version
Swift version 1.0 (swift-600.0.34.4.5)
Target: x86_64-apple-darwin13.2.0
```

If you see the version information, you’re all set. If the command fails with `xcrun: error: unable to find utility "swift", not a developer tool or in PATH`, you need to set the active developer directory:

```
> sudo xcode-select --switch /Applications/Xcode6-Beta.app/Contents/Developer
```

## Create a Swift Template in CodeRunner

In CodeRunner, open Preferences and switch to the Languages tab. Create a new entry in the list and name it “Swift”. Here is how you configure the settings for the new language:

[![Language settings for Swift in CodeRunner](https://oleb.net/media/coderunner-swift-language-settings.png)](https://oleb.net/media/coderunner-swift-language-settings.png)

- The `swift` compiler command supports an immediate mode where it directly executes the code it compiles (like a scripting language interpreter) without first creating a binary on disk. That’s why we don’t need a comilation script, so you can leave the box “Language uses compilation script” unchecked.
- In the “Run Command:” text field, enter this command:

  ```
  xcrun swift -sdk $(xcrun --show-sdk-path --sdk macosx) -i $filename
  ```

  This will compile our code against the OS X SDK and give us access to all Cocoa libraries.
- The “Code Template:” field should contain the code you want to start with when you create a blank Swift file in CodeRunner. I use this snippet to automatically import the Foundation framework:

  ```
  import Foundation

  %@
  ```
- In the “File Extension” field, enter `swift`.

That’s it. Happy coding!

[![A swift script in CodeRunner](https://oleb.net/media/coderunner-swift-script.png)](https://oleb.net/media/coderunner-swift-script.png)

<sub>A Swift script in CodeRunner. Unfortunately, syntax highlighting and code completion are not supported.</sub>

1. Playgrounds definitely have a lot of promise — in fact, it’s one of the new features I am most excited about. However, in the current beta 1 of Xcode 6, playgrounds are quite slow and crash Xcode frequently. I also don’t like the fact that I have to explicitly save every playground somewhere on the file system, even if I only want to use it for throwaway stuff. [↩︎](#fnref:1)
