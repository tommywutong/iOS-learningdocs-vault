---
title: 构建 Endpoint Security App
session_id: 10159
collection: wwdc2020
year: 2020
duration: '41:35'
topics: ['Privacy & Security', System Services]
group: I · 系统服务、进程与安全底层
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10159/'
content_hash: 'sha256:bb155011168cbd1c'
translated: true
---

# 构建 Endpoint Security App

<sub>WWDC2020 · 41:35 · Privacy & Security、System Services</sub>

系统扩展提高了 macOS 的可靠性和安全性。了解 Kernel Authorization KPI 的现代替代品……

> [!note] 归档理由
> Endpoint Security：内核事件订阅，系统监控底层

## 相关资源

- [使用 Endpoint Security 监控系统事件](https://developer.apple.com/documentation/EndpointSecurity/monitoring-system-events-with-endpoint-security)
- [系统扩展与 DriverKit](https://developer.apple.com/system-extensions/)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10159/7/8B7397DB-B3A9-48C8-A9B7-2F8512EFDB29/wwdc2020_10159_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10159/7/8B7397DB-B3A9-48C8-A9B7-2F8512EFDB29/wwdc2020_10159_sd.mp4?dl=1)
- [Endpoint Security 有啥新内容](https://developer.apple.com/videos/play/wwdc2022/110345)
- [通过更好的隐私建立信任](https://developer.apple.com/videos/play/wwdc2020/10676)
- [系统扩展与 DriverKit](https://developer.apple.com/videos/play/wwdc2019/702)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。

大家好。我叫 Matthew，来自安全工程与架构团队。今天我们将讨论 Endpoint Security 框架。Endpoint Security 框架于去年在 macOS Catalina 中首次引入。它旨在作为 Kauth KPI、不受支持的 Mac 内核框架和 OpenBSM 审计追踪的替代品。

内核扩展，或 KEXTS，可能很难开发，调试起来甚至更难。此外，KEXTS 是维护噩梦，因为内核接口经常变化。

它们还可能降低整体系统安全性和稳定性，因为即使微小的错误也经常导致内核崩溃。

使用 EndpointSecurity 框架，你不再需要开发内核扩展，可以转而专注于产品的真正目标。

使用 EndpointSecurity，或 ES，的产品能够从普通 App 中接入丰富的事件流。目前 ES 支持大约 100 种事件类型，我们还在不断添加。

事件类型分为两类。我们有 NOTIFY 事件，通知你某个操作正在发生，以及 AUTH 事件，允许你控制某个操作是否应该被允许继续。我们将讨论 EndpointSecurity 子系统如何工作，你的产品如何最好地利用事件流，以及一些更高级的可用功能。

虽然可以作为独立产品分发你的 ES App，但我们相信把产品作为基于 EndpointSecurity 的系统扩展来交付有很多好处。系统扩展也是去年在 macOS Catalina 中引入的。支持多种扩展类型，包括用于编写 VPN 和内容过滤器等 App 的网络扩展、用于控制硬件的 DriverKit，以及面向端点检测与响应等产品的 EndpointSecurity。我们不会在这里详细介绍系统扩展，但你应该查看去年 WWDC 2019 标题为 "System Extensions and DriverKit" 的会议以获取更多信息。

首先，当扩展安装后，它受到系统完整性保护的保护，防止你的扩展和资产被意外或恶意篡改。

我们还能为你 daemon 提供更高水平的保护，类似系统 daemon 的保护。这意味着我们防止即使是 root 用户也能卸载你的 launchd 作业。

此外，有些 EndpointSecurity 功能只有当产品是系统扩展时才能使用，例如在系统启动期间，在其他第三方 App 能够执行之前，执行并设置事件流的能力。我喜欢从一个例子开始，所以让我们快速看看开始使用 EndpointSecurity 所需的关键组件。有一点需要注意，这个框架以 C 库的形式提供，这与你可能遇到的许多其他 Apple 框架有点不同。使用 C 让我们对某些内存和性能特性有更大的控制。此外，我们的目标是提供一个能被现有产品快速采用的库。通过使用 C，这个库可从多种语言调用，包括 Swift、Objective-C 和 Rust。

首先，在这个例子中，你可以看到我们使用 ES new client API 初始化一个新的事件流。

这个函数把 ES client T 句柄作为输出参数返回，但重要的是，它也定义了事件处理 block。这里传递的 block 将在有事件准备好处理时被调用。

在这个例子中，你可以看到 block 简单地打印出事件类型。接下来，我们使用 es_subscribe API 设置事件流的订阅。在这个例子中，数组中有一个事件，NOTIFY_EXEC 事件。

同样在这个例子中，我们看到 es_delete client API 被使用，当设置订阅出错时，这个 API 可以用来清理之前从 es_new_client 调用获得的资源。

最后，我们调用 dispatch main，让程序继续执行并通过上面提交的事件处理 block 处理事件。

为了帮助大家理解 EndpointSecurity 如何工作，让我们看看高层架构设计。

当你的进程使用 es_new_client API 连接到 EndpointSecurity 子系统时，会建立一个通道，消息将通过它排队处理。在这个图中，有两个不同的基于 ES 的 App。

一个使用多次调用 es_new_client 设置了两个事件流，第二个有一个通道。我们通常把这些通道称为 ES 客户端。

每个 ES 客户端都能有自己的订阅集，以控制它接收哪些事件。

当事件在内核中触发，并且假设我们的客户端订阅了该事件，EndpointSecurity 会拦截并用通常对执行分析的 ES 客户端有帮助的信息丰富这个事件。

我们稍后会更详细地讨论收集的信息，但一旦收集到，这些数据会被包装在消息信封中。接下来，该消息被发送给所有适当的 ES 客户端，把消息排队给事件处理 block 处理。

消息同时排队给所有客户端。所以对于那些已经熟悉 EndpointSecurity 的人，这是行为的轻微变化，以前事件是串行交付给客户端的。

有些事件需要响应，我们稍后会谈到，这种情况下原始操作在内核中被挂起，直到收到响应。

对于普通通知事件，或收到 AUTH 事件响应后，操作在内核中立即解除阻塞并允许继续。

这个图中最后一点需要注意的是，EndpointSecurity 尽可能缓存，以减少 AUTH 事件需要交付的消息数量。我们稍后会有很多关于缓存的信息。

我刚才提到的消息信封指的是 es_message_t 结构，它是通过事件处理 block 交付给 ES 客户端的所有 ES 事件的包装器。

每条消息包含三类主要信息。第一，消息元数据。这包括事件类型、消息生成时间、它是 AUTH 还是 NOTIFY 事件，以及用于兼容性的消息版本号，我们稍后会谈到。

接下来，所有消息都包含关于最初触发事件的进程的信息。进程信息包括关于可执行文件的信息，包括完整的 stat 信息、代码签名信息、进程 ID 和用户 ID 信息，以及更多。

最后，每条消息包含关于所发生事件的特定信息。例如，SIGNAL 事件包括被信号进程和信号编号的信息。exec 事件包括将要执行的文件和可执行参数等信息，OPEN 事件包括被打开文件和打开标志的信息。

时间检查时间使用问题在开发 ES 产品时极其重要，你需要意识到。快速地，对于可能不熟悉的人，这指的是一类 bug，发生在程序对先前为真但可能不再为真的状态做出假设。这里的经典例子是先检查文件是否存在，然后打开文件作为两步过程。如果系统上有人可能在你的程序检查其存在之后、打开它之前删除了文件，而你的程序没有正确处理打开失败，就可能导致意外行为。

ES 消息中提供的信息反映的是某一时刻的快照。

系统继续同时处理多个线程，这些线程可能做改变系统状态的事，而你的 App 在有机会检查消息之前。

这意味着，在某些情况下，消息的部分可能与你自己查询该信息时有不同的值。

产品需要对时间检查时间使用问题保持谨慎。这与基于内核扩展的产品今天面临的问题没有不同。在深入 demo 之前，最后一点需要注意，EndpointSecurity 有几项运行时要求，程序必须满足才能成功建立 ES 事件流。

首先，App 必须有适当的 EndpointSecurity 授权。这是受限授权，你可以通过这里显示的链接请求 provisioning profile。

如果你的 App 作为系统扩展捆绑，安装扩展需要包含 App bundle 的额外授权。这可以在系统扩展文档中找到。

此外，系统扩展需要用户批准才能完成安装。

一旦扩展使用系统扩展 API 开始安装过程，用户必须从安全性与隐私偏好设置的通用面板批准安装。

接下来，为了提高用户隐私，我们要求你的 App 以完全磁盘访问权限的形式获得用户同意，它位于安全性与隐私偏好设置的隐私面板。

如果你作为系统扩展部署，在安装时，我们会在该对话框中预填充你的扩展，以便让用户更容易启用这些权限。

如果你的产品部署在受管理的设备上，有两个 MDM payload 可 aid 分发。第一，有 payload 定义扩展，将被自动允许安装而无需用户批准。第二，有隐私偏好 payload，可以自动启用完全磁盘访问权限。好的。现在让我们进入第一个 demo，我们将查看通知消息并扩展现有的 ES 扩展。

所以这里我们看的是 NOTIFY demo 的 main 函数，我们可以立刻看到这段代码看起来与我们几页前看到的示例代码非常相似。我们从 es_new_client 设置新的客户端事件流开始，这里的 handler block 只是调用我们的 handle_event 函数，我们稍后会看。接下来，我们设置订阅并调用 es_subscribe。现在我们有 NOTIFY_EXEC 和 NOTIFY_FORK 事件类型。

然后，一旦订阅到位，我们调用 dispatch_main，让程序继续执行并处理这些事件。所以让我们跳到 handle_event。

这里，你可以看到我们对 message event_type 使用 switch 语句，然后每个 case 只是记录消息到屏幕。所以这个扩展已经安装并运行并批准在系统上，让我们看看发生了什么。所以我们要先设置日志流，这里有一个 predicate 允许我们只关注我当前做的执行。接下来，我将使用 ps 工具作为例子。

所以现在，当我们执行 ps 时，我们看到两条消息。我们首先看到我们的 Z shell 正在 fork 一个新的子进程，然后从那个 forked 进程，它想执行新的可执行文件 /bin/ps。好的。现在让我们扩展这个 demo，添加 EXIT 事件以获得完整的进程生命周期信息。所以这里在我们的事件数组中，我们将把 ES_EVENT_TYPE_NOTIFY_EXIT 添加到我们的订阅列表中。

在 handle_event 函数中，我们需要添加这个新 case。

所以我要先添加 break 语句，以免我稍后忘记做，现在我们想记录这个信息。所以我将为 OS log 函数设置一些样板代码，对于格式字符串，让我们像上面那样添加发起进程信息，以及 pid。

然后接下来，我知道 EXIT 事件包含一些与退出状态相关的事件特定信息。所以让我们也获取它。

好的。所以现在，为了填充这个格式字符串的数据，我们首先需要查找发起进程，我们可以通过查看 message 结构的 process 成员来做到。

从那里，我们可以查看 executable，最后获取 path。

接下来，我们需要那个进程的 pid，对于进程，EndpointSecurity 提供审计 token 用于该信息，包括用户 ID 和进程 ID 等。所以你可以使用 lib BSM 函数 audit_token_to_pid 提取它。

所以，再一次，我们将深入 process 字段并拉出 audit token。

最后，我们想要 EXIT 事件的事件特定信息，也就是退出状态码。

所以为了做到，我们将查看 message 的 event 成员。从那里我们可以拉出 EXIT 事件，然后，最后，该状态码的 stat 字段。

好的。我们要构建这个扩展，现在需要安装它。快速说明我在这个系统上设置了系统扩展开发者模式，那只是让我们能更快部署测试扩展。

另一点需要注意的是，系统扩展要求包含 App bundle 位于 /Applications 才能安装扩展。所以我们要把这个刚构建的包含 App 拖到 /Applications。

然后，一旦在那里，我们可以运行那个 App 并最终安装扩展。所以这现在只是执行升级，新扩展现在在系统上运行并 live。所以，再一次，让我们使用 ps 工具作为例子。现在你可以看到我们得到第三条 exit 消息，包括状态码 zero，表示进程成功退出。作为快速例子，我们可以向 ps 传递无效标志，现在我们看到状态码是 256，表示进程可能有问题。

现在我们已经看到通知事件的实际运行，是时候谈谈 AUTH 事件了。EndpointSecurity 的一个主要功能是授权系统上的操作。AUTH 事件是同步的，这意味着在我们把消息排队给 ES 客户端后，操作在内核中被挂起，无法恢复，直到收到响应或 deadline 过期。

每个收到的 AUTH 消息在 message 结构中都有自己的 deadline 字段。你的 ES 客户端必须检查每条消息的这个值，并确保它执行的工作在 deadline 过期前完成。如果客户端未能在 deadline 前响应，App 将被终止。

如果你的 App 是系统扩展，我们为你提交的 launchd 作业将被自动重启。重要的是强调，每个单独的消息都有自己的 deadline，并不保证每条消息允许相同的响应时间。这些值可以并且会随时间变化。

当 deadline 错过时，implicit ALLOW 被应用为响应，但结果不会被缓存，允许未来操作被重新评估。

有两个 API 可用于响应 AUTH 事件。大多数事件类型需要简单的 ALLOW 或 DENY 响应，使用 es_respond_auth_result API。

第二个响应 API，es_respond_flags_result，用于事件有一系列可被允许或拒绝的选项时，比如能够允许文件以只读权限打开而不是读写。

你应该查看文档以知道每个事件类型使用哪个 API，然而到今天，只有 AUTH OPEN 事件使用 flags result API。

如果系统上有多个客户端订阅相同的 AUTH 事件，所有客户端的响应通过应用最严格的响应来组合，所以如果你有四个客户端对事件响应 ALLOW 但一个想要 DENY，总体结果是拒绝操作。

同样对于 flags 响应，只有所有客户端设置的 flags 子集将被允许。

你也应该知道 ES 不发送内省 AUTH 事件，因为这会导致 trivial deadlocks。事件将被隐式允许。然而，我们会对你的进程触发的事件发送 NOTIFY 消息。

使用 flags result API 的一个快速 caveat 是，你的 ES 客户端进程应该响应它可能 ever 允许操作的所有 flags，而不只是单个事件请求的 flags。这与缓存有关，我们稍后会更详细讨论。通过 muting，ES 客户端能够防止从可能对 App 不感兴趣的进程接收消息。主要有两种方式。

首先，使用 es_mute_process，ES App 提供一个唯一标识进程的 audit token。通常，客户端从之前的 message 获得 audit token。EndpointSecurity 子系统会自动跟踪进程退出并把它们从客户端的 muted 进程集中移除。除非客户端想再次开始从先前 muted 的进程接收消息，否则不需要手动使用相应的 es_unmute_process API。

ES 也支持按路径字面量 muting，也就是完整路径，使用 es_mute_path_literal，以及路径前缀，使用 es_mute_path_prefix。

顾名思义，这种机制将防止来自匹配提供路径的 instigating 进程的消息。我们建议 ES 客户端对最后这两个 API 谨慎使用。虽然我们使用具有快速查找操作的数据结构，但添加大量路径可能对性能有不利影响。按进程 audit token muting 通常是在更少开销下 mute 事件的更好方式。

许多 AUTH 事件可以缓存 ES 客户端响应的组合结果，这存储在一个所有 ES 客户端共享的单个全局缓存中。

EndpointSecurity 使用的缓存策略是 best effort，条目可能随时过期。EndpointSecurity 跟踪若干操作，并会自动使缓存条目失效，例如如果文件被写入、截断、删除以及更多。

虽然我们不保证响应会被缓存，如果 ES 客户端在响应 API 中把 cache 标志设为 false，ES 保证不会缓存该结果，即使另一个客户端请求缓存。

ES 客户端可能想要拒绝缓存的一些原因可能是对于 EXEC 事件，当可执行文件非常依赖可执行参数或环境变量时，比如解释器，你可能想检查解释器将执行的脚本。

ES App 能够使用 es_clear_cache API 清除整个缓存，然而我们不支持使单个缓存条目失效。

还要注意，当新客户端连接或现有客户端断开时，ES 会自动清除缓存。这允许在剩余客户端可能响应与先前组合缓存结果不同的各种场景。

几页前我提到了使用 es_respond_flags_result API 的一个重要 caveat。

虽然乍听起来可能不直观，响应必须包含 ES 客户端可能 ever 允许操作的所有 flags。这是因为 flags 响应的缓存与 AUTH 响应一样工作。

当未来事件发生时，先查询缓存。如果存在缓存条目，该条目的 flags 与新操作请求的 flags 比较，结果被应用而不会生成 AUTH 消息。

所以考虑进程以只读 flags 打开文件的情况，假设被打开的文件对你的 App 不是关注的。也就是说，你的 App 想允许该进程以它需要的任何方式操作文件。当你的 ES 客户端进程响应 flags 结果时，它应该设置所有适当的 flags，包括 WRITE flag，即使这个特定事件没有请求它。因为如果你没有设置 WRITE flag 会怎样？好吧，如果进程将来以写方式打开同一文件，并且缓存结果仍然存在，操作将被自动拒绝而不会生成 AUTH 消息，即使那不是你的产品意图。现在我们已经过完这两个，让我们快速比较 AUTH 和 NOTIFY 事件类型。

NOTIFY 事件总是异步的。我们把消息排队给客户端，但操作立即继续，可能在 ES 客户端有机会看到消息之前就完成。

AUTH 事件，如前所述，是同步的，操作被挂起直到收到响应。

关于交付，NOTIFY 消息总是被交付。然而，AUTH 消息只有在没有缓存结果且消息不是被交付给触发事件的同一进程时才被交付。

如果 instigating 进程被 muted，AUTH 和 NOTIFY 消息都不会被交付。

最后，两者之间在消息结构上略有不同。NOTIFY 消息包含由 EndpointSecurity 应用的结果。也就是说，对应 AUTH 消息的 ALLOW 或 DENY 结果。如果没有 ES 客户端订阅 AUTH 变体，或事件没有 AUTH 变体，结果隐式允许。

对于 AUTH 消息，显然还没有结果信息。然而，消息将有一个 deadline 值，并且需要 ES 客户端进程的响应。现在，让我们再做另一个 demo，这次查看 AUTH 事件类型，看看我们如何编写客户端来处理和响应这些消息。所以，再一次，我们看的是这里的 main 函数。你会立刻注意到它看起来与我们之前的 demo 设置非常相似。一个轻微的差异，我们将在异步 dispatch 队列上执行一些异步工作。所以我们要先设置那个队列。但之后，我们将用 es_new_client 初始化我们的新客户端事件流。我们的 handler block 将再次调用 handle_event 函数。

这个 demo 中，我们将查看 AUTH_EXEC 和 AUTH_OPEN 事件类型。订阅后，我们再一次调用 dispatch_main，让程序继续执行并处理这些事件。

所以，让我们看看 handle_event 函数。

再一次，我们看到 switch 语句，我们为每个单独的事件类型调用适当的 handle 函数。让我们从 EXEC 开始。

首先要注意的是，我们对所有 EXEC 调用 es_respond_auth_result 与 ES_AUTH_RESULT_ALLOW。但我们给自己留了一个 TODO，拒绝匹配 signing ID 的新 EXEC。现在，我们通常期望大多数产品想要更严格的策略，比如匹配 CD hashes，但为了演示目的，这样更清楚地看到我们试图阻止什么。所以，我们如何做？好吧，一种方式，我们可以对将要执行的新进程做简单的字符串比较，然后把 signing ID 与我们想要阻止的那个比较。

所以，因为我们正在查看事件特定数据，我们将深入 event union。从那里，我们可以查看 target process 并拉出 signing_id 数据。

所以，现在我们将把它与 signing_id_to_block 比较，如果它们相等，我们想要拒绝它。所以我们可以用 es_respond_auth_result API 做到。我们需要传递我们的 client 和 message 参数。接下来我们需要，定义我们的 result，它简单地是 AUTH_RESULT_DENY。

允许これを被缓存。为了完成这个，我们将把之前现有的响应放在这里的 else 语句中。所以，现在，如果我们的新可执行文件匹配我们想要阻止的 signing ID，我们将响应 "deny" 结果，其他一切将被允许。

所以现在让我们看看 open case。

所以在 handle_open 中，这可能看起来不那么熟悉，有一些概念我们需要介绍，我们还没谈到。建议你的 ES 客户端在它们的事件处理 block 中做尽可能少的工作。这通常意味着你不应该执行大量 I/O 或 CPU 密集型任务。这里的目标是你的事件处理 block 应该尽可能快，以便它们可以返回并继续 dequeuing 消息，以保持消息队列大小小，这将有助于防止丢弃消息。

所以在这个函数中，你可以看到我们用 es_copy_message API 复制我们的 message，并且我们稍后会更详细讨论。

在我们复制 message 后，我们异步调用 handle_open_worker 函数，然后一旦完成，我们再释放那个复制的 message。

所以，我们的 worker 函数做什么？我们有三个我们关心的 cases。我们的第一个 case 是 EICAR 文件测试，对于不熟悉的人，EICAR 文件是反病毒产品通常用来测试它们的操作而无需在系统上引入真实恶意代码的测试文件。

所以，这个函数做什么对于这个 demo 目的不重要。只需知道它需要打开并检查文件内容，并且这是为什么我们异步做这个工作的主要驱动。所以，假设这是 EICAR 文件，我们将使用 es_respond_flags_result API。你可以看到我们定义了 mask 为 zero。这基本上清除所有 bits 并将拒绝该文件的所有 open 操作。

接下来，你可以看到我们给自己留了一个 TODO。

所以，这里发生了什么？在这个 if 语句中，你可以看到我们正在检查 open 事件特定数据中被打开的文件，并把它与这里定义为 /usr/local/bin 的 read only prefix 比较。所以我们要防止任何人操作这些目录中的文件。

所以，为了做到，我们可以再次使用 es_respond_flags_result API。

我们也将传递我们的 client 和 message 参数。现在我们需要定义 flags。我们知道这里我们只想拒绝 write 操作。所以我们可以定义 mask 首先设置所有 bits 然后使用一些 bitwise 操作清除 right flag。

一点需要注意，你可能注意到 EndpointSecurity 为 open 事件提供的 flags 是 kernel versions of flags，不是你可能从 open 系统调用熟悉的 oflags。这在 open 事件中被记录，你应该检查它。

最后，我们将允许これを被缓存。然后这里的最终 case 已经写好，对于所有其他 open 操作，我们这里的 mask 设置所有 bits 并允许所有这些 open 操作成功继续。

所以，让我们 recap 我们做了什么。

所以，程序意图做的三件事首先是拒绝 text edit App 打开。我们还没安装扩展，所以现在我们可以看到所有这些工作。所以 text edit 可以成功打开。

我们也想拒绝在 usr/local/bin 中的文件写入。

所以，作为例子，我们设置了一个脚本 hi.sh，它简单地向屏幕打印 "hi"。

为了看到它运行，我们可以执行它。它完全按你期望的那样做。最后，在我的 home 目录中，我有一个 EICAR 文件。所以我们将在这里打印它，我们可以看到标准的 EICAR 测试文件定义。

好的，所以现在让我们过去，构建我们的扩展。

我们再一次需要安装系统扩展，所以我们要把它拖到 /Applications。

现在我们将启动包含 App bundle 并安装那个新扩展，现在我们的 AUTH demo 现在 live 并运行。所以，我们可以首先尝试现在打开 text edit App。我们可以看到图标弹跳，但什么也无法启动了。

接下来我们想尝试修改 usr/local/bin 中的文件。所以，这里你可以看到我试图修改 hi 脚本的内容以说 "Bye" 而不是。然而，这现在不再被允许。但你可以看到这个文件仍然允许以只读目的打开，并且脚本仍然能够执行。

最后我们有我们想防止所有操作的 EICAR 文件。所以我们可以看到甚至尝试读取那个文件也不再被允许。在看到写 ES 客户端处理 AUTH 事件有多么容易后，让我们深入一些更高级的主题。消息结构包含一个 version 字段，将允许你的基于 ES 的 App 在不同操作系统发布之间保持兼容。

新字段可以随时间添加到各种 EndpointSecurity 结构中，允许我们为你的 ES 客户端提供额外信息。版本号是单个整数值，一个 OS 发布中的所有消息共享相同的版本号。

如果 OS 发布以可能影响兼容性的方式修改了结构，版本号将被增加。使用新字段的客户端必须首先检查消息版本以确保该字段可用。失败这样做将导致 undefined behavior。请密切注意 ES 结构的 header docs，因为它们指示新字段在哪一版本添加。

作为快速例子，让我们看看 create 事件的 acl 字段。这个字段在初始发布中不存在，当它被添加时，我们把消息版本 bump 到 2。在这个小例子中，我们有 handle_notify_create 函数，它操作 NOTIFY_CREATE 事件。

我们看到，在访问 acl 成员之前，函数首先检查消息版本是否 greater than or equal to two。

所谓的 early boot 功能是 EndpointSecurity 的强大机制。作为提醒，这个功能只对作为系统扩展的基于 ES 的产品可用，不对独立 ES App 可用。扩展通过在 extensions input/out plist 中设置 NSEndpointSecurityEarlyBoot key 来 opt into 这个功能。当系统启动时有注册的 early boot 客户端时，系统仍然正常 come up。然而，直到所有 early boot 扩展 ready，没有额外的第三方 App 将被允许执行。为了 signal readiness，你的扩展需要至少调用一次 es_subscribe API。

一旦所有 early boot 客户端做了它们的第一个订阅，第三方 App 最终被允许执行。这意味着你的客户端应该准备好在单个 es_subscribe 调用中订阅所有必要事件。

如果你把事件拆分到多个调用中，第三方 App 可能在额外订阅到位之前开始执行，你的客户端可能错过事件。

还重要的是要注意，EndpointSecurity 子系统强制一个 deadline，所有 early boot 客户端必须在那时 signal readiness。一旦 deadline 过期，所有第三方执行自动被允许继续。

你的扩展应该小心不要在订阅之前执行长初始化步骤，以防止错过事件。

我们不认为 deadline 值是 API，并且 subject to change over time，但我们相信该值适合你的产品 come up 并 become ready，而不会对终端用户有大影响。

那些已经与 EndpointSecurity 框架工作过的人可能已经注意到，我们不提供与网络操作相关的事件。这是有意的，因为这些由 NetworkExtension 框架更好地覆盖。

关于 UNIX 域套接字有一个小 exception，ES 确实为这些提供事件。

你也应该知道，可以从单个 combined 系统扩展中同时使用 EndpointSecurity 和 NetworkExtension 框架。对于这些产品，你应该像通常那样使用系统扩展 API 和安装流程，用于 single extension type 的扩展。

此外，把特定于 network extensions 或 EndpointSecurity extensions 的 keys 组合在你的扩展的 info.plist 中是安全的，系统会负责适当地应用这些值。

ES 按它们在系统上发生的顺序向客户端提供消息。例如，如果客户端订阅了 FORK 和 EXEC 事件，在常见场景中，当新进程 spawn 时，客户端的 handler block 将总是先接收 fork 事件，然后是 corresponding exec。

还要注意，消息排序适用于单个 ES 客户端的订阅。如果你的 App 创建多个 ES 客户端并在它们之间拆分订阅，事件的顺序仅相对于每个 ES 客户端的订阅进行排序。

如果需要，你可以使用 message struct 中包含的消息生成时间重构全局顺序。

消息一次一个地交付给 ES 客户端，只有当 ES 客户端的事件处理 block 从处理前一条消息返回时，消息才被交付。handler block 收到的 message 结构的生命周期仅保证在该消息的 handler block 调用期间有效。

一旦你从 block 返回，你不应该继续访问 message，因为这样做将导致 undefined behavior。

如果你需要 extend message 的生命周期，就像我们在 demo 中需要的那样，你可以使用 es_copy_message API 来做到。这将返回一个 message 的句柄，它将 live 直到 corresponding es_free_message API 被调用。

这个暗示的一个重要功能是，AUTH 事件不必在 handler block 返回前被回复。这也意味着 AUTH 事件不必按呈现给 ES 客户端的相同顺序响应。

对你的 App 来说，可能重要的是先 inspect 未来消息，以便对前一条消息做出决定。在这种情况下，ES App 可以先复制 message 并从 handler block 返回以开始 inspect additional messages，然后稍后用适当的响应回复那个复制的 message。

别忘了最后在不再需要时释放 message。如果你需要做一些异步消息处理，比如使用异步 dispatch 队列，确保你用适合你 App 的 quality-of-service class 初始化 dispatch 队列。

这将 likely 依赖于许多因素，比如你是否订阅了 AUTH 事件、预期事件量，或你希望消耗多少 CPU 或系统资源。

接下来，我们想分享一些我们认为将帮助你开发出色的基于 EndpointSecurity 的产品的各种 tips。

你可能在 message 结构中注意到的一个字段是 is_es_client Boolean 成员。ES App 不能授权自己的 actions，因为这些内省事件被自动允许。然而，系统上可能有多个 ES 客户端，并且 ES 客户端确实有能力授权其他 ES 客户端的 actions。对于 AUTH 和 NOTIFY 消息，如果 instigating 进程包含 EndpointSecurity 客户端授权，is_es_client 字段将被设为 "true"。

ES 客户端应该检查这个字段并采取适当行动，以确保它们不 inappropriate 地干扰这些客户端的 actions，或执行可能创建反馈循环的 actions。

Path muting 是 fantastic 的方式来防止你的客户端被消息 inundated。它还通过减少需要处理或授权的消息数量，帮助保持整体系统更 performant。例如，如果你的客户端不关心 Mac OS 上的 Spotlight 服务索引文件，muting 适当的索引进程可以大大减少某些事件类型接收的消息数量。

利用缓存的 App 应该知道，缓存应该仅用于 performance 目的，缓存永远不应该用于 policy。

这是因为，如前所述，缓存条目可能随时过期。例如，如果你的 App 决定拒绝一个进程打开任何文件，并允许响应被缓存，那么你随后就不应该 mute 该进程。考虑如果缓存条目后来 invalidated 或 otherwise removed 会发生什么。如果该进程尝试重新打开文件，因为你的 ES 客户端 muted 了该进程，将不会生成 AUTH 事件，这些 open 操作将被自动允许。

下一个 tip 是在调试你订阅了 AUTH 事件的 ES App 时要小心。没有办法 disable 或 otherwise extend 响应 deadline。如果 AUTH 事件在你的 App 命中 break point 时被排队，你仍然 required 在 deadline 前响应，否则你的进程将 per normal rules 被终止。

最后，EndpointSecurity 可能在消息队列满时丢弃消息而不交付给客户端。客户端可以通过检查 message 结构中的 sequence number 字段来 determine 是否发生了。这是 per-client 和 per-event-type 的 sequence number，所以你可以 determine 每种事件类型可能错过了多少。看到更高 drop rates 的客户端被鼓励利用更高级的 EndpointSecurity API 使用模式，如 muting、异步处理和跨多个 ES 客户端拆分订阅。

今年我们宣布审计子系统正在被废弃。这主要指与审计事件相关的功能，如写入审计追踪文件的事件，通常在 /var/audit 目录中，以及发送到 Auditpipe pseudo-device 的事件，供想要 live event stream 的 App 使用。这不适用于像 audit tokens 和 audit sessions 这样的东西，它们将继续是系统的核心部分。依赖审计事件的产品应该迁移到使用 EndpointSecurity 框架。那么 macOS Big Sur 有啥新内容？首先，EXEC 事件有一些新的 event-specific API。ES 现在提供新执行进程将开始的文件描述符和文件描述符类型列表。我们还提供 specifically for Pipe 文件描述符的 unique identifiers，将允许你跟踪多个进程可能如何通过 Pipe interprocess communication 机制通信。由于 performance 限制，并非所有文件描述符都可能被提供。主要 focus 是 standard in、standard out 和 standard err 描述符，但我们也提供几个 more if they exist，并且我们向客户端 expose 是否有 we may not have enumerated 的 additional descriptors。

关于 performance，我们认为 EndpointSecurity 框架的 early adopters 在 macOS Big Sur 中有很多期待。我们重写了许多 data structures 以减少 memory allocations 并 increase event throughput。我们 tuned caches 以 eliminate invalidation bottlenecks 并 improved overall memory performance。Combined，这些 enhancements 导致 better system performance 和 fewer drops。我们认为这将为你的 EndpointSecurity 产品提供 much better performance characteristics。

macOS Big Sur 中还添加了 several new event types。其中一些是 previously existing NOTIFY 事件的 additional AUTH variants，一些是 brand new。我想在这里 call out 一个 couple。首先，我们添加了 widely requested 的 trace 事件。这将在进程被调试时通知你的客户端。

第二，我们 excited to introduce CS_INVALIDATED 事件。正如许多 of you know，当一个 signed 进程执行时，内核不断 validation 它 page in 的 code matches 该 binary 的 individual page hashes。如果发现 mismatch，进程的 code signing flags 被 updated 以 clear CS_VALID bit。以前，ES 客户端必须 wait for future messages 并 inspect instigating 进程的 code signing flags 以 determine 它是否 went invalid。然而，通过这个事件，客户端可以得到 immediate notification。

一点需要注意，使用 hardened run-time features 的 binaries，比如那些设置了 CS_KILL code signing flag 的，如果遇到 hash mismatch，仍然会被系统 automatically terminated。

那么，你从这里去哪里？首先，你可以使用 top link shown 开始请求受限 EndpointSecurity 授权的过程。接下来，你可以开始 reviewing Apple developer website 上的 official EndpointSecurity 和 System Extension API 文档。我还想鼓励你仔细阅读 SDK 中的 EndpointSecurity header docs。我们添加了很多 comments 和 detail，可能不在 websites 上，我们认为 answers common questions 并将帮助你构建 great products。最后，我们将提供 largely based on today's demos 的 sample code，以帮助你开始使用 EndpointSecurity 框架。With that，感谢加入我们，我们期待看到你构建什么。享受 WWDC 2020。
