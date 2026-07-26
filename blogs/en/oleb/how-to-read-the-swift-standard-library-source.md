---
title: How to Read the Swift Standard Library Source
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/10/swift-stdlib-source/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d3f769f2d960fbb1'
translated: false
---

> 原文：[How to Read the Swift Standard Library Source](https://oleb.net/blog/2016/10/swift-stdlib-source/)　·　Ole Begemann

# How to Read the Swift Standard Library Source

**~~The easiest~~ One way to read the source code of the Swift standard library after GYB preprocessing is to perform a full build of Swift. (Another is to write a small shell script. See the update below.)**

If you want to start exploring the Swift source code, the standard library is the obvious place to begin. The code in the standard library is immediately relevant to any Swift developer, and if you ever wonder about the behavior or performance characteristics of a particular API, checking the actual code itself can often be the quickest and most reliable way to answer your questions.

The standard library is also the most approachable part of the Swift project. For one, it’s written in Swift and not in C++. And you probably already know its public API since you use it every day. This means it’s not too hard to orient yourself in the code base and find what you’re looking for. And even if you’re not looking for anything specific, browsing the code can reveal [a nugget](https://oleb.net/blog/2016/09/playground-print-hook/) or [two](https://oleb.net/blog/2016/10/swift-array-of-c-strings/).

# Where can you find the standard library source code?

The bulk of the standard library’s code is in the [`stdlib/public/core`](https://github.com/apple/swift/tree/master/stdlib/public/core) directory in the [Swift repository](https://github.com/apple/swift) on GitHub. You’ll find the interfaces and implementations for all public types, protocols, and free functions there. You can of course just read the code directly in your browser or clone the repository and go through it on your local machine, but there’s one complication: you’ll notice that about a third of the files have the file extension `.swift.gyb`. If you open one of these files, e.g. [`FixedPoint.swift.gyb`](https://github.com/apple/swift/blob/master/stdlib/public/core/FixedPoint.swift.gyb) (this is where the integer types are defined), you’ll see a mixture of Swift and a templating language called GYB.

> gyb stands for Generate Your Boilerplate. It’s a preprocessor the Swift team wrote so that when they needed to build, say, ten nearly-identical variants of `Int`, they wouldn’t have to literally copy and paste the same code ten times. If you open one of those files, you’ll see that they’re mainly Swift code, but with some lines of code intermixed that are written in Python. The actual preprocessor itself is in the Swift source repository at [`utils/gyb`](https://github.com/apple/swift/blob/master/utils/gyb), though most of the code is in [`utils/gyb.py`](https://github.com/apple/swift/blob/master/utils/gyb.py).
> 
> — [Becca Royal-Gordon](https://forums.swift.org/t/what-are-swift-gyb-files/303/2)

We’ll likely see [less of GYB](https://twitter.com/gottesmang/status/787493623533215745) and more plain Swift sources as Swift [becomes more expressive](https://twitter.com/gottesmang/status/787493919072235520), but for the moment we’re stuck with it.

# Processing GYB

If you just want to read the source (as opposed to contributing to Swift), I find that GYB harms more than it helps. So how do you preprocess the files? You could try calling the `gyb` script directly, but it depends on a specific environment that’s created by the build script. The best way is to perform a full build of Swift. Building from source may seem like overkill if you’re only interested in reading the code, but I found it to be way easier than the alternatives.

**Update:** [Toni Suter pointed out to me](https://twitter.com/tonisuter/status/792325666591088668) that the `gyb` script only depends on a single variable that you can easily set yourself (the size of a pointer in bytes, i.e. if you want to build for 64-bit or 32-bit). So if processing GYB is all you need, [this little script](https://gist.github.com/tonisuter/e47267a25b3dcc90fe75a24d3ed2063a) is a great alternative to a full build:

```
#!/bin/bash
for f in `ls *.gyb`
do
    echo "Processing $f"
    name=${f%.gyb}
    ../../../utils/gyb -D CMAKE_SIZEOF_VOID_P=8 -o $name $f --line-directive ""
done
```

This will process all `.gyb` files in the current directory and save them to the same directory without the `.gyb` extension. Remove the `--line-directive ""` parameter to add source location comments to the processed files (like the Swift build process does).

# Building Swift from source

To set up the build environment, follow the instructions [in the readme](https://github.com/apple/swift/blob/master/README.md) in the Swift repository. On a Mac, you’d currently do something like this (using Homebrew to install the required build tools), but make sure to double-check if these steps are still correct:

```
# Install build tools
brew install cmake ninja
# Create base directory
mkdir swift-source
cd swift-source
# Clone Swift
git clone https://github.com/apple/swift.git
# Clone dependencies (LLVM, Clang, etc.)
./swift/utils/update-checkout --clone
```

The last command will clone the other projects that are required to build Swift: LLVM, Clang, LLDB, and other parts of the Swift distribution, like the Foundation and libdispatch modules for Linux. After this step, your `swift-source` directory will look like this:

```
du -h -d 1
250M	./clang
4,7M	./cmark
 47M	./compiler-rt
 15M	./llbuild
197M	./lldb
523M	./llvm
221M	./swift
 26M	./swift-corelibs-foundation
7,8M	./swift-corelibs-libdispatch
1,1M	./swift-corelibs-xctest
316K	./swift-integration-tests
960K	./swift-xcode-playground-support
7,0M	./swiftpm
1,3G	.
```

Now you can start the build by invoking the build script. This will first build LLVM and then Swift:

```
./swift/utils/build-script -x -R
```

The options are important:

- `-x` tells the build script to generate an Xcode project, which allows you to browse the source code in Xcode.
- `-R` specifies a release build. This is (surprisingly to me) faster than doing a debug build — it still takes about 25 minutes on a 2,6 GHz quad-core i7 from 2013, though (vs. 70 minutes for a debug build). More importantly, the build artifacts created for the release build “only” take up about 2 GB on your SSD, vs. 24 GB(!) for a debug build.

# Orienting yourself

When the build has finished, you’ll find the results in the `./build/Xcode-ReleaseAssert/swift-macosx-x86_64/` subdirectory under the `swift-source` folder. There will be an Xcode project at `Swift.xcodeproj`, and the preprocessed standard library sources are located in `./stdlib/public/core/8/`. Note that this directory only contains the files that were run through GYB; the regular `.swift` sources are still referenced from their original location.

Unfortunately, jumping to a particular API with _Open Quickly_ (⇧⌘O) in Xcode [doesn’t work](https://twitter.com/UINT_MIN/status/792101106495008768). I usually use _Find in Project_ (⇧⌘F) to navigate around. It helps if you come up with a phrase that only occurs at the definition of a type and not at its call sites. For example, to find the definition of the `print` function, search for “func print(“ and not just “print”.

You can also run the freshly built `swift` REPL or the `swiftc` compiler; both are located in `./Release/bin/`. This is useful if you want to test if some bug in a previous release has already been fixed in master.

# Updating

When you later want to update your local clone, rerun the `update-checkout` script and rebuild:

```
./swift/utils/update-checkout
./swift/utils/build-script -x -R
```

The incremental build should be much faster than the initial one.

# Checking out a specific version

If you want to verify the behavior of a particular API, you’ll probably want to read the source for the version of Swift you’re actually using in production instead of the current state in the _master_ branch. It’s not enough to simply check out the relevant tag in the Swift repository because it will probably fail to build if the versions of the dependencies don’t match.

The `update-checkout` script lets you specify a tag or branch; it will then attempt to check out this version in all depedencies. Example:

```
# Either
./swift/utils/update-checkout --tag swift-3.0-RELEASE
# or
./swift/utils/update-checkout --scheme swift-3.0-branch
```

The difference between the _swift-3.0-RELEASE_ tag and the _swift-3.0-branch_ branch is that the tag designates the specific release of Swift 3.0.0 as shipped in Xcode 8.0, whereas the branch is continuously updated with fixes as long as the 3.0.x line is in active development. So right now, one day after the official release of Xcode 8.1 with Swift 3.0.1, the _swift-3.0-branch_ branch already contains some fixes that will be part of Swift 3.0.2.

Unfortunately, I found `update-checkout --scheme` to be quite fragile (the `--tag` option worked better in my tests). The script attempts to [rebase](https://git-scm.com/docs/git-rebase) while checking out the requested branch, which often resulted in a merge conflict in one of the subprojects, although I hadn’t made any changes. I’m not really sure why the script works this way.
