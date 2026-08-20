---
title: 'Friday Q&A 2014-03-14：Socket API 入门'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-03-14-introduction-to-the-sockets-api.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:293ec1fa6957bcc4'
translated: true
---

> 原文：[Friday Q&A 2014-03-14: Introduction to the Sockets API](https://www.mikeash.com/pyblog/friday-qa-2014-03-14-introduction-to-the-sockets-api.html)　·　mikeash.com Friday Q&A

发布于 2014-03-14 13:52 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2014-05-09: When an Autorelease Isn't](https://www.mikeash.com/pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html)  
上一篇：[Tales From The Crash Mines: Issue #1](https://www.mikeash.com/pyblog/tales-from-the-crash-mines-issue-1.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [networking](https://www.mikeash.com/pyblog/?tag=networking) [sockets](https://www.mikeash.com/pyblog/?tag=sockets)

Friday Q&A 2014-03-14：Socket API 入门

作者：[Mike Ash](https://www.mikeash.com/)

**Socket**  
就这个 API 而言，一个 _socket_ 是一种 UNIX 文件描述符。也就是说，它是一个（通常很小的）`int`，对应一个内核结构体。像任何文件描述符一样，你可以对 socket 进行 `read` 和 `write`，但 socket 还允许其他操作。

要创建 socket，请调用 `socket` 函数。它需要三个参数。第一个参数是 socket 的 domain（域），基本上决定了 socket 将使用哪个 IP 级协议。这个参数的常见值有 `AF_INET`（指定 IPv4）和 `AF_INET6`（指定 IPv6）。第二个参数是 socket 的 type（类型），本质上允许你选择 TCP 或 UDP。TCP 传入 `SOCK_STREAM`，UDP 传入 `SOCK_DGRAM`。第三个参数在当今的正常使用中已几乎形同虚设，直接传零即可。下面是一行创建 socket 的代码：

```
    int s = socket(AF_INET6, SOCK_STREAM, 0)
```

按惯例，本文的示例中我将大部分省略错误检查。在你自己的代码里，请不要省略。

这个新创建的 socket 本身没什么用。它实际上没有连接到任何地方，所以你不能读写。使用它需要更专门的调用。这些调用需要 **地址**。

**地址**  
地址由一族 `struct` 来表示，它们的组织方式类似于面向对象继承——如果要在 C 里糟糕地实现面向对象继承的话。

“基类”是 `struct sockaddr`，包含地址族（基本上就是地址的类型）、原始地址数据和总长度：

```
    struct sockaddr {
        __uint8_t   sa_len;     /* total length */
        sa_family_t sa_family;  /* [XSI] address family */
        char        sa_data[14];    /* [XSI] addr value (actually larger) */
    };
```

只有 16 字节长，这对于所有用途来说确实不够，尤其考虑到 IPv6。在传递指针进行类型转换时这不是问题，但当声明一个局部的 `struct sockaddr` 来 _接收_ 函数传来的地址时就麻烦了。为了解决这个问题，有一个较新的（也就十五年左右的历史）“基类”结构体提供了更多存储空间，恰当地命名为 `struct sockaddr_storage`：

```
    struct sockaddr_storage {
        __uint8_t   ss_len;     /* address length */
        sa_family_t ss_family;  /* [XSI] address family */
        char            __ss_pad1[_SS_PAD1SIZE];
        __int64_t   __ss_align; /* force structure storage alignment */
        char            __ss_pad2[_SS_PAD2SIZE];
    };
```

概念与 `struct sockaddr` 相同，只是更长。中间还有一些精巧的设计来保证整个结构体正确对齐，不过你可以忽略它们。

各个地址族有各自的“子类”，它们与上面的布局兼容，因此你可以在不同类型之间转换指针。对于 IPv4 地址，对应的地址类型是 `struct sockaddr_in`：

```
    struct sockaddr_in {
        __uint8_t   sin_len;
        sa_family_t sin_family;
        in_port_t   sin_port;
        struct  in_addr sin_addr;
        char        sin_zero[8];
    };
```

`sin_port` 字段是地址的 TCP 或 UDP 端口，`sin_addr` 是实际的四字节 IPv4 地址。它们一起构成了一个完整的 IPv4“地址”。

IPv6 类似，但更长：

```
    struct sockaddr_in6 {
        __uint8_t   sin6_len;   /* length of this struct(sa_family_t) */
        sa_family_t sin6_family;    /* AF_INET6 (sa_family_t) */
        in_port_t   sin6_port;  /* Transport layer port # (in_port_t) */
        __uint32_t  sin6_flowinfo;  /* IP6 flow information */
        struct in6_addr sin6_addr;  /* IP6 address */
        __uint32_t  sin6_scope_id;  /* scope zone index */
    };
```

`sin6_port` 字段的作用与上面的 `sin_port` 相同，`sin6_addr` 是 16 字节的 IPv6 地址。`sin6_flowinfo` 和 `sin6_scope_id` 是专门的字段，通常不需要过多关注，我们跳过它们。

**监听连接**  
我们来看看如何监听传入的 TCP 连接。创建 socket 之后，你必须把它绑定到一个 IP 地址。这可以是当前计算机的一个具体 IP 地址，也可以是一个特殊的“监听所有”地址——后者通常是你要的。

要绑定到地址，你需要一个 socket 地址。这里我们使用 `struct sockaddr_in6` 并创建一个 IPv6 socket。这样还额外支持接收 IPv4 连接，因此一段代码可以同时处理 IPv4 和 IPv6。我们从基本长度和族信息开始：

```
    struct sockaddr_in6 addr = {
        .sin6_len = sizeof(addr),
        .sin6_family = AF_INET6,
```

我们将端口号硬编码。注意，socket 地址结构体中的端口号始终是 _网络字节序_，即 big-endian，因此在存入或取出值时需要使用字节交换函数。最自然的函数是 POSIX 级的 `htons` 及其同类，但任何字节交换函数都可以。这里我们在端口 `12345` 上监听：

```
        .sin6_port = htons(12345),
```

最后，需要使用常量 `in6addr_any` 作为地址字段，以指定它是特殊的“任意”地址：

```
        .sin6_addr = in6addr_any
    };
```

别忘了实际创建 socket：

```
    int s = socket(AF_INET6, SOCK_STREAM, 0);
```

现在我们可以将其绑定到地址。这个调用自然叫做 `bind`。`bind` 函数接受三个参数：要操作的 socket、要绑定的地址、以及该地址的长度。调用如下：

```
    bind(s, (void *)&addr, sizeof(addr));
```

第二个参数被转换为 `void *`，因为该函数接受 `struct sockaddr *`，而 `addr` 是 `struct sockaddr_in6`。试图提供一族多个半兼容的 `struct` 的代价就是这样。

你可能想知道，既然地址本身也包含长度字段，为什么还要一个长度参数。POSIX 标准实际上不要求有长度字段，所以有些系统提供它，有些不提供。这意味着任何跨平台代码或接口（如 POSIX API 本身）都不能假定长度字段存在，必须单独传递它。

绑定 socket 后，下一步是告诉系统在上面监听。这一步由——你猜对了——`listen` 函数完成。它接受两个参数：要操作的 socket，以及监听队列的期望长度。这个队列长度告诉系统，在尝试将这些传入连接移交给你的程序之前，系统应当暂存多少个传入连接。除非你有充分的理由使用其他值，否则传入 `SOMAXCONN` 会给你一个安全且较大的值。调用如下：

```
    listen(s, SOMAXCONN);
```

现在 socket 处于监听状态，你可以尝试在端口 `12345` 上连接它。程序现在必须接受传入连接，这由 `accept` 函数完成。这个函数接受三个参数：要操作的 socket、存储传入连接地址的位置、以及该存储的长度。这让你能够知道传入连接来自哪里，但它们并非严格必需，所以我们将其设为 `NULL`。该函数返回一个用于传入连接的 socket：

```
    int conn = accept(s, NULL, NULL);
```

然后你可以从这个新 socket 读取数据：

```
    int count = read(conn, buf, sizeof(buf));
    printf("%.*s\n", count, buf);
```

在读写 socket 数据时，你必须编写能处理读取或写入数据少于请求量的代码。`read` 和 `write` 函数调用返回实际读取或写入的字节数。在许多情况下你可以忽略这个值，但在 socket 编程中不行。处理 socket 时，读取或写入的数据量经常少于请求量，因此你必须编写代码来缓冲数据并循环进行多次调用。例如，要将上述数据写回，你需要这样的循环：

```
    int writeCursor = 0;
    int writeCount;
    do {
        writeCount = write(conn, buf + writeCursor, count - writeCursor);
        writeCursor += writeCount;
    } while(writeCursor < count);
```

说实话，这并不完全正确。我试图跳过错误处理，但这里有一个错误情况不能忽略。`read` 或 `write` 调用可能返回 `EINTR` 错误，这是一个瞬态错误，表明系统调用以某种方式被中断。它并不表示失败，只是要求你重试该调用。下面是修正后的代码：

```
    int writeCursor = 0;
    int writeCount;
    do {
        writeCount = write(conn, buf + writeCursor, count - writeCursor);
        if(writeCount < 0) {
            if(errno != EINTR) {
                perror(write);
                break;
            }
        } else {
            writeCursor += writeCount;
        }
    } while(writeCursor < count);
```

当你用完 socket 后，只需 `close` 它：

```
    close(conn);
```

如果需要更精细的控制，可以使用 `shutdown` 函数。这允许只关闭 socket 的一个方向，某些协议下很有用。

**建立连接**  
要建立连接，首先需要一个连接的目标地址。有大约一百六十亿种方式来获取地址，从硬编码、编写解析 IP 地址的代码，到请求系统将人类可读的字符串转换为可连接的地址。

对我们来说幸运的是，让系统替我们完成工作的 API 相对易于使用。现代调用是 `getaddrinfo`。它是一个功能丰富的 API，有很多选项，但基本用法很直接。

首先，我们需要一个主机名。你可能从 UI 或其他地方得到它，但这里我们直接硬编码：

```
    const char *name = "mikeash.com";
```

我们还需要一个端口号。我们可以稍后自己把它塞进地址 `struct`，但更方便的做法是交给 `getaddrinfo`，让它来处理这部分：

```
    int port = 80;
```

`getaddrinfo` 实际上希望端口号以字符串形式提供。如果你的端口号最初就是字符串，这非常方便，但这里意味着我们需要做一些额外的工作。我将使用 `asprintf` 把整数端口转换成字符串：

```
    char *portString;
    asprintf(&portString, "%d", port);
```

`getaddrinfo` 接受一组“提示”（hints），允许控制它将提供什么样的结果。有很多选项，但我们这里关心的只有 socket 协议。该调用可以返回不同 socket 协议（如 TCP 或 UDP）的结果，我们想确保只查找 TCP 结果。如果不这样做，调用会为每个找到的地址返回两个结果，一个对应一种协议。要指定 TCP，只需在 `ai_protocol` 字段中指定 `IPPROTO_TCP`：

```
    struct addrinfo hints = {
        .ai_protocol = IPPROTO_TCP
    };
```

现在一切就绪，可以调用 `getaddrinfo` 了：

```
    struct addrinfo *info;
    getaddrinfo(name, portString, &hints, &info);
```

一个主机名可能有多个地址。`getaddrinfo` 返回的 `struct addrinfo` 实际上是一个链表，可以遍历它以枚举所有结果：

```
    for(struct addrinfo *cursor = info; cursor; cursor = cursor->ai_next) {
```

我们来把它们全部打印出来。`struct addrinfo` 包含一个 `ai_addr` 字段，指向一个 `struct sockaddr`。我们可以像下面这样使用 `getnameinfo` 将其转换为人类可读的字符串：

```
        char addrStr[NI_MAXHOST];
        getnameinfo(cursor->ai_addr,
                    cursor->ai_addrlen,
                    addrStr,
                    sizeof(addrStr),
                    NULL,
                    0,
                    NI_NUMERICHOST));
```

我们还有一些其他相关字段一并打印出来：

```
        printf("flags=%x family=%d type=%d protocol=%d address=%s\n",
               cursor->ai_flags,
               cursor->ai_family,
               cursor->ai_socktype,
               cursor->ai_protocol,
               addrStr);
    }
```

对于 `google.com`，这会生成一个漂亮的地址列表：

```
    flags=0 family=2 type=1 protocol=6 address=74.125.228.228
    flags=0 family=2 type=1 protocol=6 address=74.125.228.224
    flags=0 family=2 type=1 protocol=6 address=74.125.228.232
    flags=0 family=2 type=1 protocol=6 address=74.125.228.227
    flags=0 family=2 type=1 protocol=6 address=74.125.228.230
    flags=0 family=2 type=1 protocol=6 address=74.125.228.233
    flags=0 family=2 type=1 protocol=6 address=74.125.228.231
    flags=0 family=2 type=1 protocol=6 address=74.125.228.229
    flags=0 family=2 type=1 protocol=6 address=74.125.228.238
    flags=0 family=2 type=1 protocol=6 address=74.125.228.226
    flags=0 family=2 type=1 protocol=6 address=74.125.228.225
    flags=0 family=30 type=1 protocol=6 address=2607:f8b0:4004:803::1009
```

我们准备好创建 socket 了。这里我们只取列表中的第一个值。在实际代码中，你会希望遍历列表，并在一个失败时尝试其他条目，可能还会同时尝试多个条目以获得更快的速度。`ai_family`、`ai_socktype` 和 `ai_protocol` 字段提供了创建 socket 所需的一切：

```
    int s = socket(info->ai_family, info->ai_socktype, info->ai_protocol);
```

现在需要让它连接到目标地址。这由名称恰当的 `connect` 函数完成，它接受 socket、目标地址及其长度：

```
    connect(s, info->ai_addr, info->ai_addrlen);
```

当此调用成功完成后，我们就得到了一个连接到目标地址的 socket。现在我们可以使用这个 socket 进行读写。在此之前，既然地址数据处理完毕，我们将其释放：

```
    freeaddrinfo(info);
```

别忘了端口字符串：

```
    free(portString);
```

由于我们连接到端口 80，可以向这个 socket 写入一个 HTTP 请求：

```
    const char *toWrite = "GET /\r\n\r\n";
```

由于 socket 是文件描述符，`write` 可以直接使用。一如既往，务必使用循环：

```
    while(*toWrite) {
        int written = write(s, toWrite, strlen(toWrite));
        if(writeCount < 0) {
            if(errno != EINTR) {
                perror(write);
                break;
            }
        } else {
            toWrite += written;
        }
    }
```

现在我们可以读取响应，同样使用循环：

```
    char buf[1024];
    int count;
    do {
        count = read(s, buf, sizeof(buf))) > 0);
        if(count < 0) {
            if(errno != EINTR) {
                perror("read");
                break;
            }
        } else {
            printf("%.*s", count, buf);
        }
    } while(count > 0);
```

当 `read` 返回 `0` 时，表示服务器已关闭连接，然后我们可以关闭自己的这一端：

```
    close(s);
```

**总结**  
POSIX socket API 有点老旧粗糙，但总体来说并不算糟糕。只要合理，你应该尽量使用更高级别的 API，不过理解底层 API 的功能以及如何使用它也是件好事，即使你并不经常真的使用它。

今天就到这里。下次再来，更多有趣的冒险在等着你。Friday Q&A 由读者建议驱动，所以如果你有想讨论的话题，请[发送给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在出售整本全是这类文章的书！第二卷和第三卷已经出版！提供 ePub、PDF、印刷版、iBooks 和 Kindle 格式。[点击这里了解更多](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-03-14-introduction-to-the-sockets-api.html)

添加你的想法，发表评论：

垃圾信息和偏离主题的帖子将不经通知删除。违规者可能在我的自行决定下被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
