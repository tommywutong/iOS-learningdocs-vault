---
title: 使用 Network Framework 实现 netcat
framework: Network
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 10.14+, Xcode 12.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/implementing-netcat-with-network-framework
source_url: 'https://developer.apple.com/documentation/network/implementing-netcat-with-network-framework'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/implementing-netcat-with-network-framework.json'
content_hash: 'sha256:fa9db4a01698c244'
translated: true
---

> 导航：[技术](../technologies.md) · [Network](../network.md)

# 使用 Network Framework 实现 netcat

<sub>示例代码</sub>

构建一个简单的 `netcat` 工具，用于建立网络连接并传输数据。

## 概述

`netcat` 工具（在 macOS 上简写为 `nc`）是一个 UNIX 工具，可让你：

- 建立出站 TCP 和 UDP 连接。
- 监听入站 TCP 和 UDP 连接。
- 在网络连接与 `stdin` 和 `stdout` 之间传输数据。

此示例代码展示了如何构建 `nwcat`，它提供了上述功能，并额外添加了 TLS 和 Bonjour 支持。

`nwcat` 工具支持两种模式：一种建立出站连接，另一种监听入站连接。你可以通过命令行参数选择模式。要建立到 `example.com` 端口 80 的出站连接，运行：

```shell
$ nwcat example.com 80
```

要监听入站连接，提供 `-l` 选项和要监听的端口号：

```shell
$ nwcat -l 12345
```

默认情况下，`nwcat` 使用 TCP。`-u` 参数切换到 UDP，`-t` 参数为 TCP 连接添加 TLS，为 UDP 连接添加 DTLS。`-b` 参数允许使用 Bonjour 服务名称而非主机名。

### 创建出站连接

在 Network 框架中，数据的双向流由连接对象（[`nw_connection_t`](nw_connection_t.md)）表示。若使用 TCP，连接对象与底层 TCP 连接之间存在直接映射。若使用 UDP，连接对象表示本地端口与特定远程对等端端口之间的双向数据报流。

要创建出站连接对象，必须提供参数对象（[`nw_parameters_t`](nw_parameters_t.md)）和端点（[`nw_endpoint_type_t`](nw_endpoint_type_t.md)）。

**创建参数对象。** 参数对象（类型为 [`nw_parameters_t`](nw_parameters_t.md)）包含配置网络连接所需的所有参数。这些参数包括：

- 涉及的协议，例如 TCP 或 UDP，或者是否启用 TLS。
- 针对这些协议的任何选项。
- 对连接的任何约束，例如是否使用蜂窝接口。

要创建参数对象，根据你想使用 TCP 还是 UDP，调用 [nw_parameters_create_secure_tcp](<nw_parameters_create_secure_tcp(____).md>) 或 [nw_parameters_create_secure_udp](<nw_parameters_create_secure_udp(____).md>) 便捷函数。

```objc
nw_parameters_configure_protocol_block_t configure_tls = NW_PARAMETERS_DISABLE_PROTOCOL;
if (g_use_udp) {
    parameters = nw_parameters_create_secure_udp(
        configure_tls,
        NW_PARAMETERS_DEFAULT_CONFIGURATION
    );
} else {
    parameters = nw_parameters_create_secure_tcp(
        configure_tls,
        NW_PARAMETERS_DEFAULT_CONFIGURATION
    );
}
```

这些函数接受两个参数：

- 第一个参数配置连接的安全协议。传入 `NW_PARAMETERS_DISABLE_PROTOCOL` 表示不使用任何安全措施。
- 第二个参数配置连接的传输协议。传入 `NW_PARAMETERS_DEFAULT_CONFIGURATION` 以获取默认配置。

> [!note] 注意
> 如果你对启用 TLS 或配置协议选项感兴趣，请查看 `create_outbound_connection` 函数，其中包含这些更高级功能的示例。例如，`nwcat` 支持为 TLS 监听器和客户端设置 TLS 预共享密钥。

