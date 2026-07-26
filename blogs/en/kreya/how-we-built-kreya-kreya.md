---
title: 'How we built Kreya | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/how-we-built-kreya/'
original_language: en
published: 2021-06-22
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:feae6966f13e5a9b'
translated: false
---

> 原文：[How we built Kreya | Kreya](https://kreya.app/blog/how-we-built-kreya/)　·　Kreya Blog

In our blog, we'll try to give you insights into decisions and considerations that went into Kreya. We'll start by showing you how we started building Kreya over a year ago. Back then, the only gRPC GUI client was [BloomRPC](https://github.com/uw-labs/bloomrpc). It worked well, but we missed some crucial features like [environments](https://kreya.app/docs/environments/) or [global authentications](https://kreya.app/docs/authentication/), which made it a bit cumbersome to use. Both Postman and Insomnia, which we used for REST APIs, did not support gRPC (Insomnia has since added basic gRPC support). We decided that we should build a gRPC GUI client similar to Postman or Insomnia, which supports advanced features to make calling and testing gRPC APIs easier.

## Cross platform GUI

We mainly develop in C#, so we tried to build the first version with it. There were (and still are) not a lot of options for true cross platform GUI support with .NET, but [AvaloniaUI](https://github.com/AvaloniaUI/Avalonia) looked promising. But as we built our MVP, more and more problems emerged. AvaloniaUI didn't have support for embedded WebViews (which we need for some OpenID Connect flows). The only text editor for AvaloniaUI is [AvaloniaEdit](https://github.com/AvaloniaUI/AvaloniaEdit), which also lacked features we preferred not to implement ourselves.

We started to evaluate different kinds of cross platform GUI technologies. Electron was dismissed as an option early in the evaluation, since we didn't want to ship a whole chromium installation with each update and preferred to keep our "backend" in C#. It was at this point that we read [a blog post from Steve Sanderson about WebWindow](https://blog.stevensanderson.com/2019/11/18/2019-11-18-webwindow-a-cross-platform-webview-for-dotnet-core/), a cross platform WebView library for .NET. Intrigued by the idea, we tried different implementations, but most of them were either unstable or lacked features. We eventually settled on using a fork of [SpiderEye](https://github.com/JBildstein/SpiderEye), which allowed us to implement missing features ourselves. The nice thing about SpiderEye is that it doesn't require us to run a webserver locally. Instead, the C# "backend" can communicate with the WebView directly.

## The frontend

The only thing missing was a decision about the frontend framework used in Kreya. Since all of us are experienced in Angular, we chose to use it. We briefly considered Svelte, but the missing TypeScript support (at that time) was a deal breaker for us.

## Challenging tasks

Satisfied with our tech stack, we went ahead and implemented the necessary features for our MVP. On the way, we encountered some challenging tasks.

### Runtime (non-compiled) gRPC support in C#

Clients for gRPC APIs are usually generated from protobuf definitions, resulting in ready-to-use classes to work with. Since Kreya needs to support all possible gRPC APIs, generating and compiling gRPC clients on the fly would be pretty complicated. This is why we used "protobuf reflection". Rather than generating actual classes, we use generic messages and operate on protobuf descriptors to access the relevant data. Since both C# and gRPC are strongly typed, we had to resort to the use of reflection and [dynamic typing](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/types/using-type-dynamic) for some edge cases.

### Defining a stable storage format

From the beginning, our idea was that the synchronisation of the Kreya data would be done via external systems, for example via git. That is why we put emphasis on the fact that the Kreya project data can be synced and diffed well via git. We avoided JSON-in-JSON-strings and tried to use self explanatory field names. This should help users in case of merge conflicts.

We also spent some time considering how Kreya will look like in the future. For example, we may want to implement support for REST or GraphQL without changing our storage format.

### Cross platform CI/CD

Continuous integration and continuous deployment are key aspects of modern software development. It helps catching bugs early (in combination with automated testing) and reduces human errors in the deployment process. Our goal was to generate and publish updates with the click of a button. Since we're using Gitlab, setting up the CI/CD process was pretty easy, especially since we use it regularly in other projects. Difficulties arose mainly when we created the executables for the different OSes. The windows installer must be built and signed on Windows, while the Linux and macOS version luckily can be created on Linux.

### Integrating Monaco Editor

Integrating the [Monaco Editor](https://microsoft.github.io/monaco-editor/) as our text editor was not as straight forward as we thought it would be. Initally, the dynamic width and height of the editor created layouting problems. Later on, newer Monaco Editor versions didn't support older Safari/WebKit versions anymore, which were still used as our WebView engines. There are still [open bugs](https://github.com/riok/Kreya/issues) because of this, which we are in the process of fixing.

### OS specific features

Features that vary depending on the OS sometimes took a bit of effort to implement. For example, menus are implemented differently in all the supported platforms. Windows has a per-window menu, while macOS only has a per-application menu. On macOS, we mimic a per-window menu by updating the application menu each time a window is activated. On Linux, which supports per-window menus, keyboard shortcuts work differently from the other platforms.

Installers also vary depending on the OS. By far the easiest were the "installer" for macOS and the tarball download for Linux, followed by the support for [snapcraft](https://snapcraft.io/kreya). The windows MSI installer probably took more time to implement than the other three combined.

Of course, there were a lot more OS specific things that we implemented, but most of them were pretty straight forward, such as path handling or launching external processes. But even there we experienced some pretty interesting behaviors, which we may cover in a future blog post.

## A year later

Over a year after the first commit, we are pretty happy with our tech stack choices. We do have the occasional differences in the WebView engines (Chromium on Windows, WebKit on Linux and macOS), but they are usually easy to fix. We are able to add new features and can be relatively sure that they work on all platforms.

Overall, working on Kreya has been a pleasant experience. We recently passed one thousand Kreya installations and are excited about what the future holds.
