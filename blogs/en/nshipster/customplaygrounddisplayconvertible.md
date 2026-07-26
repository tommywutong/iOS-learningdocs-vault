---
title: CustomPlaygroundDisplayConvertible
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/customplaygrounddisplayconvertible/'
original_language: en
published: 2018-11-12
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:0610ce952aa7152b'
translated: false
---

> 原文：[CustomPlaygroundDisplayConvertible](https://nshipster.com/customplaygrounddisplayconvertible/)　·　NSHipster (Mattt)

# [Custom​Playground​Display​Convertible](https://nshipster.com/customplaygrounddisplayconvertible/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  November 12^th, 2018

Playgrounds allow you to see what your Swift code is doing every step along the way. Each time a statement is executed, its result is logged to the sidebar along the right-hand side. From there, you can open a Quick Look preview of the result in a popover or display the result inline, directly in the code editor.

The code responsible for providing this feedback is provided by the PlaygroundLogger framework, which is part of the open source [swift-xcode-playground-support](https://github.com/apple/swift-xcode-playground-support/) project.

Reading through the code, we learn that the Playground logger distinguishes between structured values, whose state is disclosed by inspecting its internal members, and opaque values, which provide a specialized representation of itself. Beyond those two, the logger recognizes entry and exit points for scopes (control flow statements, functions, et cetera) as well as runtime errors (caused by implicitly unwrapping nil values, `fatalError()`, and the like) Anything else — imports, assignments, blank lines — are considered gaps

### Built-In Opaque Representations

The Playground logger provides built-in opaque representations for many of the types you’re likely to interact with in Foundation, UIKit, AppKit, SpriteKit, CoreGraphics, CoreImage, and the Swift standard library:

Category

Types

Result

Strings

- `String`
- `NSString`

"Hello, world!"

Attributed Strings

- `NSAttributedString`

"Hello, world!"

Numbers

- `Int`, `UInt`, …
- `Double`, `Float`, …
- `CGFloat`
- `NSNumber`

42

Ranges

- `NSRange`

{0, 10}

Boolean Values

- `Bool`

true

Pointers

- `UnsafePointer`
- `UnsafeMutablePointer`
- `UnsafeRawPointer`
- `UnsafeMutableRawPointer`

0x0123456789ABCDEF

Dates

- `Date`
- `NSDate`

Nov 12, 2018 at 10:00

URLs

- `URL`
- `NSURL`

https://nshipster.com

Colors

- `CGColor`
- `NSColor`
- `UIColor`
- `CIColor`

🔴 r 1.0 g 0.0 b 0.0 a 1.0   
 ![](https://nshipster.com/assets/playground-custom-description-color-c9dd6820a23664fbc1add7dd2576632d880df418b884390c3ac5807861bd515d89347deaaa7756e5061928a30a8ecd69a3233fe52f9d61f1ee4d763e838b45aa.png)

Geometry

- `CGPoint`
- `CGSize`
- `CGRect`

{x 0 y 0 w 100 h 100}   
 ![](https://nshipster.com/assets/playground-custom-description-geometry-3cd11a0307b2accd834e889854231f4c9a47ddde4686275472c2c18dcb4c262c4dc7eaec6e0537c00d0517b947d4a594625aa96bf3295caec5ae6cebc328eaac.png)

Bezier Paths

- `NSBezierPath`
- `UIBezierPath`

11 path elements

Images

- `CGImage`
- `NSCursor`
- `NSBitmapImageRep`
- `NSImage`
- `UIImage`

w 50 h 50

SpriteKit Nodes

- `SKShapeNode`
- `SKSpriteNode`
- `SKTexture`
- `SKTextureAtlas`

SKShapeNode

Views

- `NSView`
- `UIView`

NSView

### Structured Values

Alternatively, the Playground logger provides for values to be represented structurally — without requiring an implementation of the [`CustomReflectable` protocol](https://nshipster.com/mirror/).

This works if the value is a tuple, an enumeration case, or an instance of a class or structure. It handles aggregates, or values bridged from an Objective-C class, as well as containers, like arrays and dictionaries. If the value is an optional, the logger will implicitly unwrap its value, if present.

## Customizing How Results Are Logged In Playgrounds

Developers can customize how the Playground logger displays results by extending types to adopt the `CustomPlaygroundDisplayConvertible` protocol and implement the required `playgroundDescription` computed property.

For example, let’s say you’re using Playgrounds to familiarize yourself with the Contacts framework. _(Note: the Contacts framework is unavailable in Swift Playgrounds for iPad)_ You create a new `CNMutableContact`, set the `givenName` and `familyName` properties, and provide an array of `CNLabeledValue` values to the `emailAddresses` property:

```
import Contacts

let contact = CNMutableContact()
contact.givenName = "Johnny"
contact.familyName = "Appleseed"
contact.emailAddresses = [
    CNLabeledValue(label: CNLabelWork,
                   value: "[email protected]")
]
```

If you were hoping for feedback to validate your API usage, you’d be disappointed by what shows up in the results sidebar:

`\<CNMutableContact: 0x7ff727e38bb0: ... /\>`

To improve on this, we can extend the superclass of `CNMutableContact`, `CNContact`, and have it conform to `CustomPlaygroundDisplayConvertible`. The Contacts framework includes `CNContactFormatter`, which offers a convenient way to summarize a contact:

```
extension CNContact: CustomPlaygroundDisplayConvertible {
    public var playgroundDescription: Any {
        return CNContactFormatter.string(from: self, style: .fullName) ?? ""
    }
}
```

By putting this at the top of our Playground (or in a separate file in the Playground’s auxilliary sources), our `contact` from before now provides a much nicer Quick Look representation:

"Johnny Appleseed"

To provide a specialized Playground representation, delegate to one of the value types listed in the table above. In this case, the ContactsUI framework provides a `CNContactViewController` class whose `view` property we can use here _(annoyingly, the API is slightly different between iOS and macOS, hence the compiler directives)_:

```
import Contacts
import ContactsUI

extension CNContact: CustomPlaygroundDisplayConvertible {
    public var playgroundDescription: Any {
        let viewController: CNContactViewController
        #if os(macOS)
            viewController = CNContactViewController()
            viewController.contact = self
        #elseif os(iOS)
            viewController = CNContactViewController(for: self)
        #else
            #warning("ContactsUI unavailable")
        #endif

        return viewController.view
    }
}
```

After replacing our original `playgroundDescription` implementation, our contact displays with the following UI:

![](https://nshipster.com/assets/playground-custom-description-contact-55c05d092e1ca5312c736131e1904a6f010a23e65b1876b59f02688f67985f89f5565392ee4b92c0079c5af83068fbe9aabad154e46b61571ff28b4fcceb587f.png)

---

Playgrounds occupy an interesting space in the Xcode tooling ecosystem. It’s neither a primary debugging interface, nor a mechanism for communicating with the end user. Rather, it draws upon both low-level and user-facing functionality to provide a richer development experience. Because of this, it can be difficult to understand how Playgrounds fit in with everything else.

Here’s a run-down of some related functionality:

## Relationship to CustomStringConvertible and CustomDebugStringConvertible

The Playground logger uses the following criteria when determining how to represent a value in the results sidebar:

- If the value is a `String`, return that value
- If the value is `CustomStringConvertible` or `CustomDebugStringConvertible`, return `String(reflecting:)`
- If the value is an enumeration (as determined by `Mirror`), return `String(describing:)`
- Otherwise, return the type name, normalizing to remove the module from the fully-qualified name

Therefore, you can customize the Playground description for types by providing conformance to `CustomStringConvertible` or `CustomDebugStringConvertible`.

So the question becomes, _“How do I decide which of these protocols to adopt?”_

Here are some general guidelines:

- Use `CustomStringConvertible` (`description`) to represent values in a way that’s appropriate for users.
- Use `CustomDebugStringConvertible` (`debugDescription`) to represent values in a way that’s appropriate for developers.
- Use `CustomPlaygroundDisplayConvertible` (`playgroundDescription`) to represent values in a way that’s appropriate for developers in the context of a Playground.

Within a Playground, expressiveness is prioritized over raw execution. So we have some leeway on how much work is required to generate descriptions.

For example, the default representation of most sequences is the type name (often with cryptic generic constraints):

```
let evens = sequence(first: 0, next: {$0 + 2})
```

UnfoldSequence\<Int, (Optional, Bool)\>

Iterating a sequence has unknown performance characteristics, so it would be inappropriate to include that within a `description` or `debugDescription`. But in a Playground? Sure, _go nuts_ — by associating it in the Playground itself, there’s little risk in that code making it into production.

So back to our original example, let’s see how `CustomPlaygroundDisplayConvertible` can help us decipher our sequence:

```
extension UnfoldSequence: CustomPlaygroundDisplayConvertible
           where Element: CustomStringConvertible
{
    public var playgroundDescription: Any {
        return prefix(10).map{$0.description}
            .joined(separator: ", ") + "…"
    }
}
```

0, 2, 4, 6, 8, 10, 12, 14, 16, 18…

## Relationship to Debug Quick Look

When a Playground logs structured values, it provides an interface [similar to what you find](https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/CustomClassDisplay_in_QuickLook/CH02-std_objects_support/CH02-std_objects_support.html#//apple_ref/doc/uid/TP40014001-CH3-SW19) when running an Xcode project in debug mode.

What this means in practice is that Playgrounds can approximate a debugger interface when working with structured types.

For example, the description of a `Data` value doesn’t tell us much:

```
let data = "Hello, world!".data(using: .utf8)
```

coming from `description`

13 bytes

And for good reason! As we described in the previous section, we want to keep the implementation of `description` nice and snappy.

By contrast, the structured representation of the same data object when viewed from a Playground tells us the size and memory address — it even shows an inline byte array for up to length 64:

count 13 pointer "UnsafePointer(7FFCFB609470)" [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]

---

Playgrounds use a combination of language features and tooling to provide a real-time, interactive development environment. With the `CustomPlaygroundDisplayConvertible` protocol, you can leverage this introspection for your own types.
