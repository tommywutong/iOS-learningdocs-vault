---
title: Language Server Protocol
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/language-server-protocol/'
original_language: en
published: 2018-11-05
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:8aa9167314a3f666'
translated: false
---

> 原文：[Language Server Protocol](https://nshipster.com/language-server-protocol/)　·　NSHipster (Mattt)

# [Language Server Protocol](https://nshipster.com/language-server-protocol/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  May 7^th, 2020 ([revised](https://github.com/nshipster/articles/commits/master/2018-11-05-language-server-protocol.md))

In October 2018, Apple [announced on the Swift.org forums](https://forums.swift.org/t/new-lsp-language-service-supporting-swift-and-c-family-languages-for-any-editor-and-platform/17024) that it was starting work to adopt the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (LSP) for Swift and C languages.

> At Apple we are making it a priority to support high-quality tooling for all Swift developers, including those working on non-Apple platforms. We want to collaborate with the open-source community and focus our efforts on building common infrastructure that can be shared by Xcode and other editors and platforms. To that end, [ … ] we’ve chosen to adopt LSP.
> 
> Argyrios Kyrtzidis, October 15^th, 2018

**This is arguably the most important decision Apple has made for Swift since releasing the language as open source in 2014.** It’s a big deal for app developers, and it’s an even bigger deal for Swift developers on other platforms.

To understand why, this week’s article will take a look at what problem the Language Server Protocol solves, how it works, and what its long-term impacts may be.

---

Imagine a grid with each row representing a different programming language (Swift, JavaScript, Ruby, Python, etc.) and each column representing a different code editor (Xcode, Visual Studio, Vim, Atom, etc.), such that each cell represents the level of support that a particular editor has for a language.

![](https://nshipster.com/assets/lsp-languages-times-editors-e30cf1a62ea5dbad8145723e17e8a17716f325e58fa543c559c5e6d8c25487dd56a1f8a0e0a67299c6927fb4f097dc0f8f803aa90891454f8e9aa1a92386f992.svg)

Up until recently, what you’d find was a patchwork of compatibility across the various combinations. Some editors offered deep integration with a few languages and little to no support for anything else, whereas other editors aimed to be general-purpose with at least a modicum of support for many languages. (The term IDE is often used to describe the former.)

Case in point: _You’d be stubborn not to use Xcode for app development and foolish to use it for anything else._

For an editor to have better support for a particular language, it needs to write integration code — either directly in the code base or via a plugin system. Due to implementation differences across languages and editors, improvements to, say, Ruby support in Vim wouldn’t translate into better support for Python, nor could they be applied to make Ruby work better in Atom. The end result: inconsistent support across technologies and a lot of wasted effort.

The situation we described is often referred to as an M × N problem, where the number of integrations is the _product_ of `M` editors and `N` languages. What the Language Server Protocol does is change this M × N problem into a M + N problem.

Rather than an editor having to implement support for each language, it only needs to support the LSP. And in doing so, it gets the same level of functionality for all languages that support the LSP.

![](https://nshipster.com/assets/lsp-languages-plus-editors-0bfe50ed918be033d10d4837c90d2f697a56395950188acbdccdde68f42d67f126828a695fce31b50f41fb92ddbd991422f93bee447e97c5f9214531c2e78089.svg)

Language Server Protocol provides a common set of functionality for supported languages, including:

- Syntax Highlighting
- Automatic Formatting
- Autocomplete
- Syntax
- Tooltips
- Inline Diagnostics
- Jump to Definition
- Find References in Project
- Advanced Text and Symbol Search

Rather than reinventing the wheel for each new technology, tools and editors can invest in better usability and more advanced functionality.

## How Language Server Protocol Works

If you’re an iOS developer, you may be most familiar with the terms server and protocol in the sense of communicating with web applications in JSON format via HTTP. This actually isn’t too far off from how the Language Server Protocol works.

In the case of LSP, the _client_ refers to the editor — or more generally, the tool — and the _server_ refers to an external program run locally in a separate process.

As for the _protocol_ itself, LSP resembles a simplified version of HTTP:

- Each message consists of a header part and a content part.
- The header part has a required `Content-Length` field containing the size of the content part in bytes, and an optional `Content-Type` field (`application/vscode-jsonrpc; charset=utf-8` by default)
- The content part uses [JSON-RPC](https://www.jsonrpc.org/specification) to describe the structure of requests, responses, and notifications.

Whenever something happens in the tool, such as the user jumping to the definition of a symbol, the tool sends a request to the server. The server receives that request and then returns an appropriate response.

For example, imagine that a user opens the following Swift code in an Xcode-like editor that supported the Language Server Protocol:

```
class Parent {}
class Child: Parent {}
```

When the user ⌘-clicks the symbol `Parent` in the inheritance clause on line 2, the editor jumps to the definition of the `Parent` class on line 1.

![](https://nshipster.com/assets/lsp-jump-to-definition-82b4d11d43842656e4143254034bcb34d0d06645c826b5da833b3091ee7c985d430af313ead57060ddf3a0c27a425055dca926d27040d473d6cb2f8a7a80ee9b.gif)

Here’s how LSP enables this interaction behind the scenes:

First, when the user opens the Swift code, the editor launches its Swift language server in a separate process, if it isn’t running already, and performs any additional setup.

When the user executes the “jump to definition” command, the editor sends the following request to its Swift language server:

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/definition",
  "params": {
    "textDocument": {
      "uri": "file:///Users/NSHipster/Example.swift"
    },
    "position": {
      "line": 1,
      "character": 13
    }
  }
}
```

Upon receiving this request, the Swift language server uses a compiler tool like [SourceKit](https://github.com/apple/swift/tree/master/tools/SourceKit) to identify the corresponding code entity and find the location of its declaration on the preceding line. The language server then responds with the following message:

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "uri": "file:///Users/NSHipster/Example.swift",
    "range": {
      "start": {
        "line": 0,
        "character": 6
      },
      "end": {
        "line": 0,
        "character": 12
      }
    }
  }
}
```

Finally, the editor navigates to the file (which, in this case, is already open), moves the cursor to that range, and highlights the token.

The beauty of this approach is that the editor did all of this without knowing anything about the Swift programming language other than that `.swift` files are associated with Swift code. All the editor needs to do is talk to the language server and update the UI. And knowing how to do that, the editor can follow the same procedure to facilitate this interaction for code written in any language with a language server implementation.

## Language Server Protocol Support in Clang / LLVM

If the _M + N_ diagram from before looks familiar, it might be because it’s the same approach taken by LLVM.

At the core of LLVM is an intermediate representation (IR). Supported languages generate IR using a compiler frontend, and that IR can generate machine code for any platform supported by a compiler backend.

![](https://nshipster.com/assets/lsp-llvm-ir-51a7a3a7bdebecfd02ac7c2b25172b91005e9779b458f2d01f48b30859ef20bc83b90ec9fbfb0c048714b40bdab6a47d5ef0bc08e9fe4681f92e0038990f81c0.svg)

The LLVM compiler frontend for C languages is called [Clang](https://clang.llvm.org). It’s also used by Swift for inter-operability with Objective-C. In its recent 5.0.0 release, Clang added a new tool called [Clangd](https://clang.llvm.org/extra/clangd.html), LLVM’s implementation for the Language Server Protocol.

In April 2018, [Apple announced to the LLVM mailing list](http://lists.llvm.org/pipermail/cfe-dev/2018-April/057668.html) that it was switching the focus of its development efforts from [libclang](https://clang.llvm.org/doxygen/group__CINDEX.html) to Clangd as the primary way to create interactive tooling.

Now you might think, _“So what?”_ Apple is among the most prominent supporters of the LLVM project — having, among other things, employed the project’s founder, Chris Lattner, for over a decade. Apple’s decision to switch from one obscure Clang tool to another would seem to be an implementation detail (so to speak).

What makes this announcement quite interesting is that Clangd appears to have been created entirely outside of Apple, with significant contributions from Google and other companies. This announcement signals a significant shift in the direction of tooling development going forward — something that would be confirmed 6 months later on the Swift.org forums.

## Getting Started with Language Server Protocol

Xcode 11.4 includes `sourcekit-lsp` in its default toolchain. You can use the `xcrun` command to get the path to the language server executable:

```
$ xcrun -f sourcekit-lsp
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/sourcekit-lsp
```

Check out [our article about Visual Studio Code](https://nshipster.com/vscode/) to get started with our go-to editors. Beyond that, the sourcekit-lsp project on GitHub has [instructions for integrating with Sublime Text, Vim, Emacs, and others.](https://github.com/NSHipster/sourcekit-lsp/tree/master/Editors#editor-integration).

## Potential Consequences of Apple’s Support of Language Server Protocol

It’ll take some time to feel the full impact of these developments, but believe me: your patience will be rewarded. Here are just a few of what I believe will happen as a result of LSP in the coming months and years.

### Swift Becomes More Appealing as a General-Purpose Programming Language

Although Swift is used primarily for app development, it was designed from the start to be a capable general-purpose programming language. Between [Swift for TensorFlow](https://www.tensorflow.org/swift/), [SwiftNIO](https://github.com/apple/swift-nio), and other projects, we’re just starting to see the promise of what Swift can do beyond the App Store.

Among the biggest factors holding Swift back from mainstream adoption up to this point has been its reliance on Xcode.

It’s a lot to ask, say, a web developer or machine learning engineer to download Xcode just to try Swift when there are so many great alternatives with a much lower barrier to entry. Support for the Language Server Protocol should make it significantly easier for folks outside the Apple ecosystem to evaluate Swift with the same, familiar tools they use for everything else.

### Xcode Gets Better

Adopting LSP isn’t just about making Swift work better in other editors; Xcode stands to benefit immensely, as well.

Consider [this forum post](https://forums.swift.org/t/new-lsp-language-service-supporting-swift-and-c-family-languages-for-any-editor-and-platform/17024/29) from Project Lead for Swift at Apple, Ted Kremenek:

> The LSP service [Argyrios] is describing will be functionally more powerful than SourceKit is today.

LSP is an opportunity for the Xcode team to take a fresh approach to Swift integration, and to capitalize on all of the improvements to the language and tooling in the four years since its 1.0 release.

Our first glimpse into this overhauled infrastructure comes by way of [IndexStoreDB](https://github.com/apple/indexstore-db): a powerful new API for querying code symbols in Swift projects from a [Clang index](https://docs.google.com/document/d/1cH2sTpgSnJZCkZtJl1aY-rzy4uGPcrI-6RrUpdATO2Q/).

### Xcode (Eventually) Becomes More Capable

The benefit of LSP isn’t limited to Swift and Objective-C; [from another post by Argyrios in that thread](https://forums.swift.org/t/new-lsp-language-service-supporting-swift-and-c-family-languages-for-any-editor-and-platform/17024/33):

> Getting Xcode to use our new LSP service should make it viable to use other LSP services as well, and it’s something that we are interested in, but we don’t have specific plans to announce at this moment.

The main focus for the current efforts are to improve the story for Swift. But once that’s done, it should be relatively straightforward to have those benefits cascade down to other languages with LSP support.

---

The architecture of software reflects the structure and values of the organizations that create it. The converse is true as well, to some extent.

By adopting the open Language Server Protocol standard for Xcode, Apple is making good on its commitment to the success of Swift on platforms outside the Apple ecosystem. And I think it’ll work: tooling (or lack thereof) is often the key decider in which technologies gain mindshare. But perhaps more importantly, I believe this decision demonstrates an increased willingness within (at least some small part of) the company for collaboration and transparency.
