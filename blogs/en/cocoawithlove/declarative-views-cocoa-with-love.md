---
title: 'Declarative Views | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/declarative-views.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:0812d0fa46cc9019'
translated: false
---

> 原文：[Declarative Views | Cocoa with Love](https://www.cocoawithlove.com/blog/declarative-views.html)　·　Cocoa with Love (Matt Gallagher)

In the previous article, I released CwlViews. Its key feature is a unique take on “declarative views”.

_Most_ modern approaches to view frameworks use some form of declarative view construction. This has slowly evolved from serialization (like Storyboards), through data bindings to more modern approaches which make views into a “declarative system”. In fact, for the last couple of years, a persistent rumor claims that Apple themselves plan to release a new declarative view framework for Cocoa.

In this article, I’ll look at the the biggest problem with non-declarative views and how frameworks have slowly become more declarative, over time. I’ll take a guess at what approach a declarative view framework from Apple might use – although keep in mind, I have zero insider knowledge and there’s only a month before WWDC proves how wrong I am.

## Lifecycle is the worst aspect of imperative programming

In my article on CwlLayout, [I stated the following](https://www.cocoawithlove.com/blog/cwllayout.html#declarative-programming):

> _[In a declarative system]_ rules and relationships cannot be changed during the lifetime of the system (they are invariant), so any dynamic behavior in the system must be part of the description from the beginning.

When I was relatively new to application programming, I didn’t understand this mindset. Applications are highly changeable systems and trying to describe them using “invariant” rules seemed impossible. I thought that imperative programming was therefore better for managing change.

Except that _our programs themselves are invariant_. The code is fixed before the program is executed. Just because code is invariant, doesn’t make it less capable of describing and handling a changeable system.

A better way to think about imperative versus declarative is not to focus on “invariant” but instead to focus on timing, conditions and checkpoints:

- : you run the system to the next lifecycle checkpoint and then you read state of the system, looking for specific conditions, running your code if one of those conditions are discovered
- : you load your handlers and their conditions into the system before starting and the system runs itself to completion, calling your handlers if their conditions are met at any point

Imperative often feels easier because if you know one broadly useful checkpoint, you can set a breakpoint there, inspect the variables on the stack at that time and try to correct every value that doesn’t match what you want it to be. Programming solved!

The problem is that this type of inspect-and-set programming needs to be performed at exactly the right point in the lifecycle. You can’t make decisions if the values you need to check aren’t available or are going to change further. Similarly, it’s no good setting a property if the very next lifecycle event is going to overwrite the change.

To see how tricky choosing the right moment can be, let’s look at the standard view-lifecycle checkpoints in Cocoa. All of these are involved when segueing to a new `UIViewController` in an iOS app:

- `UIViewController.init`
- `UIViewController.prepare(for:sender:)`
- `UIViewController.loadView()`
- `UIView.init`
- `UIView.awakeFromNib()`
- `UIViewController.viewDidLoad(_:)`
- `UIViewController.viewWillAppear(_:)`
- `UIView.didAddSubview()`
- `UIView.willMove(toSuperview:)`
- `UIView.willMove(toWindow:)`
- `UIView.didMoveToWindow()`
- `UIView.didMoveToSuperview()`
- `UIView.updateConstraints()`
- `UIViewController.updateViewConstraints()`
- `UIViewController.viewWillLayoutSubviews()`
- `UIView.layoutSubviews()`
- `UIViewController.viewSafeAreaInsetsDidChange()`
- `UIViewController.viewLayoutMarginsDidChange()`
- `UIViewController.viewDidLayoutSubviews()`
- `UIViewController.viewDidAppear(_:)`

These lifecycle events relate solely to the construction and presentation lifecycle of a view. This doesn’t cover state restoration, drawing, interaction, post-presentation animation or data update lifecycles.

Needing to understand all of these lifecycle events – what data is available at each point and what properties can be safely set – is a loaded shotgun pointed at the feet of every Cocoa programmer. Even if you think you understand all these functions, eventually, you’ll shoot yourself in the foot. There’s too much to consider and the inner workings of Cocoa aren’t really documented. You mostly learn what can and cannot be safely done by screwing up.

## Declarative instead

In a declarative system, all of this goes away because your rules are always true. The lifecycle still occurs but you don’t need to make decisions based upon it. Your rules will be applied automatically, at the best possible time.

Since you don’t need to understand how the declarative system works, you’re not as dependent upon its minor details. Fewer dependencies make code easier to abstract and consequently, you can make improvements at every level.

Without lifecycle, there is still complexity. You still need to handle presentation logic and interaction logic. You still need to manage state. But you don’t need to go back to the view you’ve already built and correct its properties.

## The trend towards declarative

Over the last 30 years, I see views as having evolved towards being more declarative along the following progression:

1. XML in Cocoa Storyboards
2. Views and bindings described in XML, like .NET XAML
3. Declarative code construction
4. Immutable virtual views, emitted from a reducer, like The Elm Architecture
5. Views and bindings in immutable structures, like CwlViews

### XML in Cocoa Storyboards

Interface Builder has always been declarative. Recent versions use XML but the overall premise is the same in binary-format NeXTSTEP Interface Builder (NIB) files and the Lisp files used by ExperLisp (Interface Builder’s ancestor) before that.

Modern Storyboards XML looks like this:

```xml
<viewController id="BYZ-38-t0r" customClass="ViewController" customModuleProvider="target">
    <view key="view" contentMode="scaleToFill" id="8bC-Xf-vdC">
        <rect key="frame" x="0.0" y="0.0" width="375" height="667"/>
        <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
        <viewLayoutGuide key="safeArea" id="6Tk-OE-BBY"/>
    </view>
</viewController>
```

While XML is technically declarative (it defines a hierarchical relationship), the view objects constructed do not form a declarative system and rely on significant imperative work to establish any behaviors or data relationships.

Really, this is the baseline. Almost all declarative approaches can improve upon this.

### Views and bindings described in XML

This is a fragment of .NET XAML:

```xml
<TextBox
   Height="23"
   Margin="174,46,12,0"
   Text="{Binding Path=username}" />
```

The big difference here over Storyboard XML is the the `{Binding Path=username}`.

Within braces, XAML embeds a template language. Since this template language is purely functional, capable of transformations, loading resources, reorganizing the view hierarchy and other work, it can smooth over some aspects of lifecycle and configuring, without exposing lifecycle complications.

However, this template language is very cryptic and difficult to use. There’s no debugging, stack traces are useless and it’s usually best left as simple getter/setter bindings.

Cocoa Bindings, available on macOS and Data Bindings on Android offer _some_ of the same capabilities.

> **Benefits**: basic data lifecycle relationships are established.

> **Drawbacks**: not a complete declarative system in most cases – there are usually many lifecycle-dependent followups required to handle logic that isn’t easily captured by simple bindings. Limited ability to restructure based on parameters and data. Cryptic and hard to debug.

### Declarative Construction in Code

Historically, some programmers have preferred data-formats like XML on the grounds that they reduce the amount of code in the program and hence make the program easier to maintain.

More recently, this interpretation of data-formats has changed. Data-formats do not really reduce the amount of code in the program because they themselves _are_ code. The XML format used by Interface Builder is really code that can’t be parametrically driven, can’t easily share definitions from the rest of the project and introduces a number of potential runtime failure cases because it is not validated against definitions across the project by the compiler.

For use entirely within a single project, programmers have started to favor code that is structurally similar to XML but is written in the same language as the rest of the project.

The following example isn’t possible at the moment, but would be possible if Cocoa classes were given declarative constructors (constructors that can build and set all relationships without needing multiple steps, subclasses, delegates, data sources and lifecycle stages to configure).

```swift
UIViewController(
   title: "My view controller"
   view: UIStackView(
      axis: .vertical,
      arrangedSubviews: [
         UILabel(text: "A static table"),
         UITableView(
            rows: [
               UITableViewCell(
                  contentView: UILabel(text: "Row 1")
               ),
               UITableViewCell(
                  contentView: UILabel(text: "Row 1")
               )
            ]
         )
      ]
   )
)
```

This allows initial construction to be vastly simpler and more aesthetic in code. You can also use parameters, functions and other standard programming techniques to change the structure of the view based on data – allowing for much better reuse.

This type of programming avoids holding reference to elements in the middle of the hierarchy, so there needs to be careful consideration to avoid programming that _requires_ references (like building autolayout constraints). In my opinion though, this careful consideration results in significant improvements in usability and correctness.

The effect is very similar to what CwlViews enables minus [the syntactic tricks CwlViews uses to handle inheritance and aribtrary argument ordering](https://www.cocoawithlove.com/blog/a-view-construction-syntax.html). All of these points must also be carefully considered. And without reactive programming, you still need to set up various effects over the lifecycle of the view to handle dynamic presentation changes and interaction logic.

> **Benefits**: better construction aesthetics, can be data-driven for better flexibility, minimal changes required relative to existing Cocoa.

> **Drawbacks**: doesn’t handle any dynamic behaviors so there’s still significant management required over the lifecycle of the views.

### Immutable virtual views

The Elm Architecture, React, Flutter and other frameworks popularized another approach: immutable virtual views.

In the [App Architecture](https://www.objc.io/books/app-architecture/) book I wrote with [Chris Eidhof](https://twitter.com/chriseidhof) and [Florian Kugler](https://twitter.com/floriankugler), we showed an implementation of The Elm Architecture. This is a virtual view constructed in that code:

```swift
return View<Message>.stackView(views: [
   .stackView(views: [
      .stackView(views: [
         .label(text: timeString(position), font: .preferredFont(forTextStyle: .body)),
         .label(text: timeString(duration), font: .preferredFont(forTextStyle: .body))
      ], axis: .horizontal),
      .space(height: 10),
      .slider(
         progress: Float(position),
         max: Float(duration),
         onChange: { .seek($0) }
      )
   ])
])
```

The stack views, the labels, the slider and the space are all immutable structs, built using the `position` and `duration` values on `self` (an immutable `PlayerState`). The idea is that if everything is immutable, then there’s no lifecycle or change problems. You build some views and everything just _is_. Since this view construction is in code, it is much more flexible than XML, it is data-driven and can restructure itself entire, based on that data, if it chooses.

These types of system can’t just hook up bindings or allow imperative code – they’re immutable, so bindings or imperative code can’t do anything. Instead, this type of system must use a different way to handle change: totally recreating the view hierarchy on every frame.

This gets to the concept of “virtual views”. Virtual views are a description of the structure and properties in a view hierarchy but they are not the views themselves (so they don’t allocate graphics resources, don’t have identity onscreen and are intended to be very light and throwaway). To translate virtual views into on-screen elements, a “diffing” system must traverse the previous virtual view description and the new virtual view description, determine what has changed and allocate or update only those views which are different.

Since a new virtual view system must be emitted on each change, the diffing system typically owns all view-state in the program. This is normally done through a single global “reducer” which handles changes with functions of the type: `(changeMessage, oldState) -> (newState, sideEffectCommand)`. All your changes – like the `.seek` and `.togglePlay` messages in the code, above – are change messages that must be understood and handled by this reducer.

Frameworks usually smooth out the change management, so its global nature is less cumbersome, but it usually still remains behind all your actions.

> **Benefits**: Eliminates lifecycle concerns. Code is simple to read. State management has strong, clear rules.

> **Drawbacks**: State management is highly constrained and largely out of your control (you _must_ use the global reducer). Heavily reliant on diffing (which might not correctly detect your changes). May need to retraverse your entire view-state and rebuild the virtual views on every frame (rebuilding the virtual views is cheap but not free).

### Views and bindings in immutable structures

CwlViews is intended to look a lot like virtual views (the Binder structures it creates are immutable like virtual views) but instead of needing to re-render the entire view on each change, changes are handled through bindings. Unlike XAML/Cocoa/Data bindings, these bindings aren’t limited to data changes but can completely manage the entire view hierarchy.

```swift
func textFieldView(_ textFieldViewState: TextFieldViewState) -> ViewConvertible {
   return TextField(
      .borderStyle -- .roundedRect,
      .text <-- textFieldViewState.text,
      .textChanged() --> textFieldViewState.text.update()
   )
}
```

The advantage over Cocoa/XAML/Data bindings is that CwlViews is far more flexible and debuggable (since it is regular Swift code) and far more capable.

The advantage over an immutable virtual views approach is that it is not reliant on any large global reducer or diffing approach. You remain in control over the data and change pipelines and there is a theoretically much lower overhead on changes.

> **Benefits**: Eliminates lifecycle concerns. Capable and flexible. Not reliant on global reducer. Not reliant on diffing.

> **Drawbacks**: Reactive programming is not universally popular and can be tricky to debug.

## What would Apple use?

With Swift 5 introducing ABI stability and Swift 5.1 expected to bring module stability, Swift is finally mature enough that I expect Apple to start shipping Swift frameworks as part of the operating system. I don’t expect any radical overhaul of Cocoa but I do expect something steps that will start to smooth out the Swift experience in Cocoa.

In 2018 when the name “Marzipan” first leaked, [there were numerous references by different bloggers](https://mjtsai.com/blog/2018/05/01/scuttlebutt-regarding-apples-cross-platform-ui-project/) to a separate, unrelated project, supposedly a “declarative” UI framework for UIKit and macOS. Following a [tweet by Mark Gurman](https://twitter.com/markgurman/status/991369046628225025), most people have referred to it as “Amber”.

As much as I hate to engage in rumor speculation, it’s important to be ready for changes that might realistically affect iOS and macOS development.

If Apple were to introduce a new “declarative view construction framework” at WWDC this year, what would it be? I see three possible answers:

### Minimal declarative changes

The simplest action for Apple would be to adopt declarative construction in code for views. This wouldn’t be zero effort – as I said, many interfaces need to be rethought to allow relationships to be established without using references – but it wouldn’t conflict with existing code and wouldn’t require changing any underlying behaviors in Cocoa.

If these Swift wrappers were written carefully, they could abstract away iOS and macOS differences. Realistically though, eliminating differences between iOS and macOS will require changes in the underlying objects themselves. However, Apple have shown a desire to better integrate between iOS and macOS so I wouldn’t be surprised to see AppKit and UIKit classes co-evolve to increase similarity and support this idea.

### Swift Storyboards

Many of the rumors around declarative AppKit/UIKit have referenced Swift and Interface Builder. So let’s apply a little wishful thinking to that space.

Storyboards could entirely replace XML with programmatically generated and managed Swift. Parsing Swift using libSyntax could replace parsing XML. All of the same structures used in XML could be expressed in Swift. With a little construction interface rethinking, you could eliminate the computer-generated `id` tags that make the XIB XML format annoying to read and make the entire experience user-readable and (optionally) hand-editable.

With a file-format that uses Swift, Interface Builder could offer numerous Swift integration advantages, directly importing definitions from the remainder of the program and exporting Interface Builder definitions as Swift definitions.

Exporting definitions (like colors, localized strings and image resources) from Interface Builder could finally replace the horrible stringly-typed experience for assets with typesafe generated definitions (something other platforms have had for decades).

Storyboards could even embed user code to conditionally build or change parts of the hierarchy. Using a real programming language for Interface Builder would bring it back to its roots when it was incrementally compiled LISP code, rather than a serialization format.

Finally, the Swift declarative construction code used to replace the XML would be usable outside the Interface Builder files. In essence, this option would be a superset of the “Minimal declarative changes” approach, described above.

### Apple’s own reducer and virtual views

I do not see Apple embracing a reactive programming dependent library like CwlViews. Reactive programming just isn’t popular enough.

From my perspective then, if Apple wanted to try a wholly declarative system, the only other approach in common usage would be to use virtual views and a global view-state reducer.

In support of this idea is that Elm, Flutter, React and others have already shown that it can work so it would be easy to see as a “proven” approach to improvement change management, reusability and separation of concerns. However, Elm, Flutter and React are all decidedly more “web-inspired” than anything in Cocoa and all rely on language virtual machines and heavy-weight layout engines.

I think this might be too big a change for Apple and too opinionated for a general purpose framework.

## Conclusion

There’s a big difference between “declarative construction” (syntax) and a “declarative system” (a system where rules and relationships are fixed for the whole lifetime).

Cocoa has _always_ had “declarative construction” via NIB/XIB/Storyboard files. Meanwhile though, the experience of constructing views in code has generally required a series of mutable imperative statements to assemble most views. If nothing else, declarative Swift construction code for Cocoa classes would be a nice improvement – even though syntax along won’t change much in the long run.

A fully declarative system is required to properly eliminate the biggest problem with imperative view programming: lifecycle. However, there are only a couple choices for fully declarative systems and the choices that do exist are far from mainstream (outside of web programming).

Will Apple introduce a declarative views system at WWDC this year? I have no idea. But if they did, then I think replacing XML storyboards with generated Swift – that can further embed custom Swift and import and export definitions to the rest of the program – would be ideal because it would smooth out some pain points (including bindings and customization in Storyboards) without forcing any other large changes on Cocoa developers.

Obviously, I wrote CwlViews so I do think that Cocoa developers _should_ try more dramatic approaches towards declarative view programming but I’m not sure the developer community has fully embraced any particular approach enough that Apple would make a serious investment.

### Looking forward

There are plenty of little tricks in CwlViews that I’ll want to share but first I might wait and see what _actually_ gets released at WWDC.
