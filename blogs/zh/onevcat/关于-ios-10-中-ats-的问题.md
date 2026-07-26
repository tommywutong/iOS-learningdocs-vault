---
title: 关于 iOS 10 中 ATS 的问题
source: onevcat (王巍/喵神)
source_key: onevcat
source_url: 'https://onevcat.com/2016/06/ios-10-ats/'
original_language: zh
published: 2016-06-17
status: active
license: CC BY 4.0（页脚明示）→ 可公开，须署名并保留原文链接
archived_at: 2026-07-27
content_hash: 'sha256:f2378b28280adb9c'
translated: n/a
---

> 原文：[关于 iOS 10 中 ATS 的问题](https://onevcat.com/2016/06/ios-10-ats/)　·　onevcat (王巍/喵神)

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 )

> 本文于 2016 年 11 月 28 日按照 Apple 最新的文档和 Xcode 8 中的表现进行了部分更新。

WWDC 15 提出的 ATS (App Transport Security) 是 Apple 在推进网络通讯安全的一个重要方式。在 iOS 9 和 OS X 10.11 中，默认情况下非 HTTPS 的网络访问是被禁止的。当然，因为这样的推进影响面非常广，作为缓冲，我们可以在 Info.plist 中添加 `NSAppTransportSecurity` 字典并且将 `NSAllowsArbitraryLoads` 设置为 `YES` 来禁用 ATS。相信大家都已经对这个非常熟悉了，因为我自己也维护了一些网络相关的框架，所以我还自己准备了一个[小脚本](https://gist.github.com/onevcat/b4604aecb4ce55651a4a)来快速关闭 ATS。

不过，WWDC 16 中，Apple 表示将继续在 iOS 10 和 macOS 10.12 里收紧对普通 HTTP 的访问限制。从 2017 年 1 月 1 日起，所有的新提交 app 默认是不允许使用 `NSAllowsArbitraryLoads` 来绕过 ATS 限制的，也就是说，我们最好保证 app 的所有网络请求都是 HTTPS 加密的，否则可能会在应用审核时遇到麻烦。

现在 (2016-11-28)，这方面的相关规定和几个事实如下：

1. TLS

  v1.2 以上，AES-128 和 SHA-2 以及 ECDHC 等) 的 HTTPS 内容。这对所有的网络请求都有效，包括

  ，通过 AVFoundation 访问的流媒体，

  以及

  等。
2. 为

  来全面禁用 ATS，不过如果你这么做的话，需要在提交 app 时进行说明，为什么需要访问非 HTTPS 内容。一般来说，可能简单粗暴地开启这个选项，而又无法找到正当理由的 app 会难以通过审核。
3. 将全部 HTTP 内容开放，选择使用

  来针对特定的域名，通过设定该域名下的

  来开放 HTTP 应该要相对容易过审核。“需要访问的域名是第三方服务器，他们没有进行 HTTPS 对应”会是审核时的一个可选理由，但是这应该只需要针对特定域名，而非全面开放。如果访问的是自己的服务器的话，可能这个理由会无法通过。
4. 和

  键。通过将它们设置为

  ，可以让你的 app 中的

  、

  或者使用

  播放的在线视频不受 ATS 的限制。虽然依然需要在审核时进行说明，但这也应该是绝大多数使用了相关特性的 app 的首选。坏消息是这个键在 iOS 9 中并不会起作用。

总结一下就是以下两点：

1. 中进行添加。
2. 或/和

  ，并且将组件换成

  或

  ，以及

  中的 player 就可以了。如果你还需要支持 iOS 9，并且需要访问网页和视频的话，可能只能去开启

  然后提交时进行说明，并且看 Apple 审核员的脸色决定让不让通过了。除了

  以外，另外一个访问网页的选择是使用

  。因为其实

  就是一个独立于 app 的 Safari 进程，所以它完全不受 ATS 的限制。
3. ，而不必担心 SSL 连接的问题。

