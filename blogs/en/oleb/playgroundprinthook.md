---
title: _playgroundPrintHook
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/09/playground-print-hook/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:b20d6e07a3b9a847'
translated: false
---

> 原文：[_playgroundPrintHook](https://oleb.net/blog/2016/09/playground-print-hook/)　·　Ole Begemann

# _playgroundPrintHook

One of the great things of Swift being open-source is that you can read the [source of the standard library](https://github.com/apple/swift/tree/swift-3.0-branch/stdlib/public/core). (Even better, you don’t need to know C++ to understand it.) This is great if you need an answer to a specific question, e.g. “[How are string indices implemented](https://github.com/apple/swift/blob/swift-3.0-branch/stdlib/public/core/StringCharacterView.swift#L159-L191)?” or “[What does an `EnumeratedSequence` do](https://github.com/apple/swift/blob/swift-3.0-branch/stdlib/public/core/Algorithm.swift#L130-L142)?” From time to time, you’ll also stumble across an enjoyable little hack the standard library uses internally. I want to show you one such hack here; its purpose is to allow Xcode playgrounds to capture the output of `print` in order to display it in the sidebar.

# The `print` function

Let’s take a look at the implementation of the `print` function. There are actually two overloads for `print` in the standard library: the one you probably use the most, [`print(_:separator:terminator:)`](https://developer.apple.com/reference/swift/1541053-print) (with `separator` and `terminator` being optional because they have default values), and [a variant](https://developer.apple.com/reference/swift/1641736-print) that takes an additional in-out parameter named `to:`. The implementation of the latter [looks like this](https://github.com/apple/swift/blob/swift-3.0-branch/stdlib/public/core/Print.swift#L178-L186):

```
@inline(__always)
public func print<Target : TextOutputStream>(_ items: Any..., 
  separator: String = " ", terminator: String = "\n", to output: inout Target)
{
  _print(items, separator: separator, terminator: terminator, to: &output)
}
```

The extra [in-out](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Declarations.html#//apple_ref/doc/uid/TP40014097-CH34-ID545) `to:` parameter has a generic type with a constraint to the [`TextOutputStream`](https://developer.apple.com/reference/swift/textoutputstream) protocol. Text output streams are the standard library’s abstraction for types that can receive streaming text input. [`String`](https://developer.apple.com/reference/swift/string) is the only public type in the standard library that conforms to `TextOutputStream`; Other good candidates for adding `TextOutputStream` conformance would be [`FileHandle`](https://developer.apple.com/reference/foundation/filehandle) or [`Data`](https://developer.apple.com/reference/foundation/data) from Foundation. Here’s how you would route some `print` output directly into a string:

```
var stream = ""
print("Hello World", to: &stream)
// → stream now contains "Hello World\n"
```

We can see that the implementation of `print(_:separator:terminator:to:)` simply forwards all arguments to an internal function named `_print`, which iterates over the items and writes them to the target stream. We’re not interested in this here, but you can take a look at it [in the source code](https://github.com/apple/swift/blob/swift-3.0-branch/stdlib/public/core/Print.swift#L241-L259).

# A hook for capturing stdout

Instead, let’s turn our attention to the other overload for `print`. From what we’ve seen up to this point, I’d expect the implementation for `print(_:separator:terminator:)` to be a two-liner: one line to create an output stream that represents the [standard output](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29), and one to call `_print`. It turns out it’s a little [more complicated than that](https://github.com/apple/swift/blob/swift-3.0-branch/stdlib/public/core/Print.swift#L118-L135):

```
@inline(never)
@_semantics("stdlib_binary_only")
public func print(_ items: Any..., separator: String = " ", 
  terminator: String = "\n")
{
  if let hook = _playgroundPrintHook {
    var output = _TeeStream(left: "", right: _Stdout())
    _print(items, separator: separator, terminator: terminator, to: &output)
    hook(output.left)
  }
  else {
    var output = _Stdout()
    _print(items, separator: separator, terminator: terminator, to: &output)
  }
}
```

The `else` branch of the `if let` statement does exactly what I had expected, but what’s the other branch for? It checks if a variable named `_playgroundPrintHook` is non-`nil`. A search of the standard library for this identifier brings up [the following definition](https://github.com/apple/swift/blob/swift-3.0-branch/stdlib/public/core/OutputStream.swift#L555-L556):

```
/// A hook for playgrounds to print through.
public var _playgroundPrintHook : ((String) -> Void)? = {_ in () }
```

So `_playgroundPrintHook` is a global, _public_ variable that stores an optional function `(String) -> ()`. And if this variable is non-`nil` (which it actually is by default, albeit with an empty implementation), `print` creates a special output stream of type [`_TeeStream`](https://github.com/apple/swift/blob/swift-3.0-branch/stdlib/public/core/OutputStream.swift#L558-L571) and passes this stream to `_print`. Like a [Y splitter](https://www.google.com/search?q=y+splitter+headphones&tbm=isch) for your headphones, this “T stream” duplicates a single stream, writing all the text it receives to both its outputs.

One of the outputs is [`_Stdout()`](https://github.com/apple/swift/blob/swift-3.0-branch/stdlib/public/core/OutputStream.swift#L488-L512), the standard library’s internal stdout wrapper. This guarantees that your `print` commands will still reach the standard output. The other output is an empty string that will be stored in the T stream’s `left` property. So now, everything that `_print` writes to its target stream will get written to both stdout _and_ to the string variable that’s stored in `left`. And with `hook(output.left)`, `print` then passes the captured text to the function that was assigned to `_playgroundPrintHook`, giving whoever performed this assignment a convenient way to get a copy of the output.

# Messing with Xcode

Even though the name `_playgroundPrintHook` already gave it away, we can verify that Xcode really uses this mechanism in playgrounds. Create a new playground and paste the following code:

```
print("Hello World") // Shows up in the sidebar

var printed: [String] = []
_playgroundPrintHook = { text in
    printed.append(text)
}

print("Hello") // Doesn't show up in the sidebar
print("World") // Doesn't show up in the sidebar

printed
```

You’ll see that all three `print` statements are displayed in the console as you’d expect. But only the first (before we re-assigned `_playgroundPrintHook`) also shows up in the sidebar on the right. The next two calls to `print`, after we assigned our own custom closure to `_playgroundPrintHook`, only result in empty strings in the sidebar. Finally, we can verify that our hook really gets executed by inspecting the `printed` array, which we used to capture the text in the hook closure.

![Redirecting _playgroundPrintHook in Xcode](https://oleb.net/media/xcode-playground-print-hook.png)

<sub>Customizing `_playgroundPrintHook` trips up the display of `print` statement results in the sidebar.</sub>

If you want to have your cake and eat it too, you can store the existing hook first and call it from your own hook, like this:

```
let oldHook = _playgroundPrintHook
_playgroundPrintHook = { text in
    oldHook?(text)
    printed.append(text)
}
```

# The end

Is messing with Xcode in this manner a good idea? Definitely not. Although `_playgroundPrintHook` is technically `public` (otherwise Xcode couldn’t access it, either), it’s undocumented and should be considered an implementation detail of the standard library. You should never use this in production (or even development) code.

But is it a fun way to learn a little about text output streams? Absolutely.
