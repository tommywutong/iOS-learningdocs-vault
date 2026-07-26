---
title: Objective-Rust
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/08/Objective-Rust/'
original_language: en
published: 2020-08-26
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f126ff2e1823f5d0'
translated: false
---

> 原文：[Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/)

[The Swift Runtime: Heap Objects](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/) »

« [Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=objective-c)

[Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=objective-c) »

[Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=rust) »

« [Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/?tag=swift)

[The Swift Runtime: Heap Objects](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/?tag=swift) »

## [Objective-Rust](#)

This is going to be another one of those posts where I did something ridiculous and then show you how I got there, so let’s just get right to it.

```
use objc_rust::*;
use std::ffi::CStr;

pub fn main() {
    #[link(name = "Foundation", kind = "framework")]
    extern {}
    
    objc! {
        let cls = ObjCClass::lookup("NSNumber\0").unwrap();
        let value = [[cls.into() numberWithUnsignedInt:42u32] stringValue];
        let result = unsafe { CStr::from_ptr([value UTF8String]) };
        println!("string: {}", result.to_string_lossy()); // string: 42
    }
}
```

Yep, that’s Rust code with embedded Objective-C syntax, and it works. Why would you do such a thing? Maybe you want tighter interop between the Rust and Objective-C parts of your iOS app. Maybe you want to write your iOS app _entirely_ in Rust. Or maybe you just wanted to see if it was possible after your [colleague](https://twitter.com/porglezomp)’s offhand remark.

(For me, it was the last one, absolutely.)

This post is going to walk through what it took to make this possible, so here’s a table of contents:

1. [Background on Objective-C](#background-on-objective-c)
2. [Objective-C from Rust, manually](#objective-c-from-rust-manually)
3. [Recursive Rust macros](#recursive-rust-macros)
4. [Rust macro gotchas](#rust-macro-gotchas)
5. [Related work](#related-work)
6. [Appendix: What about Swift?](#appendix-what-about-swift)

Sections 3-5 might actually be useful to other people looking to write Rust macros, so even though this project is a toy, you may still get something out of reading the post. However, if you’re looking to use Objective-C from Rust in production, you should not be using my unsafe toy here. Instead, use Steven Sheldon’s [`objc` crate](https://crates.io/crates/objc). Sheldon also has a blog post from near the start of the project that talks about [his design process beyond the bare message-send implementation](https://sasheldon.com/blog/2014/11/28/interoperating-between-objective-c-and-rust/).

That said, if you want to see the full source of my little monstrosity, you can [check out the repository](https://belkadan.com/source/rust-inline-objc/).

## Background on Objective-C

My normal audience these days is probably Swift developers, but I expect this one to make rounds with at least some Rust people as well. It’d be easy for both groups to not have much direct experience with Objective-C, the primary language used by Apple for both macOS^[1](#fn:osx) and iOS since their releases in 2001 and 2007. So, here’s the quick summary: it’s “just” C, except when you start working with “object” types. And nearly everything you do with those objects is based on a dynamic dispatch model implemented in the _runtime._ Because of the two parts of that sentence (“dynamic dispatch” and “implemented in the runtime”), people have come up with a lot of clever and powerful techniques to make programs simpler, more expressive, or more extensible, though sometimes at the cost of security, secrecy, and stability.

More relevant to us, however, is that a language whose features are (nearly) all available in a runtime library is a language that’s easy to bridge to dynamically, as long as you don’t have really tight performance constraints. So here’s the deal: nearly everything you do in Objective-C is calling methods by _sending messages,_ and the way this works is that methods are regular C functions stored in a dispatch table keyed by a uniqued string called a selector. It is likely that the most heavily-optimized piece of code in Apple’s libraries is `objc_msgSend`, which takes a receiver, a selector, and the arguments to the method, does a (cached) lookup of the selector in the receiver’s class’s dispatch table(s), and then jumps directly to the appropriate, polymorphically-selected implementation of the method.

There are more things the Objective-C runtime exposes, but messages are absolutely the most important.

…Oh, one more thing. Because Objective-C is an extension to C, it has to use syntax that doesn’t conflict with C syntax. That means keywords with `@` signs in front of them—one of the few symbols on the US keyboard that doesn’t already have a meaning in C—and a unique bracket-based “message send” syntax that takes a while to get used to:

```
// Objective-C
NSString *fileStr = [[NSString alloc] initWithData:fileContents encoding:NSUTF8StringEncoding];

// Pseudo-Swift
let fileStr: NSString = NSString.alloc().initWithData(fileContents, encoding: NSUTF8StringEncoding)

// Actual Swift
let fileStr = NSString(data: fileContents, encoding: .utf8)

// Pseudo-Rust
let fileStr: *const NSString = NSString::alloc().initWithData(fileContents, NSUTF8StringEncoding)

// Idiomatic-ish Rust
let file_str = NSString::from_data(file_contents, NSStringEncoding::UTF8)
```

People almost universally think Objective-C syntax is ugly when they first see it, almost universally find it completely normal after a few years, and largely (though _not_ almost universally) find idiomatic Swift easier to read even if they’re used to Objective-C.

## Objective-C from Rust, manually

From this point on you’ll be expected to read Rust syntax without step-by-step explanations. I’ll try to explain what’s going on for my Swift and other non-Rust readers—I myself am still a relative newcomer to Rust—but it’ll be pretty fast. This is _not_ intended to be an introduction to Rust or Rust macros!

Given that the Objective-C runtime exposes a public API, we should be able to pretty much just call that from Rust, and indeed we can:

```
use std::ffi::CStr;

#[repr(C)]
struct ObjCObject {
  isa: isize
}

#[repr(transparent)]
#[derive(Clone,Copy)]
struct Selector(*const u8);

#[link(name = "objc")]
extern "C" {
  fn sel_registerName(name: *const u8) -> Selector;
  fn objc_getClass(name: *const u8) -> Option<&'static ObjCObject>;
  fn objc_msgSend(); // see below
}

fn main() {
  #[link(name = "Foundation", kind = "framework")]
  extern {}

  // Get a function pointer for transmuting later.
  let msg_send = objc_msgSend as unsafe extern "C" fn();

  unsafe {
    let url_class = objc_getClass("NSURL\0".as_ptr()).unwrap();
    let description_sel = sel_registerName("description\0".as_ptr());
    let description_method = std::mem::transmute::<_, unsafe extern "C" fn(_, _) -> _>(msg_send);
    let description_obj: *const ObjCObject = description_method(url_class, description_sel);

    let utf8_sel = sel_registerName("UTF8String\0".as_ptr());
    let utf8_method = std::mem::transmute::<_, unsafe extern "C" fn(_, _) -> _>(msg_send);
    let utf8_ptr = utf8_method(description_obj, utf8_sel);
    println!("{}", CStr::from_ptr(utf8_ptr).to_string_lossy());
  }
}
```

Now, this code should make most Rust users pretty horrified. It starts out okay, declaring some types and then declaring the Rust versions of the C API from libobjc. Then it’s got a funny empty extern block to link the Foundation framework, but sure, that’s fine. And it’s got explicitly-null-terminated strings because that’s what C-based APIs generally use. (Rust doesn’t guarantee null termination by default, which makes slicing a Rust string easier.)

But then there’s a monstrosity of a line involving [`std::mem::transmute`](https://doc.rust-lang.org/std/mem/fn.transmute.html), Rust’s equivalent of Swift’s `unsafeBitCast(_:)` or C++’s `reinterpret_cast` (and now [`bit_cast`](https://en.cppreference.com/w/cpp/numeric/bit_cast)) or C’s…well, okay, C doesn’t have a direct equivalent, but a plain old cast when you’re talking about function pointers like this. The [docs for `transmute`](https://doc.rust-lang.org/std/mem/fn.transmute.html) even tell you to go use other things if possible.

So, what are we doing? Well, remember what I said about Objective-C and `objc_msgSend`: methods are regular C functions, and `objc_msgSend` “jumps directly to the appropriate, polymorphically-selected implementation of the method”. That means that the correct way to call `objc_msgSend` is to _pretend it has the right type for the method you’re calling._

In C (and Swift, for that matter), that conversion would require explicitly specifying the type of all arguments and return values. But Rust has really powerful type inference within a function body, and that extends to specifying only _some_ generic parameters, and leaving others out.^[2](#fn:swift-inference) In this case I need to specify that we’re casting to a C function pointer with two arguments and a non-void return, but not anything more than that. The remaining information will be filled in based on how the function pointer is used.

With that, you should understand the (cursed) code above. Go ahead. Try it on your own machine (if your machine is a Mac).

## Recursive Rust macros

Rust has a pretty robust macro system, so it wouldn’t be impossible or even too hard to make a macro for “message send”. That’s the route that the [`objc` crate](https://crates.io/crates/objc) takes:

```
let url_class = class!(NSURL);
let description_obj: *mut Object = msg_send![url_class, description];
let utf8_ptr = msg_send![description_obj, UTF8String];
println!("{}", CStr::from_ptr(utf8_ptr).to_string_lossy());
```

But while that’s clearly the right choice for serious Rust work, I wanted something more ambitious. More integrated. More…ridiculous.

> wait a minute. this is just objective-c [pic.twitter.com/dVQMYKKVTI](https://t.co/dVQMYKKVTI)
> 
> — Harlan Haskins (@harlanhaskins) [May 28, 2019](https://twitter.com/harlanhaskins/status/1133210047952015360?ref_src=twsrc%5Etfw)

What I wanted was for Objective-C’s messaging syntax, or something like it, to be valid anywhere in Rust code. It didn’t have to be exactly Objective-C, but I quickly realized the _advantage_ of Objective-C’s syntax: it’s delimited, i.e. it’s a self-contained expression that can be dropped into something larger without changing how that larger thing parses. (That’s probably why it’s bracketed in C as well.) Within the brackets, there’s basically two forms:

```
[receiver-expr no-arg-selector]
[receiver-expr selector-piece:arg-expr selector-piece:second-arg-expr...]
```

If I were _just_ matching that, I could use Rust’s original [pattern-matching macros](https://doc.rust-lang.org/book/ch19-06-macros.html#declarative-macros-with-macro_rules-for-general-metaprogramming). But to take a whole block of code, and replace everything that looks like a message lock _in_ that block…well, it might be possible with pattern-matching and quite a bit of recursion, but it’s going to be a lot easier to use _[procedural macros](https://blog.rust-lang.org/2018/12/21/Procedural-Macros-in-Rust-2018.html),_ a Rust macro interface written in Rust and used as a compiler plugin. (Swift folks, basically what [SwiftSyntax](https://github.com/apple/swift-syntax) allows you to do, but invoked on-demand during compilation.)

The procedural macro examples I’ve seen have either been slightly more elaborate versions of the pattern-matching macros, or entire embedded DSLs that barely use Rust syntax at all. But it’s absolutely possible to make a find-and-replace macro like this; it just means a bit of recursion.

```
#[proc_macro]
pub fn MY_MACRO(tokens: TokenStream) -> TokenStream {
    // First recurse...
    let new_stream = tokens.into_iter().map(|tree| {
        if let TokenTree::Group(group) = &tree {
            let new_contents = MY_MACRO(group.stream());
            let mut result_group = Group::new(group.delimiter(), new_contents);
            result_group.set_span(group.span());
            TokenTree::Group(result_group)
        } else {
            tree
        }
    });
    
    // ...and then do your actual work.
    new_stream.map(|tree| {
        // (which is probably more interesting than this)
        tree
    }).collect()
}
```

And what is that work? Well, if we’re (1) dealing with a bracketed Group that (2) matches the syntax of a message send, we should generate code that looks like the manual code from above. I did this using the [`quote` crate](https://docs.rs/quote/1.0.7/quote/index.html), which is a very clever library that turns Rust code into…Rust code. But with variable substitution.^[3](#fn:quote)

```
let msg_expr = quote! {
  let receiver = #receiver;
  let cmd = objc_rust::Selector::get(#selector);
  let imp = objc_rust::objc_msg_lookup(receiver, cmd);
  let function = unsafe {
    std::mem::transmute::<
      _,
      extern "C" fn(*const objc_rust::ObjCObject, objc_rust::Selector #(, #underscores)*) -> _
    >(imp)
  };
  function(receiver, cmd #(, #arguments)*)
};
```

This is pretty much the same thing as the manual code, but with some interesting notes:

- The `unsafe` is limited to just the call to `transmute`. That means that if you do unsafe things in computing the arguments, you’ll still have to say `unsafe` in your own code. Of course, you could easily argue that calling Objective-C at all deserves an `unsafe`, especially since **the compiler just believes the types you use**. But, this is just a toy, and this point could still be relevant to someone else.
- Unlike before, we’re using a helper function `objc_msg_lookup` rather than directly accessing `objc_msgSend`. This is because `objc_msgSend` isn’t the only message dispatch method in Objective-C; there’s also [`objc_msgSend_stret`](http://www.sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html), and two more that only show up in rare cases on certain platforms. Why? Because on some platforms, **the calling convention for a C function depends on the return type**, and `objc_msgSend` on its own doesn’t know what method we’re calling until it does its lookup. Rather than deal with this, I sidestepped the issue by doing the lookup separately from the function call. This is going to be a little slower, but again, toy.^[4](#fn:objc_msg_lookup)
- Doing the function call means passing an unknown number of arguments, which `quote!` handles easily. But `transmute` _also_ needs to know the number of arguments, which is a bit more of a challenge. So `underscores` is just an iterator of N fake underscore tokens, which fill in after the receiver and selector types. I feel rather clever about that. :-)

That’s all the code I’m going to show here. [You can check out the full proc_macro implementation if you want.](https://belkadan.com/source/rust-inline-objc/blob/refs/heads/main:/macros/src/lib.rs)

## Rust macro gotchas

> [`syn`](https://crates.io/crates/syn), [`quote`](https://docs.rs/quote/1.0.7/quote/index.html), and [`proc-macro2`](https://docs.rs/proc-macro2/1.0.19/proc_macro2/) are your go-to libraries for writing procedural macros. They make it easy to define custom parsers, parse existing syntax, create new syntax, work with older versions of Rust, and much more!
> 
> “[Procedural Macros in Rust 2018](https://blog.rust-lang.org/2018/12/21/Procedural-Macros-in-Rust-2018.html)”

The built-in `proc_macro` and the `proc-macro2` crate handle basic “lexing”, including matching parentheses, braces, and square brackets but not much else. `syn` can take the TokenStreams that come from `proc_macro` and parse actual Rust syntax trees out of them; `quote` takes both tokens and syntax trees and puts them back into TokenStream form. However, there were a few things that tripped me up in trying to use these tools:

- **Attribute-style macros have to start with valid Rust syntax.** Rust allows macros in the form of attributes as well as explicit macro invocations, which would have allowed me to write

  ```
  #[objc]
  fn main() {
      // …
  }
  ```

  and transform all code inside the function without a second level of nesting. But alas, the whole point was that Objective-C message syntax isn’t existing Rust syntax, and so only the normal `proc_macro` form works. My colleague (Cassie again) pointed out that this allows various tools built on Rust syntax to assume that anything _outside_ a normal macro actually has valid syntax; only within a macro can Weird Stuff arise.

  There is not an explicit error message for this; you just get an error that the syntax is invalid. This is presumably because the compiler doesn’t even get to the point of invoking your macro before parsing the normal code.
- **If you want to debug a procedural macro, use `eprintln!`** and the output will be included in the compiler’s stderr. This wasn’t exactly a “gotcha” for me because I happened to spot it in David Tolnay’s “[Procedural Macros Workshop](https://github.com/dtolnay/proc-macro-workshop#debugging-tips)” repo readme, even though I didn’t actually go through the exercises in that workshop. Another important tip here is to **enable the `"extra-traits"` feature for `syn`** if you want to dump parsed syntax trees.
- **To parse custom syntax with `syn`, you have to make a new type that implements the [`Parse`](https://docs.rs/syn/1.0.39/syn/parse/trait.Parse.html) trait.** This is the only way to have `syn` give you a ParseStream, which has all the useful methods for parsing Rust syntax. Moreover, as far as I can tell you have to parse the _entire_ token stream when you do this; if you want to take some tokens in the middle of the stream, you’ll have to save the ones at the beginning and end to be dumped back out later. (I sidestepped this constraint by parsing an entire bracketed group at once.)
- **Parsing expressions with `syn` requires the `"full"` feature.** I’m glad I remembered feature flags exist, since they don’t in the Swift ecosystem for dependencies, but before I added this to my Cargo.toml config file expressions just immediately failed to parse.
- **If your macro introduces more dependencies, those dependencies have to be in a separate module. That should be your main vended library.** Unlike Swift packages, Rust crates can only have one library per crate, and procedural macros are already going to be different from normal libraries because they are built to run as part of compilation. So the simplest thing to do is put the macros in a second crate nested in the main one:^[5](#fn:tre)

  ```
  inline-objc
  ├── Cargo.toml
  ├── src
  │   ├── lib.rs
  │   └── main.rs
  ├── tests
  └── macros
      ├── Cargo.toml
      └── src
          └── lib.rs
  ```

  The top-level crate `inline-objc` depends on `macros` by relative path:^[6](#fn:relative)

  ```
  inline-objc-macros = { path = "./macros" }
  ```

  And `inline_objc` should re-export the macros so that clients don’t even need to think about all of this:

  ```
  pub use inline_objc_macros::*;
  ```

  (And the main.rs file isn’t necessary; it’s just for quick testing.)

That’s all I have for now, though I’m still relatively new to Rust and so I stumbled over a few things that a more experienced Rust programmer / Cargo user would already know.

- The Rust blog has that high-level summary, “[Procedural Macros in Rust 2018](https://blog.rust-lang.org/2018/12/21/Procedural-Macros-in-Rust-2018.html)”.
- As mentioned, David Tolnay made a [workshop repo](https://github.com/dtolnay/proc-macro-workshop#debugging-tips) for learning about procedural macros. I didn’t go through it myself but if you want a proper introduction with practice projects, this is probably a good place to start.
- For more serious Rust/Objective-C interop work, there’s the real [`objc` crate](https://crates.io/crates/objc), and Sheldon’s [accompanying blog post](https://sasheldon.com/blog/2014/11/28/interoperating-between-objective-c-and-rust/), which is a lot more step-by-step than this one.
- When I tweeted about this toy project, [Ryan McGrath responded](https://twitter.com/ryanmcgrath/status/1298336493103013888) with his own fun experiment [Cacao](https://github.com/ryanmcgrath/cacao), which builds on `objc` to provide Rust wrappers around AppKit and UIKit. I didn’t know it at the time, but the [Servo](https://servo.org) project has their own project that wraps AppKit, [`core-foundation-rs`](https://github.com/servo/core-foundation-rs).
- And as a last fun note, [Mara Bos](https://twitter.com/m_ou_se) made a crate to allow inline _Python_ code within your Rust code, though it (sensibly) doesn’t mix Python and Rust syntax. [She goes into detail on the implementation of `python!` on her blog.](https://blog.m-ou.se/writing-python-inside-rust-1/)

## Appendix: What about Swift?

Above, I mentioned that Objective-C is a language “whose features are (nearly) all available in a runtime library”. Is the same true for Swift, or for that matter, Rust? What would it take to get Swift/Rust interop?

Alas, it is not. Both Swift and Rust go beyond the set of types and operations supported by C, much more than Objective-C’s little “cast `objc_msgSend` to the type of the method you’re actually calling”, and don’t (necessarily) make information about that available at runtime. There are _many_ parts to this:

- Both Swift and Rust support enum types with payloads, intelligently using properties of the types in the enum to minimize the amount of memory used by default. They do so differently, of course.
- Both Swift and Rust have function calling conventions that differ from C’s (and from each other), allowing certain kinds of calls to be more efficient than they otherwise would be.
- Both Swift and Rust have rules about what happens when you copy values around beyond just “copy the bits in the representation”. In many cases, this information is only available in the compiler.
- Neither Swift nor Rust have a general “call a function by name on this type” operation; you have to go through a protocol/trait.

But all hope’s not lost! Even if you can’t magically invoke Swift from Rust or Rust from Swift, a `bindgen`-like approach is still possible, and my colleague Nikolai Vazquez has [done some exploratory work on that](https://github.com/rustswift/swift-bindgen). Additionally, Swift _does_ keep around a fair amount of “reflection” information for types that are used in some dynamic way, and that could be used for working with at least a subset of types. (Presumably Rust has to do a similar thing for `dyn` traits.) Meanwhile, both languages support working with C interfaces, so that’ll be a bridge for some time yet.

If you’re interested in this stuff, you should also check out Aria Beingessner (Gankra)’s write-up on [Swift’s static-yet-dynamic nature from a Rust perspective](https://gankra.github.io/blah/swift-abi/).

1. Formerly “OS X”, formerly _“Mac_ OS X”. And that’s pronounced “ten”, not “ex”! [↩︎](#fnref:osx)
2. Why doesn’t Swift have whole-function type inference? There are a lot of factors that go into it but by far the main difference between Swift and Rust is overloading. Rust only allows overloading through multiply-implemented generic traits, and it’ll give up on inferring types if the choice is ever ambiguous. Swift allows overloading functions and methods by type, which means the compiler has to do more work but also allows for _more_ type inference _within_ an expression. I’d like to talk about this more in a future blog post, but no promises. [↩︎](#fnref:swift-inference)
3. [The `quote!` macro is moving into the standard `proc_macro` module too](https://doc.rust-lang.org/proc_macro/macro.quote.html); it’s just not stable yet. [↩︎](#fnref:quote)
4. It might actually _not_ be slower, because processors try to predict the result of an indirect function call based on its address, and with `objc_msgSend` they _also_ have to look at the return address to make a good prediction. But doing separate lookup-and-then-send is also a code size increase, and that can both affect performance itself and be an issue all on its own, so Apple hasn’t done anything like that. [↩︎](#fnref:objc_msg_lookup)
5. Diagram generated by [`tre`](https://github.com/dduan/tre). [↩︎](#fnref:tre)
6. If you want to publish your crate, you’ll need to publish the helper macros crate as well, and reference it via version as well as path. Read more about this in the “[Multiple Locations](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html#multiple-locations)” section of the Cargo Reference. [↩︎](#fnref:relative)

This entry was posted on [August](https://belkadan.com/blog/2020/08) 26, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Objective-C](https://belkadan.com/blog/tags/objective-c), [Rust](https://belkadan.com/blog/tags/rust), [Swift](https://belkadan.com/blog/tags/swift)
