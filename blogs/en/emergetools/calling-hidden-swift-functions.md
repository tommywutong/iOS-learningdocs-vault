---
title: Calling Hidden Swift Functions
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/calling-hidden-swift-functions'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:7884dfb12525bc72'
translated: false
---

> 原文：[Calling Hidden Swift Functions](https://www.emergetools.com/blog/posts/calling-hidden-swift-functions)　·　Emerge Tools Blog

# Calling Hidden Swift Functions

November 25, 2024 by

[Noah Martin](https://twitter.com/sond813)

iOSReverse Engineering

![Calling Hidden Swift Functions](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.2449c550.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Swift has [6 access levels](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/accesscontrol/?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post#Access-Levels) ranging from open to private. Typically if you do not want consumers of your code to access a function or type, you can mark it `private`. However, Apple frameworks written in Swift, particularly SwiftUI, contain APIs that are meant to be used by other Apple frameworks, but not by 3rd party apps. This is achieved by limiting when the code can be seen at compile time, but still allowing it to be found at link time. In this post we’ll look at how you can still call these functions in your own code to use features that are not typically available.

## [Compiling vs. Linking](https://www.emergetools.com/blog/posts/calling-hidden-swift-functions#compiling-vs.-linking)

First, we’ll walk through how a typical external function call is compiled and used, with the SwiftUI function `Text.fontWeight` as an example. To compile your code that uses this function, the Swift compiler first finds it in a `.swiftinterface` file provided by SwiftUI. Specifically, it is found in `$SDKROOT/System/Library/Frameworks/SwiftUICore.framework/Modules/SwiftUICore.swiftmodule/arm64-apple-ios.swiftinterface` which contains the following:

```swift
extension SwiftUICore.Text {
  nonisolated public func fontWeight(_ weight: SwiftUICore.Font.Weight?) -> SwiftUICore.Text
}
```

These interface files do not provide the implementation, just this skeleton that the compiler needs to verify your code is correct. For instance, this is how the compiler knows the expected type of the `weight` parameter. Next, the linker takes the output of the compiler and creates the final binary. Just like the compiler, the linker needs to know where to find the function you are calling. This is done with `.tbd` files, which are text based stubs informing the linker of what functions are available to be called in a framework. For our function, the relevant file is `$SDKROOT/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore.tbd`. They are text files, and opening it up in a text editor reveals lines like `_$s7SwiftUI4TextV10fontWeightyAcA4FontV0E0VSgF`. This is a mangled Swift symbol, and it demangles to `SwiftUI.Text.fontWeight(SwiftUI.Font.Weight?) -> SwiftUI.Text`, which is exactly the function we are looking for.

There is a third place the function needs to be found for everything to work - the exported symbols of the framework at runtime and can be viewed with `nm`:

```shell
nm -gU /Library/Developer/CoreSimulator/Volumes/iOS_22C5125e/Library/Developer/CoreSimulator/Profiles/Runtimes/iOS\ 18.2.simruntime/Contents/Resources/RuntimeRoot/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore | xcrun swift-demangle | grep '.fontWeight('
```

This is so dyld knows what code at runtime to execute when your app calls a function in another framework.

To summarize, calling an external function from your code means it must be defined in three places:

- A `.swiftinterface` file for the compiler to recognize it
- A `.tbd` file for the linker to recognize it
- The exported symbols of the binary at runtime for dyld to recognize it

## [System Programming Interface](https://www.emergetools.com/blog/posts/calling-hidden-swift-functions#system-programming-interface)

In addition to the regular access levels in Swift, library developers can define a System Programming Interface (SPI), which is a kind of API that only some clients can use. This is defined using the experimental attribute `@_spi(spiName)`. For example:

```swift
public class MyClass {
  public function doSomething() { ... }

  @_spi(Private)
  public function doSomethingPrivate() { ... }
}
```

Now to call `doSomethingPrivate` clients will need to use a special import syntax: `@_spi(Private) import MyModule`. SPI is implemented by producing a new *.swiftinterface file, separate from the default interface that only contains the API. Apple frameworks appear to make frequent use of this feature, because they have functions that are available at link time but not part of the API. For an in-depth look at this attribute, check out [this blog post](https://www.nutrient.io/blog/swifts-approach-to-spi/?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post).

## [How to access any SPI](https://www.emergetools.com/blog/posts/calling-hidden-swift-functions#how-to-access-any-spi)

Now that we’ve seen the public API of a framework is also in the `.tbd` file, we can use this to view what functions are available to us even if we do not have the SPI interface. For SwiftUI, we can run the entire text based stub through swift-demangle and notice some APIs that are not publicly documented, like this one:

```swift
'SwiftUI.ViewPreviewSource.makeView.modify : @Swift.MainActor () -> SwiftUI.View', 
'SwiftUI.ViewPreviewSource.makeView.getter : @Swift.MainActor () -> SwiftUI.View', 
```

So there is a type called `ViewPreviewSource` that has a `makeView` property which we can call to get a `SwiftUI.View`. This is how the `#Preview` macro works internally. Since it is still accessible by the linker, we only need it to be in a swift interface file to use it. Unfortunately, it was not included as part of the ABI, likely because it is an SPI and not in the interface files that Xcode provides. However, there is a surprisingly easy workaround for this: **We can edit the `.swiftinterface` file to add the missing APIs**. The addition to the file looks like this:

```swift
public struct ViewPreviewSource {
  public var makeView: @_Concurrency.MainActor () -> any SwiftUI.View
}
```

There’s still one catch. After modifying the interface, you can build code that references the SPI, but if you distribute that code to others they will not be able to use it. I encountered this problem when developing the preview based snapshot testing package [SnapshotPreviews](https://github.com/EmergeTools/SnapshotPreviews?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post). This Swift package needed to call the SPI to render an Xcode preview to an image, but I wanted anyone to be able to use it without making any changes to their Xcode installation. To work around this I defined a protocol that re-declared the functionality:

```swift
public protocol MakeUIViewProvider {
  var makeView: @MainActor () -> UIView { get }
}

@_spi(Private)
extension ViewPreviewSource: MakeViewProvider { }
```

Notice the use of `@_spi` again. This is so when the code is compiled that conformance is not included in the interface file. This is crucial because otherwise, users of the framework would also need to modify their interface files for the type `ViewPreviewSource` to be defined. Once this code is compiled using a version of Xcode that has the modifications, other Swift packages can import it as a dynamic framework and then cast types to `MakeUIViewProvider`. This lets the runtime (instead of the compiler) find the function that was previously only in SPI. This technique re-exports a hidden type through a runtime protocol check.

The full code for this can be found in the [SnapshotsPreviews repo](https://github.com/EmergeTools/SnapshotPreviews/tree/main/PreviewsSupport?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post). If you find any other interesting hidden APIs in Apple’s frameworks I would love to hear about them! Feel free to reach out on [X](https://x.com/sond813?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) or [Mastodon](https://mastodon.social/@sond813?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post).
