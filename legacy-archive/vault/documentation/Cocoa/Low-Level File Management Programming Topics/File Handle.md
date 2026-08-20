---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/FileHandle.html
archived_at: '2026-07-15T07:16:34.050813Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [底层文件管理编程主题](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)


[下一页](HFS%20File%20Types.md)[上一页](Resolving%20Aliases.md)

# File Handle

`NSFileHandle` 对象为访问打开的文件或通信通道提供了面向对象的封装。

`NSFileHandle` 是表示一个打开的文件或通信通道的对象。它使程序能够读取或写入所表示的文件或通道中的数据。你也可以使用其他 Cocoa 方法来读写文件——`NSFileManager` 的 `contentsAtPath:` 和 `NSData` 的 [writeToFile:options:error:](https://developer.apple.com/documentation/foundation/nsdata/1414800-writetofile) 只是其中两个例子。那么为什么要使用 `NSFileHandle` 呢？它有什么优势？

- `NSFileHandle` 让你对文件的输入/输出操作有更强的控制力。它允许对打开的文件执行更多操作，例如定位（seeking）、截断（truncating），以及在文件内的精确位置（文件指针）进行读写。其他方法只能整体读取或写入整个文件；使用 `NSFileHandle`，你可以在打开的文件内移动并插入、提取和删除数据。
- `NSFileHandle` 的适用范围不限于文件。它是 Foundation 中唯一能够读写由套接字（socket）、管道（pipe）和设备实现的通信通道的对象。
- `NSFileHandle` 使异步后台通信成为可能。借助它，程序可以在单独的线程中连接套接字并从中读取数据。（具体做法请参阅下文的[使用套接字进行后台进程间通信](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44deljzg42tamq)。）

`NSPipe` 是与 `NSFileHandle` 密切相关的类，其实例表示管道：单向的进程间通信通道。详情请参阅 [NSPipe](https://developer.apple.com/documentation/foundation/nspipe) 参考文档。

`NSFileHandle` 是一个类簇（class cluster），文件句柄对象并不是 `NSFileHandle` 类的实际实例，而是其某个私有子类的实例。尽管文件句柄对象的类是私有的，但其接口是公开的，由抽象超类 `NSFileHandle` 声明。

通常，你通过向 `NSFileHandle` 类对象发送 `fileHandle...` 系列消息之一来实例化文件句柄对象。这些方法返回一个指向相应文件或通信通道的文件句柄对象。为方便起见，`NSFileHandle` 提供了类方法来创建表示文件系统中文件和设备的对象，以及返回表示标准输入、标准输出和标准错误设备的对象。你也可以使用 `initWithFileDescriptor:` 和 `initWithFileDescriptor:closeOnDealloc:` 方法从文件描述符（如 BSD 系统上的文件描述符）创建文件句柄对象。如果你使用这些方法创建文件句柄对象，你就“拥有”所表示的描述符，并负责将其从系统表中移除——通常是向该文件句柄对象发送 `closeFile` 消息。

套接字是进程之间的全双工通信通道，这些进程可以位于同一台主机上，也可以一个进程位于远程主机上。与管道中数据只能单向流动不同，套接字允许进程既发送又接收数据。`NSFileHandle` 通过提供在后台线程中运行的机制来接受套接字连接和从套接字读取数据，从而简化了流式（stream-type）套接字上的通信。

`NSFileHandle` 目前只处理流式套接字上的通信。如果你想使用数据报（datagram）或其他类型的套接字，必须使用原生系统例程来创建和管理连接。

通信通道一端的进程（服务器）首先使用系统例程创建并准备一个套接字。这些例程在 BSD 和非 BSD 系统之间略有差异，但都包含相同的步骤序列：

1. 创建某种协议的流式套接字。
2. 为该套接字绑定一个名称。
3. 将自己添加为 `NSFileHandleConnectionAcceptedNotification` 的观察者。
4. 向此文件句柄对象发送 `acceptConnectionInBackgroundAndNotify`。该方法在后台接受连接，从新的套接字描述符创建一个新的 `NSFileHandle` 对象，并发送一个 `NSFileHandleConnectionAcceptedNotification` 通知。

在为响应该通知而实现的方法中，服务器从通知的 _userInfo_ 字典中提取表示连接“近端”套接字的 `NSFileHandle` 对象；为此它使用 `NSFileHandleNotificationFileHandleItem` 键。

通常，另一个进程（客户端）随后定位由第一个进程创建的命名套接字。客户端不是通过调用相应的系统例程来接受与该套接字的连接，而是以套接字标识符作为 `initWithFileDescriptor:` 的参数来创建一个 `NSFileHandle` 对象。

现在，客户端可以通过向 `NSFileHandle` 实例发送 `writeData:` 来经通信通道向另一个进程发送数据。（注意 `writeData:` 可能会阻塞。）客户端也可以直接从 `NSFileHandle` 读取数据，但这会导致进程阻塞，直到套接字连接关闭，因此通常最好在后台读取。为此，进程必须：

1. 将自己添加为 `NSFileHandleReadCompletionNotification` 或 `NSFileHandleReadToEndOfFileCompletionNotification` 的观察者。
2. 向此 `NSFileHandle` 对象发送 `readInBackgroundAndNotify` 或 `readToEndOfFileInBackgroundAndNotify`。前一个方法在每次数据传输后发送通知；后一个方法累积数据，仅在发送进程关闭其连接一端之后才发送通知。
3. 在为响应这些通知之一而实现的方法中，进程使用 `NSFileHandleNotificationDataItem` 键从通知的 _userInfo_ 字典中提取已传输或已累积的数据。
4. 如果你希望继续接收通知，需要在你的观察者方法中再次调用 `readInBackgroundAndNotify`。

通过向 `NSFileHandle` 对象发送 `closeFile`，你可以关闭通信通道的两个方向；任一进程也可以使用特定于系统的 shutdown 命令部分或完全关闭套接字连接上的通信。

[下一页](HFS%20File%20Types.md)[上一页](Resolving%20Aliases.md)