另外，当 `NSAllowsArbitraryLoads` 和 `NSAllowsArbitraryLoadsInWebContent` 或 `NSAllowsArbitraryLoadsForMedia` 同时存在时，根据系统不同，表现的行为也会不一样。简单说，iOS 9 只看 `NSAllowsArbitraryLoads`，而 iOS 10 会优先看 `InWebContent` 和 `ForMedia` 的部分。在 iOS 10 中，要是后两者存在的话，在相关部分就会忽略掉 `NSAllowsArbitraryLoads`；如果不存在，则遵循 `NSAllowsArbitraryLoads` 的设定。说起来可能有点复杂，我在这里总结了一下根据 `NSAppTransportSecurity` 中设定条件不同，所对应的系统版本和请求组件的行为的不同，可以作为你设置这个字典时的参考 (表中使用了 `NSAllowsArbitraryLoadsInWebContent` 作为例子，`NSAllowsArbitraryLoadsForMedia` 也同理)：

| ATS 设定 | 使用的组件 | iOS 9 HTTP | iOS 10 HTTP | 备注 |
|---|---|---|---|---|
| NSAllowsArbitraryLoads: NO | WebView | ❌ | ❌ | 默认行为 |
|  | URLSession | ❌ | ❌ |  |
| NSAllowsArbitraryLoads: YES | WebView | ✅ | ✅ | 彻底禁用 ATS |
|  | URLSession | ✅ | ✅ | 审核时需要说明理由 |
| NSAllowsArbitraryLoads: NO & NSAllowsArbitraryLoadsInWebContent: YES | WebView | ❌ | ✅ | 只对网页内容禁用 ATS |
|  | URLSession | ❌ | ❌ | 保证 API 的安全性 |
| NSAllowsArbitraryLoads: NO & NSAllowsArbitraryLoadsInWebContent: NO | WebView | ❌ | ❌ |  |
|  | URLSession | ❌ | ❌ |  |
| NSAllowsArbitraryLoads: YES & NSAllowsArbitraryLoadsInWebContent: NO | WebView | ✅ | ❌ | 对于 iOS 10，NSAllowsArbitraryLoadsInWebContent 存在时忽略 NSAllowsArbitraryLoads 的设置 |
|  | URLSession | ✅ | ❌ | iOS 9 将继续使用 NSAllowsArbitraryLoads |
| NSAllowsArbitraryLoads: YES & NSAllowsArbitraryLoadsInWebContent: YES | WebView | ✅ | ✅ | 对于 iOS 10，NSAllowsArbitraryLoadsInWebContent 存在时忽略 NSAllowsArbitraryLoads 的设置 |
|  | URLSession | ✅ | ❌ | iOS 9 将继续使用 NSAllowsArbitraryLoads |

> 该列表是根据 Apple prerelease 的[文档](https://developer.apple.com/library/prerelease/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html)中关于 `NSAppTransportSecurity` 和 `NSAllowsArbitraryLoadsInWebContent` 部分的描述作出的。如果您发现这个行为发生了变化，或者上面的列表存在问题，欢迎留言，我会进行更正。

作为参考，这里将有效的 `NSAppTransportSecurity` 字典结构也一并附上：

```js
NSAppTransportSecurity : Dictionary {
    NSAllowsArbitraryLoads : Boolean
    NSAllowsArbitraryLoadsForMedia : Boolean
    NSAllowsArbitraryLoadsInWebContent : Boolean
    NSAllowsLocalNetworking : Boolean
    NSExceptionDomains : Dictionary {
        <domain-name-string> : Dictionary {
            NSIncludesSubdomains : Boolean
            NSExceptionAllowsInsecureHTTPLoads : Boolean
            NSExceptionMinimumTLSVersion : String
            NSExceptionRequiresForwardSecrecy : Boolean   // Default value is YES
            NSRequiresCertificateTransparency : Boolean
        }
    }
}
```

不得不说，Apple 使用自己现在的强势地位，在推动技术进步上的做的努力是有目共睹的。不论是前几天强制支持 IPv6，还是现在的 HTTPS，其实都不是很容易就能作出的决定。而为用户构建一个更安全的使用环境，可能不仅是 Apple 单方面可以做的，也是需要开发者来配合的一件事情。尽快适配更进步和安全的使用方式，会是一件双赢的事情。
