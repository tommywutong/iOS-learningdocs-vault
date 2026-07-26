---
title: 'Friday Q&A 2012-01-06: The Hopper Disassembler'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-01-06-the-hopper-disassembler.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9915ca53eb887562'
translated: false
---

> 原文：[Friday Q&A 2012-01-06: The Hopper Disassembler](https://www.mikeash.com/pyblog/friday-qa-2012-01-06-the-hopper-disassembler.html)　·　mikeash.com Friday Q&A

Posted at 2012-01-06 15:48 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Buy Videos of My VTM Presentations](https://www.mikeash.com/pyblog/buy-videos-of-my-vtm-presentations.html)  
Previous article: [Avoid Apress](https://www.mikeash.com/pyblog/avoid-apress.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-01-06: The Hopper Disassembler

by [Mike Ash](https://www.mikeash.com/)

**The App**  
The Hopper web site can be found at [hopperapp.com](http://hopperapp.com/). A demo is available, and the app itself is available for only $19 on the [Mac App Store](http://itunes.apple.com/us/app/hopper/id422856039?mt=12).

**Sample App**  
We'll be using the same sample app to inspect as before. Here it is again:

```
    // clang -framework Cocoa -fobjc-arc test.m

    #import <Cocoa/Cocoa.h>

    @interface MyClass : NSObject
    {
        NSString *_name;
        int _number;
    }

    - (id)initWithName: (NSString *)name number: (int)number;

    @property (strong) NSString *name;
    @property int number;

    @end

    @implementation MyClass

    @synthesize name = _name, number = _number;

    - (id)initWithName: (NSString *)name number: (int)number
    {
        if((self = [super init]))
        {
            _name = name;
            _number = number;
        }
        return self;
    }

    @end

    NSString *MyFunction(NSString *parameter)
    {
        NSString *string2 = [@"Prefix" stringByAppendingString: parameter];
        NSLog(@"%@", string2);
        return string2;
    }

    int main(int argc, char **argv)
    {
        @autoreleasepool
        {
            MyClass *obj = [[MyClass alloc] initWithName: @"name" number: 42];
            NSString *string = MyFunction([obj name]);
            NSLog(@"%@", string);
            return 0;
        }
    }
```

**Loading The Binary**  
When you first start Hopper, you get a blank document window. Hopper has a concept of documents separate from the binaries you inspect. These documents can be saved separately, preserving any comments or annotations you've added from one session to the next.

Click _Read Executable_ in the toolbar or select it from the _File_ menu to get started. Tell Hopper to open the executable created from the above code, and it will load it and perform some preliminary analysis:

![Hopper's main window with the executable loaded](https://www.mikeash.com/pyblog/friday-qna-2012-01-06-initial-screen.png)

Hopper fundamentally treats all bytes in the executable equally. Fundamentally, some sections of the executable are code and some are data, but you can have Hopper interpret any part in any way. It makes some effort to pick out code and treat it as code, but doesn't get everything right. In particular, it doesn't identify Objective-C methods as code. Fortunately, it's really easy to tell it how to interpret something.

Let's find the `initWithName:number:` method. It's annoying to scroll around searching for it, but of course Hopper knows all about the symbols in your app. Press shift-N (no Command key here, Hopper's key commands are a bit eccentric) to get a symbol search window. Type "initWithName" to find the method. Two symbols actually appear. The one which starts with `methImpl_` is the one we want. The one that starts with `objc_sel_` is a symbol for the selector, which is less interesting.

The contents of this method start off as "unexplored", so they're displayed as raw bytes. Select either the symbol name or the first byte underneath it and mark it as a procedure by pressing the P key (again, no Command key) or clicking _Mark As Procedure_ in the toolbar. Suddenly, we have a disassembly:

![A disassembled method in Hopper](https://www.mikeash.com/pyblog/friday-qna-2012-01-06-disassembly.png)

If you scroll down a bit, you'll notice a blue arrow pointing from the `je 0x10000197A` instruction to its target. Hopper inserts arrows like these to show control flow, which makes it much easier to follow code.

If control flow is what we're interested in, we can get a really nifty graph view of the procedure. Press the space bar or click _Show CFG_ while in the procedure, and Hopper breaks it into its component pieces and shows it in a separate window:

![The control flow graph](https://www.mikeash.com/pyblog/friday-qna-2012-01-06-CFG.png)

You can scroll around, zoom in and out, and even drag the components to different places to get the best view of what's going on.

If you prefer to read C code, you can get a C-like decompilation of the procedure by pressing Option-Return, or clicking _Pseudo Code_ in the toolbar. The result looks like this:

```
    void methImpl_MyClass_initWithName_number_(void) {
            var_80 = rdi;
            var_72 = rsi;
            var_32 = rcx;
            var_24 = &var_40;
            var_16 = &var_80;
            rdi = rdx;
            rax = objc_retain(rdx, rsi, rdx, rcx, &var_40);
            var_64 = rax;
            var_60 = var_32;
            var_80 = 0x0;
            var_40 = var_80;
            var_48 = *0x100002288;
            rax = objc_msgSendSuper2(var_24, *objc_sel_init, rdx, var_32, &var_40);
            var_80 = rax;
            var_8 = rax;
            rsi = rax;
            rax = objc_storeStrong(var_16, rax, var_16, var_32, &var_40);
            if (var_8 == 0x0) {
                    rax = objc_retain(var_80);
                    ...
```

While not the prettiest output in the world, it can be really helpful in understanding what's going on. Note that there isn't really enough data left over for Hopper to be able to figure out how many arguments a particular function takes. Because of this, you'll often see a lot of surplus arguments stuck on the end. For example, `objc_retain` only takes one argument, yet this code shows it taking five. As long as you know how many arguments the function really takes, you can just ignore the extra ones.

When you're working to understand the disassembly, it can be helpful to mark it up with your findings as you go along. You can add a comment to a line by pressing the semicolon key or selecting _Modify_-\>_Comment_ in the menus. Type in your comment and it gets inserted into the listing before the line you have selected, like:

```
                                           ; initialize the missile control system
    000000010000193e 483D00000000                    cmp        rax, 0x0
```

Holding Shift or selecting _Inline Comment_ lets you place the comment on the same line after the instruction.

You can also add new symbol names to the disassembly. Press the N key or select _Modify_-\>_Name_ to enter a symbol name for the selected line. Not only does the symbol name get added to the disassembly, but any references to that address in other parts of the code are replaced with the newly added name. By adding names to blocks of code, you can make the whole procedure much more readable.

If you make a mistake while adding comments or symbol names, you can change what's there by simply pressing the same key again on the same line. The editor window will reappear with the previous contents. If you want to delete the comment or name altogether, just clear out the string and it will disappear from the disassembly.

Remember to save your document as you create these annotations. Then the next time around, you can re-open your document and all of your annotations will still be there so you can resume where you left off.

Hopper makes it really easy to navigate around the code by simply double-clicking on any reference. Whether it's a symbol or an address, double-clicking a reference will immediately transport you to its target. Press the delete key to get back to where you were. This makes it really fast to move around and follow chains of references.

It works with data as well. For example, you might see a symbol like, `ds:objc_sel_initWithName_number_`. It seems fairly clear that this is a symbol for the `initWithName:number:` symbol, but you can verify by just double-clicking it. This will take you to the value of that symbol, which is another pointer. Double-click _that_ pointer, and it takes you into the middle of a chunk of data. Click _Mark As ASCII_ to interpret it as a string and you'll see that it is, indeed, `initWithName:number:`. Press delete twice and you're back to where you were.

**Scripting**  
Hopper also has a scripting interface using Python. While a full discussion of how to use it is beyond the scope of this article, it's good to know that it's there. Hopper comes with a couple of sample scripts and a short discussion of the various APIs available. Select _Scripts_-\>_Open Script Editor_ to see the scripts that are available and to make new ones. Click the help button in the lower right of this window to see the scripting API reference.

**Conclusion**  
Hopper is a powerful tool for disassembling executable code and inspecting the result. The ability to annotate code and even decompile it into semi-readable C-ish code makes it much easier to understand what the disassembled code is doing. It's an excellent tool and well worth the incredibly cheap price.

That's it for today. Come back next time for more technical excitement. Friday Q&A is driven by reader suggestions, so if you have a topic that you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
