---
title: 'Friday Q&A 2009-03-06: Using the Clang Static Analyzer'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-03-06-using-the-clang-static-analyzer.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8b4df72ec04a4e4c'
translated: false
---

> 原文：[Friday Q&A 2009-03-06: Using the Clang Static Analyzer](https://www.mikeash.com/pyblog/friday-qa-2009-03-06-using-the-clang-static-analyzer.html)　·　mikeash.com Friday Q&A

Posted at 2009-03-06 22:19 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-03-13: Intro to the Objective-C Runtime](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)  
Previous article: [Friday Q&A 2009-02-27: Holistic Optimization](https://www.mikeash.com/pyblog/friday-qa-2009-02-27-holistic-optimization.html)  
Tags: [clang](https://www.mikeash.com/pyblog/?tag=clang) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-03-06: Using the Clang Static Analyzer

by [Mike Ash](https://www.mikeash.com/)

**What Is It?**  
 Clang is part of the [LLVM](http://llvm.org/) project. LLVM is essentially a compiler and JIT virtual machine framework. Some of the compiler bits are currently available in Mac OS X as llvm-gcc, which fits a gcc parser/front-end to the LLVM code generator/back-end. Clang aims to essentially fill in the other half, and provide a parser/front-end as part of the LLVM project itself, which will allow a pure LLVM compiler.

What's the point of this, and why not just use gcc? It's actually pretty simple: gcc is old and crufty and slow. It has a huge amount of legacy baggage and is not very easy to work with. Clang is considerably more lightweight and its code is much more modular.

That last part is important for this, because some enterprising people have done taken Clang and implemented a static code analyzer with it. In essence, it's a compiler that, instead of translating your code to machine language, goes through and looks for mistakes.

The Clang Static Analyzer (which I will now abbreviate as CSA even though everybody calls it "clang", because Clang is actually the name for the entire front-end, not just CSA) is still early in development and very incomplete, but is still very useful even so.

**Where Is It?**  
 The main CSA web page can be found at [http://clang.llvm.org/StaticAnalysis.html](http://clang.llvm.org/StaticAnalysis.html), and it can be downloaded using the link at the bottom right. I won't link directly to the download because it's still in very active development and so the download link updates frequently.

**How To Use It**  
 Using CSA is extremely easy. It provides a `scan-build` command which you simply invoke at the command line, passing the command to build your code as the parameters. `scan-build` will do some funky business to convince `gcc` to pass control over to CSA as it builds, allowing CSA to analyze all of your code instead of actually getting it built.

Since an example is worth a thousand words:

```
    $ gcc -framework Foundation test.m
    $ scan-build gcc -framework Foundation test.m
    ANALYZE: test.m main
    test.m:5:16: warning: Value stored to 'x' is never read
        int x = 0; x = 1;
                   ^   ~
    1 diagnostic generated.
    scan-build: 1 bugs found.
    scan-build: Run 'scan-view /var/folders/YT/YTiq3QDl2RW4ME+BYnLyRU+++TM/-Tmp-/scan-build-2009-03-06-3' to examine bug reports.
    $ 
```

And there it is, found a bug. If you run the command it mentions at the end, it gives a _really_ swank HTML view.

Note that the `scan-build` command can be used not only with `gcc` but also with `xcodebuild` and even `make`. Running an analysis of your Xcode project is just a single command, usually as simple as `scan-build xcodebuild` in your project's directory.

**A Better Example**  
 Let's actually look at some code. I made the following contrived buggy code:

```
    #import <Foundation/Foundation.h>
    
    static void TestFunc(char *inkind, char *inname)
    {
        NSString *kind = [[NSString alloc] initWithUTF8String:inkind];
        NSString *name = [NSString stringWithUTF8String:inname];
        if(!name)
            return;
        
        const char *kindC = NULL;
        const char *nameC = NULL;
        if(kind)
            kindC = [kind UTF8String];
        if(name)
            nameC = [name UTF8String];
        if(!isalpha(kindC[0]))
            return;
        if(!isalpha(nameC[0]))
            return;
        
        [kind release];
        [name release];
    }
```

Obviously this code doesn't actually do anything useful, but of course it's meant only for illustration. There are several bugs in this code. Instead of trying to find them by looking, let's ask CSA:

```
    $ scan-build gcc -c test.m
    ANALYZE: test.m TestFunc
    test.m:5:23: warning: Potential leak of object allocated on line 5 and store into 'kind'
        NSString *kind = [[NSString alloc] initWithUTF8String:inkind];
                          ^
    test.m:18:17: warning: Dereference of null pointer.
        if(!isalpha(nameC[0]))
                    ^~~~~~~~
    2 diagnostics generated.
    scan-build: 2 bugs found.
    scan-build: Run 'scan-view /var/folders/YT/YTiq3QDl2RW4ME+BYnLyRU+++TM/-Tmp-/scan-build-2009-03-06-6' to examine bug reports.
```

And there we are two bugs! They're both pretty subtle too. The object that's leaked does get released at the end of the method. The problem is simply that there are some return statements in the middle that can cause that code not to be reached. CSA is clever enough to trace out those code paths and find the problem. The other bug requires a similar depth of analysis to find, as the null dereference can only happen if a previous if statement isn't followed.

You may have noticed that it missed a bug, though. This function releases `name`, which points to an object that it does not own. I'm not sure why CSA missed this, but it's important to keep in mind that it's not perfect and it won't catch everything.

CSA also sometimes sees false positives. These mostly occur when doing funky cross-method memory management tricks. For example, it's common when displaying a sheet to pass an object in to the `void *context` parameter so that the receiver of the end-sheet message can get information out of it. Proper memory management here requires retaining the `context` object when making the call, and then releasing it in the callback. Previous versions of CSA would consider the initial retain a leak, since it couldn't see that it was later balanced in another method. They appear to have fixed this particular case now, but other such cases will still be around, simply because it can't be perfect.

**Conclusion**  
 The Clang Static Analyzer, although limited, is an extremely useful tool. I guarantee that if you run it for the first time on any substantial base of Cocoa code, you will be surprised and frightened at what it finds. For tracking down leaks and many other common programming errors, it is invaluable. And it's under active development as part of a project with a great deal of support from Apple, so it will only get better.

That wraps up this week's Friday Q&A. Come back next week for another exciting installment. If you have a topic you'd like to see discussed, please write in. Friday Q&A is driven by your submissions, and the more I get, the better topics I can choose. Post your ideas below or [e-mail them](mailto:mike@mikeash.com) (and tell me if you don't want me to use your name).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