**创建端点。** 端点（类型为 [`nw_endpoint_type_t`](nw_endpoint_type_t.md)）持有一个网络主机或服务名称。对于出站连接，端点决定了你要连接到的远程主机。在大多数情况下，这包括一个主机名和一个端口号，但也存在其他选项。例如，你还可以创建指向 Bonjour 服务的端点。

在 `nwcat` 工具中，用户通过命令行参数提供主机名和端口号，你需要从这两个字符串创建一个端点。为此，调用 [nw_endpoint_create_host](<nw_endpoint_create_host(____).md>)。

```objc
nw_endpoint_t endpoint = nw_endpoint_create_host(name, port);
```

这些字符串支持符号值和数值：

- 主机名可以是 DNS 名称（如 `example.com`），也可以是 IP 地址的字符串表示形式（如 IPv4 的 `"203.0.113.7"` 或 IPv6 的 `"2606:2800:220:1:248:1893:25c8:1946"`）。
- 端口可以是数字值（如 `"80"`），也可以是服务名称（如 `"https"`）。

> [!important] 重要
> 如果传入 DNS 名称，连接对象会为你处理 DNS 解析，应对[决定连接哪个 IP 地址](https://tools.ietf.org/html/rfc8305)这一复杂问题。对于出站连接，无需自行进行 DNS 解析，在大多数情况下，这样做反而会导致更差的用户体验。

**创建连接对象。** 有了参数对象和端点后，就可以调用 [nw_connection_create](<nw_connection_create(____).md>) 创建连接对象。

```objc
nw_connection_t connection = nw_connection_create(endpoint, parameters);
```

**启动连接。** 要启动连接建立过程：

1. 调用 [nw_connection_set_queue](<nw_connection_set_queue(____).md>) 设置 [`dispatch_queue_t`](../dispatch/dispatch_queue_t.md)，所有回调都将在该队列上调度。对于像 `nwcat` 这样的简单应用，可以使用主队列进行回调。更复杂的应用通常会改用自定义的串行队列。
2. 安装任何更新的处理程序 block。其中最重要的是状态变更处理程序，下面会讨论。
3. 调用 [nw_connection_start](<nw_connection_start(__).md>) 启动连接。

必须在启动连接之前设置队列，之后无法更改队列。

```objc
void
start_connection(nw_connection_t connection)
{
    nw_connection_set_queue(connection, dispatch_get_main_queue());
    nw_retain(connection);
    nw_connection_set_state_changed_handler(connection, ^(nw_connection_state_t state, nw_error_t error) {
        … your state changed handler …
    });
    nw_connection_start(connection);
}
```

> [!important] 重要
> 当连接对象的最后一个引用被释放时，它会关闭底层的网络连接。因此，在连接使用完毕之前，必须通过调用 [nw_retain](nw_retain.md) 来保留连接对象。

状态变更处理程序是一个 block，每当连接状态发生变化时，连接对象就会调用它。对于像 `nwcat` 这样的简单应用，可以使用非常简单的状态变更处理程序。

```objc
if (state == nw_connection_state_waiting) {
    … tell the user that a connection couldn’t be opened but will retry when conditions are favourable …
} else if (state == nw_connection_state_failed) {
    … tell the user that the connection has failed irrecoverably …
} else if (state == nw_connection_state_ready) {
    … tell the user that you are connected …
} else if (state == nw_connection_state_cancelled) {
    nw_release(connection);
}
```

确保处理 [`nw_connection_state_cancelled`](nw_connection_state_cancelled.md) 状态。一旦不再需要该连接，必须释放你在启动连接时获取的引用。

### 监听入站连接

监听器对象（类型为 [`nw_listener_t`](nw_listener_t.md)）用于监听入站连接，并为每个入站连接创建一个新的连接对象。要创建监听器对象，必须提供参数对象（[`nw_parameters_t`](nw_parameters_t.md)）以指明要使用的协议以及要监听的本地端点信息。

**创建参数对象。** 为监听器对象创建参数对象与为出站连接创建参数对象非常相似。使用 [nw_parameters_create_secure_tcp](<nw_parameters_create_secure_tcp(____).md>) 和 [nw_parameters_create_secure_udp](<nw_parameters_create_secure_udp(____).md>) 便捷函数来定义监听器要使用的协议。这些参数将应用于监听器接受的任何入站连接。例如，如果在参数对象中启用了 TLS，那么一旦调用 [nw_connection_start](<nw_connection_start(__).md>)，所有入站连接都将协商 TLS。

**设置本地端点。** 监听器对象必须知道要在哪个本地端点上监听，即客户端必须连接的端点。本地端点可以包含端口号和接口地址，两者都是可选的。如果不指定端口号，系统会为你选择一个端口。如果不指定接口地址，系统会在所有接口和所有地址上进行监听。

大多数应用不需要在特定的接口地址上监听，因此可以使用 [nw_listener_create_with_port](<nw_listener_create_with_port(____).md>) 便捷函数创建监听器。然而，`nwcat` 允许用户指定接口地址（通过命令行参数），因此你必须使用稍微复杂一些的技术。如果用户指定了接口地址或端口，你可以调用 [nw_endpoint_create_host](<nw_endpoint_create_host(____).md>) 创建一个代表要监听的地址的端点，然后调用 [nw_parameters_set_local_endpoint](<nw_parameters_set_local_endpoint(____).md>) 将其应用到你的参数对象。

```objc
if (address || port) {
    nw_endpoint_t local_endpoint = nw_endpoint_create_host(address ? address : "::", port ? port : "0");
    nw_parameters_set_local_endpoint(parameters, local_endpoint);
    nw_release(local_endpoint);
}
```

使用 [nw_endpoint_create_host](<nw_endpoint_create_host(____).md>) 为本地地址创建端点时，请记住以下几点：

- `port` 参数可以是数字字符串，如 `"443"`，也可以是服务名称，如 `"https"`。
- 如果将 `"0"` 传递给 `port` 参数，系统会代你选择一个端口。

**创建监听器对象。** 设置好参数对象后，可以调用 [nw_listener_create](<nw_listener_create(__).md>) 创建监听器对象。

```objc
nw_listener_t listener = nw_listener_create(parameters);
```

**启动监听器。** 启动监听器对象与启动连接对象非常相似，但有一个显著区别：除了设置状态变更处理程序外，还必须设置一个新连接处理程序，该处理程序在监听器收到新的入站连接时被调用。

```objc
nw_listener_set_queue(listener, dispatch_get_main_queue());
nw_retain(listener);
nw_listener_set_state_changed_handler(listener, ^(nw_listener_state_t state, nw_error_t error) {
    … your state changed handler …
});
nw_listener_set_new_connection_handler(listener, ^(nw_connection_t connection) {
    … your new connection handler …
});
nw_listener_start(listener);
```

**接受或拒绝入站连接。** 你的新连接处理程序负责启动网络连接或拒绝它。`nwcat` 命令一次只能处理一个连接，因此如果已经存在一个网络连接，请调用 [nw_connection_cancel](<nw_connection_cancel(__).md>) 拒绝新连接。如果没有，则保留该网络连接，并使用与出站连接相同的 `start_connection` 函数来运行连接。

```objc
if (g_inbound_connection != NULL) {
    nw_connection_cancel(connection);
} else {
    g_inbound_connection = connection;
    nw_retain(g_inbound_connection);

    start_connection(g_inbound_connection);
}
```

### 传输数据

创建并启动连接（无论是出站还是入站）后，你需要编写代码来在该连接上传输数据。每个连接都有两个方向：

- 入站数据从网络连接接收并写入 `stdout`。
- 出站数据从 `stdin` 读取并发送到网络连接。

这两个方向都是异步的。从网络接收数据时，你提供一个完成处理程序（completion handler），当数据可用时被调用。同样，向网络写入数据时，你提供一个完成处理程序，当数据已被接受准备传输时被调用。

在处理异步网络时，需要考虑流量控制。例如，如果从网络接收数据的速度快于将其写入 `stdout` 的速度，你会浪费大量内存来缓冲这些数据。如果从 `stdin` 读取数据的速度快于通过网络发送的速度，也会出现类似问题。你可以通过使用异步例程来读取 `stdin` 和写入 `stdout` 来解决这个问题。基本策略如下：

1. 开始一个异步读取。
2. 读取完成后，开始一个异步写入。
3. 写入完成后，设置下一个异步读取，然后再次回到步骤 1。

对于入站和出站数据，你使用类似的策略，但存在一些细微差别，将在后续章节中讨论。

**接收数据。** 你可以使用如下代码接收数据。

```objc
void
receive_loop(nw_connection_t connection)
{
    nw_connection_receive(connection, 1, UINT32_MAX, ^(dispatch_data_t content, nw_content_context_t context, bool is_complete, nw_error_t receive_error) {

        nw_retain(context);
        dispatch_block_t schedule_next_receive = ^{
            … discussed below …
            nw_release(context);
        };

        if (content != NULL) {
            schedule_next_receive = Block_copy(schedule_next_receive);
            dispatch_write(STDOUT_FILENO, content, dispatch_get_main_queue(), ^(__unused dispatch_data_t _Nullable data, int stdout_error) {
                if (stdout_error != 0) {
                    … error logging …
                } else {
                    schedule_next_receive();
                }
                Block_release(schedule_next_receive);
            });
        } else {
            // 没有内容，因此直接调度下一次接收
            schedule_next_receive();
        }
    });
}
```

> [!note] 注意
> 虽然这个函数名为 `receive_loop`，但它实际上不是一个循环。相反，它是循环的异步等价物，在从网络的异步接收和向 `stdout` 的异步写入之间来回跳转。

该函数首先调用 [nw_connection_receive](<nw_connection_receive(________).md>)，这是一个从连接对象接收数据的异步函数。该函数有两个参数，用于控制要接收的最小和最大数据量。这里具体接收多少数据并不重要，因此分别传入 `1` 和 `UINT32_MAX`。

> [!note] 注意
> 在实现面向记录的协议时，最小和最大接收参数非常有用。许多网络协议通过 TCP 流传输记录时，会先发送记录长度，再发送记录本身。如果使用此类协议，可以先接收长度字段，然后在知道记录长度后，再进行第二次接收以获取完整的记录体。

当接收完成时，[nw_connection_receive](<nw_connection_receive(________).md>) 会调用你传入的完成处理程序。该完成处理程序有四个参数：

- 一个 [`dispatch_data_t`](../dispatch/dispatch_data_t.md)，如果非 `NULL`，则包含接收到的数据。
- 一个内容上下文（content context），下面讨论。
- 一个 `is_complete` 参数，如果接收到的数据是一个逻辑数据单元的最后一部分，则为 true。
- 一个 `receive_error` 参数，如果在接收过程中发生错误，则不为 `NULL`。

内容上下文（类型为 [`nw_content_context_t`](nw_content_context_t.md)）保存有关接收数据的附加信息。仅使用 TCP 的典型应用通常可以完全忽略这个值。然而，`netcat` 实现必须同样适用于 TCP 和 UDP，你需要内容上下文来实现这一点。

你传递给 [nw_connection_receive](<nw_connection_receive(________).md>) 的完成处理程序执行以下操作：

1. 它通过启动向 `stdout` 的异步写入来处理接收到的所有数据。
2. 当该异步写入完成时——或者在没有内容时立即——调用 `schedule_next_receive` 继续接收。

在 `schedule_next_receive` 中，你必须处理三种情况：

- 如果刚刚接收到数据流的结尾，调用 `exit` 终止程序。当远程对等端关闭网络连接时，程序通过这种方式停止。
- 如果接收因错误而失败，处理该错误。
- 否则，通过调用 `receive_loop` 启动下一个异步接收。

```objc
nw_retain(context);
dispatch_block_t schedule_next_receive = ^{
    if (is_complete &&
        (context == NULL || nw_content_context_get_is_final(context))) {
        exit(0);
    }
    if (receive_error == NULL) {
        receive_loop(connection);
    } else {
        … error logging …
    }
    nw_release(context);
};
```

> [!important] 重要
> 必须在检查其他状态（数据流结尾或错误）之前处理接收到的所有数据，因为你的完成处理程序可能同时接收到数据和其他状态。

要检查数据流的结尾：

- 一般来说，可以使用 `schedule_next_receive` 所示的技术，即同时检查 `is_complete` 标志以及上下文是否被标记为最终状态或不存在。该技术对 TCP 和 UDP 都适用，因此对于 `netcat` 实现是必需的。
- 如果只处理 TCP，可以只测试 `is_complete` 标志。

**发送数据。** 你的发送代码应具有与接收代码相同的基本结构。

```objc
void
send_loop(nw_connection_t connection)
{
    dispatch_read(STDIN_FILENO, 8192, dispatch_get_main_queue(), ^(dispatch_data_t _Nonnull read_data, int stdin_error) {
        if (stdin_error != 0) {
            … error logging …
        } else if (read_data == NULL) {
            … handle end of file …
        } else {
            nw_connection_send(connection, read_data, NW_CONNECTION_DEFAULT_MESSAGE_CONTEXT, true, ^(nw_error_t  _Nullable error) {
                if (error != NULL) {
                    … error logging …
                } else {
                    send_loop(connection);
                }
            });
        }
    });
}
```

然而，存在一些细微差别：

- 如果像本例中一样支持 UDP，则必须限制从 `stdin` 读取的数据量。如果读取超过 64 Kibibytes（KiB），结果读取将无法放入单个 UDP 数据报中。此代码使用了 8 KiB 的限制。
- 你必须通过调用 [nw_connection_send](<nw_connection_send(__________).md>) 并传入 `NW_CONNECTION_DEFAULT_MESSAGE_CONTEXT` 以及将 `is_complete` 参数设为 true，来告知网络连接将数据作为单个消息发送。这种方法适用于 TCP 和 UDP 连接。对于 TCP 连接，消息边界不影响协议发送数据的方式，但对于发送 UDP 数据报是必需的。
- 最后，当从 `stdin` 接收到文件结尾时，必须关闭连接的发送端。相关代码如下所示。

  ```objc
  nw_connection_send(connection, NULL, NW_CONNECTION_FINAL_MESSAGE_CONTEXT, true, ^(nw_error_t  _Nullable error) {
      if (error != NULL) {
          … handle error …
      }
      // 停止从 stdin 读取，不再调度下一个 send_loop
  });
  ```

  这传入了一个特殊上下文 `NW_CONNECTION_FINAL_MESSAGE_CONTEXT`，并将 `is_complete` 设为 true。这些操作共同表明不会再发送更多数据，从而允许网络连接关闭连接的发送端。

## 另请参阅

### 连接和监听器

- [nw_connection_t](nw_connection_t.md) — 本地端点与远程端点之间的双向数据连接。
- [nw_listener_t](nw_listener_t.md) — 用于监听传入网络连接的对象。
- [nw_browser_t](nw_browser_t.md) — 用于浏览可用网络服务的对象。
- [nw_connection_group_t](nw_connection_group_t.md) — 用于与一组端点通信的对象，例如本地网络上的 IP 多播组。
- [nw_ethernet_channel_t](nw_ethernet_channel_t.md) — 用于发送和接收自定义以太网帧的对象。

## 下载

- [ImplementingWithNetworkFramework.zip](https://docs-assets.developer.apple.com/published/f1d9686fa841/ImplementingWithNetworkFramework.zip)
