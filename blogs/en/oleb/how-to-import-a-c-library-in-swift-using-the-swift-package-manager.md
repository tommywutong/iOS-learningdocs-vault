---
title: How to import a C library in Swift using the Swift Package Manager
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/12/importing-c-library-into-swift/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1abdd8922e9c0219'
translated: false
---

> 原文：[How to import a C library in Swift using the Swift Package Manager](https://oleb.net/blog/2017/12/importing-c-library-into-swift/)　·　Ole Begemann

# How to import a C library in Swift using the Swift Package Manager

_This is an excerpt from the _Interoperability_ chapter in our book [_Advanced Swift_](https://www.objc.io/books/advanced-swift/). The new edition, revised and extended for Swift 4, is out now._

---

Swift is great at interoperating with C code, but the initial step of importing a C library such that the Swift compiler can see the C declarations can be quite tricky. This is a step-by-step tutorial how to do this using the [Swift Package Manager](https://swift.org/package-manager/).

We’ll use the [cmark library](https://github.com/commonmark/cmark) as an example. cmark is a reference implementation of [CommonMark](http://commonmark.org/), a strongly defined [Markdown](https://daringfireball.net/projects/markdown/syntax) specification.

# 1. Installing cmark

The first step is to install the [cmark library](https://github.com/commonmark/cmark). We use [Homebrew](https://brew.sh) as our package manager on macOS to do this. Type this command in Terminal:

```
brew install cmark
```

At the time of writing, cmark 0.28.3 was the most recent version.

# 2. Wrapping cmark in a module

In C, you’d now `#include` one or more of the library’s header files to make their declarations visible to your own code. Swift can’t handle C header files directly; it expects dependencies to be _modules_. For a C or Objective-C library to be visible to the Swift compiler, the library must provide a _module map_ in the [Clang modules](https://clang.llvm.org/docs/Modules.html) format. Among other things, the module map lists the header files that make up the module.

Since cmark doesn’t come with a module map, your next task is to make one. You’ll create a package for the Swift Package Manager that won’t contain any code; its only purpose is to act as the module wrapper for the cmark library.

## 2a. Create a SwiftPM package

Create a directory for the package and then run `swift package init`, telling the package manager to create the scaffolding for a _system module_:

```
mkdir Ccmark
cd Ccmark
swift package init --type system-module
```

In SwiftPM lingo, _system packages_ are libraries installed by systemwide package managers, such as Homebrew, or APT on Linux. A system module is any SwiftPM package that refers to such a library. By convention, the names of pure wrapper modules such as this should be prefixed with `C`.

## 2b. Edit the package manifest

Next, edit the generated `Package.swift` file to look like this:

```
// swift-tools-version:4.0
import PackageDescription

let package = Package(
    name: "Ccmark",
    pkgConfig: "libcmark",
    providers: [
        .brew(["cmark"])
    ]
)
```

The `pkgConfig` parameter specifies the name of the [pkg-config](https://en.wikipedia.org/wiki/Pkg-config) file where SwiftPM can find the header and library search paths for the imported library. You can run the `pkg-config` tool to check what values SwiftPM will see. On my machine the output looks like this:

```
pkg-config libcmark --libs --cflags
# -I/usr/local/Cellar/cmark/0.28.3/include
# -L/usr/local/Cellar/cmark/0.28.3/lib -lcmark
```

The `providers` directive is optional. It’s an installation hint the package manager can display to the user when the target library isn’t installed.

## 2c. Create a C shim header

Before you can edit the module map, create a C header file named `shim.h`. It should contain only the following line:

```
#include <cmark.h>
```

## 2d. Write the module map

Now you can create the `module.modulemap` file in the root directory of the Ccmark package. It should look like this:

```
module Ccmark [system] {
    header "shim.h"
    link "cmark"
    export *
}
```

The shim header works around the limitation that module maps must contain absolute or local paths. Alternatively, you could’ve omitted the shim and specified the cmark header directly in the module map, as in `header "/usr/local/Cellar/cmark/0.28.3/include/cmark.h"`. But then the path of `cmark.h` would be hardcoded into the module map. With the shim, the package manager reads the correct header search path from the pkg-config file and adds it to the compiler invocation.

## 2e. Create a Git repository

The final step for the Ccmark package is to commit everything to a Git repository:

```
git init
git add .
git commit -m "Initial commit"
```

This is necessary because you’ll now create a second package which imports `Ccmark`, and the package manager requires a Git branch or tag name for each dependency.

# 3. Creating the client module

## 3a. Another SwiftPM package

Create another directory on the same level as the `Ccmark` directory and run `swift package init` once more, this time for an executable:

```
cd ..
mkdir CommonMarkExample
cd CommonMarkExample
swift package init --type executable
```

You’ll need to add the `Ccmark` dependency to the package manifest. Edit `Package.swift` to look like this:

```
// swift-tools-version:4.0
import PackageDescription

let package = Package(
    name: "CommonMarkExample",
    dependencies: [
        .package(url: "../Ccmark", .branch("master")),
    ],
    targets: [
        .target(
            name: "CommonMarkExample",
            dependencies: []),
    ]
)
```

Notice that we’re using a relative file system path to refer to `Ccmark`. If you want to make this accessible to other team members, push the `Ccmark` repository to a server and replace its URL here.

## 3b. Test if it works

Now you should be able to `import Ccmark` and call any cmark API. Add the following snippet to `main.swift` for a quick test to see if everything works:

```
import Ccmark

let markdown = "*Hello World*"
let cString = cmark_markdown_to_html(markdown, markdown.utf8.count, 0)!
defer {
    free(cString)
}
let html = String(cString: cString)
print(html)
```

The [`cmark_markdown_to_html`](https://github.com/commonmark/cmark/blob/5c2f3341e3c129aeb27f70fe6ca9ed0fea8f2383/src/cmark.h#L22-L28) function takes a Markdown string and converts it to HTML.

Back in Terminal, run the program:

```
swift run
# <p><em>Hello World</em></p>
```

If you see HTML as the output, you just successfully called a C function from Swift!

---

_If you liked this excerpt, consider [purchasing the full book](https://www.objc.io/books/advanced-swift/). Thanks!_

_In the book, we show how you can write a Swift wrapper for the cmark library that allows you to use the library’s features from Swift without ever having to deal with unsafe and/or inconvenient C constructs like pointers. The public API feels like 100% idiomatic Swift, without having to reimplement the CommonMark spec from scratch. You can check out [the code for the wrapper library on GitHub](https://github.com/objcio/commonmark-swift)._
