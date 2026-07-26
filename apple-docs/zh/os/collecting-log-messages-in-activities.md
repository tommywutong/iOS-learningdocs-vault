---
title: 在活动中收集日志消息
framework: os
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/collecting-log-messages-in-activities
source_url: 'https://developer.apple.com/documentation/os/collecting-log-messages-in-activities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/collecting-log-messages-in-activities.json'
content_hash: 'sha256:4bf88a46dc969c60'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md) · [Logging](logging.md)

# 在活动中收集日志消息

<sub>文章</sub>

查找与特定用户操作或应用程序事件相关的消息。

## 概述

详尽的日志记录能提供大量关于 App 内部运作的信息，但数量庞大的日志消息可能会让你很难找到某条特定数据。此外，当你尝试复现某个 bug 时，往往需要重新追溯用户的操作步骤，把用户执行的操作和 App 的行为关联起来。_活动_ 通过把日志消息和用户操作或其他由 App 定义的事件关联起来，帮你解决这两个问题。例如，当用户从菜单里选择某个操作，或者你的更新把数据同步到数据库时，你都可以创建一个活动。当一个活动处于活跃状态时，你记录的任何消息都会自动与该活动关联。你可以在 Console 里查看这些活动，并找到每个活动捕获到的消息。

活动以父子关系的层级结构组织。对于单个子系统分类里的小任务，你可以用一个活动来封装所有消息。对于会触发其他 App 活动的更大任务和事件，则用子活动来组织消息，类似于在一个日志子系统内拆分出不同分类的做法。例如，假设你创建了一个父活动来响应某个用户操作。在该活动内部，你可以创建一个子活动来捕获对模型数据执行更新时产生的日志消息，再创建另一个单独的子活动来捕获与用户界面更新相关的消息。

### 创建一个活动

创建活动最简单的方法是调用 [os_activity_initiate](os_activity_initiate.md)，指定活动的名称，以及一个包含应作为该活动一部分执行的代码的 block。系统会创建该活动，同步调用这个 block，然后释放该活动。默认情况下，如果当前存在活跃的活动，新活动会成为它的子活动。使用 flags 参数可以覆盖这种行为。

例如，下面的代码写在一个 `IBAction` 处理程序里，当用户与用户界面交互时，系统会调用它。这个方法被调用时，会创建一个活动来封装该方法所执行的工作。这个 block 记录一些关于该操作的信息，更新模型，最后更新用户界面。

```objc
- (IBAction)treeButtonTapped:(UIButton *)sender {
    os_activity_initiate("Chop down tree", OS_ACTIVITY_FLAG_DEFAULT, ^(void) {
    os_log_info(ui_log, "Cutting down trees to turn them into logs");
    os_log_debug(ui_log, "Sender: %@", sender);
    [self.company chopDownTree];
    [self updateButtonCounts];
    });
}
```

如果你需要在同一个活动中执行多个代码 block，或者想用自定义的父对象创建活动，调用 [os_activity_create](os_activity_create.md) 创建一个活动对象，然后调用 [os_activity_apply](os_activity_apply.md) 方法为该活动执行代码。和之前一样，用一个 block 来封装活动的代码。下面的代码和前一个代码清单行为相同，但使用了这些函数。

```objc
- (IBAction)truckButtonTapped:(NSButton *)sender {
    os_activity_t pulverizeLogs = os_activity_create("pulverize logs", OS_ACTIVITY_CURRENT, OS_ACTIVITY_FLAG_DEFAULT);
    os_activity_apply(pulverizeLogs, ^(void) {
        os_log_info(ui_log, "Taking logs to the paper mill");
        os_log_debug(ui_log, "Sender: %@", sender);
        [self.company makePaper];
        [self updateButtonCounts];
    });
}
```

最后，如果你无法用 block 封装代码，可以调用函数显式地设置和恢复当前活动。如下所示，你通过调用

[os_activity_scope_enter](os_activity_scope_enter.md) 来更改当前活动。这个函数会把之前的活动信息保存到你传入该函数的一个变量中。任务完成后，用同一个变量恢复之前的活动作用域。使用这种方式时，你必须确保在离开函数作用域之前，活动作用域始终能被恢复。

```objc
- (IBAction)paperButtonTapped:(NSButton *)sender {
    os_activity_t usePaper = os_activity_create("Use paper", OS_ACTIVITY_CURRENT, OS_ACTIVITY_FLAG_DEFAULT);
    struct os_activity_scope_state_s savedScope;

    os_activity_scope_enter(usePaper, &savedScope);
    os_log_debug(ui_log, "This message is in the usePaper scope");
    os_activity_scope_leave(&savedScope);

    os_log_debug(ui_log, "This message is in the restored scope, not usePaper.");
}
```
