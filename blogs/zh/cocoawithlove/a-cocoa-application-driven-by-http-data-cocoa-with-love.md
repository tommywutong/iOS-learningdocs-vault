---
title: '由 HTTP 数据驱动的 Cocoa App | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/09/cocoa-application-driven-by-http-data.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:c57642c520fdb90c'
translated: true
---

> 原文：[A Cocoa application driven by HTTP data | Cocoa with Love](https://www.cocoawithlove.com/2008/09/cocoa-application-driven-by-http-data.html)　·　Cocoa with Love (Matt Gallagher)

这是一个小巧的 App，它通过 HTTP 查询网页，解析和搜索响应，并将结果以整齐的格式呈现于窗口中。本质上，这正是许多 Dashboard 小组件（widget）和 iPhone App 所做的，但我会向你展示如何在普通的 Cocoa App 中实现它。

由 [FuelView](https://itunes.apple.com/au/app/fuelview/id290932924?mt=8) 赞助，这是我为获取西澳大利亚州 FuelWatch 信息而编写的一个 iPhone App。

## 引言

大多数 Dashboard 小组件的工作原理都是通过 HTTP 获取数据，然后将响应格式化以便于查看。这类小组件所做的工作，你的网页浏览器都能胜任，但由于它专注于特定的目标，因此速度更快，并在其更狭窄的范围内提供更好的体验。

## 类似但以 Cocoa 实现

这种获取/解析/搜索/呈现的行为无需局限于小组件。我会向你展示如何在 Cocoa App 中复现这一过程。我将演示的示例会显示 Apple Store 中的「新品上架」项目。

以下是此应用运行时的截图：

![](https://www.cocoawithlove.com/assets/objc-era/newtothestore.png)

应用窗口中呈现的数据来源于 [http://store.apple.com](http://store.apple.com) 网页上的「新品上架」项目列表，如下方截图中圈出的部分所示：

![](https://www.cocoawithlove.com/assets/objc-era/storewebpage.png)

## 涉及的步骤

正如我已经提到的，这种类型的网络检索应用需要以下步骤：

- 通过 HTTP 获取
- 将响应解析为结构化格式
- 搜索解析后的响应并提取所需信息
- 格式化并呈现给用户

## 通过 HTTP 获取

在 Cocoa 中，NSURLConnection 负责处理 HTTP 上的数据传输。你只需提供一个要获取的 URL，它就会完成工作。

你可以使用 `sendSynchronousRequest:returningResponse:error:` 同步驱动 NSURLConnection（这无疑比我即将展示的代码量更少），但这会阻塞整个线程，直到收到响应为止（这几乎总是一个坏主意）。

对于一个拥有名为 `responseData` 的 NSMutableData 成员和名为 `baseURL` 的 NSURL 成员的类，下面展示了如何以异步方式将 http://store.apple.com 的页面获取到该 data 成员中：

```objc
    responseData = [[NSMutableData data] retain];
    baseURL = [[NSURL URLWithString:@"http://store.apple.com"] retain];

    NSURLRequest *request =
        [NSURLRequest requestWithURL:[NSURL URLWithString:@"http://store.apple.com"]];
    [[[NSURLConnection alloc] initWithRequest:request delegate:self] autorelease];
```

为了使这种异步方法能够工作，委托（delegate）对象（本例中为 `self`）还必须实现以下方法：

```objc
- (void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response
{
    [responseData setLength:0];
}

- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data
{
    [responseData appendData:data];
}

- (void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error
{
    [[NSAlert alertWithError:error] runModal];
}

- (void)connectionDidFinishLoading:(NSURLConnection *)connection
{
    // 一旦调用此方法，"responseData" 就会包含完整的结果
}
```

除了这个必需的 NSURLConnection 功能外，示例 App 还在此处实现了另一个方法来跟踪最终的 URL（因为可能会发生重定向）。

```objc
- (NSURLRequest *)connection:(NSURLConnection *)connection
    willSendRequest:(NSURLRequest *)request
    redirectResponse:(NSURLResponse *)redirectResponse
{
    [baseURL autorelease];
    baseURL = [[request URL] retain];
    return request;
}
```

拥有正确的网页基本 URL 将允许我们在需要时执行相对 URL 到绝对 URL 的转换。

## 解析和搜索 HTML 文档

HTTP 请求的响应通常是 HTML——一大段文本。为了从中提取有用的信息，你需要使用合适的工具。

有很多例子使用文本搜索和正则表达式在网页中查找数据。这些做法都是错误的。

NSXMLDocument 和 XPath 查询是你的好帮手。它们能非常轻松地在网页、RSS 源或 XML 文档中找到元素。

以下代码插入到前面展示的 `connectionDidFinishLoading:` 方法体中：

```objc
    NSError *error;
    NSXMLDocument *document =
        [[NSXMLDocument alloc] initWithData:responseData options:NSXMLDocumentTidyHTML error:&error];
    
    // 故意忽略错误：对于大多数 HTML 而言，
    // 它会被大量的 "tidy" 警告填满。
    
    NSXMLElement *rootNode = [document rootElement];
    
    NSString *xpathQueryString =
        @"//div[@id='newtothestore']/div[@class='modulecontent']/div[@id='new-to-store']/div[@class='list_content']/ul/li/a";
    NSArray *newItemsNodes = [rootNode nodesForXPath:xpathQueryString error:&error];
    if (error)
    {
        [[NSAlert alertWithError:error] runModal];
        return;
    }
```

XPath 查询是搜索操作的核心。它简单而又极其擅长从结构化文档中提取数据。

此处的查询查找了 "newtothestore" div 下列表中的所有 "a" 标签（HTML 链接）。

## 格式化并呈现给用户

在示例 App 中，窗口左侧的表格视图（table view）是根据 NewItemsClient 对象（前面讨论的所有方法都属于该对象）上名为 `newItems` 的 NSArray 来填充的。由于用户界面已在 Interface Builder 中配置为自动处理此填充，因此需要做的只是以符合键值观察（Key-Value-Observing）的方式更新 `newItems`。

以下代码片段应紧接在前一个代码片段之后插入：

```objc
    [self willChangeValueForKey:@"newItems"];
    [newItems release];
    newItems = [[NSMutableArray array] retain];
    for (NSXMLElement *node in newItemsNodes)
    {
        NSString *relativeString = [[node attributeForName:@"href"] stringValue];
        NSURL *url = [NSURL URLWithString:relativeString relativeToURL:baseURL];
        
        NSString *linkText = [[node childAtIndex:0] stringValue];
        
        [newItems addObject:
            [NSDictionary dictionaryWithObjectsAndKeys:
                [url absoluteString], @"linkURL",
                linkText, @"linkText",
                nil]];
    }
    [self didChangeValueForKey:@"newItems"];
```

最终结果使 `newItems` 数组填满了来自「新品上架」列表中各项的绝对 URL 和链接文本。

在 Interface Builder 中组装的用户界面负责处理显示每项的 "linkText" 的细节。一个连接器（connector）对象跟踪表格中的选择变化，并在 WebView 中显示选中项的 "linkURL"。

> 你可以[下载完整的 XCode 项目](https://www.cocoawithlove.com/assets/objc-era/NewToTheStore.zip)来查看所演示的示例。它基于 XCode 3.1 构建，但也可以在 3.0 中加载（会有一个可以忽略的警告）。

## 结论

我希望我已经向你展示，在 Cocoa 中，「由网络检索数据驱动的小型 App」这一 Dashboard 小组件的细分领域是可以快速、简单地实现的。

示例是从 HTML 获取的，但这些技术对于 RSS 或通过 HTTP 获取的通用 XML 数据也是类似或相同的。
