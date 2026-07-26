---
title: Hacking C++ From C
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/hacking-c-from-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:262cdc0b782eae50'
translated: false
---

> 原文：[Hacking C++ From C](https://www.mikeash.com/pyblog/hacking-c-from-c.html)　·　mikeash.com Friday Q&A

Posted at 2006-08-03 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Why CoreAudio is Hard](https://www.mikeash.com/pyblog/why-coreaudio-is-hard.html)  
Previous article: [Lesson of the Day](https://www.mikeash.com/pyblog/lesson-of-the-day.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [c++](https://www.mikeash.com/pyblog/?tag=c%2B%2B) [hack](https://www.mikeash.com/pyblog/?tag=hack) [magic](https://www.mikeash.com/pyblog/?tag=magic)

Hacking C++ From C

by [Mike Ash](https://www.mikeash.com/)

**Motivation**   
This code was initially developed over the course of about one week, and then took approximately two months of debugging before it became stable. Since then Apple has broken it several times with Safari updates, with the changes required being anything from a simple change of offsets to a large re-engineering of the function.

The prototype of the function is thus:

```
    void LiveDict_1_3_WebViewGetTextAtPoint(id webHTMLView, NSPoint point, NSString **text, int *offset)
```

Given an instance of a WebHTMLView (the thing inside a WebView that does all the work) and a point, the function is to return the text at that point, and the offset into that text which represents where that point is located inside it. This is then used to look up the appropriate word in LiveDictionary. (The 1_3 thing is a version numbering scheme so it doesn't conflict with nearly identical functions made for other versions of Safari.)

You would think that this would be easy, but at the time I originally wrote this function, there was no public way to obtain this information. Obviously there is _some_ way to do it, since WebKit itself does it, for example when you drag to select some text. So I dove into WebCore to see how it was done.

After much digging, I found the KHTMLPart class which has a method called isPointInsideSelection that does basically the same thing. I ripped out the bits I didn't need and came up with the following C++ code:

```
    id bridge = [webHTMLView _bridge];
    KWQKHTMLPart *part = [bridge part];
    DocumentImpl *impl = part->xmlDocImpl();
    khtml::RenderObject *r = impl->renderer();
    khtml::RenderObject::NodeInfo nodeInfo(true, true);
    r->layer()->hitTest(nodeInfo, (int)location.x, (int)location.y);
    NodeImpl *nodeImpl = nodeInfo.innerNonSharedNode();
    if(!nodeImpl || !nodeImpl->renderer() || !nodeImpl->renderer()->isText())
        return;
    Position position = innerNode->positionForCoordinates(absXPos - renderXPos, absYPos - renderYPos);
```

Not too bad, right? Most of the code is just drilling down to the object I need to interrogate, and then asking it. (There's a little bit at the end to get the actual text of the node that I left off.)

But... I can't just write that code. All of these classes are private and buried in WebCore so I can't link against them. I can't just copy the headers because that still requires linking against them. So I decided to replicate the entire thing in C.

The only thing is, it's a bit complicated to do from C. The entire file, which contains nothing but the above function, its support functions, and comments, is 340 lines long. Over 10kB of source code just to replicate that straightforward C++. I'm going to show you exactly how it's done.

**Virtual Reality**   
As you probably know, C++ has two types of methods (C++-ites like to call them "member functions", but that's not the sort of foolishness you'll see me spouting), virtual methods and the regular kind. Virtual methods are like the methods in other OO languages, in that the implementation is looked up at runtime. The regular kind is this weird abomination where the implementation is looked up entirely at compile time based on the declared type of the object. Since these two types of methods act so differently, we have to invoke them differently when we're hacking from C.

**Static Hiss**   
Regular C++ methods are pretty easy to call from C, as long as you can get a pointer to them. They're actually just regular C functions with funny names and a single implicit parameter (this). So, for example, the xmlDocImpl method is non-virtual. Declared as a function pointer, it looks like:

```
    void *	(*KHTMLPart_xmlDocImplP)(void *);
```

You'll see a lot of void * in this article. This is because I completely don't care about types; if I'm slinging pointers around, I'll just use void * for convenience. So here we see that it returns a pointer, and takes a single parameter, the implicit this pointer. If I've assigned the function pointer to the right value, then I can perform the equivalent call from C as:

```
    void *xmlDocImpl = KHTMLPart_xmlDocImplP(part);
```

The only remaining piece is to get the right pointer. Here, I use the APEFindSymbol function from Unsanity's APELite. (Note that this function requires having the mach_header of WebCore; getting this is left as an exercise for the reader.) All you have to know is the symbol name, which is easy to find by just dumping the symbols in WebCore using nm and looking for one that seems to fit. The code is:

```
    KHTMLPart_xmlDocImplP = APEFindSymbol(header, "__ZNK9KHTMLPart10xmlDocImplEv");
```

And that's all there is to it. The C++ code contains two other references to non-virtual methods, the renderer method, and the hitTest method. They are used similarly.

**Static Interference**   
Unlike certain other dynamic languages, C++ allows for stack-allocated objects. The NodeInfo instance is an example of this. Creating a stack object translates to C fairly directly. First you need to allocate space, which is done by creating a struct with the right memory layout. Then you need to construct the object by calling its constructor. However, in this case, I noticed that the constructor does nothing but set everything to zero. I don't know exactly what is in a NodeInfo but I know that it's five pointers. So my NodeInfo declaration in C looks like this:

```
    struct NodeInfoStruct {
        void *dummy1, *dummy2, *dummy3, *dummy4, *dummy5;
    } nodeInfo = {0};
```

Of course if WebCore's NodeInfo definition ever changes significantly I'll be in a world of hurt. Oddly enough this never happened, though....

**Inline Fun**   
C++ also likes inline methods that are declared in the header. I, however, hate them because they don't actually get a symbol in the built library. This means that their implementation is something I can't invoke. However, I can see what they do and copy them. The renderer method is one of these. All it does is return an instance variable of the object. So I just figured out the offset of that instance variable and ripped it out. It turns out that it's 22 pointer-sizes into the object, so my replacement function is just:

```
    static void *Function_DocumentImpl_renderer(void *obj)
    {
        void **objLayoutPtr = obj;
        return objLayoutPtr[22];
    }
```

Ugly but effective. Again, if the internal layout of the object ever changes then I'm screwed, but this never happened.

**Virtually Impossible**   
Unfortunately calling virtual methods is ever so slightly harder. I'll cover the theory first, then get into how to call them.

A C++ object that contains virtual methods has as its first four bytes a pointer to its class's vtable. A vtable is a big array of function pointers which exists on a per-class basis. Each virtual method is assigned an index in this table. A virtual method is invoked by indexing into the vtable, getting the function pointer, and then calling it.

Once you have a pointer to it, a virtual method works just like a non-virtual method, in that it looks like a C function with an extra parameter stuck on the front. So a function that does all this work to invoke the correct implementation looks like this:

```
    static void *RenderObject_layer(void *obj)
    {
        const int layerVtableOffset = 7;
        typedef void *(*LayerFptr)(void *);
        LayerFptr **fakeObj = obj;
        LayerFptr fptr = fakeObj[0][layerVtableOffset];
        return fptr(obj);
    }
```

There is a constant for the vtable offset, and a typedef for the function pointer that will be invoked. Next I treat the object as if it were just a vtable, since I don't care about the other parts of it. Then I just index into the object to get the vtable, index into the vtable to get the function pointer, and finally invoke it.

**Debugger? What's That?**   
Now if you've been paying close attention, right about now you're thinking, "Where did he get that 7 from?" And a very good question that is!

The answer is basically trial and error. From looking at the headers you can count the virtual methods and make a guess, but this is unreliable. Virtual methods get laid out in the order that the compiler encounters them, so you can just count them off starting from the very first method in the highest superclass, working your way down, and find the offset.

The trouble with that approach is two-fold. First, people suck at counting, especially when you're counting stuff in mountains of evil C++. Second, if you get it wrong, you'll crash in horrible and weird ways. You'll be invoking a completely different function which probably takes completely different arguments and returns a completely different values. Debugging that error will not be fun; this is already difficult enough as it is, without adding another layer of undebuggability. So ideally we'd want to come up with a guess, and then check it. We can use our friend the debugger to tell us what the offset is.

I set a breakpoint in a location where I had a pointer to the object I wanted to investigate. In this case it's obj, which is a RenderObject (or an instance of a subclass). I'll find the offset of the layer function that I used in the previous example.

```
    (gdb) p obj
    $1 = (void *) 0x55127c0
```

Here we can see the object as a plain old void *. We'll have to do some creative casting to dig into it.

```
    (gdb) p *(void **)obj
    $2 = (void *) 0xa5ca0e38
```

There's the vtable.

```
    (gdb) p **(void ***)obj
    $3 = (void *) 0x95e5deb0
```

And that's the first entry in the vtable. But it's just another address, not very informative.

```
    (gdb) p /a 0x95e5deb0
    $5 = 0x95e5deb0 <_ZN5khtml12RenderCanvasD1Ev>
```

Ah hah! If we tell gdb to format it as an address (the /a thing) then it looks up the symbol. And so now we know that the function at offset 0 is "_ZN5khtml12RenderCanvasD1Ev". That's probably a constructor or something of that nature.

```
    (gdb) p /a (*(void ***)obj)[0]
    $6 = 0x95e5deb0 <_ZN5khtml12RenderCanvasD1Ev>
```

Here's a nicer way to look into the vtable. Instead of chasing pointers and manually printing addresses, I'll grab the vtable and then treat it like an array. I don't want to manually print off vtable entries until I find the right one, so I'm going to see if I can get gdb to print a bunch of them for me.

```
    (gdb) set $i = 0
    (gdb) p /a (*(void ***)obj)[$i]
    $7 = 0x95e5deb0 <_ZN5khtml12RenderCanvasD1Ev>
```

Better, it will print the entry at the index in $i. Now I just need a loop.

```
    (gdb) while $i < 10
     >print $i
     >p /a (*(void ***)obj)[$i]
     >set $i = $i + 1
     >end
    $29 = 0
    $30 = 0x95e5deb0 <_ZN5khtml12RenderCanvasD1Ev>
    $31 = 1
    $32 = 0x95d5e130 <_ZN5khtml12RenderCanvasD0Ev>
    $33 = 2
    $34 = 0x95cef53c <_ZN5khtml12RenderObject9setPixmapERK7QPixmapRK5QRectPNS_11CachedImageE>
    $35 = 3
    $36 = 0x95e31ea8 <_ZN5khtml18CachedObjectClient13setStyleSheetERKN3DOM9DOMStringES4_>
    $37 = 4
    $38 = 0x95cef538 <_ZN5khtml18CachedObjectClient14notifyFinishedEPNS_12CachedObjectE>
    $39 = 5
    $40 = 0x95f1e24c <_ZNK5khtml15RenderContainer10firstChildEv>
    $41 = 6
    $42 = 0x95f1e254 <_ZNK5khtml15RenderContainer9lastChildEv>
    $43 = 7
    $44 = 0x95f1dd80 <_ZNK5khtml9RenderBox5layerEv>
    $45 = 8
    $46 = 0x95f1d7a0 <_ZN5khtml12RenderObject19positionChildLayersEv>
    $47 = 9
    $48 = 0x95c9d7b8 <_ZN5khtml12RenderObject13requiresLayerEv>
```

The number 10 was arbitrary, somewhat informed by my guessing from reading the headers. You can keep going higher if you don't find it. But in this case we hit the jackpot; we see a function called layer at offset 7. And that is the story of the 7 in the vtable example above.

**Insects and Other Horrors**   
This isn't exactly a technique to use, but it's a cautionary tale. One of the C++ lines reads:

```
    Position position = innerNode->positionForCoordinates(absXPos - renderXPos, absYPos - renderYPos);
```

This gets translated into C as:

```
    struct DOMPosition position = RenderObject_positionForCoordinatesP(parentRenderer, absXPos /*- renderXPos*/, absYPos /*- renderYPos*/);
```

The original definition of struct DOMPosition was:

```
    struct DOMPosition {
        void *m_node;
        long m_offset;
    };
```

This worked fine for a long time, but this past winter it came time to make a Universal binary of LiveDictionary. I groveled through the source code, checked it over with a fine-toothed comb, made sure all of my endians were swapped, and then sent off a build to somebody with an actual Intel Mac. And of course, it crashed almost instantly. And as I'm sure you've guessed, it crashed on that very line.

I spent a while not finding very much, just verifying that the PPC and Intel versions were doing the same thing. This line was suspicious because it's the only hacked C++ method that returns a struct.

On PPC, struct returns are done by using an implicit parameter and returning by reference. If you write this:

```
    struct Point p = Function(x);
```

It gets translated internally to something like this:

```
    struct Point p;
    Function(&p, x);
```

With the return being done by having Function write to the struct via this implicit first parameter.

I thought that Intel might be different, and it is just a little bit. It turns out that on Intel, this convention is only used for structs that are longer than 8 bytes. Small structs are returned just like primitives. But still, there was no difference in calling convention between C functions and C++ methods, so things should still work even if this struct was only 8 bytes.

After some more digging I discovered the problem. At some point, DOMPosition had gained a _third member_. Doh! My struct was 4 bytes too short. It had continued to work on PPC through sheer luck; either the new member wasn't used, or the four bytes following the struct on the stack were something that could be harmlessly overwritten. But on Intel, those extra 4 bytes were enough to push the function over the edge; WebCore was returning the struct using the implicit parameter, but LiveDictionary was expecting a normal return, and so wasn't passing an implicit parameter. The result was a nasty crash.

The latest definition of the struct looks like:

```
    struct DOMPosition {
        void *m_node;
        long m_offset;
        int m_affinity;
    };
```

With that fix, the Intel build worked fine.

**Conclusions**   
Hacking on private C++ classes is harrowing and dangerous but doable. With the proper care, it can form the backbone of a whole application, so long as frequent updates are part of the plan, and the application is suitably paranoid. LiveDictionary would put up a very dire warning and disable itself by default if it detected a version of Safari that was newer than what it knew about. While I recommend this as the absolute last resort, and all other avenues should be explored first, it can be done if it's necessary.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
