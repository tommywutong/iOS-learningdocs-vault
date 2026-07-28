---
title: 在 Xcode 中使用 StoreKit 事务管理器测试 App 内购买项目
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/testing-in-app-purchases-with-storekit-transaction-manager-in-code
source_url: 'https://developer.apple.com/documentation/xcode/testing-in-app-purchases-with-storekit-transaction-manager-in-code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/testing-in-app-purchases-with-storekit-transaction-manager-in-code.json'
content_hash: 'sha256:bb01f8c0d15fb7bc'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [测试](testing.md)

# 在 Xcode 中使用 StoreKit 事务管理器测试 App 内购买项目

<sub>文章</sub>

使用 Xcode 中的事务管理器测试 App 内购买项目，无需连接 App Store 服务器。

## 概述

Xcode 提供了一个_事务管理器_，与 StoreKit Testing in Xcode 配合使用。借助事务管理器，你可以在开发的任何阶段测试 App 内购买项目。在将 App 推送到生产环境之前测试 App 内购买项目，有助于你确保购买流程顺畅无阻，测试各种边界情况和逻辑，并验证购买行为是否正确。

使用事务管理器更改设置和启动测试条件、检查事务以及模拟不同类型的购买。

> [!note] 注意
> 在使用事务管理器进行测试之前，你需要在 Xcode 中设置 StoreKit。有关更多信息，请参阅[在 Xcode 中设置 StoreKit 测试](setting-up-storekit-testing-in-xcode.md)。

### 更改设置和启动测试条件

在项目导航器中选择你的 StoreKit 配置文件，然后选取“Editor”（编辑器）来更改以下设置：

- **Default Storefront（默认店面）** — 设置事务的 [storefront](../storekit/transaction/storefront.md) 属性。
- **Default Localization（默认本地化）** — 设置本地化，这会影响付款表单（payment sheet）中的货币显示，以及 [Product](../storekit/product.md) 的本地化属性返回的值。你可以在 StoreKit 配置文件中提供本地化数据。
- **Subscription Renewal Rate（订阅续订速率）** — 更改测试环境中订阅时间流逝速度相对于真实时间的比率。
- **Enable Interrupted Purchases（启用中断的购买）** — 使测试环境模拟阻止顾客完成购买的条件。导致购买中断的情况包括支付卡过期或顾客需要批准更新后的条款与条件。选取“Debug”（调试）>“StoreKit”>“Manage Transactions”（管理事务）中的“Resolve Issue”（解决问题）选项，以模拟顾客解决问题。
- **Enable Billing Retry on Renewal（启用续订计费重试）** — 使测试环境模拟顾客对续订的付款未成功且订阅进入计费重试状态的情况。选取“Debug”（调试）>“StoreKit”>“Manage Transactions”（管理事务）中的“Resolve Issue”（解决问题）选项，以模拟计费重试成功。
- **Enable Billing Grace Period（启用计费宽限期）** — 在 Xcode 测试环境中为你的 App 启用计费宽限期。要测试此条件，请设置“Enable Billing Retry on Renewal”（启用续订计费重试）。当订阅续订失败时，它会进入已启用计费宽限期的计费重试状态。
- **Enable Ask to Buy（启用“询问购买”）** — 使测试环境在测试者尝试购买时显示“询问购买”提示。选取“Debug”（调试）>“StoreKit”>“Manage Transactions”（管理事务）菜单中的“Approve Transaction”（批准交易）或“Decline Transaction”（拒绝交易）选项来解决该事务。
- **Enable Dialogs（启用对话框）** — 关闭此选项可加快测试速度。关闭此选项后，系统会假设用户已确认付款，并在测试期间抑制确认动画和交互。开启此选项可在测试期间显示所有付款对话框。
- **Subscription Offers Key（订阅优惠密钥）** — 提供用于在测试环境中签署订阅优惠的密钥。请使用此密钥代替你的常规密钥在服务器上生成签名。有关更多信息，请参阅[为促销优惠生成签名](../storekit/generating-a-signature-for-promotional-offers.md)。
- **Simulate StoreKit failures（模拟 StoreKit 失败）** — 使测试环境应用你指定的错误条件，以便你测试 App 的错误处理。

![](../../../attachments/92929c16bb06f5eb8416c9742796684e/storekit-testing-editor@2x.png)

<sub>Xcode 中的屏幕截图，显示了在 Xcode 的项目导航器中选中的 StoreKit 配置文件。侧边栏显示了选中的“Configuration Settings”（配置设置）选项，主内容区域列出了各种要测试的测试条件。</sub>

### 使用事务管理器检查事务

使用事务管理器中的选项来执行 App 内购买流程中通常发生在你的 App 之外的步骤，例如批准或拒绝“询问购买”事务、接收退款等。要打开事务管理器，请选取“Debug”（调试）>“StoreKit”>“Manage Transactions”（管理事务）。

