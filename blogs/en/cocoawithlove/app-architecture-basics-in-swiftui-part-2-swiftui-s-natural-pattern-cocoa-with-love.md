---
title: 'App architecture basics in SwiftUI, Part 2: SwiftUI''s natural pattern | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/swiftui-natural-pattern.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:b5c6c9ed00ec16f6'
translated: false
---

> 原文：[App architecture basics in SwiftUI, Part 2: SwiftUI's natural pattern | Cocoa with Love](https://www.cocoawithlove.com/blog/swiftui-natural-pattern.html)　·　Cocoa with Love (Matt Gallagher)

In the [previous article](https://www.cocoawithlove.com/blog/coding-through-iteration-and-integration.html), I wrote a simple SwiftUI app. During the writing, I deliberately kept the code simple – writing code only when needed to satisfy user-facing goals. I want to take a closer look at the application architecture that naturally emerges in SwiftUI when following this kind of functionally minimalist approach.

Perform a web search for “SwiftUI pattern” and you’ll find numerous discussions of SwiftUI that wonder if its use of model-bindings make it a form of Model-View-ViewModel (MVVM) or if its use of immutable views and view-state make it redux or Elm-like. While SwiftUI does include these components, the reality is much simpler: SwiftUI’s natural pattern is a form of Model-View-Controller (MVC), although very different from UIKit MVC.

In any case, the precise naming is less important than the components that work together to form the architecture. In this article, I’ll identify the different application architectural roles fulfilled by components of SwiftUI and talk about how they work together to form the overall pattern.

## Changes triggered by model data

SwiftUI introduces many differences compared to macOS AppKit or iOS UIKit but a single difference has the biggest effect on application architecture: how changes are triggered.

Let’s start by looking at how UIKit triggers changes. In UIKit, you construct a tree of view-objects. These objects are reference types and you can hold onto those references to trigger a change.

```swift
let window = UIWindow()
window.makeKeyAndVisible()

DispatchQueue.main.asyncAfter(deadline: .now() + .seconds(1)) {
   let label = UILabel(frame: window.frame)
   label.text = "Boo!"
   window.addSubview(label)
}
```

Here, I’ve created a view (`window`) and I’ve changed its content after 1 second by holding onto the `window` reference and adding a new subview which triggers the update.

Here’s how it might look in SwiftUI:

```swift
struct ContentView: View {
   @State var showSubview: Bool
   var body: some View {
      ZStack {
         Color.white
            .onAppear {
               DispatchQueue.main.asyncAfter(deadline: .now() + .seconds(1)) {
                  self.showSubview = true
               }
            }
         if showSubview {
            Text("Boo!")
         }
      }
   }
}
```

Oh look, I’ve managed to find one of the few scenarios where UIKit is more syntactically efficient than SwiftUI.

Let’s ignore that because there’s a more important difference.

- In UIKit, I changed the `subviews` of the window – a **UIKit** property – and that triggered the view update.
- In SwiftUI, I changed `showSubview` – my **own** property – and that triggered the view update.

What difference does that make?

It means my own values are the source of truth for the View, not the state of a view-tree. I must create data which represents the current view-state. This is a Model (or a Model-interface*) and it is mandatory in SwiftUI whereas in UIKit is was [possible to create an app without one](https://www.cocoawithlove.com/blog/worst-possible-application.html).

> * A Model is a repository of domain _logic_, not _data_. Data and definitions exist in the Model only to communicate (interface) with other layers. Please don’t look at this `@State var showSubview: Bool` and think that’s all a Model should do. Ideally, the timing details and the assignment would be expressed inside the Model but I’m trying to keep things simple.

## Construction role

In UIKit, lots of components can, and do, fulfill parts of the view-construction role. Some of them are scattered across storyboards, `UIViewController` lifecycle methods, methods in `UITableViewDelegate` (among others) and `UIView`s themselves. Nominally, construction is a `UIViewController` responsibility but implementation-wise, it’s a bit of a mess.

In SwiftUI, it should be obvious that `View`s construct themselves however, it’s not as simple as that. While SwiftUI doesn’t have a direct counterpart to `UIViewController`, there are some `View`s that focus on construction and some that focus on layout and drawing.

To explain how this works, I want to look a little closer at the two different kinds of `View`:

1. **built-in views** return `Never` from their `body` function
2. **compositional views** return another `View` from their `body` function because they really just serve to configure and aggregate underlying views and may hold observable state

You could break each of these into sub categories but this is enough for the purposes of this article.

We can’t write the first kind of `View` ourselves because they are effectively the rendering primitives in SwiftUI (like CoreGraphics functions in UIKit). They draw the text, fill and stroke the beziers and position elements.

By contrast, all of the views we actually write in SwiftUI primarily serve to group, layout, bind to data and construct these built-in views.

Let’s look at the default Xcode template for the `ContentView`, used as the placeholder View in the code for the previous article:

```swift
struct ContentView: View {
   var body: some View {
      Text("Hello, world!")
         .padding()
   }
}
```

In this example, `ContentView` is a compositional view but `Text` and the `ModifiedLayout` produced by the `.padding()` call are built-in views and are specially handled by the SwiftUI system.

```swift
@available(iOS 13.0, macOS 10.15, tvOS 13.0, watchOS 6.0, *)
extension Text : View {
    public typealias Body = Never
}
```

It’s not possible to have a `Body = Never` for our own views. It is feature of built-in views, only.

It should be clear that compositional views (particularly the higher level ones) are the scene constructors in SwiftUI and the built-in views fulfilling the rendering role.

## Event handling role

For view interaction to work, there must be code that receives “events” and can trigger code in other parts of the system.

In SwiftUI this is handled by `action` closures, sometimes as part of a visible `View` (like a `Button`) and sometimes as a standalone `on` event-handler.

The `.onAppear` transformation appends an event-handling view – another SwiftUI built-in view – which calls a closure that captures our view and can access its `@State` variable.

```swift
struct ContentView: View {
   @State var showSubview: Bool
   var body: some View {
      ZStack {
         Color.white
            .onAppear {
               DispatchQueue.main.asyncAfter(deadline: .now() + .seconds(1)) {
                  self.showSubview = true
               }
            }

         /* ... other code omitted ... */
      }
   }
}
```

In some respects, this is similar to the Target-Action pattern in UIKit. However, the immutable nature of SwiftUI views encourages the notion that destination of an event should be one of the mutable SwiftUI model properties, like the `@State` in this example.

This enforces the notion that events come from view-hierarchy elements and the interaction is sent directly to the Model – an improvement compared to Target-Action in UIKit which typically sent interactions via the Controller-layer.

> I’m making the claim that all `@State` properties in SwiftUI (like the `showSubview` property) are Model-layer entities since they are decoupled, observable and directly drive View-updates. SwiftUI’s View-state is similar to the Elm architecture where View-state is just a kind of Model-state, compared to UIKit where View-state was an unobserved side-effect.

## Data binding role

Where the event-handling role is concerned with incoming changes triggered by the View-layer, data-binding is concerned with outgoing changes from the Model-layer.

UIKit traditionally (prior to Combine) had no data-binding beyond key-value observing and `NotificationCenter`. Cocoa on macOS had Cocoa Bindings, which could be powerful but were difficult to extend, opaque to the reader and have been effectively deprecated for a decade.

SwiftUI, on the other hand, is built around data-bindings – tracking which `View`s are dependent on which `DynamicProperty` (`@State`, `@ObservedObject`, et al) state properties and making sure views are re-generated when the state changes. While the exact machinery inside these property wrapper attributes is opaque to us, we don’t typically need to worry – just use the state and the binding is established automatically.

Once again, this is a role assigned to our compositional views, since they are the ones which host Model properties like `@ObservedObject` and `@State` properties.

In the `showSubview` example, above, the `ContentView` is responsible for establishing a connection between the `showSubview` View-state and the appearance of the `Text`.

```swift
struct ContentView: View {
   @State var showSubview: Bool
   var body: some View {
      ZStack {
         /* ... other code omitted ... */

         if showSubview {
            Text("Boo!")
         }
      }
   }
}
```

## Taken together, what does all this mean?

We have:

1. A Model, enforced by SwiftUI’s approach to change management
2. Built-in views handle all the drawing
3. Composite views handle construction
4. Composite views establish Model-to-View bindings
5. Event views route events using Model references provided by composite views

With separate Model and View roles, plus an amalgam of Construction, Event and Binding roles around our composite views, SwiftUI is really just Model-View-Controller, with the composite views acting as the Controller.

If you pay attention only to the names `State` and `View`, you could be forgiven for thinking that SwiftUI’s natural pattern is Model-View but the roles performed by composite views clearly cover the responsibilities of the Controller in MVC, even if SwiftUI makes the syntactic overhead so low that you could overlook it.

The boundary that I’ve drawn between a composite and built-in view is blurred (many built-in views may be internally composite and many of our own views might be static and behavior-less). However, this blurry boundary is not a new complication in an MVC pattern. The UIKit `UIViewController` could perform view styling and didn’t need to have data or behaviors; and container `UIView`s would often function as controllers, applying data connections and establishing links between events and the model.

## Why is the pattern not MVVM?

I want to address MVVM for two reasons:

1. I’ve seen commenters make the mistake of claiming that SwiftUI is, or uses, MVVM.
2. I will talk about ViewModels in a later article of this series and I want the distinction to be clear.

In general MVVM programs should aim to follow these two principles:

1. every data-driven property in the View should be driven by a unique Model property;
2. presentation-logic (like sorting or string formatting) should be applied in the Model before the property is exposed to the View.

Lets focus on two lines from `detailView` in the code for the [CwlFeedReader app in the previous article](https://www.cocoawithlove.com/blog/coding-through-iteration-and-integration.html):

```swift
let isRead = model.isReadStatuses[article.url] ?? false
```

and

```swift
Text(isRead ? "Mark as unread" : "Mark as read")
```

These lines clearly show:

1. the `detailView` reading `model.isReadStatuses` (a property used in multiple parts of the program and definitely not unique to this button label in the `detailView`)
2. the code performs two transformations on the value: `x ?? false` to give a default value when `nil` and then `isRead ? a : b` to transform the `Bool` into a display `String`.

Each of these are violations of the principles that an MVVM program should aim to follow.

You might point out – particularly with the second point – that this is some very minor presentation-logic. And its true that most implementations of MVVM permit _some_ transformations in the View – often including this type of boolean logic. But I’m using this example to highlight in a simple way that SwiftUI allows for an _unbounded_ amount of logic in the View and ultimately this is contrary to MVVM which tries to put all presentation logic in the ViewModel.

If SwiftUI wanted to force an MVVM pattern, it could have made `@Published` properties a single-use, one-to-one binding, to address the first requirement. Upcoming Swift “Ownership” features like consumable and move-only types would make this possible. They were not used.

Similarly, SwiftUI could have taken steps to prevent or limit arbitrary logic in the `body` of `View`. In .NET, the domain-specific language XAML is used to achieve this goal. SwiftUI could have introduced a subset of Swift that permitted only combining operators. SwiftUI did introduce a domain-specific language with `@ViewBuilder` but it is focussed on simplifying composition, not limiting logic.

SwiftUI didn’t take any of these steps so it’s clear that SwiftUI is not MVVM.

## Why do people claim SwiftUI is MVVM?

In researching this article, I found multiple articles and forum responses claiming that SwiftUI is or uses MVVM. Why would people jump to this conclusion?

### Is it the Model-data bindings?

The `@Published` and `@ObservedObject` attributes used in SwiftUI do make observing data changes much easier – especially since some form of data observing is _required_ to perform view updates. Good data observing can significantly improve MVVM where you might have dozens of bindings between each view-model and view.

But the reality is that good MVC apps also use data observing – it is not unique to MVVM. UIKit offered some out-of-the-box tools and most developers supplemented this with their own additions.

The `@Published` attributes make no effort to limit observing to one-to-one scenarios so really, this isn’t a boost to MVVM as much as it is a rejection of programming without data observing.

### Is it Combine?

Apple introduced the Combine framework alongside SwiftUI. Combine is a reactive programming framework and reactive programming frameworks have been commonly used on iOS/macOS to implement bindings as part of an MVVM pattern.

The incorrect implication here, is that SwiftUI implies Combine implies MVVM.

I stated above that Model-data bindings (even reactive programming bindings) don’t imply MVVM but the other implication is also incorrect: just because you’re using SwiftUI doesn’t mean you have to use Combine. SwiftUI offers good _interoperability_ with Combine but any reactive programming when using SwiftUI is a totally optional addition.

Yes, there are some parts of the SwiftUI data flow that _internally_ use Combine (most notably `@Published` and `ObservableObject`) but these are internal implementation details. My [CwlFeedReader in the previous article](https://www.cocoawithlove.com/blog/coding-through-iteration-and-integration.html) did not import Combine or use reactive programming.

### Is it just because UIViewController is gone?

The original Smalltalk definition of MVC had the Controller filling a role closer to “event handling role” than anything else in this article. As I discussed in [Looking at Model-View-Controller in Cocoa](https://www.cocoawithlove.com/blog/mvc-and-cocoa.html) the precise definition of MVC is platform specific, making a precise declaration of whether or not something is MVC a little difficult.

To be honest, I think this might be close to reality.

When MVC in UIKit was discussed, people were not discussing MVC in general. MVC on UIKit meant `UIViewController` and the way it dominated iOS development. `UIViewController` was the screens, the storyboards, the delegate and 80% of the rest.

To many UIKit developers, `UIViewController` defined the Controller in Model-View-Controller. Without it, what do we have?

## Conclusion

I think SwiftUI’s pattern is best described as Model-View-Controller. The Controller role is downplayed and mixed with the View, but that’s common in MVC+Bindings approaches like SwiftUI. However, top-level “composite” views retain the contruction, binding and event routing roles that the Controller in UIKit fulfilled.

Even if we call SwiftUI’s pattern “The SwiftUI pattern” to distinguish from UIKit’s MVC, I think the more important point is to understand that SwiftUI includes:

1. Models and view-state
2. Render-primitive-like built-in views
3. Construction
4. Event handling and model-interactions
5. Data observing and binding

and even though all of these can appear in a 10 line SwiftUI `View`, they are distinct roles and you should be able to identify them separately.

As a developer who has focussed heavily on application architecture, I’m struck by how straightforward the architecture around the View is in SwiftUI. In AppKit/UIKit, there was a continuous question around how to set up observing, where to perform View construction and configuration and whether to bother with the overhead of bindings and event handling. SwiftUI doesn’t eliminate bad architecture but in my experience so far, a good architecture feels much more natural than it ever did in UIKit.

### Looking forward…

In SwiftUI there are fewer application architecture problems to solve around the View-layer and View-bindings but there are still plenty of places for improvement. In the next couple articles, I’m going to look at some architectural patterns to improve the Model-layer.
