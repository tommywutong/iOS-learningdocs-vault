---
title: Swift Development with Visual Studio Code
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/vscode/'
original_language: en
published: 2018-11-19
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:a53ec7ffcc1980d3'
translated: false
---

> 原文：[Swift Development with Visual Studio Code](https://nshipster.com/vscode/)　·　NSHipster (Mattt)

# [Swift Development with Visual Studio Code](https://nshipster.com/vscode/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  May 6^th, 2020 ([revised](https://github.com/nshipster/articles/commits/master/2018-11-19-vscode.md))

[Visual Studio Code (VSCode)](https://code.visualstudio.com) is a cross-platform text and source code editor from Microsoft. It’s one of the most exciting open source projects today, with regular updates from hundreds of contributors. VSCode was among the first tools to support [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/), which has played a large part in providing a great developer experience, in a variety of languages and technologies.

With the [previously announced](https://nshipster.com/language-server-protocol/) [now shipping in Xcode](https://developer.apple.com/documentation/xcode_release_notes/xcode_11_4_beta_release_notes), it’s a great time to see how this integration works for yourself.

This week, we’ll walk through the process of how to get started with Swift’s new Language Server Protocol support in Visual Studio Code on macOS. If you haven’t tried writing Swift outside Xcode, or are already a VSCode user and new to the language entirely, this article will tell you everything you need to know.

---

![](https://nshipster.com/assets/vscode-banner-2f6618b018729b639085bf3144354c51423c30a30f9b4b3c6806a95ae2e9c8ce3e5f1b9ac05a40071846112b0757e20f67ccd946bd874e9b6dba7ba8bb9a547b.png)

## Step 0: Install Xcode

If you don’t already have Xcode installed on your machine, open the Terminal app and run the following command:

```
$ xcode-select --install
```

Running this command presents a system prompt.

![](https://nshipster.com/assets/xcode-select-window-4009aaac50fc3fe10ad7811886fab013771b6ca9f62c33c3afaf95c7cc62e4e4cecf90a1702bee0d4763dc5c768950e90ae0b96bb731b57ce83e3d584121c57a.png)

Click the “Get Xcode” button and continue installation on the App Store.

You can verify that everything is working as expected by running the `sourcekit-lsp` command:

```
$ xcrun sourcekit-lsp
```

This command launches a new language server process, but don’t worry if it doesn’t provide any feedback to `STDOUT` — that means it’s working as intended. Exit the process with an ETX signal (^C).

## Step 1: Install Visual Studio Code

[Download Visual Studio Code](https://code.visualstudio.com) and install it to your system Applications folder. Open the app and [follow the instructions for launching from the command line](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line). You’ll need to have the `code` command accessible from `$PATH` in order to install the SourceKit-LSP extension later on.

## Step 2: Install Node and NPM

VSCode extensions are written in JavaScript / TypeScript. If you’re not already set up for JS development, you can download Node (a JavaScript run-time for outside the browser)  
 and npm (a package manager for Node) with [Homebrew](https://brew.sh) using the following commands or manually by [following these instructions](https://www.npmjs.com/get-npm):

```
$ brew install node
```

To verify that you have a working installation, run the following command:

```
$ npm --version
6.13.4
```

## Step 3: Build and Install SourceKit-LSP Extension for Visual Studio Code

From the command line, clone the [sourcekit-lsp repository](https://github.com/apple/sourcekit-lsp) and navigate to `Editors/vscode` in the resulting directory. Use `npm` to build the extension and then use the `code` command to install it:

```
$ git clone https://github.com/apple/sourcekit-lsp.git
$ cd sourcekit-lsp/Editors/vscode/
$ npm run createDevPackage
$ code --install-extension out/sourcekit-lsp-vscode-dev.vsix
```

Now launch (or relaunch) VSCode and open a Swift project, such as [this one](https://github.com/flight-school/money), and test out Language Server Protocol support for Swift.

![](https://nshipster.com/assets/vscode-swift-lsp-screenshot-6852df25f683c5f0c7f751aaf31b8cb32db1fe16b85d44540dec7a63dfd21fea5c1dded771e0a9bc21b110e66d31c5d45f03dc8c2ea209798be83eb730e0b7fb.png)

---

So there you have it — the makings of a first-class Swift development experience outside of Xcode.

And with GitHub’s recent announcement of [Codespaces](https://github.com/features/codespaces/), that future may be coming sooner than we once thought. Thanks to Swift’s support for [Language Server Protocol](https://nshipster.com/language-server-protocol/), we’ll soon be able to edit Swift code — syntax highlighting, autocompletion, and all — directly from the browser.
