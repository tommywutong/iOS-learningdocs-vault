---
title: Default Arguments and Label-based Overloading
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/'
original_language: en
published: 2022-04-24
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9bb107afd2d9daa6'
translated: false
---

> 原文：[Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [#TalkPay](https://belkadan.com/blog/2022/03/TalkPay/)

[Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/) »

« [Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=rust)

[The Two Faces of Codable/Serde](https://belkadan.com/blog/2022/11/Codable-Serde/?tag=rust) »

« [Swift Regrets: Wrap-up](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/?tag=swift)

[Swift was always going to be part of the OS](https://belkadan.com/blog/2022/10/Swift-in-the-OS/?tag=swift) »

« [Swift Regrets: Wrap-up](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/?tag=programming-languages)

[Run-time Polymorphism in Swift](https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/?tag=programming-languages) »

## [Default Arguments and Label-based Overloading](#)

This post is in response to Aria Beingessner’s “[Defaults Affect Inference in Rust: Expressions Instead Of Types](https://gankra.github.io/blah/defaults-affect-inference/)”, which describes how adding default arguments to Rust could help with some Rust stdlib problems around generics. At the same time, the Rust internals forum has a thread on “[Named Arguments](https://internals.rust-lang.org/t/pre-rfc-named-arguments/16413)” something that’s been discussed for Rust off and on for years (at varying levels of seriousness).

Here I’m going to discuss how those two features interact, and why considering them separately is potentially a bad idea. It’s a lot more braindump-y than my usual style, so be warned. The post is written with a Rust audience in mind, but makes frequent reference to Swift, Python, and C# as examples of real-world languages that have some version of these features. It also overlaps quite a bit with Aria’s post.

Contents:

- [Terminology](#terminology)
- [Optional Argument Labels](#optional-argument-labels)
- [Required Argument Labels](#required-argument-labels)
- [Default Arguments Without Overloading](#default-arguments-without-overloading)
- [Default Arguments with Arity-Based Overloading](#default-arguments-with-arity-based-overloading)
- [Default Arguments + Optional Labels + Label-Based Overloading](#default-arguments--optional-labels--label-based-overloading)
- [Default Arguments + Required Labels + Label-Based Overloading](#default-arguments--required-labels--label-based-overloading)
- [Type Inference](#type-inference)
- [“None of this Nonsense, Please”](#none-of-this-nonsense-please)
- [Bonus Information](#bonus-information)

### Terminology

In this post I’m mostly going to use Swift terminology, which means a function like

```
func append(_ value: Int, checkForDuplicates dupCheck: Bool = false)

append(1, checkForDuplicates: true)
append(2) // dupCheck is implicitly false
```

has a _full name_ of `append(``_:checkForDuplicates:)` and a _base name_ of `append`. `checkForDuplicates` is an _argument label_ and `dupCheck` is the (name of the) _parameter,_ with `false` being a _default argument._ The underscore represents an unlabeled parameter.

For the purposes of this post, we’re going to call any feature that allows declaring multiple functions with the same _base name_ “overloading”. In most languages this includes _type-based overloading,_ where `process(i64)` and `process(f64)` can coexist. But we’re more interested today in name​-based or _label-based overloading,_ where `append(_:)` and `append(``contentsOf:)` coexist, and are selected between by the labels at the call site. This doesn’t actually require “overload resolution” as long as all argument labels are present at the call site, but depending on what other features you have in the language that might not be the case. Finally, there’s _arity-based overloading,_ where we ignore labels altogether and just count the number of arguments at the call site. I don’t know any major languages that work like this, but it’s a useful tool in examining how these features interact.

> EDIT: A few people have pointed out that both [Prolog](https://en.wikipedia.org/wiki/Prolog) and [Erlang](https://www.erlang.org) (and derivatives of each, like Elixir) use arity-based overloading. A full function name in Erlang would be `append/2`.

### Optional Argument Labels

C#, Python, and several other languages allow the caller to label arguments with the same name used in the declaration of the parameter. This is useful, but makes the parameter names part of the source compatibility contract, which not everybody thinks about! (If you’re writing docs you probably have reasonable parameter names, at least.)

I’m not actually such a fan of this one, cause it makes it less obvious that two calls that look different can end up calling the _same_ function (as opposed to the usual complaint about overload resolution, where two calls that looks similar end up calling _different_ functions). It also makes adding new overloads especially fragile (what if someone provided only some of the existing set of labels, or none?), which means a library designer can accidentally box themself in. But that only matters in a language with overloading like C#, not one where functions are resolved by basename like Python.

C# does not allow overloading _purely_ by argument labels, but nothing in [the compile-time model](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/named-and-optional-arguments#overload-resolution) would prevent that; you’d “just” provide “enough” labels to disambiguate.

In every language I know with this feature, labeled arguments can appear in any order at the call site, because once you have labels, the positions “don’t matter”.

### Required Argument Labels

Swift has required argument labels, i.e. the call site has to match the declaration site. There are a few reasons for this, but the main one is it makes label-based overloading super simple, and the reason _that’s_ important is because Swift was designed from the start to interoperate with Objective-C, which has [a completely different scheme for method names borrowed from Smalltalk](https://belkadan.com/blog/2020/08/Objective-Rust/#background-on-objective-c)…

I could talk about this for an entire post, but let’s move on. (Besides, modern Python _also_ allows you to declare parameters that must have argument labels.) The direct advantage here is that call sites always match the declaration, but this’ll be more interesting when we talk about how it interacts with other features. On the other hand, this means changing an argument label is _definitely_ a source-breaking change for all existing APIs, including the ones with no labels today.

Swift’s arguments are also _not_ reorderable even with labels. One reason is that Swift does not keep you from repeating argument labels, which is mostly because ObjC didn’t prevent it first but also a little because in this model “positional” or “unlabeled” arguments aren’t really special, and of course you can have more than one of _those._ This also means the compiler doesn’t have to worry about an ambiguity between `process(x:y:)` and `process(y:x:)`. An upshot is that unlabeled parameters can follow labeled parameters, if that’s what makes sense for your call site. (In practice this isn’t super common.) But a downside is that you can end up with arguments like `tag: tag`, and you can’t pull the Rust field trick of shortening to just `tag` (because that would be an unlabeled argument, which is valid).

Swift is the only language I know that separates the concept of “argument label” from “parameter name” (not counting ObjC and Smalltalk). This leads to some very different call sites than C# or Python, because in addition to the “nouny” ways people name parameters you also get “prepositiony” names as argument labels: `sprite.move(``to: dropLoc)`, `recipients.append(``contentsOf: discountGroup)`. I really like this style but it does take some getting used to if you’re used to nouns only. (It helps at least partly with the `tag: tag` problem, but only for arguments where a preposition reads well; otherwise you’ll reach for `with:` and at that point a nouny label is probably clearer.)

I strongly recommend checking out the [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/) to see what this looks like in practice.

### Default Arguments Without Overloading

This is a sound and easy point in the design space because there’s no ambiguity: you look up the function by base name, and either it accepts the extra arguments or it doesn’t. I can say that it’s useful, too: many methods in Apple’s Objective-C libraries just call the more general API with some sensible defaults (think `localizedSort()` vs. `localizedSort(``locale:)`), and Rust has an awful lot of `foo` / `foo_with_bar` pairs.

This feature works without argument labels, but it’s often better with argument labels. You can see the “full extent” of this in Python, where you can declare a function that takes positional arguments, then a catch-all, then named arguments, then a catch-all for _those_. I don’t think named catch-alls make as much sense in a static language like Swift or Rust (because compile-time identifiers turn into run-time strings, and because it makes spell-checking the labels impossible), but you _could_ have that.

Swift is somewhat unique in that a labeled parameter with a default argument can come _anywhere in the argument list_, not just at the end, because argument labels in Swift are mandatory if present. On the other hand, Swift doesn’t allow argument reordering, with which this is sort of a moot point. Still, the order at the declaration strongly influences the order at the call site (both for humans and for tools like code completion).

At the other end of the spectrum you can have a rule that says “you can’t omit an argument from the middle of the list, even if you wanted to use its default”. This is how things work in C++ and Java, which don’t have argument labels at all, and it stinks when it comes up.

### Default Arguments with Arity-Based Overloading

This one is an interesting thought experiment because it immediately shows the problems with combining these features.

```
fn log(message: &str, tag: &str = "main")
fn log(message: &str, file: &str = "<unknown>", line: usize = 0)

log("huh")
```

It’s common in languages with type-based overloading to prefer an overload that requires fewer default arguments, which for arity-based overloading just becomes “fewest total arguments”. Without labels, there’s no way to _use_ the defaults in `log(_:_:_:)`, because the first overload will always be preferred. I haven’t seen anyone actually try to prevent this at the definition site in the language itself (though it’s not hard to lint for), but it doesn’t happen if you don’t have overloading.

This also puts you in a world where adding a new overload to a library can change the meaning of existing code in clients of that library. You don’t have that with arity-based overloads on their own (or label-based, for that matter).

Finally, people are going to want this to work:

```
impl<T> Foo<T> {
  fn bar(&self, tag: &str = "") { … }
}

impl Foo<String> {
  fn bar(&self) { … }
}

Foo::<usize>::new().bar(); // trying to call bar(_:)
```

and you will have to explain to them that no, that’d be type-based overloading, and Rust doesn’t do that. (I think?)

You can somewhat fake default arguments with just arity-based overloads, as long as you weren’t using arity-based overloads for anything else, but then users can’t omit one of the middle arguments (same restriction as C++ or Java). Still, if Rust added arity-based overloads but not default arguments I’d expect a proc-macro to appear within the week.

### Default Arguments + Optional Labels + Label-Based Overloading

No language I know actually has this combination, but it’s very close to [C#’s model](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/named-and-optional-arguments#overload-resolution), if C#’s model didn’t bother comparing signatures at all. So you can certainly imagine this kind of thing.

Unfortunately, now we can get into a truly ambiguous case: `log(_:tag:)` and `log(_:severity:)` perhaps. Again, I haven’t seen anyone try to prevent defining such overloads; they just complain at the call site. This makes the “adding an overload can break existing clients” problem worse. (As noted above, this is not my favorite point in the design space.)

Faking default arguments by making label-based overloads is still possible, but becomes combinatoric. In practice people tend to still only provide overloads with all args defaulted, then all but one, all but two, until you’re back to the original signature, just like you would with arity-based overloads.

### Default Arguments + Required Labels + Label-Based Overloading

This is close to Swift’s model, and in practice I’ve seen very few overload sets where after disambiguating by labels there’s still disambiguation by type, with the exception of unlabeled arguments (especially the “converting initializer” idiom). So you can say this model has been demonstrated to mostly work, and adding new overloads isn’t as likely to be a problem as for the labels-optional model. The existence of default arguments means it still requires overload resolution and can still produce ambiguous results, however, and faking default arguments is no easier than with optional labels.

This post has mostly been about highlighting the _pitfalls_ and _added complexity_ of these new features, so I should probably say that in practice Swift’s world feels very nice. Default arguments are way nicer than defining overload sets, especially with SE-0347 that we’ll talk about in the next section. Swift _has_ type-based overloading, but most of the time it’s all label-based overloading in practice, which has _helped_ library evolution by not requiring successive versions of a function to be named `foo`, `foo2`, `foo_ext` like C does. The source compatibility implications could and should have been thought out better than Swift did, but I don’t think the _model_ of label-based overloading is what makes that more complex.

### Type Inference

We’ve gone through all the possible combinations of features; can we use them for Aria’s use case, inferring generic arguments (types) based on the use of default arguments (values)? Swift has long supported this through overloading:

```
extension Array {
  static func create(repeating element: Element) -> Array<Element> { … }
}

extension Array where Element == Int {
  static func create() -> Array<Int> { … }
}

let array = Array.create() // Array<Int>
```

…and, well, if you actually _believe_ that methods with different full names are different methods this isn’t surprising, but you can add more complexity to it by bringing other overload rules into play:

```
extension Array where Element == String {
  static func create(shouldLog: Bool = false) -> Array<String> { … }
}

let ints = Array.create() // Array<Int>
let strings: Array<String> = Array.create()
```

which is a lot like the two-`impl` example above, but is also pretty close to what Aria’s trying to do. [SE-0347 “Type inference from default expressions”](https://github.com/apple/swift-evolution/blob/main/proposals/0347-type-inference-from-default-exprs.md) lets you get the same effect from just one function declaration with a default argument, which is convenient especially if you have multiple defaults.

```
extension Array {
  static func create(repeating element: Element = 0) -> Array<Element> { … }
}

let ints = Array.create() // Array<Int>
let bools = Array.create(repeating: true) // Array<Bool>
// yes this is a bad example
```

Unfortunately I can’t speak intimately to what this does to Swift’s already-complicated overload resolution because I’ve been gone for years now, but my sense is it doesn’t add that much complexity simply _because_ there were alreay ways to get the same effect. How about in some of these other systems though?

- Default args with no overloading: no extra complexity that I see; either the default argument has the right type, or there are no other constraints on the type, or it has a conflict and the compiler can diagnose it.
- Default args with arity-based overloading: you now have to choose whether the type constraint on the default argument affects overload resolution or not. Maybe `foo(_:)` has a default that doesn’t match, but the separately-defined `foo(_:_:)` has defaults that do. My gut feeling says that if you say “yes” here, though, you are in practice doing type-based overload resolution, just like the two-impl example above. If you say “no”, it’s the same as if the caller explicitly provided an argument with the wrong type.
- Default args with label-based overloading: same problems as arity-based, plus you now have the question of whether these constrained defaults can “tiebreak” between the truly ambiguous cases. Again, you can say “no”, and complain that it’s ambiguous even if only one of the default arguments would actually work.

(Swift also does not allow adding generic parameters to existing declarations, because Swift generics are run-time polymorphic and the stable ABI sometimes passes the run-time representation of each parameter directly and this would break that. At least, I think it does and I think it would.)

### “None of this Nonsense, Please”

[ExpHP neatly summed up the main benefits to argument labels as follows:](https://internals.rust-lang.org/t/pre-rfc-named-arguments/16413/35)

> - Providing library authors with an easier (for the author and for the user) alternative to newtypes/builders for a function which faces the problem of, “it can be unclear what this `bool` parameter is at callsites.”
> - Letting a library author provide `::new(bar: ...)` and `::new(foo: ...)` rather than `::new_bar` and `::new_foo`

Both of these are nice, but they’re not _major_ improvements in expressiveness. But also, those two features are separable: you can ditch the second and still get the first! That’s the Python route, where argument labels exist (required or optional), but there’s no overloading. And Aria’s goals only depend on default arguments.

After writing this whole post, I think I’ve talked myself into this being the best way for Rust to get the benefits of both argument labels and default arguments, especially given the amount of existing code out there that might want to adopt these features without breaking source compatibility. As much as I like Swift’s label-based overloading model, it’d be hard to retrofit onto Rust, and that’s okay.

But if there’s one thing I’d like you to take away from this, it’s that **default arguments and label-based overloading are not independent features**; you can have one or the other without major changes to your language, but once you have both you need to worry about overload resolution. And therefore, adding either one on its own will make it harder to add the other in the future.

### Bonus Information

- The best way to model default arguments is as implicit functions that get called as needed. This handles scoping correctly and avoids weirdness trying to clone expressions.
- However, the default for a parameter is part of a function’s API; changing it counts as changing the behavior of the function just as much as changing the body. Moreover, someone should always be able to explicitly provide a default, so in Swift it’s not even allowed to reference anything non-public (for a public function).
- Defaults should generally be shown in API docs, so that people don’t have to write prose for them. (Having neither the expression nor prose makes the default a wild card for callers, which is not responsible API stewardship.)
- Sometimes you reference a function _without_ calling it. This should use the full name, not the base name, if you support label-based overloading. (Swift unfortunately does not have this rule, largely because we couldn’t think of how to spell it for functions with no arguments.) If retrofitting this onto an existing system, the base name should unambiguously refer to “the overload with no labels” or something.
- [Argument labels do not belong in function types.](https://internals.rust-lang.org/t/pre-rfc-named-arguments/16413/80) If you want function-typed values to have labels, figure out how to write bindings with argument labels.
- What’s the type of a function with default arguments? Most languages say it’s the full signature, but I think a few allow that to be coerced to a function with fewer arguments. Which can be more convenient than a closure. (Swift does not have this but might get it in the future. Aria touches on this in her post; she’s in favor.)

  It’s also _possible_ to have function types _know about default arguments_, but because labels don’t belong in function types I don’t think I recommend that. Consider the default arguments to be associated with the name of the function and not the value.
- Traits get weird, because now there’s _more than one place_ a default can come from. Swift kinda shrugs its shoulders about this, but because Rust separates trait methods from inherent methods it could do something stronger.
- Rust _has_ overload resolution today, in preferring inherent methods over trait methods. How does that work if the trait has `append(_:)` and the inherent impl adds `append(``contents_of:)`? I think you want to allow access to both, but default arguments could make that trickier.
- Default arguments have a knock-on effect of making it cheaper to add _just one more argument_ to a function, leading to signatures in Python in particular that I find super unwieldy. This is a style argument, but it’s a slippery slope case: the first few default args are convenient, but then you can’t remove them if you want to switch to a Config struct instead. Doubly so if you don’t have label-based overloading. (I’m pretty sure this is one of the main reasons Python ended up with catch-all labeled arguments: it simplifies forwarding.)

This entry was posted on [April](https://belkadan.com/blog/2022/04) 24, [2022](https://belkadan.com/blog/2022) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Rust](https://belkadan.com/blog/tags/rust), [Swift](https://belkadan.com/blog/tags/swift), [Programming languages](https://belkadan.com/blog/tags/programming-languages)
