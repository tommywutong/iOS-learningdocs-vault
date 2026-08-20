---
title: 'Friday Q&A 2009-12-11：一个 GCD 案例研究：构建 HTTP 服务器'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-12-11-a-gcd-case-study-building-an-http-server.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e69ec3b8b792588b'
translated: true
---

> 原文：[Friday Q&A 2009-12-11: A GCD Case Study: Building an HTTP Server](https://www.mikeash.com/pyblog/friday-qa-2009-12-11-a-gcd-case-study-building-an-http-server.html)　·　mikeash.com Friday Q&A

发布于 2009-12-11 23:58 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 RSS](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Rogue Amoeba 正在招聘](https://www.mikeash.com/pyblog/rogue-amoeba-is-hiring.html)  
上一篇文章：[Friday Q&A 2009-12-04：构建独立的 iPhone Web App](https://www.mikeash.com/pyblog/friday-qa-2009-12-04-building-standalone-iphone-web-apps.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [generators](https://www.mikeash.com/pyblog/?tag=generators) [http](https://www.mikeash.com/pyblog/?tag=http) [networking](https://www.mikeash.com/pyblog/?tag=networking)

Friday Q&A 2009-12-11：一个 GCD 案例研究：构建 HTTP 服务器

作者：[Mike Ash](https://www.mikeash.com/)

**技术**  
 HTTP 服务器显然要做大量网络通信，而 GCD 非常适合管理 IO。可以快速轻松地设置一个 dispatch source，在文件描述符可读或可写时触发事件，从而能够编写一个同时支持多个连接的服务器，无需使用为每个连接分配独立线程这种低效技术，也无需编写自己的调度循环或处理混乱的 runloop source。

对异步 IO 的需求也使这个场景成为使用 [generator](https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html) 的绝佳案例。使用 generator 可以让代码以自然的自上而下方式编写，同时保持完全异步，并且在完成之前不会占用线程。这使得增量解析传入的 HTTP 请求或增量发送响应变得非常容易。

此 web 服务器的设计目的主要是为了说明技术并易于理解，而非追求高性能。低效的主要来源是它每次只读写一个字符，这带来了大量的开销，但极大地简化了代码。真正的服务器应该一次性读写大缓冲区，并在使用的 generator 之间传递这些大缓冲区。

**源代码**  
 如果你想在家跟着做，源代码[可在我的公共 subversion 仓库中找到](http://www.mikeash.com/svn/GCDWeb/GCDWeb.m)。

它还依赖于 [MAGenerator](http://www.mikeash.com/svn/MAGenerator/)，因此如果你想要构建它，还需要构建 `MAGenerator.m`，并确保 `MAGenerator.h` 在你的 include 路径中。

由于大量使用 generator，你需要了解它们是什么以及 `MAGenerator` 如何工作。如果你还没看过，[请在继续之前阅读我关于 `MAGenerator` 的文章](https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html)。

**`main`**  
 我将采用自上而下的方式来讲解这个服务器，因此合乎逻辑的起点是 `main`。该程序旨在通过一个参数（端口号）运行，因此它首先检查参数数量是否正确，然后提取端口号：

```
    int main(int argc, char **argv)
    {
        if(argc != 2)
        {
            fprintf(stderr, "usage: %s <port>\n", argv[0]);
            return 1;
        }
        
        int port = atoi(argv[1]);
```

接下来，它会在该端口上设置监听套接字（IPv4 和 IPv6 各一个），然后调用 `dispatch_main` 让 GCD 开始工作：

```
        SetupSockets(port);
        
        LOG("listening on port %d", port);
        
        dispatch_main();
        
        return 0;
    }
```

**Setup**  
 设置套接字的代码是标准的套接字代码，我不会深入细节。如果你不熟悉套接字，网上有很多参考资料。注意，`CHECK` 宏只是用来检查返回值是否为 `-1`，如果是则打印错误并退出程序。

```
    static void SetupSockets(int port)
    {
        int listenSocket4 = CHECK(socket(PF_INET, SOCK_STREAM, 0));
        int listenSocket6 = CHECK(socket(PF_INET6, SOCK_STREAM, 0));
        
        struct sockaddr_in addr4 = { sizeof(addr4), AF_INET, htons(port), { INADDR_ANY }, { 0 } };
        struct sockaddr_in6 addr6 = { sizeof(addr6), AF_INET6, htons(port), 0, IN6ADDR_ANY_INIT, 0 };
        
        int yes = 1;
        CHECK(setsockopt(listenSocket4, SOL_SOCKET, SO_REUSEADDR, (void *)&yes, sizeof(yes)));
        CHECK(setsockopt(listenSocket6, SOL_SOCKET, SO_REUSEADDR, (void *)&yes, sizeof(yes)));
        CHECK(bind(listenSocket4, (void *)&addr4, sizeof(addr4)));
        CHECK(bind(listenSocket6, (void *)&addr6, sizeof(addr6)));
        
        SetupListenSource(listenSocket4);
        SetupListenSource(listenSocket6);
    }
```

`SetupListenSource` 函数是事情开始变得有趣的地方。它首先在套接字上调用 `listen` 使其开始监听连接。然后创建一个新的 `dispatch_source_t` 来处理套接字上的事件。注意，与 `select` 一样，GCD 将监听套接字上的新连接视为读取事件，因此这就是此函数创建的 dispatch source 类型：

```
    static void SetupListenSource(int s)
    {
        CHECK(listen(s, 16));
        
        dispatch_source_t source = NewFDSource(s, DISPATCH_SOURCE_TYPE_READ, ^{
            AcceptConnection(s);
        });
        dispatch_resume(source);
        
        // 泄漏它，它永久存在
    }
```

`NewFDSource` 函数只是对几个 GCD 调用的简单包装：

```
    static dispatch_source_t NewFDSource(int s, dispatch_source_type_t type, dispatch_block_t block)
    {
        dispatch_source_t source = dispatch_source_create(type, s, 0, dispatch_get_global_queue(0, 0));
        dispatch_source_set_event_handler(source, block);
        return source;
    }
```

**Reading**  
 当新连接到达时，会调用 `AcceptConnection` 来建立连接。它首先调用 `accept` 来获取该特定连接的套接字：

```
    static void AcceptConnection(int listenSock)
    {
        struct sockaddr addr;
        socklen_t addrlen = sizeof(addr);
        int newSock = CHECK(accept(listenSock, &addr, &addrlen;));
        LOG("new connection on socket %d, new socket is %d", listenSock, newSock);
```

接下来，它创建一个新的 `Connection` 结构体：

```
        struct Connection *connection = NewConnection(newSock);
```

我最初以为可以完全不用这个结构体，让连接的所有状态都隐式地由 block/generator 状态管理。但这里有个问题。这源于 `dispatch_source` 手册页中的这段话：

```
     Important: a cancellation handler is required for file descriptor and
     mach port based sources in order to safely close the descriptor or
     destroy the port. Closing the descriptor or port before the cancellation
     handler has run may result in a race condition: if a new descriptor is
     allocated with the same value as the recently cosed descriptor while the
     source's event handler is still running, the event handler may read/write
     data to the wrong descriptor.
```

关键在于，套接字是双向的，服务器最终会有两个 dispatch source 监视它，一个用于读取，一个用于写入。任何一个都无法在其取消处理器中安全地关闭套接字，因为不知道哪个会先被取消。因此，`Connection` 结构体只保存套接字以及一个从 2 开始的引用计数。每个取消处理器都会递减引用计数，如果是最后一个，则关闭套接字。

下一步是创建一个请求读取器，这是一个解析传入 HTTP 请求的 generator：

```
        int (^requestReader)(char) = RequestReader(connection);
```

接下来，它创建一个 dispatch source 来检查新套接字上是否有可用数据。事件处理器从套接字读取一个字符，然后将该字符传递给请求读取器。当遇到 `EOF` 时，如果请求不够完整无法生成正常响应，则写出错误响应，然后取消处理器。由于这是一个 HTTP 1.0 服务器，而非 1.1 服务器，因此该连接不可重用于后续请求，客户端必须每次打开一个新连接。

```
        __block BOOL didSendResponse = NO;
        __block dispatch_source_t source; // gcc won't compile if the next line is an initializer?!
        source = NewFDSource(newSock, DISPATCH_SOURCE_TYPE_READ, ^{
            char c;
            LOG("reading from %d", newSock);
            int howMuch = read(newSock, &c, 1);
            LOG("read from %d returned %d (errno is %d %s)", newSock, howMuch, errno, strerror(errno));
            
            BOOL isErr = NO;
            if(howMuch == -1 && errno != EAGAIN && errno != EINTR)
            {
                LOG("read returned error %d (%s)", errno, strerror(errno));
                isErr = YES;
            }
            if(howMuch > 0)
            {
                int ret = requestReader(c);
                if(ret)
                    didSendResponse = YES;
            }
            if(howMuch == 0 || isErr)
            {
                if(!didSendResponse)
                    Write(connection, ErrCodeWriter(400));
                dispatch_source_cancel(source);
            }
        });
```

注意，在读取一个字节后，处理器会自然结束。只要数据可用，GCD 就会继续调用事件处理器，因此 GCD 本质上充当了此代码的外层循环。

取消处理器只是释放连接和 dispatch source：

```
        dispatch_source_set_cancel_handler(source, ^{
            ReleaseConnection(connection);
            dispatch_release(source);
        });
```

作为最后一步，`AcceptConnection` "恢复" source，使其开始处理：

```
        dispatch_resume(source);
    }
```

请求读取器 generator 每次接受一个字符作为参数，并解析 HTTP 请求。使用 generator 的一大优势在此体现：解析器完全以自上而下的方式编写，但却是完全异步的。它返回一个整数来指示调用方是否已发送响应，以便调用方知道是否需要发送自己的故障安全错误响应。如果在任何时候遇到解析错误，它会用错误响应并退出；否则，它会调用 `ProcessResource` 并告知它需要处理哪个资源。此解析器完全忽略客户端发送的任何标头，因此一旦读取了方法和资源，它就简单地进入一个循环并跳过任何剩余的输入。

```
    GENERATOR(int, RequestReader(struct Connection *connection), (char))
    {
        NSMutableData *buffer = [NSMutableData data];
        GENERATOR_BEGIN(char c)
        {
            // 读取请求方法
            while(c != '\r' && c != '\n' && c != ' ')
            {
                [buffer appendBytes: &c length: 1];
                GENERATOR_YIELD(0);
            }
            
            // 如果在遇到空格之前行结束了，那我们不懂这个请求
            if(c != ' ')
            {
                LOG("Got a bad request from the client on %d", connection->sock);
                Write(connection, ErrCodeWriter(400));
                GENERATOR_YIELD(1); // signal that we got enough for a response
            }
            else
            {
                // 我们只支持 GET
                if([buffer length] != 3 || memcmp([buffer bytes], "GET", 3) != 0)
                {
                    LOG("Got an unknown method from the client on %d", connection->sock);
                    Write(connection, ErrCodeWriter(501));
                    GENERATOR_YIELD(1); // signal that we got enough for a response
                }
                else
                {
                    // 跳过分隔符
                    GENERATOR_YIELD(0);
                    
                    // 读取资源
                    [buffer setLength: 0];
                    while(c != '\r' && c != '\n' && c != ' ')
                    {
                        [buffer appendBytes: &c length: 1];
                        GENERATOR_YIELD(0);
                    }
                    
                    LOG("Servicing request from the client on %d", connection->sock);
                    NSString *s = [[[NSString alloc] initWithData: buffer encoding: NSUTF8StringEncoding] autorelease];
                    if(!s)
                        Write(connection, ErrCodeWriter(400));
                    else
                        ProcessResource(connection, s);
                    GENERATOR_YIELD(1); // signal that we got enough for a response
                }
            }
            
            // 我们只忽略客户端发送的其他所有内容
            while(1)
                GENERATOR_YIELD(0);
        }
        GENERATOR_END
    }
```

**响应**  
 `ProcessResource` 函数非常简单。它只是获取所请求资源的 content generator，并写入它：

```
    static void ProcessResource(struct Connection *connection, NSString *resource)
    {
        Write(connection, ContentGeneratorForResource(resource));
    }
```

`ContentGeneratorForResource` 只检查已知的资源并返回相应的处理器，如果找不到则返回"not found"处理器。如果你想添加更多处理器，这里就是添加的地方：

```
    static NSData *(^ContentGeneratorForResource(NSString *resource))(void)
    {
        if([resource isEqual: @"/"])
            return RootHandler(resource);
        if([resource isEqual: @"/listing"])
            return ListingHandler(resource);
        
        return NotFoundHandler(resource);
    }
```

`Write` 函数基本上是上面所示读取处理器的逆操作。它接收 content generator，并将其包装在一个每次生成一个字节的字节 generator 中。然后写入这些字节，直到没有剩余或发生错误，此时它会关闭套接字的写入端并释放连接和 dispatch source：

```
    static void Write(struct Connection *connection, NSData *(^contentGenerator)(void))
    {
        int (^byteGenerator)(void) = ByteGenerator(contentGenerator);
        __block dispatch_source_t source;
        source = NewFDSource(connection->sock, DISPATCH_SOURCE_TYPE_WRITE, ^{
            int byte = byteGenerator();
            BOOL err = NO;
            if(byte != -1) // EOF
            {
                unsigned char buf = byte;
                int howMuch;
                do
                {
                    howMuch = write(connection->sock, &buf, 1);
                }
                while(howMuch == -1 && (errno == EAGAIN || errno == EINTR));
                if(howMuch == -1)
                {
                    err = YES;
                    LOG("write returned error %d (%s)", errno, strerror(errno));
                }
            }
            if(byte == -1 || err)
            {
                LOG("Done servicing %d", connection->sock);
                dispatch_source_cancel(source);
            }
        });
        dispatch_source_set_cancel_handler(source, ^{
            CHECK(shutdown(connection->sock, SHUT_WR));
            ReleaseConnection(connection);
            dispatch_release(source);
        });
        dispatch_resume(source);
    }
```

从声明可以看出，content generator 是一个返回 `NSData` 实例的 generator。其思想是，它可以以合适大小的块返回其响应，而不必一次性在内存中构建整个响应。然而，为了简化写入，此服务器每次只写入一个字节。`ByteGenerator` generator 接收一个 `NSData` generator，并逐个返回单个字节。由于它需要能够在到达末尾时发出信号，它实际上返回一个 `int`，使用 `-1` 作为 `EOF` 信号，用正数表示字节值：

```
    GENERATOR(int, ByteGenerator(NSData *(^contentGenerator)(void)), (void))
    {
        __block NSData *data = nil;
        __block NSUInteger cursor = 0;
        GENERATOR_BEGIN(void)
        {
            do
            {
                if(cursor < [data length])
                {
                    const unsigned char *ptr = [data bytes];
                    GENERATOR_YIELD((int)ptr[cursor++]);
                }
                else
                {
                    [data release];
                    data = [contentGenerator() retain];
                    cursor = 0;
                }
            } while(data);
            GENERATOR_YIELD(-1);
        }
        GENERATOR_CLEANUP
        {
            [data release];
        }
        GENERATOR_END
    }
```

至此，除了处理器之外，服务器基本完成了。

**资源处理器**  
 第一个处理器是错误码写入器。给它一个错误码，它会输出一个适当的错误响应。这用于请求解析代码中的错误处理：

```
    GENERATOR(NSData *, ErrCodeWriter(int code), (void))
    {
        GENERATOR_BEGIN(void)
        {
            if(code == 400)
                GENERATOR_YIELD(Data(@"HTTP/1.0 400 Bad Request"));
            else if(code == 501)
                GENERATOR_YIELD(Data(@"HTTP/1.0 501 Not Implemented"));
            else
                GENERATOR_YIELD(Data(@"HTTP/1.0 500 Internal Server Error"));
            
            NSString *str = [NSString stringWithFormat:
                @"\r\n"
                @"Content-type: text/html\r\n"
                @"\r\n"
                @"The server generated error code %d while processing the HTTP request",
                code];
            GENERATOR_YIELD(Data(str));
        }
        GENERATOR_END
    }
```

接下来，"not found"处理器只生成一个典型的 `404` 错误页面：

```
    GENERATOR(NSData *, NotFoundHandler(NSString *resource), (void))
    {
        GENERATOR_BEGIN(void)
        {
            NSString *str = [NSString stringWithFormat:
                @"HTTP/1.0 404 Not Found\r\n"
                @"Content-type: text/html\r\n"
                @"\r\n"
                @"The resource %@ could not be found",
                HTMLEscape(resource)];
            GENERATOR_YIELD(Data(str));
        }
        GENERATOR_END
    }
```

根处理器只显示一个带有指向另一个更有趣处理器的链接的简单欢迎页面：

```
    GENERATOR(NSData *, RootHandler(NSString *resource), (void))
    {
        GENERATOR_BEGIN(void)
        {
            NSString *str = @"HTTP/1.0 200 OK\r\n"
                            @"Content-type: text/html\r\n"
                            @"\r\n"
                            @"Welcome to GCDWeb. There isn't much here. <a href=\"listing\">Try the listing.</a>";
            GENERATOR_YIELD(Data(str));
        }
        GENERATOR_END
    }
```

最后是一个列表处理器，它用于说明此服务器的异步特性。它使用 `NSDirectoryEnumerator` 列出 `/tmp` 的全部内容。服务器架构允许在创建响应的同时增量生成响应并发送给客户端，而不是缓冲所有内容并以一大块发送，然而响应处理器代码又一次是完全直接的自上而下形式：

```
    GENERATOR(NSData *, ListingHandler(NSString *resource), (void))
    {
        __block NSEnumerator *enumerator = nil;
        GENERATOR_BEGIN(void)
        {
            NSString *str = @"HTTP/1.0 200 OK\r\n"
                            @"Content-type: text/html; charset=utf-8\r\n"
                            @"\r\n"
                            @"Directory listing of <tt>/tmp</tt>:<p>";
            GENERATOR_YIELD(Data(str));
            
            NSFileManager *fm = [[NSFileManager alloc] init]; // +defaultManager is not thread safe
            enumerator = [[fm enumeratorAtPath: @"/tmp"] retain];
            [fm release];
            
            NSString *file;
            while((file = [enumerator nextObject]))
            {
                GENERATOR_YIELD(Data(file));
                // 注意：file 在此之后不再有效！
                
                GENERATOR_YIELD(Data(@"<br>"));
            }
        }
        GENERATOR_CLEANUP
        {
            [enumerator release];
        }
        GENERATOR_END
    }
```

这就是服务器中所有重要的代码。还有一些辅助函数和管理 `Connection` 结构体的代码，这里不再赘述，但如果你想看的话，随时可以[阅读源代码](http://www.mikeash.com/svn/GCDWeb/GCDWeb.m)。

**结论**  
 GCD 和 generator 的组合提供了一个相对简单的异步服务器架构。400 行代码为我们提供了一个相当完整（虽然功能不多）的 web 服务器，它完全多线程化以同时处理多个连接，并自动使用线程池来分配工作。

然而，由于每次读写单个字节，这个服务器的效率并不高。更好的方法是管理缓冲区。这样做不会使代码变得太复杂，并且会消除大量开销。我认为，这将使这个服务器进入可应用于实际场景的范畴。

另一个值得思考的有趣点是，服务器的响应端只在单一方向上是异步的。资源处理器通常会读取文件，但此服务器的架构不允许在资源处理器中异步读取文件，只允许异步写入数据。尽管在正常情况下可能不是问题（文件读取可以简单地阻塞一段时间，除了在完成之前持有一个工作线程外不会造成麻烦），但让服务器在双向都实现异步会更干净，也可能更高效。

实现这一点需要相当多的工作。写入端需要使用两个 dispatch source，一个用于写入套接字，一个用于文件，并且必须以复杂的方式暂停和恢复它们，以阻止 GCD 在等待另一个 source 可用时调用一个 source 的事件处理器。这是可以做到的，并且不会非常复杂，但远远超出了这个演示服务器的范围。

本周的内容就到这里。请于 5e-1 个两周后回来参加一个特别版（特别之处在于，你会不想读它）的一周年回顾版。一如既往，[欢迎继续提出话题建议](mailto:mike@mikeash.com)。Friday Q&A 由你们的想法驱动，所以如果你想看到某个话题的讨论，请发送过来。

喜欢这篇文章吗？我整套书都在卖它们！第二卷和第三卷已经出版！有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-12-11-a-gcd-case-study-building-an-http-server.html)

添加你的想法，发表评论：

垃圾邮件和跑题帖子将被立即删除。违规者可能会被公开羞辱，由我自行决定。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
