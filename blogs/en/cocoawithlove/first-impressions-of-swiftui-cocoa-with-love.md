---
title: 'First impressions of SwiftUI | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/swiftui.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:b5a53a8e30acc1e4'
translated: false
---

> 原文：[First impressions of SwiftUI | Cocoa with Love](https://www.cocoawithlove.com/blog/swiftui.html)　·　Cocoa with Love (Matt Gallagher)

A little over a month ago, [I released CwlViews](https://www.cocoawithlove.com/blog/introducing-cwlviews.html) and then [followed up with an article](https://www.cocoawithlove.com/blog/declarative-views.html) suggesting that Apple might be about to release their own declarative views library. [At WWDC this week](https://developer.apple.com/wwdc19/), they did just that, [releasing SwiftUI](https://developer.apple.com/xcode/swiftui/).

This article will look at how SwiftUI’s approach to declarative views compares to CwlViews, why the two approaches differ and what Apple changed to make this possible. I’ll end with some thoughts about how this will affect macOS and iOS development.

## Everyone and no-one saw this coming

Hooray, I predicted a thing. But I still managed to be surprised.

Apple did, [as rumors suggested over a year ago](https://mjtsai.com/blog/2018/05/01/scuttlebutt-regarding-apples-cross-platform-ui-project/), introduce a declarative views library. I correctly surmised that Interface Builder XML would be replaced by Swift code. I didn’t include my prediction that numerous recent Swift evolution proposals might herald integration with this library but that too was apparent.

However, I had expected the library to be a layer on top of AppKit/UIKit so almost everything else about SwiftUI took me by surprise. I mean, you don’t just casually replace frameworks with a 30 year history.

Of course, Apple didn’t do this on a whim and it appears that parts of SwiftUI have been in development for 7-10 years (yes, [multiple Swift components released at WWDC this year predate Swift](https://twitter.com/jckarter/status/1135903779071483906)). A huge number of components (across platforms, Xcode, toolchains) have been developed to support the effort. It’s possible that hundreds of developers have been involved with an effort of this scale.

## SwiftUI versus CwlViews

How does SwiftUI compare to my one-developer side-project?

SwiftUI and CwlViews have some similar goals.

1. Both are syntactically declarative, building composeable expressions.
2. Both eliminate Controllers, stepping away from the Cocoa MVC pattern.
3. Both have their own concept called bindings.
4. Both build views in code, eliminating Interface Builder XML.
5. Both can be hosted in an NS/UIView and can host NS/UIViews.

But there’s a single, big difference between the approaches of the two: CwlViews is based around the idea of _maintaining_ the underlying behaviors of AppKit/UIKit. SwiftUI set aside most of these underpinnings and remade parts of the Swift language and Xcode IDE to support it.

### Quick comparison

A CwlViews constructor for a text field looks like this:

```swift
TextField(
   .borderStyle -- .roundedRect,
   .text <-- textFieldViewState.text,
   .textChanged() --> textFieldViewState.text.update()
)
```

Equivalent code in SwiftUI looks like this:

```swift
TextField($text)
   .padding(8)
   .border(Color.gray, width: 1.0, cornerRadius: 8.0)
```

They are both single expression constructors hiding significant work under the hood and the onscreen appearance of both is very similar to the user. But there are many differences in approach – even in this small amount of code.

### One-way versus two-way bindings

SwiftUI uses two-way bindings (the solitary `$text` value), versus CwlViews’ dual one-way bindings (`textFieldViewState.text` and `textFieldViewState.text.update()`).

One-way bindings are largely _required_ when interacting with `UIKit` views because `UIKit` will emit a notification whether the user interacts with the control or you set the controls value programmatically. Emitting a notification in response to programmatic changes is bothersome and requires that any binding to the control treat send and receive paths separately or you’ll get a recursive loop (set a value on the view and it immediately emits the change back to your model which re-emits that value to the view again).

SwiftUI clearly has different behavior at the core of its views so they emit changes only from the user, not from programmatic events. This is an example of SwiftUI fixing the underlying behaviors, rather than creating a system that works around existing behaviors. It does have some downsides (it’s harder to handle asymmetric view-logic like view-formatting and input-sanitization) but overall, two-way bindings are more concise so it’s a win.

### Applying multiple styles

It might not be clear but the very approach that CwlViews and SwiftUI each use for constructing the `TextField` (parameters to a constructor for CwlViews and chained transformations for SwiftUI) is not merely an aesthetic choice but reflects how the underlying framework functions in each case.

Imagine if CwlViews used the same trailing transformation functions to apply properties, like this:

```swift
TextField()
   .borderStyle(.roundedRect)
   .text(textFieldViewState.text)
   .textChanged(textFieldViewState.text.update())
```

To do this, CwlViews would need to mutate the `Array` of bindings it contained. This would mean that the Binder would need to be inherently _mutable_ (which could lead to a range of correctness problems and reduced performance) or would require applying the bindings over time to the underlying view (which would lead to significantly more problems, including removing CwlView’s ability to shield the programmer from view-lifecycle and loss of testability).

CwlViews _must_ pass all its parameters to a single constructor because it is constructing a single immutable object.

SwiftUI is doing something very different. SwiftUI is not mutating a single underlying `TextField`. Each of the SwiftUI properties is applied to a different view. The `TextField` in Swift is constructed as a series of progressive wrappers with each enclosing the previous layer. Among other things, this means that you can acheive different effects by applying properties in different orders (e.g. `border` then `padding` would put the padding _outside_ the border, rather than inside).

SwiftUI performs transformations as a series of trailing actions because each one wraps the previous result.

In the `TextField` example, SwiftUI is ultimately building an instace of the following type:

```swift
_ModifiedContent<
   _ModifiedContent<TextField, _PaddingLayout>,
   _OverlayModifier<ShapeView<RoundedRectangle.InsetShape.Stroked, Color>>
>
```

Do you see the `TextField` in the middle, there? It’s wrapped in a padding modifier and overlayed with a stroke modifier that are applied by the two trailing transformations.

### Virtual views versus Binders

If every `View` in SwiftUI was heap allocated, all of these layers would be a nightmare but SwiftUI represents views as value types (typically `struct` instances). Stack allocated `structs` are extremely low cost and can be omitted by the compiler entirely, in some cases.

An **existential** in Swift is a value where the compiler knows the protocol conformance of the type but not the full concrete type. Since the compiler doesn't know the runtime size, it allocates a small box for the value. If the value is bigger than the box – limit is a few 64-bit values – it must be heap allocated, even if the concrete type doesn't normally require heap allocation.

CwlViews is forced to be more heavy-weight. CwlViews `Binder`s (the abstraction it uses around views) are reference (`class`) types. This isn’t by choice. I originally tried writing CwlViews with `struct` types but there were many cases where it seemed natural to use the `Binder` as a proxy for the underlying view and this requires that the two have similar semantics. Additionally, since a `Binder` is normally passed around as an existential type (e.g. the `ViewConvertible` protocol) there’s usually a heap allocation and a reference involved, whether you want it or not (existentials use heap allocation for anything over a few bytes).

CwlViews requires heap allocated references because of the one-to-one relationship between `Binder`s and views and the use of protocols rather than concrete types.

Meanwhile, the `View` types you use in SwiftUI are quite different from the underlying views that get presented onscreen. With SwiftUI, the onscreen views have names like “overlay”, “modifier” or they may be NSViews and UIViews (yes, SwiftUI still uses NSViews and UIViews as tools in its display hierarchy). The SwiftUI `View`s are significantly removed from these runtime types making SwiftUI `View`s a kind of “virtual-view”. This separation means that there’s no expectation for SwiftUI `View`s to behave the same way as a `UIView`. A value type can work.

Of course, SwiftUI also “cheats” relative to CwlViews by changing the Swift language to include opaque return type (i.e. `some View`). With opaque return types, the type signature _looks_ more like a protocol than a concrete type (e.g. `some View` versus `_ModifiedContent<TextField, _PaddingLayout>`) but the compiler always knows the true underlying type so it can make a range of optimizations including correct space allocation to keep the type on the stack rather than overflowing from an existential container onto the heap.

## Change model

Mentioning virtual-views brings me to the biggest surprise in SwiftUI and the biggest difference with CwlViews: the way in which changes are handled.

CwlViews’ change model requires that you send values to your views through reactive programming bindings and your views – which are persistent mutable entities underneath the CwlViews layers – are directly mutated by the bindings. Despite the intermediate layer, you are updating the on-screen representation directly for yourself.

SwiftUI’s change model is a very different beast. Virtual-views like SwiftUI’s, require a specific “render” process to build the real view hierarchy and this process needs to be scheduled. Typically this requires that all changes notify the framework in some way so the framework can schedule rendering. This is why many virtual-view frameworks use a “global reducer” (a single function where all mutations to application state are applied). When the global reducer completes an invocation, it can schedule a render.

In my previous article, I guessed that Apple wouldn’t use a change model as restrictive as a global reducer – and I was correct in that guess. While I’ve already seen people treat a single top-level `@State` variable as an ad-hoc reducer in SwiftUI, that is not the expected approach.

The expected model is that each view in SwiftUI uses properties tagged with one of `@State`, `@Bindable`, `@ObjectBinding` or `@EnvironmentObject`. These attributes are Swift 5.1 [property wrappers](https://github.com/DougGregor/swift-evolution/blob/property-wrappers/proposals/0258-property-wrappers.md) that register the tagged state in a global location and track their changes to invalidate the view hierarchy and start the render process. Introducing property wrappers is another way in which SwiftUI “cheats” relative to CwlViews because it altered the Swift language to smooth out this type of registered state.

Since specific views are tagged, SwiftUI can track the node in the hierarchy associated with the change and avoid re-rendering parent nodes.

A much more surprising optimization is that SwiftUI will avoid re-rendering children that are unchanged, even when the parent nodes change. Exactly how this is done is unclear since SwiftUI `View`s are not `Equatable`. At this point, it appears to me that SwiftUI performs a raw memory comparison on each child `View`. More investigation is required to confirm this but if true, it has significant implications for what you can – and cannot – safely do in a SwiftUI `View` hierarchy.

## Lack of clarity

“Surprising” and “unclear” are not terms we want when exploring new APIs.

I’m going to need plenty of slow, careful investigation around exactly how SwiftUI’s change model works, how SwiftUI optimizes the render-graph and how to precisely control layouts before I feel comfortable using the framework. I dread the fact that I might need to slowly step through everything in assembly just to understand what’s happening.

SwiftUI offers a lot of promise but it has made everyone into a novice and lack of both documentation and experts in the field are adding to the disorientation at the moment. In addition, the nature of larger declarative systems is such that API documentation will never fill-in all the details; there is too much behavior that does not manifest through the interface.

I hope Apple considers open-sourcing SwiftUI. It’s the only way we’ll ever get enough documentation on such a complex framework. Until that happens, the SwiftUI community is going to be full of programmers with inaccurate superstitions about how fuctionality works, avoiding useful parts of the design because they simply don’t have knowledge about the rules that drive it.

Would Apple ever open-source SwiftUI? Based on the history of Apple UI frameworks, the answer would be a firm “no”. However, expectations have changed dramatically in the last 10 years and Apple’s UI frameworks are now the _last_ bastion of closed source in the world of application frameworks. Android, web and now _Windows_ all open source their application frameworks. Keeping SwiftUI closed source would be a competitive disadvantage.

## Where does all this leave CwlViews?

SwiftUI has effectively superceded CwlViews for iOS 13, macOS 10.15 and beyond. CwlViews had a good month. 😄

If you need to target iOS 10 to 12 or macOS 10.11 to 10.14, you’re welcome to use CwlViews. I think it’s much better than using AppKit or UIKit directly but if you want new features in future, you’ll need to maintain the project for yourself. But don’t worry, CwlViews _is_ open source.

Rumors offered a more-than-one-year tip-off that declarative views was the likely direction Apple would take. I continued with CwlViews through to release since I enjoyed the experiments with application design, state management and API design. I also wasn’t sure what Apple’s timeline would be or whether Apple’s declarative views would cover all the same situations that CwlViews covered. It would have been nice if the library itself had a greater life beyond experimentation but there’s no point complaining that technology keeps changing.

SwiftUI starts with a better representation than the `NSView`/`UIView` that underpin CwlViews. This is the final way that it “cheats” relative to CwlViews – even if the surface description is similar, SwiftUI is playing very different game. SwiftUI views describe structure and intent but limit details unless required, allowing the framework to fill-in context and platform-specific details as needed. This lets SwiftUI operate in a multiplatform manner. And of course, SwiftUI features interactive integration with Xcode, making the editing experience responsive and enjoyable.

CwlViews had much smaller ambitions so it achieves significantly less. Not bad for a single-person side project but it’s nowhere near the massive effort that SwiftUI has likely been (and will continue to be).

My CwlSignal library is probably deprecated now, too. This is more sad to me. I haven’t taken a close look at Combine but the WWDC presentation and API documentation imply that Combine is a conventional implementation of reactive programming (offering subjects and independently evaluated sequences). CwlSignal used a different model (asynchronous message passing through a shared graph of actor-like nodes) which enabled re-entrant sending, multi-threaded graph manipulation during signal sending, synchronous delivery of cached values and activation/deactivation events. These concepts are likely to get left behind but they were great.

I’m hardly the only developer to be impacted by changes this year: everyone with a reactive programming framework, package manager, or _anything_ tied to UIKit or AppKit is in a tough spot. [I wrote a book on App Architecture last year](https://www.objc.io/books/app-architecture/), largely based upon UIKit; I don’t know if it needs an update or a sequel but books focussing on UIKit aren’t likely to be the future. I have friends with commercial libraries and developer tools reliant on aspects of UIKit and AppKit that are wondering if anything can be salvaged or if they’ll have to cut their losses and move on.

## Conclusion

SwiftUI, Combine and other changes like Swift Package Manager in Xcode are all big disruptions announced at WWDC this year.

Long term, SwiftUI will be good but it’s going to be years of transition before most projects have a minimum deployment target of iOS 13 or macOS 10.15. As with the first year or two of Swift development, I expect a lot of hastily started, poorly implemented and quickly forgotten projects. The SwiftUI implementation, its API and associated tooling are likely to change rapidly as serious bugs and gaping holes are patched.

I hope Apple open source SwiftUI – to aid understanding, promote developer confidence and enable the possibility of SwiftUI outside Apple platforms. But I won’t hold my breath for an official answer, even though the Swift language and every major UI framework on every other platform have all shown the benefits.

I’m sad that two of my biggest open-source projects are largely deprecated but that’s the way things go.

### Addendum: what happens to the name “Cocoa”?

Is the name “Cocoa” deprecated for describing iOS/macOS UI development?

We can write a program without linking the “Cocoa.framework” but that was always true since “Cocoa.framework” was only ever a wrapper for “AppKit.framework”, “Foundation.framework” and a few others. iOS development never had a framework with “Cocoa” in the name but was still officially called “Cocoa Touch”.

It’s not as though the NeXTStep derived Objective-C classes are going to be wholly replaced any time soon. Even excluding Foundation, SwiftUI replaces only _some_ Objective-C user-interface classes. Many, like `NSApplication` and `UIApplication` remain required, while others, like `UINavigationController` and `NSButton` are used internally by SwiftUI.
