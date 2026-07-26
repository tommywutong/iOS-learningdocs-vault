---
title: Using Clang from SVN in Xcode
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/07/Using-Clang-from-SVN-in-Xcode/'
original_language: en
published: 2011-07-25
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d1021cdd3ec0b634'
translated: false
---

> 原文：[Using Clang from SVN in Xcode](https://belkadan.com/blog/2011/07/Using-Clang-from-SVN-in-Xcode/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/)

[Weak Linking](https://belkadan.com/blog/2011/07/Weak-Linking/) »

« [Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=llvm)

[Big News](https://belkadan.com/blog/2012/05/Big-News/?tag=llvm) »

« [Short Xcode Tip: Plugins](https://belkadan.com/blog/2007/09/Short-Xcode-Tip-on-Plugins/?tag=xcode)

## [Using Clang from SVN in Xcode](#)

In my free time, I work on the [Clang](http://clang.llvm.org/) open source project, mostly on the [static analyzer](http://clang-analyzer.llvm.org/). This is the backend behind Xcode’s wonderful “Analyze” tool, which catches path-sensitive problems like memory leaks and then _shows you the path_ where the leak happens.

Using custom builds of the analyzer in Xcode has always been fairly easy with the [`set-xcode-analyzer`](http://clang-analyzer.llvm.org/xcode.html) tool, distributed with packaged builds of the checker or hidden in the `tools/scan-build` directory in the Clang source repository. But what if you want to use a custom build as your _compiler?_…say, to play with [Automatic Reference Counting](http://clang.llvm.org/docs/AutomaticReferenceCounting.html) (which [I’ve discussed](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting)). It’s a little bit harder and requires some reverse engineering of the Xcode plug-in format.

NOTE: I was an intern on the Xcode frontend team two years ago, experimenting with the early stages of what became Xcode 4. I swear this post does not in any way take advantage of any internal knowledge of Xcode or the Apple Developer Tools in general, only my usual penchant for reverse-engineeering and the relative transparency of the `xcspec` plist format, which is shared by Xcode 3 and Xcode 4.

Now, we could hack Xcode’s own LLVM bundle to replace their version of Clang with ours. But I’d rather add my custom build of Clang as an _additional_ compiler, and still have the option to use the possibly-more-stable one that came with Xcode. That means making our own Xcode plug-in.

**Warning: the following procedure is completely unsupported by Apple and may break with future Xcode updates.** On the other hand, it is unlikely to cause any project corruption, and has almost zero chance of damaging your source files. So, full steam ahead!

Xcode looks for plug-ins in `Library/Application Support/Developer/VERSION/Xcode/Plug-ins`, where `VERSION` is the version of Xcode you’re running. Or, you can put `Shared` to have the plug-ins loaded by any version of Xcode…which is handy if you have Xcode 3.2 alongside Xcode 4.1.

The template you want is `Clang 1.0 LLVM.xcplugin`, which lives at one of the two following paths, depending on whether you have Xcode 3 or Xcode 4 installed. Use “Go to Location” in the Finder to get there quickly. (We’re going to be deleting most of it, so if you have both you can use either.)

```
Xcode 3:
/Developer/Library/Xcode/Plug-ins/

Xcode 4:
/Developer/Library/Xcode/PrivatePlugIns/Xcode3Core.ideplugin/Contents/SharedSupport/Developer/Library/Xcode/Plug-ins/
```

**Step 1: Copy `Clang LLVM 1.0.xcplugin` to your own Xcode plug-ins folder and rename it `Clang LLVM Trunk.xcplugin`.** You’ll probably have to create the plug-in folder inside your Library folder, using the expected location above.

It turns out Xcode plug-ins are just bundles. Let’s strip out all the unnecessary information and focus on what’s necessary.

**Step 2: Delete everything inside `Clang LLVM Trunk.xcplugin` except `Info.plist` and the `.xcspec` file in the Resources folder.**

It’s probably not a good idea for two plug-ins to conflict in registration information.

**Step 3: Edit the `Info.plist` file. At the very least, change the bundle identifier.**

**Step 4: Rename `Clang LLVM 1.0.xcspec` to `Clang LLVM Trunk.xcspec`.** I’m not sure if this is necessary, but it seems like a good idea anyway.

Finally, we have to actually register our new compiler. Here I’ll just give you the file:

**Step 5: Replace the contents of `Clang LLVM Trunk.xcspec` with the ASCII plist below.** Make sure to put in your own path where it says `/PATH/TO/llvm`!

```
(
	{
		Identifier = "com.apple.compilers.llvm.clang.trunk";
		Type = Compiler;
		BasedOn = "com.apple.compilers.llvm.clang.1_0";
		Class = "XCCompilerSpecificationClang";
		Name = "LLVM-Clang from SVN";
		Description = "LLVM/Clang from SVN";
		Vendor = LLVM;
		Version = "2.9";
		ExecPath = "$(CLANG_BIN_DIR)/clang";
		Architectures = (
			i386,
			ppc,
			"x86_64",
		);
		"ExecCPlusPlusLinkerPath" = "$(CLANG_BIN_DIR)/clang++";
		Options = (
			{
				Name = LLVM_DIR;
				Type = Path;
				DefaultValue = "/PATH/TO/llvm";
				Category = Version;
			},
			{
				Name = LLVM_BUILD_TYPE;
				Type = String;
				DefaultValue = "Release+Asserts";
				Category = Version;
			},
			{
				Name = CLANG_BIN_DIR;
				Type = Path;
				DefaultValue = "$(LLVM_DIR)/$(LLVM_BUILD_TYPE)/bin";
				Category = Version;
			},
		);
	},
)
```

A note on the “Options” there: I’ve set it up so that you can customize both your build type (Release, Release+Asserts, Debug+Asserts, etc.) with `LLVM_BUILD_TYPE`, and your build path separately with `LLVM_DIR`. Or you can just override everything with `CLANG_BIN_DIR`.

That’s all that’s necessary to get it working! Now if you want to try out ARC on your own machine, just add `-fobjc-arc` to your “Other C Flags”. (Remember that since there is no runtime support, you won’t be able to use ARC’s zeroing `weak` references.)

If you’re a UI stickler like me, you might want your build settings to show up more nicely. As you might expect, this is accomplished as a localization.

**(Optional) Step 6: Create a `LLVM-Clang from SVN.strings` file in an `en.lproj` folder for pretty build settings.** Note that the name matches the `Name` we specified inside the `xcspec` file, rather than the name of the plug-in.

```
"[Version]-category" = "Version";

"[CLANG_BIN_DIR]-name" = "Clang bin Directory";
"[CLANG_BIN_DIR]-description" = "Defaults to $(LLVM_DIR)/$(LLVM_BUILD_TYPE)/bin";

"[LLVM_DIR]-name" = "LLVM Source Root";

"[LLVM_BUILD_TYPE]-name" = "LLVM Build Type";
"[LLVM_BUILD_TYPE]-description" = "Common values include \"Debug+Asserts\" and \"Release\". The default is \"Release+Asserts\".";
```

That’s it!

---

Coda: Since I was able to figure out how to add options for `LLVM_BUILD_TYPE`, etc., you might wonder why I didn’t add a boolean option for “Use Objective-C ARC”. I actually tried this and got it to work. The trouble was, the option isn’t part of the _analyzer’s_ `xcspec`, and so the analyzer ignores it even if the compiler doesn’t. And this is even if you’ve set a custom analyzer for Xcode! Moreover, you can’t swap out the analyzer like you can with a compiler, so to make this work you’d have to modify the original analyzer’s specification.

Since this guide did _not_ require modifying any of the files in the Developer folder, I decided that “Other C Flags” was the way to go for now. I’m sure Apple will release ARC-on-Mac soon enough.

This entry was posted on [July](https://belkadan.com/blog/2011/07) 25, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [LLVM](https://belkadan.com/blog/tags/llvm), [Xcode](https://belkadan.com/blog/tags/xcode)
