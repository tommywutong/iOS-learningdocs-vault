---
title: Swift Program Distribution with Homebrew
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/homebrew/'
original_language: en
published: 2018-12-03
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:c58a0a3f39230b5e'
translated: false
---

> 原文：[Swift Program Distribution with Homebrew](https://nshipster.com/homebrew/)　·　NSHipster (Mattt)

# [Swift Program Distribution with Homebrew](https://nshipster.com/homebrew/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  December 3^rd, 2018

It’s not enough to make software; you also have to make it easy to install.

Apple’s had this figured out for almost a decade. Anyone can go to the App Store and — with a single tap — start using any one of a million apps in just a few moments.

Compare that to the all-too-common scenario when you go to install any other random piece of software:

> Download this gzip’d tarball of source code — oh, and all of its dependencies, too. And make sure you have the latest version of Xcode (but if you’re running latest beta, use the development branch instead). You might hit this one bug, but don’t worry: there’s a workaround posted on StackOverflow… _wait, where are you going?_

Of course, we know there’s a better way.

For iOS and macOS frameworks, we use [Carthage](https://github.com/Carthage/Carthage) or [CocoaPods](https://github.com/CocoaPods/CocoaPods). For Swift packages, we use [Swift Package Manager](https://swift.org/package-manager/). And when it comes time to distribute a command-line tool built in Swift, we use [Homebrew](https://brew.sh/).

Not sure how? Go ahead and pour a glass of your beverage of choice and read on — you’ll learn everything you need to know before you’re due for a refill. 🍺

---

Homebrew is the _de facto_ system package manager for macOS. It’s the best way to install and manage programs that run on the command-line (and with [Homebrew Cask](https://github.com/Homebrew/homebrew-cask), it’s the best way to install apps, too).

Simply put: **If you want your software to reach the largest audience of developers on macOS, write and publish a Homebrew formula for it.**

Even if you’re a long-time user of Homebrew, you may find the prospect of contributing to it daunting. But fear not — the process is straightforward and [well-documented](https://docs.brew.sh). For relatively simple projects, newcomers can expect to have a working formula finished within an hour; projects with a complex build process or dependency graph may take a while longer, but Homebrew is flexible enough to handle anything you throw at it.

For our article about the [SwiftSyntax](https://nshipster.com/swiftsyntax/) library, we wrote a [syntax highlighter for Swift code](https://github.com/NSHipster/SwiftSyntaxHighlighter). We’ll be using that project again for this article as an example for how to write and publish a Homebrew formula. (If you’d like to follow along at home, make sure you have [Homebrew](https://brew.sh/#install) installed and can run the `brew` command from the Terminal)

## Creating a Makefile

Although we _could_ write out all of our build instructions directly to Homebrew, a better approach would be to delegate that process to proper build automation system.

There are lots of build automation tools out there — notably [Bazel](https://www.bazel.build) and [Buck](https://buckbuild.com), which have both gained traction within the iOS community recently. For this example, though, we’re going to use [Make](https://en.wikipedia.org/wiki/Make_%28software%29).

Now, we could dedicate an entire ~~article~~ book to Make. But here’s a quick intro:

Make is a declarative build automation tool, meaning that it can infer everything that needs to happen when you ask it to build something. Build instructions are declared in a file named `Makefile`, which contains one or more rules. Each rule has a target, the target’s dependencies, and the commands to run.

Here’s a [simplified](https://github.com/NSHipster/SwiftSyntaxHighlighter/blob/master/Makefile) version of the `Makefile` used to build the `swift-syntax-highlight` command-line executable:

```
prefix ?= /usr/local
bindir = $(prefix)/bin
libdir = $(prefix)/lib

build:
	swift build -c release --disable-sandbox

install: build
	install -d "$(bindir)" "$(libdir)"
	install ".build/release/swift-syntax-highlight" "$(bindir)"
	install ".build/release/libSwiftSyntax.dylib" "$(libdir)"
	install_name_tool -change \
		".build/x86_64-apple-macosx10.10/release/libSwiftSyntax.dylib" \
		"$(libdir)/libSwiftSyntax.dylib" \
		"$(bindir)/swift-syntax-highlight"

uninstall:
	rm -rf "$(bindir)/swift-syntax-highlight"
	rm -rf "$(libdir)/libSwiftSyntax.dylib"

clean:
	rm -rf .build

.PHONY: build install uninstall clean
```

This `Makefile` declares four targets: `build`, `install`, `uninstall`, and `clean`.

`build` calls `swift build` with `release` configuration and the option to disable [App Sandboxing](https://developer.apple.com/app-sandboxing/) (which otherwise causes problems when installing via Homebrew).

`install` depends on `build` — which makes sense because you can’t install something that hasn’t been built yet. The `install` command copies the executable to `/usr/local/bin`, but because `swift-syntax-highlighter` links to `libSwiftSyntax.dylib`, we need to install that to `/usr/local/lib` and use the `install_name_tool` command to modify the executable and update its path to the [dynamic library](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/UsingDynamicLibraries.html). If your project only links to system dynamic libraries (like `@rpath/libswiftCore.dylib`) then you won’t have to do any of this.

The `uninstall` and `clean` targets are the inverse to `install` and `build`, and are particularly useful when you’re writing or debugging your `Makefile`.

Before proceeding to the next step, you should be able to do the following with your `Makefile`:

- **Perform a clean install.** If you have any build failures, address those first and foremost.
- **Run the program after cleaning.** Cleaning the project after installation reveals any linker errors.
- **Uninstall successfully.** After running `make uninstall`, your executable should no longer be accessible from your `$PATH`.

## Writing a Homebrew Formula

A Homebrew formula is a Ruby file that contains instructions for installing a library or executable on your system.

Run the `brew create` subcommand to generate a formula, passing a URL to your project. Homebrew will automatically fill in a few details, including the formula name and Git repository.

```
$ brew create https://github.com/NSHipster/SwiftSyntaxHighlighter
```

After filling in the metadata fields and specifying installation and test instructions, here’s what the formula for `swift-syntax-highlight` looks like:

```
class SwiftSyntaxHighlight < Formula
  desc "Syntax highlighter for Swift code"
  homepage "https://github.com/NSHipster/SwiftSyntaxHighlighter"
  url "https://github.com/NSHipster/SwiftSyntaxHighlighter.git",
      tag: "0.1.0", revision: "6c3e2dca81965f902694cff83d361986ad86f443"
  head "https://github.com/NSHipster/SwiftSyntaxHighlighter.git"

  depends_on xcode: ["10.0", :build]

  def install
    system "make", "install", "prefix=#{prefix}"
  end

  test do
    system "#{bin}/swift-syntax-highlight" "import Foundation\n"
  end
end
```

## Testing a Homebrew Formula Locally

Once you’ve put the finishing touches on your formula, it’s a good idea to give it a quick taste test before you share it with the rest of the world.

You can do that by running `brew install` and passing the `--build-from-source` option with a path to your formula. Homebrew will run through the entire process as if it were just fetched from the internet.

```
$ brew install --build-from-source Formula/swift-syntax-highlight.rb
==> Cloning https://github.com/NSHipster/SwiftSyntaxHighlighter.git
Updating ~/Library/Caches/Homebrew/swift-syntax-highlight--git
==> Checking out tag 0.1.0
HEAD is now at 6c3e2dc
==> make install prefix=/usr/local/Cellar/swift-syntax-highlight/0.1.0
```

Assuming that works as expected, go ahead and `brew uninstall` and get ready to publish.

## Publishing a Tap

In [Homebrew parlance](https://docs.brew.sh/Formula-Cookbook#homebrew-terminology), a tap is a collection of formulae contained within a Git repository. Creating a tap is as simple as creating a directory, copying your formula from the previous step, and setting up your repo:

```
$ mkdir -p homebrew-formulae/Formula
$ cd homebrew-formulae
$ cp path/to/formula.rb Formula/
$ git init
$ git add .
$ git commit -m "Initial commit"
```

## Installing a Formula from a Tap

By convention, taps named `"homebrew-formulae"` and published on GitHub are accessible from the command line at `organization/formulae`. You can either add the tap to Homebrew’s search list or install a formula by fully-qualified name:

```
# Option 1:
$ brew tap nshipster/formulae
$ brew install swift-syntax-highlight

# Option 2:
$ brew install nshipster/formulae/swift-syntax-highlight
```

With your formula installed, you can now run any of its packaged executables from the command-line:

```
$ swift-syntax-highlight 'print("Hello, world!")'
<pre class="highlight"><code><span class="n">print</span><span class="p">(</span><span class="s2">"Hello, world!"</span><span class="p">)</span></code></pre>
```

_Neat!_

---

Now looking at all of this, you might think that this is a lot of work — and you’d be right, to some extent. It’s not nothing.

You might say,

> I’m doing this for free, and I don’t owe nothing to nobody. Read the [license](https://opensource.org/licenses/MIT): This software is provided _“as-is”_. If you don’t like that, go ahead and fork it yourself.

If you do, that’s fine. You’re completely entitled to feel this way, and we sincerely appreciate your contributions.

But please consider this: if you spend, say, an hour making it easier to install your software, that’s at least that much saved for everyone else who wants to use it. For a popular piece of software, that can literally add up to _years_ of time spent doing something more important.

You’ve already put so much effort into your work, why not share it with someone else who will appreciate it. 🍻
