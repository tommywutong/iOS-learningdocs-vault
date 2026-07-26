---
title: iOS 第三方开源库的吐槽和备忘
source: ibireme (郭曜源)
source_key: ibireme
source_url: 'https://blog.ibireme.com/2013/09/23/ios-third-party-libs/'
original_language: zh
published: 2013-09-23
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:83f18e4f2b95b696'
translated: n/a
---

> 原文：[iOS 第三方开源库的吐槽和备忘](https://blog.ibireme.com/2013/09/23/ios-third-party-libs/)　·　ibireme (郭曜源)

注意：这篇文章已经过期

做iOS开发总会接触到一些第三方库，这里整理一下，做一些吐槽。

目前比较活跃的社区仍旧是Github，除此以外也有一些不错的库散落在Google Code、SourceForge等地方。由于Github社区太过主流，这里主要介绍一下Github里面流行的iOS库。

首先整理了一份[Github上排名靠前的iOS库](http://github.ibireme.com/github/list/ios/)(大概600个repos)

除了逛一下每日/每月流行之外，也可以到[这里](https://github.com/search?l=Objective-C&o=desc&q=stars%3A%3E1&s=stars&type=Repositories)来看一下整个iOS Repos的排名。

下面是一些比较流行的第三方库：

### HTTP

相比较之下,[AFNetworking](https://github.com/AFNetworking/AFNetworking)是目前最优秀的一个了：轻量、易用、使用者多、开发者有在积极维护。在AFN出现之前，这个角色是由[ASIHTTPRequest](https://github.com/pokeb/asi-http-request)扮演的，只是到现在年久失修了。关于AFN和ASI的对比，这里有一篇不错的文章[http://www.infoq.com/cn/articles/afn_vs_asi](http://www.infoq.com/cn/articles/afn_vs_asi)。除此之外，[MKNetworkKit](https://github.com/MugunthKumar/MKNetworkKit)和[RestKit](https://github.com/RestKit/RestKit)也有一定的使用者。

### Socket

[CocoaAsyncSocket](https://github.com/robbiehanson/CocoaAsyncSocket)无疑是目前封装得最完善的Socket库了：支持异步TCP/UDP，支持GCD，Objective-C接口封装。。目前没有发现可以与之相比的同类产品。。

### JSON

[JSONKit](https://github.com/johnezang/JSONKit)算是第三方中最优秀的一个了：性能很高，文件少。在JSONKit之前，[SBJson](https://github.com/stig/json-framework)非常非常流行，但是SBJson性能够差，只是由于历史原因仍然存在在某些工程里面。如果工程只需要支持iOS5以上的系统，那就可以放弃那些第三方Json库了，直接用系统提供的NSJSONSerialization，性能比第三方的好，又是官方API。。

### XMPP

现在做个实时聊天，XMPP协议算是很成熟的方案了。[XMPPFramework](https://github.com/robbiehanson/XMPPFramework)一个很不错的选择，可以直接和OpenFire服务器打交道。项目不大人手不多的话，可以看看这个。

### 基础工具类

[SSToolkit](https://github.com/soffes/sstoolkit)算是一个不错的工具包，提供各种比如编码、加密、字符串处理等等东西，还提供了一些不错的自定义控件，并且文档非常齐全。

### 框架

过去有很多人再用[three20](https://github.com/facebook/three20)，这个东西太大太重，文档又少，到头来连Facebook都停止维护了。作为替代品[nimbus](https://github.com/jverkoey/nimbus)现在流行了开来，关键在于它文档齐全。。国内有个MVC框架叫[BeeFramework](https://github.com/gavinkwoe/BeeFramework)，号称是顶级框架并且功能超过nimbus，有兴趣的可以看一下。。 [ReactiveCocoa](https://github.com/ReactiveCocoa/ReactiveCocoa)把响应式编程这种上流的东西带了过来，值得试一试。。

### 数据存储

还是挺多人(比如我)喜欢直接跟SQLite打交道的，这方面[fmdb](https://github.com/ccgus/fmdb)封装的很不错。如果用CoreData来做存储的，可以用一下[MagicalRecord](https://github.com/magicalpanda/MagicalRecord)。

### 图像处理

[GPUImage](https://github.com/BradLarson/GPUImage)无疑是这方面的集大成者了。。用OpenGL ES2.0来实时处理图片和视频流，性能和功能都是顶尖的。

### 开发和调试工具

[PonyDebugger](https://github.com/square/PonyDebugger)看上去是一个不错的调试工具，可以在电脑浏览器上远程调试iOS程序、查看试图层次、网络等等。[CocoaLumberjack](https://github.com/robbiehanson/CocoaLumberjack)是个Log工具，号称是可以提供企业级Log，使用者也挺多。

---

---

为了了解一下目前第三方库的普及程度，下面列举一些知名App对第三方库的依赖。

**网易新闻**  
 [AppleReachability](https://developer.apple.com/library/ios/samplecode/reachability/Introduction/Intro.html)  
 [ASIHTTPRequest](https://github.com/pokeb/asi-http-request)  
 [EGOTableViewPullRefresh](https://github.com/enormego/EGOTableViewPullRefresh)  
 [GTMNSString+HTML](https://code.google.com/p/google-toolbox-for-mac/)  
 [MGTemplateEngine](https://github.com/nxtbgthng/MGTemplateEngine)  
 [MPOAuth](https://github.com/thekarladam/MPOAuth)  
 [RegexKitLite](http://regexkit.sourceforge.net/RegexKitLite)  
 [SDWebImage](https://github.com/rs/SDWebImage)  
 [SSZipArchive](https://github.com/soffes/ssziparchive)  
 [wax](https://github.com/probablycorey/wax)

**Garageband**  
 [MurmurHash](https://sites.google.com/site/murmurhash/)  
 [libpng](http://www.libpng.org/pub/png/libpng.html‎)  
 [zlib](http://www.zlib.net/)  
 [SBJson](https://github.com/stig/json-framework) (json-framework)

**iWork三套件**  
 [MOKit](http://mokit.sourceforge.net)  
 [Boost C++ Library](http://www.boost.org/‎)  
 [protobuf](http://code.google.com/p/protobuf/‎)  
 [OpenGL Mathematics](http://glm.g-truc.net/)  
 [SQLite](http://www.sqlite.org)  
 [cephes math library](http://www.boutell.com/lsm/lsmbyid.cgi/000626)

**Pinterest**  
 [AFNetworking](https://github.com/AFNetworking/AFNetworking)  
 [AFHttpClientLogger](https://github.com/jparise/AFHTTPClientLogger)  
 [Facebook SDK](https://github.com/facebook/facebook-ios-sdk)  
 [iRate](https://github.com/nicklockwood/iRate)  
 [MAKVONotificationCenter](https://github.com/mikeash/MAKVONotificationCenter)  
 [SDWebImage](https://github.com/rs/SDWebImage)  
 [SFHFKeychainUtils](https://github.com/ldandersen/scifihifi-iphone)  
 [SSPullToRefresh](https://github.com/soffes/sspulltorefresh)  
 [SVProgressHUD](https://github.com/samvermette/SVProgressHUD)  
 [TTTAttributedLabel](https://github.com/mattt/TTTAttributedLabel)  
 [TTTLocalizedPluralString](https://github.com/mattt/TTTLocalizedPluralString)  
 [UIAlertView-Blocks](https://github.com/jivadevoe/UIAlertView-Blocks)

**多看阅读**  
 [fmdb](https://github.com/ccgus/fmdb)  
 [ASIHTTPRequest](https://github.com/pokeb/asi-http-request)  
 [FreeType](http://www.freetype.org/)  
 [JSONKit](https://github.com/johnezang/JSONKit)  
 [Objective-Zip](https://github.com/flyingdolphinstudio/Objective-Zip)  
 [Skia](https://code.google.com/p/skia/) (Google)  
 [MBProgressHUD](https://github.com/jdg/MBProgressHUD)

**淘宝**  
 [MAZeroingWeakRef](https://github.com/mikeash/MAZeroingWeakRef)  
 [MBProgressHUD](https://github.com/jdg/MBProgressHUD)  
 [ABContactHelper](https://github.com/erica/ABContactHelper)  
 [ASIHTTPRequest](https://github.com/pokeb/asi-http-request)  
 [CocoaLumberjack](https://github.com/robbiehanson/CocoaLumberjack)  
 [EGOTableViewPullRefresh](https://github.com/enormego/EGOTableViewPullRefresh)  
 [fmdb](https://github.com/ccgus/fmdb)  
 [GTMBase64](https://code.google.com/p/google-toolbox-for-mac/)  
 [JSONKit](https://github.com/johnezang/JSONKit)  
 [SBJson](https://github.com/stig/json-framework)(json-framework)  
 [RTLabel](https://github.com/honcheng/RTLabel)  
 [SDWebImage](https://github.com/rs/SDWebImage)  
 [SVPullToRefresh](https://github.com/samvermette/SVPullToRefresh)  
 [three20](https://github.com/facebook/three20)  
 [ziparchive](http://code.google.com/p/ziparchive/‎)  
 **微信**  
 [cocos2d](https://github.com/cocos2d/cocos2d-iphone)  
 [EGOTableViewPullRefresh](https://github.com/enormego/EGOTableViewPullRefresh)  
 [Facebook iOS SDK](https://github.com/facebook/facebook-ios-sdk)  
 [JSONKit](https://github.com/johnezang/JSONKit)  
 [SBJson](https://github.com/stig/json-framework)  
 [ziparchive](http://code.google.com/p/ziparchive/‎)

**QQ**  
 [ASIHTTPRequest](https://github.com/pokeb/asi-http-request)  
 [FMDB](https://github.com/ccgus/fmdb)  
 [CocoaAsyncSocket](https://github.com/robbiehanson/CocoaAsyncSocket)  
 [JSONKit](https://github.com/johnezang/JSONKit)  
 [MBProgressHUD](https://github.com/jdg/MBProgressHUD)  
 [OpenUDID](https://github.com/ylechelle/OpenUDID)  
 [SBJson](https://github.com/stig/json-framework)  
 [SVPullToRefresh](https://github.com/samvermette/SVPullToRefresh)

**百度地图**  
 [AFNetworking](https://github.com/AFNetworking/AFNetworking)  
 [GTMBase64](https://code.google.com/p/google-toolbox-for-mac/)  
 [JSONKit](https://github.com/johnezang/JSONKit)  
 [MBProgressHUD](https://github.com/jdg/MBProgressHUD)  
 [RNCachingURLProtocol](https://github.com/rnapier/RNCachingURLProtocol)  
 [SDWebImage](https://github.com/rs/SDWebImage)

**微博**  
 [ABContactHelper](https://github.com/erica/ABContactHelper)  
 [AFNetworking](https://github.com/AFNetworking/AFNetworking)  
 [ASIHTTPRequest](https://github.com/pokeb/asi-http-request)  
 [DACircularProgressView](https://github.com/danielamitay/DACircularProgress)  
 [DDProgressView](https://github.com/ddeville/DDProgressView)  
 [DTFoundation](https://github.com/Cocoanetics/DTFoundation)  
 [fmdb](https://github.com/ccgus/fmdb)  
 [JSONKit](https://github.com/johnezang/JSONKit)  
 [SBJson](https://github.com/stig/json-framework)  
 [MBProgressHUD](https://github.com/jdg/MBProgressHUD)  
 [MTStatusBarOverlay](https://github.com/myell0w/MTStatusBarOverlay)  
 [OpenUDID](https://github.com/ylechelle/OpenUDID)  
 [SFHFKeychainUtils](https://github.com/ldandersen/scifihifi-iphone)

**人人**  
 [cocoaasyncsocket](https://github.com/robbiehanson/CocoaAsyncSocket)  
 [ZipArchive](http://code.google.com/p/ziparchive/‎)  
 [MBProgressHUD](https://github.com/jdg/MBProgressHUD)  
 [JSONKit](https://github.com/johnezang/JSONKit)  
 [GTMBase64](https://code.google.com/p/google-toolbox-for-mac/)  
 [MKNetworkKit](https://github.com/MugunthKumar/MKNetworkKit)  
 [HPGrowingTextView](https://github.com/HansPinckaers/GrowingTextView)  
 [zxing](https://code.google.com/p/zxing/)  
 可以看到，这些大型的App的依赖都很混乱，所以稍微解释一下。这些大公司都有一个iOS团队来协同开发，团队成员的水平也参差不齐。有时由于历史原因，例如某个App的某个组件依赖了ASIHttpRequest，但之后的新人改用了AFNetworking，就造成上面这种比较混乱的库依赖关系。这就造成难以维护、代码冗余等问题了。所以，引入一个第三方库一定要慎重考虑，如果可能，尽量自己开发和实现相应的功能，第三方库尽量只作为参考。 小团队或者个人开发者可以不必过多考虑，开发速度优先。

---

---

最后吐槽一下cocoapods。  
 一个语言的流行总伴随着第三方库的丰富，相应的也会出现依赖库管理的工具。cocoapods之于ObjC,就像maven/gradle 之于java、gem之于ruby那样。 cocoapods基本上是创建在在github社区上的，开源并且社区活跃。除了用github上的中央仓库外，也可以自己搭建私服什么的随便乱搞。  
 但就我来说，不推荐使用cocoapods，吐槽如下：

1. 像maven这样的工具，是为了管理庞大的第三方库依赖、控制版本、构建工程等等而产生的，很难想象一个依赖了上百个jar包的web项目不用包管理构建会变成什么样。。但是，iOS开发是客户端的开发啊，如果真有一个工程依赖了那么多第三方工具，这个App能保持稳定吗。。通常情况下一个iOS工程不会有那么多包依赖。
2. 按常理来看，一个人的手头不可能有太多的工程同时进行，也不太可能一天之内创建N个App来发布。cocoapods能节省的重复工作量，还不如它带来麻烦多。。
3. 修改和调试不便。如果某个第三方库需要少量修改才能实现需求，用cocoapods来处理会比较麻烦。

关于第三方库，同样也不推荐过多使用，吐槽如下：

1. 消耗时间，一个开源库，拿过来需要仔细考察代码质量，确认是否足够可靠。如果出现问题，需要仔细审查开源库的内部实现。如果这些工作太消耗时间，还不如自己实现。
2. 可维护性差。一旦遇到系统升级、API更换，第三方库不能确保不出问题。当出问题后也难以找到人来维护。如果跟进第三方库的改变，仍然容易出现新问题。
3. 法律问题。。大公司需要仔细审查许可协议，小公司各种不怕那就没问题。。

Update: 两年多过去了，这篇文章已经过时了嗯。。另外我现觉得 CocoaPods/Carthage 很不错。
