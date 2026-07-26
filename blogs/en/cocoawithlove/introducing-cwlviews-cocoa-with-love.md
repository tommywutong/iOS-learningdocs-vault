---
title: 'Introducing CwlViews | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/introducing-cwlviews.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:d78acbabe61605c9'
translated: false
---

> 原文：[Introducing CwlViews | Cocoa with Love](https://www.cocoawithlove.com/blog/introducing-cwlviews.html)　·　Cocoa with Love (Matt Gallagher)

CwlViews replaces the diverse collection of construction and management interfaces in Cocoa with a set of composable, declarative “binding” constructors. The result hides much of the busywork that dogs Cocoa application programming, leaving behind a highly concise, view-state driven, reactively connected experience and offers end-to-end testability.

I’ve been slowly playing with the ideas behind CwlViews in private for 4 years. My primary use-case has been prototyping and experimentation and I’ve been loving every moment of it. I don’t know how others will respond to using CwlViews but it’s now available to try. It’s not an exaggeration to call it a profoundly different way to program Cocoa applications.

> Technically, this isn’t the first release of CwlViews. A limited iOS implementation was included as part of the MAVB chapter of the [App Architecture](https://www.objc.io/books/app-architecture/) book I wrote with [Chris Eidhof](https://twitter.com/chriseidhof) and [Florian Kugler](https://twitter.com/floriankugler), last year. Fun fact: Chris helped with much of the terminology in CwlViews since the terms I initially used didn’t make sense (naming is hard).

## Try CwlViews

The remainder of this article will provide some introductory documentation for CwlViews but if you prefer to learn by doing, then you can start by [downloading or cloning the CwlViews from its github repository](https://github.com/mattgallagher/CwlViews).

The README file includes instructions for manual framework inclusion, Carthage or CocoaPods but the fastest way to try CwlViews is to install the Xcode templates. Once you’ve download the repository, open a Terminal and go to the “Scripts” directory in the repository and run `./install_cwlviews_templates.swift`. After this command completes, you can create a new iOS or macOS “CwlViews” application project from the Xcode “File” menu under “New” → “Project…”. There are also Playgrounds templates to quickly start a CwlViews playground.

> NOTE: you can uninstall the templates by running `./install_cwlviews_templates.swift --uninstall`

If you’re having difficulty seeing how to construct or use a particular view, you can also take a look at the CwlViewsCatalog_macOS and CwlViewsCatalog_iOS apps in the CwlViews.xcodeproj. These are macOS and iOS apps that demonstrate the basic functionality of the views.

![](https://www.cocoawithlove.com/assets/blog/cwlviewscatalog_macos.png)

These catalog apps are primarily a sandbox to test functionality so some examples are more complicated than necessary. For example, the Button includes a combination resizing/fading view layout animation, which is great for testing animation but bad for seeing how a button works.

## What is CwlViews?

### A question about view controllers

The code that became CwlViews started with a simple question: why are view controllers not reusable? When you take away the application-specific code in a typical view controller, there is still a lot of structure and setup work that gets repeated across every similar view in your application.

Common approaches to reuse around view controllers (and composite views and presentation models) all fail. You can achieve reuse with Controls and simple views are through object-oriented abstraction but composite view structures resist any significant attempt at this type of reuse, degrading into “God objects” and other anti-patterns, without offering any real advantages.

View controllers are – by unfortunate design – an intersection of view-logic, view-state and view-lifecycle, multiplied across an entire subtree of a view hierarchy. This multi-axis intersection creates a complicated problem space that is difficult to simplify or replace with a reusable abstraction.

### What CwlViews does

CwlView’s primary aim is to replace composite, multi-role view constructs (including view controllers, storyboards and presentation models) and handle these roles using new constructs that focus on one role at a time. However, the aim is _not_ to force the programmer to do this. The aim is to provide tools to the programmer that _already_ do this, all the programmer need do is use the standard toolset.

CwlViews implements view-logic as Bindings. View-state is abstracted through a construct called Adapters. And view-lifecycle is removed by a construct called Binders. Through these, CwlViews can entirely replace storyboards, view construction code, lifecycle management, presentation logic and observation, interaction logic and actions.

By separating roles in this way, CwlViews can offer highly reusable abstractions and dramatically reduce the number of lines in your program (particularly when Storyboard lines are considered) at the same time as it makes some complex behaviors dramatically easier.

### What CwlViews avoids

CwlViews does not change the behavior of Cocoa classes or objects. The same class names are used for CwlViews Binders (minus their `UI` or `NS` prefix). The same property, method and notification names are used but they are accessed via Bindings. Using properties, methods and notifications will have the same effect as in regular Cocoa without CwlViews.

CwlViews is not an “all-or-nothing” choice. CwlViews is two-way interchangeable with non-CwlViews Cocoa objects. Any CwlViews Binding which accepts a view will accept a `ViewConvertible` (either a Cocoa view or a CwlViews Binder). Any Binder can be turned into its underlying Cocoa view (Binders are merely a lazy-constructors that build a Cocoa view). You can have one subtree in your application that uses CwlViews and another subtree that uses standard storyboards and `UIViewController` subclasses.

CwlViews does not rely on swizzling, undocumented behavior or languages other than Swift. While CwlViews does use the Objective-C runtime for object associated value storage, this is merely a convenience and there are some Binders in the CwlViews library that choose to use an Objective-C runtime independent approach instead.

CwlViews does not hide information – it represents behaviors in a transparent, inspectable manner. In fact, the ability to pull apart a Binder and ask what it is doing is a key part of CwlViewsTesting (the unit/interface testing library). Similar parsing and interrogation is used by multiple Binders to avoid conflicts between base and derived uses of inherited Bindings.

## CwlViews basics

I’ve [previously discussed the view-syntax behind CwlViews](https://www.cocoawithlove.com/blog/a-view-construction-syntax.html) and the [“Model-Adapter View-Binder” (MAVB) pattern it uses](https://www.cocoawithlove.com/blog/mvc-without-the-c.html). This is a quick recap.

Here is small example for constructing a `UITextField`, setting some properties on it and tracking the text value of the field as it changes:

```swift
struct TextFieldViewState: CodableContainer {
   let text: Var<String>
   init() {
      text = Var("")
   }
}

func textFieldView(_ textFieldViewState: TextFieldViewState) -> ViewConvertible {
   return TextField(
      .borderStyle -- .roundedRect,
      .text <-- textFieldViewState.text,
      .textChanged() --> textFieldViewState.text.update()
   )
}
```

This might appear to be a trivial example that you could easily replicate in standard Cocoa but the point of CwlViews is that a small amount of code hides a lot of concepts that are verbose and tricky to implement in Cocoa without library support.

Let’s look at each part line-by-line.

```swift
struct TextFieldViewState: CodableContainer
```

This is an example of a view-state struct. In MAVB, if we want to track any state associated with a view, that state is not stored in the view or a view controller but in a view-state struct, like this. View-state forms a tree that largely mirrors the view hierarchy (albeit more coarsely) and you can serialize the whole view-state tree or log its contents from the top-level view-state value. The `CodableContainer` protocol enables automatic state restoration and also offers tricks like view-state logging on each change.

All properties of a view-state struct should be immutable. `TextFieldViewState` does not directly store the `text` value; instead, it contains a `Var` which wraps the value.

```swift
let text: Var<String>
```

This `Var` is an example of a “Model-Adapter”. A Model-Adapter contains a mutable value and exposes it through a reactive signal input (to update the value) and reactive signal output (to observe the value). Different Model-Adapters offer different inputs to update the stored value in different ways.

This `Var` Adapter – the most common type of Model-Adapter for view-state – offers three inputs:

1. : set a new value and notify the change (default)
2. : set a new value but don’t notify
3. : emit a notification for a new temporary value without changing the persistent value

These inputs are the `Var` semantics in CwlViews but there are other library provided Model-Adapters which provide different semantics – e.g. `TempVar` which notifies but never stores a persistent value or `ToggleVar` which can switch between `true` and `false` but cannot be explicitly set to a value or `StackAdapter` which pushes and pops values onto an internal array.

> A quirk to note is that this `Var` is not initialized at its declaration – e.g. we do not write `let text = Var("")` – but is instead initialized in the `init` function. This is due to a Swift limitation: if you assign a value at declaration then the default `Decodable` conformance won’t be able to set its decoded value – even though `Encodable` has stored an encoded value.

```swift
func textFieldView(_ textFieldViewState: TextFieldViewState) -> ViewConvertible {
```

The `TextFieldViewState` itself is passed as a parameter into the view construction function. The default CwlViews style employs strict dependencies-by-parameter approach (no globals, no two-phase construction). This supports the aim of high refactorability since all dependencies are clearly marked. The return type `ViewConvertible` is a protocol; it is implemented by both `UIView` and `CwlViews.View`. This is key to ensuring two-way interoperability between views that do and don’t use CwlViews – both CwlViews and non-CwlViews variants can be supplied at any point and after construction, the difference is immediately abstracted.

```swift
return TextField(
```

This `TextField` is an example of a Binder. A Binder builds an underlying object and fully configures all the properties so that the underlying object is completely self-managed (you don’t need to set up future property updates, observation, delegates, actions since it is _all_ preconfigured at construction).

This binder is of type `TextField`. A `TextField` will lazily construct and return a `UITextField` when you invoke `uiView()` on it. If you hold onto the `TextField` and call `uiView()` again, you will receive the originally constructed `UITextField` again.

```swift
.borderStyle -- .roundedRect,
```

This is an example of a “Binding” in CwlViews. The left-hand side (the “Binding-Name”) refers to the `borderStyle` property of the underlying `UITextField` object. The right-hand side (the “Binding-Argument”) provides a value of `.roundedRect`. The constant “Binding-Operator” `--` indicates that the property will be set to this value once on construction and then will never change.

```swift
.text <-- textFieldViewState.text,
```

This Binding drives the underlying `text` property of the `UITextField` with a signal. The `text` property will get the initial and subsequent values emitted from the `text` var on the `textFieldViewState`. When a Binding uses `<--` (the signal Binding-Operator) then the Binding-Argument must be a `SignalInterface` (either a `Signal` or a type which exposes a `Signal`). For the `Var` type, it exposes its default output `Signal` that emits every notification (including the initial value).

```swift
.textChanged() --> textFieldViewState.text.update()
```

This Binding provides `text` changes from the `UITextField` and delivers them to the `update()` input of the `textFieldViewState.text` Adapter. As discussed above, the semantics of `Var` specify that `update` changes the persistent value _without_ notifying a new value. This ensures that `textFieldViewState.text` will receive the latest value but won’t immediately emit it back to our `.text <-- textFieldViewState.text` Binding (possibly causing an infinite loop).

> The `update()` input is a good way to break two-way feedback loops. However, sometimes you might have an external observer of state which wants to see both the model-driven values and view-driven feedback updates. This second observer can observe the `allChanges()` output instead of the default (notifications) output – this will ensure the second observer receives both kinds of change.

The `textChanged()` here does not directly refer to any property on `UITextField`. In CwlViews, paretheses in a Binding-Name indicate that this is a “Composite Binding-Name” (an abstraction built on top of another Binding-Name). In this case, the underlying Binding-Name is `didChange` (corresponding to `UITextField.textDidChangeNotification`). The underlying Binding-Name is a little clumsy since it provides the raw `UITextField` to a closure. The `textChanged()` composite binding extracts the latest value of the text field’s `text`, unwraps the optionality of that field (discarding `nil` values) and emits the unwrapped `String` to the `SignalInput` on the right-hand side.

## Binder

A Binder is just a lazy constructor for an underlying object that sets values on construction and hooks up reactive signals for setting future values and receiving future changes.

Binder implementations take the name of their underlying UIKit or AppKit types, minus the prefix. e.g. `View` is the Binder for `UIView`.

A `Binder` always implements the following `init` function:

```swift
init(type: Instance.Type, parameters: Parameters, bindings: [Binding])
```

but you’re more likely to use the convenience constructor where Bindings are provided as a variable argument list:

```swift
View(
   .backgroundColor -- .red,
   .isHidden -- true
)
```

When you construct this `View` Binder, nothing happens. An array of Bindings is built but nothing is done with them.

All Binders can be constructed by calling `instance()` on it. However, `instance()` requires that you know the raw type of the Binder so it’s more common to use the `ViewConvertible` protocol function `uiView()`:

```swift
let view = View(
   .backgroundColor -- .red,
   .isHidden -- true
).uiView()
```

This will construct and configure a `UIView` with the described properties.

You can always specify the subclass for an instance constructed through a Binder.

```swift
View(
   type: UIButton.self
   .backgroundColor -- .red,
   .isHidden -- true
)
```

If a more-specific Binder exists, it’s usually better to use the more-specific binder:

```swift
Button(
   .backgroundColor -- .red,
   .isHidden -- true
)
```

Aside from calling the `Button(type:)` constructor, this `Button` binder implements the `uiButton()` function to construct and return a `UIButton` in a type-safe way – in case you’re passing to a function or other interface that requires a `UIButton`.

You can also construct Bindings as an array:

```swift
let colorBindings = [.backgroundColor -- .red] as [View.Binding]
let visibilityBindings = [.isHidden -- true] as [View.Binding]
View(type: UIButton.self, bindings: colorBindings + visibilityBindings)
```

### Useless error diagnostics

If you ever see Swift point of the end of a Binder constructor and complain about:

```
Missing argument for parameter 'bindings' in call
```

or

```
Missing argument for parameter 'parameters' in call
```

or point to the fourth parameter and complain about an

```
Extra argument in call
```

then Swift is almost certainly wrong about the cause of the error.

In these cases, what has happened is that Swift couldn’t match your code to either constructor (Bindings passed as an array or Bindings passed as a variable argument list) so it has tried to match against the bindings as array variant and failed.

Make sure your code has commas where needed (ensure commas between arguments and remove commas after the final argument). If that’s not the problem, break apart your Bindings into individual arrays (as shown above) and see if you can get Swift to give a better error message when it encounters the bindings one-at-a-time.

## Binding variants

View logic in CwlViews (both presentation and interaction) is primarily expressed through Bindings.

To make Bindings easier to abstract and simplify, they are classified into 5 different varieties (plus one that is built upon the others). These varieties are:

- ,

  and

  Bindings (the presentation logic Bindings that set values on views)
- Bindings (the interaction logic Bindings that communicate view events back to the model)
- Bindings (view-triggered closures used in a variety of ways)

Clearly defining variants is one of the primary ways that CwlViews reduces code duplication and makes code more concise. By clearly defining the overall structure of a variant, it is easier to replace with a reusable abstraction.

### Constant Bindings

This is a property you can set on construction but cannot be changed after construction. You may only provide a constant Binding-Argument.

An example is an iOS button’s `type`. This is a value that is provided to the `UIButton(type:)` initializer and cannot subsequently be changed.

```swift
Button(.type -- .system)
```

### Value Bindings

These are the most common type of binding and represent a typical mutable property. CwlViews will let you set it with a constant value or provide a `Signal` that may give it an initial and/or future value.

```swift
View(.backgroundColor -- .red)
View(.backgroundColor <-- myViewState.isBlue.map { $0 ? .blue : .white })
```

Note that a different Binding-Operator is used (`--` to indicate constant and `<--` to indicate a `Signal`).

### Signal Bindings

These Bindings represent methods that can be invoked after construction and cannot be set with a constant value. They generally involve behaviors that should only be invoked in response to user-actions.

```swift
TextField(.resignFirstResponder <-- myViewState.submitButtonPressed)
```

The distinction between a Signal Binding and a Value Binding is often more informative than technical but some views in Cocoa will not respond to these method-like behaviors until the view is displayed onscreen, or have loaded their data.

### Action Bindings

The Bindings represent target-action behaviors or notifications from Cocoa views. While they are one of the most _important_ Bindings (the primary starting point for interaction logic), they are also the least numerous since a few key implementations (e.g. `UIControl`’s and `NSControl`’s target-actions) handle a large number of scenarios.

```swift
ScrollView(.userDidScroll --> myViewState.scrollLocation)
```

### Composite Bindings

The most commonly used Action-like Bindings are actually Composite Bindings. Composite Bindings are not really their own kind of Binding but are conveniences built on top of primitive Bindings underneath.

The reason Composte Bindings are so common on top of Action bindings is:

1. parameter of

  ) and setting these via the right-hand side Binding-Argument make things look clumsy so a parameter on the left-hand side can help aesthetics
2. The Action often needs to pick up associated view-state from the view to usefully handle the interaction.

The following Composite Binding:

```swift
Switch(
   .action(.valueChanged, \.isOn) --> switchViewState.value
)
```

is equivalent to the underlying Action Binding:

```swift
Switch(
   .action --> ControlActions(
      scope: .valueChanged,
      value: .singleTarget(
         Input()
            .map { ($0 as! UISwitch)[keyPath: \.isOn] }
            .bind(to: switchViewState.value)
      )
   )
)
```

but the Composite Binding is much easier to read.

### Delegate Bindings

The final kind of Binding in CwlViews is a Delegate Binding. These usually correspond to Delegate methods, DataSource methods or other behaviors that require an immediate response. The Binding-Argument for a Delegate Binding must be a function or closure.

For example, the CwlViews equivalent of `UITableViewDataSource`’s `tableView(_:cellForRowAt:)` method is the `cellConstructor` Delegate Binding:

```swift
TableView<String>(
   .tableData -- [["One", "Two", "Three"]],
   .cellIdentifier -- { rowData in "TextRow" },
   .cellConstructor -- { reuseIdentifier, cellData in
      TableViewCell(.textLabel -- Label(.text <-- cellData))
   }
)
```

The `.cellIdentifier` Binding is invoked each time a new row is encountered in the single-section, three-row table.

If no reusable rows exist with that identifier, the `.cellConstructor` Binding is invoked with its closure argument for each row in the single-section, three-row table, constructing the `UITableViewCell` as required.

> In CwlViews, `TableView` is generic over its `RowData` type. Additionally, the Delegate Bindings don’t correspond to `UITableViewDataSource` in a one-to-one fashion. Changes along data driven pathways are the only signficant area where CwlViews has chosen to break the one-to-one mapping between Bindings and underlying class behaviors. In general, Cocoa’s data source interfaces are not well suited to driving via reactive Bindings so some changes were required.

There are two important Delegate Bindings that all CwlViews Binders accept:

```swift
.adHocPrepare -- { (instance: Any) -> Void in /* do something */ }
.adHocFinalize -- { (instance: Any) -> Lifetime? in /* do something */ }
```

These Bindings give you a chance to access the underlying instance and either apply initial changes before any other Binding or final changes after any other Binding. The `adHocFinalize` Binding can also return a `Lifetime` (so it can set up its own behaviors over-time that are tied to the lifetime of the constructed instance).

If you have created your own view subclass with its own properties, you can use these `adHoc` Bindings to manage those properties, without needing to create an entire Binder for your subclass.

## Creating your own Binder

Adhoc Bindings will handle simple cases but you might also want to create your own Binders – especially if you plan to use a class frequently.

Creating a Binder for your own subclasses (or Cocoa classes that aren’t covered by CwlViews) isn’t technically challenging but there is a lot of boilerplate. A trivial implementation is around 85 lines spread over 10 sections.

To simplify this, one of the Xcode templates installed by the `./install_cwlviews_templates.swift` script is a file template named CwlViewsBinder. This will automate the ugliest parts and provides examples of the most common scenarios.

Most of the work a Binder does is mapping Value Binding names onto property setters so most of your Binder will look like this:

```swift
case .currentPage(let x): return x.apply(instance) { i, v in i.currentPage = v }
```

Keep in mind though: there are no “getter” Bindings so you must offer notifications (Action Bindings) when state changes.

## Adapters

Model-Adapters manage mutable state in CwlViews. Model-Adapters in CwlViews are instances of `Adapter<State: AdapterState>` with the different `State` types determining the valid input messages, the reducer function and the notification type.

For example, the typical view-state Model-Adapter, `Var` is a typealias for `Adapter<VarState>` where the `.set`, `.update` and `.notify` messages and the behavior in response to those messages is determined by the `VarState` type.

A majority of state – particularly view-state which tends to follow basic setter semantics – can use one of the library provided Model-Adapters. But there will certainly be cases where you want custom change/update rules and in these cases you’ll need to implement your own `AdapterState`.

Here’s a custom AdapterState implementation that is primarily a settable variable but emits a notification only if the newly set value is different to the old value:

```swift
struct DistinctState<Value: Equatable & Codable>: PersistentContainerAdapterState {
   var value: Value
   init(value: Value) {
      self.value = value
   }

   func reduce(message: Value, feedback: SignalMultiInput<Value>)
      throws -> (state: DistinctState<Value>, notification: Value?) {
      if message != value {
         return (state: DistinctState(value: message), notification: message)
      } else {
         return (state: self, notification: nil)
      }
   }
}
```

With larger models, observers are most likely interested in a specific “slice” of the model, rather than receiving the entire model on every change. For this reason, CwlViews also provides `ModelState` which can be used to build Model-Adapters that efficiently emit filtered subviews of the overall model.

For example, here is `DocumentAdapter`, the Model-Adapter which wraps the `Document` model type in the CwlViews sample application:

```swift
typealias DocumentAdapter = Adapter<ModelState<Document, Document.Action, Document.Change>>
extension Adapter where State == ModelState<Document, Document.Action, Document.Change> {
   init(document: Document) {
      self.init(adapterState: ModelState(
         async: false,
         initial: document,
         resumer: { model in Document.Change.reload },
         reducer: { model, message, feedback in try? model.apply(message) }
      ))
   }
   
   func rowsSignal() -> Signal<TableRowMutation<String>> {
      return slice(resume: .reload) { document, notification in
         switch notification {
         case .addedRowIndex(let i): return .value(.inserted(document.contents.rows[i], at: i))
         case .removedRowIndex(let i): return .value(.deleted(at: i))
         case .reload: return .value(.reload(document.contents.rows))
         case .none: return .none
         }
      }
   }
}
```

When the underlying model is changed, the `slice` closure is called and produces a view of just the table row changes within the document.

Any `Adapter` built using the `ModelState` type also offers a `sync` method for gaining access to the model outside of the reactive pipeline – which is useful for save operations and other accesses that must be synchronous, even when the model is managed on a background thread.

## Testing code written using CwlViews

A key feature of CwlViews is the ability to test all of your presentation and interaction logic – including the Binding to the views themselves – in unit/interface tests. This is an improvement over typical MVC and MVVM approaches which either omit view-controllers from testing or must resort to reading the view hierarchy (unreliable) or running UI tests (slow).

At test time, provided you haven’t constructed the underlying Cocoa view, you can “consume” the Bindings from a Binder, parse the Bindings and use them as an interface to test your program’s logic.

```swift
let viewController = tableViewController(tableState, navState, doc)
let bindings = try ViewController.consumeBindings(from: viewController)
let title = try ViewController.latestValue(for: .title, in: bindings)
XCTAssertEqual(expectedTitle, title)
```

By sending signals to the model-adapters in examples like this, you can test the end-to-end logic in your program without missing any layers.

## Release status

> You can [**download CwlViews**](https://github.com/mattgallagher/CwlViews) and try it for yourself.

The first release is version number 0.1.0. I don’t generally release libraries with a pre-1.0 version number but CwlViews is a difficult project to “finish”.

I broke all my unit tests during refactorings late last year and unit tests on the latest iteration cover just 3 of the 70+ Binder classes so issues likely remain outside these tested areas. Unlike the Binders themselves, there are no templates, scripts or easy patterns to aid writing these unit tests, so it is manual and tedious. Also, while 70+ Binder classes may sound like a lot, they are split between iOS and macOS (40 iOS classes, 32 macOS classes and 6 shared classes) which still leaves plenty of other Cocoa classes that could be covered.

Despite those caveats, I’m happy with the status of the project so I wanted to share it. If you’re prepared to deal with the occasional failure in an untested area, the project is definitely usable.

## Conclusion

CwlViews is probably the most personal project I’ve released on Cocoa with Love. I love writing apps within this framework and miss it when I’m at my day job writing more-conventional MVVM and MVC projects. By comparison, MVVM feels verbose (filled with incessant re-abstraction of data) while MVC feels like you must jump through plenty of hoops to achieve essential functionality and all new functionality interferes with existing functionality.

Of course, there are drawbacks to CwlViews. Swift offers very poor diagnostics if you make a mistake. None of the debugging tools provided with Xcode understand reactive programming flows enough to track the flow of messages through a graph. And some people just don’t want to express their programming logic through reactive programming pipelines.

### Looking forward

CwlViews take on “declarative views” is unique but you may have heard “declarative” applied to other approaches. A long running rumor claims that Apple plan to release their own Swift framework for declarative view construction. As I write this in May 2019, it’s possible Apple could do this as soon as WWDC, next month.

In the next article, I’ll look at the different interpretations of the term “declarative views” and why the overall concept is so popular in new view frameworks. I’ll also guess at what declarative improvements Apple might bring to Cocoa. Spoiler: I really don’t know.
