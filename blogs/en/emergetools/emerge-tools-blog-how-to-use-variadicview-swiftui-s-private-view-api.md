---
title: 'Emerge Tools Blog | How to use VariadicView, SwiftUI''s private View API'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/how-to-use-variadic-view'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:81ff3baf246ea8bb'
translated: false
---

> 原文：[Emerge Tools Blog | How to use VariadicView, SwiftUI's private View API](https://www.emergetools.com/blog/posts/how-to-use-variadic-view)　·　Emerge Tools Blog

# How to use VariadicView, SwiftUI's Private View API

February 26, 2024 by

[Noah Martin](https://twitter.com/sond813)

iOSSwift

![How to use VariadicView, SwiftUI's Private View API](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.6711c553.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

SwiftUI has an undocumented system for interacting with collections of `View` types known as `VariadicView`. The enum `_VariadicView` is the entry point to this system, which includes other types like `_VariadicView_MultiViewRoot` and `_VariadicView.Tree`. The details of these were explored in a great [post from MovingParts](https://movingparts.io/variadic-views-in-swiftui) and there have been a few other helpful [blogs about it](https://chris.eidhof.nl/post/variadic-views/).

```swift
@available(iOS 13.0, macOS 10.15, tvOS 13.0, watchOS 6.0, *)
public enum _VariadicView {
public typealias Root = SwiftUI._VariadicView_Root
public typealias ViewRoot = SwiftUI._VariadicView_ViewRoot
public typealias Children = SwiftUI._VariadicView_Children
public typealias UnaryViewRoot = SwiftUI._VariadicView_UnaryViewRoot
public typealias MultiViewRoot = SwiftUI._VariadicView_MultiViewRoot
@frozen public struct Tree<Root, Content> where Root : SwiftUI._VariadicView_Root {
  public var root: Root
  public var content: Content
  @inlinable internal init(root: Root, content: Content) {
          self.root = root
          self.content = content
      }
  @inlinable public init(_ root: Root, @SwiftUI.ViewBuilder content: () -> Content) {
          self.root = root
          self.content = content()
      }
}
}
```

The definition of `_VariadicView` in SwiftUI's public interface

When I first read about it, I didn't see the applications to my code. As with most SwiftUI, it relies heavily on generics and can be difficult to see how to use it just from reading the API. Since then, I’ve made it a core part of [SnapshotPreviews](https://github.com/EmergeTools/SnapshotPreviews-iOS) and learned that, despite being a private API, it is very safe to use in production - in fact, many popular apps use it extensively.

This post will explain the specific use case I found for extracting snapshots from SwiftUI previews. Hopefully a concrete example will inspire others to use this powerful SwiftUI feature!

## [Snapshot previews](https://www.emergetools.com/blog/posts/how-to-use-variadic-view#snapshot-previews)

[SnapshotPreviews](https://github.com/EmergeTools/SnapshotPreviews-iOS) is an open-source framework to turn Xcode previews into image snapshots. It powers the Emerge Tools Snapshots product that brings automated snapshot testing to pull requests.

![Snapshots status check](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog20%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Snapshots status check

When you create an Xcode preview with SwiftUI's `PreviewProvider`, you can return multiple previews in a single provider using containers such as `Group`, `TupleView`, and `ForEach`. For example, this code would create two previews:

```swift
struct Provider: PreviewProvider {
static var previews: some View {
  Group {
    Text("Hello")
    Text("World")
  }.previewLayout(.sizeThatFits)
}
}
```

![Two previews from one PreviewProvider](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog20%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

To snapshot each of these previews, we need to take the `View` from a preview provider and split it into multiple views, which can be rendered separately. First, I tried doing this using runtime reflection.

## [Inspecting Swift](https://www.emergetools.com/blog/posts/how-to-use-variadic-view#inspecting-swift)

The open-source framework [ViewInspector](https://github.com/nalexn/ViewInspector) uses runtime reflection like `Mirror` to traverse a SwiftUI view hierarchy and access subviews. You can use it to access internal properties of Apple views, like each subview of a `TupleView`. However, this solution required brittle checks for every type of view and was prone to breaking, Ex: [Optional](https://github.com/EmergeTools/SnapshotPreviews-iOS/pull/54/files#diff-571645ad88ff7f6588274af9a50a7999fb1bcaf3bcb7565a43e4dbd2c5e5ee6eR34), [Group, Tuple, and ForEach](https://github.com/EmergeTools/SnapshotPreviews-iOS/pull/52/files#diff-571645ad88ff7f6588274af9a50a7999fb1bcaf3bcb7565a43e4dbd2c5e5ee6eR84). Additionally, it wouldn't work if you had a custom View that conformed to VariadicView or a [custom ViewModifier](https://github.com/nalexn/ViewInspector/issues/262) that changes the number of views. I needed something more robust to get snapshots working well.

## [Layouts](https://www.emergetools.com/blog/posts/how-to-use-variadic-view#layouts)

In iOS 16, SwiftUI added native support for [layouts](https://developer.apple.com/documentation/swiftui/layout). This lets you treat a `View` as a collection of views to arrange in custom positions. It does almost what I needed, but it does not support hiding views in the collection.

## [Variadic View](https://www.emergetools.com/blog/posts/how-to-use-variadic-view#variadic-view)

The solution to match Xcode’s previewing behavior is to use VariadicView. The whole thing is about [10 lines of code](https://github.com/EmergeTools/SnapshotPreviews-iOS/blob/327e18a10fe07c9b298b7bba91c520fa37406de0/Sources/SnapshotPreviewsCore/ViewInspection.swift).

First, I define a new type, `ViewSelector`, which conforms to `_VariadicView_MultiViewRoot` and, therefore, also `View`. This type has one property `position`, which selects the position in the child views to display.

```swift
fileprivate struct ViewSelector: _VariadicView_MultiViewRoot {
  let position: Int
  func body(children: _VariadicView.Children) -> some View {
    children[position]
  }
}
```

The body function, required by the protocol, receives the children as `_VariadicView.Children`. This type conforms to `RandomAccessCollection` so we can subscript the children and access only the selected position.

Next, an extension on `View` provides functionality to select the subview at a specific index. This uses `_VaradicView.Tree`. The new view type is the tree's root and `self` is the content of the tree.

```swift
extension View {
func selectSubview(_ position: Int) -> some View {
  _VariadicView.Tree(ViewSelector(position: position)) {
    self
  }
}
}
```

## [Is it safe to use?](https://www.emergetools.com/blog/posts/how-to-use-variadic-view#is-it-safe)

We can see all the details of this API in `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/System/Library/Frameworks/SwiftUI.framework/Modules/SwiftUI.swiftmodule/arm64-apple-ios.swiftinterface`. But, this is a private API, so is it safe to use in production? I think it is, and it has been used successfully by many apps.

The key reason you can use it is the VariadicView API is already used in apps, even without developers writing the code explicitly. `_VariadicView` can be emitted into your app just by using `HStack` since it is part of the `@inlinable` initializer:

```swift
@frozen public struct HStack<Content> : SwiftUI.View where Content : SwiftUI.View {
@usableFromInline
internal var _tree: SwiftUI._VariadicView.Tree<SwiftUI._HStackLayout, Content>
@inlinable public init(alignment: SwiftUI.VerticalAlignment = .center, spacing: CoreFoundation.CGFloat? = nil, @SwiftUI.ViewBuilder content: () -> Content) {
      _tree = .init(
          root: _HStackLayout(alignment: alignment, spacing: spacing), content: content())
  }
```

The struct is also marked with `@frozen`, making `_VariadicView.Tree` part of the SwiftUI ABI. If it changed, it would break previously compiled apps that used `HStack`. There are also public SwiftUI types that conform to `_VariadicView.UnaryViewRoot`, such as [`GridLayout`](https://developer.apple.com/documentation/swiftui/gridlayout), making it impossible to remove these protocols. Thanks to [@EricHoracek](https://mastodon.social/@erichoracek) for pointing out these examples!

Since this VariadicView code is already used by having the compiler emit it inline, it’s unlikely there would be any problem using it from your source code directly. Emerge is now using it as the root view of every snapshot we generate, and it might be useful for your views as well!