![](../../../attachments/673ddf4dd4cb710f43467eebcc476ec3/storekit-testing-transaction-manager.png)

<sub>StoreKit 事务管理器的屏幕截图，列出了 App 事务。窗口左侧列出了设备和模拟器及其各自安装的 App。主内容区域列出了事务。每个事务都有标题、时间戳和简短的产品描述。</sub>

事务管理器列出了正在运行的 App 的所有事务。如果你在多个设备上运行多个 App，请在侧边栏中选择 App 以查看其事务。使用事务管理器可以执行以下操作：

- **Filter transactions（过滤事务）** — 在对话框底部的过滤框中输入搜索词，以缩减显示的事务数量。
- **Inspect a transaction（检查事务）** — 点击某个事务，然后在检查器中查看该事务的详细信息。点击产品或组旁边的跳转按钮，即可在 Xcode 的 StoreKit 配置文件中导航到该产品或组。
- **Create a transaction（创建事务）** — 点击过滤栏左侧的加号按钮。选择要为其创建事务的产品，然后配置该事务。使用此功能可以测试在设备外进行的 App 内购买项目，并模拟顾客在不同设备上完成的 App 内购买项目。有关创建事务的更多信息，请参阅[模拟购买](#Simulate-a-purchase)。
- **Delete a transaction（删除事务）** — 选择一个事务，然后点击“Delete”（删除），以重新测试顾客只能执行一次的场景。例如，顾客只能购买一次非消耗型产品，因此删除该事务可以重新测试该购买。删除订阅事务可以重新测试推介优惠（introductory offer）。有关更多信息，请参阅[在 App 中实现推介优惠](../storekit/implementing-introductory-offers-in-your-app.md)。如果你的 App 使用[用于 App 内购买项目的原始 API](https://developer.apple.com/documentation/storekit/in-app_purchase/original_api_for_in-app_purchase)，请刷新收据以获取不包含已删除事务的更新后收据。
- **Send a purchase intent（发送购买意图）** — 模拟向你的 App 发送购买意图，以确保你的 App 能正确处理它们。有关在 App 中接收和处理购买意图的更多信息，请参阅 [PurchaseIntent](../storekit/purchaseintent.md)。有关在测试环境中发送购买意图的更多信息，请参阅[发送购买意图](#Send-a-purchase-intent)。
- **Approve or decline a transaction（批准或拒绝事务）** — 点击“Approve”（批准）或“Decline”（拒绝）来解决正在测试“询问购买”场景的待处理事务。
- **Refund a transaction（退款事务）** — 点击“Refund”（退款）来模拟顾客收到退款。
- **Resolve a transaction（解决事务）** — 点击“Resolve”（解决）来模拟顾客解决中断的购买。要模拟中断，请选取“Editor”（编辑器）>“Enable Interrupted Purchases”（启用中断的购买）。
- **Test a price increase（测试价格上调）** — 选择一个订阅事务，然后点击工具栏中的“Request Price Increase Consent”（请求价格上调同意）按钮。使用系统在你的 App 中显示的价格上调表单进行测试，或使用这些按钮模拟顾客从 App 外部（例如推送通知）的响应。点击“Approve”（批准）按钮表示顾客接受价格上调。点击“Decline”（拒绝）按钮模拟顾客取消订阅。

测试环境会自动同步你所做的事务更改。你无需重新构建和运行你的 App。

### 模拟购买

StoreKit 配置文件允许你在两个部分中定义 App 内购买项目。使用“Products”（产品）部分来定义消耗型和非消耗型 App 内购买项目。使用“Subscriptions”（订阅）部分来定义自动续期订阅和非续期订阅。

要进行一次性 App 内购买，请从左侧选择要测试的 App，然后点击过滤栏左侧的加号按钮。在显示的产品屏幕中，选择你想要购买的产品，然后点击“Next”（下一步）。

![](../../../attachments/94aab1121d536b5d8962c4600429cb1e/storekit-testing-product-selection.png)

<sub>给定 App 的 StoreKit 产品屏幕截图。窗口顶部显示一个空的搜索框。主内容区域列出了产品，其中一个产品被选中。底部部分显示可以进行的各种购买类型（默认选中“Purchase”（购买）产品）。底部行列出了三个按钮：“Cancel”（取消）、“Previous”（上一步）和“Next”（下一步）。“Next”（下一步）按钮处于活动状态并已启用。</sub>

在显示的配置弹出窗口中，你可以接受默认值，也可以更改属性以反映你想要的购买。配置完 App 内购买项目后，点击“Done”（完成）按钮。

![](../../../attachments/c85d285e177e5156b2ee702348bd36c0/storekit-testing-product-configuration.png)

<sub>产品购买配置弹出窗口的屏幕截图，从上到下显示了一列配置选项。“Quantity”（数量）选项输入的值为 1。“Purchase Date”（购买日期）文本字段包含日期和时间。“App Account Token”（App 账户令牌）文本字段为空。底部行列出了三个按钮：“Cancel”（取消）、“Previous”（上一步）和“Done”（完成）。“Done”（完成）按钮处于活动状态并已启用。</sub>

如果你的设备或模拟器未运行，则事务会以未完成状态显示在事务管理器屏幕顶部的新项目中。未完成的事务旁边会显示警告符号。要完成该事务，请在设备或模拟器上运行你的 App。然后你可以测试你的 App 是否成功完成了该事务。

要创建测试订阅购买，请返回事务管理器主屏幕，再次点击加号按钮，但这次从产品列表中选择一个自动续期订阅，然后点击“Next”（下一步）。

![](../../../attachments/305ee837dd7c3f1f553553fc2dc9ad41/storekit-testing-filter-products.png)

<sub>StoreKit 事务管理器产品弹出窗口的屏幕截图，其中选中了一个过滤后的订阅产品。右上角的过滤文本字段包含文本 pass。中心内容区域显示了一个过滤后的产品列表，其中一个订阅产品被选中。靠近底部是一行，列出了不同类型的 App 内购买项目作为单选按钮选项。默认选中了“Purchase”（购买）。底部行列出了三个按钮：“Cancel”（取消）、“Previous”（上一步）和“Next”（下一步）。“Next”（下一步）按钮处于活动状态并已启用。</sub>

当订阅配置弹出窗口出现时，接受默认值，或更改属性以反映你想要的订阅类型。例如，如果你的订阅有多种优惠类型，你可以选择从优惠下拉菜单中选择一个优惠代码。要测试不同的续订选项，请选择“Automatically Renew”（自动续订）以测试默认情况下在生产环境中的续订行为，或选择“Don’t Renew”（不续订），这将创建一次购买，然后取消订阅。点击“Done”（完成）以触发订阅购买。

![](../../../attachments/90a576afe5fe761f9697a49dcd89f518/storekit-testing-subscription-configuration.png)

<sub>显示订阅产品配置选项的屏幕截图。第一个选项显示可以从菜单中选择的优惠。未选择任何优惠。其下方是一个“Purchase Date”（购买日期）文本字段，包含日期和时间。“Renewal Options”（续订选项）部分显示两个单选按钮选项：“Automatically Renew”（自动续订）和“Don’t Renew”（不续订）。选中了“Automatically Renew”（自动续订）单选按钮。接下来是一个空的“App Account Token”（App 账户令牌）文本字段。底部行列出了三个按钮：“Cancel”（取消）、“Previous”（上一步）和“Done”（完成）。</sub>

要完成测试购买，请在发生购买的设备或模拟器上启动 App，然后查看事务管理器中的购买是否完成，以及购买是否显示在 App 中。

### 发送购买意图

进行 App 内购买并非人们为你的 App 或游戏购买内容的唯一方式。作为开发者，你可以从 App Store 推广 App 内购买项目。当顾客在 App Store 中看到某个 App 内购买项目时，他们可以发起购买。然后，App Store 会将该购买意图发送到顾客的设备上。当顾客打开他们的设备时，他们会完成购买。

> [!note] 注意
> 要发送购买意图，你的 App 需要实现 [PurchaseIntent](https://developer.apple.com/documentation/storekit/purchaseintent) API。

这种从 App Store 将购买发送到你的 App 的行为称为购买意图。你可以按如下方式在事务管理器中测试此交互：

1. 点击加号以创建新的购买。
2. 选择要为其发送购买意图的产品。
3. 将产品列表下方的购买类型更改为“Purchase Intent”（购买意图）。
4. 点击“Done”（完成）并检查你的设备以继续。

![](../../../attachments/99d415bbf9df27f59f2bdaeb03e22a71/storekit-testing-send-purchase-intent.png)

<sub>StoreKit 事务管理器产品（类型为“Purchase Intent”（购买意图））的屏幕截图。中间内容区域显示了一个选中的产品，其中产品类型单选按钮选中了“Purchase Intent”（购买意图）。靠近底部是一行，列出了不同类型的 App 内购买项目作为单选按钮选项。底部行列出了三个按钮：“Cancel”（取消）、“Previous”（上一步）和“Done”（完成）。“Done”（完成）按钮处于活动状态并已启用。</sub>

一旦顾客在其设备上确认购买，购买即完成。之后，事务会显示出来。

## 另请参阅

### StoreKit

- [在 Xcode 中设置 StoreKit 测试](setting-up-storekit-testing-in-xcode.md) — 准备你的测试环境，以使用本地配置的数据测试 App 内购买项目。
